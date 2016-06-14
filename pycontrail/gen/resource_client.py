
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

import pycontrail.gen.resource_common
import pycontrail.gen.resource_xsd


class Domain(pycontrail.gen.resource_common.Domain):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, domain_limits=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if domain_limits is not None:
            pending_fields.append('domain_limits')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(Domain, self).__init__(name, parent_obj, domain_limits, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'domain_limits' in kwargs:
            if kwargs['domain_limits'] is None:
                props_dict['domain_limits'] = None
            else:
                props_dict['domain_limits'] = pycontrail.gen.resource_xsd.DomainLimitsType(**kwargs['domain_limits'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = Domain(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'projects' in kwargs:
            obj.projects = kwargs['projects']
        if 'namespaces' in kwargs:
            obj.namespaces = kwargs['namespaces']
        if 'service_templates' in kwargs:
            obj.service_templates = kwargs['service_templates']
        if 'virtual_DNSs' in kwargs:
            obj.virtual_DNSs = kwargs['virtual_DNSs']
        if 'api_access_lists' in kwargs:
            obj.api_access_lists = kwargs['api_access_lists']

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.Domain.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.Domain.domain_limits.setter
    def domain_limits(self, domain_limits):
        """Set domain-limits for domain.
        
        :param domain_limits: DomainLimitsType object
        
        """
        if 'domain_limits' not in self._pending_field_updates:
            self._pending_field_updates.add('domain_limits')

        self._domain_limits = domain_limits
    #end domain_limits

    def set_domain_limits(self, value):
        self.domain_limits = value
    #end set_domain_limits

    @pycontrail.gen.resource_common.Domain.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for domain.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.Domain.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for domain.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.Domain.display_name.setter
    def display_name(self, display_name):
        """Set display-name for domain.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_projects(self):
        children = super(Domain, self).get_projects()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.domain_read(id = self.uuid, fields = ['projects'])
            children = getattr(obj, 'projects', None)
            self.projects = children

        return children
    #end get_projects

    def get_namespaces(self):
        children = super(Domain, self).get_namespaces()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.domain_read(id = self.uuid, fields = ['namespaces'])
            children = getattr(obj, 'namespaces', None)
            self.namespaces = children

        return children
    #end get_namespaces

    def get_service_templates(self):
        children = super(Domain, self).get_service_templates()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.domain_read(id = self.uuid, fields = ['service_templates'])
            children = getattr(obj, 'service_templates', None)
            self.service_templates = children

        return children
    #end get_service_templates

    def get_virtual_DNSs(self):
        children = super(Domain, self).get_virtual_DNSs()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.domain_read(id = self.uuid, fields = ['virtual_DNSs'])
            children = getattr(obj, 'virtual_DNSs', None)
            self.virtual_DNSs = children

        return children
    #end get_virtual_DNSs

    def get_api_access_lists(self):
        children = super(Domain, self).get_api_access_lists()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.domain_read(id = self.uuid, fields = ['api_access_lists'])
            children = getattr(obj, 'api_access_lists', None)
            self.api_access_lists = children

        return children
    #end get_api_access_lists


#end class Domain

class GlobalVrouterConfig(pycontrail.gen.resource_common.GlobalVrouterConfig):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, ecmp_hashing_include_fields=None, linklocal_services=None, encapsulation_priorities=None, vxlan_network_identifier_mode=None, flow_export_rate=None, flow_aging_timeout_list=None, forwarding_mode=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if ecmp_hashing_include_fields is not None:
            pending_fields.append('ecmp_hashing_include_fields')
        if linklocal_services is not None:
            pending_fields.append('linklocal_services')
        if encapsulation_priorities is not None:
            pending_fields.append('encapsulation_priorities')
        if vxlan_network_identifier_mode is not None:
            pending_fields.append('vxlan_network_identifier_mode')
        if flow_export_rate is not None:
            pending_fields.append('flow_export_rate')
        if flow_aging_timeout_list is not None:
            pending_fields.append('flow_aging_timeout_list')
        if forwarding_mode is not None:
            pending_fields.append('forwarding_mode')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(GlobalVrouterConfig, self).__init__(name, parent_obj, ecmp_hashing_include_fields, linklocal_services, encapsulation_priorities, vxlan_network_identifier_mode, flow_export_rate, flow_aging_timeout_list, forwarding_mode, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'ecmp_hashing_include_fields' in kwargs:
            if kwargs['ecmp_hashing_include_fields'] is None:
                props_dict['ecmp_hashing_include_fields'] = None
            else:
                props_dict['ecmp_hashing_include_fields'] = pycontrail.gen.resource_xsd.EcmpHashingIncludeFields(**kwargs['ecmp_hashing_include_fields'])
        if 'linklocal_services' in kwargs:
            if kwargs['linklocal_services'] is None:
                props_dict['linklocal_services'] = None
            else:
                props_dict['linklocal_services'] = pycontrail.gen.resource_xsd.LinklocalServicesTypes(**kwargs['linklocal_services'])
        if 'encapsulation_priorities' in kwargs:
            if kwargs['encapsulation_priorities'] is None:
                props_dict['encapsulation_priorities'] = None
            else:
                props_dict['encapsulation_priorities'] = pycontrail.gen.resource_xsd.EncapsulationPrioritiesType(**kwargs['encapsulation_priorities'])
        if 'vxlan_network_identifier_mode' in kwargs:
            props_dict['vxlan_network_identifier_mode'] = kwargs['vxlan_network_identifier_mode']
        if 'flow_export_rate' in kwargs:
            props_dict['flow_export_rate'] = kwargs['flow_export_rate']
        if 'flow_aging_timeout_list' in kwargs:
            if kwargs['flow_aging_timeout_list'] is None:
                props_dict['flow_aging_timeout_list'] = None
            else:
                props_dict['flow_aging_timeout_list'] = pycontrail.gen.resource_xsd.FlowAgingTimeoutList(**kwargs['flow_aging_timeout_list'])
        if 'forwarding_mode' in kwargs:
            props_dict['forwarding_mode'] = kwargs['forwarding_mode']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = GlobalVrouterConfig(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.GlobalVrouterConfig.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.GlobalVrouterConfig.ecmp_hashing_include_fields.setter
    def ecmp_hashing_include_fields(self, ecmp_hashing_include_fields):
        """Set ecmp-hashing-include-fields for global-vrouter-config.
        
        :param ecmp_hashing_include_fields: EcmpHashingIncludeFields object
        
        """
        if 'ecmp_hashing_include_fields' not in self._pending_field_updates:
            self._pending_field_updates.add('ecmp_hashing_include_fields')

        self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
    #end ecmp_hashing_include_fields

    def set_ecmp_hashing_include_fields(self, value):
        self.ecmp_hashing_include_fields = value
    #end set_ecmp_hashing_include_fields

    @pycontrail.gen.resource_common.GlobalVrouterConfig.linklocal_services.setter
    def linklocal_services(self, linklocal_services):
        """Set linklocal-services for global-vrouter-config.
        
        :param linklocal_services: LinklocalServicesTypes object
        
        """
        if 'linklocal_services' not in self._pending_field_updates:
            self._pending_field_updates.add('linklocal_services')

        self._linklocal_services = linklocal_services
    #end linklocal_services

    def set_linklocal_services(self, value):
        self.linklocal_services = value
    #end set_linklocal_services

    @pycontrail.gen.resource_common.GlobalVrouterConfig.encapsulation_priorities.setter
    def encapsulation_priorities(self, encapsulation_priorities):
        """Set encapsulation-priorities for global-vrouter-config.
        
        :param encapsulation_priorities: EncapsulationPrioritiesType object
        
        """
        if 'encapsulation_priorities' not in self._pending_field_updates:
            self._pending_field_updates.add('encapsulation_priorities')

        self._encapsulation_priorities = encapsulation_priorities
    #end encapsulation_priorities

    def set_encapsulation_priorities(self, value):
        self.encapsulation_priorities = value
    #end set_encapsulation_priorities

    @pycontrail.gen.resource_common.GlobalVrouterConfig.vxlan_network_identifier_mode.setter
    def vxlan_network_identifier_mode(self, vxlan_network_identifier_mode):
        """Set vxlan-network-identifier-mode for global-vrouter-config.
        
        :param vxlan_network_identifier_mode: VxlanNetworkIdentifierModeType object
        
        """
        if 'vxlan_network_identifier_mode' not in self._pending_field_updates:
            self._pending_field_updates.add('vxlan_network_identifier_mode')

        self._vxlan_network_identifier_mode = vxlan_network_identifier_mode
    #end vxlan_network_identifier_mode

    def set_vxlan_network_identifier_mode(self, value):
        self.vxlan_network_identifier_mode = value
    #end set_vxlan_network_identifier_mode

    @pycontrail.gen.resource_common.GlobalVrouterConfig.flow_export_rate.setter
    def flow_export_rate(self, flow_export_rate):
        """Set flow-export-rate for global-vrouter-config.
        
        :param flow_export_rate: xsd:integer object
        
        """
        if 'flow_export_rate' not in self._pending_field_updates:
            self._pending_field_updates.add('flow_export_rate')

        self._flow_export_rate = flow_export_rate
    #end flow_export_rate

    def set_flow_export_rate(self, value):
        self.flow_export_rate = value
    #end set_flow_export_rate

    @pycontrail.gen.resource_common.GlobalVrouterConfig.flow_aging_timeout_list.setter
    def flow_aging_timeout_list(self, flow_aging_timeout_list):
        """Set flow-aging-timeout-list for global-vrouter-config.
        
        :param flow_aging_timeout_list: FlowAgingTimeoutList object
        
        """
        if 'flow_aging_timeout_list' not in self._pending_field_updates:
            self._pending_field_updates.add('flow_aging_timeout_list')

        self._flow_aging_timeout_list = flow_aging_timeout_list
    #end flow_aging_timeout_list

    def set_flow_aging_timeout_list(self, value):
        self.flow_aging_timeout_list = value
    #end set_flow_aging_timeout_list

    @pycontrail.gen.resource_common.GlobalVrouterConfig.forwarding_mode.setter
    def forwarding_mode(self, forwarding_mode):
        """Set forwarding-mode for global-vrouter-config.
        
        :param forwarding_mode: ForwardingModeType object
        
        """
        if 'forwarding_mode' not in self._pending_field_updates:
            self._pending_field_updates.add('forwarding_mode')

        self._forwarding_mode = forwarding_mode
    #end forwarding_mode

    def set_forwarding_mode(self, value):
        self.forwarding_mode = value
    #end set_forwarding_mode

    @pycontrail.gen.resource_common.GlobalVrouterConfig.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for global-vrouter-config.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.GlobalVrouterConfig.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for global-vrouter-config.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.GlobalVrouterConfig.display_name.setter
    def display_name(self, display_name):
        """Set display-name for global-vrouter-config.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class GlobalVrouterConfig

class InstanceIp(pycontrail.gen.resource_common.InstanceIp):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, instance_ip_address=None, instance_ip_family=None, instance_ip_mode=None, secondary_ip_tracking_ip=None, subnet_uuid=None, instance_ip_secondary=False, service_instance_ip=False, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if instance_ip_address is not None:
            pending_fields.append('instance_ip_address')
        if instance_ip_family is not None:
            pending_fields.append('instance_ip_family')
        if instance_ip_mode is not None:
            pending_fields.append('instance_ip_mode')
        if secondary_ip_tracking_ip is not None:
            pending_fields.append('secondary_ip_tracking_ip')
        if subnet_uuid is not None:
            pending_fields.append('subnet_uuid')
        if instance_ip_secondary is not None:
            pending_fields.append('instance_ip_secondary')
        if service_instance_ip is not None:
            pending_fields.append('service_instance_ip')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(InstanceIp, self).__init__(name, instance_ip_address, instance_ip_family, instance_ip_mode, secondary_ip_tracking_ip, subnet_uuid, instance_ip_secondary, service_instance_ip, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'instance_ip_address' in kwargs:
            props_dict['instance_ip_address'] = kwargs['instance_ip_address']
        if 'instance_ip_family' in kwargs:
            props_dict['instance_ip_family'] = kwargs['instance_ip_family']
        if 'instance_ip_mode' in kwargs:
            props_dict['instance_ip_mode'] = kwargs['instance_ip_mode']
        if 'secondary_ip_tracking_ip' in kwargs:
            if kwargs['secondary_ip_tracking_ip'] is None:
                props_dict['secondary_ip_tracking_ip'] = None
            else:
                props_dict['secondary_ip_tracking_ip'] = pycontrail.gen.resource_xsd.SubnetType(**kwargs['secondary_ip_tracking_ip'])
        if 'subnet_uuid' in kwargs:
            props_dict['subnet_uuid'] = kwargs['subnet_uuid']
        if 'instance_ip_secondary' in kwargs:
            props_dict['instance_ip_secondary'] = kwargs['instance_ip_secondary']
        if 'service_instance_ip' in kwargs:
            props_dict['service_instance_ip'] = kwargs['service_instance_ip']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = InstanceIp(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_network_refs' in kwargs:
            obj.virtual_network_refs = kwargs['virtual_network_refs']
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']
        if 'physical_router_refs' in kwargs:
            obj.physical_router_refs = kwargs['physical_router_refs']

        # and back references but no obj api for it...
        if 'service_instance_back_refs' in kwargs:
            obj.service_instance_back_refs = kwargs['service_instance_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.InstanceIp.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.InstanceIp.instance_ip_address.setter
    def instance_ip_address(self, instance_ip_address):
        """Set instance-ip-address for instance-ip.
        
        :param instance_ip_address: IpAddressType object
        
        """
        if 'instance_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('instance_ip_address')

        self._instance_ip_address = instance_ip_address
    #end instance_ip_address

    def set_instance_ip_address(self, value):
        self.instance_ip_address = value
    #end set_instance_ip_address

    @pycontrail.gen.resource_common.InstanceIp.instance_ip_family.setter
    def instance_ip_family(self, instance_ip_family):
        """Set instance-ip-family for instance-ip.
        
        :param instance_ip_family: IpAddressFamilyType object
        
        """
        if 'instance_ip_family' not in self._pending_field_updates:
            self._pending_field_updates.add('instance_ip_family')

        self._instance_ip_family = instance_ip_family
    #end instance_ip_family

    def set_instance_ip_family(self, value):
        self.instance_ip_family = value
    #end set_instance_ip_family

    @pycontrail.gen.resource_common.InstanceIp.instance_ip_mode.setter
    def instance_ip_mode(self, instance_ip_mode):
        """Set instance-ip-mode for instance-ip.
        
        :param instance_ip_mode: AddressMode object
        
        """
        if 'instance_ip_mode' not in self._pending_field_updates:
            self._pending_field_updates.add('instance_ip_mode')

        self._instance_ip_mode = instance_ip_mode
    #end instance_ip_mode

    def set_instance_ip_mode(self, value):
        self.instance_ip_mode = value
    #end set_instance_ip_mode

    @pycontrail.gen.resource_common.InstanceIp.secondary_ip_tracking_ip.setter
    def secondary_ip_tracking_ip(self, secondary_ip_tracking_ip):
        """Set secondary-ip-tracking-ip for instance-ip.
        
        :param secondary_ip_tracking_ip: SubnetType object
        
        """
        if 'secondary_ip_tracking_ip' not in self._pending_field_updates:
            self._pending_field_updates.add('secondary_ip_tracking_ip')

        self._secondary_ip_tracking_ip = secondary_ip_tracking_ip
    #end secondary_ip_tracking_ip

    def set_secondary_ip_tracking_ip(self, value):
        self.secondary_ip_tracking_ip = value
    #end set_secondary_ip_tracking_ip

    @pycontrail.gen.resource_common.InstanceIp.subnet_uuid.setter
    def subnet_uuid(self, subnet_uuid):
        """Set subnet-uuid for instance-ip.
        
        :param subnet_uuid: xsd:string object
        
        """
        if 'subnet_uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('subnet_uuid')

        self._subnet_uuid = subnet_uuid
    #end subnet_uuid

    def set_subnet_uuid(self, value):
        self.subnet_uuid = value
    #end set_subnet_uuid

    @pycontrail.gen.resource_common.InstanceIp.instance_ip_secondary.setter
    def instance_ip_secondary(self, instance_ip_secondary):
        """Set instance-ip-secondary for instance-ip.
        
        :param instance_ip_secondary: xsd:boolean object
        
        """
        if 'instance_ip_secondary' not in self._pending_field_updates:
            self._pending_field_updates.add('instance_ip_secondary')

        self._instance_ip_secondary = instance_ip_secondary
    #end instance_ip_secondary

    def set_instance_ip_secondary(self, value):
        self.instance_ip_secondary = value
    #end set_instance_ip_secondary

    @pycontrail.gen.resource_common.InstanceIp.service_instance_ip.setter
    def service_instance_ip(self, service_instance_ip):
        """Set service-instance-ip for instance-ip.
        
        :param service_instance_ip: xsd:boolean object
        
        """
        if 'service_instance_ip' not in self._pending_field_updates:
            self._pending_field_updates.add('service_instance_ip')

        self._service_instance_ip = service_instance_ip
    #end service_instance_ip

    def set_service_instance_ip(self, value):
        self.service_instance_ip = value
    #end set_service_instance_ip

    @pycontrail.gen.resource_common.InstanceIp.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for instance-ip.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.InstanceIp.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for instance-ip.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.InstanceIp.display_name.setter
    def display_name(self, display_name):
        """Set display-name for instance-ip.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_network(self, *args, **kwargs):
        """Set virtual-network for instance-ip.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(InstanceIp, self).set_virtual_network(*args, **kwargs)

    #end set_virtual_network

    def add_virtual_network(self, *args, **kwargs):
        """Add virtual-network to instance-ip.
        
        :param ref_obj: VirtualNetwork object
        
        """
        if 'virtual_network_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(InstanceIp, self).add_virtual_network(*args, **kwargs)
    #end add_virtual_network

    def del_virtual_network(self, *args, **kwargs):
        if 'virtual_network_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(InstanceIp, self).del_virtual_network(*args, **kwargs)
    #end del_virtual_network

    def set_virtual_network_list(self, *args, **kwargs):
        """Set virtual-network list for instance-ip.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(InstanceIp, self).set_virtual_network_list(*args, **kwargs)
    #end set_virtual_network_list

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for instance-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(InstanceIp, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to instance-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(InstanceIp, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(InstanceIp, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for instance-ip.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(InstanceIp, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list

    def set_physical_router(self, *args, **kwargs):
        """Set physical-router for instance-ip.
        
        :param ref_obj: PhysicalRouter object
        
        """
        self._pending_field_updates.add('physical_router_refs')
        self._pending_ref_updates.discard('physical_router_refs')
        super(InstanceIp, self).set_physical_router(*args, **kwargs)

    #end set_physical_router

    def add_physical_router(self, *args, **kwargs):
        """Add physical-router to instance-ip.
        
        :param ref_obj: PhysicalRouter object
        
        """
        if 'physical_router_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('physical_router_refs')
            self._original_physical_router_refs = (self.get_physical_router_refs() or [])[:]
        super(InstanceIp, self).add_physical_router(*args, **kwargs)
    #end add_physical_router

    def del_physical_router(self, *args, **kwargs):
        if 'physical_router_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('physical_router_refs')
            self._original_physical_router_refs = (self.get_physical_router_refs() or [])[:]
        super(InstanceIp, self).del_physical_router(*args, **kwargs)
    #end del_physical_router

    def set_physical_router_list(self, *args, **kwargs):
        """Set physical-router list for instance-ip.
        
        :param ref_obj_list: list of PhysicalRouter object
        
        """
        self._pending_field_updates.add('physical_router_refs')
        self._pending_ref_updates.discard('physical_router_refs')
        super(InstanceIp, self).set_physical_router_list(*args, **kwargs)
    #end set_physical_router_list


    def get_service_instance_back_refs(self):
        """Return list of all service-instances using this instance-ip"""
        back_refs = super(InstanceIp, self).get_service_instance_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.instance_ip_read(id = self.uuid, fields = ['service_instance_back_refs'])
        back_refs = getattr(obj, 'service_instance_back_refs', None)
        self.service_instance_back_refs = back_refs

        return back_refs
    #end get_service_instance_back_refs

#end class InstanceIp

class FloatingIpPool(pycontrail.gen.resource_common.FloatingIpPool):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, floating_ip_pool_prefixes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if floating_ip_pool_prefixes is not None:
            pending_fields.append('floating_ip_pool_prefixes')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(FloatingIpPool, self).__init__(name, parent_obj, floating_ip_pool_prefixes, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'floating_ip_pool_prefixes' in kwargs:
            if kwargs['floating_ip_pool_prefixes'] is None:
                props_dict['floating_ip_pool_prefixes'] = None
            else:
                props_dict['floating_ip_pool_prefixes'] = pycontrail.gen.resource_xsd.FloatingIpPoolType(**kwargs['floating_ip_pool_prefixes'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = FloatingIpPool(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'floating_ips' in kwargs:
            obj.floating_ips = kwargs['floating_ips']

        # add any specified references...

        # and back references but no obj api for it...
        if 'project_back_refs' in kwargs:
            obj.project_back_refs = kwargs['project_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.FloatingIpPool.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.FloatingIpPool.floating_ip_pool_prefixes.setter
    def floating_ip_pool_prefixes(self, floating_ip_pool_prefixes):
        """Set floating-ip-pool-prefixes for floating-ip-pool.
        
        :param floating_ip_pool_prefixes: FloatingIpPoolType object
        
        """
        if 'floating_ip_pool_prefixes' not in self._pending_field_updates:
            self._pending_field_updates.add('floating_ip_pool_prefixes')

        self._floating_ip_pool_prefixes = floating_ip_pool_prefixes
    #end floating_ip_pool_prefixes

    def set_floating_ip_pool_prefixes(self, value):
        self.floating_ip_pool_prefixes = value
    #end set_floating_ip_pool_prefixes

    @pycontrail.gen.resource_common.FloatingIpPool.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for floating-ip-pool.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.FloatingIpPool.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for floating-ip-pool.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.FloatingIpPool.display_name.setter
    def display_name(self, display_name):
        """Set display-name for floating-ip-pool.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_floating_ips(self):
        children = super(FloatingIpPool, self).get_floating_ips()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.floating_ip_pool_read(id = self.uuid, fields = ['floating_ips'])
            children = getattr(obj, 'floating_ips', None)
            self.floating_ips = children

        return children
    #end get_floating_ips


    def get_project_back_refs(self):
        """Return list of all projects using this floating-ip-pool"""
        back_refs = super(FloatingIpPool, self).get_project_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.floating_ip_pool_read(id = self.uuid, fields = ['project_back_refs'])
        back_refs = getattr(obj, 'project_back_refs', None)
        self.project_back_refs = back_refs

        return back_refs
    #end get_project_back_refs

#end class FloatingIpPool

class LoadbalancerPool(pycontrail.gen.resource_common.LoadbalancerPool):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, loadbalancer_pool_properties=None, loadbalancer_pool_provider=None, loadbalancer_pool_custom_attributes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if loadbalancer_pool_properties is not None:
            pending_fields.append('loadbalancer_pool_properties')
        if loadbalancer_pool_provider is not None:
            pending_fields.append('loadbalancer_pool_provider')
        if loadbalancer_pool_custom_attributes is not None:
            pending_fields.append('loadbalancer_pool_custom_attributes')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(LoadbalancerPool, self).__init__(name, parent_obj, loadbalancer_pool_properties, loadbalancer_pool_provider, loadbalancer_pool_custom_attributes, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'loadbalancer_pool_properties' in kwargs:
            if kwargs['loadbalancer_pool_properties'] is None:
                props_dict['loadbalancer_pool_properties'] = None
            else:
                props_dict['loadbalancer_pool_properties'] = pycontrail.gen.resource_xsd.LoadbalancerPoolType(**kwargs['loadbalancer_pool_properties'])
        if 'loadbalancer_pool_provider' in kwargs:
            props_dict['loadbalancer_pool_provider'] = kwargs['loadbalancer_pool_provider']
        if 'loadbalancer_pool_custom_attributes' in kwargs:
            if kwargs['loadbalancer_pool_custom_attributes'] is None:
                props_dict['loadbalancer_pool_custom_attributes'] = None
            else:
                props_dict['loadbalancer_pool_custom_attributes'] = pycontrail.gen.resource_xsd.KeyValuePairs(**kwargs['loadbalancer_pool_custom_attributes'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = LoadbalancerPool(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'loadbalancer_members' in kwargs:
            obj.loadbalancer_members = kwargs['loadbalancer_members']

        # add any specified references...
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']
        if 'loadbalancer_listener_refs' in kwargs:
            obj.loadbalancer_listener_refs = kwargs['loadbalancer_listener_refs']
        if 'service_appliance_set_refs' in kwargs:
            obj.service_appliance_set_refs = kwargs['service_appliance_set_refs']
        if 'loadbalancer_healthmonitor_refs' in kwargs:
            obj.loadbalancer_healthmonitor_refs = kwargs['loadbalancer_healthmonitor_refs']

        # and back references but no obj api for it...
        if 'virtual_ip_back_refs' in kwargs:
            obj.virtual_ip_back_refs = kwargs['virtual_ip_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.LoadbalancerPool.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.LoadbalancerPool.loadbalancer_pool_properties.setter
    def loadbalancer_pool_properties(self, loadbalancer_pool_properties):
        """Set loadbalancer-pool-properties for loadbalancer-pool.
        
        :param loadbalancer_pool_properties: LoadbalancerPoolType object
        
        """
        if 'loadbalancer_pool_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_pool_properties')

        self._loadbalancer_pool_properties = loadbalancer_pool_properties
    #end loadbalancer_pool_properties

    def set_loadbalancer_pool_properties(self, value):
        self.loadbalancer_pool_properties = value
    #end set_loadbalancer_pool_properties

    @pycontrail.gen.resource_common.LoadbalancerPool.loadbalancer_pool_provider.setter
    def loadbalancer_pool_provider(self, loadbalancer_pool_provider):
        """Set loadbalancer-pool-provider for loadbalancer-pool.
        
        :param loadbalancer_pool_provider: xsd:string object
        
        """
        if 'loadbalancer_pool_provider' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_pool_provider')

        self._loadbalancer_pool_provider = loadbalancer_pool_provider
    #end loadbalancer_pool_provider

    def set_loadbalancer_pool_provider(self, value):
        self.loadbalancer_pool_provider = value
    #end set_loadbalancer_pool_provider

    @pycontrail.gen.resource_common.LoadbalancerPool.loadbalancer_pool_custom_attributes.setter
    def loadbalancer_pool_custom_attributes(self, loadbalancer_pool_custom_attributes):
        """Set loadbalancer-pool-custom-attributes for loadbalancer-pool.
        
        :param loadbalancer_pool_custom_attributes: KeyValuePairs object
        
        """
        if 'loadbalancer_pool_custom_attributes' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_pool_custom_attributes')

        self._loadbalancer_pool_custom_attributes = loadbalancer_pool_custom_attributes
    #end loadbalancer_pool_custom_attributes

    def set_loadbalancer_pool_custom_attributes(self, value):
        self.loadbalancer_pool_custom_attributes = value
    #end set_loadbalancer_pool_custom_attributes

    @pycontrail.gen.resource_common.LoadbalancerPool.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-pool.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.LoadbalancerPool.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-pool.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.LoadbalancerPool.display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-pool.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for loadbalancer-pool.
        
        :param ref_obj: ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(LoadbalancerPool, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to loadbalancer-pool.
        
        :param ref_obj: ServiceInstance object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(LoadbalancerPool, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(LoadbalancerPool, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for loadbalancer-pool.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(LoadbalancerPool, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for loadbalancer-pool.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(LoadbalancerPool, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to loadbalancer-pool.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(LoadbalancerPool, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(LoadbalancerPool, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for loadbalancer-pool.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(LoadbalancerPool, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list

    def set_loadbalancer_listener(self, *args, **kwargs):
        """Set loadbalancer-listener for loadbalancer-pool.
        
        :param ref_obj: LoadbalancerListener object
        
        """
        self._pending_field_updates.add('loadbalancer_listener_refs')
        self._pending_ref_updates.discard('loadbalancer_listener_refs')
        super(LoadbalancerPool, self).set_loadbalancer_listener(*args, **kwargs)

    #end set_loadbalancer_listener

    def add_loadbalancer_listener(self, *args, **kwargs):
        """Add loadbalancer-listener to loadbalancer-pool.
        
        :param ref_obj: LoadbalancerListener object
        
        """
        if 'loadbalancer_listener_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('loadbalancer_listener_refs')
            self._original_loadbalancer_listener_refs = (self.get_loadbalancer_listener_refs() or [])[:]
        super(LoadbalancerPool, self).add_loadbalancer_listener(*args, **kwargs)
    #end add_loadbalancer_listener

    def del_loadbalancer_listener(self, *args, **kwargs):
        if 'loadbalancer_listener_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('loadbalancer_listener_refs')
            self._original_loadbalancer_listener_refs = (self.get_loadbalancer_listener_refs() or [])[:]
        super(LoadbalancerPool, self).del_loadbalancer_listener(*args, **kwargs)
    #end del_loadbalancer_listener

    def set_loadbalancer_listener_list(self, *args, **kwargs):
        """Set loadbalancer-listener list for loadbalancer-pool.
        
        :param ref_obj_list: list of LoadbalancerListener object
        
        """
        self._pending_field_updates.add('loadbalancer_listener_refs')
        self._pending_ref_updates.discard('loadbalancer_listener_refs')
        super(LoadbalancerPool, self).set_loadbalancer_listener_list(*args, **kwargs)
    #end set_loadbalancer_listener_list

    def set_service_appliance_set(self, *args, **kwargs):
        """Set service-appliance-set for loadbalancer-pool.
        
        :param ref_obj: ServiceApplianceSet object
        
        """
        self._pending_field_updates.add('service_appliance_set_refs')
        self._pending_ref_updates.discard('service_appliance_set_refs')
        super(LoadbalancerPool, self).set_service_appliance_set(*args, **kwargs)

    #end set_service_appliance_set

    def add_service_appliance_set(self, *args, **kwargs):
        """Add service-appliance-set to loadbalancer-pool.
        
        :param ref_obj: ServiceApplianceSet object
        
        """
        if 'service_appliance_set_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_appliance_set_refs')
            self._original_service_appliance_set_refs = (self.get_service_appliance_set_refs() or [])[:]
        super(LoadbalancerPool, self).add_service_appliance_set(*args, **kwargs)
    #end add_service_appliance_set

    def del_service_appliance_set(self, *args, **kwargs):
        if 'service_appliance_set_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_appliance_set_refs')
            self._original_service_appliance_set_refs = (self.get_service_appliance_set_refs() or [])[:]
        super(LoadbalancerPool, self).del_service_appliance_set(*args, **kwargs)
    #end del_service_appliance_set

    def set_service_appliance_set_list(self, *args, **kwargs):
        """Set service-appliance-set list for loadbalancer-pool.
        
        :param ref_obj_list: list of ServiceApplianceSet object
        
        """
        self._pending_field_updates.add('service_appliance_set_refs')
        self._pending_ref_updates.discard('service_appliance_set_refs')
        super(LoadbalancerPool, self).set_service_appliance_set_list(*args, **kwargs)
    #end set_service_appliance_set_list

    def set_loadbalancer_healthmonitor(self, *args, **kwargs):
        """Set loadbalancer-healthmonitor for loadbalancer-pool.
        
        :param ref_obj: LoadbalancerHealthmonitor object
        
        """
        self._pending_field_updates.add('loadbalancer_healthmonitor_refs')
        self._pending_ref_updates.discard('loadbalancer_healthmonitor_refs')
        super(LoadbalancerPool, self).set_loadbalancer_healthmonitor(*args, **kwargs)

    #end set_loadbalancer_healthmonitor

    def add_loadbalancer_healthmonitor(self, *args, **kwargs):
        """Add loadbalancer-healthmonitor to loadbalancer-pool.
        
        :param ref_obj: LoadbalancerHealthmonitor object
        
        """
        if 'loadbalancer_healthmonitor_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('loadbalancer_healthmonitor_refs')
            self._original_loadbalancer_healthmonitor_refs = (self.get_loadbalancer_healthmonitor_refs() or [])[:]
        super(LoadbalancerPool, self).add_loadbalancer_healthmonitor(*args, **kwargs)
    #end add_loadbalancer_healthmonitor

    def del_loadbalancer_healthmonitor(self, *args, **kwargs):
        if 'loadbalancer_healthmonitor_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('loadbalancer_healthmonitor_refs')
            self._original_loadbalancer_healthmonitor_refs = (self.get_loadbalancer_healthmonitor_refs() or [])[:]
        super(LoadbalancerPool, self).del_loadbalancer_healthmonitor(*args, **kwargs)
    #end del_loadbalancer_healthmonitor

    def set_loadbalancer_healthmonitor_list(self, *args, **kwargs):
        """Set loadbalancer-healthmonitor list for loadbalancer-pool.
        
        :param ref_obj_list: list of LoadbalancerHealthmonitor object
        
        """
        self._pending_field_updates.add('loadbalancer_healthmonitor_refs')
        self._pending_ref_updates.discard('loadbalancer_healthmonitor_refs')
        super(LoadbalancerPool, self).set_loadbalancer_healthmonitor_list(*args, **kwargs)
    #end set_loadbalancer_healthmonitor_list

    def get_loadbalancer_members(self):
        children = super(LoadbalancerPool, self).get_loadbalancer_members()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.loadbalancer_pool_read(id = self.uuid, fields = ['loadbalancer_members'])
            children = getattr(obj, 'loadbalancer_members', None)
            self.loadbalancer_members = children

        return children
    #end get_loadbalancer_members


    def get_virtual_ip_back_refs(self):
        """Return list of all virtual-ips using this loadbalancer-pool"""
        back_refs = super(LoadbalancerPool, self).get_virtual_ip_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.loadbalancer_pool_read(id = self.uuid, fields = ['virtual_ip_back_refs'])
        back_refs = getattr(obj, 'virtual_ip_back_refs', None)
        self.virtual_ip_back_refs = back_refs

        return back_refs
    #end get_virtual_ip_back_refs

#end class LoadbalancerPool

class VirtualDnsRecord(pycontrail.gen.resource_common.VirtualDnsRecord):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, virtual_DNS_record_data=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if virtual_DNS_record_data is not None:
            pending_fields.append('virtual_DNS_record_data')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(VirtualDnsRecord, self).__init__(name, parent_obj, virtual_DNS_record_data, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'virtual_DNS_record_data' in kwargs:
            if kwargs['virtual_DNS_record_data'] is None:
                props_dict['virtual_DNS_record_data'] = None
            else:
                props_dict['virtual_DNS_record_data'] = pycontrail.gen.resource_xsd.VirtualDnsRecordType(**kwargs['virtual_DNS_record_data'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = VirtualDnsRecord(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.VirtualDnsRecord.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.VirtualDnsRecord.virtual_DNS_record_data.setter
    def virtual_DNS_record_data(self, virtual_DNS_record_data):
        """Set virtual-DNS-record-data for virtual-DNS-record.
        
        :param virtual_DNS_record_data: VirtualDnsRecordType object
        
        """
        if 'virtual_DNS_record_data' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_DNS_record_data')

        self._virtual_DNS_record_data = virtual_DNS_record_data
    #end virtual_DNS_record_data

    def set_virtual_DNS_record_data(self, value):
        self.virtual_DNS_record_data = value
    #end set_virtual_DNS_record_data

    @pycontrail.gen.resource_common.VirtualDnsRecord.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-DNS-record.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.VirtualDnsRecord.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-DNS-record.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.VirtualDnsRecord.display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-DNS-record.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class VirtualDnsRecord

class RouteTarget(pycontrail.gen.resource_common.RouteTarget):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(RouteTarget, self).__init__(name, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = RouteTarget(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...
        if 'logical_router_back_refs' in kwargs:
            obj.logical_router_back_refs = kwargs['logical_router_back_refs']
        if 'routing_instance_back_refs' in kwargs:
            obj.routing_instance_back_refs = kwargs['routing_instance_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.RouteTarget.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.RouteTarget.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for route-target.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.RouteTarget.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for route-target.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.RouteTarget.display_name.setter
    def display_name(self, display_name):
        """Set display-name for route-target.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this route-target"""
        back_refs = super(RouteTarget, self).get_logical_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.route_target_read(id = self.uuid, fields = ['logical_router_back_refs'])
        back_refs = getattr(obj, 'logical_router_back_refs', None)
        self.logical_router_back_refs = back_refs

        return back_refs
    #end get_logical_router_back_refs

    def get_routing_instance_back_refs(self):
        """Return list of all routing-instances using this route-target"""
        back_refs = super(RouteTarget, self).get_routing_instance_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.route_target_read(id = self.uuid, fields = ['routing_instance_back_refs'])
        back_refs = getattr(obj, 'routing_instance_back_refs', None)
        self.routing_instance_back_refs = back_refs

        return back_refs
    #end get_routing_instance_back_refs

#end class RouteTarget

class DiscoveryServiceAssignment(pycontrail.gen.resource_common.DiscoveryServiceAssignment):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(DiscoveryServiceAssignment, self).__init__(name, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = DiscoveryServiceAssignment(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'dsa_rules' in kwargs:
            obj.dsa_rules = kwargs['dsa_rules']

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.DiscoveryServiceAssignment.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.DiscoveryServiceAssignment.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for discovery-service-assignment.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.DiscoveryServiceAssignment.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for discovery-service-assignment.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.DiscoveryServiceAssignment.display_name.setter
    def display_name(self, display_name):
        """Set display-name for discovery-service-assignment.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_dsa_rules(self):
        children = super(DiscoveryServiceAssignment, self).get_dsa_rules()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.discovery_service_assignment_read(id = self.uuid, fields = ['dsa_rules'])
            children = getattr(obj, 'dsa_rules', None)
            self.dsa_rules = children

        return children
    #end get_dsa_rules


#end class DiscoveryServiceAssignment

class FloatingIp(pycontrail.gen.resource_common.FloatingIp):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, floating_ip_address=None, floating_ip_is_virtual_ip=None, floating_ip_fixed_ip_address=None, floating_ip_address_family=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if floating_ip_address is not None:
            pending_fields.append('floating_ip_address')
        if floating_ip_is_virtual_ip is not None:
            pending_fields.append('floating_ip_is_virtual_ip')
        if floating_ip_fixed_ip_address is not None:
            pending_fields.append('floating_ip_fixed_ip_address')
        if floating_ip_address_family is not None:
            pending_fields.append('floating_ip_address_family')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(FloatingIp, self).__init__(name, parent_obj, floating_ip_address, floating_ip_is_virtual_ip, floating_ip_fixed_ip_address, floating_ip_address_family, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'floating_ip_address' in kwargs:
            props_dict['floating_ip_address'] = kwargs['floating_ip_address']
        if 'floating_ip_is_virtual_ip' in kwargs:
            props_dict['floating_ip_is_virtual_ip'] = kwargs['floating_ip_is_virtual_ip']
        if 'floating_ip_fixed_ip_address' in kwargs:
            props_dict['floating_ip_fixed_ip_address'] = kwargs['floating_ip_fixed_ip_address']
        if 'floating_ip_address_family' in kwargs:
            props_dict['floating_ip_address_family'] = kwargs['floating_ip_address_family']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = FloatingIp(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'project_refs' in kwargs:
            obj.project_refs = kwargs['project_refs']
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']

        # and back references but no obj api for it...
        if 'customer_attachment_back_refs' in kwargs:
            obj.customer_attachment_back_refs = kwargs['customer_attachment_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.FloatingIp.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.FloatingIp.floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Set floating-ip-address for floating-ip.
        
        :param floating_ip_address: IpAddressType object
        
        """
        if 'floating_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('floating_ip_address')

        self._floating_ip_address = floating_ip_address
    #end floating_ip_address

    def set_floating_ip_address(self, value):
        self.floating_ip_address = value
    #end set_floating_ip_address

    @pycontrail.gen.resource_common.FloatingIp.floating_ip_is_virtual_ip.setter
    def floating_ip_is_virtual_ip(self, floating_ip_is_virtual_ip):
        """Set floating-ip-is-virtual-ip for floating-ip.
        
        :param floating_ip_is_virtual_ip: xsd:boolean object
        
        """
        if 'floating_ip_is_virtual_ip' not in self._pending_field_updates:
            self._pending_field_updates.add('floating_ip_is_virtual_ip')

        self._floating_ip_is_virtual_ip = floating_ip_is_virtual_ip
    #end floating_ip_is_virtual_ip

    def set_floating_ip_is_virtual_ip(self, value):
        self.floating_ip_is_virtual_ip = value
    #end set_floating_ip_is_virtual_ip

    @pycontrail.gen.resource_common.FloatingIp.floating_ip_fixed_ip_address.setter
    def floating_ip_fixed_ip_address(self, floating_ip_fixed_ip_address):
        """Set floating-ip-fixed-ip-address for floating-ip.
        
        :param floating_ip_fixed_ip_address: IpAddressType object
        
        """
        if 'floating_ip_fixed_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('floating_ip_fixed_ip_address')

        self._floating_ip_fixed_ip_address = floating_ip_fixed_ip_address
    #end floating_ip_fixed_ip_address

    def set_floating_ip_fixed_ip_address(self, value):
        self.floating_ip_fixed_ip_address = value
    #end set_floating_ip_fixed_ip_address

    @pycontrail.gen.resource_common.FloatingIp.floating_ip_address_family.setter
    def floating_ip_address_family(self, floating_ip_address_family):
        """Set floating-ip-address-family for floating-ip.
        
        :param floating_ip_address_family: IpAddressFamilyType object
        
        """
        if 'floating_ip_address_family' not in self._pending_field_updates:
            self._pending_field_updates.add('floating_ip_address_family')

        self._floating_ip_address_family = floating_ip_address_family
    #end floating_ip_address_family

    def set_floating_ip_address_family(self, value):
        self.floating_ip_address_family = value
    #end set_floating_ip_address_family

    @pycontrail.gen.resource_common.FloatingIp.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for floating-ip.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.FloatingIp.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for floating-ip.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.FloatingIp.display_name.setter
    def display_name(self, display_name):
        """Set display-name for floating-ip.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_project(self, *args, **kwargs):
        """Set project for floating-ip.
        
        :param ref_obj: Project object
        
        """
        self._pending_field_updates.add('project_refs')
        self._pending_ref_updates.discard('project_refs')
        super(FloatingIp, self).set_project(*args, **kwargs)

    #end set_project

    def add_project(self, *args, **kwargs):
        """Add project to floating-ip.
        
        :param ref_obj: Project object
        
        """
        if 'project_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('project_refs')
            self._original_project_refs = (self.get_project_refs() or [])[:]
        super(FloatingIp, self).add_project(*args, **kwargs)
    #end add_project

    def del_project(self, *args, **kwargs):
        if 'project_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('project_refs')
            self._original_project_refs = (self.get_project_refs() or [])[:]
        super(FloatingIp, self).del_project(*args, **kwargs)
    #end del_project

    def set_project_list(self, *args, **kwargs):
        """Set project list for floating-ip.
        
        :param ref_obj_list: list of Project object
        
        """
        self._pending_field_updates.add('project_refs')
        self._pending_ref_updates.discard('project_refs')
        super(FloatingIp, self).set_project_list(*args, **kwargs)
    #end set_project_list

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for floating-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(FloatingIp, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to floating-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(FloatingIp, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(FloatingIp, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for floating-ip.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(FloatingIp, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list


    def get_customer_attachment_back_refs(self):
        """Return list of all customer-attachments using this floating-ip"""
        back_refs = super(FloatingIp, self).get_customer_attachment_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.floating_ip_read(id = self.uuid, fields = ['customer_attachment_back_refs'])
        back_refs = getattr(obj, 'customer_attachment_back_refs', None)
        self.customer_attachment_back_refs = back_refs

        return back_refs
    #end get_customer_attachment_back_refs

#end class FloatingIp

class NetworkPolicy(pycontrail.gen.resource_common.NetworkPolicy):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, network_policy_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if network_policy_entries is not None:
            pending_fields.append('network_policy_entries')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(NetworkPolicy, self).__init__(name, parent_obj, network_policy_entries, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'network_policy_entries' in kwargs:
            if kwargs['network_policy_entries'] is None:
                props_dict['network_policy_entries'] = None
            else:
                props_dict['network_policy_entries'] = pycontrail.gen.resource_xsd.PolicyEntriesType(**kwargs['network_policy_entries'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = NetworkPolicy(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...
        if 'virtual_network_back_refs' in kwargs:
            obj.virtual_network_back_refs = kwargs['virtual_network_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.NetworkPolicy.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.NetworkPolicy.network_policy_entries.setter
    def network_policy_entries(self, network_policy_entries):
        """Set network-policy-entries for network-policy.
        
        :param network_policy_entries: PolicyEntriesType object
        
        """
        if 'network_policy_entries' not in self._pending_field_updates:
            self._pending_field_updates.add('network_policy_entries')

        self._network_policy_entries = network_policy_entries
    #end network_policy_entries

    def set_network_policy_entries(self, value):
        self.network_policy_entries = value
    #end set_network_policy_entries

    @pycontrail.gen.resource_common.NetworkPolicy.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for network-policy.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.NetworkPolicy.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for network-policy.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.NetworkPolicy.display_name.setter
    def display_name(self, display_name):
        """Set display-name for network-policy.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this network-policy"""
        back_refs = super(NetworkPolicy, self).get_virtual_network_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.network_policy_read(id = self.uuid, fields = ['virtual_network_back_refs'])
        back_refs = getattr(obj, 'virtual_network_back_refs', None)
        self.virtual_network_back_refs = back_refs

        return back_refs
    #end get_virtual_network_back_refs

#end class NetworkPolicy

class PhysicalRouter(pycontrail.gen.resource_common.PhysicalRouter):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, physical_router_management_ip=None, physical_router_dataplane_ip=None, physical_router_vendor_name=None, physical_router_product_name=None, physical_router_vnc_managed=None, physical_router_user_credentials=None, physical_router_snmp_credentials=None, physical_router_junos_service_ports=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if physical_router_management_ip is not None:
            pending_fields.append('physical_router_management_ip')
        if physical_router_dataplane_ip is not None:
            pending_fields.append('physical_router_dataplane_ip')
        if physical_router_vendor_name is not None:
            pending_fields.append('physical_router_vendor_name')
        if physical_router_product_name is not None:
            pending_fields.append('physical_router_product_name')
        if physical_router_vnc_managed is not None:
            pending_fields.append('physical_router_vnc_managed')
        if physical_router_user_credentials is not None:
            pending_fields.append('physical_router_user_credentials')
        if physical_router_snmp_credentials is not None:
            pending_fields.append('physical_router_snmp_credentials')
        if physical_router_junos_service_ports is not None:
            pending_fields.append('physical_router_junos_service_ports')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(PhysicalRouter, self).__init__(name, parent_obj, physical_router_management_ip, physical_router_dataplane_ip, physical_router_vendor_name, physical_router_product_name, physical_router_vnc_managed, physical_router_user_credentials, physical_router_snmp_credentials, physical_router_junos_service_ports, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'physical_router_management_ip' in kwargs:
            props_dict['physical_router_management_ip'] = kwargs['physical_router_management_ip']
        if 'physical_router_dataplane_ip' in kwargs:
            props_dict['physical_router_dataplane_ip'] = kwargs['physical_router_dataplane_ip']
        if 'physical_router_vendor_name' in kwargs:
            props_dict['physical_router_vendor_name'] = kwargs['physical_router_vendor_name']
        if 'physical_router_product_name' in kwargs:
            props_dict['physical_router_product_name'] = kwargs['physical_router_product_name']
        if 'physical_router_vnc_managed' in kwargs:
            props_dict['physical_router_vnc_managed'] = kwargs['physical_router_vnc_managed']
        if 'physical_router_user_credentials' in kwargs:
            if kwargs['physical_router_user_credentials'] is None:
                props_dict['physical_router_user_credentials'] = None
            else:
                props_dict['physical_router_user_credentials'] = pycontrail.gen.resource_xsd.UserCredentials(**kwargs['physical_router_user_credentials'])
        if 'physical_router_snmp_credentials' in kwargs:
            if kwargs['physical_router_snmp_credentials'] is None:
                props_dict['physical_router_snmp_credentials'] = None
            else:
                props_dict['physical_router_snmp_credentials'] = pycontrail.gen.resource_xsd.SNMPCredentials(**kwargs['physical_router_snmp_credentials'])
        if 'physical_router_junos_service_ports' in kwargs:
            if kwargs['physical_router_junos_service_ports'] is None:
                props_dict['physical_router_junos_service_ports'] = None
            else:
                props_dict['physical_router_junos_service_ports'] = pycontrail.gen.resource_xsd.JunosServicePorts(**kwargs['physical_router_junos_service_ports'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = PhysicalRouter(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'physical_interfaces' in kwargs:
            obj.physical_interfaces = kwargs['physical_interfaces']
        if 'logical_interfaces' in kwargs:
            obj.logical_interfaces = kwargs['logical_interfaces']

        # add any specified references...
        if 'virtual_router_refs' in kwargs:
            obj.virtual_router_refs = kwargs['virtual_router_refs']
        if 'bgp_router_refs' in kwargs:
            obj.bgp_router_refs = kwargs['bgp_router_refs']
        if 'virtual_network_refs' in kwargs:
            obj.virtual_network_refs = kwargs['virtual_network_refs']

        # and back references but no obj api for it...
        if 'instance_ip_back_refs' in kwargs:
            obj.instance_ip_back_refs = kwargs['instance_ip_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.PhysicalRouter.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_management_ip.setter
    def physical_router_management_ip(self, physical_router_management_ip):
        """Set physical-router-management-ip for physical-router.
        
        :param physical_router_management_ip: IpAddress object
        
        """
        if 'physical_router_management_ip' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_management_ip')

        self._physical_router_management_ip = physical_router_management_ip
    #end physical_router_management_ip

    def set_physical_router_management_ip(self, value):
        self.physical_router_management_ip = value
    #end set_physical_router_management_ip

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_dataplane_ip.setter
    def physical_router_dataplane_ip(self, physical_router_dataplane_ip):
        """Set physical-router-dataplane-ip for physical-router.
        
        :param physical_router_dataplane_ip: IpAddress object
        
        """
        if 'physical_router_dataplane_ip' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_dataplane_ip')

        self._physical_router_dataplane_ip = physical_router_dataplane_ip
    #end physical_router_dataplane_ip

    def set_physical_router_dataplane_ip(self, value):
        self.physical_router_dataplane_ip = value
    #end set_physical_router_dataplane_ip

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_vendor_name.setter
    def physical_router_vendor_name(self, physical_router_vendor_name):
        """Set physical-router-vendor-name for physical-router.
        
        :param physical_router_vendor_name: xsd:string object
        
        """
        if 'physical_router_vendor_name' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_vendor_name')

        self._physical_router_vendor_name = physical_router_vendor_name
    #end physical_router_vendor_name

    def set_physical_router_vendor_name(self, value):
        self.physical_router_vendor_name = value
    #end set_physical_router_vendor_name

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_product_name.setter
    def physical_router_product_name(self, physical_router_product_name):
        """Set physical-router-product-name for physical-router.
        
        :param physical_router_product_name: xsd:string object
        
        """
        if 'physical_router_product_name' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_product_name')

        self._physical_router_product_name = physical_router_product_name
    #end physical_router_product_name

    def set_physical_router_product_name(self, value):
        self.physical_router_product_name = value
    #end set_physical_router_product_name

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_vnc_managed.setter
    def physical_router_vnc_managed(self, physical_router_vnc_managed):
        """Set physical-router-vnc-managed for physical-router.
        
        :param physical_router_vnc_managed: xsd:boolean object
        
        """
        if 'physical_router_vnc_managed' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_vnc_managed')

        self._physical_router_vnc_managed = physical_router_vnc_managed
    #end physical_router_vnc_managed

    def set_physical_router_vnc_managed(self, value):
        self.physical_router_vnc_managed = value
    #end set_physical_router_vnc_managed

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_user_credentials.setter
    def physical_router_user_credentials(self, physical_router_user_credentials):
        """Set physical-router-user-credentials for physical-router.
        
        :param physical_router_user_credentials: UserCredentials object
        
        """
        if 'physical_router_user_credentials' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_user_credentials')

        self._physical_router_user_credentials = physical_router_user_credentials
    #end physical_router_user_credentials

    def set_physical_router_user_credentials(self, value):
        self.physical_router_user_credentials = value
    #end set_physical_router_user_credentials

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_snmp_credentials.setter
    def physical_router_snmp_credentials(self, physical_router_snmp_credentials):
        """Set physical-router-snmp-credentials for physical-router.
        
        :param physical_router_snmp_credentials: SNMPCredentials object
        
        """
        if 'physical_router_snmp_credentials' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_snmp_credentials')

        self._physical_router_snmp_credentials = physical_router_snmp_credentials
    #end physical_router_snmp_credentials

    def set_physical_router_snmp_credentials(self, value):
        self.physical_router_snmp_credentials = value
    #end set_physical_router_snmp_credentials

    @pycontrail.gen.resource_common.PhysicalRouter.physical_router_junos_service_ports.setter
    def physical_router_junos_service_ports(self, physical_router_junos_service_ports):
        """Set physical-router-junos-service-ports for physical-router.
        
        :param physical_router_junos_service_ports: JunosServicePorts object
        
        """
        if 'physical_router_junos_service_ports' not in self._pending_field_updates:
            self._pending_field_updates.add('physical_router_junos_service_ports')

        self._physical_router_junos_service_ports = physical_router_junos_service_ports
    #end physical_router_junos_service_ports

    def set_physical_router_junos_service_ports(self, value):
        self.physical_router_junos_service_ports = value
    #end set_physical_router_junos_service_ports

    @pycontrail.gen.resource_common.PhysicalRouter.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for physical-router.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.PhysicalRouter.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for physical-router.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.PhysicalRouter.display_name.setter
    def display_name(self, display_name):
        """Set display-name for physical-router.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_router(self, *args, **kwargs):
        """Set virtual-router for physical-router.
        
        :param ref_obj: VirtualRouter object
        
        """
        self._pending_field_updates.add('virtual_router_refs')
        self._pending_ref_updates.discard('virtual_router_refs')
        super(PhysicalRouter, self).set_virtual_router(*args, **kwargs)

    #end set_virtual_router

    def add_virtual_router(self, *args, **kwargs):
        """Add virtual-router to physical-router.
        
        :param ref_obj: VirtualRouter object
        
        """
        if 'virtual_router_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_router_refs')
            self._original_virtual_router_refs = (self.get_virtual_router_refs() or [])[:]
        super(PhysicalRouter, self).add_virtual_router(*args, **kwargs)
    #end add_virtual_router

    def del_virtual_router(self, *args, **kwargs):
        if 'virtual_router_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_router_refs')
            self._original_virtual_router_refs = (self.get_virtual_router_refs() or [])[:]
        super(PhysicalRouter, self).del_virtual_router(*args, **kwargs)
    #end del_virtual_router

    def set_virtual_router_list(self, *args, **kwargs):
        """Set virtual-router list for physical-router.
        
        :param ref_obj_list: list of VirtualRouter object
        
        """
        self._pending_field_updates.add('virtual_router_refs')
        self._pending_ref_updates.discard('virtual_router_refs')
        super(PhysicalRouter, self).set_virtual_router_list(*args, **kwargs)
    #end set_virtual_router_list

    def set_bgp_router(self, *args, **kwargs):
        """Set bgp-router for physical-router.
        
        :param ref_obj: BgpRouter object
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(PhysicalRouter, self).set_bgp_router(*args, **kwargs)

    #end set_bgp_router

    def add_bgp_router(self, *args, **kwargs):
        """Add bgp-router to physical-router.
        
        :param ref_obj: BgpRouter object
        
        """
        if 'bgp_router_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(PhysicalRouter, self).add_bgp_router(*args, **kwargs)
    #end add_bgp_router

    def del_bgp_router(self, *args, **kwargs):
        if 'bgp_router_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(PhysicalRouter, self).del_bgp_router(*args, **kwargs)
    #end del_bgp_router

    def set_bgp_router_list(self, *args, **kwargs):
        """Set bgp-router list for physical-router.
        
        :param ref_obj_list: list of BgpRouter object
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(PhysicalRouter, self).set_bgp_router_list(*args, **kwargs)
    #end set_bgp_router_list

    def set_virtual_network(self, *args, **kwargs):
        """Set virtual-network for physical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(PhysicalRouter, self).set_virtual_network(*args, **kwargs)

    #end set_virtual_network

    def add_virtual_network(self, *args, **kwargs):
        """Add virtual-network to physical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        if 'virtual_network_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(PhysicalRouter, self).add_virtual_network(*args, **kwargs)
    #end add_virtual_network

    def del_virtual_network(self, *args, **kwargs):
        if 'virtual_network_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(PhysicalRouter, self).del_virtual_network(*args, **kwargs)
    #end del_virtual_network

    def set_virtual_network_list(self, *args, **kwargs):
        """Set virtual-network list for physical-router.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(PhysicalRouter, self).set_virtual_network_list(*args, **kwargs)
    #end set_virtual_network_list

    def get_physical_interfaces(self):
        children = super(PhysicalRouter, self).get_physical_interfaces()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.physical_router_read(id = self.uuid, fields = ['physical_interfaces'])
            children = getattr(obj, 'physical_interfaces', None)
            self.physical_interfaces = children

        return children
    #end get_physical_interfaces

    def get_logical_interfaces(self):
        children = super(PhysicalRouter, self).get_logical_interfaces()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.physical_router_read(id = self.uuid, fields = ['logical_interfaces'])
            children = getattr(obj, 'logical_interfaces', None)
            self.logical_interfaces = children

        return children
    #end get_logical_interfaces


    def get_instance_ip_back_refs(self):
        """Return list of all instance-ips using this physical-router"""
        back_refs = super(PhysicalRouter, self).get_instance_ip_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.physical_router_read(id = self.uuid, fields = ['instance_ip_back_refs'])
        back_refs = getattr(obj, 'instance_ip_back_refs', None)
        self.instance_ip_back_refs = back_refs

        return back_refs
    #end get_instance_ip_back_refs

#end class PhysicalRouter

class BgpRouter(pycontrail.gen.resource_common.BgpRouter):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, bgp_router_parameters=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if bgp_router_parameters is not None:
            pending_fields.append('bgp_router_parameters')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(BgpRouter, self).__init__(name, parent_obj, bgp_router_parameters, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'bgp_router_parameters' in kwargs:
            if kwargs['bgp_router_parameters'] is None:
                props_dict['bgp_router_parameters'] = None
            else:
                props_dict['bgp_router_parameters'] = pycontrail.gen.resource_xsd.BgpRouterParams(**kwargs['bgp_router_parameters'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = BgpRouter(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'bgp_router_refs' in kwargs:
            obj.bgp_router_refs = kwargs['bgp_router_refs']
            for ref in obj.bgp_router_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.BgpPeeringAttributes(**ref['attr'])

        # and back references but no obj api for it...
        if 'global_system_config_back_refs' in kwargs:
            obj.global_system_config_back_refs = kwargs['global_system_config_back_refs']
        if 'physical_router_back_refs' in kwargs:
            obj.physical_router_back_refs = kwargs['physical_router_back_refs']
        if 'bgp_as_a_service_back_refs' in kwargs:
            obj.bgp_as_a_service_back_refs = kwargs['bgp_as_a_service_back_refs']
        if 'bgp_router_back_refs' in kwargs:
            obj.bgp_router_back_refs = kwargs['bgp_router_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.BgpRouter.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.BgpRouter.bgp_router_parameters.setter
    def bgp_router_parameters(self, bgp_router_parameters):
        """Set bgp-router-parameters for bgp-router.
        
        :param bgp_router_parameters: BgpRouterParams object
        
        """
        if 'bgp_router_parameters' not in self._pending_field_updates:
            self._pending_field_updates.add('bgp_router_parameters')

        self._bgp_router_parameters = bgp_router_parameters
    #end bgp_router_parameters

    def set_bgp_router_parameters(self, value):
        self.bgp_router_parameters = value
    #end set_bgp_router_parameters

    @pycontrail.gen.resource_common.BgpRouter.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for bgp-router.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.BgpRouter.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for bgp-router.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.BgpRouter.display_name.setter
    def display_name(self, display_name):
        """Set display-name for bgp-router.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_bgp_router(self, *args, **kwargs):
        """Set bgp-router for bgp-router.
        
        :param ref_obj: BgpRouter object
        :param ref_data: BgpPeeringAttributes object
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(BgpRouter, self).set_bgp_router(*args, **kwargs)

    #end set_bgp_router

    def add_bgp_router(self, *args, **kwargs):
        """Add bgp-router to bgp-router.
        
        :param ref_obj: BgpRouter object
        :param ref_data: BgpPeeringAttributes object
        
        """
        if 'bgp_router_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(BgpRouter, self).add_bgp_router(*args, **kwargs)
    #end add_bgp_router

    def del_bgp_router(self, *args, **kwargs):
        if 'bgp_router_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(BgpRouter, self).del_bgp_router(*args, **kwargs)
    #end del_bgp_router

    def set_bgp_router_list(self, *args, **kwargs):
        """Set bgp-router list for bgp-router.
        
        :param ref_obj_list: list of BgpRouter object
        :param ref_data_list: list of BgpPeeringAttributes summary
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(BgpRouter, self).set_bgp_router_list(*args, **kwargs)
    #end set_bgp_router_list


    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this bgp-router"""
        back_refs = super(BgpRouter, self).get_global_system_config_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.bgp_router_read(id = self.uuid, fields = ['global_system_config_back_refs'])
        back_refs = getattr(obj, 'global_system_config_back_refs', None)
        self.global_system_config_back_refs = back_refs

        return back_refs
    #end get_global_system_config_back_refs

    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this bgp-router"""
        back_refs = super(BgpRouter, self).get_physical_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.bgp_router_read(id = self.uuid, fields = ['physical_router_back_refs'])
        back_refs = getattr(obj, 'physical_router_back_refs', None)
        self.physical_router_back_refs = back_refs

        return back_refs
    #end get_physical_router_back_refs

    def get_bgp_as_a_service_back_refs(self):
        """Return list of all bgp-as-a-services using this bgp-router"""
        back_refs = super(BgpRouter, self).get_bgp_as_a_service_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.bgp_router_read(id = self.uuid, fields = ['bgp_as_a_service_back_refs'])
        back_refs = getattr(obj, 'bgp_as_a_service_back_refs', None)
        self.bgp_as_a_service_back_refs = back_refs

        return back_refs
    #end get_bgp_as_a_service_back_refs

    def get_bgp_router_back_refs(self):
        """Return list of all bgp-routers using this bgp-router"""
        back_refs = super(BgpRouter, self).get_bgp_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.bgp_router_read(id = self.uuid, fields = ['bgp_router_back_refs'])
        back_refs = getattr(obj, 'bgp_router_back_refs', None)
        self.bgp_router_back_refs = back_refs

        return back_refs
    #end get_bgp_router_back_refs

#end class BgpRouter

class ApiAccessList(pycontrail.gen.resource_common.ApiAccessList):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, api_access_list_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if api_access_list_entries is not None:
            pending_fields.append('api_access_list_entries')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ApiAccessList, self).__init__(name, parent_obj, api_access_list_entries, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'api_access_list_entries' in kwargs:
            if kwargs['api_access_list_entries'] is None:
                props_dict['api_access_list_entries'] = None
            else:
                props_dict['api_access_list_entries'] = pycontrail.gen.resource_xsd.RbacRuleEntriesType(**kwargs['api_access_list_entries'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ApiAccessList(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ApiAccessList.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ApiAccessList.api_access_list_entries.setter
    def api_access_list_entries(self, api_access_list_entries):
        """Set api-access-list-entries for api-access-list.
        
        :param api_access_list_entries: RbacRuleEntriesType object
        
        """
        if 'api_access_list_entries' not in self._pending_field_updates:
            self._pending_field_updates.add('api_access_list_entries')

        self._api_access_list_entries = api_access_list_entries
    #end api_access_list_entries

    def set_api_access_list_entries(self, value):
        self.api_access_list_entries = value
    #end set_api_access_list_entries

    @pycontrail.gen.resource_common.ApiAccessList.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for api-access-list.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ApiAccessList.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for api-access-list.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ApiAccessList.display_name.setter
    def display_name(self, display_name):
        """Set display-name for api-access-list.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class ApiAccessList

class VirtualRouter(pycontrail.gen.resource_common.VirtualRouter):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, virtual_router_type=None, virtual_router_dpdk_enabled=None, virtual_router_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if virtual_router_type is not None:
            pending_fields.append('virtual_router_type')
        if virtual_router_dpdk_enabled is not None:
            pending_fields.append('virtual_router_dpdk_enabled')
        if virtual_router_ip_address is not None:
            pending_fields.append('virtual_router_ip_address')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(VirtualRouter, self).__init__(name, parent_obj, virtual_router_type, virtual_router_dpdk_enabled, virtual_router_ip_address, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'virtual_router_type' in kwargs:
            props_dict['virtual_router_type'] = kwargs['virtual_router_type']
        if 'virtual_router_dpdk_enabled' in kwargs:
            props_dict['virtual_router_dpdk_enabled'] = kwargs['virtual_router_dpdk_enabled']
        if 'virtual_router_ip_address' in kwargs:
            props_dict['virtual_router_ip_address'] = kwargs['virtual_router_ip_address']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = VirtualRouter(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_machine_refs' in kwargs:
            obj.virtual_machine_refs = kwargs['virtual_machine_refs']

        # and back references but no obj api for it...
        if 'physical_router_back_refs' in kwargs:
            obj.physical_router_back_refs = kwargs['physical_router_back_refs']
        if 'provider_attachment_back_refs' in kwargs:
            obj.provider_attachment_back_refs = kwargs['provider_attachment_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.VirtualRouter.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.VirtualRouter.virtual_router_type.setter
    def virtual_router_type(self, virtual_router_type):
        """Set virtual-router-type for virtual-router.
        
        :param virtual_router_type: VirtualRouterType object
        
        """
        if 'virtual_router_type' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_router_type')

        self._virtual_router_type = virtual_router_type
    #end virtual_router_type

    def set_virtual_router_type(self, value):
        self.virtual_router_type = value
    #end set_virtual_router_type

    @pycontrail.gen.resource_common.VirtualRouter.virtual_router_dpdk_enabled.setter
    def virtual_router_dpdk_enabled(self, virtual_router_dpdk_enabled):
        """Set virtual-router-dpdk-enabled for virtual-router.
        
        :param virtual_router_dpdk_enabled: xsd:boolean object
        
        """
        if 'virtual_router_dpdk_enabled' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_router_dpdk_enabled')

        self._virtual_router_dpdk_enabled = virtual_router_dpdk_enabled
    #end virtual_router_dpdk_enabled

    def set_virtual_router_dpdk_enabled(self, value):
        self.virtual_router_dpdk_enabled = value
    #end set_virtual_router_dpdk_enabled

    @pycontrail.gen.resource_common.VirtualRouter.virtual_router_ip_address.setter
    def virtual_router_ip_address(self, virtual_router_ip_address):
        """Set virtual-router-ip-address for virtual-router.
        
        :param virtual_router_ip_address: IpAddressType object
        
        """
        if 'virtual_router_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_router_ip_address')

        self._virtual_router_ip_address = virtual_router_ip_address
    #end virtual_router_ip_address

    def set_virtual_router_ip_address(self, value):
        self.virtual_router_ip_address = value
    #end set_virtual_router_ip_address

    @pycontrail.gen.resource_common.VirtualRouter.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-router.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.VirtualRouter.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-router.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.VirtualRouter.display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-router.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_machine(self, *args, **kwargs):
        """Set virtual-machine for virtual-router.
        
        :param ref_obj: VirtualMachine object
        
        """
        self._pending_field_updates.add('virtual_machine_refs')
        self._pending_ref_updates.discard('virtual_machine_refs')
        super(VirtualRouter, self).set_virtual_machine(*args, **kwargs)

    #end set_virtual_machine

    def add_virtual_machine(self, *args, **kwargs):
        """Add virtual-machine to virtual-router.
        
        :param ref_obj: VirtualMachine object
        
        """
        if 'virtual_machine_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_refs')
            self._original_virtual_machine_refs = (self.get_virtual_machine_refs() or [])[:]
        super(VirtualRouter, self).add_virtual_machine(*args, **kwargs)
    #end add_virtual_machine

    def del_virtual_machine(self, *args, **kwargs):
        if 'virtual_machine_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_refs')
            self._original_virtual_machine_refs = (self.get_virtual_machine_refs() or [])[:]
        super(VirtualRouter, self).del_virtual_machine(*args, **kwargs)
    #end del_virtual_machine

    def set_virtual_machine_list(self, *args, **kwargs):
        """Set virtual-machine list for virtual-router.
        
        :param ref_obj_list: list of VirtualMachine object
        
        """
        self._pending_field_updates.add('virtual_machine_refs')
        self._pending_ref_updates.discard('virtual_machine_refs')
        super(VirtualRouter, self).set_virtual_machine_list(*args, **kwargs)
    #end set_virtual_machine_list


    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this virtual-router"""
        back_refs = super(VirtualRouter, self).get_physical_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_router_read(id = self.uuid, fields = ['physical_router_back_refs'])
        back_refs = getattr(obj, 'physical_router_back_refs', None)
        self.physical_router_back_refs = back_refs

        return back_refs
    #end get_physical_router_back_refs

    def get_provider_attachment_back_refs(self):
        """Return list of all provider-attachments using this virtual-router"""
        back_refs = super(VirtualRouter, self).get_provider_attachment_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_router_read(id = self.uuid, fields = ['provider_attachment_back_refs'])
        back_refs = getattr(obj, 'provider_attachment_back_refs', None)
        self.provider_attachment_back_refs = back_refs

        return back_refs
    #end get_provider_attachment_back_refs

#end class VirtualRouter

class ConfigRoot(pycontrail.gen.resource_common.ConfigRoot):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ConfigRoot, self).__init__(name, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ConfigRoot(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'global_system_configs' in kwargs:
            obj.global_system_configs = kwargs['global_system_configs']
        if 'domains' in kwargs:
            obj.domains = kwargs['domains']

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ConfigRoot.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ConfigRoot.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for config-root.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ConfigRoot.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for config-root.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ConfigRoot.display_name.setter
    def display_name(self, display_name):
        """Set display-name for config-root.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_global_system_configs(self):
        children = super(ConfigRoot, self).get_global_system_configs()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.config_root_read(id = self.uuid, fields = ['global_system_configs'])
            children = getattr(obj, 'global_system_configs', None)
            self.global_system_configs = children

        return children
    #end get_global_system_configs

    def get_domains(self):
        children = super(ConfigRoot, self).get_domains()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.config_root_read(id = self.uuid, fields = ['domains'])
            children = getattr(obj, 'domains', None)
            self.domains = children

        return children
    #end get_domains


#end class ConfigRoot

class Subnet(pycontrail.gen.resource_common.Subnet):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, subnet_ip_prefix=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if subnet_ip_prefix is not None:
            pending_fields.append('subnet_ip_prefix')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(Subnet, self).__init__(name, subnet_ip_prefix, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'subnet_ip_prefix' in kwargs:
            if kwargs['subnet_ip_prefix'] is None:
                props_dict['subnet_ip_prefix'] = None
            else:
                props_dict['subnet_ip_prefix'] = pycontrail.gen.resource_xsd.SubnetType(**kwargs['subnet_ip_prefix'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = Subnet(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.Subnet.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.Subnet.subnet_ip_prefix.setter
    def subnet_ip_prefix(self, subnet_ip_prefix):
        """Set subnet-ip-prefix for subnet.
        
        :param subnet_ip_prefix: SubnetType object
        
        """
        if 'subnet_ip_prefix' not in self._pending_field_updates:
            self._pending_field_updates.add('subnet_ip_prefix')

        self._subnet_ip_prefix = subnet_ip_prefix
    #end subnet_ip_prefix

    def set_subnet_ip_prefix(self, value):
        self.subnet_ip_prefix = value
    #end set_subnet_ip_prefix

    @pycontrail.gen.resource_common.Subnet.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for subnet.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.Subnet.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for subnet.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.Subnet.display_name.setter
    def display_name(self, display_name):
        """Set display-name for subnet.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for subnet.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(Subnet, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to subnet.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(Subnet, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(Subnet, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for subnet.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(Subnet, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list


#end class Subnet

class GlobalSystemConfig(pycontrail.gen.resource_common.GlobalSystemConfig):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, autonomous_system=None, config_version=None, plugin_tuning=None, ibgp_auto_mesh=None, ip_fabric_subnets=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if autonomous_system is not None:
            pending_fields.append('autonomous_system')
        if config_version is not None:
            pending_fields.append('config_version')
        if plugin_tuning is not None:
            pending_fields.append('plugin_tuning')
        if ibgp_auto_mesh is not None:
            pending_fields.append('ibgp_auto_mesh')
        if ip_fabric_subnets is not None:
            pending_fields.append('ip_fabric_subnets')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(GlobalSystemConfig, self).__init__(name, parent_obj, autonomous_system, config_version, plugin_tuning, ibgp_auto_mesh, ip_fabric_subnets, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'autonomous_system' in kwargs:
            props_dict['autonomous_system'] = kwargs['autonomous_system']
        if 'config_version' in kwargs:
            props_dict['config_version'] = kwargs['config_version']
        if 'plugin_tuning' in kwargs:
            if kwargs['plugin_tuning'] is None:
                props_dict['plugin_tuning'] = None
            else:
                props_dict['plugin_tuning'] = pycontrail.gen.resource_xsd.PluginProperties(**kwargs['plugin_tuning'])
        if 'ibgp_auto_mesh' in kwargs:
            props_dict['ibgp_auto_mesh'] = kwargs['ibgp_auto_mesh']
        if 'ip_fabric_subnets' in kwargs:
            if kwargs['ip_fabric_subnets'] is None:
                props_dict['ip_fabric_subnets'] = None
            else:
                props_dict['ip_fabric_subnets'] = pycontrail.gen.resource_xsd.SubnetListType(**kwargs['ip_fabric_subnets'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = GlobalSystemConfig(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'global_vrouter_configs' in kwargs:
            obj.global_vrouter_configs = kwargs['global_vrouter_configs']
        if 'physical_routers' in kwargs:
            obj.physical_routers = kwargs['physical_routers']
        if 'virtual_routers' in kwargs:
            obj.virtual_routers = kwargs['virtual_routers']
        if 'config_nodes' in kwargs:
            obj.config_nodes = kwargs['config_nodes']
        if 'analytics_nodes' in kwargs:
            obj.analytics_nodes = kwargs['analytics_nodes']
        if 'database_nodes' in kwargs:
            obj.database_nodes = kwargs['database_nodes']
        if 'service_appliance_sets' in kwargs:
            obj.service_appliance_sets = kwargs['service_appliance_sets']

        # add any specified references...
        if 'bgp_router_refs' in kwargs:
            obj.bgp_router_refs = kwargs['bgp_router_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.GlobalSystemConfig.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.GlobalSystemConfig.autonomous_system.setter
    def autonomous_system(self, autonomous_system):
        """Set autonomous-system for global-system-config.
        
        :param autonomous_system: AutonomousSystemType object
        
        """
        if 'autonomous_system' not in self._pending_field_updates:
            self._pending_field_updates.add('autonomous_system')

        self._autonomous_system = autonomous_system
    #end autonomous_system

    def set_autonomous_system(self, value):
        self.autonomous_system = value
    #end set_autonomous_system

    @pycontrail.gen.resource_common.GlobalSystemConfig.config_version.setter
    def config_version(self, config_version):
        """Set config-version for global-system-config.
        
        :param config_version: xsd:string object
        
        """
        if 'config_version' not in self._pending_field_updates:
            self._pending_field_updates.add('config_version')

        self._config_version = config_version
    #end config_version

    def set_config_version(self, value):
        self.config_version = value
    #end set_config_version

    @pycontrail.gen.resource_common.GlobalSystemConfig.plugin_tuning.setter
    def plugin_tuning(self, plugin_tuning):
        """Set plugin-tuning for global-system-config.
        
        :param plugin_tuning: PluginProperties object
        
        """
        if 'plugin_tuning' not in self._pending_field_updates:
            self._pending_field_updates.add('plugin_tuning')

        self._plugin_tuning = plugin_tuning
    #end plugin_tuning

    def set_plugin_tuning(self, value):
        self.plugin_tuning = value
    #end set_plugin_tuning

    @pycontrail.gen.resource_common.GlobalSystemConfig.ibgp_auto_mesh.setter
    def ibgp_auto_mesh(self, ibgp_auto_mesh):
        """Set ibgp-auto-mesh for global-system-config.
        
        :param ibgp_auto_mesh: xsd:boolean object
        
        """
        if 'ibgp_auto_mesh' not in self._pending_field_updates:
            self._pending_field_updates.add('ibgp_auto_mesh')

        self._ibgp_auto_mesh = ibgp_auto_mesh
    #end ibgp_auto_mesh

    def set_ibgp_auto_mesh(self, value):
        self.ibgp_auto_mesh = value
    #end set_ibgp_auto_mesh

    @pycontrail.gen.resource_common.GlobalSystemConfig.ip_fabric_subnets.setter
    def ip_fabric_subnets(self, ip_fabric_subnets):
        """Set ip-fabric-subnets for global-system-config.
        
        :param ip_fabric_subnets: SubnetListType object
        
        """
        if 'ip_fabric_subnets' not in self._pending_field_updates:
            self._pending_field_updates.add('ip_fabric_subnets')

        self._ip_fabric_subnets = ip_fabric_subnets
    #end ip_fabric_subnets

    def set_ip_fabric_subnets(self, value):
        self.ip_fabric_subnets = value
    #end set_ip_fabric_subnets

    @pycontrail.gen.resource_common.GlobalSystemConfig.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for global-system-config.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.GlobalSystemConfig.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for global-system-config.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.GlobalSystemConfig.display_name.setter
    def display_name(self, display_name):
        """Set display-name for global-system-config.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_bgp_router(self, *args, **kwargs):
        """Set bgp-router for global-system-config.
        
        :param ref_obj: BgpRouter object
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(GlobalSystemConfig, self).set_bgp_router(*args, **kwargs)

    #end set_bgp_router

    def add_bgp_router(self, *args, **kwargs):
        """Add bgp-router to global-system-config.
        
        :param ref_obj: BgpRouter object
        
        """
        if 'bgp_router_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(GlobalSystemConfig, self).add_bgp_router(*args, **kwargs)
    #end add_bgp_router

    def del_bgp_router(self, *args, **kwargs):
        if 'bgp_router_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(GlobalSystemConfig, self).del_bgp_router(*args, **kwargs)
    #end del_bgp_router

    def set_bgp_router_list(self, *args, **kwargs):
        """Set bgp-router list for global-system-config.
        
        :param ref_obj_list: list of BgpRouter object
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(GlobalSystemConfig, self).set_bgp_router_list(*args, **kwargs)
    #end set_bgp_router_list

    def get_global_vrouter_configs(self):
        children = super(GlobalSystemConfig, self).get_global_vrouter_configs()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.global_system_config_read(id = self.uuid, fields = ['global_vrouter_configs'])
            children = getattr(obj, 'global_vrouter_configs', None)
            self.global_vrouter_configs = children

        return children
    #end get_global_vrouter_configs

    def get_physical_routers(self):
        children = super(GlobalSystemConfig, self).get_physical_routers()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.global_system_config_read(id = self.uuid, fields = ['physical_routers'])
            children = getattr(obj, 'physical_routers', None)
            self.physical_routers = children

        return children
    #end get_physical_routers

    def get_virtual_routers(self):
        children = super(GlobalSystemConfig, self).get_virtual_routers()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.global_system_config_read(id = self.uuid, fields = ['virtual_routers'])
            children = getattr(obj, 'virtual_routers', None)
            self.virtual_routers = children

        return children
    #end get_virtual_routers

    def get_config_nodes(self):
        children = super(GlobalSystemConfig, self).get_config_nodes()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.global_system_config_read(id = self.uuid, fields = ['config_nodes'])
            children = getattr(obj, 'config_nodes', None)
            self.config_nodes = children

        return children
    #end get_config_nodes

    def get_analytics_nodes(self):
        children = super(GlobalSystemConfig, self).get_analytics_nodes()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.global_system_config_read(id = self.uuid, fields = ['analytics_nodes'])
            children = getattr(obj, 'analytics_nodes', None)
            self.analytics_nodes = children

        return children
    #end get_analytics_nodes

    def get_database_nodes(self):
        children = super(GlobalSystemConfig, self).get_database_nodes()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.global_system_config_read(id = self.uuid, fields = ['database_nodes'])
            children = getattr(obj, 'database_nodes', None)
            self.database_nodes = children

        return children
    #end get_database_nodes

    def get_service_appliance_sets(self):
        children = super(GlobalSystemConfig, self).get_service_appliance_sets()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.global_system_config_read(id = self.uuid, fields = ['service_appliance_sets'])
            children = getattr(obj, 'service_appliance_sets', None)
            self.service_appliance_sets = children

        return children
    #end get_service_appliance_sets


#end class GlobalSystemConfig

class ServiceAppliance(pycontrail.gen.resource_common.ServiceAppliance):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, service_appliance_user_credentials=None, service_appliance_ip_address=None, service_appliance_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if service_appliance_user_credentials is not None:
            pending_fields.append('service_appliance_user_credentials')
        if service_appliance_ip_address is not None:
            pending_fields.append('service_appliance_ip_address')
        if service_appliance_properties is not None:
            pending_fields.append('service_appliance_properties')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ServiceAppliance, self).__init__(name, parent_obj, service_appliance_user_credentials, service_appliance_ip_address, service_appliance_properties, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'service_appliance_user_credentials' in kwargs:
            if kwargs['service_appliance_user_credentials'] is None:
                props_dict['service_appliance_user_credentials'] = None
            else:
                props_dict['service_appliance_user_credentials'] = pycontrail.gen.resource_xsd.UserCredentials(**kwargs['service_appliance_user_credentials'])
        if 'service_appliance_ip_address' in kwargs:
            props_dict['service_appliance_ip_address'] = kwargs['service_appliance_ip_address']
        if 'service_appliance_properties' in kwargs:
            if kwargs['service_appliance_properties'] is None:
                props_dict['service_appliance_properties'] = None
            else:
                props_dict['service_appliance_properties'] = pycontrail.gen.resource_xsd.KeyValuePairs(**kwargs['service_appliance_properties'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ServiceAppliance(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'physical_interface_refs' in kwargs:
            obj.physical_interface_refs = kwargs['physical_interface_refs']
            for ref in obj.physical_interface_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.ServiceApplianceInterfaceType(**ref['attr'])

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ServiceAppliance.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ServiceAppliance.service_appliance_user_credentials.setter
    def service_appliance_user_credentials(self, service_appliance_user_credentials):
        """Set service-appliance-user-credentials for service-appliance.
        
        :param service_appliance_user_credentials: UserCredentials object
        
        """
        if 'service_appliance_user_credentials' not in self._pending_field_updates:
            self._pending_field_updates.add('service_appliance_user_credentials')

        self._service_appliance_user_credentials = service_appliance_user_credentials
    #end service_appliance_user_credentials

    def set_service_appliance_user_credentials(self, value):
        self.service_appliance_user_credentials = value
    #end set_service_appliance_user_credentials

    @pycontrail.gen.resource_common.ServiceAppliance.service_appliance_ip_address.setter
    def service_appliance_ip_address(self, service_appliance_ip_address):
        """Set service-appliance-ip-address for service-appliance.
        
        :param service_appliance_ip_address: IpAddressType object
        
        """
        if 'service_appliance_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('service_appliance_ip_address')

        self._service_appliance_ip_address = service_appliance_ip_address
    #end service_appliance_ip_address

    def set_service_appliance_ip_address(self, value):
        self.service_appliance_ip_address = value
    #end set_service_appliance_ip_address

    @pycontrail.gen.resource_common.ServiceAppliance.service_appliance_properties.setter
    def service_appliance_properties(self, service_appliance_properties):
        """Set service-appliance-properties for service-appliance.
        
        :param service_appliance_properties: KeyValuePairs object
        
        """
        if 'service_appliance_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('service_appliance_properties')

        self._service_appliance_properties = service_appliance_properties
    #end service_appliance_properties

    def set_service_appliance_properties(self, value):
        self.service_appliance_properties = value
    #end set_service_appliance_properties

    @pycontrail.gen.resource_common.ServiceAppliance.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-appliance.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ServiceAppliance.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-appliance.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ServiceAppliance.display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-appliance.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_physical_interface(self, *args, **kwargs):
        """Set physical-interface for service-appliance.
        
        :param ref_obj: PhysicalInterface object
        :param ref_data: ServiceApplianceInterfaceType object
        
        """
        self._pending_field_updates.add('physical_interface_refs')
        self._pending_ref_updates.discard('physical_interface_refs')
        super(ServiceAppliance, self).set_physical_interface(*args, **kwargs)

    #end set_physical_interface

    def add_physical_interface(self, *args, **kwargs):
        """Add physical-interface to service-appliance.
        
        :param ref_obj: PhysicalInterface object
        :param ref_data: ServiceApplianceInterfaceType object
        
        """
        if 'physical_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('physical_interface_refs')
            self._original_physical_interface_refs = (self.get_physical_interface_refs() or [])[:]
        super(ServiceAppliance, self).add_physical_interface(*args, **kwargs)
    #end add_physical_interface

    def del_physical_interface(self, *args, **kwargs):
        if 'physical_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('physical_interface_refs')
            self._original_physical_interface_refs = (self.get_physical_interface_refs() or [])[:]
        super(ServiceAppliance, self).del_physical_interface(*args, **kwargs)
    #end del_physical_interface

    def set_physical_interface_list(self, *args, **kwargs):
        """Set physical-interface list for service-appliance.
        
        :param ref_obj_list: list of PhysicalInterface object
        :param ref_data_list: list of ServiceApplianceInterfaceType summary
        
        """
        self._pending_field_updates.add('physical_interface_refs')
        self._pending_ref_updates.discard('physical_interface_refs')
        super(ServiceAppliance, self).set_physical_interface_list(*args, **kwargs)
    #end set_physical_interface_list


#end class ServiceAppliance

class RoutingPolicy(pycontrail.gen.resource_common.RoutingPolicy):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, routing_policy_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if routing_policy_entries is not None:
            pending_fields.append('routing_policy_entries')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(RoutingPolicy, self).__init__(name, parent_obj, routing_policy_entries, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'routing_policy_entries' in kwargs:
            if kwargs['routing_policy_entries'] is None:
                props_dict['routing_policy_entries'] = None
            else:
                props_dict['routing_policy_entries'] = pycontrail.gen.resource_xsd.PolicyStatementType(**kwargs['routing_policy_entries'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = RoutingPolicy(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']
            for ref in obj.service_instance_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.RoutingPolicyServiceInstanceType(**ref['attr'])
        if 'routing_instance_refs' in kwargs:
            obj.routing_instance_refs = kwargs['routing_instance_refs']
            for ref in obj.routing_instance_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.RoutingPolicyType(**ref['attr'])

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.RoutingPolicy.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.RoutingPolicy.routing_policy_entries.setter
    def routing_policy_entries(self, routing_policy_entries):
        """Set routing-policy-entries for routing-policy.
        
        :param routing_policy_entries: PolicyStatementType object
        
        """
        if 'routing_policy_entries' not in self._pending_field_updates:
            self._pending_field_updates.add('routing_policy_entries')

        self._routing_policy_entries = routing_policy_entries
    #end routing_policy_entries

    def set_routing_policy_entries(self, value):
        self.routing_policy_entries = value
    #end set_routing_policy_entries

    @pycontrail.gen.resource_common.RoutingPolicy.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for routing-policy.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.RoutingPolicy.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for routing-policy.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.RoutingPolicy.display_name.setter
    def display_name(self, display_name):
        """Set display-name for routing-policy.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for routing-policy.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: RoutingPolicyServiceInstanceType object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(RoutingPolicy, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to routing-policy.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: RoutingPolicyServiceInstanceType object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(RoutingPolicy, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(RoutingPolicy, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for routing-policy.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of RoutingPolicyServiceInstanceType summary
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(RoutingPolicy, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list

    def set_routing_instance(self, *args, **kwargs):
        """Set routing-instance for routing-policy.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: RoutingPolicyType object
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(RoutingPolicy, self).set_routing_instance(*args, **kwargs)

    #end set_routing_instance

    def add_routing_instance(self, *args, **kwargs):
        """Add routing-instance to routing-policy.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: RoutingPolicyType object
        
        """
        if 'routing_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(RoutingPolicy, self).add_routing_instance(*args, **kwargs)
    #end add_routing_instance

    def del_routing_instance(self, *args, **kwargs):
        if 'routing_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(RoutingPolicy, self).del_routing_instance(*args, **kwargs)
    #end del_routing_instance

    def set_routing_instance_list(self, *args, **kwargs):
        """Set routing-instance list for routing-policy.
        
        :param ref_obj_list: list of RoutingInstance object
        :param ref_data_list: list of RoutingPolicyType summary
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(RoutingPolicy, self).set_routing_instance_list(*args, **kwargs)
    #end set_routing_instance_list


#end class RoutingPolicy

class Namespace(pycontrail.gen.resource_common.Namespace):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, namespace_cidr=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if namespace_cidr is not None:
            pending_fields.append('namespace_cidr')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(Namespace, self).__init__(name, parent_obj, namespace_cidr, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'namespace_cidr' in kwargs:
            if kwargs['namespace_cidr'] is None:
                props_dict['namespace_cidr'] = None
            else:
                props_dict['namespace_cidr'] = pycontrail.gen.resource_xsd.SubnetType(**kwargs['namespace_cidr'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = Namespace(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...
        if 'project_back_refs' in kwargs:
            obj.project_back_refs = kwargs['project_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.Namespace.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.Namespace.namespace_cidr.setter
    def namespace_cidr(self, namespace_cidr):
        """Set namespace-cidr for namespace.
        
        :param namespace_cidr: SubnetType object
        
        """
        if 'namespace_cidr' not in self._pending_field_updates:
            self._pending_field_updates.add('namespace_cidr')

        self._namespace_cidr = namespace_cidr
    #end namespace_cidr

    def set_namespace_cidr(self, value):
        self.namespace_cidr = value
    #end set_namespace_cidr

    @pycontrail.gen.resource_common.Namespace.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for namespace.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.Namespace.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for namespace.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.Namespace.display_name.setter
    def display_name(self, display_name):
        """Set display-name for namespace.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


    def get_project_back_refs(self):
        """Return list of all projects using this namespace"""
        back_refs = super(Namespace, self).get_project_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.namespace_read(id = self.uuid, fields = ['project_back_refs'])
        back_refs = getattr(obj, 'project_back_refs', None)
        self.project_back_refs = back_refs

        return back_refs
    #end get_project_back_refs

#end class Namespace

class LogicalInterface(pycontrail.gen.resource_common.LogicalInterface):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, logical_interface_vlan_tag=None, logical_interface_type=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if logical_interface_vlan_tag is not None:
            pending_fields.append('logical_interface_vlan_tag')
        if logical_interface_type is not None:
            pending_fields.append('logical_interface_type')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(LogicalInterface, self).__init__(name, parent_obj, logical_interface_vlan_tag, logical_interface_type, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'logical_interface_vlan_tag' in kwargs:
            props_dict['logical_interface_vlan_tag'] = kwargs['logical_interface_vlan_tag']
        if 'logical_interface_type' in kwargs:
            props_dict['logical_interface_type'] = kwargs['logical_interface_type']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = LogicalInterface(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.LogicalInterface.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.LogicalInterface.logical_interface_vlan_tag.setter
    def logical_interface_vlan_tag(self, logical_interface_vlan_tag):
        """Set logical-interface-vlan-tag for logical-interface.
        
        :param logical_interface_vlan_tag: xsd:integer object
        
        """
        if 'logical_interface_vlan_tag' not in self._pending_field_updates:
            self._pending_field_updates.add('logical_interface_vlan_tag')

        self._logical_interface_vlan_tag = logical_interface_vlan_tag
    #end logical_interface_vlan_tag

    def set_logical_interface_vlan_tag(self, value):
        self.logical_interface_vlan_tag = value
    #end set_logical_interface_vlan_tag

    @pycontrail.gen.resource_common.LogicalInterface.logical_interface_type.setter
    def logical_interface_type(self, logical_interface_type):
        """Set logical-interface-type for logical-interface.
        
        :param logical_interface_type: LogicalInterfaceType object
        
        """
        if 'logical_interface_type' not in self._pending_field_updates:
            self._pending_field_updates.add('logical_interface_type')

        self._logical_interface_type = logical_interface_type
    #end logical_interface_type

    def set_logical_interface_type(self, value):
        self.logical_interface_type = value
    #end set_logical_interface_type

    @pycontrail.gen.resource_common.LogicalInterface.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for logical-interface.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.LogicalInterface.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for logical-interface.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.LogicalInterface.display_name.setter
    def display_name(self, display_name):
        """Set display-name for logical-interface.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for logical-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(LogicalInterface, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to logical-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(LogicalInterface, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(LogicalInterface, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for logical-interface.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(LogicalInterface, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list


#end class LogicalInterface

class ServiceInstance(pycontrail.gen.resource_common.ServiceInstance):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, service_instance_properties=None, service_instance_bindings=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if service_instance_properties is not None:
            pending_fields.append('service_instance_properties')
        if service_instance_bindings is not None:
            pending_fields.append('service_instance_bindings')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ServiceInstance, self).__init__(name, parent_obj, service_instance_properties, service_instance_bindings, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'service_instance_properties' in kwargs:
            if kwargs['service_instance_properties'] is None:
                props_dict['service_instance_properties'] = None
            else:
                props_dict['service_instance_properties'] = pycontrail.gen.resource_xsd.ServiceInstanceType(**kwargs['service_instance_properties'])
        if 'service_instance_bindings' in kwargs:
            if kwargs['service_instance_bindings'] is None:
                props_dict['service_instance_bindings'] = None
            else:
                props_dict['service_instance_bindings'] = pycontrail.gen.resource_xsd.KeyValuePairs(**kwargs['service_instance_bindings'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ServiceInstance(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'port_tuples' in kwargs:
            obj.port_tuples = kwargs['port_tuples']

        # add any specified references...
        if 'service_template_refs' in kwargs:
            obj.service_template_refs = kwargs['service_template_refs']
        if 'instance_ip_refs' in kwargs:
            obj.instance_ip_refs = kwargs['instance_ip_refs']
            for ref in obj.instance_ip_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.ServiceInterfaceTag(**ref['attr'])

        # and back references but no obj api for it...
        if 'virtual_machine_back_refs' in kwargs:
            obj.virtual_machine_back_refs = kwargs['virtual_machine_back_refs']
        if 'service_health_check_back_refs' in kwargs:
            obj.service_health_check_back_refs = kwargs['service_health_check_back_refs']
        if 'interface_route_table_back_refs' in kwargs:
            obj.interface_route_table_back_refs = kwargs['interface_route_table_back_refs']
        if 'routing_policy_back_refs' in kwargs:
            obj.routing_policy_back_refs = kwargs['routing_policy_back_refs']
        if 'route_aggregate_back_refs' in kwargs:
            obj.route_aggregate_back_refs = kwargs['route_aggregate_back_refs']
        if 'logical_router_back_refs' in kwargs:
            obj.logical_router_back_refs = kwargs['logical_router_back_refs']
        if 'loadbalancer_pool_back_refs' in kwargs:
            obj.loadbalancer_pool_back_refs = kwargs['loadbalancer_pool_back_refs']
        if 'loadbalancer_back_refs' in kwargs:
            obj.loadbalancer_back_refs = kwargs['loadbalancer_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ServiceInstance.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ServiceInstance.service_instance_properties.setter
    def service_instance_properties(self, service_instance_properties):
        """Set service-instance-properties for service-instance.
        
        :param service_instance_properties: ServiceInstanceType object
        
        """
        if 'service_instance_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('service_instance_properties')

        self._service_instance_properties = service_instance_properties
    #end service_instance_properties

    def set_service_instance_properties(self, value):
        self.service_instance_properties = value
    #end set_service_instance_properties

    @pycontrail.gen.resource_common.ServiceInstance.service_instance_bindings.setter
    def service_instance_bindings(self, service_instance_bindings):
        """Set service-instance-bindings for service-instance.
        
        :param service_instance_bindings: KeyValuePairs object
        
        """
        if 'service_instance_bindings' not in self._pending_field_updates:
            self._pending_field_updates.add('service_instance_bindings')

        if 'service_instance_bindings' in self._pending_field_map_updates:
            # set clobbers earlier add/del on prop map elements
            del self._pending_field_map_updates['service_instance_bindings']

        self._service_instance_bindings = service_instance_bindings
    #end service_instance_bindings

    def set_service_instance_bindings(self, value):
        self.service_instance_bindings = value
    #end set_service_instance_bindings

    @pycontrail.gen.resource_common.ServiceInstance.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-instance.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ServiceInstance.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-instance.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ServiceInstance.display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-instance.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def add_service_instance_bindings(self, elem):
        """Add element to service-instance-bindings for service-instance.
        
        :param elem: xsd:string object
        
        """
        elem_position = getattr(elem, 'key')
        if 'service_instance_bindings' not in self._pending_field_map_updates:
            self._pending_field_map_updates['service_instance_bindings'] = [
                ('set', elem, elem_position)]
        else:
            self._pending_field_map_updates['service_instance_bindings'].append(
                ('set', elem, elem_position))
    #end set_service_instance_bindings

    def del_service_instance_bindings(self, elem_position):
        """Delete element from service-instance-bindings for service-instance.
        
        :param elem_position: string indicating map-key
        
        """
        if 'service_instance_bindings' not in self._pending_field_map_updates:
            self._pending_field_map_updates['service_instance_bindings'] = [
                ('delete', None, elem_position)]
        else:
            self._pending_field_map_updates['service_instance_bindings'].append(
                ('delete', None, elem_position))
    #end del_service_instance_bindings
    def set_service_template(self, *args, **kwargs):
        """Set service-template for service-instance.
        
        :param ref_obj: ServiceTemplate object
        
        """
        self._pending_field_updates.add('service_template_refs')
        self._pending_ref_updates.discard('service_template_refs')
        super(ServiceInstance, self).set_service_template(*args, **kwargs)

    #end set_service_template

    def add_service_template(self, *args, **kwargs):
        """Add service-template to service-instance.
        
        :param ref_obj: ServiceTemplate object
        
        """
        if 'service_template_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_template_refs')
            self._original_service_template_refs = (self.get_service_template_refs() or [])[:]
        super(ServiceInstance, self).add_service_template(*args, **kwargs)
    #end add_service_template

    def del_service_template(self, *args, **kwargs):
        if 'service_template_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_template_refs')
            self._original_service_template_refs = (self.get_service_template_refs() or [])[:]
        super(ServiceInstance, self).del_service_template(*args, **kwargs)
    #end del_service_template

    def set_service_template_list(self, *args, **kwargs):
        """Set service-template list for service-instance.
        
        :param ref_obj_list: list of ServiceTemplate object
        
        """
        self._pending_field_updates.add('service_template_refs')
        self._pending_ref_updates.discard('service_template_refs')
        super(ServiceInstance, self).set_service_template_list(*args, **kwargs)
    #end set_service_template_list

    def set_instance_ip(self, *args, **kwargs):
        """Set instance-ip for service-instance.
        
        :param ref_obj: InstanceIp object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self._pending_field_updates.add('instance_ip_refs')
        self._pending_ref_updates.discard('instance_ip_refs')
        super(ServiceInstance, self).set_instance_ip(*args, **kwargs)

    #end set_instance_ip

    def add_instance_ip(self, *args, **kwargs):
        """Add instance-ip to service-instance.
        
        :param ref_obj: InstanceIp object
        :param ref_data: ServiceInterfaceTag object
        
        """
        if 'instance_ip_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('instance_ip_refs')
            self._original_instance_ip_refs = (self.get_instance_ip_refs() or [])[:]
        super(ServiceInstance, self).add_instance_ip(*args, **kwargs)
    #end add_instance_ip

    def del_instance_ip(self, *args, **kwargs):
        if 'instance_ip_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('instance_ip_refs')
            self._original_instance_ip_refs = (self.get_instance_ip_refs() or [])[:]
        super(ServiceInstance, self).del_instance_ip(*args, **kwargs)
    #end del_instance_ip

    def set_instance_ip_list(self, *args, **kwargs):
        """Set instance-ip list for service-instance.
        
        :param ref_obj_list: list of InstanceIp object
        :param ref_data_list: list of ServiceInterfaceTag summary
        
        """
        self._pending_field_updates.add('instance_ip_refs')
        self._pending_ref_updates.discard('instance_ip_refs')
        super(ServiceInstance, self).set_instance_ip_list(*args, **kwargs)
    #end set_instance_ip_list

    def get_port_tuples(self):
        children = super(ServiceInstance, self).get_port_tuples()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.service_instance_read(id = self.uuid, fields = ['port_tuples'])
            children = getattr(obj, 'port_tuples', None)
            self.port_tuples = children

        return children
    #end get_port_tuples


    def get_virtual_machine_back_refs(self):
        """Return list of all virtual-machines using this service-instance"""
        back_refs = super(ServiceInstance, self).get_virtual_machine_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['virtual_machine_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_back_refs', None)
        self.virtual_machine_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_back_refs

    def get_service_health_check_back_refs(self):
        """Return list of all service-health-checks using this service-instance"""
        back_refs = super(ServiceInstance, self).get_service_health_check_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['service_health_check_back_refs'])
        back_refs = getattr(obj, 'service_health_check_back_refs', None)
        self.service_health_check_back_refs = back_refs

        return back_refs
    #end get_service_health_check_back_refs

    def get_interface_route_table_back_refs(self):
        """Return list of all interface-route-tables using this service-instance"""
        back_refs = super(ServiceInstance, self).get_interface_route_table_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['interface_route_table_back_refs'])
        back_refs = getattr(obj, 'interface_route_table_back_refs', None)
        self.interface_route_table_back_refs = back_refs

        return back_refs
    #end get_interface_route_table_back_refs

    def get_routing_policy_back_refs(self):
        """Return list of all routing-policys using this service-instance"""
        back_refs = super(ServiceInstance, self).get_routing_policy_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['routing_policy_back_refs'])
        back_refs = getattr(obj, 'routing_policy_back_refs', None)
        self.routing_policy_back_refs = back_refs

        return back_refs
    #end get_routing_policy_back_refs

    def get_route_aggregate_back_refs(self):
        """Return list of all route-aggregates using this service-instance"""
        back_refs = super(ServiceInstance, self).get_route_aggregate_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['route_aggregate_back_refs'])
        back_refs = getattr(obj, 'route_aggregate_back_refs', None)
        self.route_aggregate_back_refs = back_refs

        return back_refs
    #end get_route_aggregate_back_refs

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this service-instance"""
        back_refs = super(ServiceInstance, self).get_logical_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['logical_router_back_refs'])
        back_refs = getattr(obj, 'logical_router_back_refs', None)
        self.logical_router_back_refs = back_refs

        return back_refs
    #end get_logical_router_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this service-instance"""
        back_refs = super(ServiceInstance, self).get_loadbalancer_pool_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['loadbalancer_pool_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_pool_back_refs', None)
        self.loadbalancer_pool_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_pool_back_refs

    def get_loadbalancer_back_refs(self):
        """Return list of all loadbalancers using this service-instance"""
        back_refs = super(ServiceInstance, self).get_loadbalancer_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_instance_read(id = self.uuid, fields = ['loadbalancer_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_back_refs', None)
        self.loadbalancer_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_back_refs

#end class ServiceInstance

class RouteTable(pycontrail.gen.resource_common.RouteTable):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, routes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if routes is not None:
            pending_fields.append('routes')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(RouteTable, self).__init__(name, parent_obj, routes, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'routes' in kwargs:
            if kwargs['routes'] is None:
                props_dict['routes'] = None
            else:
                props_dict['routes'] = pycontrail.gen.resource_xsd.RouteTableType(**kwargs['routes'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = RouteTable(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...
        if 'virtual_network_back_refs' in kwargs:
            obj.virtual_network_back_refs = kwargs['virtual_network_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.RouteTable.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.RouteTable.routes.setter
    def routes(self, routes):
        """Set routes for route-table.
        
        :param routes: RouteTableType object
        
        """
        if 'routes' not in self._pending_field_updates:
            self._pending_field_updates.add('routes')

        self._routes = routes
    #end routes

    def set_routes(self, value):
        self.routes = value
    #end set_routes

    @pycontrail.gen.resource_common.RouteTable.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for route-table.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.RouteTable.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for route-table.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.RouteTable.display_name.setter
    def display_name(self, display_name):
        """Set display-name for route-table.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this route-table"""
        back_refs = super(RouteTable, self).get_virtual_network_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.route_table_read(id = self.uuid, fields = ['virtual_network_back_refs'])
        back_refs = getattr(obj, 'virtual_network_back_refs', None)
        self.virtual_network_back_refs = back_refs

        return back_refs
    #end get_virtual_network_back_refs

#end class RouteTable

class PhysicalInterface(pycontrail.gen.resource_common.PhysicalInterface):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(PhysicalInterface, self).__init__(name, parent_obj, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = PhysicalInterface(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'logical_interfaces' in kwargs:
            obj.logical_interfaces = kwargs['logical_interfaces']

        # add any specified references...
        if 'physical_interface_refs' in kwargs:
            obj.physical_interface_refs = kwargs['physical_interface_refs']

        # and back references but no obj api for it...
        if 'service_appliance_back_refs' in kwargs:
            obj.service_appliance_back_refs = kwargs['service_appliance_back_refs']
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']
        if 'physical_interface_back_refs' in kwargs:
            obj.physical_interface_back_refs = kwargs['physical_interface_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.PhysicalInterface.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.PhysicalInterface.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for physical-interface.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.PhysicalInterface.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for physical-interface.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.PhysicalInterface.display_name.setter
    def display_name(self, display_name):
        """Set display-name for physical-interface.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_physical_interface(self, *args, **kwargs):
        """Set physical-interface for physical-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        self._pending_field_updates.add('physical_interface_refs')
        self._pending_ref_updates.discard('physical_interface_refs')
        super(PhysicalInterface, self).set_physical_interface(*args, **kwargs)

    #end set_physical_interface

    def add_physical_interface(self, *args, **kwargs):
        """Add physical-interface to physical-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        if 'physical_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('physical_interface_refs')
            self._original_physical_interface_refs = (self.get_physical_interface_refs() or [])[:]
        super(PhysicalInterface, self).add_physical_interface(*args, **kwargs)
    #end add_physical_interface

    def del_physical_interface(self, *args, **kwargs):
        if 'physical_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('physical_interface_refs')
            self._original_physical_interface_refs = (self.get_physical_interface_refs() or [])[:]
        super(PhysicalInterface, self).del_physical_interface(*args, **kwargs)
    #end del_physical_interface

    def set_physical_interface_list(self, *args, **kwargs):
        """Set physical-interface list for physical-interface.
        
        :param ref_obj_list: list of PhysicalInterface object
        
        """
        self._pending_field_updates.add('physical_interface_refs')
        self._pending_ref_updates.discard('physical_interface_refs')
        super(PhysicalInterface, self).set_physical_interface_list(*args, **kwargs)
    #end set_physical_interface_list

    def get_logical_interfaces(self):
        children = super(PhysicalInterface, self).get_logical_interfaces()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.physical_interface_read(id = self.uuid, fields = ['logical_interfaces'])
            children = getattr(obj, 'logical_interfaces', None)
            self.logical_interfaces = children

        return children
    #end get_logical_interfaces


    def get_service_appliance_back_refs(self):
        """Return list of all service-appliances using this physical-interface"""
        back_refs = super(PhysicalInterface, self).get_service_appliance_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.physical_interface_read(id = self.uuid, fields = ['service_appliance_back_refs'])
        back_refs = getattr(obj, 'service_appliance_back_refs', None)
        self.service_appliance_back_refs = back_refs

        return back_refs
    #end get_service_appliance_back_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this physical-interface"""
        back_refs = super(PhysicalInterface, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.physical_interface_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

    def get_physical_interface_back_refs(self):
        """Return list of all physical-interfaces using this physical-interface"""
        back_refs = super(PhysicalInterface, self).get_physical_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.physical_interface_read(id = self.uuid, fields = ['physical_interface_back_refs'])
        back_refs = getattr(obj, 'physical_interface_back_refs', None)
        self.physical_interface_back_refs = back_refs

        return back_refs
    #end get_physical_interface_back_refs

#end class PhysicalInterface

class AccessControlList(pycontrail.gen.resource_common.AccessControlList):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, access_control_list_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if access_control_list_entries is not None:
            pending_fields.append('access_control_list_entries')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(AccessControlList, self).__init__(name, parent_obj, access_control_list_entries, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'access_control_list_entries' in kwargs:
            if kwargs['access_control_list_entries'] is None:
                props_dict['access_control_list_entries'] = None
            else:
                props_dict['access_control_list_entries'] = pycontrail.gen.resource_xsd.AclEntriesType(**kwargs['access_control_list_entries'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = AccessControlList(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.AccessControlList.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.AccessControlList.access_control_list_entries.setter
    def access_control_list_entries(self, access_control_list_entries):
        """Set access-control-list-entries for access-control-list.
        
        :param access_control_list_entries: AclEntriesType object
        
        """
        if 'access_control_list_entries' not in self._pending_field_updates:
            self._pending_field_updates.add('access_control_list_entries')

        self._access_control_list_entries = access_control_list_entries
    #end access_control_list_entries

    def set_access_control_list_entries(self, value):
        self.access_control_list_entries = value
    #end set_access_control_list_entries

    @pycontrail.gen.resource_common.AccessControlList.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for access-control-list.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.AccessControlList.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for access-control-list.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.AccessControlList.display_name.setter
    def display_name(self, display_name):
        """Set display-name for access-control-list.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class AccessControlList

class BgpAsAService(pycontrail.gen.resource_common.BgpAsAService):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, autonomous_system=None, bgpaas_ip_address=None, bgpaas_session_attributes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if autonomous_system is not None:
            pending_fields.append('autonomous_system')
        if bgpaas_ip_address is not None:
            pending_fields.append('bgpaas_ip_address')
        if bgpaas_session_attributes is not None:
            pending_fields.append('bgpaas_session_attributes')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(BgpAsAService, self).__init__(name, parent_obj, autonomous_system, bgpaas_ip_address, bgpaas_session_attributes, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'autonomous_system' in kwargs:
            props_dict['autonomous_system'] = kwargs['autonomous_system']
        if 'bgpaas_ip_address' in kwargs:
            props_dict['bgpaas_ip_address'] = kwargs['bgpaas_ip_address']
        if 'bgpaas_session_attributes' in kwargs:
            if kwargs['bgpaas_session_attributes'] is None:
                props_dict['bgpaas_session_attributes'] = None
            else:
                props_dict['bgpaas_session_attributes'] = pycontrail.gen.resource_xsd.BgpSessionAttributes(**kwargs['bgpaas_session_attributes'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = BgpAsAService(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']
        if 'bgp_router_refs' in kwargs:
            obj.bgp_router_refs = kwargs['bgp_router_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.BgpAsAService.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.BgpAsAService.autonomous_system.setter
    def autonomous_system(self, autonomous_system):
        """Set autonomous-system for bgp-as-a-service.
        
        :param autonomous_system: AutonomousSystemType object
        
        """
        if 'autonomous_system' not in self._pending_field_updates:
            self._pending_field_updates.add('autonomous_system')

        self._autonomous_system = autonomous_system
    #end autonomous_system

    def set_autonomous_system(self, value):
        self.autonomous_system = value
    #end set_autonomous_system

    @pycontrail.gen.resource_common.BgpAsAService.bgpaas_ip_address.setter
    def bgpaas_ip_address(self, bgpaas_ip_address):
        """Set bgpaas-ip-address for bgp-as-a-service.
        
        :param bgpaas_ip_address: IpAddressType object
        
        """
        if 'bgpaas_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('bgpaas_ip_address')

        self._bgpaas_ip_address = bgpaas_ip_address
    #end bgpaas_ip_address

    def set_bgpaas_ip_address(self, value):
        self.bgpaas_ip_address = value
    #end set_bgpaas_ip_address

    @pycontrail.gen.resource_common.BgpAsAService.bgpaas_session_attributes.setter
    def bgpaas_session_attributes(self, bgpaas_session_attributes):
        """Set bgpaas-session-attributes for bgp-as-a-service.
        
        :param bgpaas_session_attributes: BgpSessionAttributes object
        
        """
        if 'bgpaas_session_attributes' not in self._pending_field_updates:
            self._pending_field_updates.add('bgpaas_session_attributes')

        self._bgpaas_session_attributes = bgpaas_session_attributes
    #end bgpaas_session_attributes

    def set_bgpaas_session_attributes(self, value):
        self.bgpaas_session_attributes = value
    #end set_bgpaas_session_attributes

    @pycontrail.gen.resource_common.BgpAsAService.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for bgp-as-a-service.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.BgpAsAService.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for bgp-as-a-service.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.BgpAsAService.display_name.setter
    def display_name(self, display_name):
        """Set display-name for bgp-as-a-service.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for bgp-as-a-service.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(BgpAsAService, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to bgp-as-a-service.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(BgpAsAService, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(BgpAsAService, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for bgp-as-a-service.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(BgpAsAService, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list

    def set_bgp_router(self, *args, **kwargs):
        """Set bgp-router for bgp-as-a-service.
        
        :param ref_obj: BgpRouter object
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(BgpAsAService, self).set_bgp_router(*args, **kwargs)

    #end set_bgp_router

    def add_bgp_router(self, *args, **kwargs):
        """Add bgp-router to bgp-as-a-service.
        
        :param ref_obj: BgpRouter object
        
        """
        if 'bgp_router_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(BgpAsAService, self).add_bgp_router(*args, **kwargs)
    #end add_bgp_router

    def del_bgp_router(self, *args, **kwargs):
        if 'bgp_router_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('bgp_router_refs')
            self._original_bgp_router_refs = (self.get_bgp_router_refs() or [])[:]
        super(BgpAsAService, self).del_bgp_router(*args, **kwargs)
    #end del_bgp_router

    def set_bgp_router_list(self, *args, **kwargs):
        """Set bgp-router list for bgp-as-a-service.
        
        :param ref_obj_list: list of BgpRouter object
        
        """
        self._pending_field_updates.add('bgp_router_refs')
        self._pending_ref_updates.discard('bgp_router_refs')
        super(BgpAsAService, self).set_bgp_router_list(*args, **kwargs)
    #end set_bgp_router_list


#end class BgpAsAService

class PortTuple(pycontrail.gen.resource_common.PortTuple):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(PortTuple, self).__init__(name, parent_obj, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = PortTuple(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.PortTuple.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.PortTuple.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for port-tuple.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.PortTuple.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for port-tuple.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.PortTuple.display_name.setter
    def display_name(self, display_name):
        """Set display-name for port-tuple.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this port-tuple"""
        back_refs = super(PortTuple, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.port_tuple_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

#end class PortTuple

class AnalyticsNode(pycontrail.gen.resource_common.AnalyticsNode):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, analytics_node_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if analytics_node_ip_address is not None:
            pending_fields.append('analytics_node_ip_address')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(AnalyticsNode, self).__init__(name, parent_obj, analytics_node_ip_address, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'analytics_node_ip_address' in kwargs:
            props_dict['analytics_node_ip_address'] = kwargs['analytics_node_ip_address']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = AnalyticsNode(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.AnalyticsNode.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.AnalyticsNode.analytics_node_ip_address.setter
    def analytics_node_ip_address(self, analytics_node_ip_address):
        """Set analytics-node-ip-address for analytics-node.
        
        :param analytics_node_ip_address: IpAddressType object
        
        """
        if 'analytics_node_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('analytics_node_ip_address')

        self._analytics_node_ip_address = analytics_node_ip_address
    #end analytics_node_ip_address

    def set_analytics_node_ip_address(self, value):
        self.analytics_node_ip_address = value
    #end set_analytics_node_ip_address

    @pycontrail.gen.resource_common.AnalyticsNode.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for analytics-node.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.AnalyticsNode.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for analytics-node.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.AnalyticsNode.display_name.setter
    def display_name(self, display_name):
        """Set display-name for analytics-node.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class AnalyticsNode

class VirtualDns(pycontrail.gen.resource_common.VirtualDns):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, virtual_DNS_data=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if virtual_DNS_data is not None:
            pending_fields.append('virtual_DNS_data')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(VirtualDns, self).__init__(name, parent_obj, virtual_DNS_data, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'virtual_DNS_data' in kwargs:
            if kwargs['virtual_DNS_data'] is None:
                props_dict['virtual_DNS_data'] = None
            else:
                props_dict['virtual_DNS_data'] = pycontrail.gen.resource_xsd.VirtualDnsType(**kwargs['virtual_DNS_data'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = VirtualDns(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'virtual_DNS_records' in kwargs:
            obj.virtual_DNS_records = kwargs['virtual_DNS_records']

        # add any specified references...

        # and back references but no obj api for it...
        if 'network_ipam_back_refs' in kwargs:
            obj.network_ipam_back_refs = kwargs['network_ipam_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.VirtualDns.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.VirtualDns.virtual_DNS_data.setter
    def virtual_DNS_data(self, virtual_DNS_data):
        """Set virtual-DNS-data for virtual-DNS.
        
        :param virtual_DNS_data: VirtualDnsType object
        
        """
        if 'virtual_DNS_data' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_DNS_data')

        self._virtual_DNS_data = virtual_DNS_data
    #end virtual_DNS_data

    def set_virtual_DNS_data(self, value):
        self.virtual_DNS_data = value
    #end set_virtual_DNS_data

    @pycontrail.gen.resource_common.VirtualDns.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-DNS.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.VirtualDns.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-DNS.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.VirtualDns.display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-DNS.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_virtual_DNS_records(self):
        children = super(VirtualDns, self).get_virtual_DNS_records()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.virtual_DNS_read(id = self.uuid, fields = ['virtual_DNS_records'])
            children = getattr(obj, 'virtual_DNS_records', None)
            self.virtual_DNS_records = children

        return children
    #end get_virtual_DNS_records


    def get_network_ipam_back_refs(self):
        """Return list of all network-ipams using this virtual-DNS"""
        back_refs = super(VirtualDns, self).get_network_ipam_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_DNS_read(id = self.uuid, fields = ['network_ipam_back_refs'])
        back_refs = getattr(obj, 'network_ipam_back_refs', None)
        self.network_ipam_back_refs = back_refs

        return back_refs
    #end get_network_ipam_back_refs

#end class VirtualDns

class CustomerAttachment(pycontrail.gen.resource_common.CustomerAttachment):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, attachment_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if attachment_address is not None:
            pending_fields.append('attachment_address')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(CustomerAttachment, self).__init__(name, attachment_address, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'attachment_address' in kwargs:
            if kwargs['attachment_address'] is None:
                props_dict['attachment_address'] = None
            else:
                props_dict['attachment_address'] = pycontrail.gen.resource_xsd.AttachmentAddressType(**kwargs['attachment_address'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = CustomerAttachment(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']
        if 'floating_ip_refs' in kwargs:
            obj.floating_ip_refs = kwargs['floating_ip_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.CustomerAttachment.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.CustomerAttachment.attachment_address.setter
    def attachment_address(self, attachment_address):
        """Set attachment-address for customer-attachment.
        
        :param attachment_address: AttachmentAddressType object
        
        """
        if 'attachment_address' not in self._pending_field_updates:
            self._pending_field_updates.add('attachment_address')

        self._attachment_address = attachment_address
    #end attachment_address

    def set_attachment_address(self, value):
        self.attachment_address = value
    #end set_attachment_address

    @pycontrail.gen.resource_common.CustomerAttachment.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for customer-attachment.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.CustomerAttachment.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for customer-attachment.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.CustomerAttachment.display_name.setter
    def display_name(self, display_name):
        """Set display-name for customer-attachment.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for customer-attachment.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(CustomerAttachment, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to customer-attachment.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(CustomerAttachment, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(CustomerAttachment, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for customer-attachment.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(CustomerAttachment, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list

    def set_floating_ip(self, *args, **kwargs):
        """Set floating-ip for customer-attachment.
        
        :param ref_obj: FloatingIp object
        
        """
        self._pending_field_updates.add('floating_ip_refs')
        self._pending_ref_updates.discard('floating_ip_refs')
        super(CustomerAttachment, self).set_floating_ip(*args, **kwargs)

    #end set_floating_ip

    def add_floating_ip(self, *args, **kwargs):
        """Add floating-ip to customer-attachment.
        
        :param ref_obj: FloatingIp object
        
        """
        if 'floating_ip_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('floating_ip_refs')
            self._original_floating_ip_refs = (self.get_floating_ip_refs() or [])[:]
        super(CustomerAttachment, self).add_floating_ip(*args, **kwargs)
    #end add_floating_ip

    def del_floating_ip(self, *args, **kwargs):
        if 'floating_ip_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('floating_ip_refs')
            self._original_floating_ip_refs = (self.get_floating_ip_refs() or [])[:]
        super(CustomerAttachment, self).del_floating_ip(*args, **kwargs)
    #end del_floating_ip

    def set_floating_ip_list(self, *args, **kwargs):
        """Set floating-ip list for customer-attachment.
        
        :param ref_obj_list: list of FloatingIp object
        
        """
        self._pending_field_updates.add('floating_ip_refs')
        self._pending_ref_updates.discard('floating_ip_refs')
        super(CustomerAttachment, self).set_floating_ip_list(*args, **kwargs)
    #end set_floating_ip_list


#end class CustomerAttachment

class ServiceApplianceSet(pycontrail.gen.resource_common.ServiceApplianceSet):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, service_appliance_set_properties=None, service_appliance_driver=None, service_appliance_ha_mode=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if service_appliance_set_properties is not None:
            pending_fields.append('service_appliance_set_properties')
        if service_appliance_driver is not None:
            pending_fields.append('service_appliance_driver')
        if service_appliance_ha_mode is not None:
            pending_fields.append('service_appliance_ha_mode')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ServiceApplianceSet, self).__init__(name, parent_obj, service_appliance_set_properties, service_appliance_driver, service_appliance_ha_mode, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'service_appliance_set_properties' in kwargs:
            if kwargs['service_appliance_set_properties'] is None:
                props_dict['service_appliance_set_properties'] = None
            else:
                props_dict['service_appliance_set_properties'] = pycontrail.gen.resource_xsd.KeyValuePairs(**kwargs['service_appliance_set_properties'])
        if 'service_appliance_driver' in kwargs:
            props_dict['service_appliance_driver'] = kwargs['service_appliance_driver']
        if 'service_appliance_ha_mode' in kwargs:
            props_dict['service_appliance_ha_mode'] = kwargs['service_appliance_ha_mode']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ServiceApplianceSet(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'service_appliances' in kwargs:
            obj.service_appliances = kwargs['service_appliances']

        # add any specified references...

        # and back references but no obj api for it...
        if 'service_template_back_refs' in kwargs:
            obj.service_template_back_refs = kwargs['service_template_back_refs']
        if 'loadbalancer_pool_back_refs' in kwargs:
            obj.loadbalancer_pool_back_refs = kwargs['loadbalancer_pool_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ServiceApplianceSet.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ServiceApplianceSet.service_appliance_set_properties.setter
    def service_appliance_set_properties(self, service_appliance_set_properties):
        """Set service-appliance-set-properties for service-appliance-set.
        
        :param service_appliance_set_properties: KeyValuePairs object
        
        """
        if 'service_appliance_set_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('service_appliance_set_properties')

        self._service_appliance_set_properties = service_appliance_set_properties
    #end service_appliance_set_properties

    def set_service_appliance_set_properties(self, value):
        self.service_appliance_set_properties = value
    #end set_service_appliance_set_properties

    @pycontrail.gen.resource_common.ServiceApplianceSet.service_appliance_driver.setter
    def service_appliance_driver(self, service_appliance_driver):
        """Set service-appliance-driver for service-appliance-set.
        
        :param service_appliance_driver: xsd:string object
        
        """
        if 'service_appliance_driver' not in self._pending_field_updates:
            self._pending_field_updates.add('service_appliance_driver')

        self._service_appliance_driver = service_appliance_driver
    #end service_appliance_driver

    def set_service_appliance_driver(self, value):
        self.service_appliance_driver = value
    #end set_service_appliance_driver

    @pycontrail.gen.resource_common.ServiceApplianceSet.service_appliance_ha_mode.setter
    def service_appliance_ha_mode(self, service_appliance_ha_mode):
        """Set service-appliance-ha-mode for service-appliance-set.
        
        :param service_appliance_ha_mode: xsd:string object
        
        """
        if 'service_appliance_ha_mode' not in self._pending_field_updates:
            self._pending_field_updates.add('service_appliance_ha_mode')

        self._service_appliance_ha_mode = service_appliance_ha_mode
    #end service_appliance_ha_mode

    def set_service_appliance_ha_mode(self, value):
        self.service_appliance_ha_mode = value
    #end set_service_appliance_ha_mode

    @pycontrail.gen.resource_common.ServiceApplianceSet.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-appliance-set.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ServiceApplianceSet.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-appliance-set.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ServiceApplianceSet.display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-appliance-set.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_service_appliances(self):
        children = super(ServiceApplianceSet, self).get_service_appliances()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.service_appliance_set_read(id = self.uuid, fields = ['service_appliances'])
            children = getattr(obj, 'service_appliances', None)
            self.service_appliances = children

        return children
    #end get_service_appliances


    def get_service_template_back_refs(self):
        """Return list of all service-templates using this service-appliance-set"""
        back_refs = super(ServiceApplianceSet, self).get_service_template_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_appliance_set_read(id = self.uuid, fields = ['service_template_back_refs'])
        back_refs = getattr(obj, 'service_template_back_refs', None)
        self.service_template_back_refs = back_refs

        return back_refs
    #end get_service_template_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this service-appliance-set"""
        back_refs = super(ServiceApplianceSet, self).get_loadbalancer_pool_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_appliance_set_read(id = self.uuid, fields = ['loadbalancer_pool_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_pool_back_refs', None)
        self.loadbalancer_pool_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_pool_back_refs

#end class ServiceApplianceSet

class ConfigNode(pycontrail.gen.resource_common.ConfigNode):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, config_node_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if config_node_ip_address is not None:
            pending_fields.append('config_node_ip_address')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ConfigNode, self).__init__(name, parent_obj, config_node_ip_address, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'config_node_ip_address' in kwargs:
            props_dict['config_node_ip_address'] = kwargs['config_node_ip_address']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ConfigNode(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ConfigNode.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ConfigNode.config_node_ip_address.setter
    def config_node_ip_address(self, config_node_ip_address):
        """Set config-node-ip-address for config-node.
        
        :param config_node_ip_address: IpAddressType object
        
        """
        if 'config_node_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('config_node_ip_address')

        self._config_node_ip_address = config_node_ip_address
    #end config_node_ip_address

    def set_config_node_ip_address(self, value):
        self.config_node_ip_address = value
    #end set_config_node_ip_address

    @pycontrail.gen.resource_common.ConfigNode.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for config-node.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ConfigNode.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for config-node.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ConfigNode.display_name.setter
    def display_name(self, display_name):
        """Set display-name for config-node.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class ConfigNode

class QosQueue(pycontrail.gen.resource_common.QosQueue):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, min_bandwidth=None, max_bandwidth=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if min_bandwidth is not None:
            pending_fields.append('min_bandwidth')
        if max_bandwidth is not None:
            pending_fields.append('max_bandwidth')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(QosQueue, self).__init__(name, parent_obj, min_bandwidth, max_bandwidth, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'min_bandwidth' in kwargs:
            props_dict['min_bandwidth'] = kwargs['min_bandwidth']
        if 'max_bandwidth' in kwargs:
            props_dict['max_bandwidth'] = kwargs['max_bandwidth']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = QosQueue(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...
        if 'qos_forwarding_class_back_refs' in kwargs:
            obj.qos_forwarding_class_back_refs = kwargs['qos_forwarding_class_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.QosQueue.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.QosQueue.min_bandwidth.setter
    def min_bandwidth(self, min_bandwidth):
        """Set min-bandwidth for qos-queue.
        
        :param min_bandwidth: xsd:integer object
        
        """
        if 'min_bandwidth' not in self._pending_field_updates:
            self._pending_field_updates.add('min_bandwidth')

        self._min_bandwidth = min_bandwidth
    #end min_bandwidth

    def set_min_bandwidth(self, value):
        self.min_bandwidth = value
    #end set_min_bandwidth

    @pycontrail.gen.resource_common.QosQueue.max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Set max-bandwidth for qos-queue.
        
        :param max_bandwidth: xsd:integer object
        
        """
        if 'max_bandwidth' not in self._pending_field_updates:
            self._pending_field_updates.add('max_bandwidth')

        self._max_bandwidth = max_bandwidth
    #end max_bandwidth

    def set_max_bandwidth(self, value):
        self.max_bandwidth = value
    #end set_max_bandwidth

    @pycontrail.gen.resource_common.QosQueue.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for qos-queue.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.QosQueue.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for qos-queue.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.QosQueue.display_name.setter
    def display_name(self, display_name):
        """Set display-name for qos-queue.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


    def get_qos_forwarding_class_back_refs(self):
        """Return list of all qos-forwarding-classs using this qos-queue"""
        back_refs = super(QosQueue, self).get_qos_forwarding_class_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.qos_queue_read(id = self.uuid, fields = ['qos_forwarding_class_back_refs'])
        back_refs = getattr(obj, 'qos_forwarding_class_back_refs', None)
        self.qos_forwarding_class_back_refs = back_refs

        return back_refs
    #end get_qos_forwarding_class_back_refs

#end class QosQueue

class VirtualMachine(pycontrail.gen.resource_common.VirtualMachine):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(VirtualMachine, self).__init__(name, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = VirtualMachine(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'virtual_machine_interfaces' in kwargs:
            obj.virtual_machine_interfaces = kwargs['virtual_machine_interfaces']

        # add any specified references...
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']
        if 'virtual_router_back_refs' in kwargs:
            obj.virtual_router_back_refs = kwargs['virtual_router_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.VirtualMachine.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.VirtualMachine.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-machine.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.VirtualMachine.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-machine.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.VirtualMachine.display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-machine.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for virtual-machine.
        
        :param ref_obj: ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(VirtualMachine, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to virtual-machine.
        
        :param ref_obj: ServiceInstance object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(VirtualMachine, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(VirtualMachine, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for virtual-machine.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(VirtualMachine, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list

    def get_virtual_machine_interfaces(self):
        children = super(VirtualMachine, self).get_virtual_machine_interfaces()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.virtual_machine_read(id = self.uuid, fields = ['virtual_machine_interfaces'])
            children = getattr(obj, 'virtual_machine_interfaces', None)
            self.virtual_machine_interfaces = children

        return children
    #end get_virtual_machine_interfaces


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this virtual-machine"""
        back_refs = super(VirtualMachine, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

    def get_virtual_router_back_refs(self):
        """Return list of all virtual-routers using this virtual-machine"""
        back_refs = super(VirtualMachine, self).get_virtual_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_read(id = self.uuid, fields = ['virtual_router_back_refs'])
        back_refs = getattr(obj, 'virtual_router_back_refs', None)
        self.virtual_router_back_refs = back_refs

        return back_refs
    #end get_virtual_router_back_refs

#end class VirtualMachine

class InterfaceRouteTable(pycontrail.gen.resource_common.InterfaceRouteTable):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, interface_route_table_routes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if interface_route_table_routes is not None:
            pending_fields.append('interface_route_table_routes')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(InterfaceRouteTable, self).__init__(name, parent_obj, interface_route_table_routes, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'interface_route_table_routes' in kwargs:
            if kwargs['interface_route_table_routes'] is None:
                props_dict['interface_route_table_routes'] = None
            else:
                props_dict['interface_route_table_routes'] = pycontrail.gen.resource_xsd.RouteTableType(**kwargs['interface_route_table_routes'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = InterfaceRouteTable(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']
            for ref in obj.service_instance_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.ServiceInterfaceTag(**ref['attr'])

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.InterfaceRouteTable.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.InterfaceRouteTable.interface_route_table_routes.setter
    def interface_route_table_routes(self, interface_route_table_routes):
        """Set interface-route-table-routes for interface-route-table.
        
        :param interface_route_table_routes: RouteTableType object
        
        """
        if 'interface_route_table_routes' not in self._pending_field_updates:
            self._pending_field_updates.add('interface_route_table_routes')

        self._interface_route_table_routes = interface_route_table_routes
    #end interface_route_table_routes

    def set_interface_route_table_routes(self, value):
        self.interface_route_table_routes = value
    #end set_interface_route_table_routes

    @pycontrail.gen.resource_common.InterfaceRouteTable.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for interface-route-table.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.InterfaceRouteTable.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for interface-route-table.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.InterfaceRouteTable.display_name.setter
    def display_name(self, display_name):
        """Set display-name for interface-route-table.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for interface-route-table.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(InterfaceRouteTable, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to interface-route-table.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(InterfaceRouteTable, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(InterfaceRouteTable, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for interface-route-table.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of ServiceInterfaceTag summary
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(InterfaceRouteTable, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this interface-route-table"""
        back_refs = super(InterfaceRouteTable, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.interface_route_table_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

#end class InterfaceRouteTable

class ServiceTemplate(pycontrail.gen.resource_common.ServiceTemplate):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, service_template_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if service_template_properties is not None:
            pending_fields.append('service_template_properties')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ServiceTemplate, self).__init__(name, parent_obj, service_template_properties, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'service_template_properties' in kwargs:
            if kwargs['service_template_properties'] is None:
                props_dict['service_template_properties'] = None
            else:
                props_dict['service_template_properties'] = pycontrail.gen.resource_xsd.ServiceTemplateType(**kwargs['service_template_properties'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ServiceTemplate(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'service_appliance_set_refs' in kwargs:
            obj.service_appliance_set_refs = kwargs['service_appliance_set_refs']

        # and back references but no obj api for it...
        if 'service_instance_back_refs' in kwargs:
            obj.service_instance_back_refs = kwargs['service_instance_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ServiceTemplate.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ServiceTemplate.service_template_properties.setter
    def service_template_properties(self, service_template_properties):
        """Set service-template-properties for service-template.
        
        :param service_template_properties: ServiceTemplateType object
        
        """
        if 'service_template_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('service_template_properties')

        self._service_template_properties = service_template_properties
    #end service_template_properties

    def set_service_template_properties(self, value):
        self.service_template_properties = value
    #end set_service_template_properties

    @pycontrail.gen.resource_common.ServiceTemplate.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-template.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ServiceTemplate.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-template.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ServiceTemplate.display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-template.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_appliance_set(self, *args, **kwargs):
        """Set service-appliance-set for service-template.
        
        :param ref_obj: ServiceApplianceSet object
        
        """
        self._pending_field_updates.add('service_appliance_set_refs')
        self._pending_ref_updates.discard('service_appliance_set_refs')
        super(ServiceTemplate, self).set_service_appliance_set(*args, **kwargs)

    #end set_service_appliance_set

    def add_service_appliance_set(self, *args, **kwargs):
        """Add service-appliance-set to service-template.
        
        :param ref_obj: ServiceApplianceSet object
        
        """
        if 'service_appliance_set_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_appliance_set_refs')
            self._original_service_appliance_set_refs = (self.get_service_appliance_set_refs() or [])[:]
        super(ServiceTemplate, self).add_service_appliance_set(*args, **kwargs)
    #end add_service_appliance_set

    def del_service_appliance_set(self, *args, **kwargs):
        if 'service_appliance_set_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_appliance_set_refs')
            self._original_service_appliance_set_refs = (self.get_service_appliance_set_refs() or [])[:]
        super(ServiceTemplate, self).del_service_appliance_set(*args, **kwargs)
    #end del_service_appliance_set

    def set_service_appliance_set_list(self, *args, **kwargs):
        """Set service-appliance-set list for service-template.
        
        :param ref_obj_list: list of ServiceApplianceSet object
        
        """
        self._pending_field_updates.add('service_appliance_set_refs')
        self._pending_ref_updates.discard('service_appliance_set_refs')
        super(ServiceTemplate, self).set_service_appliance_set_list(*args, **kwargs)
    #end set_service_appliance_set_list


    def get_service_instance_back_refs(self):
        """Return list of all service-instances using this service-template"""
        back_refs = super(ServiceTemplate, self).get_service_instance_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_template_read(id = self.uuid, fields = ['service_instance_back_refs'])
        back_refs = getattr(obj, 'service_instance_back_refs', None)
        self.service_instance_back_refs = back_refs

        return back_refs
    #end get_service_instance_back_refs

#end class ServiceTemplate

class DsaRule(pycontrail.gen.resource_common.DsaRule):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, dsa_rule_entry=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if dsa_rule_entry is not None:
            pending_fields.append('dsa_rule_entry')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(DsaRule, self).__init__(name, parent_obj, dsa_rule_entry, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'dsa_rule_entry' in kwargs:
            if kwargs['dsa_rule_entry'] is None:
                props_dict['dsa_rule_entry'] = None
            else:
                props_dict['dsa_rule_entry'] = pycontrail.gen.resource_xsd.DiscoveryServiceAssignmentType(**kwargs['dsa_rule_entry'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = DsaRule(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.DsaRule.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.DsaRule.dsa_rule_entry.setter
    def dsa_rule_entry(self, dsa_rule_entry):
        """Set dsa-rule-entry for dsa-rule.
        
        :param dsa_rule_entry: DiscoveryServiceAssignmentType object
        
        """
        if 'dsa_rule_entry' not in self._pending_field_updates:
            self._pending_field_updates.add('dsa_rule_entry')

        self._dsa_rule_entry = dsa_rule_entry
    #end dsa_rule_entry

    def set_dsa_rule_entry(self, value):
        self.dsa_rule_entry = value
    #end set_dsa_rule_entry

    @pycontrail.gen.resource_common.DsaRule.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for dsa-rule.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.DsaRule.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for dsa-rule.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.DsaRule.display_name.setter
    def display_name(self, display_name):
        """Set display-name for dsa-rule.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class DsaRule

class VirtualIp(pycontrail.gen.resource_common.VirtualIp):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, virtual_ip_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if virtual_ip_properties is not None:
            pending_fields.append('virtual_ip_properties')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(VirtualIp, self).__init__(name, parent_obj, virtual_ip_properties, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'virtual_ip_properties' in kwargs:
            if kwargs['virtual_ip_properties'] is None:
                props_dict['virtual_ip_properties'] = None
            else:
                props_dict['virtual_ip_properties'] = pycontrail.gen.resource_xsd.VirtualIpType(**kwargs['virtual_ip_properties'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = VirtualIp(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'loadbalancer_pool_refs' in kwargs:
            obj.loadbalancer_pool_refs = kwargs['loadbalancer_pool_refs']
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.VirtualIp.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.VirtualIp.virtual_ip_properties.setter
    def virtual_ip_properties(self, virtual_ip_properties):
        """Set virtual-ip-properties for virtual-ip.
        
        :param virtual_ip_properties: VirtualIpType object
        
        """
        if 'virtual_ip_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_ip_properties')

        self._virtual_ip_properties = virtual_ip_properties
    #end virtual_ip_properties

    def set_virtual_ip_properties(self, value):
        self.virtual_ip_properties = value
    #end set_virtual_ip_properties

    @pycontrail.gen.resource_common.VirtualIp.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-ip.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.VirtualIp.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-ip.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.VirtualIp.display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-ip.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_loadbalancer_pool(self, *args, **kwargs):
        """Set loadbalancer-pool for virtual-ip.
        
        :param ref_obj: LoadbalancerPool object
        
        """
        self._pending_field_updates.add('loadbalancer_pool_refs')
        self._pending_ref_updates.discard('loadbalancer_pool_refs')
        super(VirtualIp, self).set_loadbalancer_pool(*args, **kwargs)

    #end set_loadbalancer_pool

    def add_loadbalancer_pool(self, *args, **kwargs):
        """Add loadbalancer-pool to virtual-ip.
        
        :param ref_obj: LoadbalancerPool object
        
        """
        if 'loadbalancer_pool_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('loadbalancer_pool_refs')
            self._original_loadbalancer_pool_refs = (self.get_loadbalancer_pool_refs() or [])[:]
        super(VirtualIp, self).add_loadbalancer_pool(*args, **kwargs)
    #end add_loadbalancer_pool

    def del_loadbalancer_pool(self, *args, **kwargs):
        if 'loadbalancer_pool_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('loadbalancer_pool_refs')
            self._original_loadbalancer_pool_refs = (self.get_loadbalancer_pool_refs() or [])[:]
        super(VirtualIp, self).del_loadbalancer_pool(*args, **kwargs)
    #end del_loadbalancer_pool

    def set_loadbalancer_pool_list(self, *args, **kwargs):
        """Set loadbalancer-pool list for virtual-ip.
        
        :param ref_obj_list: list of LoadbalancerPool object
        
        """
        self._pending_field_updates.add('loadbalancer_pool_refs')
        self._pending_ref_updates.discard('loadbalancer_pool_refs')
        super(VirtualIp, self).set_loadbalancer_pool_list(*args, **kwargs)
    #end set_loadbalancer_pool_list

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for virtual-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(VirtualIp, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to virtual-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(VirtualIp, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(VirtualIp, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for virtual-ip.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(VirtualIp, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list


#end class VirtualIp

class LoadbalancerMember(pycontrail.gen.resource_common.LoadbalancerMember):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, loadbalancer_member_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if loadbalancer_member_properties is not None:
            pending_fields.append('loadbalancer_member_properties')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(LoadbalancerMember, self).__init__(name, parent_obj, loadbalancer_member_properties, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'loadbalancer_member_properties' in kwargs:
            if kwargs['loadbalancer_member_properties'] is None:
                props_dict['loadbalancer_member_properties'] = None
            else:
                props_dict['loadbalancer_member_properties'] = pycontrail.gen.resource_xsd.LoadbalancerMemberType(**kwargs['loadbalancer_member_properties'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = LoadbalancerMember(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.LoadbalancerMember.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.LoadbalancerMember.loadbalancer_member_properties.setter
    def loadbalancer_member_properties(self, loadbalancer_member_properties):
        """Set loadbalancer-member-properties for loadbalancer-member.
        
        :param loadbalancer_member_properties: LoadbalancerMemberType object
        
        """
        if 'loadbalancer_member_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_member_properties')

        self._loadbalancer_member_properties = loadbalancer_member_properties
    #end loadbalancer_member_properties

    def set_loadbalancer_member_properties(self, value):
        self.loadbalancer_member_properties = value
    #end set_loadbalancer_member_properties

    @pycontrail.gen.resource_common.LoadbalancerMember.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-member.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.LoadbalancerMember.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-member.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.LoadbalancerMember.display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-member.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class LoadbalancerMember

class SecurityGroup(pycontrail.gen.resource_common.SecurityGroup):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, security_group_id=None, configured_security_group_id=None, security_group_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if security_group_id is not None:
            pending_fields.append('security_group_id')
        if configured_security_group_id is not None:
            pending_fields.append('configured_security_group_id')
        if security_group_entries is not None:
            pending_fields.append('security_group_entries')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(SecurityGroup, self).__init__(name, parent_obj, security_group_id, configured_security_group_id, security_group_entries, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'security_group_id' in kwargs:
            props_dict['security_group_id'] = kwargs['security_group_id']
        if 'configured_security_group_id' in kwargs:
            props_dict['configured_security_group_id'] = kwargs['configured_security_group_id']
        if 'security_group_entries' in kwargs:
            if kwargs['security_group_entries'] is None:
                props_dict['security_group_entries'] = None
            else:
                props_dict['security_group_entries'] = pycontrail.gen.resource_xsd.PolicyEntriesType(**kwargs['security_group_entries'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = SecurityGroup(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'access_control_lists' in kwargs:
            obj.access_control_lists = kwargs['access_control_lists']

        # add any specified references...

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.SecurityGroup.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.SecurityGroup.security_group_id.setter
    def security_group_id(self, security_group_id):
        """Set security-group-id for security-group.
        
        :param security_group_id: xsd:string object
        
        """
        if 'security_group_id' not in self._pending_field_updates:
            self._pending_field_updates.add('security_group_id')

        self._security_group_id = security_group_id
    #end security_group_id

    def set_security_group_id(self, value):
        self.security_group_id = value
    #end set_security_group_id

    @pycontrail.gen.resource_common.SecurityGroup.configured_security_group_id.setter
    def configured_security_group_id(self, configured_security_group_id):
        """Set configured-security-group-id for security-group.
        
        :param configured_security_group_id: xsd:integer object
        
        """
        if 'configured_security_group_id' not in self._pending_field_updates:
            self._pending_field_updates.add('configured_security_group_id')

        self._configured_security_group_id = configured_security_group_id
    #end configured_security_group_id

    def set_configured_security_group_id(self, value):
        self.configured_security_group_id = value
    #end set_configured_security_group_id

    @pycontrail.gen.resource_common.SecurityGroup.security_group_entries.setter
    def security_group_entries(self, security_group_entries):
        """Set security-group-entries for security-group.
        
        :param security_group_entries: PolicyEntriesType object
        
        """
        if 'security_group_entries' not in self._pending_field_updates:
            self._pending_field_updates.add('security_group_entries')

        self._security_group_entries = security_group_entries
    #end security_group_entries

    def set_security_group_entries(self, value):
        self.security_group_entries = value
    #end set_security_group_entries

    @pycontrail.gen.resource_common.SecurityGroup.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for security-group.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.SecurityGroup.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for security-group.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.SecurityGroup.display_name.setter
    def display_name(self, display_name):
        """Set display-name for security-group.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_access_control_lists(self):
        children = super(SecurityGroup, self).get_access_control_lists()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.security_group_read(id = self.uuid, fields = ['access_control_lists'])
            children = getattr(obj, 'access_control_lists', None)
            self.access_control_lists = children

        return children
    #end get_access_control_lists


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this security-group"""
        back_refs = super(SecurityGroup, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.security_group_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

#end class SecurityGroup

class ServiceHealthCheck(pycontrail.gen.resource_common.ServiceHealthCheck):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, service_health_check_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if service_health_check_properties is not None:
            pending_fields.append('service_health_check_properties')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ServiceHealthCheck, self).__init__(name, parent_obj, service_health_check_properties, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'service_health_check_properties' in kwargs:
            if kwargs['service_health_check_properties'] is None:
                props_dict['service_health_check_properties'] = None
            else:
                props_dict['service_health_check_properties'] = pycontrail.gen.resource_xsd.ServiceHealthCheckType(**kwargs['service_health_check_properties'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ServiceHealthCheck(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']
            for ref in obj.service_instance_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.ServiceInterfaceTag(**ref['attr'])

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ServiceHealthCheck.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ServiceHealthCheck.service_health_check_properties.setter
    def service_health_check_properties(self, service_health_check_properties):
        """Set service-health-check-properties for service-health-check.
        
        :param service_health_check_properties: ServiceHealthCheckType object
        
        """
        if 'service_health_check_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('service_health_check_properties')

        self._service_health_check_properties = service_health_check_properties
    #end service_health_check_properties

    def set_service_health_check_properties(self, value):
        self.service_health_check_properties = value
    #end set_service_health_check_properties

    @pycontrail.gen.resource_common.ServiceHealthCheck.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-health-check.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ServiceHealthCheck.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-health-check.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ServiceHealthCheck.display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-health-check.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for service-health-check.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(ServiceHealthCheck, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to service-health-check.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(ServiceHealthCheck, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(ServiceHealthCheck, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for service-health-check.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of ServiceInterfaceTag summary
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(ServiceHealthCheck, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this service-health-check"""
        back_refs = super(ServiceHealthCheck, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.service_health_check_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

#end class ServiceHealthCheck

class ProviderAttachment(pycontrail.gen.resource_common.ProviderAttachment):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name']

        self._server_conn = None

        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(ProviderAttachment, self).__init__(name, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = ProviderAttachment(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_router_refs' in kwargs:
            obj.virtual_router_refs = kwargs['virtual_router_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.ProviderAttachment.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.ProviderAttachment.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for provider-attachment.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.ProviderAttachment.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for provider-attachment.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.ProviderAttachment.display_name.setter
    def display_name(self, display_name):
        """Set display-name for provider-attachment.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_router(self, *args, **kwargs):
        """Set virtual-router for provider-attachment.
        
        :param ref_obj: VirtualRouter object
        
        """
        self._pending_field_updates.add('virtual_router_refs')
        self._pending_ref_updates.discard('virtual_router_refs')
        super(ProviderAttachment, self).set_virtual_router(*args, **kwargs)

    #end set_virtual_router

    def add_virtual_router(self, *args, **kwargs):
        """Add virtual-router to provider-attachment.
        
        :param ref_obj: VirtualRouter object
        
        """
        if 'virtual_router_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_router_refs')
            self._original_virtual_router_refs = (self.get_virtual_router_refs() or [])[:]
        super(ProviderAttachment, self).add_virtual_router(*args, **kwargs)
    #end add_virtual_router

    def del_virtual_router(self, *args, **kwargs):
        if 'virtual_router_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_router_refs')
            self._original_virtual_router_refs = (self.get_virtual_router_refs() or [])[:]
        super(ProviderAttachment, self).del_virtual_router(*args, **kwargs)
    #end del_virtual_router

    def set_virtual_router_list(self, *args, **kwargs):
        """Set virtual-router list for provider-attachment.
        
        :param ref_obj_list: list of VirtualRouter object
        
        """
        self._pending_field_updates.add('virtual_router_refs')
        self._pending_ref_updates.discard('virtual_router_refs')
        super(ProviderAttachment, self).set_virtual_router_list(*args, **kwargs)
    #end set_virtual_router_list


#end class ProviderAttachment

class VirtualMachineInterface(pycontrail.gen.resource_common.VirtualMachineInterface):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, ecmp_hashing_include_fields=None, virtual_machine_interface_mac_addresses=None, virtual_machine_interface_dhcp_option_list=None, virtual_machine_interface_host_routes=None, virtual_machine_interface_allowed_address_pairs=None, vrf_assign_table=None, virtual_machine_interface_device_owner=None, virtual_machine_interface_disable_policy=False, virtual_machine_interface_properties=None, virtual_machine_interface_bindings=None, virtual_machine_interface_fat_flow_protocols=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if ecmp_hashing_include_fields is not None:
            pending_fields.append('ecmp_hashing_include_fields')
        if virtual_machine_interface_mac_addresses is not None:
            pending_fields.append('virtual_machine_interface_mac_addresses')
        if virtual_machine_interface_dhcp_option_list is not None:
            pending_fields.append('virtual_machine_interface_dhcp_option_list')
        if virtual_machine_interface_host_routes is not None:
            pending_fields.append('virtual_machine_interface_host_routes')
        if virtual_machine_interface_allowed_address_pairs is not None:
            pending_fields.append('virtual_machine_interface_allowed_address_pairs')
        if vrf_assign_table is not None:
            pending_fields.append('vrf_assign_table')
        if virtual_machine_interface_device_owner is not None:
            pending_fields.append('virtual_machine_interface_device_owner')
        if virtual_machine_interface_disable_policy is not None:
            pending_fields.append('virtual_machine_interface_disable_policy')
        if virtual_machine_interface_properties is not None:
            pending_fields.append('virtual_machine_interface_properties')
        if virtual_machine_interface_bindings is not None:
            pending_fields.append('virtual_machine_interface_bindings')
        if virtual_machine_interface_fat_flow_protocols is not None:
            pending_fields.append('virtual_machine_interface_fat_flow_protocols')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(VirtualMachineInterface, self).__init__(name, parent_obj, ecmp_hashing_include_fields, virtual_machine_interface_mac_addresses, virtual_machine_interface_dhcp_option_list, virtual_machine_interface_host_routes, virtual_machine_interface_allowed_address_pairs, vrf_assign_table, virtual_machine_interface_device_owner, virtual_machine_interface_disable_policy, virtual_machine_interface_properties, virtual_machine_interface_bindings, virtual_machine_interface_fat_flow_protocols, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'ecmp_hashing_include_fields' in kwargs:
            if kwargs['ecmp_hashing_include_fields'] is None:
                props_dict['ecmp_hashing_include_fields'] = None
            else:
                props_dict['ecmp_hashing_include_fields'] = pycontrail.gen.resource_xsd.EcmpHashingIncludeFields(**kwargs['ecmp_hashing_include_fields'])
        if 'virtual_machine_interface_mac_addresses' in kwargs:
            if kwargs['virtual_machine_interface_mac_addresses'] is None:
                props_dict['virtual_machine_interface_mac_addresses'] = None
            else:
                props_dict['virtual_machine_interface_mac_addresses'] = pycontrail.gen.resource_xsd.MacAddressesType(**kwargs['virtual_machine_interface_mac_addresses'])
        if 'virtual_machine_interface_dhcp_option_list' in kwargs:
            if kwargs['virtual_machine_interface_dhcp_option_list'] is None:
                props_dict['virtual_machine_interface_dhcp_option_list'] = None
            else:
                props_dict['virtual_machine_interface_dhcp_option_list'] = pycontrail.gen.resource_xsd.DhcpOptionsListType(**kwargs['virtual_machine_interface_dhcp_option_list'])
        if 'virtual_machine_interface_host_routes' in kwargs:
            if kwargs['virtual_machine_interface_host_routes'] is None:
                props_dict['virtual_machine_interface_host_routes'] = None
            else:
                props_dict['virtual_machine_interface_host_routes'] = pycontrail.gen.resource_xsd.RouteTableType(**kwargs['virtual_machine_interface_host_routes'])
        if 'virtual_machine_interface_allowed_address_pairs' in kwargs:
            if kwargs['virtual_machine_interface_allowed_address_pairs'] is None:
                props_dict['virtual_machine_interface_allowed_address_pairs'] = None
            else:
                props_dict['virtual_machine_interface_allowed_address_pairs'] = pycontrail.gen.resource_xsd.AllowedAddressPairs(**kwargs['virtual_machine_interface_allowed_address_pairs'])
        if 'vrf_assign_table' in kwargs:
            if kwargs['vrf_assign_table'] is None:
                props_dict['vrf_assign_table'] = None
            else:
                props_dict['vrf_assign_table'] = pycontrail.gen.resource_xsd.VrfAssignTableType(**kwargs['vrf_assign_table'])
        if 'virtual_machine_interface_device_owner' in kwargs:
            props_dict['virtual_machine_interface_device_owner'] = kwargs['virtual_machine_interface_device_owner']
        if 'virtual_machine_interface_disable_policy' in kwargs:
            props_dict['virtual_machine_interface_disable_policy'] = kwargs['virtual_machine_interface_disable_policy']
        if 'virtual_machine_interface_properties' in kwargs:
            if kwargs['virtual_machine_interface_properties'] is None:
                props_dict['virtual_machine_interface_properties'] = None
            else:
                props_dict['virtual_machine_interface_properties'] = pycontrail.gen.resource_xsd.VirtualMachineInterfacePropertiesType(**kwargs['virtual_machine_interface_properties'])
        if 'virtual_machine_interface_bindings' in kwargs:
            if kwargs['virtual_machine_interface_bindings'] is None:
                props_dict['virtual_machine_interface_bindings'] = None
            else:
                props_dict['virtual_machine_interface_bindings'] = pycontrail.gen.resource_xsd.KeyValuePairs(**kwargs['virtual_machine_interface_bindings'])
        if 'virtual_machine_interface_fat_flow_protocols' in kwargs:
            if kwargs['virtual_machine_interface_fat_flow_protocols'] is None:
                props_dict['virtual_machine_interface_fat_flow_protocols'] = None
            else:
                props_dict['virtual_machine_interface_fat_flow_protocols'] = pycontrail.gen.resource_xsd.FatFlowProtocols(**kwargs['virtual_machine_interface_fat_flow_protocols'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = VirtualMachineInterface(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'qos_forwarding_class_refs' in kwargs:
            obj.qos_forwarding_class_refs = kwargs['qos_forwarding_class_refs']
        if 'security_group_refs' in kwargs:
            obj.security_group_refs = kwargs['security_group_refs']
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']
        if 'virtual_machine_refs' in kwargs:
            obj.virtual_machine_refs = kwargs['virtual_machine_refs']
        if 'virtual_network_refs' in kwargs:
            obj.virtual_network_refs = kwargs['virtual_network_refs']
        if 'routing_instance_refs' in kwargs:
            obj.routing_instance_refs = kwargs['routing_instance_refs']
            for ref in obj.routing_instance_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.PolicyBasedForwardingRuleType(**ref['attr'])
        if 'port_tuple_refs' in kwargs:
            obj.port_tuple_refs = kwargs['port_tuple_refs']
        if 'service_health_check_refs' in kwargs:
            obj.service_health_check_refs = kwargs['service_health_check_refs']
        if 'interface_route_table_refs' in kwargs:
            obj.interface_route_table_refs = kwargs['interface_route_table_refs']
        if 'physical_interface_refs' in kwargs:
            obj.physical_interface_refs = kwargs['physical_interface_refs']

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']
        if 'instance_ip_back_refs' in kwargs:
            obj.instance_ip_back_refs = kwargs['instance_ip_back_refs']
        if 'subnet_back_refs' in kwargs:
            obj.subnet_back_refs = kwargs['subnet_back_refs']
        if 'floating_ip_back_refs' in kwargs:
            obj.floating_ip_back_refs = kwargs['floating_ip_back_refs']
        if 'logical_interface_back_refs' in kwargs:
            obj.logical_interface_back_refs = kwargs['logical_interface_back_refs']
        if 'bgp_as_a_service_back_refs' in kwargs:
            obj.bgp_as_a_service_back_refs = kwargs['bgp_as_a_service_back_refs']
        if 'customer_attachment_back_refs' in kwargs:
            obj.customer_attachment_back_refs = kwargs['customer_attachment_back_refs']
        if 'logical_router_back_refs' in kwargs:
            obj.logical_router_back_refs = kwargs['logical_router_back_refs']
        if 'loadbalancer_pool_back_refs' in kwargs:
            obj.loadbalancer_pool_back_refs = kwargs['loadbalancer_pool_back_refs']
        if 'virtual_ip_back_refs' in kwargs:
            obj.virtual_ip_back_refs = kwargs['virtual_ip_back_refs']
        if 'loadbalancer_back_refs' in kwargs:
            obj.loadbalancer_back_refs = kwargs['loadbalancer_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.VirtualMachineInterface.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.VirtualMachineInterface.ecmp_hashing_include_fields.setter
    def ecmp_hashing_include_fields(self, ecmp_hashing_include_fields):
        """Set ecmp-hashing-include-fields for virtual-machine-interface.
        
        :param ecmp_hashing_include_fields: EcmpHashingIncludeFields object
        
        """
        if 'ecmp_hashing_include_fields' not in self._pending_field_updates:
            self._pending_field_updates.add('ecmp_hashing_include_fields')

        self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
    #end ecmp_hashing_include_fields

    def set_ecmp_hashing_include_fields(self, value):
        self.ecmp_hashing_include_fields = value
    #end set_ecmp_hashing_include_fields

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_mac_addresses.setter
    def virtual_machine_interface_mac_addresses(self, virtual_machine_interface_mac_addresses):
        """Set virtual-machine-interface-mac-addresses for virtual-machine-interface.
        
        :param virtual_machine_interface_mac_addresses: MacAddressesType object
        
        """
        if 'virtual_machine_interface_mac_addresses' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_mac_addresses')

        self._virtual_machine_interface_mac_addresses = virtual_machine_interface_mac_addresses
    #end virtual_machine_interface_mac_addresses

    def set_virtual_machine_interface_mac_addresses(self, value):
        self.virtual_machine_interface_mac_addresses = value
    #end set_virtual_machine_interface_mac_addresses

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_dhcp_option_list.setter
    def virtual_machine_interface_dhcp_option_list(self, virtual_machine_interface_dhcp_option_list):
        """Set virtual-machine-interface-dhcp-option-list for virtual-machine-interface.
        
        :param virtual_machine_interface_dhcp_option_list: DhcpOptionsListType object
        
        """
        if 'virtual_machine_interface_dhcp_option_list' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_dhcp_option_list')

        self._virtual_machine_interface_dhcp_option_list = virtual_machine_interface_dhcp_option_list
    #end virtual_machine_interface_dhcp_option_list

    def set_virtual_machine_interface_dhcp_option_list(self, value):
        self.virtual_machine_interface_dhcp_option_list = value
    #end set_virtual_machine_interface_dhcp_option_list

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_host_routes.setter
    def virtual_machine_interface_host_routes(self, virtual_machine_interface_host_routes):
        """Set virtual-machine-interface-host-routes for virtual-machine-interface.
        
        :param virtual_machine_interface_host_routes: RouteTableType object
        
        """
        if 'virtual_machine_interface_host_routes' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_host_routes')

        self._virtual_machine_interface_host_routes = virtual_machine_interface_host_routes
    #end virtual_machine_interface_host_routes

    def set_virtual_machine_interface_host_routes(self, value):
        self.virtual_machine_interface_host_routes = value
    #end set_virtual_machine_interface_host_routes

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_allowed_address_pairs.setter
    def virtual_machine_interface_allowed_address_pairs(self, virtual_machine_interface_allowed_address_pairs):
        """Set virtual-machine-interface-allowed-address-pairs for virtual-machine-interface.
        
        :param virtual_machine_interface_allowed_address_pairs: AllowedAddressPairs object
        
        """
        if 'virtual_machine_interface_allowed_address_pairs' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_allowed_address_pairs')

        self._virtual_machine_interface_allowed_address_pairs = virtual_machine_interface_allowed_address_pairs
    #end virtual_machine_interface_allowed_address_pairs

    def set_virtual_machine_interface_allowed_address_pairs(self, value):
        self.virtual_machine_interface_allowed_address_pairs = value
    #end set_virtual_machine_interface_allowed_address_pairs

    @pycontrail.gen.resource_common.VirtualMachineInterface.vrf_assign_table.setter
    def vrf_assign_table(self, vrf_assign_table):
        """Set vrf-assign-table for virtual-machine-interface.
        
        :param vrf_assign_table: VrfAssignTableType object
        
        """
        if 'vrf_assign_table' not in self._pending_field_updates:
            self._pending_field_updates.add('vrf_assign_table')

        self._vrf_assign_table = vrf_assign_table
    #end vrf_assign_table

    def set_vrf_assign_table(self, value):
        self.vrf_assign_table = value
    #end set_vrf_assign_table

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_device_owner.setter
    def virtual_machine_interface_device_owner(self, virtual_machine_interface_device_owner):
        """Set virtual-machine-interface-device-owner for virtual-machine-interface.
        
        :param virtual_machine_interface_device_owner: xsd:string object
        
        """
        if 'virtual_machine_interface_device_owner' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_device_owner')

        self._virtual_machine_interface_device_owner = virtual_machine_interface_device_owner
    #end virtual_machine_interface_device_owner

    def set_virtual_machine_interface_device_owner(self, value):
        self.virtual_machine_interface_device_owner = value
    #end set_virtual_machine_interface_device_owner

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_disable_policy.setter
    def virtual_machine_interface_disable_policy(self, virtual_machine_interface_disable_policy):
        """Set virtual-machine-interface-disable-policy for virtual-machine-interface.
        
        :param virtual_machine_interface_disable_policy: xsd:boolean object
        
        """
        if 'virtual_machine_interface_disable_policy' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_disable_policy')

        self._virtual_machine_interface_disable_policy = virtual_machine_interface_disable_policy
    #end virtual_machine_interface_disable_policy

    def set_virtual_machine_interface_disable_policy(self, value):
        self.virtual_machine_interface_disable_policy = value
    #end set_virtual_machine_interface_disable_policy

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_properties.setter
    def virtual_machine_interface_properties(self, virtual_machine_interface_properties):
        """Set virtual-machine-interface-properties for virtual-machine-interface.
        
        :param virtual_machine_interface_properties: VirtualMachineInterfacePropertiesType object
        
        """
        if 'virtual_machine_interface_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_properties')

        self._virtual_machine_interface_properties = virtual_machine_interface_properties
    #end virtual_machine_interface_properties

    def set_virtual_machine_interface_properties(self, value):
        self.virtual_machine_interface_properties = value
    #end set_virtual_machine_interface_properties

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_bindings.setter
    def virtual_machine_interface_bindings(self, virtual_machine_interface_bindings):
        """Set virtual-machine-interface-bindings for virtual-machine-interface.
        
        :param virtual_machine_interface_bindings: KeyValuePairs object
        
        """
        if 'virtual_machine_interface_bindings' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_bindings')

        if 'virtual_machine_interface_bindings' in self._pending_field_map_updates:
            # set clobbers earlier add/del on prop map elements
            del self._pending_field_map_updates['virtual_machine_interface_bindings']

        self._virtual_machine_interface_bindings = virtual_machine_interface_bindings
    #end virtual_machine_interface_bindings

    def set_virtual_machine_interface_bindings(self, value):
        self.virtual_machine_interface_bindings = value
    #end set_virtual_machine_interface_bindings

    @pycontrail.gen.resource_common.VirtualMachineInterface.virtual_machine_interface_fat_flow_protocols.setter
    def virtual_machine_interface_fat_flow_protocols(self, virtual_machine_interface_fat_flow_protocols):
        """Set virtual-machine-interface-fat-flow-protocols for virtual-machine-interface.
        
        :param virtual_machine_interface_fat_flow_protocols: FatFlowProtocols object
        
        """
        if 'virtual_machine_interface_fat_flow_protocols' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_machine_interface_fat_flow_protocols')

        if 'virtual_machine_interface_fat_flow_protocols' in self._pending_field_list_updates:
            # set clobbers earlier add/del on prop list elements
            del self._pending_field_list_updates['virtual_machine_interface_fat_flow_protocols']

        self._virtual_machine_interface_fat_flow_protocols = virtual_machine_interface_fat_flow_protocols
    #end virtual_machine_interface_fat_flow_protocols

    def set_virtual_machine_interface_fat_flow_protocols(self, value):
        self.virtual_machine_interface_fat_flow_protocols = value
    #end set_virtual_machine_interface_fat_flow_protocols

    @pycontrail.gen.resource_common.VirtualMachineInterface.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-machine-interface.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.VirtualMachineInterface.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-machine-interface.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.VirtualMachineInterface.display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-machine-interface.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def add_virtual_machine_interface_fat_flow_protocols(self, elem_value, elem_position=None):
        """Add element to virtual-machine-interface-fat-flow-protocols for virtual-machine-interface.
        
        :param elem_value: xsd:string object
        :param elem_position: optional string order-key
        
        """
        if 'virtual_machine_interface_fat_flow_protocols' not in self._pending_field_list_updates:
            self._pending_field_list_updates['virtual_machine_interface_fat_flow_protocols'] = [
                ('add', elem_value, elem_position)]
        else:
            self._pending_field_list_updates['virtual_machine_interface_fat_flow_protocols'].append(
                ('add', elem_value, elem_position))
    #end add_virtual_machine_interface_fat_flow_protocols

    def del_virtual_machine_interface_fat_flow_protocols(self, elem_position):
        """Delete element from virtual-machine-interface-fat-flow-protocols for virtual-machine-interface.
        
        :param elem_position: string indicating order-key
        
        """
        if 'virtual_machine_interface_fat_flow_protocols' not in self._pending_field_list_updates:
            self._pending_field_list_updates['virtual_machine_interface_fat_flow_protocols'] = [
                ('delete', None, elem_position)]
        else:
            self._pending_field_list_updates['virtual_machine_interface_fat_flow_protocols'].append(
                ('delete', None, elem_position))
    #end del_virtual_machine_interface_fat_flow_protocols
    def add_virtual_machine_interface_bindings(self, elem):
        """Add element to virtual-machine-interface-bindings for virtual-machine-interface.
        
        :param elem: xsd:string object
        
        """
        elem_position = getattr(elem, 'key')
        if 'virtual_machine_interface_bindings' not in self._pending_field_map_updates:
            self._pending_field_map_updates['virtual_machine_interface_bindings'] = [
                ('set', elem, elem_position)]
        else:
            self._pending_field_map_updates['virtual_machine_interface_bindings'].append(
                ('set', elem, elem_position))
    #end set_virtual_machine_interface_bindings

    def del_virtual_machine_interface_bindings(self, elem_position):
        """Delete element from virtual-machine-interface-bindings for virtual-machine-interface.
        
        :param elem_position: string indicating map-key
        
        """
        if 'virtual_machine_interface_bindings' not in self._pending_field_map_updates:
            self._pending_field_map_updates['virtual_machine_interface_bindings'] = [
                ('delete', None, elem_position)]
        else:
            self._pending_field_map_updates['virtual_machine_interface_bindings'].append(
                ('delete', None, elem_position))
    #end del_virtual_machine_interface_bindings
    def set_qos_forwarding_class(self, *args, **kwargs):
        """Set qos-forwarding-class for virtual-machine-interface.
        
        :param ref_obj: QosForwardingClass object
        
        """
        self._pending_field_updates.add('qos_forwarding_class_refs')
        self._pending_ref_updates.discard('qos_forwarding_class_refs')
        super(VirtualMachineInterface, self).set_qos_forwarding_class(*args, **kwargs)

    #end set_qos_forwarding_class

    def add_qos_forwarding_class(self, *args, **kwargs):
        """Add qos-forwarding-class to virtual-machine-interface.
        
        :param ref_obj: QosForwardingClass object
        
        """
        if 'qos_forwarding_class_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('qos_forwarding_class_refs')
            self._original_qos_forwarding_class_refs = (self.get_qos_forwarding_class_refs() or [])[:]
        super(VirtualMachineInterface, self).add_qos_forwarding_class(*args, **kwargs)
    #end add_qos_forwarding_class

    def del_qos_forwarding_class(self, *args, **kwargs):
        if 'qos_forwarding_class_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('qos_forwarding_class_refs')
            self._original_qos_forwarding_class_refs = (self.get_qos_forwarding_class_refs() or [])[:]
        super(VirtualMachineInterface, self).del_qos_forwarding_class(*args, **kwargs)
    #end del_qos_forwarding_class

    def set_qos_forwarding_class_list(self, *args, **kwargs):
        """Set qos-forwarding-class list for virtual-machine-interface.
        
        :param ref_obj_list: list of QosForwardingClass object
        
        """
        self._pending_field_updates.add('qos_forwarding_class_refs')
        self._pending_ref_updates.discard('qos_forwarding_class_refs')
        super(VirtualMachineInterface, self).set_qos_forwarding_class_list(*args, **kwargs)
    #end set_qos_forwarding_class_list

    def set_security_group(self, *args, **kwargs):
        """Set security-group for virtual-machine-interface.
        
        :param ref_obj: SecurityGroup object
        
        """
        self._pending_field_updates.add('security_group_refs')
        self._pending_ref_updates.discard('security_group_refs')
        super(VirtualMachineInterface, self).set_security_group(*args, **kwargs)

    #end set_security_group

    def add_security_group(self, *args, **kwargs):
        """Add security-group to virtual-machine-interface.
        
        :param ref_obj: SecurityGroup object
        
        """
        if 'security_group_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('security_group_refs')
            self._original_security_group_refs = (self.get_security_group_refs() or [])[:]
        super(VirtualMachineInterface, self).add_security_group(*args, **kwargs)
    #end add_security_group

    def del_security_group(self, *args, **kwargs):
        if 'security_group_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('security_group_refs')
            self._original_security_group_refs = (self.get_security_group_refs() or [])[:]
        super(VirtualMachineInterface, self).del_security_group(*args, **kwargs)
    #end del_security_group

    def set_security_group_list(self, *args, **kwargs):
        """Set security-group list for virtual-machine-interface.
        
        :param ref_obj_list: list of SecurityGroup object
        
        """
        self._pending_field_updates.add('security_group_refs')
        self._pending_ref_updates.discard('security_group_refs')
        super(VirtualMachineInterface, self).set_security_group_list(*args, **kwargs)
    #end set_security_group_list

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for virtual-machine-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(VirtualMachineInterface, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to virtual-machine-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(VirtualMachineInterface, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(VirtualMachineInterface, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for virtual-machine-interface.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(VirtualMachineInterface, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list

    def set_virtual_machine(self, *args, **kwargs):
        """Set virtual-machine for virtual-machine-interface.
        
        :param ref_obj: VirtualMachine object
        
        """
        self._pending_field_updates.add('virtual_machine_refs')
        self._pending_ref_updates.discard('virtual_machine_refs')
        super(VirtualMachineInterface, self).set_virtual_machine(*args, **kwargs)

    #end set_virtual_machine

    def add_virtual_machine(self, *args, **kwargs):
        """Add virtual-machine to virtual-machine-interface.
        
        :param ref_obj: VirtualMachine object
        
        """
        if 'virtual_machine_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_refs')
            self._original_virtual_machine_refs = (self.get_virtual_machine_refs() or [])[:]
        super(VirtualMachineInterface, self).add_virtual_machine(*args, **kwargs)
    #end add_virtual_machine

    def del_virtual_machine(self, *args, **kwargs):
        if 'virtual_machine_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_refs')
            self._original_virtual_machine_refs = (self.get_virtual_machine_refs() or [])[:]
        super(VirtualMachineInterface, self).del_virtual_machine(*args, **kwargs)
    #end del_virtual_machine

    def set_virtual_machine_list(self, *args, **kwargs):
        """Set virtual-machine list for virtual-machine-interface.
        
        :param ref_obj_list: list of VirtualMachine object
        
        """
        self._pending_field_updates.add('virtual_machine_refs')
        self._pending_ref_updates.discard('virtual_machine_refs')
        super(VirtualMachineInterface, self).set_virtual_machine_list(*args, **kwargs)
    #end set_virtual_machine_list

    def set_virtual_network(self, *args, **kwargs):
        """Set virtual-network for virtual-machine-interface.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(VirtualMachineInterface, self).set_virtual_network(*args, **kwargs)

    #end set_virtual_network

    def add_virtual_network(self, *args, **kwargs):
        """Add virtual-network to virtual-machine-interface.
        
        :param ref_obj: VirtualNetwork object
        
        """
        if 'virtual_network_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(VirtualMachineInterface, self).add_virtual_network(*args, **kwargs)
    #end add_virtual_network

    def del_virtual_network(self, *args, **kwargs):
        if 'virtual_network_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(VirtualMachineInterface, self).del_virtual_network(*args, **kwargs)
    #end del_virtual_network

    def set_virtual_network_list(self, *args, **kwargs):
        """Set virtual-network list for virtual-machine-interface.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(VirtualMachineInterface, self).set_virtual_network_list(*args, **kwargs)
    #end set_virtual_network_list

    def set_routing_instance(self, *args, **kwargs):
        """Set routing-instance for virtual-machine-interface.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: PolicyBasedForwardingRuleType object
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(VirtualMachineInterface, self).set_routing_instance(*args, **kwargs)

    #end set_routing_instance

    def add_routing_instance(self, *args, **kwargs):
        """Add routing-instance to virtual-machine-interface.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: PolicyBasedForwardingRuleType object
        
        """
        if 'routing_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(VirtualMachineInterface, self).add_routing_instance(*args, **kwargs)
    #end add_routing_instance

    def del_routing_instance(self, *args, **kwargs):
        if 'routing_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(VirtualMachineInterface, self).del_routing_instance(*args, **kwargs)
    #end del_routing_instance

    def set_routing_instance_list(self, *args, **kwargs):
        """Set routing-instance list for virtual-machine-interface.
        
        :param ref_obj_list: list of RoutingInstance object
        :param ref_data_list: list of PolicyBasedForwardingRuleType summary
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(VirtualMachineInterface, self).set_routing_instance_list(*args, **kwargs)
    #end set_routing_instance_list

    def set_port_tuple(self, *args, **kwargs):
        """Set port-tuple for virtual-machine-interface.
        
        :param ref_obj: PortTuple object
        
        """
        self._pending_field_updates.add('port_tuple_refs')
        self._pending_ref_updates.discard('port_tuple_refs')
        super(VirtualMachineInterface, self).set_port_tuple(*args, **kwargs)

    #end set_port_tuple

    def add_port_tuple(self, *args, **kwargs):
        """Add port-tuple to virtual-machine-interface.
        
        :param ref_obj: PortTuple object
        
        """
        if 'port_tuple_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('port_tuple_refs')
            self._original_port_tuple_refs = (self.get_port_tuple_refs() or [])[:]
        super(VirtualMachineInterface, self).add_port_tuple(*args, **kwargs)
    #end add_port_tuple

    def del_port_tuple(self, *args, **kwargs):
        if 'port_tuple_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('port_tuple_refs')
            self._original_port_tuple_refs = (self.get_port_tuple_refs() or [])[:]
        super(VirtualMachineInterface, self).del_port_tuple(*args, **kwargs)
    #end del_port_tuple

    def set_port_tuple_list(self, *args, **kwargs):
        """Set port-tuple list for virtual-machine-interface.
        
        :param ref_obj_list: list of PortTuple object
        
        """
        self._pending_field_updates.add('port_tuple_refs')
        self._pending_ref_updates.discard('port_tuple_refs')
        super(VirtualMachineInterface, self).set_port_tuple_list(*args, **kwargs)
    #end set_port_tuple_list

    def set_service_health_check(self, *args, **kwargs):
        """Set service-health-check for virtual-machine-interface.
        
        :param ref_obj: ServiceHealthCheck object
        
        """
        self._pending_field_updates.add('service_health_check_refs')
        self._pending_ref_updates.discard('service_health_check_refs')
        super(VirtualMachineInterface, self).set_service_health_check(*args, **kwargs)

    #end set_service_health_check

    def add_service_health_check(self, *args, **kwargs):
        """Add service-health-check to virtual-machine-interface.
        
        :param ref_obj: ServiceHealthCheck object
        
        """
        if 'service_health_check_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_health_check_refs')
            self._original_service_health_check_refs = (self.get_service_health_check_refs() or [])[:]
        super(VirtualMachineInterface, self).add_service_health_check(*args, **kwargs)
    #end add_service_health_check

    def del_service_health_check(self, *args, **kwargs):
        if 'service_health_check_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_health_check_refs')
            self._original_service_health_check_refs = (self.get_service_health_check_refs() or [])[:]
        super(VirtualMachineInterface, self).del_service_health_check(*args, **kwargs)
    #end del_service_health_check

    def set_service_health_check_list(self, *args, **kwargs):
        """Set service-health-check list for virtual-machine-interface.
        
        :param ref_obj_list: list of ServiceHealthCheck object
        
        """
        self._pending_field_updates.add('service_health_check_refs')
        self._pending_ref_updates.discard('service_health_check_refs')
        super(VirtualMachineInterface, self).set_service_health_check_list(*args, **kwargs)
    #end set_service_health_check_list

    def set_interface_route_table(self, *args, **kwargs):
        """Set interface-route-table for virtual-machine-interface.
        
        :param ref_obj: InterfaceRouteTable object
        
        """
        self._pending_field_updates.add('interface_route_table_refs')
        self._pending_ref_updates.discard('interface_route_table_refs')
        super(VirtualMachineInterface, self).set_interface_route_table(*args, **kwargs)

    #end set_interface_route_table

    def add_interface_route_table(self, *args, **kwargs):
        """Add interface-route-table to virtual-machine-interface.
        
        :param ref_obj: InterfaceRouteTable object
        
        """
        if 'interface_route_table_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('interface_route_table_refs')
            self._original_interface_route_table_refs = (self.get_interface_route_table_refs() or [])[:]
        super(VirtualMachineInterface, self).add_interface_route_table(*args, **kwargs)
    #end add_interface_route_table

    def del_interface_route_table(self, *args, **kwargs):
        if 'interface_route_table_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('interface_route_table_refs')
            self._original_interface_route_table_refs = (self.get_interface_route_table_refs() or [])[:]
        super(VirtualMachineInterface, self).del_interface_route_table(*args, **kwargs)
    #end del_interface_route_table

    def set_interface_route_table_list(self, *args, **kwargs):
        """Set interface-route-table list for virtual-machine-interface.
        
        :param ref_obj_list: list of InterfaceRouteTable object
        
        """
        self._pending_field_updates.add('interface_route_table_refs')
        self._pending_ref_updates.discard('interface_route_table_refs')
        super(VirtualMachineInterface, self).set_interface_route_table_list(*args, **kwargs)
    #end set_interface_route_table_list

    def set_physical_interface(self, *args, **kwargs):
        """Set physical-interface for virtual-machine-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        self._pending_field_updates.add('physical_interface_refs')
        self._pending_ref_updates.discard('physical_interface_refs')
        super(VirtualMachineInterface, self).set_physical_interface(*args, **kwargs)

    #end set_physical_interface

    def add_physical_interface(self, *args, **kwargs):
        """Add physical-interface to virtual-machine-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        if 'physical_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('physical_interface_refs')
            self._original_physical_interface_refs = (self.get_physical_interface_refs() or [])[:]
        super(VirtualMachineInterface, self).add_physical_interface(*args, **kwargs)
    #end add_physical_interface

    def del_physical_interface(self, *args, **kwargs):
        if 'physical_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('physical_interface_refs')
            self._original_physical_interface_refs = (self.get_physical_interface_refs() or [])[:]
        super(VirtualMachineInterface, self).del_physical_interface(*args, **kwargs)
    #end del_physical_interface

    def set_physical_interface_list(self, *args, **kwargs):
        """Set physical-interface list for virtual-machine-interface.
        
        :param ref_obj_list: list of PhysicalInterface object
        
        """
        self._pending_field_updates.add('physical_interface_refs')
        self._pending_ref_updates.discard('physical_interface_refs')
        super(VirtualMachineInterface, self).set_physical_interface_list(*args, **kwargs)
    #end set_physical_interface_list


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

    def get_instance_ip_back_refs(self):
        """Return list of all instance-ips using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_instance_ip_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['instance_ip_back_refs'])
        back_refs = getattr(obj, 'instance_ip_back_refs', None)
        self.instance_ip_back_refs = back_refs

        return back_refs
    #end get_instance_ip_back_refs

    def get_subnet_back_refs(self):
        """Return list of all subnets using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_subnet_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['subnet_back_refs'])
        back_refs = getattr(obj, 'subnet_back_refs', None)
        self.subnet_back_refs = back_refs

        return back_refs
    #end get_subnet_back_refs

    def get_floating_ip_back_refs(self):
        """Return list of all floating-ips using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_floating_ip_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['floating_ip_back_refs'])
        back_refs = getattr(obj, 'floating_ip_back_refs', None)
        self.floating_ip_back_refs = back_refs

        return back_refs
    #end get_floating_ip_back_refs

    def get_logical_interface_back_refs(self):
        """Return list of all logical-interfaces using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_logical_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['logical_interface_back_refs'])
        back_refs = getattr(obj, 'logical_interface_back_refs', None)
        self.logical_interface_back_refs = back_refs

        return back_refs
    #end get_logical_interface_back_refs

    def get_bgp_as_a_service_back_refs(self):
        """Return list of all bgp-as-a-services using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_bgp_as_a_service_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['bgp_as_a_service_back_refs'])
        back_refs = getattr(obj, 'bgp_as_a_service_back_refs', None)
        self.bgp_as_a_service_back_refs = back_refs

        return back_refs
    #end get_bgp_as_a_service_back_refs

    def get_customer_attachment_back_refs(self):
        """Return list of all customer-attachments using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_customer_attachment_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['customer_attachment_back_refs'])
        back_refs = getattr(obj, 'customer_attachment_back_refs', None)
        self.customer_attachment_back_refs = back_refs

        return back_refs
    #end get_customer_attachment_back_refs

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_logical_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['logical_router_back_refs'])
        back_refs = getattr(obj, 'logical_router_back_refs', None)
        self.logical_router_back_refs = back_refs

        return back_refs
    #end get_logical_router_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_loadbalancer_pool_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['loadbalancer_pool_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_pool_back_refs', None)
        self.loadbalancer_pool_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_pool_back_refs

    def get_virtual_ip_back_refs(self):
        """Return list of all virtual-ips using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_virtual_ip_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['virtual_ip_back_refs'])
        back_refs = getattr(obj, 'virtual_ip_back_refs', None)
        self.virtual_ip_back_refs = back_refs

        return back_refs
    #end get_virtual_ip_back_refs

    def get_loadbalancer_back_refs(self):
        """Return list of all loadbalancers using this virtual-machine-interface"""
        back_refs = super(VirtualMachineInterface, self).get_loadbalancer_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_machine_interface_read(id = self.uuid, fields = ['loadbalancer_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_back_refs', None)
        self.loadbalancer_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_back_refs

#end class VirtualMachineInterface

class LoadbalancerHealthmonitor(pycontrail.gen.resource_common.LoadbalancerHealthmonitor):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, loadbalancer_healthmonitor_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if loadbalancer_healthmonitor_properties is not None:
            pending_fields.append('loadbalancer_healthmonitor_properties')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(LoadbalancerHealthmonitor, self).__init__(name, parent_obj, loadbalancer_healthmonitor_properties, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'loadbalancer_healthmonitor_properties' in kwargs:
            if kwargs['loadbalancer_healthmonitor_properties'] is None:
                props_dict['loadbalancer_healthmonitor_properties'] = None
            else:
                props_dict['loadbalancer_healthmonitor_properties'] = pycontrail.gen.resource_xsd.LoadbalancerHealthmonitorType(**kwargs['loadbalancer_healthmonitor_properties'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = LoadbalancerHealthmonitor(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...
        if 'loadbalancer_pool_back_refs' in kwargs:
            obj.loadbalancer_pool_back_refs = kwargs['loadbalancer_pool_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.LoadbalancerHealthmonitor.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.LoadbalancerHealthmonitor.loadbalancer_healthmonitor_properties.setter
    def loadbalancer_healthmonitor_properties(self, loadbalancer_healthmonitor_properties):
        """Set loadbalancer-healthmonitor-properties for loadbalancer-healthmonitor.
        
        :param loadbalancer_healthmonitor_properties: LoadbalancerHealthmonitorType object
        
        """
        if 'loadbalancer_healthmonitor_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_healthmonitor_properties')

        self._loadbalancer_healthmonitor_properties = loadbalancer_healthmonitor_properties
    #end loadbalancer_healthmonitor_properties

    def set_loadbalancer_healthmonitor_properties(self, value):
        self.loadbalancer_healthmonitor_properties = value
    #end set_loadbalancer_healthmonitor_properties

    @pycontrail.gen.resource_common.LoadbalancerHealthmonitor.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-healthmonitor.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.LoadbalancerHealthmonitor.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-healthmonitor.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.LoadbalancerHealthmonitor.display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-healthmonitor.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this loadbalancer-healthmonitor"""
        back_refs = super(LoadbalancerHealthmonitor, self).get_loadbalancer_pool_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.loadbalancer_healthmonitor_read(id = self.uuid, fields = ['loadbalancer_pool_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_pool_back_refs', None)
        self.loadbalancer_pool_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_pool_back_refs

#end class LoadbalancerHealthmonitor

class LoadbalancerListener(pycontrail.gen.resource_common.LoadbalancerListener):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, loadbalancer_listener_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if loadbalancer_listener_properties is not None:
            pending_fields.append('loadbalancer_listener_properties')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(LoadbalancerListener, self).__init__(name, parent_obj, loadbalancer_listener_properties, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'loadbalancer_listener_properties' in kwargs:
            if kwargs['loadbalancer_listener_properties'] is None:
                props_dict['loadbalancer_listener_properties'] = None
            else:
                props_dict['loadbalancer_listener_properties'] = pycontrail.gen.resource_xsd.LoadbalancerListenerType(**kwargs['loadbalancer_listener_properties'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = LoadbalancerListener(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'loadbalancer_refs' in kwargs:
            obj.loadbalancer_refs = kwargs['loadbalancer_refs']

        # and back references but no obj api for it...
        if 'loadbalancer_pool_back_refs' in kwargs:
            obj.loadbalancer_pool_back_refs = kwargs['loadbalancer_pool_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.LoadbalancerListener.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.LoadbalancerListener.loadbalancer_listener_properties.setter
    def loadbalancer_listener_properties(self, loadbalancer_listener_properties):
        """Set loadbalancer-listener-properties for loadbalancer-listener.
        
        :param loadbalancer_listener_properties: LoadbalancerListenerType object
        
        """
        if 'loadbalancer_listener_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_listener_properties')

        self._loadbalancer_listener_properties = loadbalancer_listener_properties
    #end loadbalancer_listener_properties

    def set_loadbalancer_listener_properties(self, value):
        self.loadbalancer_listener_properties = value
    #end set_loadbalancer_listener_properties

    @pycontrail.gen.resource_common.LoadbalancerListener.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-listener.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.LoadbalancerListener.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-listener.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.LoadbalancerListener.display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-listener.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_loadbalancer(self, *args, **kwargs):
        """Set loadbalancer for loadbalancer-listener.
        
        :param ref_obj: Loadbalancer object
        
        """
        self._pending_field_updates.add('loadbalancer_refs')
        self._pending_ref_updates.discard('loadbalancer_refs')
        super(LoadbalancerListener, self).set_loadbalancer(*args, **kwargs)

    #end set_loadbalancer

    def add_loadbalancer(self, *args, **kwargs):
        """Add loadbalancer to loadbalancer-listener.
        
        :param ref_obj: Loadbalancer object
        
        """
        if 'loadbalancer_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('loadbalancer_refs')
            self._original_loadbalancer_refs = (self.get_loadbalancer_refs() or [])[:]
        super(LoadbalancerListener, self).add_loadbalancer(*args, **kwargs)
    #end add_loadbalancer

    def del_loadbalancer(self, *args, **kwargs):
        if 'loadbalancer_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('loadbalancer_refs')
            self._original_loadbalancer_refs = (self.get_loadbalancer_refs() or [])[:]
        super(LoadbalancerListener, self).del_loadbalancer(*args, **kwargs)
    #end del_loadbalancer

    def set_loadbalancer_list(self, *args, **kwargs):
        """Set loadbalancer list for loadbalancer-listener.
        
        :param ref_obj_list: list of Loadbalancer object
        
        """
        self._pending_field_updates.add('loadbalancer_refs')
        self._pending_ref_updates.discard('loadbalancer_refs')
        super(LoadbalancerListener, self).set_loadbalancer_list(*args, **kwargs)
    #end set_loadbalancer_list


    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this loadbalancer-listener"""
        back_refs = super(LoadbalancerListener, self).get_loadbalancer_pool_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.loadbalancer_listener_read(id = self.uuid, fields = ['loadbalancer_pool_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_pool_back_refs', None)
        self.loadbalancer_pool_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_pool_back_refs

#end class LoadbalancerListener

class VirtualNetwork(pycontrail.gen.resource_common.VirtualNetwork):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, ecmp_hashing_include_fields=None, virtual_network_properties=None, provider_properties=None, virtual_network_network_id=None, route_target_list=None, import_route_target_list=None, export_route_target_list=None, router_external=None, is_shared=None, external_ipam=None, flood_unknown_unicast=False, multi_policy_service_chains_enabled=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if ecmp_hashing_include_fields is not None:
            pending_fields.append('ecmp_hashing_include_fields')
        if virtual_network_properties is not None:
            pending_fields.append('virtual_network_properties')
        if provider_properties is not None:
            pending_fields.append('provider_properties')
        if virtual_network_network_id is not None:
            pending_fields.append('virtual_network_network_id')
        if route_target_list is not None:
            pending_fields.append('route_target_list')
        if import_route_target_list is not None:
            pending_fields.append('import_route_target_list')
        if export_route_target_list is not None:
            pending_fields.append('export_route_target_list')
        if router_external is not None:
            pending_fields.append('router_external')
        if is_shared is not None:
            pending_fields.append('is_shared')
        if external_ipam is not None:
            pending_fields.append('external_ipam')
        if flood_unknown_unicast is not None:
            pending_fields.append('flood_unknown_unicast')
        if multi_policy_service_chains_enabled is not None:
            pending_fields.append('multi_policy_service_chains_enabled')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(VirtualNetwork, self).__init__(name, parent_obj, ecmp_hashing_include_fields, virtual_network_properties, provider_properties, virtual_network_network_id, route_target_list, import_route_target_list, export_route_target_list, router_external, is_shared, external_ipam, flood_unknown_unicast, multi_policy_service_chains_enabled, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'ecmp_hashing_include_fields' in kwargs:
            if kwargs['ecmp_hashing_include_fields'] is None:
                props_dict['ecmp_hashing_include_fields'] = None
            else:
                props_dict['ecmp_hashing_include_fields'] = pycontrail.gen.resource_xsd.EcmpHashingIncludeFields(**kwargs['ecmp_hashing_include_fields'])
        if 'virtual_network_properties' in kwargs:
            if kwargs['virtual_network_properties'] is None:
                props_dict['virtual_network_properties'] = None
            else:
                props_dict['virtual_network_properties'] = pycontrail.gen.resource_xsd.VirtualNetworkType(**kwargs['virtual_network_properties'])
        if 'provider_properties' in kwargs:
            if kwargs['provider_properties'] is None:
                props_dict['provider_properties'] = None
            else:
                props_dict['provider_properties'] = pycontrail.gen.resource_xsd.ProviderDetails(**kwargs['provider_properties'])
        if 'virtual_network_network_id' in kwargs:
            props_dict['virtual_network_network_id'] = kwargs['virtual_network_network_id']
        if 'route_target_list' in kwargs:
            if kwargs['route_target_list'] is None:
                props_dict['route_target_list'] = None
            else:
                props_dict['route_target_list'] = pycontrail.gen.resource_xsd.RouteTargetList(**kwargs['route_target_list'])
        if 'import_route_target_list' in kwargs:
            if kwargs['import_route_target_list'] is None:
                props_dict['import_route_target_list'] = None
            else:
                props_dict['import_route_target_list'] = pycontrail.gen.resource_xsd.RouteTargetList(**kwargs['import_route_target_list'])
        if 'export_route_target_list' in kwargs:
            if kwargs['export_route_target_list'] is None:
                props_dict['export_route_target_list'] = None
            else:
                props_dict['export_route_target_list'] = pycontrail.gen.resource_xsd.RouteTargetList(**kwargs['export_route_target_list'])
        if 'router_external' in kwargs:
            props_dict['router_external'] = kwargs['router_external']
        if 'is_shared' in kwargs:
            props_dict['is_shared'] = kwargs['is_shared']
        if 'external_ipam' in kwargs:
            props_dict['external_ipam'] = kwargs['external_ipam']
        if 'flood_unknown_unicast' in kwargs:
            props_dict['flood_unknown_unicast'] = kwargs['flood_unknown_unicast']
        if 'multi_policy_service_chains_enabled' in kwargs:
            props_dict['multi_policy_service_chains_enabled'] = kwargs['multi_policy_service_chains_enabled']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = VirtualNetwork(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'access_control_lists' in kwargs:
            obj.access_control_lists = kwargs['access_control_lists']
        if 'floating_ip_pools' in kwargs:
            obj.floating_ip_pools = kwargs['floating_ip_pools']
        if 'routing_instances' in kwargs:
            obj.routing_instances = kwargs['routing_instances']

        # add any specified references...
        if 'qos_forwarding_class_refs' in kwargs:
            obj.qos_forwarding_class_refs = kwargs['qos_forwarding_class_refs']
        if 'network_ipam_refs' in kwargs:
            obj.network_ipam_refs = kwargs['network_ipam_refs']
            for ref in obj.network_ipam_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.VnSubnetsType(**ref['attr'])
        if 'network_policy_refs' in kwargs:
            obj.network_policy_refs = kwargs['network_policy_refs']
            for ref in obj.network_policy_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.VirtualNetworkPolicyType(**ref['attr'])
        if 'route_table_refs' in kwargs:
            obj.route_table_refs = kwargs['route_table_refs']

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']
        if 'instance_ip_back_refs' in kwargs:
            obj.instance_ip_back_refs = kwargs['instance_ip_back_refs']
        if 'physical_router_back_refs' in kwargs:
            obj.physical_router_back_refs = kwargs['physical_router_back_refs']
        if 'logical_router_back_refs' in kwargs:
            obj.logical_router_back_refs = kwargs['logical_router_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.VirtualNetwork.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.VirtualNetwork.ecmp_hashing_include_fields.setter
    def ecmp_hashing_include_fields(self, ecmp_hashing_include_fields):
        """Set ecmp-hashing-include-fields for virtual-network.
        
        :param ecmp_hashing_include_fields: EcmpHashingIncludeFields object
        
        """
        if 'ecmp_hashing_include_fields' not in self._pending_field_updates:
            self._pending_field_updates.add('ecmp_hashing_include_fields')

        self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
    #end ecmp_hashing_include_fields

    def set_ecmp_hashing_include_fields(self, value):
        self.ecmp_hashing_include_fields = value
    #end set_ecmp_hashing_include_fields

    @pycontrail.gen.resource_common.VirtualNetwork.virtual_network_properties.setter
    def virtual_network_properties(self, virtual_network_properties):
        """Set virtual-network-properties for virtual-network.
        
        :param virtual_network_properties: VirtualNetworkType object
        
        """
        if 'virtual_network_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_network_properties')

        self._virtual_network_properties = virtual_network_properties
    #end virtual_network_properties

    def set_virtual_network_properties(self, value):
        self.virtual_network_properties = value
    #end set_virtual_network_properties

    @pycontrail.gen.resource_common.VirtualNetwork.provider_properties.setter
    def provider_properties(self, provider_properties):
        """Set provider-properties for virtual-network.
        
        :param provider_properties: ProviderDetails object
        
        """
        if 'provider_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('provider_properties')

        self._provider_properties = provider_properties
    #end provider_properties

    def set_provider_properties(self, value):
        self.provider_properties = value
    #end set_provider_properties

    @pycontrail.gen.resource_common.VirtualNetwork.virtual_network_network_id.setter
    def virtual_network_network_id(self, virtual_network_network_id):
        """Set virtual-network-network-id for virtual-network.
        
        :param virtual_network_network_id: xsd:integer object
        
        """
        if 'virtual_network_network_id' not in self._pending_field_updates:
            self._pending_field_updates.add('virtual_network_network_id')

        self._virtual_network_network_id = virtual_network_network_id
    #end virtual_network_network_id

    def set_virtual_network_network_id(self, value):
        self.virtual_network_network_id = value
    #end set_virtual_network_network_id

    @pycontrail.gen.resource_common.VirtualNetwork.route_target_list.setter
    def route_target_list(self, route_target_list):
        """Set route-target-list for virtual-network.
        
        :param route_target_list: RouteTargetList object
        
        """
        if 'route_target_list' not in self._pending_field_updates:
            self._pending_field_updates.add('route_target_list')

        self._route_target_list = route_target_list
    #end route_target_list

    def set_route_target_list(self, value):
        self.route_target_list = value
    #end set_route_target_list

    @pycontrail.gen.resource_common.VirtualNetwork.import_route_target_list.setter
    def import_route_target_list(self, import_route_target_list):
        """Set import-route-target-list for virtual-network.
        
        :param import_route_target_list: RouteTargetList object
        
        """
        if 'import_route_target_list' not in self._pending_field_updates:
            self._pending_field_updates.add('import_route_target_list')

        self._import_route_target_list = import_route_target_list
    #end import_route_target_list

    def set_import_route_target_list(self, value):
        self.import_route_target_list = value
    #end set_import_route_target_list

    @pycontrail.gen.resource_common.VirtualNetwork.export_route_target_list.setter
    def export_route_target_list(self, export_route_target_list):
        """Set export-route-target-list for virtual-network.
        
        :param export_route_target_list: RouteTargetList object
        
        """
        if 'export_route_target_list' not in self._pending_field_updates:
            self._pending_field_updates.add('export_route_target_list')

        self._export_route_target_list = export_route_target_list
    #end export_route_target_list

    def set_export_route_target_list(self, value):
        self.export_route_target_list = value
    #end set_export_route_target_list

    @pycontrail.gen.resource_common.VirtualNetwork.router_external.setter
    def router_external(self, router_external):
        """Set router-external for virtual-network.
        
        :param router_external: xsd:boolean object
        
        """
        if 'router_external' not in self._pending_field_updates:
            self._pending_field_updates.add('router_external')

        self._router_external = router_external
    #end router_external

    def set_router_external(self, value):
        self.router_external = value
    #end set_router_external

    @pycontrail.gen.resource_common.VirtualNetwork.is_shared.setter
    def is_shared(self, is_shared):
        """Set is-shared for virtual-network.
        
        :param is_shared: xsd:boolean object
        
        """
        if 'is_shared' not in self._pending_field_updates:
            self._pending_field_updates.add('is_shared')

        self._is_shared = is_shared
    #end is_shared

    def set_is_shared(self, value):
        self.is_shared = value
    #end set_is_shared

    @pycontrail.gen.resource_common.VirtualNetwork.external_ipam.setter
    def external_ipam(self, external_ipam):
        """Set external-ipam for virtual-network.
        
        :param external_ipam: xsd:boolean object
        
        """
        if 'external_ipam' not in self._pending_field_updates:
            self._pending_field_updates.add('external_ipam')

        self._external_ipam = external_ipam
    #end external_ipam

    def set_external_ipam(self, value):
        self.external_ipam = value
    #end set_external_ipam

    @pycontrail.gen.resource_common.VirtualNetwork.flood_unknown_unicast.setter
    def flood_unknown_unicast(self, flood_unknown_unicast):
        """Set flood-unknown-unicast for virtual-network.
        
        :param flood_unknown_unicast: xsd:boolean object
        
        """
        if 'flood_unknown_unicast' not in self._pending_field_updates:
            self._pending_field_updates.add('flood_unknown_unicast')

        self._flood_unknown_unicast = flood_unknown_unicast
    #end flood_unknown_unicast

    def set_flood_unknown_unicast(self, value):
        self.flood_unknown_unicast = value
    #end set_flood_unknown_unicast

    @pycontrail.gen.resource_common.VirtualNetwork.multi_policy_service_chains_enabled.setter
    def multi_policy_service_chains_enabled(self, multi_policy_service_chains_enabled):
        """Set multi-policy-service-chains-enabled for virtual-network.
        
        :param multi_policy_service_chains_enabled: xsd:Boolean object
        
        """
        if 'multi_policy_service_chains_enabled' not in self._pending_field_updates:
            self._pending_field_updates.add('multi_policy_service_chains_enabled')

        self._multi_policy_service_chains_enabled = multi_policy_service_chains_enabled
    #end multi_policy_service_chains_enabled

    def set_multi_policy_service_chains_enabled(self, value):
        self.multi_policy_service_chains_enabled = value
    #end set_multi_policy_service_chains_enabled

    @pycontrail.gen.resource_common.VirtualNetwork.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-network.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.VirtualNetwork.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-network.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.VirtualNetwork.display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-network.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_qos_forwarding_class(self, *args, **kwargs):
        """Set qos-forwarding-class for virtual-network.
        
        :param ref_obj: QosForwardingClass object
        
        """
        self._pending_field_updates.add('qos_forwarding_class_refs')
        self._pending_ref_updates.discard('qos_forwarding_class_refs')
        super(VirtualNetwork, self).set_qos_forwarding_class(*args, **kwargs)

    #end set_qos_forwarding_class

    def add_qos_forwarding_class(self, *args, **kwargs):
        """Add qos-forwarding-class to virtual-network.
        
        :param ref_obj: QosForwardingClass object
        
        """
        if 'qos_forwarding_class_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('qos_forwarding_class_refs')
            self._original_qos_forwarding_class_refs = (self.get_qos_forwarding_class_refs() or [])[:]
        super(VirtualNetwork, self).add_qos_forwarding_class(*args, **kwargs)
    #end add_qos_forwarding_class

    def del_qos_forwarding_class(self, *args, **kwargs):
        if 'qos_forwarding_class_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('qos_forwarding_class_refs')
            self._original_qos_forwarding_class_refs = (self.get_qos_forwarding_class_refs() or [])[:]
        super(VirtualNetwork, self).del_qos_forwarding_class(*args, **kwargs)
    #end del_qos_forwarding_class

    def set_qos_forwarding_class_list(self, *args, **kwargs):
        """Set qos-forwarding-class list for virtual-network.
        
        :param ref_obj_list: list of QosForwardingClass object
        
        """
        self._pending_field_updates.add('qos_forwarding_class_refs')
        self._pending_ref_updates.discard('qos_forwarding_class_refs')
        super(VirtualNetwork, self).set_qos_forwarding_class_list(*args, **kwargs)
    #end set_qos_forwarding_class_list

    def set_network_ipam(self, *args, **kwargs):
        """Set network-ipam for virtual-network.
        
        :param ref_obj: NetworkIpam object
        :param ref_data: VnSubnetsType object
        
        """
        self._pending_field_updates.add('network_ipam_refs')
        self._pending_ref_updates.discard('network_ipam_refs')
        super(VirtualNetwork, self).set_network_ipam(*args, **kwargs)

    #end set_network_ipam

    def add_network_ipam(self, *args, **kwargs):
        """Add network-ipam to virtual-network.
        
        :param ref_obj: NetworkIpam object
        :param ref_data: VnSubnetsType object
        
        """
        if 'network_ipam_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('network_ipam_refs')
            self._original_network_ipam_refs = (self.get_network_ipam_refs() or [])[:]
        super(VirtualNetwork, self).add_network_ipam(*args, **kwargs)
    #end add_network_ipam

    def del_network_ipam(self, *args, **kwargs):
        if 'network_ipam_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('network_ipam_refs')
            self._original_network_ipam_refs = (self.get_network_ipam_refs() or [])[:]
        super(VirtualNetwork, self).del_network_ipam(*args, **kwargs)
    #end del_network_ipam

    def set_network_ipam_list(self, *args, **kwargs):
        """Set network-ipam list for virtual-network.
        
        :param ref_obj_list: list of NetworkIpam object
        :param ref_data_list: list of VnSubnetsType summary
        
        """
        self._pending_field_updates.add('network_ipam_refs')
        self._pending_ref_updates.discard('network_ipam_refs')
        super(VirtualNetwork, self).set_network_ipam_list(*args, **kwargs)
    #end set_network_ipam_list

    def set_network_policy(self, *args, **kwargs):
        """Set network-policy for virtual-network.
        
        :param ref_obj: NetworkPolicy object
        :param ref_data: VirtualNetworkPolicyType object
        
        """
        self._pending_field_updates.add('network_policy_refs')
        self._pending_ref_updates.discard('network_policy_refs')
        super(VirtualNetwork, self).set_network_policy(*args, **kwargs)

    #end set_network_policy

    def add_network_policy(self, *args, **kwargs):
        """Add network-policy to virtual-network.
        
        :param ref_obj: NetworkPolicy object
        :param ref_data: VirtualNetworkPolicyType object
        
        """
        if 'network_policy_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('network_policy_refs')
            self._original_network_policy_refs = (self.get_network_policy_refs() or [])[:]
        super(VirtualNetwork, self).add_network_policy(*args, **kwargs)
    #end add_network_policy

    def del_network_policy(self, *args, **kwargs):
        if 'network_policy_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('network_policy_refs')
            self._original_network_policy_refs = (self.get_network_policy_refs() or [])[:]
        super(VirtualNetwork, self).del_network_policy(*args, **kwargs)
    #end del_network_policy

    def set_network_policy_list(self, *args, **kwargs):
        """Set network-policy list for virtual-network.
        
        :param ref_obj_list: list of NetworkPolicy object
        :param ref_data_list: list of VirtualNetworkPolicyType summary
        
        """
        self._pending_field_updates.add('network_policy_refs')
        self._pending_ref_updates.discard('network_policy_refs')
        super(VirtualNetwork, self).set_network_policy_list(*args, **kwargs)
    #end set_network_policy_list

    def set_route_table(self, *args, **kwargs):
        """Set route-table for virtual-network.
        
        :param ref_obj: RouteTable object
        
        """
        self._pending_field_updates.add('route_table_refs')
        self._pending_ref_updates.discard('route_table_refs')
        super(VirtualNetwork, self).set_route_table(*args, **kwargs)

    #end set_route_table

    def add_route_table(self, *args, **kwargs):
        """Add route-table to virtual-network.
        
        :param ref_obj: RouteTable object
        
        """
        if 'route_table_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('route_table_refs')
            self._original_route_table_refs = (self.get_route_table_refs() or [])[:]
        super(VirtualNetwork, self).add_route_table(*args, **kwargs)
    #end add_route_table

    def del_route_table(self, *args, **kwargs):
        if 'route_table_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('route_table_refs')
            self._original_route_table_refs = (self.get_route_table_refs() or [])[:]
        super(VirtualNetwork, self).del_route_table(*args, **kwargs)
    #end del_route_table

    def set_route_table_list(self, *args, **kwargs):
        """Set route-table list for virtual-network.
        
        :param ref_obj_list: list of RouteTable object
        
        """
        self._pending_field_updates.add('route_table_refs')
        self._pending_ref_updates.discard('route_table_refs')
        super(VirtualNetwork, self).set_route_table_list(*args, **kwargs)
    #end set_route_table_list

    def get_access_control_lists(self):
        children = super(VirtualNetwork, self).get_access_control_lists()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.virtual_network_read(id = self.uuid, fields = ['access_control_lists'])
            children = getattr(obj, 'access_control_lists', None)
            self.access_control_lists = children

        return children
    #end get_access_control_lists

    def get_floating_ip_pools(self):
        children = super(VirtualNetwork, self).get_floating_ip_pools()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.virtual_network_read(id = self.uuid, fields = ['floating_ip_pools'])
            children = getattr(obj, 'floating_ip_pools', None)
            self.floating_ip_pools = children

        return children
    #end get_floating_ip_pools

    def get_routing_instances(self):
        children = super(VirtualNetwork, self).get_routing_instances()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.virtual_network_read(id = self.uuid, fields = ['routing_instances'])
            children = getattr(obj, 'routing_instances', None)
            self.routing_instances = children

        return children
    #end get_routing_instances


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this virtual-network"""
        back_refs = super(VirtualNetwork, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_network_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

    def get_instance_ip_back_refs(self):
        """Return list of all instance-ips using this virtual-network"""
        back_refs = super(VirtualNetwork, self).get_instance_ip_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_network_read(id = self.uuid, fields = ['instance_ip_back_refs'])
        back_refs = getattr(obj, 'instance_ip_back_refs', None)
        self.instance_ip_back_refs = back_refs

        return back_refs
    #end get_instance_ip_back_refs

    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this virtual-network"""
        back_refs = super(VirtualNetwork, self).get_physical_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_network_read(id = self.uuid, fields = ['physical_router_back_refs'])
        back_refs = getattr(obj, 'physical_router_back_refs', None)
        self.physical_router_back_refs = back_refs

        return back_refs
    #end get_physical_router_back_refs

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this virtual-network"""
        back_refs = super(VirtualNetwork, self).get_logical_router_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.virtual_network_read(id = self.uuid, fields = ['logical_router_back_refs'])
        back_refs = getattr(obj, 'logical_router_back_refs', None)
        self.logical_router_back_refs = back_refs

        return back_refs
    #end get_logical_router_back_refs

#end class VirtualNetwork

class Project(pycontrail.gen.resource_common.Project):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, quota=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if quota is not None:
            pending_fields.append('quota')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(Project, self).__init__(name, parent_obj, quota, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'quota' in kwargs:
            if kwargs['quota'] is None:
                props_dict['quota'] = None
            else:
                props_dict['quota'] = pycontrail.gen.resource_xsd.QuotaType(**kwargs['quota'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = Project(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'security_groups' in kwargs:
            obj.security_groups = kwargs['security_groups']
        if 'virtual_networks' in kwargs:
            obj.virtual_networks = kwargs['virtual_networks']
        if 'qos_queues' in kwargs:
            obj.qos_queues = kwargs['qos_queues']
        if 'qos_forwarding_classs' in kwargs:
            obj.qos_forwarding_classs = kwargs['qos_forwarding_classs']
        if 'network_ipams' in kwargs:
            obj.network_ipams = kwargs['network_ipams']
        if 'network_policys' in kwargs:
            obj.network_policys = kwargs['network_policys']
        if 'virtual_machine_interfaces' in kwargs:
            obj.virtual_machine_interfaces = kwargs['virtual_machine_interfaces']
        if 'bgp_as_a_services' in kwargs:
            obj.bgp_as_a_services = kwargs['bgp_as_a_services']
        if 'routing_policys' in kwargs:
            obj.routing_policys = kwargs['routing_policys']
        if 'route_aggregates' in kwargs:
            obj.route_aggregates = kwargs['route_aggregates']
        if 'service_instances' in kwargs:
            obj.service_instances = kwargs['service_instances']
        if 'service_health_checks' in kwargs:
            obj.service_health_checks = kwargs['service_health_checks']
        if 'route_tables' in kwargs:
            obj.route_tables = kwargs['route_tables']
        if 'interface_route_tables' in kwargs:
            obj.interface_route_tables = kwargs['interface_route_tables']
        if 'logical_routers' in kwargs:
            obj.logical_routers = kwargs['logical_routers']
        if 'api_access_lists' in kwargs:
            obj.api_access_lists = kwargs['api_access_lists']
        if 'loadbalancer_pools' in kwargs:
            obj.loadbalancer_pools = kwargs['loadbalancer_pools']
        if 'loadbalancer_healthmonitors' in kwargs:
            obj.loadbalancer_healthmonitors = kwargs['loadbalancer_healthmonitors']
        if 'virtual_ips' in kwargs:
            obj.virtual_ips = kwargs['virtual_ips']
        if 'loadbalancer_listeners' in kwargs:
            obj.loadbalancer_listeners = kwargs['loadbalancer_listeners']
        if 'loadbalancers' in kwargs:
            obj.loadbalancers = kwargs['loadbalancers']

        # add any specified references...
        if 'namespace_refs' in kwargs:
            obj.namespace_refs = kwargs['namespace_refs']
            for ref in obj.namespace_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.SubnetType(**ref['attr'])
        if 'floating_ip_pool_refs' in kwargs:
            obj.floating_ip_pool_refs = kwargs['floating_ip_pool_refs']

        # and back references but no obj api for it...
        if 'floating_ip_back_refs' in kwargs:
            obj.floating_ip_back_refs = kwargs['floating_ip_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.Project.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.Project.quota.setter
    def quota(self, quota):
        """Set quota for project.
        
        :param quota: QuotaType object
        
        """
        if 'quota' not in self._pending_field_updates:
            self._pending_field_updates.add('quota')

        self._quota = quota
    #end quota

    def set_quota(self, value):
        self.quota = value
    #end set_quota

    @pycontrail.gen.resource_common.Project.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for project.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.Project.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for project.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.Project.display_name.setter
    def display_name(self, display_name):
        """Set display-name for project.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_namespace(self, *args, **kwargs):
        """Set namespace for project.
        
        :param ref_obj: Namespace object
        :param ref_data: SubnetType object
        
        """
        self._pending_field_updates.add('namespace_refs')
        self._pending_ref_updates.discard('namespace_refs')
        super(Project, self).set_namespace(*args, **kwargs)

    #end set_namespace

    def add_namespace(self, *args, **kwargs):
        """Add namespace to project.
        
        :param ref_obj: Namespace object
        :param ref_data: SubnetType object
        
        """
        if 'namespace_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('namespace_refs')
            self._original_namespace_refs = (self.get_namespace_refs() or [])[:]
        super(Project, self).add_namespace(*args, **kwargs)
    #end add_namespace

    def del_namespace(self, *args, **kwargs):
        if 'namespace_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('namespace_refs')
            self._original_namespace_refs = (self.get_namespace_refs() or [])[:]
        super(Project, self).del_namespace(*args, **kwargs)
    #end del_namespace

    def set_namespace_list(self, *args, **kwargs):
        """Set namespace list for project.
        
        :param ref_obj_list: list of Namespace object
        :param ref_data_list: list of SubnetType summary
        
        """
        self._pending_field_updates.add('namespace_refs')
        self._pending_ref_updates.discard('namespace_refs')
        super(Project, self).set_namespace_list(*args, **kwargs)
    #end set_namespace_list

    def set_floating_ip_pool(self, *args, **kwargs):
        """Set floating-ip-pool for project.
        
        :param ref_obj: FloatingIpPool object
        
        """
        self._pending_field_updates.add('floating_ip_pool_refs')
        self._pending_ref_updates.discard('floating_ip_pool_refs')
        super(Project, self).set_floating_ip_pool(*args, **kwargs)

    #end set_floating_ip_pool

    def add_floating_ip_pool(self, *args, **kwargs):
        """Add floating-ip-pool to project.
        
        :param ref_obj: FloatingIpPool object
        
        """
        if 'floating_ip_pool_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('floating_ip_pool_refs')
            self._original_floating_ip_pool_refs = (self.get_floating_ip_pool_refs() or [])[:]
        super(Project, self).add_floating_ip_pool(*args, **kwargs)
    #end add_floating_ip_pool

    def del_floating_ip_pool(self, *args, **kwargs):
        if 'floating_ip_pool_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('floating_ip_pool_refs')
            self._original_floating_ip_pool_refs = (self.get_floating_ip_pool_refs() or [])[:]
        super(Project, self).del_floating_ip_pool(*args, **kwargs)
    #end del_floating_ip_pool

    def set_floating_ip_pool_list(self, *args, **kwargs):
        """Set floating-ip-pool list for project.
        
        :param ref_obj_list: list of FloatingIpPool object
        
        """
        self._pending_field_updates.add('floating_ip_pool_refs')
        self._pending_ref_updates.discard('floating_ip_pool_refs')
        super(Project, self).set_floating_ip_pool_list(*args, **kwargs)
    #end set_floating_ip_pool_list

    def get_security_groups(self):
        children = super(Project, self).get_security_groups()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['security_groups'])
            children = getattr(obj, 'security_groups', None)
            self.security_groups = children

        return children
    #end get_security_groups

    def get_virtual_networks(self):
        children = super(Project, self).get_virtual_networks()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['virtual_networks'])
            children = getattr(obj, 'virtual_networks', None)
            self.virtual_networks = children

        return children
    #end get_virtual_networks

    def get_qos_queues(self):
        children = super(Project, self).get_qos_queues()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['qos_queues'])
            children = getattr(obj, 'qos_queues', None)
            self.qos_queues = children

        return children
    #end get_qos_queues

    def get_qos_forwarding_classs(self):
        children = super(Project, self).get_qos_forwarding_classs()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['qos_forwarding_classs'])
            children = getattr(obj, 'qos_forwarding_classs', None)
            self.qos_forwarding_classs = children

        return children
    #end get_qos_forwarding_classs

    def get_network_ipams(self):
        children = super(Project, self).get_network_ipams()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['network_ipams'])
            children = getattr(obj, 'network_ipams', None)
            self.network_ipams = children

        return children
    #end get_network_ipams

    def get_network_policys(self):
        children = super(Project, self).get_network_policys()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['network_policys'])
            children = getattr(obj, 'network_policys', None)
            self.network_policys = children

        return children
    #end get_network_policys

    def get_virtual_machine_interfaces(self):
        children = super(Project, self).get_virtual_machine_interfaces()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['virtual_machine_interfaces'])
            children = getattr(obj, 'virtual_machine_interfaces', None)
            self.virtual_machine_interfaces = children

        return children
    #end get_virtual_machine_interfaces

    def get_bgp_as_a_services(self):
        children = super(Project, self).get_bgp_as_a_services()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['bgp_as_a_services'])
            children = getattr(obj, 'bgp_as_a_services', None)
            self.bgp_as_a_services = children

        return children
    #end get_bgp_as_a_services

    def get_routing_policys(self):
        children = super(Project, self).get_routing_policys()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['routing_policys'])
            children = getattr(obj, 'routing_policys', None)
            self.routing_policys = children

        return children
    #end get_routing_policys

    def get_route_aggregates(self):
        children = super(Project, self).get_route_aggregates()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['route_aggregates'])
            children = getattr(obj, 'route_aggregates', None)
            self.route_aggregates = children

        return children
    #end get_route_aggregates

    def get_service_instances(self):
        children = super(Project, self).get_service_instances()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['service_instances'])
            children = getattr(obj, 'service_instances', None)
            self.service_instances = children

        return children
    #end get_service_instances

    def get_service_health_checks(self):
        children = super(Project, self).get_service_health_checks()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['service_health_checks'])
            children = getattr(obj, 'service_health_checks', None)
            self.service_health_checks = children

        return children
    #end get_service_health_checks

    def get_route_tables(self):
        children = super(Project, self).get_route_tables()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['route_tables'])
            children = getattr(obj, 'route_tables', None)
            self.route_tables = children

        return children
    #end get_route_tables

    def get_interface_route_tables(self):
        children = super(Project, self).get_interface_route_tables()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['interface_route_tables'])
            children = getattr(obj, 'interface_route_tables', None)
            self.interface_route_tables = children

        return children
    #end get_interface_route_tables

    def get_logical_routers(self):
        children = super(Project, self).get_logical_routers()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['logical_routers'])
            children = getattr(obj, 'logical_routers', None)
            self.logical_routers = children

        return children
    #end get_logical_routers

    def get_api_access_lists(self):
        children = super(Project, self).get_api_access_lists()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['api_access_lists'])
            children = getattr(obj, 'api_access_lists', None)
            self.api_access_lists = children

        return children
    #end get_api_access_lists

    def get_loadbalancer_pools(self):
        children = super(Project, self).get_loadbalancer_pools()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['loadbalancer_pools'])
            children = getattr(obj, 'loadbalancer_pools', None)
            self.loadbalancer_pools = children

        return children
    #end get_loadbalancer_pools

    def get_loadbalancer_healthmonitors(self):
        children = super(Project, self).get_loadbalancer_healthmonitors()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['loadbalancer_healthmonitors'])
            children = getattr(obj, 'loadbalancer_healthmonitors', None)
            self.loadbalancer_healthmonitors = children

        return children
    #end get_loadbalancer_healthmonitors

    def get_virtual_ips(self):
        children = super(Project, self).get_virtual_ips()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['virtual_ips'])
            children = getattr(obj, 'virtual_ips', None)
            self.virtual_ips = children

        return children
    #end get_virtual_ips

    def get_loadbalancer_listeners(self):
        children = super(Project, self).get_loadbalancer_listeners()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['loadbalancer_listeners'])
            children = getattr(obj, 'loadbalancer_listeners', None)
            self.loadbalancer_listeners = children

        return children
    #end get_loadbalancer_listeners

    def get_loadbalancers(self):
        children = super(Project, self).get_loadbalancers()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.project_read(id = self.uuid, fields = ['loadbalancers'])
            children = getattr(obj, 'loadbalancers', None)
            self.loadbalancers = children

        return children
    #end get_loadbalancers


    def get_floating_ip_back_refs(self):
        """Return list of all floating-ips using this project"""
        back_refs = super(Project, self).get_floating_ip_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.project_read(id = self.uuid, fields = ['floating_ip_back_refs'])
        back_refs = getattr(obj, 'floating_ip_back_refs', None)
        self.floating_ip_back_refs = back_refs

        return back_refs
    #end get_floating_ip_back_refs

#end class Project

class QosForwardingClass(pycontrail.gen.resource_common.QosForwardingClass):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, dscp=None, trusted=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if dscp is not None:
            pending_fields.append('dscp')
        if trusted is not None:
            pending_fields.append('trusted')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(QosForwardingClass, self).__init__(name, parent_obj, dscp, trusted, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'dscp' in kwargs:
            props_dict['dscp'] = kwargs['dscp']
        if 'trusted' in kwargs:
            props_dict['trusted'] = kwargs['trusted']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = QosForwardingClass(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'qos_queue_refs' in kwargs:
            obj.qos_queue_refs = kwargs['qos_queue_refs']

        # and back references but no obj api for it...
        if 'virtual_network_back_refs' in kwargs:
            obj.virtual_network_back_refs = kwargs['virtual_network_back_refs']
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.QosForwardingClass.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.QosForwardingClass.dscp.setter
    def dscp(self, dscp):
        """Set dscp for qos-forwarding-class.
        
        :param dscp: xsd:integer object
        
        """
        if 'dscp' not in self._pending_field_updates:
            self._pending_field_updates.add('dscp')

        self._dscp = dscp
    #end dscp

    def set_dscp(self, value):
        self.dscp = value
    #end set_dscp

    @pycontrail.gen.resource_common.QosForwardingClass.trusted.setter
    def trusted(self, trusted):
        """Set trusted for qos-forwarding-class.
        
        :param trusted: xsd:boolean object
        
        """
        if 'trusted' not in self._pending_field_updates:
            self._pending_field_updates.add('trusted')

        self._trusted = trusted
    #end trusted

    def set_trusted(self, value):
        self.trusted = value
    #end set_trusted

    @pycontrail.gen.resource_common.QosForwardingClass.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for qos-forwarding-class.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.QosForwardingClass.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for qos-forwarding-class.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.QosForwardingClass.display_name.setter
    def display_name(self, display_name):
        """Set display-name for qos-forwarding-class.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_qos_queue(self, *args, **kwargs):
        """Set qos-queue for qos-forwarding-class.
        
        :param ref_obj: QosQueue object
        
        """
        self._pending_field_updates.add('qos_queue_refs')
        self._pending_ref_updates.discard('qos_queue_refs')
        super(QosForwardingClass, self).set_qos_queue(*args, **kwargs)

    #end set_qos_queue

    def add_qos_queue(self, *args, **kwargs):
        """Add qos-queue to qos-forwarding-class.
        
        :param ref_obj: QosQueue object
        
        """
        if 'qos_queue_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('qos_queue_refs')
            self._original_qos_queue_refs = (self.get_qos_queue_refs() or [])[:]
        super(QosForwardingClass, self).add_qos_queue(*args, **kwargs)
    #end add_qos_queue

    def del_qos_queue(self, *args, **kwargs):
        if 'qos_queue_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('qos_queue_refs')
            self._original_qos_queue_refs = (self.get_qos_queue_refs() or [])[:]
        super(QosForwardingClass, self).del_qos_queue(*args, **kwargs)
    #end del_qos_queue

    def set_qos_queue_list(self, *args, **kwargs):
        """Set qos-queue list for qos-forwarding-class.
        
        :param ref_obj_list: list of QosQueue object
        
        """
        self._pending_field_updates.add('qos_queue_refs')
        self._pending_ref_updates.discard('qos_queue_refs')
        super(QosForwardingClass, self).set_qos_queue_list(*args, **kwargs)
    #end set_qos_queue_list


    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this qos-forwarding-class"""
        back_refs = super(QosForwardingClass, self).get_virtual_network_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.qos_forwarding_class_read(id = self.uuid, fields = ['virtual_network_back_refs'])
        back_refs = getattr(obj, 'virtual_network_back_refs', None)
        self.virtual_network_back_refs = back_refs

        return back_refs
    #end get_virtual_network_back_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this qos-forwarding-class"""
        back_refs = super(QosForwardingClass, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.qos_forwarding_class_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

#end class QosForwardingClass

class Loadbalancer(pycontrail.gen.resource_common.Loadbalancer):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, loadbalancer_properties=None, loadbalancer_provider=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if loadbalancer_properties is not None:
            pending_fields.append('loadbalancer_properties')
        if loadbalancer_provider is not None:
            pending_fields.append('loadbalancer_provider')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(Loadbalancer, self).__init__(name, parent_obj, loadbalancer_properties, loadbalancer_provider, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'loadbalancer_properties' in kwargs:
            if kwargs['loadbalancer_properties'] is None:
                props_dict['loadbalancer_properties'] = None
            else:
                props_dict['loadbalancer_properties'] = pycontrail.gen.resource_xsd.LoadbalancerType(**kwargs['loadbalancer_properties'])
        if 'loadbalancer_provider' in kwargs:
            props_dict['loadbalancer_provider'] = kwargs['loadbalancer_provider']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = Loadbalancer(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']

        # and back references but no obj api for it...
        if 'loadbalancer_listener_back_refs' in kwargs:
            obj.loadbalancer_listener_back_refs = kwargs['loadbalancer_listener_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.Loadbalancer.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.Loadbalancer.loadbalancer_properties.setter
    def loadbalancer_properties(self, loadbalancer_properties):
        """Set loadbalancer-properties for loadbalancer.
        
        :param loadbalancer_properties: LoadbalancerType object
        
        """
        if 'loadbalancer_properties' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_properties')

        self._loadbalancer_properties = loadbalancer_properties
    #end loadbalancer_properties

    def set_loadbalancer_properties(self, value):
        self.loadbalancer_properties = value
    #end set_loadbalancer_properties

    @pycontrail.gen.resource_common.Loadbalancer.loadbalancer_provider.setter
    def loadbalancer_provider(self, loadbalancer_provider):
        """Set loadbalancer-provider for loadbalancer.
        
        :param loadbalancer_provider: xsd:string object
        
        """
        if 'loadbalancer_provider' not in self._pending_field_updates:
            self._pending_field_updates.add('loadbalancer_provider')

        self._loadbalancer_provider = loadbalancer_provider
    #end loadbalancer_provider

    def set_loadbalancer_provider(self, value):
        self.loadbalancer_provider = value
    #end set_loadbalancer_provider

    @pycontrail.gen.resource_common.Loadbalancer.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.Loadbalancer.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.Loadbalancer.display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for loadbalancer.
        
        :param ref_obj: ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(Loadbalancer, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to loadbalancer.
        
        :param ref_obj: ServiceInstance object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(Loadbalancer, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(Loadbalancer, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for loadbalancer.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(Loadbalancer, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for loadbalancer.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(Loadbalancer, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to loadbalancer.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(Loadbalancer, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(Loadbalancer, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for loadbalancer.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(Loadbalancer, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list


    def get_loadbalancer_listener_back_refs(self):
        """Return list of all loadbalancer-listeners using this loadbalancer"""
        back_refs = super(Loadbalancer, self).get_loadbalancer_listener_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.loadbalancer_read(id = self.uuid, fields = ['loadbalancer_listener_back_refs'])
        back_refs = getattr(obj, 'loadbalancer_listener_back_refs', None)
        self.loadbalancer_listener_back_refs = back_refs

        return back_refs
    #end get_loadbalancer_listener_back_refs

#end class Loadbalancer

class DatabaseNode(pycontrail.gen.resource_common.DatabaseNode):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, database_node_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if database_node_ip_address is not None:
            pending_fields.append('database_node_ip_address')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(DatabaseNode, self).__init__(name, parent_obj, database_node_ip_address, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'database_node_ip_address' in kwargs:
            props_dict['database_node_ip_address'] = kwargs['database_node_ip_address']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = DatabaseNode(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.DatabaseNode.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.DatabaseNode.database_node_ip_address.setter
    def database_node_ip_address(self, database_node_ip_address):
        """Set database-node-ip-address for database-node.
        
        :param database_node_ip_address: IpAddressType object
        
        """
        if 'database_node_ip_address' not in self._pending_field_updates:
            self._pending_field_updates.add('database_node_ip_address')

        self._database_node_ip_address = database_node_ip_address
    #end database_node_ip_address

    def set_database_node_ip_address(self, value):
        self.database_node_ip_address = value
    #end set_database_node_ip_address

    @pycontrail.gen.resource_common.DatabaseNode.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for database-node.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.DatabaseNode.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for database-node.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.DatabaseNode.display_name.setter
    def display_name(self, display_name):
        """Set display-name for database-node.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name


#end class DatabaseNode

class RoutingInstance(pycontrail.gen.resource_common.RoutingInstance):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, service_chain_information=None, ipv6_service_chain_information=None, routing_instance_is_default=False, routing_instance_has_pnf=False, static_route_entries=None, default_ce_protocol=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if service_chain_information is not None:
            pending_fields.append('service_chain_information')
        if ipv6_service_chain_information is not None:
            pending_fields.append('ipv6_service_chain_information')
        if routing_instance_is_default is not None:
            pending_fields.append('routing_instance_is_default')
        if routing_instance_has_pnf is not None:
            pending_fields.append('routing_instance_has_pnf')
        if static_route_entries is not None:
            pending_fields.append('static_route_entries')
        if default_ce_protocol is not None:
            pending_fields.append('default_ce_protocol')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(RoutingInstance, self).__init__(name, parent_obj, service_chain_information, ipv6_service_chain_information, routing_instance_is_default, routing_instance_has_pnf, static_route_entries, default_ce_protocol, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'service_chain_information' in kwargs:
            if kwargs['service_chain_information'] is None:
                props_dict['service_chain_information'] = None
            else:
                props_dict['service_chain_information'] = pycontrail.gen.resource_xsd.ServiceChainInfo(**kwargs['service_chain_information'])
        if 'ipv6_service_chain_information' in kwargs:
            if kwargs['ipv6_service_chain_information'] is None:
                props_dict['ipv6_service_chain_information'] = None
            else:
                props_dict['ipv6_service_chain_information'] = pycontrail.gen.resource_xsd.ServiceChainInfo(**kwargs['ipv6_service_chain_information'])
        if 'routing_instance_is_default' in kwargs:
            props_dict['routing_instance_is_default'] = kwargs['routing_instance_is_default']
        if 'routing_instance_has_pnf' in kwargs:
            props_dict['routing_instance_has_pnf'] = kwargs['routing_instance_has_pnf']
        if 'static_route_entries' in kwargs:
            if kwargs['static_route_entries'] is None:
                props_dict['static_route_entries'] = None
            else:
                props_dict['static_route_entries'] = pycontrail.gen.resource_xsd.StaticRouteEntriesType(**kwargs['static_route_entries'])
        if 'default_ce_protocol' in kwargs:
            if kwargs['default_ce_protocol'] is None:
                props_dict['default_ce_protocol'] = None
            else:
                props_dict['default_ce_protocol'] = pycontrail.gen.resource_xsd.DefaultProtocolType(**kwargs['default_ce_protocol'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = RoutingInstance(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...
        if 'bgp_routers' in kwargs:
            obj.bgp_routers = kwargs['bgp_routers']

        # add any specified references...
        if 'routing_instance_refs' in kwargs:
            obj.routing_instance_refs = kwargs['routing_instance_refs']
            for ref in obj.routing_instance_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.ConnectionType(**ref['attr'])
        if 'route_target_refs' in kwargs:
            obj.route_target_refs = kwargs['route_target_refs']
            for ref in obj.route_target_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.InstanceTargetType(**ref['attr'])

        # and back references but no obj api for it...
        if 'virtual_machine_interface_back_refs' in kwargs:
            obj.virtual_machine_interface_back_refs = kwargs['virtual_machine_interface_back_refs']
        if 'route_aggregate_back_refs' in kwargs:
            obj.route_aggregate_back_refs = kwargs['route_aggregate_back_refs']
        if 'routing_policy_back_refs' in kwargs:
            obj.routing_policy_back_refs = kwargs['routing_policy_back_refs']
        if 'routing_instance_back_refs' in kwargs:
            obj.routing_instance_back_refs = kwargs['routing_instance_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.RoutingInstance.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.RoutingInstance.service_chain_information.setter
    def service_chain_information(self, service_chain_information):
        """Set service-chain-information for routing-instance.
        
        :param service_chain_information: ServiceChainInfo object
        
        """
        if 'service_chain_information' not in self._pending_field_updates:
            self._pending_field_updates.add('service_chain_information')

        self._service_chain_information = service_chain_information
    #end service_chain_information

    def set_service_chain_information(self, value):
        self.service_chain_information = value
    #end set_service_chain_information

    @pycontrail.gen.resource_common.RoutingInstance.ipv6_service_chain_information.setter
    def ipv6_service_chain_information(self, ipv6_service_chain_information):
        """Set ipv6-service-chain-information for routing-instance.
        
        :param ipv6_service_chain_information: ServiceChainInfo object
        
        """
        if 'ipv6_service_chain_information' not in self._pending_field_updates:
            self._pending_field_updates.add('ipv6_service_chain_information')

        self._ipv6_service_chain_information = ipv6_service_chain_information
    #end ipv6_service_chain_information

    def set_ipv6_service_chain_information(self, value):
        self.ipv6_service_chain_information = value
    #end set_ipv6_service_chain_information

    @pycontrail.gen.resource_common.RoutingInstance.routing_instance_is_default.setter
    def routing_instance_is_default(self, routing_instance_is_default):
        """Set routing-instance-is-default for routing-instance.
        
        :param routing_instance_is_default: xsd:boolean object
        
        """
        if 'routing_instance_is_default' not in self._pending_field_updates:
            self._pending_field_updates.add('routing_instance_is_default')

        self._routing_instance_is_default = routing_instance_is_default
    #end routing_instance_is_default

    def set_routing_instance_is_default(self, value):
        self.routing_instance_is_default = value
    #end set_routing_instance_is_default

    @pycontrail.gen.resource_common.RoutingInstance.routing_instance_has_pnf.setter
    def routing_instance_has_pnf(self, routing_instance_has_pnf):
        """Set routing-instance-has-pnf for routing-instance.
        
        :param routing_instance_has_pnf: xsd:boolean object
        
        """
        if 'routing_instance_has_pnf' not in self._pending_field_updates:
            self._pending_field_updates.add('routing_instance_has_pnf')

        self._routing_instance_has_pnf = routing_instance_has_pnf
    #end routing_instance_has_pnf

    def set_routing_instance_has_pnf(self, value):
        self.routing_instance_has_pnf = value
    #end set_routing_instance_has_pnf

    @pycontrail.gen.resource_common.RoutingInstance.static_route_entries.setter
    def static_route_entries(self, static_route_entries):
        """Set static-route-entries for routing-instance.
        
        :param static_route_entries: StaticRouteEntriesType object
        
        """
        if 'static_route_entries' not in self._pending_field_updates:
            self._pending_field_updates.add('static_route_entries')

        self._static_route_entries = static_route_entries
    #end static_route_entries

    def set_static_route_entries(self, value):
        self.static_route_entries = value
    #end set_static_route_entries

    @pycontrail.gen.resource_common.RoutingInstance.default_ce_protocol.setter
    def default_ce_protocol(self, default_ce_protocol):
        """Set default-ce-protocol for routing-instance.
        
        :param default_ce_protocol: DefaultProtocolType object
        
        """
        if 'default_ce_protocol' not in self._pending_field_updates:
            self._pending_field_updates.add('default_ce_protocol')

        self._default_ce_protocol = default_ce_protocol
    #end default_ce_protocol

    def set_default_ce_protocol(self, value):
        self.default_ce_protocol = value
    #end set_default_ce_protocol

    @pycontrail.gen.resource_common.RoutingInstance.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for routing-instance.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.RoutingInstance.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for routing-instance.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.RoutingInstance.display_name.setter
    def display_name(self, display_name):
        """Set display-name for routing-instance.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_routing_instance(self, *args, **kwargs):
        """Set routing-instance for routing-instance.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: ConnectionType object
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(RoutingInstance, self).set_routing_instance(*args, **kwargs)

    #end set_routing_instance

    def add_routing_instance(self, *args, **kwargs):
        """Add routing-instance to routing-instance.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: ConnectionType object
        
        """
        if 'routing_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(RoutingInstance, self).add_routing_instance(*args, **kwargs)
    #end add_routing_instance

    def del_routing_instance(self, *args, **kwargs):
        if 'routing_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(RoutingInstance, self).del_routing_instance(*args, **kwargs)
    #end del_routing_instance

    def set_routing_instance_list(self, *args, **kwargs):
        """Set routing-instance list for routing-instance.
        
        :param ref_obj_list: list of RoutingInstance object
        :param ref_data_list: list of ConnectionType summary
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(RoutingInstance, self).set_routing_instance_list(*args, **kwargs)
    #end set_routing_instance_list

    def set_route_target(self, *args, **kwargs):
        """Set route-target for routing-instance.
        
        :param ref_obj: RouteTarget object
        :param ref_data: InstanceTargetType object
        
        """
        self._pending_field_updates.add('route_target_refs')
        self._pending_ref_updates.discard('route_target_refs')
        super(RoutingInstance, self).set_route_target(*args, **kwargs)

    #end set_route_target

    def add_route_target(self, *args, **kwargs):
        """Add route-target to routing-instance.
        
        :param ref_obj: RouteTarget object
        :param ref_data: InstanceTargetType object
        
        """
        if 'route_target_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('route_target_refs')
            self._original_route_target_refs = (self.get_route_target_refs() or [])[:]
        super(RoutingInstance, self).add_route_target(*args, **kwargs)
    #end add_route_target

    def del_route_target(self, *args, **kwargs):
        if 'route_target_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('route_target_refs')
            self._original_route_target_refs = (self.get_route_target_refs() or [])[:]
        super(RoutingInstance, self).del_route_target(*args, **kwargs)
    #end del_route_target

    def set_route_target_list(self, *args, **kwargs):
        """Set route-target list for routing-instance.
        
        :param ref_obj_list: list of RouteTarget object
        :param ref_data_list: list of InstanceTargetType summary
        
        """
        self._pending_field_updates.add('route_target_refs')
        self._pending_ref_updates.discard('route_target_refs')
        super(RoutingInstance, self).set_route_target_list(*args, **kwargs)
    #end set_route_target_list

    def get_bgp_routers(self):
        children = super(RoutingInstance, self).get_bgp_routers()
        if not children: # read it for first time
            # if object not created/read from lib can't service
            svr_conn = self._server_conn
            if not svr_conn:
                return None

            obj = svr_conn.routing_instance_read(id = self.uuid, fields = ['bgp_routers'])
            children = getattr(obj, 'bgp_routers', None)
            self.bgp_routers = children

        return children
    #end get_bgp_routers


    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this routing-instance"""
        back_refs = super(RoutingInstance, self).get_virtual_machine_interface_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.routing_instance_read(id = self.uuid, fields = ['virtual_machine_interface_back_refs'])
        back_refs = getattr(obj, 'virtual_machine_interface_back_refs', None)
        self.virtual_machine_interface_back_refs = back_refs

        return back_refs
    #end get_virtual_machine_interface_back_refs

    def get_route_aggregate_back_refs(self):
        """Return list of all route-aggregates using this routing-instance"""
        back_refs = super(RoutingInstance, self).get_route_aggregate_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.routing_instance_read(id = self.uuid, fields = ['route_aggregate_back_refs'])
        back_refs = getattr(obj, 'route_aggregate_back_refs', None)
        self.route_aggregate_back_refs = back_refs

        return back_refs
    #end get_route_aggregate_back_refs

    def get_routing_policy_back_refs(self):
        """Return list of all routing-policys using this routing-instance"""
        back_refs = super(RoutingInstance, self).get_routing_policy_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.routing_instance_read(id = self.uuid, fields = ['routing_policy_back_refs'])
        back_refs = getattr(obj, 'routing_policy_back_refs', None)
        self.routing_policy_back_refs = back_refs

        return back_refs
    #end get_routing_policy_back_refs

    def get_routing_instance_back_refs(self):
        """Return list of all routing-instances using this routing-instance"""
        back_refs = super(RoutingInstance, self).get_routing_instance_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.routing_instance_read(id = self.uuid, fields = ['routing_instance_back_refs'])
        back_refs = getattr(obj, 'routing_instance_back_refs', None)
        self.routing_instance_back_refs = back_refs

        return back_refs
    #end get_routing_instance_back_refs

#end class RoutingInstance

class NetworkIpam(pycontrail.gen.resource_common.NetworkIpam):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, network_ipam_mgmt=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if network_ipam_mgmt is not None:
            pending_fields.append('network_ipam_mgmt')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(NetworkIpam, self).__init__(name, parent_obj, network_ipam_mgmt, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'network_ipam_mgmt' in kwargs:
            if kwargs['network_ipam_mgmt'] is None:
                props_dict['network_ipam_mgmt'] = None
            else:
                props_dict['network_ipam_mgmt'] = pycontrail.gen.resource_xsd.IpamType(**kwargs['network_ipam_mgmt'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = NetworkIpam(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_DNS_refs' in kwargs:
            obj.virtual_DNS_refs = kwargs['virtual_DNS_refs']

        # and back references but no obj api for it...
        if 'virtual_network_back_refs' in kwargs:
            obj.virtual_network_back_refs = kwargs['virtual_network_back_refs']

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.NetworkIpam.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.NetworkIpam.network_ipam_mgmt.setter
    def network_ipam_mgmt(self, network_ipam_mgmt):
        """Set network-ipam-mgmt for network-ipam.
        
        :param network_ipam_mgmt: IpamType object
        
        """
        if 'network_ipam_mgmt' not in self._pending_field_updates:
            self._pending_field_updates.add('network_ipam_mgmt')

        self._network_ipam_mgmt = network_ipam_mgmt
    #end network_ipam_mgmt

    def set_network_ipam_mgmt(self, value):
        self.network_ipam_mgmt = value
    #end set_network_ipam_mgmt

    @pycontrail.gen.resource_common.NetworkIpam.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for network-ipam.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.NetworkIpam.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for network-ipam.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.NetworkIpam.display_name.setter
    def display_name(self, display_name):
        """Set display-name for network-ipam.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_DNS(self, *args, **kwargs):
        """Set virtual-DNS for network-ipam.
        
        :param ref_obj: VirtualDns object
        
        """
        self._pending_field_updates.add('virtual_DNS_refs')
        self._pending_ref_updates.discard('virtual_DNS_refs')
        super(NetworkIpam, self).set_virtual_DNS(*args, **kwargs)

    #end set_virtual_DNS

    def add_virtual_DNS(self, *args, **kwargs):
        """Add virtual-DNS to network-ipam.
        
        :param ref_obj: VirtualDns object
        
        """
        if 'virtual_DNS_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_DNS_refs')
            self._original_virtual_DNS_refs = (self.get_virtual_DNS_refs() or [])[:]
        super(NetworkIpam, self).add_virtual_DNS(*args, **kwargs)
    #end add_virtual_DNS

    def del_virtual_DNS(self, *args, **kwargs):
        if 'virtual_DNS_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_DNS_refs')
            self._original_virtual_DNS_refs = (self.get_virtual_DNS_refs() or [])[:]
        super(NetworkIpam, self).del_virtual_DNS(*args, **kwargs)
    #end del_virtual_DNS

    def set_virtual_DNS_list(self, *args, **kwargs):
        """Set virtual-DNS list for network-ipam.
        
        :param ref_obj_list: list of VirtualDns object
        
        """
        self._pending_field_updates.add('virtual_DNS_refs')
        self._pending_ref_updates.discard('virtual_DNS_refs')
        super(NetworkIpam, self).set_virtual_DNS_list(*args, **kwargs)
    #end set_virtual_DNS_list


    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this network-ipam"""
        back_refs = super(NetworkIpam, self).get_virtual_network_back_refs()
        if back_refs:
            return back_refs
        # if object not created/read from lib can't service
        svr_conn = self._server_conn
        if not svr_conn:
            return None

        obj = svr_conn.network_ipam_read(id = self.uuid, fields = ['virtual_network_back_refs'])
        back_refs = getattr(obj, 'virtual_network_back_refs', None)
        self.virtual_network_back_refs = back_refs

        return back_refs
    #end get_virtual_network_back_refs

#end class NetworkIpam

class RouteAggregate(pycontrail.gen.resource_common.RouteAggregate):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, aggregate_route_entries=None, aggregate_route_nexthop=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if aggregate_route_entries is not None:
            pending_fields.append('aggregate_route_entries')
        if aggregate_route_nexthop is not None:
            pending_fields.append('aggregate_route_nexthop')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(RouteAggregate, self).__init__(name, parent_obj, aggregate_route_entries, aggregate_route_nexthop, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'aggregate_route_entries' in kwargs:
            if kwargs['aggregate_route_entries'] is None:
                props_dict['aggregate_route_entries'] = None
            else:
                props_dict['aggregate_route_entries'] = pycontrail.gen.resource_xsd.RouteListType(**kwargs['aggregate_route_entries'])
        if 'aggregate_route_nexthop' in kwargs:
            props_dict['aggregate_route_nexthop'] = kwargs['aggregate_route_nexthop']
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = RouteAggregate(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']
            for ref in obj.service_instance_refs:
                ref['attr'] = pycontrail.gen.resource_xsd.ServiceInterfaceTag(**ref['attr'])
        if 'routing_instance_refs' in kwargs:
            obj.routing_instance_refs = kwargs['routing_instance_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.RouteAggregate.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.RouteAggregate.aggregate_route_entries.setter
    def aggregate_route_entries(self, aggregate_route_entries):
        """Set aggregate-route-entries for route-aggregate.
        
        :param aggregate_route_entries: RouteListType object
        
        """
        if 'aggregate_route_entries' not in self._pending_field_updates:
            self._pending_field_updates.add('aggregate_route_entries')

        self._aggregate_route_entries = aggregate_route_entries
    #end aggregate_route_entries

    def set_aggregate_route_entries(self, value):
        self.aggregate_route_entries = value
    #end set_aggregate_route_entries

    @pycontrail.gen.resource_common.RouteAggregate.aggregate_route_nexthop.setter
    def aggregate_route_nexthop(self, aggregate_route_nexthop):
        """Set aggregate-route-nexthop for route-aggregate.
        
        :param aggregate_route_nexthop: xsd:string object
        
        """
        if 'aggregate_route_nexthop' not in self._pending_field_updates:
            self._pending_field_updates.add('aggregate_route_nexthop')

        self._aggregate_route_nexthop = aggregate_route_nexthop
    #end aggregate_route_nexthop

    def set_aggregate_route_nexthop(self, value):
        self.aggregate_route_nexthop = value
    #end set_aggregate_route_nexthop

    @pycontrail.gen.resource_common.RouteAggregate.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for route-aggregate.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.RouteAggregate.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for route-aggregate.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.RouteAggregate.display_name.setter
    def display_name(self, display_name):
        """Set display-name for route-aggregate.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for route-aggregate.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(RouteAggregate, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to route-aggregate.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(RouteAggregate, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(RouteAggregate, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for route-aggregate.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of ServiceInterfaceTag summary
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(RouteAggregate, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list

    def set_routing_instance(self, *args, **kwargs):
        """Set routing-instance for route-aggregate.
        
        :param ref_obj: RoutingInstance object
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(RouteAggregate, self).set_routing_instance(*args, **kwargs)

    #end set_routing_instance

    def add_routing_instance(self, *args, **kwargs):
        """Add routing-instance to route-aggregate.
        
        :param ref_obj: RoutingInstance object
        
        """
        if 'routing_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(RouteAggregate, self).add_routing_instance(*args, **kwargs)
    #end add_routing_instance

    def del_routing_instance(self, *args, **kwargs):
        if 'routing_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('routing_instance_refs')
            self._original_routing_instance_refs = (self.get_routing_instance_refs() or [])[:]
        super(RouteAggregate, self).del_routing_instance(*args, **kwargs)
    #end del_routing_instance

    def set_routing_instance_list(self, *args, **kwargs):
        """Set routing-instance list for route-aggregate.
        
        :param ref_obj_list: list of RoutingInstance object
        
        """
        self._pending_field_updates.add('routing_instance_refs')
        self._pending_ref_updates.discard('routing_instance_refs')
        super(RouteAggregate, self).set_routing_instance_list(*args, **kwargs)
    #end set_routing_instance_list


#end class RouteAggregate

class LogicalRouter(pycontrail.gen.resource_common.LogicalRouter):
    create_uri = ''
    resource_uri_base = {}
    def __init__(self, name = None, parent_obj = None, configured_route_target_list=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        pending_fields = ['fq_name', 'parent_type']

        self._server_conn = None

        if configured_route_target_list is not None:
            pending_fields.append('configured_route_target_list')
        if id_perms is not None:
            pending_fields.append('id_perms')
        if perms2 is not None:
            pending_fields.append('perms2')
        if display_name is not None:
            pending_fields.append('display_name')

        self._pending_field_updates = set(pending_fields)
        # dict of prop-list-fields with list of opers
        self._pending_field_list_updates = {}
        # dict of prop-map-fields with list of opers
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])

        super(LogicalRouter, self).__init__(name, parent_obj, configured_route_target_list, id_perms, perms2, display_name, *args, **kwargs)
    #end __init__

    def get_pending_updates(self):
        return self._pending_field_updates
    #end get_pending_updates

    def get_ref_updates(self):
        return self._pending_ref_updates
    #end get_ref_updates

    def clear_pending_updates(self):
        self._pending_field_updates = set([])
        self._pending_field_list_updates = {}
        self._pending_field_map_updates = {}
        self._pending_ref_updates = set([])
    #end clear_pending_updates

    def set_server_conn(self, vnc_api_handle):
        self._server_conn = vnc_api_handle
    #end set_server_conn

    @classmethod
    def from_dict(cls, **kwargs):
        props_dict = {}
        if 'configured_route_target_list' in kwargs:
            if kwargs['configured_route_target_list'] is None:
                props_dict['configured_route_target_list'] = None
            else:
                props_dict['configured_route_target_list'] = pycontrail.gen.resource_xsd.RouteTargetList(**kwargs['configured_route_target_list'])
        if 'id_perms' in kwargs:
            if kwargs['id_perms'] is None:
                props_dict['id_perms'] = None
            else:
                props_dict['id_perms'] = pycontrail.gen.resource_xsd.IdPermsType(**kwargs['id_perms'])
        if 'perms2' in kwargs:
            if kwargs['perms2'] is None:
                props_dict['perms2'] = None
            else:
                props_dict['perms2'] = pycontrail.gen.resource_xsd.PermType2(**kwargs['perms2'])
        if 'display_name' in kwargs:
            props_dict['display_name'] = kwargs['display_name']

        # obj constructor takes only props
        parent_type = kwargs.get('parent_type', None)
        fq_name = kwargs['fq_name']
        props_dict.update({'parent_type': parent_type, 'fq_name': fq_name})
        obj = LogicalRouter(fq_name[-1], **props_dict)
        obj.uuid = kwargs['uuid']
        if 'parent_uuid' in kwargs:
            obj.parent_uuid = kwargs['parent_uuid']

        # add summary of any children...

        # add any specified references...
        if 'virtual_machine_interface_refs' in kwargs:
            obj.virtual_machine_interface_refs = kwargs['virtual_machine_interface_refs']
        if 'route_target_refs' in kwargs:
            obj.route_target_refs = kwargs['route_target_refs']
        if 'virtual_network_refs' in kwargs:
            obj.virtual_network_refs = kwargs['virtual_network_refs']
        if 'service_instance_refs' in kwargs:
            obj.service_instance_refs = kwargs['service_instance_refs']

        # and back references but no obj api for it...

        return obj
    #end from_dict

    @pycontrail.gen.resource_common.LogicalRouter.uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
        if 'uuid' not in self._pending_field_updates:
            self._pending_field_updates.add('uuid')
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    @pycontrail.gen.resource_common.LogicalRouter.configured_route_target_list.setter
    def configured_route_target_list(self, configured_route_target_list):
        """Set configured-route-target-list for logical-router.
        
        :param configured_route_target_list: RouteTargetList object
        
        """
        if 'configured_route_target_list' not in self._pending_field_updates:
            self._pending_field_updates.add('configured_route_target_list')

        self._configured_route_target_list = configured_route_target_list
    #end configured_route_target_list

    def set_configured_route_target_list(self, value):
        self.configured_route_target_list = value
    #end set_configured_route_target_list

    @pycontrail.gen.resource_common.LogicalRouter.id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for logical-router.
        
        :param id_perms: IdPermsType object
        
        """
        if 'id_perms' not in self._pending_field_updates:
            self._pending_field_updates.add('id_perms')

        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    @pycontrail.gen.resource_common.LogicalRouter.perms2.setter
    def perms2(self, perms2):
        """Set perms2 for logical-router.
        
        :param perms2: PermType2 object
        
        """
        if 'perms2' not in self._pending_field_updates:
            self._pending_field_updates.add('perms2')

        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    @pycontrail.gen.resource_common.LogicalRouter.display_name.setter
    def display_name(self, display_name):
        """Set display-name for logical-router.
        
        :param display_name: xsd:string object
        
        """
        if 'display_name' not in self._pending_field_updates:
            self._pending_field_updates.add('display_name')

        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def set_virtual_machine_interface(self, *args, **kwargs):
        """Set virtual-machine-interface for logical-router.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(LogicalRouter, self).set_virtual_machine_interface(*args, **kwargs)

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, *args, **kwargs):
        """Add virtual-machine-interface to logical-router.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(LogicalRouter, self).add_virtual_machine_interface(*args, **kwargs)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, *args, **kwargs):
        if 'virtual_machine_interface_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_machine_interface_refs')
            self._original_virtual_machine_interface_refs = (self.get_virtual_machine_interface_refs() or [])[:]
        super(LogicalRouter, self).del_virtual_machine_interface(*args, **kwargs)
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, *args, **kwargs):
        """Set virtual-machine-interface list for logical-router.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self._pending_field_updates.add('virtual_machine_interface_refs')
        self._pending_ref_updates.discard('virtual_machine_interface_refs')
        super(LogicalRouter, self).set_virtual_machine_interface_list(*args, **kwargs)
    #end set_virtual_machine_interface_list

    def set_route_target(self, *args, **kwargs):
        """Set route-target for logical-router.
        
        :param ref_obj: RouteTarget object
        
        """
        self._pending_field_updates.add('route_target_refs')
        self._pending_ref_updates.discard('route_target_refs')
        super(LogicalRouter, self).set_route_target(*args, **kwargs)

    #end set_route_target

    def add_route_target(self, *args, **kwargs):
        """Add route-target to logical-router.
        
        :param ref_obj: RouteTarget object
        
        """
        if 'route_target_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('route_target_refs')
            self._original_route_target_refs = (self.get_route_target_refs() or [])[:]
        super(LogicalRouter, self).add_route_target(*args, **kwargs)
    #end add_route_target

    def del_route_target(self, *args, **kwargs):
        if 'route_target_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('route_target_refs')
            self._original_route_target_refs = (self.get_route_target_refs() or [])[:]
        super(LogicalRouter, self).del_route_target(*args, **kwargs)
    #end del_route_target

    def set_route_target_list(self, *args, **kwargs):
        """Set route-target list for logical-router.
        
        :param ref_obj_list: list of RouteTarget object
        
        """
        self._pending_field_updates.add('route_target_refs')
        self._pending_ref_updates.discard('route_target_refs')
        super(LogicalRouter, self).set_route_target_list(*args, **kwargs)
    #end set_route_target_list

    def set_virtual_network(self, *args, **kwargs):
        """Set virtual-network for logical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(LogicalRouter, self).set_virtual_network(*args, **kwargs)

    #end set_virtual_network

    def add_virtual_network(self, *args, **kwargs):
        """Add virtual-network to logical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        if 'virtual_network_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(LogicalRouter, self).add_virtual_network(*args, **kwargs)
    #end add_virtual_network

    def del_virtual_network(self, *args, **kwargs):
        if 'virtual_network_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('virtual_network_refs')
            self._original_virtual_network_refs = (self.get_virtual_network_refs() or [])[:]
        super(LogicalRouter, self).del_virtual_network(*args, **kwargs)
    #end del_virtual_network

    def set_virtual_network_list(self, *args, **kwargs):
        """Set virtual-network list for logical-router.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self._pending_field_updates.add('virtual_network_refs')
        self._pending_ref_updates.discard('virtual_network_refs')
        super(LogicalRouter, self).set_virtual_network_list(*args, **kwargs)
    #end set_virtual_network_list

    def set_service_instance(self, *args, **kwargs):
        """Set service-instance for logical-router.
        
        :param ref_obj: ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(LogicalRouter, self).set_service_instance(*args, **kwargs)

    #end set_service_instance

    def add_service_instance(self, *args, **kwargs):
        """Add service-instance to logical-router.
        
        :param ref_obj: ServiceInstance object
        
        """
        if 'service_instance_refs' not in self._pending_ref_updates|self._pending_field_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(LogicalRouter, self).add_service_instance(*args, **kwargs)
    #end add_service_instance

    def del_service_instance(self, *args, **kwargs):
        if 'service_instance_refs' not in self._pending_ref_updates:
            self._pending_ref_updates.add('service_instance_refs')
            self._original_service_instance_refs = (self.get_service_instance_refs() or [])[:]
        super(LogicalRouter, self).del_service_instance(*args, **kwargs)
    #end del_service_instance

    def set_service_instance_list(self, *args, **kwargs):
        """Set service-instance list for logical-router.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self._pending_field_updates.add('service_instance_refs')
        self._pending_ref_updates.discard('service_instance_refs')
        super(LogicalRouter, self).set_service_instance_list(*args, **kwargs)
    #end set_service_instance_list


#end class LogicalRouter

