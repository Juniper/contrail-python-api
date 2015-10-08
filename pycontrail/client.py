#
# Copyright (c) 2015 Juniper Networks, Inc. All rights reserved.
#
import sys
import time
import logging
from pprint import pformat
import platform
import functools
import __main__ as main

import json
import requests
from requests.exceptions import ConnectionError

import pycontrail.gen.resource_common
import pycontrail.gen.vnc_api_client_gen
import exceptions

logger = logging.getLogger(__name__)

def CamelCase(input):
    words = input.replace('_', '-').split('-')
    name = ''
    for w in words:
        name += w.capitalize()
    return name

def str_to_class(class_name):
    return getattr(sys.modules['pycontrail.gen.resource_client'], class_name)

def obj_type_to_class(obj_type):
    try:
        return str_to_class(CamelCase(obj_type.replace('-', '_')))
    except AttributeError:
        return None

class ActionUrlDict(dict):
    """Action url dictionary with operator([]) overloading to parse home page
       and populate the action_url, if not populated already.
    """
    def __init__(self, client,  *args, **kwargs):
        dict.__init__(self, args, **kwargs)
        self.client = client

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            homepage = self.client._request(rest.OP_GET,
                self.client._base_url, retry_on_error=False)
            self.client._root_url = self.client._parse_homepage(homepage)
            return dict.__getitem__(self, key)


class Client(object):

    hostname = platform.node()
    _DEFAULT_HEADERS = {
        'Content-type': 'application/json; charset="UTF-8"',
        'X-Contrail-Useragent': '%s:%s'
             %(hostname, getattr(main, '__file__', '')),
    }

    # The number of items beyond which instead of GET /<collection>
    # a POST /list-bulk-collection is issued
    POST_FOR_LIST_THRESHOLD = 25

    N_POOL_CONNS = 100
    POOL_MAXSIZE = 100

    def __init__(self, url='http://localhost:8082/',
                 blocking=True, headers=None, auth_params=None):
        self.api_url = url
        self._auth_params = auth_params
        self._headers = headers or Client._DEFAULT_HEADERS

        self._obj_serializer = self._obj_serializer_diff
        if hasattr(pycontrail.gen.vnc_api_client_gen, 'all_resource_types'):
            all_resource_types = pycontrail.gen.all_resource_types
        else:
            # <=2.20
            obj_types = \
            pycontrail.gen.vnc_api_client_gen.VncApiClientGen(None)._type_to_class.keys()
            all_resource_types = [x.replace('_', '-') for x in obj_types]

        for resource_type in all_resource_types:
            obj_type = resource_type.replace('-', '_')
            for oper_str in ('_create', '_read', '_update', '_delete',
                         's_list', '_get_default_id'):
                method = getattr(self, '_object%s' %(oper_str))
                bound_method = functools.partial(method, resource_type)
                functools.update_wrapper(bound_method, method)
                setattr(self, '%s%s' %(obj_type, oper_str),
                    bound_method)

        # Type-independent actions offered by server
        self._action_url = ActionUrlDict(self)

        self._create_api_server_session()

        homepage = self._request('GET', self.api_url,
                                 blocking=blocking)
        self._cfg_root_url = self._parse_homepage(homepage)

    def _parse_homepage(self, json_body):
        py_obj = json.loads(json_body)

        srv_root_url = py_obj['href']
        self._srv_root_url = srv_root_url

        for link in py_obj['links']:
            url = link['link']['href']
            if link['link']['rel'] == 'collection':
                cls = obj_type_to_class(link['link']['name'])
                if not cls:
                    continue
                cls.create_url = url
            elif link['link']['rel'] == 'resource-base':
                cls = obj_type_to_class(link['link']['name'])
                if not cls:
                    continue
                resource_type = link['link']['name']
                cls.resource_url_base = url
            elif link['link']['rel'] == 'action':
                act_type = link['link']['name']
                self._action_url[act_type] = url

    def _find_url(self, json_body, resource_name):
        rname = unicode(resource_name)
        py_obj = json.loads(json_body)
        pprint.pprint(py_obj)
        for link in py_obj['links']:
            if link['link']['name'] == rname:
                return link['link']['href']

        return None

    def _create_api_server_session(self):
        self._api_server_session = requests.Session()

        adapter = requests.adapters.HTTPAdapter(
            pool_connections=Client.N_POOL_CONNS,
            pool_maxsize=Client.POOL_MAXSIZE)
        self._api_server_session.mount("http://", adapter)
        self._api_server_session.mount("https://", adapter)

    def _authenticate(self, response=None, headers=None):
        new_headers = headers or {}
        try:
            response = requests.post(
                self._auth_params['auth_url']+'/tokens',
                data=self._generate_auth_body(),
                headers=self._DEFAULT_HEADERS)
        except Exception as e:
            raise RuntimeError('Unable to connect to keystone for authentication. Verify keystone server details')

        if (response.status_code == 200) or (response.status_code == 201):
            # plan is to re-issue original request with new token
            if 'v2' in self._auth_params['auth_url']:
                auth_content = json.loads(response.text)
                auth_token = auth_content['access']['token']['id']
            else:
                auth_token = response.headers['x-subject-token']
            new_headers['X-AUTH-TOKEN'] = auth_token
            return new_headers
        else:
            raise RuntimeError('Authentication Failure')

    def _http_get(self, url, headers=None, query_params=None):
        logger.debug('GET Request %s %s %s',
            pformat(url), pformat(headers), pformat(query_params))
        response = None
        response = self._api_server_session.get(url, headers=headers,
                                                params=query_params)
        logger.debug('GET Response %s %s',
            pformat(response.status_code), pformat(response.text))
        return (response.status_code, response.text)

    def _http_post(self, url, body, headers):
        logger.debug('POST Request %s %s %s',
            pformat(url), pformat(headers), pformat(body))
        response = self._api_server_session.post(url, data=body,
                                                 headers=headers)
        logger.debug('POST Response %s %s',
            pformat(response.status_code), pformat(response.text))
        return (response.status_code, response.text)

    def _http_delete(self, url, body, headers):
        logger.debug('DELETE Request %s %s',
            pformat(url), pformat(headers))
        response = self._api_server_session.delete(url, data=body,
                                                   headers=headers)
        logger.debug('DELETE Response %s %s',
            pformat(response.status_code), pformat(response.text))
        return (response.status_code, response.text)

    def _http_put(self, url, body, headers):
        logger.debug('PUT Request %s %s %s',
            pformat(url), pformat(headers), pformat(body))
        response = self._api_server_session.put(url, data=body,
                                                headers=headers)
        logger.debug('PUT Response %s %s',
            pformat(response.status_code), pformat(response.text))
        return (response.status_code, response.text)

    def _request(self, op, url, data=None, blocking=True, retry_after_auth=False):
        retried = 0
        while True:
            try:
                if (op.upper() == 'GET'):
                    (status, content) = self._http_get(url, headers=self._headers,
                                                       query_params=data)
                elif (op.upper() == 'POST'):
                    (status, content) = self._http_post(url, body=data,
                                                        headers=self._headers)
                elif (op.upper() == 'DELETE'):
                    (status, content) = self._http_delete(url, body=data,
                                                          headers=self._headers)
                elif (op.upper() == 'PUT'):
                    (status, content) = self._http_put(url, body=data,
                                                       headers=self._headers)
                else:
                    raise ValueError
            except ConnectionError as e:
                if not blocking:
                    raise
     
                retried += 1
                time.sleep(1)
                self._create_api_server_session()
                continue
     
            if status == 200:
                return content
     
            # Exception Response, see if it can be resolved
            if status == 401:
                if retry_after_auth:
                    raise exceptions.AuthenticationFailed(content)
                else:
                    self._headers = self._authenticate(content, self._headers)
                    # Recursive call after authentication (max 1 level)
                    content = self._request(op, url, data=data, retry_after_auth=True)
                return content
            elif status == 404:
                raise exceptions.NoIdError('Error: oper %s url %s body %s response %s'
                                % (op, url, data, content))
            elif status == 403:
                raise exceptions.PermissionDenied(content)
            elif status == 409:
                raise exceptions.RefsExistError(content)
            elif status == 504:
                # Request sent to API server, but no response came within lb timeout
                raise exceptions.TimeOutError('Gateway Timeout 504')
            elif status in [502, 503]:
                # 502: API server died after accepting request, so retry
                # 503: no API server available even before sending the request
                if not blocking:
                    raise exceptions.ServiceUnavailableError('Service Unavailable Timeout %d' % status)

                retried += 1
                time.sleep(1)
                continue
            elif status == 400:
                raise exceptions.BadRequest(status, content)
            else:  # Unknown Error
                raise exceptions.HttpError(status, content)
        # end while True

    def _read_args_to_id(self, obj_type, fq_name=None, fq_name_str=None,
                         id=None):
        arg_count = ((fq_name is not None) + (fq_name_str is not None) +
                     (id is not None))

        if (arg_count == 0):
            return (False, "at least one of the arguments has to be provided")
        elif (arg_count > 1):
            return (False, "only one of the arguments should be provided")

        if id:
            return (True, id)
        if fq_name:
            return (True, self.fq_name_to_id(obj_type, fq_name))
        if fq_name_str:
            return (True, self.fq_name_to_id(obj_type, fq_name_str.split(':')))

    def _object_create(self, res_type, obj):
        obj_type = res_type.replace('-', '_')
        obj_cls = obj_type_to_class(res_type)

        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default=self._obj_serializer)
        json_body = '{"%s":%s}' %(res_type, json_param)
        content = self._request('POST',
                       obj_cls.create_url,
                       data = json_body)

        obj_dict = json.loads(content)[res_type]
        obj.uuid = obj_dict['uuid']
        if 'parent_uuid' in obj_dict:
            obj.parent_uuid = obj_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid

    def _object_read(self, res_type, fq_name=None, fq_name_str=None,
                     id=None, fields=None):
        obj_type = res_type.replace('-', '_')
        obj_cls = obj_type_to_class(res_type)

        (args_ok, result) = self._read_args_to_id(
            res_type, fq_name, fq_name_str, id)
        if not args_ok:
            return result

        id = result
        url = obj_cls.resource_url_base + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request('GET', url, query_params)

        obj_dict = json.loads(content)[res_type]
        obj = obj_cls.from_dict(**obj_dict)
        obj.clear_pending_updates()
        obj.set_server_conn(self)

        return obj

    def _object_update(self, res_type, obj):
        obj_type = res_type.replace('-', '_')
        obj_cls = obj_type_to_class(res_type)

        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id(res_type, obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default=self._obj_serializer)
        json_body = '{"%s":%s}' %(res_type, json_param)

        id = obj.uuid
        url = obj_cls.resource_url_base + '/' + id
        content = self._request('PUT', url, data=json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'),
                             tuple(x.get('to', [])), x.get('attr'))
                        for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'),
                            tuple(x.get('to', [])), x.get('attr'))
                       for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update(res_type, obj.uuid, ref_name, ref[0],
                                 list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update(res_type, obj.uuid, ref_name, ref[0],
                                 list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    # end _object_update

    def _objects_list(self, res_type, parent_id=None, parent_fq_name=None,
                     obj_uuids=None, back_ref_id=None, fields=None,
                     detail=False, count=False, filters=None):
        return self.resource_list(res_type, parent_id=parent_id,
            parent_fq_name=parent_fq_name, back_ref_id=back_ref_id,
            obj_uuids=obj_uuids, fields=fields, detail=detail, count=count,
            filters=filters)
    # end _objects_list

    def _object_delete(self, res_type, fq_name=None, id=None):
        obj_type = res_type.replace('-', '_')
        obj_cls = obj_type_to_class(res_type)

        (args_ok, result) = self._read_args_to_id(
            obj_type=res_type, fq_name=fq_name, id=id)
        if not args_ok:
            return result

        id = result
        url = obj_cls.resource_url_base + '/' + id

        content = self._request('DELETE', url)
    # end _object_delete

    def _object_get_default_id(self, res_type):
        obj_type = res_type.replace('-', '_')
        obj_cls = obj_type_to_class(res_type)

        return self.fq_name_to_id(res_type, obj_cls().get_fq_name())
    # end _object_get_default_id

    def _obj_serializer_diff(self, obj):
        if hasattr(obj, 'serialize_to_json'):
            return obj.serialize_to_json(obj.get_pending_updates())
        else:
            return dict((k, v) for k, v in obj.__dict__.iteritems())
    #end _obj_serializer_diff

    def _obj_serializer_all(self, obj):
        if hasattr(obj, 'serialize_to_json'):
            return obj.serialize_to_json()
        else:
            return dict((k, v) for k, v in obj.__dict__.iteritems())
    #end _obj_serializer_all

    def _generate_auth_body(self):
        # find cases where we cannot produce a valid auth request
        if (not self._auth_params or 
            self._auth_params.get('type') != 'keystone' or
            self._auth_params.get('auth_url') is None or
            self._auth_params.get('username') is None or
            self._auth_params.get('password') is None or
            self._auth_params.get('tenant_name') is None):
            return None

        if 'v2' in self._auth_params['auth_url']:
            body_dict = {
                'auth': {
                    'passwordCredentials': {
                        'username': self._auth_params['username'],
                        'password': self._auth_params['password'],
                    },
                    'tenantName': self._auth_params['tenant_name']
                }}
            return json.dumps(body_dict)
        else:
            body_dict = {'auth': {
                'identity': {
                    'methods': ['password'],
                    'password': {
                        'user': {
                            'name': self._auth_params['username'],
                            'domain': {
                                'id': self._auth_params.get('domain_id',
                                                            'default')},
                            'password': self._auth_params['password']}},
                    'scope': {
                        'project': {
                            'domain': {
                                'id': self._auth_params.get('domain_id',
                                                            'default')},
                            'name': self._auth_params['username']}}}}}
            return json.dumps(body_dict)

    def ref_update(self, obj_type, obj_uuid, 
        ref_type, ref_uuid, ref_fq_name, operation, attr=None):
        if ref_type.endswith('_refs'):
            ref_type = ref_type[:-5].replace('_', '-')
        json_body = json.dumps({'type': obj_type, 'uuid': obj_uuid,
                                'ref-type': ref_type, 'ref-uuid': ref_uuid,
                                'ref-fq-name': ref_fq_name,
                                'operation': operation, 'attr': attr},
                               default=self._obj_serializer_diff)
        url = self._action_url['ref-update']
        try:
            content = self._request('POST', url, data=json_body)
        except exceptions.HttpError as he:
            if he.status_code == 404:
                return None
            raise he

        return json.loads(content)['uuid']

    def obj_to_id(self, obj):
        return self.fq_name_to_id(obj.get_type(), obj.get_fq_name())

    def fq_name_to_id(self, obj_type, fq_name):
        json_body = json.dumps({'type': obj_type, 'fq_name': fq_name})
        url = self._action_url['name-to-id']
        try:
            content = self._request('POST', url, data=json_body)
        except exceptions.HttpError as he:
            if he.status_code == 404:
                return None
            raise he

        return json.loads(content)['uuid']

    def id_to_fq_name(self, id):
        json_body = json.dumps({'uuid': id})
        url = self._action_url['id-to-name']
        content = self._request('POST', url, data=json_body)

        return json.loads(content)['fq_name']

    def id_to_fq_name_type(self, id):
        json_body = json.dumps({'uuid': id})
        url = self._action_url['id-to-name']
        content = self._request('POST', url, data=json_body)

        json_rsp = json.loads(content)
        return (json_rsp['fq_name'], json_rsp['type'])

    def resource_list(self, obj_type, parent_id=None, parent_fq_name=None,
                      back_ref_id=None, obj_uuids=None, fields=None,
                      detail=False, count=False, filters=None):
        if not obj_type:
            raise exceptions.ResourceTypeUnknownError(obj_type)

        obj_class = obj_type_to_class(obj_type)
        if not obj_class:
            raise exceptions.ResourceTypeUnknownError(obj_type)

        query_params = {}
        do_post_for_list = False

        if parent_fq_name:
            parent_fq_name_str = ':'.join(parent_fq_name)
            query_params['parent_fq_name_str'] = parent_fq_name_str
        elif parent_id:
            if isinstance(parent_id, list):
                query_params['parent_id'] = ','.join(parent_id)
                if len(parent_id) > self.POST_FOR_LIST_THRESHOLD:
                    do_post_for_list = True
            else:
                query_params['parent_id'] = parent_id

        if back_ref_id:
            if isinstance(back_ref_id, list):
                query_params['back_ref_id'] = ','.join(back_ref_id)
                if len(back_ref_id) > self.POST_FOR_LIST_THRESHOLD:
                    do_post_for_list = True
            else:
                query_params['back_ref_id'] = back_ref_id

        if obj_uuids:
            comma_sep_obj_uuids = ','.join(u for u in obj_uuids)
            query_params['obj_uuids'] = comma_sep_obj_uuids
            if len(obj_uuids) > self.POST_FOR_LIST_THRESHOLD:
                do_post_for_list = True

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params['fields'] = comma_sep_fields

        query_params['detail'] = detail

        query_params['count'] = count

        if filters:
            query_params['filters'] = ','.join(
                '%s==%s' %(k,json.dumps(v)) for k,v in filters.items())

        if do_post_for_list:
            url = self._action_url.get('list-bulk-collection')
            if not url:
                raise

            # use same keys as in GET with additional 'type'
            query_params['type'] = obj_type
            json_body = json.dumps(query_params)
            content = self._request('POST', url, json_body)
        else: # GET /<collection>
            try:
                content = self._request('GET',
                               obj_class.create_url,
                               data=query_params)
            except exceptions.NoIdError:
                # dont allow NoIdError propagate to user
                return []

        if not detail:
            return json.loads(content)

        resource_dicts = json.loads(content)['%ss' %(obj_type)]
        resource_objs = []
        for resource_dict in resource_dicts:
            obj_dict = resource_dict['%s' %(obj_type)]
            resource_obj = obj_class.from_dict(**obj_dict)
            resource_obj.clear_pending_updates()
            resource_obj.set_server_conn(self)
            resource_objs.append(resource_obj)

        return resource_objs
