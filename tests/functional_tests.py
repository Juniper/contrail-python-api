
# Example Usage: 
# python tests/functional_tests.py --api-url http://10.84.34.141:9100 --auth-url http://10.84.34.141:5000/v2.0 --username admin --password secret123 --tenant-name admin

import sys
from pprint import pprint
import argparse
import uuid
from testtools.assertions import assert_that
from testtools.matchers import Contains

import pycontrail.client as client
import pycontrail.types as types
import pycontrail.exceptions

def execute_tests(args):
    c = client.Client(
            url=args.api_url,
            auth_params={'type':'keystone',
                         'auth_url':args.auth_url,
                         'username':args.username,
                         'password':args.password,
                         'tenant_name':args.tenant_name})
    test_default(c)
    vn_obj = []
    try:
        def test_create():
            obj = types.VirtualNetwork('pyc-testvn-%s' %(uuid.uuid4()))
            c.virtual_network_create(obj)
            vn_obj.append(obj)

        def test_read():
            c.virtual_network_read(id=vn_obj[0].uuid)
        
        def test_update():
            vn_obj[0].display_name = 'updated name'
            c.virtual_network_update(vn_obj[0])
        
        def test_list():
            ret_vns = c.virtual_networks_list()
            uuids = [vn['uuid'] for vn in ret_vns['virtual-networks']]
            assert_that(uuids, Contains(vn_obj[0].uuid))
        
        def test_delete():
            c.virtual_network_delete(id=vn_obj[0].uuid)

        test_create()
        test_read()
        test_update()
        test_list()
        test_delete()
    except:
        if vn_obj:
            c.virtual_network_delete(id=vn_obj.uuid)

def test_default(client):
    pprint(client.virtual_networks_list())

def main(args_str=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api-url", help="api-server url", default="http://localhost:9100")
    parser.add_argument(
        "--auth-url", help="keystone auth url",
        default="http://localhost:5000/v2.0/")
    parser.add_argument(
        "--username", help="keystone admin name")
    parser.add_argument(
        "--password", help="keystone admin password")
    parser.add_argument(
        "--tenant-name", help="keystone tenant name")
    args, remaining_argv = parser.parse_known_args(
        args_str.split() if args_str else [])

    execute_tests(args)

if __name__ == "__main__":
    main(' '.join(sys.argv[1:]))
