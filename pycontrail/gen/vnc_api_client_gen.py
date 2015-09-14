
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

import json
import pycontrail.gen.resource_xsd
import pycontrail.gen.resource_client
from pycontrail.gen.connection_drv_gen import ConnectionDriverBase

class VncApiClientGen(ConnectionDriverBase):
    """
    This class provides type specific methods to create,
    read, update, delete and list objects from the server
    """

    _tenant_name = 'default-tenant'
    def __init__(self, obj_serializer):
        self._obj_serializer = obj_serializer
        self._type_to_class = {}
        self._type_to_class['domain'] = pycontrail.gen.resource_client.Domain
        self._type_to_class['global_vrouter_config'] = pycontrail.gen.resource_client.GlobalVrouterConfig
        self._type_to_class['instance_ip'] = pycontrail.gen.resource_client.InstanceIp
        self._type_to_class['network_policy'] = pycontrail.gen.resource_client.NetworkPolicy
        self._type_to_class['loadbalancer_pool'] = pycontrail.gen.resource_client.LoadbalancerPool
        self._type_to_class['virtual_DNS_record'] = pycontrail.gen.resource_client.VirtualDnsRecord
        self._type_to_class['route_target'] = pycontrail.gen.resource_client.RouteTarget
        self._type_to_class['floating_ip'] = pycontrail.gen.resource_client.FloatingIp
        self._type_to_class['floating_ip_pool'] = pycontrail.gen.resource_client.FloatingIpPool
        self._type_to_class['physical_router'] = pycontrail.gen.resource_client.PhysicalRouter
        self._type_to_class['bgp_router'] = pycontrail.gen.resource_client.BgpRouter
        self._type_to_class['virtual_router'] = pycontrail.gen.resource_client.VirtualRouter
        self._type_to_class['config_root'] = pycontrail.gen.resource_client.ConfigRoot
        self._type_to_class['subnet'] = pycontrail.gen.resource_client.Subnet
        self._type_to_class['global_system_config'] = pycontrail.gen.resource_client.GlobalSystemConfig
        self._type_to_class['service_appliance'] = pycontrail.gen.resource_client.ServiceAppliance
        self._type_to_class['service_instance'] = pycontrail.gen.resource_client.ServiceInstance
        self._type_to_class['namespace'] = pycontrail.gen.resource_client.Namespace
        self._type_to_class['logical_interface'] = pycontrail.gen.resource_client.LogicalInterface
        self._type_to_class['route_table'] = pycontrail.gen.resource_client.RouteTable
        self._type_to_class['physical_interface'] = pycontrail.gen.resource_client.PhysicalInterface
        self._type_to_class['access_control_list'] = pycontrail.gen.resource_client.AccessControlList
        self._type_to_class['analytics_node'] = pycontrail.gen.resource_client.AnalyticsNode
        self._type_to_class['virtual_DNS'] = pycontrail.gen.resource_client.VirtualDns
        self._type_to_class['customer_attachment'] = pycontrail.gen.resource_client.CustomerAttachment
        self._type_to_class['service_appliance_set'] = pycontrail.gen.resource_client.ServiceApplianceSet
        self._type_to_class['config_node'] = pycontrail.gen.resource_client.ConfigNode
        self._type_to_class['qos_queue'] = pycontrail.gen.resource_client.QosQueue
        self._type_to_class['virtual_machine'] = pycontrail.gen.resource_client.VirtualMachine
        self._type_to_class['interface_route_table'] = pycontrail.gen.resource_client.InterfaceRouteTable
        self._type_to_class['service_template'] = pycontrail.gen.resource_client.ServiceTemplate
        self._type_to_class['virtual_ip'] = pycontrail.gen.resource_client.VirtualIp
        self._type_to_class['loadbalancer_member'] = pycontrail.gen.resource_client.LoadbalancerMember
        self._type_to_class['security_group'] = pycontrail.gen.resource_client.SecurityGroup
        self._type_to_class['provider_attachment'] = pycontrail.gen.resource_client.ProviderAttachment
        self._type_to_class['virtual_machine_interface'] = pycontrail.gen.resource_client.VirtualMachineInterface
        self._type_to_class['loadbalancer_healthmonitor'] = pycontrail.gen.resource_client.LoadbalancerHealthmonitor
        self._type_to_class['virtual_network'] = pycontrail.gen.resource_client.VirtualNetwork
        self._type_to_class['project'] = pycontrail.gen.resource_client.Project
        self._type_to_class['qos_forwarding_class'] = pycontrail.gen.resource_client.QosForwardingClass
        self._type_to_class['database_node'] = pycontrail.gen.resource_client.DatabaseNode
        self._type_to_class['routing_instance'] = pycontrail.gen.resource_client.RoutingInstance
        self._type_to_class['network_ipam'] = pycontrail.gen.resource_client.NetworkIpam
        self._type_to_class['logical_router'] = pycontrail.gen.resource_client.LogicalRouter
    #end __init__
    def domain_create(self, obj):
        """Create new domain.
        
        :param obj: :class:`.Domain` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"domain":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.Domain.create_uri,
                       data = json_body)

        domain_dict = json.loads(content)['domain']
        obj.uuid = domain_dict['uuid']
        if 'parent_uuid' in domain_dict:
            obj.parent_uuid = domain_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end domain_create

    def domain_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return domain information.
        
        :param fq_name: Fully qualified name of domain
        :param fq_name_str: Fully qualified name string of domain
        :param id: UUID of domain
        :param ifmap_id: IFMAP id of domain
        :returns: :class:`.Domain` object
        
        """
        (args_ok, result) = self._read_args_to_id('domain', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Domain.resource_uri_base['domain'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['domain']
        domain_obj = pycontrail.gen.resource_client.Domain.from_dict(**obj_dict)
        domain_obj.clear_pending_updates()
        domain_obj.set_server_conn(self)

        return domain_obj
    #end domain_read

    def domain_update(self, obj):
        """Update domain.
        
        :param obj: :class:`.Domain` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('domain', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"domain":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.Domain.resource_uri_base['domain'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('domain', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('domain', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end domain_update

    def domains_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all domains.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Domain` objects
        
        """
        return self.resource_list('domain', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end domains_list

    def domain_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete domain from the system.
        
        :param fq_name: Fully qualified name of domain
        :param id: UUID of domain
        :param ifmap_id: IFMAP id of domain
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'domain', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Domain.resource_uri_base['domain'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end domain_delete

    def get_default_domain_id(self):
        """Return UUID of default domain."""
        return self.fq_name_to_id('domain', pycontrail.gen.resource_client.Domain().get_fq_name())
    #end get_default_domain_delete

    def global_vrouter_config_create(self, obj):
        """Create new global-vrouter-config.
        
        :param obj: :class:`.GlobalVrouterConfig` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"global-vrouter-config":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.GlobalVrouterConfig.create_uri,
                       data = json_body)

        global_vrouter_config_dict = json.loads(content)['global-vrouter-config']
        obj.uuid = global_vrouter_config_dict['uuid']
        if 'parent_uuid' in global_vrouter_config_dict:
            obj.parent_uuid = global_vrouter_config_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end global_vrouter_config_create

    def global_vrouter_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return global-vrouter-config information.
        
        :param fq_name: Fully qualified name of global-vrouter-config
        :param fq_name_str: Fully qualified name string of global-vrouter-config
        :param id: UUID of global-vrouter-config
        :param ifmap_id: IFMAP id of global-vrouter-config
        :returns: :class:`.GlobalVrouterConfig` object
        
        """
        (args_ok, result) = self._read_args_to_id('global-vrouter-config', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.GlobalVrouterConfig.resource_uri_base['global-vrouter-config'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['global-vrouter-config']
        global_vrouter_config_obj = pycontrail.gen.resource_client.GlobalVrouterConfig.from_dict(**obj_dict)
        global_vrouter_config_obj.clear_pending_updates()
        global_vrouter_config_obj.set_server_conn(self)

        return global_vrouter_config_obj
    #end global_vrouter_config_read

    def global_vrouter_config_update(self, obj):
        """Update global-vrouter-config.
        
        :param obj: :class:`.GlobalVrouterConfig` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('global-vrouter-config', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"global-vrouter-config":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.GlobalVrouterConfig.resource_uri_base['global-vrouter-config'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('global-vrouter-config', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('global-vrouter-config', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end global_vrouter_config_update

    def global_vrouter_configs_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all global-vrouter-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalVrouterConfig` objects
        
        """
        return self.resource_list('global-vrouter-config', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end global_vrouter_configs_list

    def global_vrouter_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-vrouter-config from the system.
        
        :param fq_name: Fully qualified name of global-vrouter-config
        :param id: UUID of global-vrouter-config
        :param ifmap_id: IFMAP id of global-vrouter-config
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'global-vrouter-config', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.GlobalVrouterConfig.resource_uri_base['global-vrouter-config'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end global_vrouter_config_delete

    def get_default_global_vrouter_config_id(self):
        """Return UUID of default global-vrouter-config."""
        return self.fq_name_to_id('global-vrouter-config', pycontrail.gen.resource_client.GlobalVrouterConfig().get_fq_name())
    #end get_default_global_vrouter_config_delete

    def instance_ip_create(self, obj):
        """Create new instance-ip.
        
        :param obj: :class:`.InstanceIp` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"instance-ip":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.InstanceIp.create_uri,
                       data = json_body)

        instance_ip_dict = json.loads(content)['instance-ip']
        obj.uuid = instance_ip_dict['uuid']
        if 'parent_uuid' in instance_ip_dict:
            obj.parent_uuid = instance_ip_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end instance_ip_create

    def instance_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return instance-ip information.
        
        :param fq_name: Fully qualified name of instance-ip
        :param fq_name_str: Fully qualified name string of instance-ip
        :param id: UUID of instance-ip
        :param ifmap_id: IFMAP id of instance-ip
        :returns: :class:`.InstanceIp` object
        
        """
        (args_ok, result) = self._read_args_to_id('instance-ip', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.InstanceIp.resource_uri_base['instance-ip'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['instance-ip']
        instance_ip_obj = pycontrail.gen.resource_client.InstanceIp.from_dict(**obj_dict)
        instance_ip_obj.clear_pending_updates()
        instance_ip_obj.set_server_conn(self)

        return instance_ip_obj
    #end instance_ip_read

    def instance_ip_update(self, obj):
        """Update instance-ip.
        
        :param obj: :class:`.InstanceIp` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('instance-ip', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"instance-ip":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.InstanceIp.resource_uri_base['instance-ip'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('instance-ip', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('instance-ip', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end instance_ip_update

    def instance_ips_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all instance-ips."""
        return self.resource_list('instance-ip', back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end instance_ips_list

    def instance_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete instance-ip from the system.
        
        :param fq_name: Fully qualified name of instance-ip
        :param id: UUID of instance-ip
        :param ifmap_id: IFMAP id of instance-ip
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'instance-ip', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.InstanceIp.resource_uri_base['instance-ip'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end instance_ip_delete

    def get_default_instance_ip_id(self):
        """Return UUID of default instance-ip."""
        return self.fq_name_to_id('instance-ip', pycontrail.gen.resource_client.InstanceIp().get_fq_name())
    #end get_default_instance_ip_delete

    def network_policy_create(self, obj):
        """Create new network-policy.
        
        :param obj: :class:`.NetworkPolicy` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"network-policy":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.NetworkPolicy.create_uri,
                       data = json_body)

        network_policy_dict = json.loads(content)['network-policy']
        obj.uuid = network_policy_dict['uuid']
        if 'parent_uuid' in network_policy_dict:
            obj.parent_uuid = network_policy_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end network_policy_create

    def network_policy_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return network-policy information.
        
        :param fq_name: Fully qualified name of network-policy
        :param fq_name_str: Fully qualified name string of network-policy
        :param id: UUID of network-policy
        :param ifmap_id: IFMAP id of network-policy
        :returns: :class:`.NetworkPolicy` object
        
        """
        (args_ok, result) = self._read_args_to_id('network-policy', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.NetworkPolicy.resource_uri_base['network-policy'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['network-policy']
        network_policy_obj = pycontrail.gen.resource_client.NetworkPolicy.from_dict(**obj_dict)
        network_policy_obj.clear_pending_updates()
        network_policy_obj.set_server_conn(self)

        return network_policy_obj
    #end network_policy_read

    def network_policy_update(self, obj):
        """Update network-policy.
        
        :param obj: :class:`.NetworkPolicy` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('network-policy', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"network-policy":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.NetworkPolicy.resource_uri_base['network-policy'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('network-policy', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('network-policy', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end network_policy_update

    def network_policys_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all network-policys.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.NetworkPolicy` objects
        
        """
        return self.resource_list('network-policy', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end network_policys_list

    def network_policy_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete network-policy from the system.
        
        :param fq_name: Fully qualified name of network-policy
        :param id: UUID of network-policy
        :param ifmap_id: IFMAP id of network-policy
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'network-policy', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.NetworkPolicy.resource_uri_base['network-policy'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end network_policy_delete

    def get_default_network_policy_id(self):
        """Return UUID of default network-policy."""
        return self.fq_name_to_id('network-policy', pycontrail.gen.resource_client.NetworkPolicy().get_fq_name())
    #end get_default_network_policy_delete

    def loadbalancer_pool_create(self, obj):
        """Create new loadbalancer-pool.
        
        :param obj: :class:`.LoadbalancerPool` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"loadbalancer-pool":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.LoadbalancerPool.create_uri,
                       data = json_body)

        loadbalancer_pool_dict = json.loads(content)['loadbalancer-pool']
        obj.uuid = loadbalancer_pool_dict['uuid']
        if 'parent_uuid' in loadbalancer_pool_dict:
            obj.parent_uuid = loadbalancer_pool_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end loadbalancer_pool_create

    def loadbalancer_pool_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return loadbalancer-pool information.
        
        :param fq_name: Fully qualified name of loadbalancer-pool
        :param fq_name_str: Fully qualified name string of loadbalancer-pool
        :param id: UUID of loadbalancer-pool
        :param ifmap_id: IFMAP id of loadbalancer-pool
        :returns: :class:`.LoadbalancerPool` object
        
        """
        (args_ok, result) = self._read_args_to_id('loadbalancer-pool', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LoadbalancerPool.resource_uri_base['loadbalancer-pool'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['loadbalancer-pool']
        loadbalancer_pool_obj = pycontrail.gen.resource_client.LoadbalancerPool.from_dict(**obj_dict)
        loadbalancer_pool_obj.clear_pending_updates()
        loadbalancer_pool_obj.set_server_conn(self)

        return loadbalancer_pool_obj
    #end loadbalancer_pool_read

    def loadbalancer_pool_update(self, obj):
        """Update loadbalancer-pool.
        
        :param obj: :class:`.LoadbalancerPool` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('loadbalancer-pool', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"loadbalancer-pool":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.LoadbalancerPool.resource_uri_base['loadbalancer-pool'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('loadbalancer-pool', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('loadbalancer-pool', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end loadbalancer_pool_update

    def loadbalancer_pools_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all loadbalancer-pools.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerPool` objects
        
        """
        return self.resource_list('loadbalancer-pool', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end loadbalancer_pools_list

    def loadbalancer_pool_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-pool from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-pool
        :param id: UUID of loadbalancer-pool
        :param ifmap_id: IFMAP id of loadbalancer-pool
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'loadbalancer-pool', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LoadbalancerPool.resource_uri_base['loadbalancer-pool'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end loadbalancer_pool_delete

    def get_default_loadbalancer_pool_id(self):
        """Return UUID of default loadbalancer-pool."""
        return self.fq_name_to_id('loadbalancer-pool', pycontrail.gen.resource_client.LoadbalancerPool().get_fq_name())
    #end get_default_loadbalancer_pool_delete

    def virtual_DNS_record_create(self, obj):
        """Create new virtual-DNS-record.
        
        :param obj: :class:`.VirtualDnsRecord` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-DNS-record":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.VirtualDnsRecord.create_uri,
                       data = json_body)

        virtual_DNS_record_dict = json.loads(content)['virtual-DNS-record']
        obj.uuid = virtual_DNS_record_dict['uuid']
        if 'parent_uuid' in virtual_DNS_record_dict:
            obj.parent_uuid = virtual_DNS_record_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end virtual_DNS_record_create

    def virtual_DNS_record_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return virtual-DNS-record information.
        
        :param fq_name: Fully qualified name of virtual-DNS-record
        :param fq_name_str: Fully qualified name string of virtual-DNS-record
        :param id: UUID of virtual-DNS-record
        :param ifmap_id: IFMAP id of virtual-DNS-record
        :returns: :class:`.VirtualDnsRecord` object
        
        """
        (args_ok, result) = self._read_args_to_id('virtual-DNS-record', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualDnsRecord.resource_uri_base['virtual-DNS-record'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['virtual-DNS-record']
        virtual_DNS_record_obj = pycontrail.gen.resource_client.VirtualDnsRecord.from_dict(**obj_dict)
        virtual_DNS_record_obj.clear_pending_updates()
        virtual_DNS_record_obj.set_server_conn(self)

        return virtual_DNS_record_obj
    #end virtual_DNS_record_read

    def virtual_DNS_record_update(self, obj):
        """Update virtual-DNS-record.
        
        :param obj: :class:`.VirtualDnsRecord` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('virtual-DNS-record', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-DNS-record":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.VirtualDnsRecord.resource_uri_base['virtual-DNS-record'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('virtual-DNS-record', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('virtual-DNS-record', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end virtual_DNS_record_update

    def virtual_DNS_records_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all virtual-DNS-records.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualDnsRecord` objects
        
        """
        return self.resource_list('virtual-DNS-record', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end virtual_DNS_records_list

    def virtual_DNS_record_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-DNS-record from the system.
        
        :param fq_name: Fully qualified name of virtual-DNS-record
        :param id: UUID of virtual-DNS-record
        :param ifmap_id: IFMAP id of virtual-DNS-record
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'virtual-DNS-record', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualDnsRecord.resource_uri_base['virtual-DNS-record'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end virtual_DNS_record_delete

    def get_default_virtual_DNS_record_id(self):
        """Return UUID of default virtual-DNS-record."""
        return self.fq_name_to_id('virtual-DNS-record', pycontrail.gen.resource_client.VirtualDnsRecord().get_fq_name())
    #end get_default_virtual_DNS_record_delete

    def route_target_create(self, obj):
        """Create new route-target.
        
        :param obj: :class:`.RouteTarget` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"route-target":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.RouteTarget.create_uri,
                       data = json_body)

        route_target_dict = json.loads(content)['route-target']
        obj.uuid = route_target_dict['uuid']
        if 'parent_uuid' in route_target_dict:
            obj.parent_uuid = route_target_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end route_target_create

    def route_target_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return route-target information.
        
        :param fq_name: Fully qualified name of route-target
        :param fq_name_str: Fully qualified name string of route-target
        :param id: UUID of route-target
        :param ifmap_id: IFMAP id of route-target
        :returns: :class:`.RouteTarget` object
        
        """
        (args_ok, result) = self._read_args_to_id('route-target', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.RouteTarget.resource_uri_base['route-target'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['route-target']
        route_target_obj = pycontrail.gen.resource_client.RouteTarget.from_dict(**obj_dict)
        route_target_obj.clear_pending_updates()
        route_target_obj.set_server_conn(self)

        return route_target_obj
    #end route_target_read

    def route_target_update(self, obj):
        """Update route-target.
        
        :param obj: :class:`.RouteTarget` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('route-target', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"route-target":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.RouteTarget.resource_uri_base['route-target'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('route-target', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('route-target', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end route_target_update

    def route_targets_list(self, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all route-targets."""
        return self.resource_list('route-target', obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end route_targets_list

    def route_target_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete route-target from the system.
        
        :param fq_name: Fully qualified name of route-target
        :param id: UUID of route-target
        :param ifmap_id: IFMAP id of route-target
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'route-target', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.RouteTarget.resource_uri_base['route-target'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end route_target_delete

    def get_default_route_target_id(self):
        """Return UUID of default route-target."""
        return self.fq_name_to_id('route-target', pycontrail.gen.resource_client.RouteTarget().get_fq_name())
    #end get_default_route_target_delete

    def floating_ip_create(self, obj):
        """Create new floating-ip.
        
        :param obj: :class:`.FloatingIp` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"floating-ip":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.FloatingIp.create_uri,
                       data = json_body)

        floating_ip_dict = json.loads(content)['floating-ip']
        obj.uuid = floating_ip_dict['uuid']
        if 'parent_uuid' in floating_ip_dict:
            obj.parent_uuid = floating_ip_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end floating_ip_create

    def floating_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return floating-ip information.
        
        :param fq_name: Fully qualified name of floating-ip
        :param fq_name_str: Fully qualified name string of floating-ip
        :param id: UUID of floating-ip
        :param ifmap_id: IFMAP id of floating-ip
        :returns: :class:`.FloatingIp` object
        
        """
        (args_ok, result) = self._read_args_to_id('floating-ip', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.FloatingIp.resource_uri_base['floating-ip'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['floating-ip']
        floating_ip_obj = pycontrail.gen.resource_client.FloatingIp.from_dict(**obj_dict)
        floating_ip_obj.clear_pending_updates()
        floating_ip_obj.set_server_conn(self)

        return floating_ip_obj
    #end floating_ip_read

    def floating_ip_update(self, obj):
        """Update floating-ip.
        
        :param obj: :class:`.FloatingIp` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('floating-ip', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"floating-ip":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.FloatingIp.resource_uri_base['floating-ip'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('floating-ip', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('floating-ip', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end floating_ip_update

    def floating_ips_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all floating-ips.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FloatingIp` objects
        
        """
        return self.resource_list('floating-ip', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end floating_ips_list

    def floating_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete floating-ip from the system.
        
        :param fq_name: Fully qualified name of floating-ip
        :param id: UUID of floating-ip
        :param ifmap_id: IFMAP id of floating-ip
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'floating-ip', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.FloatingIp.resource_uri_base['floating-ip'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end floating_ip_delete

    def get_default_floating_ip_id(self):
        """Return UUID of default floating-ip."""
        return self.fq_name_to_id('floating-ip', pycontrail.gen.resource_client.FloatingIp().get_fq_name())
    #end get_default_floating_ip_delete

    def floating_ip_pool_create(self, obj):
        """Create new floating-ip-pool.
        
        :param obj: :class:`.FloatingIpPool` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"floating-ip-pool":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.FloatingIpPool.create_uri,
                       data = json_body)

        floating_ip_pool_dict = json.loads(content)['floating-ip-pool']
        obj.uuid = floating_ip_pool_dict['uuid']
        if 'parent_uuid' in floating_ip_pool_dict:
            obj.parent_uuid = floating_ip_pool_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end floating_ip_pool_create

    def floating_ip_pool_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return floating-ip-pool information.
        
        :param fq_name: Fully qualified name of floating-ip-pool
        :param fq_name_str: Fully qualified name string of floating-ip-pool
        :param id: UUID of floating-ip-pool
        :param ifmap_id: IFMAP id of floating-ip-pool
        :returns: :class:`.FloatingIpPool` object
        
        """
        (args_ok, result) = self._read_args_to_id('floating-ip-pool', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.FloatingIpPool.resource_uri_base['floating-ip-pool'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['floating-ip-pool']
        floating_ip_pool_obj = pycontrail.gen.resource_client.FloatingIpPool.from_dict(**obj_dict)
        floating_ip_pool_obj.clear_pending_updates()
        floating_ip_pool_obj.set_server_conn(self)

        return floating_ip_pool_obj
    #end floating_ip_pool_read

    def floating_ip_pool_update(self, obj):
        """Update floating-ip-pool.
        
        :param obj: :class:`.FloatingIpPool` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('floating-ip-pool', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"floating-ip-pool":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.FloatingIpPool.resource_uri_base['floating-ip-pool'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('floating-ip-pool', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('floating-ip-pool', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end floating_ip_pool_update

    def floating_ip_pools_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all floating-ip-pools.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FloatingIpPool` objects
        
        """
        return self.resource_list('floating-ip-pool', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end floating_ip_pools_list

    def floating_ip_pool_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete floating-ip-pool from the system.
        
        :param fq_name: Fully qualified name of floating-ip-pool
        :param id: UUID of floating-ip-pool
        :param ifmap_id: IFMAP id of floating-ip-pool
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'floating-ip-pool', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.FloatingIpPool.resource_uri_base['floating-ip-pool'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end floating_ip_pool_delete

    def get_default_floating_ip_pool_id(self):
        """Return UUID of default floating-ip-pool."""
        return self.fq_name_to_id('floating-ip-pool', pycontrail.gen.resource_client.FloatingIpPool().get_fq_name())
    #end get_default_floating_ip_pool_delete

    def physical_router_create(self, obj):
        """Create new physical-router.
        
        :param obj: :class:`.PhysicalRouter` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"physical-router":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.PhysicalRouter.create_uri,
                       data = json_body)

        physical_router_dict = json.loads(content)['physical-router']
        obj.uuid = physical_router_dict['uuid']
        if 'parent_uuid' in physical_router_dict:
            obj.parent_uuid = physical_router_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end physical_router_create

    def physical_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return physical-router information.
        
        :param fq_name: Fully qualified name of physical-router
        :param fq_name_str: Fully qualified name string of physical-router
        :param id: UUID of physical-router
        :param ifmap_id: IFMAP id of physical-router
        :returns: :class:`.PhysicalRouter` object
        
        """
        (args_ok, result) = self._read_args_to_id('physical-router', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.PhysicalRouter.resource_uri_base['physical-router'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['physical-router']
        physical_router_obj = pycontrail.gen.resource_client.PhysicalRouter.from_dict(**obj_dict)
        physical_router_obj.clear_pending_updates()
        physical_router_obj.set_server_conn(self)

        return physical_router_obj
    #end physical_router_read

    def physical_router_update(self, obj):
        """Update physical-router.
        
        :param obj: :class:`.PhysicalRouter` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('physical-router', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"physical-router":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.PhysicalRouter.resource_uri_base['physical-router'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('physical-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('physical-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end physical_router_update

    def physical_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all physical-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PhysicalRouter` objects
        
        """
        return self.resource_list('physical-router', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end physical_routers_list

    def physical_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete physical-router from the system.
        
        :param fq_name: Fully qualified name of physical-router
        :param id: UUID of physical-router
        :param ifmap_id: IFMAP id of physical-router
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'physical-router', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.PhysicalRouter.resource_uri_base['physical-router'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end physical_router_delete

    def get_default_physical_router_id(self):
        """Return UUID of default physical-router."""
        return self.fq_name_to_id('physical-router', pycontrail.gen.resource_client.PhysicalRouter().get_fq_name())
    #end get_default_physical_router_delete

    def bgp_router_create(self, obj):
        """Create new bgp-router.
        
        :param obj: :class:`.BgpRouter` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"bgp-router":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.BgpRouter.create_uri,
                       data = json_body)

        bgp_router_dict = json.loads(content)['bgp-router']
        obj.uuid = bgp_router_dict['uuid']
        if 'parent_uuid' in bgp_router_dict:
            obj.parent_uuid = bgp_router_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end bgp_router_create

    def bgp_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return bgp-router information.
        
        :param fq_name: Fully qualified name of bgp-router
        :param fq_name_str: Fully qualified name string of bgp-router
        :param id: UUID of bgp-router
        :param ifmap_id: IFMAP id of bgp-router
        :returns: :class:`.BgpRouter` object
        
        """
        (args_ok, result) = self._read_args_to_id('bgp-router', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.BgpRouter.resource_uri_base['bgp-router'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['bgp-router']
        bgp_router_obj = pycontrail.gen.resource_client.BgpRouter.from_dict(**obj_dict)
        bgp_router_obj.clear_pending_updates()
        bgp_router_obj.set_server_conn(self)

        return bgp_router_obj
    #end bgp_router_read

    def bgp_router_update(self, obj):
        """Update bgp-router.
        
        :param obj: :class:`.BgpRouter` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('bgp-router', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"bgp-router":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.BgpRouter.resource_uri_base['bgp-router'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('bgp-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('bgp-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end bgp_router_update

    def bgp_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all bgp-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.BgpRouter` objects
        
        """
        return self.resource_list('bgp-router', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end bgp_routers_list

    def bgp_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete bgp-router from the system.
        
        :param fq_name: Fully qualified name of bgp-router
        :param id: UUID of bgp-router
        :param ifmap_id: IFMAP id of bgp-router
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'bgp-router', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.BgpRouter.resource_uri_base['bgp-router'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end bgp_router_delete

    def get_default_bgp_router_id(self):
        """Return UUID of default bgp-router."""
        return self.fq_name_to_id('bgp-router', pycontrail.gen.resource_client.BgpRouter().get_fq_name())
    #end get_default_bgp_router_delete

    def virtual_router_create(self, obj):
        """Create new virtual-router.
        
        :param obj: :class:`.VirtualRouter` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-router":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.VirtualRouter.create_uri,
                       data = json_body)

        virtual_router_dict = json.loads(content)['virtual-router']
        obj.uuid = virtual_router_dict['uuid']
        if 'parent_uuid' in virtual_router_dict:
            obj.parent_uuid = virtual_router_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end virtual_router_create

    def virtual_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return virtual-router information.
        
        :param fq_name: Fully qualified name of virtual-router
        :param fq_name_str: Fully qualified name string of virtual-router
        :param id: UUID of virtual-router
        :param ifmap_id: IFMAP id of virtual-router
        :returns: :class:`.VirtualRouter` object
        
        """
        (args_ok, result) = self._read_args_to_id('virtual-router', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualRouter.resource_uri_base['virtual-router'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['virtual-router']
        virtual_router_obj = pycontrail.gen.resource_client.VirtualRouter.from_dict(**obj_dict)
        virtual_router_obj.clear_pending_updates()
        virtual_router_obj.set_server_conn(self)

        return virtual_router_obj
    #end virtual_router_read

    def virtual_router_update(self, obj):
        """Update virtual-router.
        
        :param obj: :class:`.VirtualRouter` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('virtual-router', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-router":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.VirtualRouter.resource_uri_base['virtual-router'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('virtual-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('virtual-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end virtual_router_update

    def virtual_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all virtual-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualRouter` objects
        
        """
        return self.resource_list('virtual-router', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end virtual_routers_list

    def virtual_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-router from the system.
        
        :param fq_name: Fully qualified name of virtual-router
        :param id: UUID of virtual-router
        :param ifmap_id: IFMAP id of virtual-router
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'virtual-router', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualRouter.resource_uri_base['virtual-router'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end virtual_router_delete

    def get_default_virtual_router_id(self):
        """Return UUID of default virtual-router."""
        return self.fq_name_to_id('virtual-router', pycontrail.gen.resource_client.VirtualRouter().get_fq_name())
    #end get_default_virtual_router_delete

    def config_root_create(self, obj):
        """Create new config-root.
        
        :param obj: :class:`.ConfigRoot` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"config-root":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.ConfigRoot.create_uri,
                       data = json_body)

        config_root_dict = json.loads(content)['config-root']
        obj.uuid = config_root_dict['uuid']
        if 'parent_uuid' in config_root_dict:
            obj.parent_uuid = config_root_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end config_root_create

    def config_root_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return config-root information.
        
        :param fq_name: Fully qualified name of config-root
        :param fq_name_str: Fully qualified name string of config-root
        :param id: UUID of config-root
        :param ifmap_id: IFMAP id of config-root
        :returns: :class:`.ConfigRoot` object
        
        """
        (args_ok, result) = self._read_args_to_id('config-root', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ConfigRoot.resource_uri_base['config-root'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['config-root']
        config_root_obj = pycontrail.gen.resource_client.ConfigRoot.from_dict(**obj_dict)
        config_root_obj.clear_pending_updates()
        config_root_obj.set_server_conn(self)

        return config_root_obj
    #end config_root_read

    def config_root_update(self, obj):
        """Update config-root.
        
        :param obj: :class:`.ConfigRoot` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('config-root', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"config-root":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.ConfigRoot.resource_uri_base['config-root'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('config-root', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('config-root', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end config_root_update

    def config_roots_list(self, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all config-roots."""
        return self.resource_list('config-root', obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end config_roots_list

    def config_root_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete config-root from the system.
        
        :param fq_name: Fully qualified name of config-root
        :param id: UUID of config-root
        :param ifmap_id: IFMAP id of config-root
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'config-root', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ConfigRoot.resource_uri_base['config-root'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end config_root_delete

    def get_default_config_root_id(self):
        """Return UUID of default config-root."""
        return self.fq_name_to_id('config-root', pycontrail.gen.resource_client.ConfigRoot().get_fq_name())
    #end get_default_config_root_delete

    def subnet_create(self, obj):
        """Create new subnet.
        
        :param obj: :class:`.Subnet` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"subnet":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.Subnet.create_uri,
                       data = json_body)

        subnet_dict = json.loads(content)['subnet']
        obj.uuid = subnet_dict['uuid']
        if 'parent_uuid' in subnet_dict:
            obj.parent_uuid = subnet_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end subnet_create

    def subnet_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return subnet information.
        
        :param fq_name: Fully qualified name of subnet
        :param fq_name_str: Fully qualified name string of subnet
        :param id: UUID of subnet
        :param ifmap_id: IFMAP id of subnet
        :returns: :class:`.Subnet` object
        
        """
        (args_ok, result) = self._read_args_to_id('subnet', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Subnet.resource_uri_base['subnet'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['subnet']
        subnet_obj = pycontrail.gen.resource_client.Subnet.from_dict(**obj_dict)
        subnet_obj.clear_pending_updates()
        subnet_obj.set_server_conn(self)

        return subnet_obj
    #end subnet_read

    def subnet_update(self, obj):
        """Update subnet.
        
        :param obj: :class:`.Subnet` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('subnet', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"subnet":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.Subnet.resource_uri_base['subnet'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('subnet', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('subnet', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end subnet_update

    def subnets_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all subnets."""
        return self.resource_list('subnet', back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end subnets_list

    def subnet_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete subnet from the system.
        
        :param fq_name: Fully qualified name of subnet
        :param id: UUID of subnet
        :param ifmap_id: IFMAP id of subnet
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'subnet', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Subnet.resource_uri_base['subnet'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end subnet_delete

    def get_default_subnet_id(self):
        """Return UUID of default subnet."""
        return self.fq_name_to_id('subnet', pycontrail.gen.resource_client.Subnet().get_fq_name())
    #end get_default_subnet_delete

    def global_system_config_create(self, obj):
        """Create new global-system-config.
        
        :param obj: :class:`.GlobalSystemConfig` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"global-system-config":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.GlobalSystemConfig.create_uri,
                       data = json_body)

        global_system_config_dict = json.loads(content)['global-system-config']
        obj.uuid = global_system_config_dict['uuid']
        if 'parent_uuid' in global_system_config_dict:
            obj.parent_uuid = global_system_config_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end global_system_config_create

    def global_system_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return global-system-config information.
        
        :param fq_name: Fully qualified name of global-system-config
        :param fq_name_str: Fully qualified name string of global-system-config
        :param id: UUID of global-system-config
        :param ifmap_id: IFMAP id of global-system-config
        :returns: :class:`.GlobalSystemConfig` object
        
        """
        (args_ok, result) = self._read_args_to_id('global-system-config', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.GlobalSystemConfig.resource_uri_base['global-system-config'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['global-system-config']
        global_system_config_obj = pycontrail.gen.resource_client.GlobalSystemConfig.from_dict(**obj_dict)
        global_system_config_obj.clear_pending_updates()
        global_system_config_obj.set_server_conn(self)

        return global_system_config_obj
    #end global_system_config_read

    def global_system_config_update(self, obj):
        """Update global-system-config.
        
        :param obj: :class:`.GlobalSystemConfig` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('global-system-config', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"global-system-config":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.GlobalSystemConfig.resource_uri_base['global-system-config'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('global-system-config', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('global-system-config', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end global_system_config_update

    def global_system_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all global-system-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalSystemConfig` objects
        
        """
        return self.resource_list('global-system-config', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end global_system_configs_list

    def global_system_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-system-config from the system.
        
        :param fq_name: Fully qualified name of global-system-config
        :param id: UUID of global-system-config
        :param ifmap_id: IFMAP id of global-system-config
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'global-system-config', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.GlobalSystemConfig.resource_uri_base['global-system-config'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end global_system_config_delete

    def get_default_global_system_config_id(self):
        """Return UUID of default global-system-config."""
        return self.fq_name_to_id('global-system-config', pycontrail.gen.resource_client.GlobalSystemConfig().get_fq_name())
    #end get_default_global_system_config_delete

    def service_appliance_create(self, obj):
        """Create new service-appliance.
        
        :param obj: :class:`.ServiceAppliance` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-appliance":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.ServiceAppliance.create_uri,
                       data = json_body)

        service_appliance_dict = json.loads(content)['service-appliance']
        obj.uuid = service_appliance_dict['uuid']
        if 'parent_uuid' in service_appliance_dict:
            obj.parent_uuid = service_appliance_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end service_appliance_create

    def service_appliance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return service-appliance information.
        
        :param fq_name: Fully qualified name of service-appliance
        :param fq_name_str: Fully qualified name string of service-appliance
        :param id: UUID of service-appliance
        :param ifmap_id: IFMAP id of service-appliance
        :returns: :class:`.ServiceAppliance` object
        
        """
        (args_ok, result) = self._read_args_to_id('service-appliance', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceAppliance.resource_uri_base['service-appliance'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['service-appliance']
        service_appliance_obj = pycontrail.gen.resource_client.ServiceAppliance.from_dict(**obj_dict)
        service_appliance_obj.clear_pending_updates()
        service_appliance_obj.set_server_conn(self)

        return service_appliance_obj
    #end service_appliance_read

    def service_appliance_update(self, obj):
        """Update service-appliance.
        
        :param obj: :class:`.ServiceAppliance` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('service-appliance', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-appliance":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.ServiceAppliance.resource_uri_base['service-appliance'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('service-appliance', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('service-appliance', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end service_appliance_update

    def service_appliances_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all service-appliances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceAppliance` objects
        
        """
        return self.resource_list('service-appliance', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end service_appliances_list

    def service_appliance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-appliance from the system.
        
        :param fq_name: Fully qualified name of service-appliance
        :param id: UUID of service-appliance
        :param ifmap_id: IFMAP id of service-appliance
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'service-appliance', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceAppliance.resource_uri_base['service-appliance'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end service_appliance_delete

    def get_default_service_appliance_id(self):
        """Return UUID of default service-appliance."""
        return self.fq_name_to_id('service-appliance', pycontrail.gen.resource_client.ServiceAppliance().get_fq_name())
    #end get_default_service_appliance_delete

    def service_instance_create(self, obj):
        """Create new service-instance.
        
        :param obj: :class:`.ServiceInstance` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-instance":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.ServiceInstance.create_uri,
                       data = json_body)

        service_instance_dict = json.loads(content)['service-instance']
        obj.uuid = service_instance_dict['uuid']
        if 'parent_uuid' in service_instance_dict:
            obj.parent_uuid = service_instance_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end service_instance_create

    def service_instance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return service-instance information.
        
        :param fq_name: Fully qualified name of service-instance
        :param fq_name_str: Fully qualified name string of service-instance
        :param id: UUID of service-instance
        :param ifmap_id: IFMAP id of service-instance
        :returns: :class:`.ServiceInstance` object
        
        """
        (args_ok, result) = self._read_args_to_id('service-instance', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceInstance.resource_uri_base['service-instance'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['service-instance']
        service_instance_obj = pycontrail.gen.resource_client.ServiceInstance.from_dict(**obj_dict)
        service_instance_obj.clear_pending_updates()
        service_instance_obj.set_server_conn(self)

        return service_instance_obj
    #end service_instance_read

    def service_instance_update(self, obj):
        """Update service-instance.
        
        :param obj: :class:`.ServiceInstance` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('service-instance', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-instance":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.ServiceInstance.resource_uri_base['service-instance'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('service-instance', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('service-instance', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end service_instance_update

    def service_instances_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all service-instances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceInstance` objects
        
        """
        return self.resource_list('service-instance', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end service_instances_list

    def service_instance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-instance from the system.
        
        :param fq_name: Fully qualified name of service-instance
        :param id: UUID of service-instance
        :param ifmap_id: IFMAP id of service-instance
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'service-instance', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceInstance.resource_uri_base['service-instance'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end service_instance_delete

    def get_default_service_instance_id(self):
        """Return UUID of default service-instance."""
        return self.fq_name_to_id('service-instance', pycontrail.gen.resource_client.ServiceInstance().get_fq_name())
    #end get_default_service_instance_delete

    def namespace_create(self, obj):
        """Create new namespace.
        
        :param obj: :class:`.Namespace` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"namespace":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.Namespace.create_uri,
                       data = json_body)

        namespace_dict = json.loads(content)['namespace']
        obj.uuid = namespace_dict['uuid']
        if 'parent_uuid' in namespace_dict:
            obj.parent_uuid = namespace_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end namespace_create

    def namespace_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return namespace information.
        
        :param fq_name: Fully qualified name of namespace
        :param fq_name_str: Fully qualified name string of namespace
        :param id: UUID of namespace
        :param ifmap_id: IFMAP id of namespace
        :returns: :class:`.Namespace` object
        
        """
        (args_ok, result) = self._read_args_to_id('namespace', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Namespace.resource_uri_base['namespace'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['namespace']
        namespace_obj = pycontrail.gen.resource_client.Namespace.from_dict(**obj_dict)
        namespace_obj.clear_pending_updates()
        namespace_obj.set_server_conn(self)

        return namespace_obj
    #end namespace_read

    def namespace_update(self, obj):
        """Update namespace.
        
        :param obj: :class:`.Namespace` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('namespace', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"namespace":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.Namespace.resource_uri_base['namespace'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('namespace', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('namespace', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end namespace_update

    def namespaces_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all namespaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Namespace` objects
        
        """
        return self.resource_list('namespace', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end namespaces_list

    def namespace_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete namespace from the system.
        
        :param fq_name: Fully qualified name of namespace
        :param id: UUID of namespace
        :param ifmap_id: IFMAP id of namespace
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'namespace', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Namespace.resource_uri_base['namespace'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end namespace_delete

    def get_default_namespace_id(self):
        """Return UUID of default namespace."""
        return self.fq_name_to_id('namespace', pycontrail.gen.resource_client.Namespace().get_fq_name())
    #end get_default_namespace_delete

    def logical_interface_create(self, obj):
        """Create new logical-interface.
        
        :param obj: :class:`.LogicalInterface` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"logical-interface":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.LogicalInterface.create_uri,
                       data = json_body)

        logical_interface_dict = json.loads(content)['logical-interface']
        obj.uuid = logical_interface_dict['uuid']
        if 'parent_uuid' in logical_interface_dict:
            obj.parent_uuid = logical_interface_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end logical_interface_create

    def logical_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return logical-interface information.
        
        :param fq_name: Fully qualified name of logical-interface
        :param fq_name_str: Fully qualified name string of logical-interface
        :param id: UUID of logical-interface
        :param ifmap_id: IFMAP id of logical-interface
        :returns: :class:`.LogicalInterface` object
        
        """
        (args_ok, result) = self._read_args_to_id('logical-interface', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LogicalInterface.resource_uri_base['logical-interface'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['logical-interface']
        logical_interface_obj = pycontrail.gen.resource_client.LogicalInterface.from_dict(**obj_dict)
        logical_interface_obj.clear_pending_updates()
        logical_interface_obj.set_server_conn(self)

        return logical_interface_obj
    #end logical_interface_read

    def logical_interface_update(self, obj):
        """Update logical-interface.
        
        :param obj: :class:`.LogicalInterface` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('logical-interface', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"logical-interface":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.LogicalInterface.resource_uri_base['logical-interface'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('logical-interface', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('logical-interface', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end logical_interface_update

    def logical_interfaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all logical-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LogicalInterface` objects
        
        """
        return self.resource_list('logical-interface', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end logical_interfaces_list

    def logical_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete logical-interface from the system.
        
        :param fq_name: Fully qualified name of logical-interface
        :param id: UUID of logical-interface
        :param ifmap_id: IFMAP id of logical-interface
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'logical-interface', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LogicalInterface.resource_uri_base['logical-interface'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end logical_interface_delete

    def get_default_logical_interface_id(self):
        """Return UUID of default logical-interface."""
        return self.fq_name_to_id('logical-interface', pycontrail.gen.resource_client.LogicalInterface().get_fq_name())
    #end get_default_logical_interface_delete

    def route_table_create(self, obj):
        """Create new route-table.
        
        :param obj: :class:`.RouteTable` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"route-table":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.RouteTable.create_uri,
                       data = json_body)

        route_table_dict = json.loads(content)['route-table']
        obj.uuid = route_table_dict['uuid']
        if 'parent_uuid' in route_table_dict:
            obj.parent_uuid = route_table_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end route_table_create

    def route_table_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return route-table information.
        
        :param fq_name: Fully qualified name of route-table
        :param fq_name_str: Fully qualified name string of route-table
        :param id: UUID of route-table
        :param ifmap_id: IFMAP id of route-table
        :returns: :class:`.RouteTable` object
        
        """
        (args_ok, result) = self._read_args_to_id('route-table', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.RouteTable.resource_uri_base['route-table'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['route-table']
        route_table_obj = pycontrail.gen.resource_client.RouteTable.from_dict(**obj_dict)
        route_table_obj.clear_pending_updates()
        route_table_obj.set_server_conn(self)

        return route_table_obj
    #end route_table_read

    def route_table_update(self, obj):
        """Update route-table.
        
        :param obj: :class:`.RouteTable` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('route-table', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"route-table":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.RouteTable.resource_uri_base['route-table'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('route-table', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('route-table', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end route_table_update

    def route_tables_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all route-tables.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RouteTable` objects
        
        """
        return self.resource_list('route-table', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end route_tables_list

    def route_table_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete route-table from the system.
        
        :param fq_name: Fully qualified name of route-table
        :param id: UUID of route-table
        :param ifmap_id: IFMAP id of route-table
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'route-table', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.RouteTable.resource_uri_base['route-table'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end route_table_delete

    def get_default_route_table_id(self):
        """Return UUID of default route-table."""
        return self.fq_name_to_id('route-table', pycontrail.gen.resource_client.RouteTable().get_fq_name())
    #end get_default_route_table_delete

    def physical_interface_create(self, obj):
        """Create new physical-interface.
        
        :param obj: :class:`.PhysicalInterface` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"physical-interface":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.PhysicalInterface.create_uri,
                       data = json_body)

        physical_interface_dict = json.loads(content)['physical-interface']
        obj.uuid = physical_interface_dict['uuid']
        if 'parent_uuid' in physical_interface_dict:
            obj.parent_uuid = physical_interface_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end physical_interface_create

    def physical_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return physical-interface information.
        
        :param fq_name: Fully qualified name of physical-interface
        :param fq_name_str: Fully qualified name string of physical-interface
        :param id: UUID of physical-interface
        :param ifmap_id: IFMAP id of physical-interface
        :returns: :class:`.PhysicalInterface` object
        
        """
        (args_ok, result) = self._read_args_to_id('physical-interface', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.PhysicalInterface.resource_uri_base['physical-interface'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['physical-interface']
        physical_interface_obj = pycontrail.gen.resource_client.PhysicalInterface.from_dict(**obj_dict)
        physical_interface_obj.clear_pending_updates()
        physical_interface_obj.set_server_conn(self)

        return physical_interface_obj
    #end physical_interface_read

    def physical_interface_update(self, obj):
        """Update physical-interface.
        
        :param obj: :class:`.PhysicalInterface` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('physical-interface', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"physical-interface":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.PhysicalInterface.resource_uri_base['physical-interface'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('physical-interface', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('physical-interface', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end physical_interface_update

    def physical_interfaces_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all physical-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PhysicalInterface` objects
        
        """
        return self.resource_list('physical-interface', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end physical_interfaces_list

    def physical_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete physical-interface from the system.
        
        :param fq_name: Fully qualified name of physical-interface
        :param id: UUID of physical-interface
        :param ifmap_id: IFMAP id of physical-interface
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'physical-interface', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.PhysicalInterface.resource_uri_base['physical-interface'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end physical_interface_delete

    def get_default_physical_interface_id(self):
        """Return UUID of default physical-interface."""
        return self.fq_name_to_id('physical-interface', pycontrail.gen.resource_client.PhysicalInterface().get_fq_name())
    #end get_default_physical_interface_delete

    def access_control_list_create(self, obj):
        """Create new access-control-list.
        
        :param obj: :class:`.AccessControlList` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"access-control-list":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.AccessControlList.create_uri,
                       data = json_body)

        access_control_list_dict = json.loads(content)['access-control-list']
        obj.uuid = access_control_list_dict['uuid']
        if 'parent_uuid' in access_control_list_dict:
            obj.parent_uuid = access_control_list_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end access_control_list_create

    def access_control_list_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return access-control-list information.
        
        :param fq_name: Fully qualified name of access-control-list
        :param fq_name_str: Fully qualified name string of access-control-list
        :param id: UUID of access-control-list
        :param ifmap_id: IFMAP id of access-control-list
        :returns: :class:`.AccessControlList` object
        
        """
        (args_ok, result) = self._read_args_to_id('access-control-list', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.AccessControlList.resource_uri_base['access-control-list'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['access-control-list']
        access_control_list_obj = pycontrail.gen.resource_client.AccessControlList.from_dict(**obj_dict)
        access_control_list_obj.clear_pending_updates()
        access_control_list_obj.set_server_conn(self)

        return access_control_list_obj
    #end access_control_list_read

    def access_control_list_update(self, obj):
        """Update access-control-list.
        
        :param obj: :class:`.AccessControlList` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('access-control-list', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"access-control-list":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.AccessControlList.resource_uri_base['access-control-list'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('access-control-list', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('access-control-list', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end access_control_list_update

    def access_control_lists_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all access-control-lists.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AccessControlList` objects
        
        """
        return self.resource_list('access-control-list', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end access_control_lists_list

    def access_control_list_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete access-control-list from the system.
        
        :param fq_name: Fully qualified name of access-control-list
        :param id: UUID of access-control-list
        :param ifmap_id: IFMAP id of access-control-list
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'access-control-list', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.AccessControlList.resource_uri_base['access-control-list'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end access_control_list_delete

    def get_default_access_control_list_id(self):
        """Return UUID of default access-control-list."""
        return self.fq_name_to_id('access-control-list', pycontrail.gen.resource_client.AccessControlList().get_fq_name())
    #end get_default_access_control_list_delete

    def analytics_node_create(self, obj):
        """Create new analytics-node.
        
        :param obj: :class:`.AnalyticsNode` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"analytics-node":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.AnalyticsNode.create_uri,
                       data = json_body)

        analytics_node_dict = json.loads(content)['analytics-node']
        obj.uuid = analytics_node_dict['uuid']
        if 'parent_uuid' in analytics_node_dict:
            obj.parent_uuid = analytics_node_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end analytics_node_create

    def analytics_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return analytics-node information.
        
        :param fq_name: Fully qualified name of analytics-node
        :param fq_name_str: Fully qualified name string of analytics-node
        :param id: UUID of analytics-node
        :param ifmap_id: IFMAP id of analytics-node
        :returns: :class:`.AnalyticsNode` object
        
        """
        (args_ok, result) = self._read_args_to_id('analytics-node', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.AnalyticsNode.resource_uri_base['analytics-node'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['analytics-node']
        analytics_node_obj = pycontrail.gen.resource_client.AnalyticsNode.from_dict(**obj_dict)
        analytics_node_obj.clear_pending_updates()
        analytics_node_obj.set_server_conn(self)

        return analytics_node_obj
    #end analytics_node_read

    def analytics_node_update(self, obj):
        """Update analytics-node.
        
        :param obj: :class:`.AnalyticsNode` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('analytics-node', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"analytics-node":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.AnalyticsNode.resource_uri_base['analytics-node'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('analytics-node', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('analytics-node', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end analytics_node_update

    def analytics_nodes_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all analytics-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AnalyticsNode` objects
        
        """
        return self.resource_list('analytics-node', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end analytics_nodes_list

    def analytics_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete analytics-node from the system.
        
        :param fq_name: Fully qualified name of analytics-node
        :param id: UUID of analytics-node
        :param ifmap_id: IFMAP id of analytics-node
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'analytics-node', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.AnalyticsNode.resource_uri_base['analytics-node'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end analytics_node_delete

    def get_default_analytics_node_id(self):
        """Return UUID of default analytics-node."""
        return self.fq_name_to_id('analytics-node', pycontrail.gen.resource_client.AnalyticsNode().get_fq_name())
    #end get_default_analytics_node_delete

    def virtual_DNS_create(self, obj):
        """Create new virtual-DNS.
        
        :param obj: :class:`.VirtualDns` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-DNS":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.VirtualDns.create_uri,
                       data = json_body)

        virtual_DNS_dict = json.loads(content)['virtual-DNS']
        obj.uuid = virtual_DNS_dict['uuid']
        if 'parent_uuid' in virtual_DNS_dict:
            obj.parent_uuid = virtual_DNS_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end virtual_DNS_create

    def virtual_DNS_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return virtual-DNS information.
        
        :param fq_name: Fully qualified name of virtual-DNS
        :param fq_name_str: Fully qualified name string of virtual-DNS
        :param id: UUID of virtual-DNS
        :param ifmap_id: IFMAP id of virtual-DNS
        :returns: :class:`.VirtualDns` object
        
        """
        (args_ok, result) = self._read_args_to_id('virtual-DNS', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualDns.resource_uri_base['virtual-DNS'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['virtual-DNS']
        virtual_DNS_obj = pycontrail.gen.resource_client.VirtualDns.from_dict(**obj_dict)
        virtual_DNS_obj.clear_pending_updates()
        virtual_DNS_obj.set_server_conn(self)

        return virtual_DNS_obj
    #end virtual_DNS_read

    def virtual_DNS_update(self, obj):
        """Update virtual-DNS.
        
        :param obj: :class:`.VirtualDns` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('virtual-DNS', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-DNS":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.VirtualDns.resource_uri_base['virtual-DNS'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('virtual-DNS', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('virtual-DNS', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end virtual_DNS_update

    def virtual_DNSs_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all virtual-DNSs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualDns` objects
        
        """
        return self.resource_list('virtual-DNS', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end virtual_DNSs_list

    def virtual_DNS_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-DNS from the system.
        
        :param fq_name: Fully qualified name of virtual-DNS
        :param id: UUID of virtual-DNS
        :param ifmap_id: IFMAP id of virtual-DNS
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'virtual-DNS', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualDns.resource_uri_base['virtual-DNS'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end virtual_DNS_delete

    def get_default_virtual_DNS_id(self):
        """Return UUID of default virtual-DNS."""
        return self.fq_name_to_id('virtual-DNS', pycontrail.gen.resource_client.VirtualDns().get_fq_name())
    #end get_default_virtual_DNS_delete

    def customer_attachment_create(self, obj):
        """Create new customer-attachment.
        
        :param obj: :class:`.CustomerAttachment` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"customer-attachment":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.CustomerAttachment.create_uri,
                       data = json_body)

        customer_attachment_dict = json.loads(content)['customer-attachment']
        obj.uuid = customer_attachment_dict['uuid']
        if 'parent_uuid' in customer_attachment_dict:
            obj.parent_uuid = customer_attachment_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end customer_attachment_create

    def customer_attachment_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return customer-attachment information.
        
        :param fq_name: Fully qualified name of customer-attachment
        :param fq_name_str: Fully qualified name string of customer-attachment
        :param id: UUID of customer-attachment
        :param ifmap_id: IFMAP id of customer-attachment
        :returns: :class:`.CustomerAttachment` object
        
        """
        (args_ok, result) = self._read_args_to_id('customer-attachment', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.CustomerAttachment.resource_uri_base['customer-attachment'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['customer-attachment']
        customer_attachment_obj = pycontrail.gen.resource_client.CustomerAttachment.from_dict(**obj_dict)
        customer_attachment_obj.clear_pending_updates()
        customer_attachment_obj.set_server_conn(self)

        return customer_attachment_obj
    #end customer_attachment_read

    def customer_attachment_update(self, obj):
        """Update customer-attachment.
        
        :param obj: :class:`.CustomerAttachment` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('customer-attachment', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"customer-attachment":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.CustomerAttachment.resource_uri_base['customer-attachment'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('customer-attachment', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('customer-attachment', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end customer_attachment_update

    def customer_attachments_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all customer-attachments."""
        return self.resource_list('customer-attachment', back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end customer_attachments_list

    def customer_attachment_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete customer-attachment from the system.
        
        :param fq_name: Fully qualified name of customer-attachment
        :param id: UUID of customer-attachment
        :param ifmap_id: IFMAP id of customer-attachment
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'customer-attachment', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.CustomerAttachment.resource_uri_base['customer-attachment'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end customer_attachment_delete

    def get_default_customer_attachment_id(self):
        """Return UUID of default customer-attachment."""
        return self.fq_name_to_id('customer-attachment', pycontrail.gen.resource_client.CustomerAttachment().get_fq_name())
    #end get_default_customer_attachment_delete

    def service_appliance_set_create(self, obj):
        """Create new service-appliance-set.
        
        :param obj: :class:`.ServiceApplianceSet` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-appliance-set":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.ServiceApplianceSet.create_uri,
                       data = json_body)

        service_appliance_set_dict = json.loads(content)['service-appliance-set']
        obj.uuid = service_appliance_set_dict['uuid']
        if 'parent_uuid' in service_appliance_set_dict:
            obj.parent_uuid = service_appliance_set_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end service_appliance_set_create

    def service_appliance_set_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return service-appliance-set information.
        
        :param fq_name: Fully qualified name of service-appliance-set
        :param fq_name_str: Fully qualified name string of service-appliance-set
        :param id: UUID of service-appliance-set
        :param ifmap_id: IFMAP id of service-appliance-set
        :returns: :class:`.ServiceApplianceSet` object
        
        """
        (args_ok, result) = self._read_args_to_id('service-appliance-set', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceApplianceSet.resource_uri_base['service-appliance-set'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['service-appliance-set']
        service_appliance_set_obj = pycontrail.gen.resource_client.ServiceApplianceSet.from_dict(**obj_dict)
        service_appliance_set_obj.clear_pending_updates()
        service_appliance_set_obj.set_server_conn(self)

        return service_appliance_set_obj
    #end service_appliance_set_read

    def service_appliance_set_update(self, obj):
        """Update service-appliance-set.
        
        :param obj: :class:`.ServiceApplianceSet` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('service-appliance-set', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-appliance-set":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.ServiceApplianceSet.resource_uri_base['service-appliance-set'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('service-appliance-set', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('service-appliance-set', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end service_appliance_set_update

    def service_appliance_sets_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all service-appliance-sets.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceApplianceSet` objects
        
        """
        return self.resource_list('service-appliance-set', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end service_appliance_sets_list

    def service_appliance_set_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-appliance-set from the system.
        
        :param fq_name: Fully qualified name of service-appliance-set
        :param id: UUID of service-appliance-set
        :param ifmap_id: IFMAP id of service-appliance-set
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'service-appliance-set', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceApplianceSet.resource_uri_base['service-appliance-set'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end service_appliance_set_delete

    def get_default_service_appliance_set_id(self):
        """Return UUID of default service-appliance-set."""
        return self.fq_name_to_id('service-appliance-set', pycontrail.gen.resource_client.ServiceApplianceSet().get_fq_name())
    #end get_default_service_appliance_set_delete

    def config_node_create(self, obj):
        """Create new config-node.
        
        :param obj: :class:`.ConfigNode` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"config-node":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.ConfigNode.create_uri,
                       data = json_body)

        config_node_dict = json.loads(content)['config-node']
        obj.uuid = config_node_dict['uuid']
        if 'parent_uuid' in config_node_dict:
            obj.parent_uuid = config_node_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end config_node_create

    def config_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return config-node information.
        
        :param fq_name: Fully qualified name of config-node
        :param fq_name_str: Fully qualified name string of config-node
        :param id: UUID of config-node
        :param ifmap_id: IFMAP id of config-node
        :returns: :class:`.ConfigNode` object
        
        """
        (args_ok, result) = self._read_args_to_id('config-node', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ConfigNode.resource_uri_base['config-node'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['config-node']
        config_node_obj = pycontrail.gen.resource_client.ConfigNode.from_dict(**obj_dict)
        config_node_obj.clear_pending_updates()
        config_node_obj.set_server_conn(self)

        return config_node_obj
    #end config_node_read

    def config_node_update(self, obj):
        """Update config-node.
        
        :param obj: :class:`.ConfigNode` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('config-node', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"config-node":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.ConfigNode.resource_uri_base['config-node'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('config-node', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('config-node', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end config_node_update

    def config_nodes_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all config-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ConfigNode` objects
        
        """
        return self.resource_list('config-node', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end config_nodes_list

    def config_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete config-node from the system.
        
        :param fq_name: Fully qualified name of config-node
        :param id: UUID of config-node
        :param ifmap_id: IFMAP id of config-node
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'config-node', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ConfigNode.resource_uri_base['config-node'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end config_node_delete

    def get_default_config_node_id(self):
        """Return UUID of default config-node."""
        return self.fq_name_to_id('config-node', pycontrail.gen.resource_client.ConfigNode().get_fq_name())
    #end get_default_config_node_delete

    def qos_queue_create(self, obj):
        """Create new qos-queue.
        
        :param obj: :class:`.QosQueue` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"qos-queue":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.QosQueue.create_uri,
                       data = json_body)

        qos_queue_dict = json.loads(content)['qos-queue']
        obj.uuid = qos_queue_dict['uuid']
        if 'parent_uuid' in qos_queue_dict:
            obj.parent_uuid = qos_queue_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end qos_queue_create

    def qos_queue_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return qos-queue information.
        
        :param fq_name: Fully qualified name of qos-queue
        :param fq_name_str: Fully qualified name string of qos-queue
        :param id: UUID of qos-queue
        :param ifmap_id: IFMAP id of qos-queue
        :returns: :class:`.QosQueue` object
        
        """
        (args_ok, result) = self._read_args_to_id('qos-queue', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.QosQueue.resource_uri_base['qos-queue'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['qos-queue']
        qos_queue_obj = pycontrail.gen.resource_client.QosQueue.from_dict(**obj_dict)
        qos_queue_obj.clear_pending_updates()
        qos_queue_obj.set_server_conn(self)

        return qos_queue_obj
    #end qos_queue_read

    def qos_queue_update(self, obj):
        """Update qos-queue.
        
        :param obj: :class:`.QosQueue` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('qos-queue', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"qos-queue":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.QosQueue.resource_uri_base['qos-queue'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('qos-queue', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('qos-queue', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end qos_queue_update

    def qos_queues_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all qos-queues.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.QosQueue` objects
        
        """
        return self.resource_list('qos-queue', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end qos_queues_list

    def qos_queue_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete qos-queue from the system.
        
        :param fq_name: Fully qualified name of qos-queue
        :param id: UUID of qos-queue
        :param ifmap_id: IFMAP id of qos-queue
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'qos-queue', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.QosQueue.resource_uri_base['qos-queue'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end qos_queue_delete

    def get_default_qos_queue_id(self):
        """Return UUID of default qos-queue."""
        return self.fq_name_to_id('qos-queue', pycontrail.gen.resource_client.QosQueue().get_fq_name())
    #end get_default_qos_queue_delete

    def virtual_machine_create(self, obj):
        """Create new virtual-machine.
        
        :param obj: :class:`.VirtualMachine` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-machine":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.VirtualMachine.create_uri,
                       data = json_body)

        virtual_machine_dict = json.loads(content)['virtual-machine']
        obj.uuid = virtual_machine_dict['uuid']
        if 'parent_uuid' in virtual_machine_dict:
            obj.parent_uuid = virtual_machine_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end virtual_machine_create

    def virtual_machine_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return virtual-machine information.
        
        :param fq_name: Fully qualified name of virtual-machine
        :param fq_name_str: Fully qualified name string of virtual-machine
        :param id: UUID of virtual-machine
        :param ifmap_id: IFMAP id of virtual-machine
        :returns: :class:`.VirtualMachine` object
        
        """
        (args_ok, result) = self._read_args_to_id('virtual-machine', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualMachine.resource_uri_base['virtual-machine'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['virtual-machine']
        virtual_machine_obj = pycontrail.gen.resource_client.VirtualMachine.from_dict(**obj_dict)
        virtual_machine_obj.clear_pending_updates()
        virtual_machine_obj.set_server_conn(self)

        return virtual_machine_obj
    #end virtual_machine_read

    def virtual_machine_update(self, obj):
        """Update virtual-machine.
        
        :param obj: :class:`.VirtualMachine` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('virtual-machine', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-machine":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.VirtualMachine.resource_uri_base['virtual-machine'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('virtual-machine', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('virtual-machine', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end virtual_machine_update

    def virtual_machines_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all virtual-machines."""
        return self.resource_list('virtual-machine', back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end virtual_machines_list

    def virtual_machine_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-machine from the system.
        
        :param fq_name: Fully qualified name of virtual-machine
        :param id: UUID of virtual-machine
        :param ifmap_id: IFMAP id of virtual-machine
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'virtual-machine', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualMachine.resource_uri_base['virtual-machine'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end virtual_machine_delete

    def get_default_virtual_machine_id(self):
        """Return UUID of default virtual-machine."""
        return self.fq_name_to_id('virtual-machine', pycontrail.gen.resource_client.VirtualMachine().get_fq_name())
    #end get_default_virtual_machine_delete

    def interface_route_table_create(self, obj):
        """Create new interface-route-table.
        
        :param obj: :class:`.InterfaceRouteTable` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"interface-route-table":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.InterfaceRouteTable.create_uri,
                       data = json_body)

        interface_route_table_dict = json.loads(content)['interface-route-table']
        obj.uuid = interface_route_table_dict['uuid']
        if 'parent_uuid' in interface_route_table_dict:
            obj.parent_uuid = interface_route_table_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end interface_route_table_create

    def interface_route_table_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return interface-route-table information.
        
        :param fq_name: Fully qualified name of interface-route-table
        :param fq_name_str: Fully qualified name string of interface-route-table
        :param id: UUID of interface-route-table
        :param ifmap_id: IFMAP id of interface-route-table
        :returns: :class:`.InterfaceRouteTable` object
        
        """
        (args_ok, result) = self._read_args_to_id('interface-route-table', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.InterfaceRouteTable.resource_uri_base['interface-route-table'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['interface-route-table']
        interface_route_table_obj = pycontrail.gen.resource_client.InterfaceRouteTable.from_dict(**obj_dict)
        interface_route_table_obj.clear_pending_updates()
        interface_route_table_obj.set_server_conn(self)

        return interface_route_table_obj
    #end interface_route_table_read

    def interface_route_table_update(self, obj):
        """Update interface-route-table.
        
        :param obj: :class:`.InterfaceRouteTable` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('interface-route-table', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"interface-route-table":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.InterfaceRouteTable.resource_uri_base['interface-route-table'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('interface-route-table', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('interface-route-table', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end interface_route_table_update

    def interface_route_tables_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all interface-route-tables.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.InterfaceRouteTable` objects
        
        """
        return self.resource_list('interface-route-table', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end interface_route_tables_list

    def interface_route_table_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete interface-route-table from the system.
        
        :param fq_name: Fully qualified name of interface-route-table
        :param id: UUID of interface-route-table
        :param ifmap_id: IFMAP id of interface-route-table
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'interface-route-table', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.InterfaceRouteTable.resource_uri_base['interface-route-table'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end interface_route_table_delete

    def get_default_interface_route_table_id(self):
        """Return UUID of default interface-route-table."""
        return self.fq_name_to_id('interface-route-table', pycontrail.gen.resource_client.InterfaceRouteTable().get_fq_name())
    #end get_default_interface_route_table_delete

    def service_template_create(self, obj):
        """Create new service-template.
        
        :param obj: :class:`.ServiceTemplate` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-template":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.ServiceTemplate.create_uri,
                       data = json_body)

        service_template_dict = json.loads(content)['service-template']
        obj.uuid = service_template_dict['uuid']
        if 'parent_uuid' in service_template_dict:
            obj.parent_uuid = service_template_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end service_template_create

    def service_template_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return service-template information.
        
        :param fq_name: Fully qualified name of service-template
        :param fq_name_str: Fully qualified name string of service-template
        :param id: UUID of service-template
        :param ifmap_id: IFMAP id of service-template
        :returns: :class:`.ServiceTemplate` object
        
        """
        (args_ok, result) = self._read_args_to_id('service-template', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceTemplate.resource_uri_base['service-template'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['service-template']
        service_template_obj = pycontrail.gen.resource_client.ServiceTemplate.from_dict(**obj_dict)
        service_template_obj.clear_pending_updates()
        service_template_obj.set_server_conn(self)

        return service_template_obj
    #end service_template_read

    def service_template_update(self, obj):
        """Update service-template.
        
        :param obj: :class:`.ServiceTemplate` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('service-template', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"service-template":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.ServiceTemplate.resource_uri_base['service-template'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('service-template', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('service-template', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end service_template_update

    def service_templates_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all service-templates.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceTemplate` objects
        
        """
        return self.resource_list('service-template', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end service_templates_list

    def service_template_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-template from the system.
        
        :param fq_name: Fully qualified name of service-template
        :param id: UUID of service-template
        :param ifmap_id: IFMAP id of service-template
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'service-template', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ServiceTemplate.resource_uri_base['service-template'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end service_template_delete

    def get_default_service_template_id(self):
        """Return UUID of default service-template."""
        return self.fq_name_to_id('service-template', pycontrail.gen.resource_client.ServiceTemplate().get_fq_name())
    #end get_default_service_template_delete

    def virtual_ip_create(self, obj):
        """Create new virtual-ip.
        
        :param obj: :class:`.VirtualIp` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-ip":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.VirtualIp.create_uri,
                       data = json_body)

        virtual_ip_dict = json.loads(content)['virtual-ip']
        obj.uuid = virtual_ip_dict['uuid']
        if 'parent_uuid' in virtual_ip_dict:
            obj.parent_uuid = virtual_ip_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end virtual_ip_create

    def virtual_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return virtual-ip information.
        
        :param fq_name: Fully qualified name of virtual-ip
        :param fq_name_str: Fully qualified name string of virtual-ip
        :param id: UUID of virtual-ip
        :param ifmap_id: IFMAP id of virtual-ip
        :returns: :class:`.VirtualIp` object
        
        """
        (args_ok, result) = self._read_args_to_id('virtual-ip', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualIp.resource_uri_base['virtual-ip'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['virtual-ip']
        virtual_ip_obj = pycontrail.gen.resource_client.VirtualIp.from_dict(**obj_dict)
        virtual_ip_obj.clear_pending_updates()
        virtual_ip_obj.set_server_conn(self)

        return virtual_ip_obj
    #end virtual_ip_read

    def virtual_ip_update(self, obj):
        """Update virtual-ip.
        
        :param obj: :class:`.VirtualIp` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('virtual-ip', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-ip":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.VirtualIp.resource_uri_base['virtual-ip'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('virtual-ip', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('virtual-ip', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end virtual_ip_update

    def virtual_ips_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all virtual-ips.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualIp` objects
        
        """
        return self.resource_list('virtual-ip', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end virtual_ips_list

    def virtual_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-ip from the system.
        
        :param fq_name: Fully qualified name of virtual-ip
        :param id: UUID of virtual-ip
        :param ifmap_id: IFMAP id of virtual-ip
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'virtual-ip', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualIp.resource_uri_base['virtual-ip'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end virtual_ip_delete

    def get_default_virtual_ip_id(self):
        """Return UUID of default virtual-ip."""
        return self.fq_name_to_id('virtual-ip', pycontrail.gen.resource_client.VirtualIp().get_fq_name())
    #end get_default_virtual_ip_delete

    def loadbalancer_member_create(self, obj):
        """Create new loadbalancer-member.
        
        :param obj: :class:`.LoadbalancerMember` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"loadbalancer-member":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.LoadbalancerMember.create_uri,
                       data = json_body)

        loadbalancer_member_dict = json.loads(content)['loadbalancer-member']
        obj.uuid = loadbalancer_member_dict['uuid']
        if 'parent_uuid' in loadbalancer_member_dict:
            obj.parent_uuid = loadbalancer_member_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end loadbalancer_member_create

    def loadbalancer_member_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return loadbalancer-member information.
        
        :param fq_name: Fully qualified name of loadbalancer-member
        :param fq_name_str: Fully qualified name string of loadbalancer-member
        :param id: UUID of loadbalancer-member
        :param ifmap_id: IFMAP id of loadbalancer-member
        :returns: :class:`.LoadbalancerMember` object
        
        """
        (args_ok, result) = self._read_args_to_id('loadbalancer-member', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LoadbalancerMember.resource_uri_base['loadbalancer-member'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['loadbalancer-member']
        loadbalancer_member_obj = pycontrail.gen.resource_client.LoadbalancerMember.from_dict(**obj_dict)
        loadbalancer_member_obj.clear_pending_updates()
        loadbalancer_member_obj.set_server_conn(self)

        return loadbalancer_member_obj
    #end loadbalancer_member_read

    def loadbalancer_member_update(self, obj):
        """Update loadbalancer-member.
        
        :param obj: :class:`.LoadbalancerMember` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('loadbalancer-member', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"loadbalancer-member":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.LoadbalancerMember.resource_uri_base['loadbalancer-member'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('loadbalancer-member', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('loadbalancer-member', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end loadbalancer_member_update

    def loadbalancer_members_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all loadbalancer-members.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerMember` objects
        
        """
        return self.resource_list('loadbalancer-member', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end loadbalancer_members_list

    def loadbalancer_member_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-member from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-member
        :param id: UUID of loadbalancer-member
        :param ifmap_id: IFMAP id of loadbalancer-member
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'loadbalancer-member', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LoadbalancerMember.resource_uri_base['loadbalancer-member'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end loadbalancer_member_delete

    def get_default_loadbalancer_member_id(self):
        """Return UUID of default loadbalancer-member."""
        return self.fq_name_to_id('loadbalancer-member', pycontrail.gen.resource_client.LoadbalancerMember().get_fq_name())
    #end get_default_loadbalancer_member_delete

    def security_group_create(self, obj):
        """Create new security-group.
        
        :param obj: :class:`.SecurityGroup` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"security-group":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.SecurityGroup.create_uri,
                       data = json_body)

        security_group_dict = json.loads(content)['security-group']
        obj.uuid = security_group_dict['uuid']
        if 'parent_uuid' in security_group_dict:
            obj.parent_uuid = security_group_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end security_group_create

    def security_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return security-group information.
        
        :param fq_name: Fully qualified name of security-group
        :param fq_name_str: Fully qualified name string of security-group
        :param id: UUID of security-group
        :param ifmap_id: IFMAP id of security-group
        :returns: :class:`.SecurityGroup` object
        
        """
        (args_ok, result) = self._read_args_to_id('security-group', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.SecurityGroup.resource_uri_base['security-group'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['security-group']
        security_group_obj = pycontrail.gen.resource_client.SecurityGroup.from_dict(**obj_dict)
        security_group_obj.clear_pending_updates()
        security_group_obj.set_server_conn(self)

        return security_group_obj
    #end security_group_read

    def security_group_update(self, obj):
        """Update security-group.
        
        :param obj: :class:`.SecurityGroup` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('security-group', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"security-group":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.SecurityGroup.resource_uri_base['security-group'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('security-group', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('security-group', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end security_group_update

    def security_groups_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all security-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.SecurityGroup` objects
        
        """
        return self.resource_list('security-group', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end security_groups_list

    def security_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete security-group from the system.
        
        :param fq_name: Fully qualified name of security-group
        :param id: UUID of security-group
        :param ifmap_id: IFMAP id of security-group
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'security-group', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.SecurityGroup.resource_uri_base['security-group'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end security_group_delete

    def get_default_security_group_id(self):
        """Return UUID of default security-group."""
        return self.fq_name_to_id('security-group', pycontrail.gen.resource_client.SecurityGroup().get_fq_name())
    #end get_default_security_group_delete

    def provider_attachment_create(self, obj):
        """Create new provider-attachment.
        
        :param obj: :class:`.ProviderAttachment` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"provider-attachment":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.ProviderAttachment.create_uri,
                       data = json_body)

        provider_attachment_dict = json.loads(content)['provider-attachment']
        obj.uuid = provider_attachment_dict['uuid']
        if 'parent_uuid' in provider_attachment_dict:
            obj.parent_uuid = provider_attachment_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end provider_attachment_create

    def provider_attachment_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return provider-attachment information.
        
        :param fq_name: Fully qualified name of provider-attachment
        :param fq_name_str: Fully qualified name string of provider-attachment
        :param id: UUID of provider-attachment
        :param ifmap_id: IFMAP id of provider-attachment
        :returns: :class:`.ProviderAttachment` object
        
        """
        (args_ok, result) = self._read_args_to_id('provider-attachment', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ProviderAttachment.resource_uri_base['provider-attachment'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['provider-attachment']
        provider_attachment_obj = pycontrail.gen.resource_client.ProviderAttachment.from_dict(**obj_dict)
        provider_attachment_obj.clear_pending_updates()
        provider_attachment_obj.set_server_conn(self)

        return provider_attachment_obj
    #end provider_attachment_read

    def provider_attachment_update(self, obj):
        """Update provider-attachment.
        
        :param obj: :class:`.ProviderAttachment` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('provider-attachment', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"provider-attachment":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.ProviderAttachment.resource_uri_base['provider-attachment'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('provider-attachment', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('provider-attachment', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end provider_attachment_update

    def provider_attachments_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all provider-attachments."""
        return self.resource_list('provider-attachment', back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end provider_attachments_list

    def provider_attachment_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete provider-attachment from the system.
        
        :param fq_name: Fully qualified name of provider-attachment
        :param id: UUID of provider-attachment
        :param ifmap_id: IFMAP id of provider-attachment
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'provider-attachment', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.ProviderAttachment.resource_uri_base['provider-attachment'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end provider_attachment_delete

    def get_default_provider_attachment_id(self):
        """Return UUID of default provider-attachment."""
        return self.fq_name_to_id('provider-attachment', pycontrail.gen.resource_client.ProviderAttachment().get_fq_name())
    #end get_default_provider_attachment_delete

    def virtual_machine_interface_create(self, obj):
        """Create new virtual-machine-interface.
        
        :param obj: :class:`.VirtualMachineInterface` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-machine-interface":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.VirtualMachineInterface.create_uri,
                       data = json_body)

        virtual_machine_interface_dict = json.loads(content)['virtual-machine-interface']
        obj.uuid = virtual_machine_interface_dict['uuid']
        if 'parent_uuid' in virtual_machine_interface_dict:
            obj.parent_uuid = virtual_machine_interface_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end virtual_machine_interface_create

    def virtual_machine_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return virtual-machine-interface information.
        
        :param fq_name: Fully qualified name of virtual-machine-interface
        :param fq_name_str: Fully qualified name string of virtual-machine-interface
        :param id: UUID of virtual-machine-interface
        :param ifmap_id: IFMAP id of virtual-machine-interface
        :returns: :class:`.VirtualMachineInterface` object
        
        """
        (args_ok, result) = self._read_args_to_id('virtual-machine-interface', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualMachineInterface.resource_uri_base['virtual-machine-interface'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['virtual-machine-interface']
        virtual_machine_interface_obj = pycontrail.gen.resource_client.VirtualMachineInterface.from_dict(**obj_dict)
        virtual_machine_interface_obj.clear_pending_updates()
        virtual_machine_interface_obj.set_server_conn(self)

        return virtual_machine_interface_obj
    #end virtual_machine_interface_read

    def virtual_machine_interface_update(self, obj):
        """Update virtual-machine-interface.
        
        :param obj: :class:`.VirtualMachineInterface` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('virtual-machine-interface', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-machine-interface":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.VirtualMachineInterface.resource_uri_base['virtual-machine-interface'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('virtual-machine-interface', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('virtual-machine-interface', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end virtual_machine_interface_update

    def virtual_machine_interfaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all virtual-machine-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualMachineInterface` objects
        
        """
        return self.resource_list('virtual-machine-interface', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end virtual_machine_interfaces_list

    def virtual_machine_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-machine-interface from the system.
        
        :param fq_name: Fully qualified name of virtual-machine-interface
        :param id: UUID of virtual-machine-interface
        :param ifmap_id: IFMAP id of virtual-machine-interface
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'virtual-machine-interface', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualMachineInterface.resource_uri_base['virtual-machine-interface'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end virtual_machine_interface_delete

    def get_default_virtual_machine_interface_id(self):
        """Return UUID of default virtual-machine-interface."""
        return self.fq_name_to_id('virtual-machine-interface', pycontrail.gen.resource_client.VirtualMachineInterface().get_fq_name())
    #end get_default_virtual_machine_interface_delete

    def loadbalancer_healthmonitor_create(self, obj):
        """Create new loadbalancer-healthmonitor.
        
        :param obj: :class:`.LoadbalancerHealthmonitor` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"loadbalancer-healthmonitor":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.LoadbalancerHealthmonitor.create_uri,
                       data = json_body)

        loadbalancer_healthmonitor_dict = json.loads(content)['loadbalancer-healthmonitor']
        obj.uuid = loadbalancer_healthmonitor_dict['uuid']
        if 'parent_uuid' in loadbalancer_healthmonitor_dict:
            obj.parent_uuid = loadbalancer_healthmonitor_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end loadbalancer_healthmonitor_create

    def loadbalancer_healthmonitor_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return loadbalancer-healthmonitor information.
        
        :param fq_name: Fully qualified name of loadbalancer-healthmonitor
        :param fq_name_str: Fully qualified name string of loadbalancer-healthmonitor
        :param id: UUID of loadbalancer-healthmonitor
        :param ifmap_id: IFMAP id of loadbalancer-healthmonitor
        :returns: :class:`.LoadbalancerHealthmonitor` object
        
        """
        (args_ok, result) = self._read_args_to_id('loadbalancer-healthmonitor', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LoadbalancerHealthmonitor.resource_uri_base['loadbalancer-healthmonitor'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['loadbalancer-healthmonitor']
        loadbalancer_healthmonitor_obj = pycontrail.gen.resource_client.LoadbalancerHealthmonitor.from_dict(**obj_dict)
        loadbalancer_healthmonitor_obj.clear_pending_updates()
        loadbalancer_healthmonitor_obj.set_server_conn(self)

        return loadbalancer_healthmonitor_obj
    #end loadbalancer_healthmonitor_read

    def loadbalancer_healthmonitor_update(self, obj):
        """Update loadbalancer-healthmonitor.
        
        :param obj: :class:`.LoadbalancerHealthmonitor` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('loadbalancer-healthmonitor', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"loadbalancer-healthmonitor":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.LoadbalancerHealthmonitor.resource_uri_base['loadbalancer-healthmonitor'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('loadbalancer-healthmonitor', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('loadbalancer-healthmonitor', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end loadbalancer_healthmonitor_update

    def loadbalancer_healthmonitors_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all loadbalancer-healthmonitors.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerHealthmonitor` objects
        
        """
        return self.resource_list('loadbalancer-healthmonitor', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end loadbalancer_healthmonitors_list

    def loadbalancer_healthmonitor_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-healthmonitor from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-healthmonitor
        :param id: UUID of loadbalancer-healthmonitor
        :param ifmap_id: IFMAP id of loadbalancer-healthmonitor
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'loadbalancer-healthmonitor', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LoadbalancerHealthmonitor.resource_uri_base['loadbalancer-healthmonitor'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end loadbalancer_healthmonitor_delete

    def get_default_loadbalancer_healthmonitor_id(self):
        """Return UUID of default loadbalancer-healthmonitor."""
        return self.fq_name_to_id('loadbalancer-healthmonitor', pycontrail.gen.resource_client.LoadbalancerHealthmonitor().get_fq_name())
    #end get_default_loadbalancer_healthmonitor_delete

    def virtual_network_create(self, obj):
        """Create new virtual-network.
        
        :param obj: :class:`.VirtualNetwork` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-network":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.VirtualNetwork.create_uri,
                       data = json_body)

        virtual_network_dict = json.loads(content)['virtual-network']
        obj.uuid = virtual_network_dict['uuid']
        if 'parent_uuid' in virtual_network_dict:
            obj.parent_uuid = virtual_network_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end virtual_network_create

    def virtual_network_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return virtual-network information.
        
        :param fq_name: Fully qualified name of virtual-network
        :param fq_name_str: Fully qualified name string of virtual-network
        :param id: UUID of virtual-network
        :param ifmap_id: IFMAP id of virtual-network
        :returns: :class:`.VirtualNetwork` object
        
        """
        (args_ok, result) = self._read_args_to_id('virtual-network', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualNetwork.resource_uri_base['virtual-network'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['virtual-network']
        virtual_network_obj = pycontrail.gen.resource_client.VirtualNetwork.from_dict(**obj_dict)
        virtual_network_obj.clear_pending_updates()
        virtual_network_obj.set_server_conn(self)

        return virtual_network_obj
    #end virtual_network_read

    def virtual_network_update(self, obj):
        """Update virtual-network.
        
        :param obj: :class:`.VirtualNetwork` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('virtual-network', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"virtual-network":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.VirtualNetwork.resource_uri_base['virtual-network'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('virtual-network', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('virtual-network', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end virtual_network_update

    def virtual_networks_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all virtual-networks.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualNetwork` objects
        
        """
        return self.resource_list('virtual-network', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end virtual_networks_list

    def virtual_network_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-network from the system.
        
        :param fq_name: Fully qualified name of virtual-network
        :param id: UUID of virtual-network
        :param ifmap_id: IFMAP id of virtual-network
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'virtual-network', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.VirtualNetwork.resource_uri_base['virtual-network'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end virtual_network_delete

    def get_default_virtual_network_id(self):
        """Return UUID of default virtual-network."""
        return self.fq_name_to_id('virtual-network', pycontrail.gen.resource_client.VirtualNetwork().get_fq_name())
    #end get_default_virtual_network_delete

    def project_create(self, obj):
        """Create new project.
        
        :param obj: :class:`.Project` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"project":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.Project.create_uri,
                       data = json_body)

        project_dict = json.loads(content)['project']
        obj.uuid = project_dict['uuid']
        if 'parent_uuid' in project_dict:
            obj.parent_uuid = project_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end project_create

    def project_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return project information.
        
        :param fq_name: Fully qualified name of project
        :param fq_name_str: Fully qualified name string of project
        :param id: UUID of project
        :param ifmap_id: IFMAP id of project
        :returns: :class:`.Project` object
        
        """
        (args_ok, result) = self._read_args_to_id('project', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Project.resource_uri_base['project'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['project']
        project_obj = pycontrail.gen.resource_client.Project.from_dict(**obj_dict)
        project_obj.clear_pending_updates()
        project_obj.set_server_conn(self)

        return project_obj
    #end project_read

    def project_update(self, obj):
        """Update project.
        
        :param obj: :class:`.Project` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('project', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"project":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.Project.resource_uri_base['project'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('project', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('project', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end project_update

    def projects_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all projects.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Project` objects
        
        """
        return self.resource_list('project', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end projects_list

    def project_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete project from the system.
        
        :param fq_name: Fully qualified name of project
        :param id: UUID of project
        :param ifmap_id: IFMAP id of project
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'project', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.Project.resource_uri_base['project'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end project_delete

    def get_default_project_id(self):
        """Return UUID of default project."""
        return self.fq_name_to_id('project', pycontrail.gen.resource_client.Project().get_fq_name())
    #end get_default_project_delete

    def qos_forwarding_class_create(self, obj):
        """Create new qos-forwarding-class.
        
        :param obj: :class:`.QosForwardingClass` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"qos-forwarding-class":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.QosForwardingClass.create_uri,
                       data = json_body)

        qos_forwarding_class_dict = json.loads(content)['qos-forwarding-class']
        obj.uuid = qos_forwarding_class_dict['uuid']
        if 'parent_uuid' in qos_forwarding_class_dict:
            obj.parent_uuid = qos_forwarding_class_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end qos_forwarding_class_create

    def qos_forwarding_class_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return qos-forwarding-class information.
        
        :param fq_name: Fully qualified name of qos-forwarding-class
        :param fq_name_str: Fully qualified name string of qos-forwarding-class
        :param id: UUID of qos-forwarding-class
        :param ifmap_id: IFMAP id of qos-forwarding-class
        :returns: :class:`.QosForwardingClass` object
        
        """
        (args_ok, result) = self._read_args_to_id('qos-forwarding-class', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.QosForwardingClass.resource_uri_base['qos-forwarding-class'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['qos-forwarding-class']
        qos_forwarding_class_obj = pycontrail.gen.resource_client.QosForwardingClass.from_dict(**obj_dict)
        qos_forwarding_class_obj.clear_pending_updates()
        qos_forwarding_class_obj.set_server_conn(self)

        return qos_forwarding_class_obj
    #end qos_forwarding_class_read

    def qos_forwarding_class_update(self, obj):
        """Update qos-forwarding-class.
        
        :param obj: :class:`.QosForwardingClass` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('qos-forwarding-class', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"qos-forwarding-class":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.QosForwardingClass.resource_uri_base['qos-forwarding-class'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('qos-forwarding-class', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('qos-forwarding-class', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end qos_forwarding_class_update

    def qos_forwarding_classs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all qos-forwarding-classs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.QosForwardingClass` objects
        
        """
        return self.resource_list('qos-forwarding-class', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end qos_forwarding_classs_list

    def qos_forwarding_class_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete qos-forwarding-class from the system.
        
        :param fq_name: Fully qualified name of qos-forwarding-class
        :param id: UUID of qos-forwarding-class
        :param ifmap_id: IFMAP id of qos-forwarding-class
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'qos-forwarding-class', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.QosForwardingClass.resource_uri_base['qos-forwarding-class'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end qos_forwarding_class_delete

    def get_default_qos_forwarding_class_id(self):
        """Return UUID of default qos-forwarding-class."""
        return self.fq_name_to_id('qos-forwarding-class', pycontrail.gen.resource_client.QosForwardingClass().get_fq_name())
    #end get_default_qos_forwarding_class_delete

    def database_node_create(self, obj):
        """Create new database-node.
        
        :param obj: :class:`.DatabaseNode` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"database-node":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.DatabaseNode.create_uri,
                       data = json_body)

        database_node_dict = json.loads(content)['database-node']
        obj.uuid = database_node_dict['uuid']
        if 'parent_uuid' in database_node_dict:
            obj.parent_uuid = database_node_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end database_node_create

    def database_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return database-node information.
        
        :param fq_name: Fully qualified name of database-node
        :param fq_name_str: Fully qualified name string of database-node
        :param id: UUID of database-node
        :param ifmap_id: IFMAP id of database-node
        :returns: :class:`.DatabaseNode` object
        
        """
        (args_ok, result) = self._read_args_to_id('database-node', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.DatabaseNode.resource_uri_base['database-node'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['database-node']
        database_node_obj = pycontrail.gen.resource_client.DatabaseNode.from_dict(**obj_dict)
        database_node_obj.clear_pending_updates()
        database_node_obj.set_server_conn(self)

        return database_node_obj
    #end database_node_read

    def database_node_update(self, obj):
        """Update database-node.
        
        :param obj: :class:`.DatabaseNode` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('database-node', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"database-node":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.DatabaseNode.resource_uri_base['database-node'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('database-node', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('database-node', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end database_node_update

    def database_nodes_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all database-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DatabaseNode` objects
        
        """
        return self.resource_list('database-node', parent_id = parent_id, parent_fq_name = parent_fq_name, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end database_nodes_list

    def database_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete database-node from the system.
        
        :param fq_name: Fully qualified name of database-node
        :param id: UUID of database-node
        :param ifmap_id: IFMAP id of database-node
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'database-node', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.DatabaseNode.resource_uri_base['database-node'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end database_node_delete

    def get_default_database_node_id(self):
        """Return UUID of default database-node."""
        return self.fq_name_to_id('database-node', pycontrail.gen.resource_client.DatabaseNode().get_fq_name())
    #end get_default_database_node_delete

    def routing_instance_create(self, obj):
        """Create new routing-instance.
        
        :param obj: :class:`.RoutingInstance` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"routing-instance":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.RoutingInstance.create_uri,
                       data = json_body)

        routing_instance_dict = json.loads(content)['routing-instance']
        obj.uuid = routing_instance_dict['uuid']
        if 'parent_uuid' in routing_instance_dict:
            obj.parent_uuid = routing_instance_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end routing_instance_create

    def routing_instance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return routing-instance information.
        
        :param fq_name: Fully qualified name of routing-instance
        :param fq_name_str: Fully qualified name string of routing-instance
        :param id: UUID of routing-instance
        :param ifmap_id: IFMAP id of routing-instance
        :returns: :class:`.RoutingInstance` object
        
        """
        (args_ok, result) = self._read_args_to_id('routing-instance', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.RoutingInstance.resource_uri_base['routing-instance'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['routing-instance']
        routing_instance_obj = pycontrail.gen.resource_client.RoutingInstance.from_dict(**obj_dict)
        routing_instance_obj.clear_pending_updates()
        routing_instance_obj.set_server_conn(self)

        return routing_instance_obj
    #end routing_instance_read

    def routing_instance_update(self, obj):
        """Update routing-instance.
        
        :param obj: :class:`.RoutingInstance` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('routing-instance', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"routing-instance":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.RoutingInstance.resource_uri_base['routing-instance'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('routing-instance', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('routing-instance', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end routing_instance_update

    def routing_instances_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all routing-instances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RoutingInstance` objects
        
        """
        return self.resource_list('routing-instance', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end routing_instances_list

    def routing_instance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete routing-instance from the system.
        
        :param fq_name: Fully qualified name of routing-instance
        :param id: UUID of routing-instance
        :param ifmap_id: IFMAP id of routing-instance
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'routing-instance', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.RoutingInstance.resource_uri_base['routing-instance'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end routing_instance_delete

    def get_default_routing_instance_id(self):
        """Return UUID of default routing-instance."""
        return self.fq_name_to_id('routing-instance', pycontrail.gen.resource_client.RoutingInstance().get_fq_name())
    #end get_default_routing_instance_delete

    def network_ipam_create(self, obj):
        """Create new network-ipam.
        
        :param obj: :class:`.NetworkIpam` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"network-ipam":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.NetworkIpam.create_uri,
                       data = json_body)

        network_ipam_dict = json.loads(content)['network-ipam']
        obj.uuid = network_ipam_dict['uuid']
        if 'parent_uuid' in network_ipam_dict:
            obj.parent_uuid = network_ipam_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end network_ipam_create

    def network_ipam_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return network-ipam information.
        
        :param fq_name: Fully qualified name of network-ipam
        :param fq_name_str: Fully qualified name string of network-ipam
        :param id: UUID of network-ipam
        :param ifmap_id: IFMAP id of network-ipam
        :returns: :class:`.NetworkIpam` object
        
        """
        (args_ok, result) = self._read_args_to_id('network-ipam', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.NetworkIpam.resource_uri_base['network-ipam'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['network-ipam']
        network_ipam_obj = pycontrail.gen.resource_client.NetworkIpam.from_dict(**obj_dict)
        network_ipam_obj.clear_pending_updates()
        network_ipam_obj.set_server_conn(self)

        return network_ipam_obj
    #end network_ipam_read

    def network_ipam_update(self, obj):
        """Update network-ipam.
        
        :param obj: :class:`.NetworkIpam` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('network-ipam', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"network-ipam":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.NetworkIpam.resource_uri_base['network-ipam'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('network-ipam', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('network-ipam', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end network_ipam_update

    def network_ipams_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all network-ipams.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.NetworkIpam` objects
        
        """
        return self.resource_list('network-ipam', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end network_ipams_list

    def network_ipam_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete network-ipam from the system.
        
        :param fq_name: Fully qualified name of network-ipam
        :param id: UUID of network-ipam
        :param ifmap_id: IFMAP id of network-ipam
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'network-ipam', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.NetworkIpam.resource_uri_base['network-ipam'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end network_ipam_delete

    def get_default_network_ipam_id(self):
        """Return UUID of default network-ipam."""
        return self.fq_name_to_id('network-ipam', pycontrail.gen.resource_client.NetworkIpam().get_fq_name())
    #end get_default_network_ipam_delete

    def logical_router_create(self, obj):
        """Create new logical-router.
        
        :param obj: :class:`.LogicalRouter` object
        
        """
        obj._pending_field_updates |= obj._pending_ref_updates
        obj._pending_ref_updates = set([])
        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"logical-router":' + json_param + '}'
        content = self._request_server(rest.OP_POST,
                       pycontrail.gen.resource_client.LogicalRouter.create_uri,
                       data = json_body)

        logical_router_dict = json.loads(content)['logical-router']
        obj.uuid = logical_router_dict['uuid']
        if 'parent_uuid' in logical_router_dict:
            obj.parent_uuid = logical_router_dict['parent_uuid']

        obj.set_server_conn(self)

        return obj.uuid
    #end logical_router_create

    def logical_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None, fields = None):
        """Return logical-router information.
        
        :param fq_name: Fully qualified name of logical-router
        :param fq_name_str: Fully qualified name string of logical-router
        :param id: UUID of logical-router
        :param ifmap_id: IFMAP id of logical-router
        :returns: :class:`.LogicalRouter` object
        
        """
        (args_ok, result) = self._read_args_to_id('logical-router', fq_name, fq_name_str, id, ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LogicalRouter.resource_uri_base['logical-router'] + '/' + id

        if fields:
            comma_sep_fields = ','.join(f for f in fields)
            query_params = {'fields': comma_sep_fields}
        else:
            query_params = {'exclude_back_refs':True,
                            'exclude_children':True,}
        content = self._request_server(rest.OP_GET, uri, query_params)

        obj_dict = json.loads(content)['logical-router']
        logical_router_obj = pycontrail.gen.resource_client.LogicalRouter.from_dict(**obj_dict)
        logical_router_obj.clear_pending_updates()
        logical_router_obj.set_server_conn(self)

        return logical_router_obj
    #end logical_router_read

    def logical_router_update(self, obj):
        """Update logical-router.
        
        :param obj: :class:`.LogicalRouter` object
        
        """
        # Read in uuid from api-server if not specified in obj
        if not obj.uuid:
            obj.uuid = self.fq_name_to_id('logical-router', obj.get_fq_name())

        # Ignore fields with None value in json representation
        json_param = json.dumps(obj, default = self._obj_serializer)
        json_body = '{"logical-router":' + json_param + '}'

        id = obj.uuid
        uri = pycontrail.gen.resource_client.LogicalRouter.resource_uri_base['logical-router'] + '/' + id
        content = self._request_server(rest.OP_PUT, uri, data = json_body)
        for ref_name in obj._pending_ref_updates:
             ref_orig = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, '_original_' + ref_name, [])])
             ref_new = set([(x.get('uuid'), tuple(x.get('to', [])), x.get('attr')) for x in getattr(obj, ref_name, [])])
             for ref in ref_orig - ref_new:
                 self.ref_update('logical-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'DELETE')
             for ref in ref_new - ref_orig:
                 self.ref_update('logical-router', obj.uuid, ref_name, ref[0], list(ref[1]), 'ADD', ref[2])
        obj.clear_pending_updates()

        return content
    #end logical_router_update

    def logical_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False, filters = None):
        """List all logical-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LogicalRouter` objects
        
        """
        return self.resource_list('logical-router', parent_id = parent_id, parent_fq_name = parent_fq_name, back_ref_id = back_ref_id, obj_uuids=obj_uuids, fields=fields, detail=detail, count=count, filters=filters)
    #end logical_routers_list

    def logical_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete logical-router from the system.
        
        :param fq_name: Fully qualified name of logical-router
        :param id: UUID of logical-router
        :param ifmap_id: IFMAP id of logical-router
        
        """
        (args_ok, result) = self._read_args_to_id(obj_type = 'logical-router', fq_name = fq_name, id = id, ifmap_id = ifmap_id)
        if not args_ok:
            return result

        id = result
        uri = pycontrail.gen.resource_client.LogicalRouter.resource_uri_base['logical-router'] + '/' + id

        content = self._request_server(rest.OP_DELETE, uri)
    #end logical_router_delete

    def get_default_logical_router_id(self):
        """Return UUID of default logical-router."""
        return self.fq_name_to_id('logical-router', pycontrail.gen.resource_client.LogicalRouter().get_fq_name())
    #end get_default_logical_router_delete

#end class VncApiClientGen

    prop_name_to_xsd_type = {
        
        }

ConnectionDriverBase.register (VncApiClientGen)
