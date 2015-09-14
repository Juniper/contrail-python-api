
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

"""
This module defines the classes for every configuration element managed by the system
"""

class Domain(object):
    """
    Represents domain configuration representation.

    Child of:
        :class:`.ConfigRoot` object OR

    Properties:
        * domain-limits (:class:`.DomainLimitsType` type)
        * api-access-list (:class:`.ApiAccessListType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.Project` objects
        * list of :class:`.Namespace` objects
        * list of :class:`.ServiceTemplate` objects
        * list of :class:`.VirtualDns` objects

    References to:

    Referred by:
    """

    prop_fields = set([u'domain_limits', u'api_access_list', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'config_root_back_refs'])
    children_fields = set([u'projects', u'namespaces', 'service_templates', u'virtual_DNSs'])

    def __init__(self, name = None, parent_obj = None, domain_limits = None, api_access_list = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'domain'
        if not name:
            name = u'default-domain'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.fq_name = [name]

        # property fields
        if domain_limits:
            self._domain_limits = domain_limits
        if api_access_list:
            self._api_access_list = api_access_list
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (domain)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of domain in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of domain as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of domain's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of domain's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def domain_limits(self):
        """Get domain-limits for domain.
        
        :returns: DomainLimitsType object
        
        """
        return getattr(self, '_domain_limits', None)
    #end domain_limits

    @domain_limits.setter
    def domain_limits(self, domain_limits):
        """Set domain-limits for domain.
        
        :param domain_limits: DomainLimitsType object
        
        """
        self._domain_limits = domain_limits
    #end domain_limits

    def set_domain_limits(self, value):
        self.domain_limits = value
    #end set_domain_limits

    def get_domain_limits(self):
        return self.domain_limits
    #end get_domain_limits

    @property
    def api_access_list(self):
        """Get api-access-list for domain.
        
        :returns: ApiAccessListType object
        
        """
        return getattr(self, '_api_access_list', None)
    #end api_access_list

    @api_access_list.setter
    def api_access_list(self, api_access_list):
        """Set api-access-list for domain.
        
        :param api_access_list: ApiAccessListType object
        
        """
        self._api_access_list = api_access_list
    #end api_access_list

    def set_api_access_list(self, value):
        self.api_access_list = value
    #end set_api_access_list

    def get_api_access_list(self):
        return self.api_access_list
    #end get_api_access_list

    @property
    def id_perms(self):
        """Get id-perms for domain.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for domain.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for domain.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for domain.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_domain_limits'):
            self._serialize_field_to_json(serialized, field_names, 'domain_limits')
        if hasattr(self, '_api_access_list'):
            self._serialize_field_to_json(serialized, field_names, 'api_access_list')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_projects(self):
        return getattr(self, 'projects', None)
    #end get_projects

    def get_namespaces(self):
        return getattr(self, 'namespaces', None)
    #end get_namespaces

    def get_service_templates(self):
        return getattr(self, 'service_templates', None)
    #end get_service_templates

    def get_virtual_DNSs(self):
        return getattr(self, 'virtual_DNSs', None)
    #end get_virtual_DNSs

    def get_config_root_back_refs(self):
        """Return list of all config-roots using this domain"""
        return getattr(self, 'config_root_back_refs', None)
    #end get_config_root_back_refs

    def dump(self):
        """Display domain object in compact form."""
        print '------------ domain ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P domain_limits = ', self.get_domain_limits()
        print 'P api_access_list = ', self.get_api_access_list()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS project = ', self.get_projects()
        print 'HAS namespace = ', self.get_namespaces()
        print 'HAS service_template = ', self.get_service_templates()
        print 'HAS virtual_DNS = ', self.get_virtual_DNSs()
    #end dump

#end class Domain

class GlobalVrouterConfig(object):
    """
    Represents global-vrouter-config configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * linklocal-services (:class:`.LinklocalServicesTypes` type)
        * encapsulation-priorities (:class:`.EncapsulationPrioritiesType` type)
        * vxlan-network-identifier-mode (VxlanNetworkIdentifierModeType type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'linklocal_services', u'encapsulation_priorities', u'vxlan_network_identifier_mode', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'global_system_config_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, linklocal_services = None, encapsulation_priorities = None, vxlan_network_identifier_mode = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'global-vrouter-config'
        if not name:
            name = u'default-global-vrouter-config'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'global-system-config'
            self.fq_name = [u'default-global-system-config']
            self.fq_name.append(name)


        # property fields
        if linklocal_services:
            self._linklocal_services = linklocal_services
        if encapsulation_priorities:
            self._encapsulation_priorities = encapsulation_priorities
        if vxlan_network_identifier_mode:
            self._vxlan_network_identifier_mode = vxlan_network_identifier_mode
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (global-vrouter-config)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of global-vrouter-config in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of global-vrouter-config as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of global-vrouter-config's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of global-vrouter-config's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def linklocal_services(self):
        """Get linklocal-services for global-vrouter-config.
        
        :returns: LinklocalServicesTypes object
        
        """
        return getattr(self, '_linklocal_services', None)
    #end linklocal_services

    @linklocal_services.setter
    def linklocal_services(self, linklocal_services):
        """Set linklocal-services for global-vrouter-config.
        
        :param linklocal_services: LinklocalServicesTypes object
        
        """
        self._linklocal_services = linklocal_services
    #end linklocal_services

    def set_linklocal_services(self, value):
        self.linklocal_services = value
    #end set_linklocal_services

    def get_linklocal_services(self):
        return self.linklocal_services
    #end get_linklocal_services

    @property
    def encapsulation_priorities(self):
        """Get encapsulation-priorities for global-vrouter-config.
        
        :returns: EncapsulationPrioritiesType object
        
        """
        return getattr(self, '_encapsulation_priorities', None)
    #end encapsulation_priorities

    @encapsulation_priorities.setter
    def encapsulation_priorities(self, encapsulation_priorities):
        """Set encapsulation-priorities for global-vrouter-config.
        
        :param encapsulation_priorities: EncapsulationPrioritiesType object
        
        """
        self._encapsulation_priorities = encapsulation_priorities
    #end encapsulation_priorities

    def set_encapsulation_priorities(self, value):
        self.encapsulation_priorities = value
    #end set_encapsulation_priorities

    def get_encapsulation_priorities(self):
        return self.encapsulation_priorities
    #end get_encapsulation_priorities

    @property
    def vxlan_network_identifier_mode(self):
        """Get vxlan-network-identifier-mode for global-vrouter-config.
        
        :returns: VxlanNetworkIdentifierModeType object
        
        """
        return getattr(self, '_vxlan_network_identifier_mode', None)
    #end vxlan_network_identifier_mode

    @vxlan_network_identifier_mode.setter
    def vxlan_network_identifier_mode(self, vxlan_network_identifier_mode):
        """Set vxlan-network-identifier-mode for global-vrouter-config.
        
        :param vxlan_network_identifier_mode: VxlanNetworkIdentifierModeType object
        
        """
        self._vxlan_network_identifier_mode = vxlan_network_identifier_mode
    #end vxlan_network_identifier_mode

    def set_vxlan_network_identifier_mode(self, value):
        self.vxlan_network_identifier_mode = value
    #end set_vxlan_network_identifier_mode

    def get_vxlan_network_identifier_mode(self):
        return self.vxlan_network_identifier_mode
    #end get_vxlan_network_identifier_mode

    @property
    def id_perms(self):
        """Get id-perms for global-vrouter-config.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for global-vrouter-config.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for global-vrouter-config.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for global-vrouter-config.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_linklocal_services'):
            self._serialize_field_to_json(serialized, field_names, 'linklocal_services')
        if hasattr(self, '_encapsulation_priorities'):
            self._serialize_field_to_json(serialized, field_names, 'encapsulation_priorities')
        if hasattr(self, '_vxlan_network_identifier_mode'):
            self._serialize_field_to_json(serialized, field_names, 'vxlan_network_identifier_mode')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this global-vrouter-config"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def dump(self):
        """Display global-vrouter-config object in compact form."""
        print '------------ global-vrouter-config ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P linklocal_services = ', self.get_linklocal_services()
        print 'P encapsulation_priorities = ', self.get_encapsulation_priorities()
        print 'P vxlan_network_identifier_mode = ', self.get_vxlan_network_identifier_mode()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class GlobalVrouterConfig

class InstanceIp(object):
    """
    Represents instance-ip configuration representation.

    Properties:
        * instance-ip-address (IpAddressType type)
        * instance-ip-family (IpAddressFamilyType type)
        * instance-ip-mode (AddressMode type)
        * subnet-uuid (xsd:string type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.VirtualNetwork` objects
        * list of :class:`.VirtualMachineInterface` objects

    Referred by:
    """

    prop_fields = set([u'instance_ip_address', u'instance_ip_family', u'instance_ip_mode', u'subnet_uuid', u'id_perms', u'display_name'])
    ref_fields = set([u'virtual_network_refs', 'virtual_machine_interface_refs'])
    backref_fields = set([])
    children_fields = set([])

    def __init__(self, name = None, instance_ip_address = None, instance_ip_family = None, instance_ip_mode = None, subnet_uuid = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'instance-ip'
        if not name:
            name = u'default-instance-ip'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if instance_ip_address:
            self._instance_ip_address = instance_ip_address
        if instance_ip_family:
            self._instance_ip_family = instance_ip_family
        if instance_ip_mode:
            self._instance_ip_mode = instance_ip_mode
        if subnet_uuid:
            self._subnet_uuid = subnet_uuid
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (instance-ip)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of instance-ip in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of instance-ip as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def instance_ip_address(self):
        """Get instance-ip-address for instance-ip.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_instance_ip_address', None)
    #end instance_ip_address

    @instance_ip_address.setter
    def instance_ip_address(self, instance_ip_address):
        """Set instance-ip-address for instance-ip.
        
        :param instance_ip_address: IpAddressType object
        
        """
        self._instance_ip_address = instance_ip_address
    #end instance_ip_address

    def set_instance_ip_address(self, value):
        self.instance_ip_address = value
    #end set_instance_ip_address

    def get_instance_ip_address(self):
        return self.instance_ip_address
    #end get_instance_ip_address

    @property
    def instance_ip_family(self):
        """Get instance-ip-family for instance-ip.
        
        :returns: IpAddressFamilyType object
        
        """
        return getattr(self, '_instance_ip_family', None)
    #end instance_ip_family

    @instance_ip_family.setter
    def instance_ip_family(self, instance_ip_family):
        """Set instance-ip-family for instance-ip.
        
        :param instance_ip_family: IpAddressFamilyType object
        
        """
        self._instance_ip_family = instance_ip_family
    #end instance_ip_family

    def set_instance_ip_family(self, value):
        self.instance_ip_family = value
    #end set_instance_ip_family

    def get_instance_ip_family(self):
        return self.instance_ip_family
    #end get_instance_ip_family

    @property
    def instance_ip_mode(self):
        """Get instance-ip-mode for instance-ip.
        
        :returns: AddressMode object
        
        """
        return getattr(self, '_instance_ip_mode', None)
    #end instance_ip_mode

    @instance_ip_mode.setter
    def instance_ip_mode(self, instance_ip_mode):
        """Set instance-ip-mode for instance-ip.
        
        :param instance_ip_mode: AddressMode object
        
        """
        self._instance_ip_mode = instance_ip_mode
    #end instance_ip_mode

    def set_instance_ip_mode(self, value):
        self.instance_ip_mode = value
    #end set_instance_ip_mode

    def get_instance_ip_mode(self):
        return self.instance_ip_mode
    #end get_instance_ip_mode

    @property
    def subnet_uuid(self):
        """Get subnet-uuid for instance-ip.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_subnet_uuid', None)
    #end subnet_uuid

    @subnet_uuid.setter
    def subnet_uuid(self, subnet_uuid):
        """Set subnet-uuid for instance-ip.
        
        :param subnet_uuid: xsd:string object
        
        """
        self._subnet_uuid = subnet_uuid
    #end subnet_uuid

    def set_subnet_uuid(self, value):
        self.subnet_uuid = value
    #end set_subnet_uuid

    def get_subnet_uuid(self):
        return self.subnet_uuid
    #end get_subnet_uuid

    @property
    def id_perms(self):
        """Get id-perms for instance-ip.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for instance-ip.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for instance-ip.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for instance-ip.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_instance_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'instance_ip_address')
        if hasattr(self, '_instance_ip_family'):
            self._serialize_field_to_json(serialized, field_names, 'instance_ip_family')
        if hasattr(self, '_instance_ip_mode'):
            self._serialize_field_to_json(serialized, field_names, 'instance_ip_mode')
        if hasattr(self, '_subnet_uuid'):
            self._serialize_field_to_json(serialized, field_names, 'subnet_uuid')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_network_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_network(self, ref_obj):
        """Set virtual-network for instance-ip.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self.virtual_network_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_network_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_network

    def add_virtual_network(self, ref_obj):
        """Add virtual-network to instance-ip.
        
        :param ref_obj: VirtualNetwork object
        
        """
        refs = getattr(self, 'virtual_network_refs', [])
        if not refs:
            self.virtual_network_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_network_refs.append(ref_info)
    #end add_virtual_network

    def del_virtual_network(self, ref_obj):
        refs = self.get_virtual_network_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_network_refs.remove(ref)
                return
    #end del_virtual_network

    def set_virtual_network_list(self, ref_obj_list):
        """Set virtual-network list for instance-ip.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self.virtual_network_refs = ref_obj_list
    #end set_virtual_network_list

    def get_virtual_network_refs(self):
        """Return virtual-network list for instance-ip.
        
        :returns: list of <VirtualNetwork>
        
        """
        return getattr(self, 'virtual_network_refs', None)
    #end get_virtual_network_refs

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for instance-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to instance-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for instance-ip.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for instance-ip.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def dump(self):
        """Display instance-ip object in compact form."""
        print '------------ instance-ip ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P instance_ip_address = ', self.get_instance_ip_address()
        print 'P instance_ip_family = ', self.get_instance_ip_family()
        print 'P instance_ip_mode = ', self.get_instance_ip_mode()
        print 'P subnet_uuid = ', self.get_subnet_uuid()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
    #end dump

#end class InstanceIp

class NetworkPolicy(object):
    """
    Represents network-policy configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * network-policy-entries (:class:`.PolicyEntriesType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.VirtualNetwork` objects
    """

    prop_fields = set([u'network_policy_entries', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs', u'virtual_network_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, network_policy_entries = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'network-policy'
        if not name:
            name = u'default-network-policy'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if network_policy_entries:
            self._network_policy_entries = network_policy_entries
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (network-policy)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of network-policy in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of network-policy as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of network-policy's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of network-policy's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def network_policy_entries(self):
        """Get network-policy-entries for network-policy.
        
        :returns: PolicyEntriesType object
        
        """
        return getattr(self, '_network_policy_entries', None)
    #end network_policy_entries

    @network_policy_entries.setter
    def network_policy_entries(self, network_policy_entries):
        """Set network-policy-entries for network-policy.
        
        :param network_policy_entries: PolicyEntriesType object
        
        """
        self._network_policy_entries = network_policy_entries
    #end network_policy_entries

    def set_network_policy_entries(self, value):
        self.network_policy_entries = value
    #end set_network_policy_entries

    def get_network_policy_entries(self):
        return self.network_policy_entries
    #end get_network_policy_entries

    @property
    def id_perms(self):
        """Get id-perms for network-policy.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for network-policy.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for network-policy.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for network-policy.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_network_policy_entries'):
            self._serialize_field_to_json(serialized, field_names, 'network_policy_entries')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_project_back_refs(self):
        """Return list of all projects using this network-policy"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this network-policy"""
        return getattr(self, 'virtual_network_back_refs', None)
    #end get_virtual_network_back_refs

    def dump(self):
        """Display network-policy object in compact form."""
        print '------------ network-policy ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P network_policy_entries = ', self.get_network_policy_entries()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK virtual_network = ', self.get_virtual_network_back_refs()
    #end dump

#end class NetworkPolicy

class LoadbalancerPool(object):
    """
    Represents loadbalancer-pool configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * loadbalancer-pool-properties (:class:`.LoadbalancerPoolType` type)
        * loadbalancer-pool-provider (xsd:string type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.LoadbalancerMember` objects

    References to:
        * list of :class:`.ServiceInstance` objects
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.ServiceApplianceSet` objects
        * list of :class:`.LoadbalancerHealthmonitor` objects

    Referred by:
        * list of :class:`.VirtualIp` objects
    """

    prop_fields = set([u'loadbalancer_pool_properties', u'loadbalancer_pool_provider', u'id_perms', u'display_name'])
    ref_fields = set([u'service_instance_refs', 'virtual_machine_interface_refs', u'service_appliance_set_refs', u'loadbalancer_healthmonitor_refs'])
    backref_fields = set([u'project_back_refs', u'virtual_ip_back_refs'])
    children_fields = set([u'loadbalancer_members'])

    def __init__(self, name = None, parent_obj = None, loadbalancer_pool_properties = None, loadbalancer_pool_provider = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'loadbalancer-pool'
        if not name:
            name = u'default-loadbalancer-pool'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if loadbalancer_pool_properties:
            self._loadbalancer_pool_properties = loadbalancer_pool_properties
        if loadbalancer_pool_provider:
            self._loadbalancer_pool_provider = loadbalancer_pool_provider
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (loadbalancer-pool)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of loadbalancer-pool in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of loadbalancer-pool as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of loadbalancer-pool's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of loadbalancer-pool's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def loadbalancer_pool_properties(self):
        """Get loadbalancer-pool-properties for loadbalancer-pool.
        
        :returns: LoadbalancerPoolType object
        
        """
        return getattr(self, '_loadbalancer_pool_properties', None)
    #end loadbalancer_pool_properties

    @loadbalancer_pool_properties.setter
    def loadbalancer_pool_properties(self, loadbalancer_pool_properties):
        """Set loadbalancer-pool-properties for loadbalancer-pool.
        
        :param loadbalancer_pool_properties: LoadbalancerPoolType object
        
        """
        self._loadbalancer_pool_properties = loadbalancer_pool_properties
    #end loadbalancer_pool_properties

    def set_loadbalancer_pool_properties(self, value):
        self.loadbalancer_pool_properties = value
    #end set_loadbalancer_pool_properties

    def get_loadbalancer_pool_properties(self):
        return self.loadbalancer_pool_properties
    #end get_loadbalancer_pool_properties

    @property
    def loadbalancer_pool_provider(self):
        """Get loadbalancer-pool-provider for loadbalancer-pool.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_loadbalancer_pool_provider', None)
    #end loadbalancer_pool_provider

    @loadbalancer_pool_provider.setter
    def loadbalancer_pool_provider(self, loadbalancer_pool_provider):
        """Set loadbalancer-pool-provider for loadbalancer-pool.
        
        :param loadbalancer_pool_provider: xsd:string object
        
        """
        self._loadbalancer_pool_provider = loadbalancer_pool_provider
    #end loadbalancer_pool_provider

    def set_loadbalancer_pool_provider(self, value):
        self.loadbalancer_pool_provider = value
    #end set_loadbalancer_pool_provider

    def get_loadbalancer_pool_provider(self):
        return self.loadbalancer_pool_provider
    #end get_loadbalancer_pool_provider

    @property
    def id_perms(self):
        """Get id-perms for loadbalancer-pool.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-pool.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for loadbalancer-pool.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-pool.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_loadbalancer_pool_properties'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_pool_properties')
        if hasattr(self, '_loadbalancer_pool_provider'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_pool_provider')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        if hasattr(self, 'service_appliance_set_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_set_refs')
        if hasattr(self, 'loadbalancer_healthmonitor_refs'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_healthmonitor_refs')
        return serialized
    #end serialize_to_json

    def get_loadbalancer_members(self):
        return getattr(self, 'loadbalancer_members', None)
    #end get_loadbalancer_members

    def set_service_instance(self, ref_obj):
        """Set service-instance for loadbalancer-pool.
        
        :param ref_obj: ServiceInstance object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj):
        """Add service-instance to loadbalancer-pool.
        
        :param ref_obj: ServiceInstance object
        
        """
        refs = getattr(self, 'service_instance_refs', [])
        if not refs:
            self.service_instance_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.service_instance_refs.append(ref_info)
    #end add_service_instance

    def del_service_instance(self, ref_obj):
        refs = self.get_service_instance_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.service_instance_refs.remove(ref)
                return
    #end del_service_instance

    def set_service_instance_list(self, ref_obj_list):
        """Set service-instance list for loadbalancer-pool.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self.service_instance_refs = ref_obj_list
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for loadbalancer-pool.
        
        :returns: list of <ServiceInstance>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for loadbalancer-pool.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to loadbalancer-pool.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for loadbalancer-pool.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for loadbalancer-pool.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def set_service_appliance_set(self, ref_obj):
        """Set service-appliance-set for loadbalancer-pool.
        
        :param ref_obj: ServiceApplianceSet object
        
        """
        self.service_appliance_set_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_appliance_set_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_appliance_set

    def add_service_appliance_set(self, ref_obj):
        """Add service-appliance-set to loadbalancer-pool.
        
        :param ref_obj: ServiceApplianceSet object
        
        """
        refs = getattr(self, 'service_appliance_set_refs', [])
        if not refs:
            self.service_appliance_set_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.service_appliance_set_refs.append(ref_info)
    #end add_service_appliance_set

    def del_service_appliance_set(self, ref_obj):
        refs = self.get_service_appliance_set_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.service_appliance_set_refs.remove(ref)
                return
    #end del_service_appliance_set

    def set_service_appliance_set_list(self, ref_obj_list):
        """Set service-appliance-set list for loadbalancer-pool.
        
        :param ref_obj_list: list of ServiceApplianceSet object
        
        """
        self.service_appliance_set_refs = ref_obj_list
    #end set_service_appliance_set_list

    def get_service_appliance_set_refs(self):
        """Return service-appliance-set list for loadbalancer-pool.
        
        :returns: list of <ServiceApplianceSet>
        
        """
        return getattr(self, 'service_appliance_set_refs', None)
    #end get_service_appliance_set_refs

    def set_loadbalancer_healthmonitor(self, ref_obj):
        """Set loadbalancer-healthmonitor for loadbalancer-pool.
        
        :param ref_obj: LoadbalancerHealthmonitor object
        
        """
        self.loadbalancer_healthmonitor_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.loadbalancer_healthmonitor_refs[0]['uuid'] = ref_obj.uuid

    #end set_loadbalancer_healthmonitor

    def add_loadbalancer_healthmonitor(self, ref_obj):
        """Add loadbalancer-healthmonitor to loadbalancer-pool.
        
        :param ref_obj: LoadbalancerHealthmonitor object
        
        """
        refs = getattr(self, 'loadbalancer_healthmonitor_refs', [])
        if not refs:
            self.loadbalancer_healthmonitor_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.loadbalancer_healthmonitor_refs.append(ref_info)
    #end add_loadbalancer_healthmonitor

    def del_loadbalancer_healthmonitor(self, ref_obj):
        refs = self.get_loadbalancer_healthmonitor_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.loadbalancer_healthmonitor_refs.remove(ref)
                return
    #end del_loadbalancer_healthmonitor

    def set_loadbalancer_healthmonitor_list(self, ref_obj_list):
        """Set loadbalancer-healthmonitor list for loadbalancer-pool.
        
        :param ref_obj_list: list of LoadbalancerHealthmonitor object
        
        """
        self.loadbalancer_healthmonitor_refs = ref_obj_list
    #end set_loadbalancer_healthmonitor_list

    def get_loadbalancer_healthmonitor_refs(self):
        """Return loadbalancer-healthmonitor list for loadbalancer-pool.
        
        :returns: list of <LoadbalancerHealthmonitor>
        
        """
        return getattr(self, 'loadbalancer_healthmonitor_refs', None)
    #end get_loadbalancer_healthmonitor_refs

    def get_project_back_refs(self):
        """Return list of all projects using this loadbalancer-pool"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_ip_back_refs(self):
        """Return list of all virtual-ips using this loadbalancer-pool"""
        return getattr(self, 'virtual_ip_back_refs', None)
    #end get_virtual_ip_back_refs

    def dump(self):
        """Display loadbalancer-pool object in compact form."""
        print '------------ loadbalancer-pool ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P loadbalancer_pool_properties = ', self.get_loadbalancer_pool_properties()
        print 'P loadbalancer_pool_provider = ', self.get_loadbalancer_pool_provider()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF service_appliance_set = ', self.get_service_appliance_set_refs()
        print 'HAS loadbalancer_member = ', self.get_loadbalancer_members()
        print 'REF loadbalancer_healthmonitor = ', self.get_loadbalancer_healthmonitor_refs()
        print 'BCK virtual_ip = ', self.get_virtual_ip_back_refs()
    #end dump

#end class LoadbalancerPool

class VirtualDnsRecord(object):
    """
    Represents virtual-DNS-record configuration representation.

    Child of:
        :class:`.VirtualDns` object OR

    Properties:
        * virtual-DNS-record-data (:class:`.VirtualDnsRecordType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'virtual_DNS_record_data', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'virtual_DNS_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, virtual_DNS_record_data = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-DNS-record'
        if not name:
            name = u'default-virtual-DNS-record'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'virtual-DNS'
            self.fq_name = [u'default-domain', u'default-virtual-DNS']
            self.fq_name.append(name)


        # property fields
        if virtual_DNS_record_data:
            self._virtual_DNS_record_data = virtual_DNS_record_data
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (virtual-DNS-record)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of virtual-DNS-record in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of virtual-DNS-record as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of virtual-DNS-record's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of virtual-DNS-record's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def virtual_DNS_record_data(self):
        """Get virtual-DNS-record-data for virtual-DNS-record.
        
        :returns: VirtualDnsRecordType object
        
        """
        return getattr(self, '_virtual_DNS_record_data', None)
    #end virtual_DNS_record_data

    @virtual_DNS_record_data.setter
    def virtual_DNS_record_data(self, virtual_DNS_record_data):
        """Set virtual-DNS-record-data for virtual-DNS-record.
        
        :param virtual_DNS_record_data: VirtualDnsRecordType object
        
        """
        self._virtual_DNS_record_data = virtual_DNS_record_data
    #end virtual_DNS_record_data

    def set_virtual_DNS_record_data(self, value):
        self.virtual_DNS_record_data = value
    #end set_virtual_DNS_record_data

    def get_virtual_DNS_record_data(self):
        return self.virtual_DNS_record_data
    #end get_virtual_DNS_record_data

    @property
    def id_perms(self):
        """Get id-perms for virtual-DNS-record.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-DNS-record.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for virtual-DNS-record.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-DNS-record.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_virtual_DNS_record_data'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_DNS_record_data')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_virtual_DNS_back_refs(self):
        """Return list of all virtual-DNSs using this virtual-DNS-record"""
        return getattr(self, 'virtual_DNS_back_refs', None)
    #end get_virtual_DNS_back_refs

    def dump(self):
        """Display virtual-DNS-record object in compact form."""
        print '------------ virtual-DNS-record ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_DNS_record_data = ', self.get_virtual_DNS_record_data()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class VirtualDnsRecord

class RouteTarget(object):
    """
    Represents route-target configuration representation.

    Properties:
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.LogicalRouter` objects
        * list of :class:`.RoutingInstance` objects
    """

    prop_fields = set([u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'logical_router_back_refs', 'routing_instance_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'route-target'
        if not name:
            name = u'default-route-target'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (route-target)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of route-target in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of route-target as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def id_perms(self):
        """Get id-perms for route-target.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for route-target.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for route-target.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for route-target.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this route-target"""
        return getattr(self, 'logical_router_back_refs', None)
    #end get_logical_router_back_refs

    def get_routing_instance_back_refs(self):
        """Return list of all routing-instances using this route-target"""
        return getattr(self, 'routing_instance_back_refs', None)
    #end get_routing_instance_back_refs

    def dump(self):
        """Display route-target object in compact form."""
        print '------------ route-target ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK logical_router = ', self.get_logical_router_back_refs()
        print 'BCK routing_instance = ', self.get_routing_instance_back_refs()
    #end dump

#end class RouteTarget

class FloatingIp(object):
    """
    Represents floating-ip configuration representation.

    Child of:
        :class:`.FloatingIpPool` object OR

    Properties:
        * floating-ip-address (IpAddressType type)
        * floating-ip-is-virtual-ip (xsd:boolean type)
        * floating-ip-fixed-ip-address (IpAddressType type)
        * floating-ip-address-family (IpAddressFamilyType type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.Project` objects
        * list of :class:`.VirtualMachineInterface` objects

    Referred by:
        * list of :class:`.CustomerAttachment` objects
    """

    prop_fields = set([u'floating_ip_address', u'floating_ip_is_virtual_ip', u'floating_ip_fixed_ip_address', u'floating_ip_address_family', u'id_perms', u'display_name'])
    ref_fields = set([u'project_refs', 'virtual_machine_interface_refs'])
    backref_fields = set([u'floating_ip_pool_back_refs', 'customer_attachment_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, floating_ip_address = None, floating_ip_is_virtual_ip = None, floating_ip_fixed_ip_address = None, floating_ip_address_family = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'floating-ip'
        if not name:
            name = u'default-floating-ip'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'floating-ip-pool'
            self.fq_name = [u'default-domain', u'default-project', u'default-virtual-network', u'default-floating-ip-pool']
            self.fq_name.append(name)


        # property fields
        if floating_ip_address:
            self._floating_ip_address = floating_ip_address
        if floating_ip_is_virtual_ip:
            self._floating_ip_is_virtual_ip = floating_ip_is_virtual_ip
        if floating_ip_fixed_ip_address:
            self._floating_ip_fixed_ip_address = floating_ip_fixed_ip_address
        if floating_ip_address_family:
            self._floating_ip_address_family = floating_ip_address_family
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (floating-ip)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of floating-ip in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of floating-ip as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of floating-ip's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of floating-ip's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def floating_ip_address(self):
        """Get floating-ip-address for floating-ip.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_floating_ip_address', None)
    #end floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Set floating-ip-address for floating-ip.
        
        :param floating_ip_address: IpAddressType object
        
        """
        self._floating_ip_address = floating_ip_address
    #end floating_ip_address

    def set_floating_ip_address(self, value):
        self.floating_ip_address = value
    #end set_floating_ip_address

    def get_floating_ip_address(self):
        return self.floating_ip_address
    #end get_floating_ip_address

    @property
    def floating_ip_is_virtual_ip(self):
        """Get floating-ip-is-virtual-ip for floating-ip.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_floating_ip_is_virtual_ip', None)
    #end floating_ip_is_virtual_ip

    @floating_ip_is_virtual_ip.setter
    def floating_ip_is_virtual_ip(self, floating_ip_is_virtual_ip):
        """Set floating-ip-is-virtual-ip for floating-ip.
        
        :param floating_ip_is_virtual_ip: xsd:boolean object
        
        """
        self._floating_ip_is_virtual_ip = floating_ip_is_virtual_ip
    #end floating_ip_is_virtual_ip

    def set_floating_ip_is_virtual_ip(self, value):
        self.floating_ip_is_virtual_ip = value
    #end set_floating_ip_is_virtual_ip

    def get_floating_ip_is_virtual_ip(self):
        return self.floating_ip_is_virtual_ip
    #end get_floating_ip_is_virtual_ip

    @property
    def floating_ip_fixed_ip_address(self):
        """Get floating-ip-fixed-ip-address for floating-ip.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_floating_ip_fixed_ip_address', None)
    #end floating_ip_fixed_ip_address

    @floating_ip_fixed_ip_address.setter
    def floating_ip_fixed_ip_address(self, floating_ip_fixed_ip_address):
        """Set floating-ip-fixed-ip-address for floating-ip.
        
        :param floating_ip_fixed_ip_address: IpAddressType object
        
        """
        self._floating_ip_fixed_ip_address = floating_ip_fixed_ip_address
    #end floating_ip_fixed_ip_address

    def set_floating_ip_fixed_ip_address(self, value):
        self.floating_ip_fixed_ip_address = value
    #end set_floating_ip_fixed_ip_address

    def get_floating_ip_fixed_ip_address(self):
        return self.floating_ip_fixed_ip_address
    #end get_floating_ip_fixed_ip_address

    @property
    def floating_ip_address_family(self):
        """Get floating-ip-address-family for floating-ip.
        
        :returns: IpAddressFamilyType object
        
        """
        return getattr(self, '_floating_ip_address_family', None)
    #end floating_ip_address_family

    @floating_ip_address_family.setter
    def floating_ip_address_family(self, floating_ip_address_family):
        """Set floating-ip-address-family for floating-ip.
        
        :param floating_ip_address_family: IpAddressFamilyType object
        
        """
        self._floating_ip_address_family = floating_ip_address_family
    #end floating_ip_address_family

    def set_floating_ip_address_family(self, value):
        self.floating_ip_address_family = value
    #end set_floating_ip_address_family

    def get_floating_ip_address_family(self):
        return self.floating_ip_address_family
    #end get_floating_ip_address_family

    @property
    def id_perms(self):
        """Get id-perms for floating-ip.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for floating-ip.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for floating-ip.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for floating-ip.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_floating_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'floating_ip_address')
        if hasattr(self, '_floating_ip_is_virtual_ip'):
            self._serialize_field_to_json(serialized, field_names, 'floating_ip_is_virtual_ip')
        if hasattr(self, '_floating_ip_fixed_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'floating_ip_fixed_ip_address')
        if hasattr(self, '_floating_ip_address_family'):
            self._serialize_field_to_json(serialized, field_names, 'floating_ip_address_family')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'project_refs'):
            self._serialize_field_to_json(serialized, field_names, 'project_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        return serialized
    #end serialize_to_json

    def set_project(self, ref_obj):
        """Set project for floating-ip.
        
        :param ref_obj: Project object
        
        """
        self.project_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.project_refs[0]['uuid'] = ref_obj.uuid

    #end set_project

    def add_project(self, ref_obj):
        """Add project to floating-ip.
        
        :param ref_obj: Project object
        
        """
        refs = getattr(self, 'project_refs', [])
        if not refs:
            self.project_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.project_refs.append(ref_info)
    #end add_project

    def del_project(self, ref_obj):
        refs = self.get_project_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.project_refs.remove(ref)
                return
    #end del_project

    def set_project_list(self, ref_obj_list):
        """Set project list for floating-ip.
        
        :param ref_obj_list: list of Project object
        
        """
        self.project_refs = ref_obj_list
    #end set_project_list

    def get_project_refs(self):
        """Return project list for floating-ip.
        
        :returns: list of <Project>
        
        """
        return getattr(self, 'project_refs', None)
    #end get_project_refs

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for floating-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to floating-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for floating-ip.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for floating-ip.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def get_floating_ip_pool_back_refs(self):
        """Return list of all floating-ip-pools using this floating-ip"""
        return getattr(self, 'floating_ip_pool_back_refs', None)
    #end get_floating_ip_pool_back_refs

    def get_customer_attachment_back_refs(self):
        """Return list of all customer-attachments using this floating-ip"""
        return getattr(self, 'customer_attachment_back_refs', None)
    #end get_customer_attachment_back_refs

    def dump(self):
        """Display floating-ip object in compact form."""
        print '------------ floating-ip ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P floating_ip_address = ', self.get_floating_ip_address()
        print 'P floating_ip_is_virtual_ip = ', self.get_floating_ip_is_virtual_ip()
        print 'P floating_ip_fixed_ip_address = ', self.get_floating_ip_fixed_ip_address()
        print 'P floating_ip_address_family = ', self.get_floating_ip_address_family()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF project = ', self.get_project_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'BCK customer_attachment = ', self.get_customer_attachment_back_refs()
    #end dump

#end class FloatingIp

class FloatingIpPool(object):
    """
    Represents floating-ip-pool configuration representation.

    Child of:
        :class:`.VirtualNetwork` object OR

    Properties:
        * floating-ip-pool-prefixes (:class:`.FloatingIpPoolType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.FloatingIp` objects

    References to:

    Referred by:
        * list of :class:`.Project` objects
    """

    prop_fields = set([u'floating_ip_pool_prefixes', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'virtual_network_back_refs', u'project_back_refs'])
    children_fields = set([u'floating_ips'])

    def __init__(self, name = None, parent_obj = None, floating_ip_pool_prefixes = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'floating-ip-pool'
        if not name:
            name = u'default-floating-ip-pool'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'virtual-network'
            self.fq_name = [u'default-domain', u'default-project', u'default-virtual-network']
            self.fq_name.append(name)


        # property fields
        if floating_ip_pool_prefixes:
            self._floating_ip_pool_prefixes = floating_ip_pool_prefixes
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (floating-ip-pool)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of floating-ip-pool in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of floating-ip-pool as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of floating-ip-pool's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of floating-ip-pool's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def floating_ip_pool_prefixes(self):
        """Get floating-ip-pool-prefixes for floating-ip-pool.
        
        :returns: FloatingIpPoolType object
        
        """
        return getattr(self, '_floating_ip_pool_prefixes', None)
    #end floating_ip_pool_prefixes

    @floating_ip_pool_prefixes.setter
    def floating_ip_pool_prefixes(self, floating_ip_pool_prefixes):
        """Set floating-ip-pool-prefixes for floating-ip-pool.
        
        :param floating_ip_pool_prefixes: FloatingIpPoolType object
        
        """
        self._floating_ip_pool_prefixes = floating_ip_pool_prefixes
    #end floating_ip_pool_prefixes

    def set_floating_ip_pool_prefixes(self, value):
        self.floating_ip_pool_prefixes = value
    #end set_floating_ip_pool_prefixes

    def get_floating_ip_pool_prefixes(self):
        return self.floating_ip_pool_prefixes
    #end get_floating_ip_pool_prefixes

    @property
    def id_perms(self):
        """Get id-perms for floating-ip-pool.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for floating-ip-pool.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for floating-ip-pool.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for floating-ip-pool.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_floating_ip_pool_prefixes'):
            self._serialize_field_to_json(serialized, field_names, 'floating_ip_pool_prefixes')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_floating_ips(self):
        return getattr(self, 'floating_ips', None)
    #end get_floating_ips

    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this floating-ip-pool"""
        return getattr(self, 'virtual_network_back_refs', None)
    #end get_virtual_network_back_refs

    def get_project_back_refs(self):
        """Return list of all projects using this floating-ip-pool"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def dump(self):
        """Display floating-ip-pool object in compact form."""
        print '------------ floating-ip-pool ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P floating_ip_pool_prefixes = ', self.get_floating_ip_pool_prefixes()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS floating_ip = ', self.get_floating_ips()
        print 'BCK project = ', self.get_project_back_refs()
    #end dump

#end class FloatingIpPool

class PhysicalRouter(object):
    """
    Represents physical-router configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * physical-router-management-ip (IpAddress type)
        * physical-router-dataplane-ip (IpAddress type)
        * physical-router-vendor-name (xsd:string type)
        * physical-router-product-name (xsd:string type)
        * physical-router-vnc-managed (xsd:boolean type)
        * physical-router-user-credentials (:class:`.UserCredentials` type)
        * physical-router-snmp-credentials (:class:`.SNMPCredentials` type)
        * physical-router-junos-service-ports (:class:`.JunosServicePorts` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.PhysicalInterface` objects
        * list of :class:`.LogicalInterface` objects

    References to:
        * list of :class:`.VirtualRouter` objects
        * list of :class:`.BgpRouter` objects
        * list of :class:`.VirtualNetwork` objects

    Referred by:
    """

    prop_fields = set([u'physical_router_management_ip', u'physical_router_dataplane_ip', u'physical_router_vendor_name', u'physical_router_product_name', u'physical_router_vnc_managed', u'physical_router_user_credentials', u'physical_router_snmp_credentials', u'physical_router_junos_service_ports', u'id_perms', u'display_name'])
    ref_fields = set(['virtual_router_refs', 'bgp_router_refs', u'virtual_network_refs'])
    backref_fields = set([u'global_system_config_back_refs'])
    children_fields = set([u'physical_interfaces', u'logical_interfaces'])

    def __init__(self, name = None, parent_obj = None, physical_router_management_ip = None, physical_router_dataplane_ip = None, physical_router_vendor_name = None, physical_router_product_name = None, physical_router_vnc_managed = None, physical_router_user_credentials = None, physical_router_snmp_credentials = None, physical_router_junos_service_ports = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'physical-router'
        if not name:
            name = u'default-physical-router'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'global-system-config'
            self.fq_name = [u'default-global-system-config']
            self.fq_name.append(name)


        # property fields
        if physical_router_management_ip:
            self._physical_router_management_ip = physical_router_management_ip
        if physical_router_dataplane_ip:
            self._physical_router_dataplane_ip = physical_router_dataplane_ip
        if physical_router_vendor_name:
            self._physical_router_vendor_name = physical_router_vendor_name
        if physical_router_product_name:
            self._physical_router_product_name = physical_router_product_name
        if physical_router_vnc_managed:
            self._physical_router_vnc_managed = physical_router_vnc_managed
        if physical_router_user_credentials:
            self._physical_router_user_credentials = physical_router_user_credentials
        if physical_router_snmp_credentials:
            self._physical_router_snmp_credentials = physical_router_snmp_credentials
        if physical_router_junos_service_ports:
            self._physical_router_junos_service_ports = physical_router_junos_service_ports
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (physical-router)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of physical-router in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of physical-router as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of physical-router's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of physical-router's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def physical_router_management_ip(self):
        """Get physical-router-management-ip for physical-router.
        
        :returns: IpAddress object
        
        """
        return getattr(self, '_physical_router_management_ip', None)
    #end physical_router_management_ip

    @physical_router_management_ip.setter
    def physical_router_management_ip(self, physical_router_management_ip):
        """Set physical-router-management-ip for physical-router.
        
        :param physical_router_management_ip: IpAddress object
        
        """
        self._physical_router_management_ip = physical_router_management_ip
    #end physical_router_management_ip

    def set_physical_router_management_ip(self, value):
        self.physical_router_management_ip = value
    #end set_physical_router_management_ip

    def get_physical_router_management_ip(self):
        return self.physical_router_management_ip
    #end get_physical_router_management_ip

    @property
    def physical_router_dataplane_ip(self):
        """Get physical-router-dataplane-ip for physical-router.
        
        :returns: IpAddress object
        
        """
        return getattr(self, '_physical_router_dataplane_ip', None)
    #end physical_router_dataplane_ip

    @physical_router_dataplane_ip.setter
    def physical_router_dataplane_ip(self, physical_router_dataplane_ip):
        """Set physical-router-dataplane-ip for physical-router.
        
        :param physical_router_dataplane_ip: IpAddress object
        
        """
        self._physical_router_dataplane_ip = physical_router_dataplane_ip
    #end physical_router_dataplane_ip

    def set_physical_router_dataplane_ip(self, value):
        self.physical_router_dataplane_ip = value
    #end set_physical_router_dataplane_ip

    def get_physical_router_dataplane_ip(self):
        return self.physical_router_dataplane_ip
    #end get_physical_router_dataplane_ip

    @property
    def physical_router_vendor_name(self):
        """Get physical-router-vendor-name for physical-router.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_physical_router_vendor_name', None)
    #end physical_router_vendor_name

    @physical_router_vendor_name.setter
    def physical_router_vendor_name(self, physical_router_vendor_name):
        """Set physical-router-vendor-name for physical-router.
        
        :param physical_router_vendor_name: xsd:string object
        
        """
        self._physical_router_vendor_name = physical_router_vendor_name
    #end physical_router_vendor_name

    def set_physical_router_vendor_name(self, value):
        self.physical_router_vendor_name = value
    #end set_physical_router_vendor_name

    def get_physical_router_vendor_name(self):
        return self.physical_router_vendor_name
    #end get_physical_router_vendor_name

    @property
    def physical_router_product_name(self):
        """Get physical-router-product-name for physical-router.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_physical_router_product_name', None)
    #end physical_router_product_name

    @physical_router_product_name.setter
    def physical_router_product_name(self, physical_router_product_name):
        """Set physical-router-product-name for physical-router.
        
        :param physical_router_product_name: xsd:string object
        
        """
        self._physical_router_product_name = physical_router_product_name
    #end physical_router_product_name

    def set_physical_router_product_name(self, value):
        self.physical_router_product_name = value
    #end set_physical_router_product_name

    def get_physical_router_product_name(self):
        return self.physical_router_product_name
    #end get_physical_router_product_name

    @property
    def physical_router_vnc_managed(self):
        """Get physical-router-vnc-managed for physical-router.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_physical_router_vnc_managed', None)
    #end physical_router_vnc_managed

    @physical_router_vnc_managed.setter
    def physical_router_vnc_managed(self, physical_router_vnc_managed):
        """Set physical-router-vnc-managed for physical-router.
        
        :param physical_router_vnc_managed: xsd:boolean object
        
        """
        self._physical_router_vnc_managed = physical_router_vnc_managed
    #end physical_router_vnc_managed

    def set_physical_router_vnc_managed(self, value):
        self.physical_router_vnc_managed = value
    #end set_physical_router_vnc_managed

    def get_physical_router_vnc_managed(self):
        return self.physical_router_vnc_managed
    #end get_physical_router_vnc_managed

    @property
    def physical_router_user_credentials(self):
        """Get physical-router-user-credentials for physical-router.
        
        :returns: UserCredentials object
        
        """
        return getattr(self, '_physical_router_user_credentials', None)
    #end physical_router_user_credentials

    @physical_router_user_credentials.setter
    def physical_router_user_credentials(self, physical_router_user_credentials):
        """Set physical-router-user-credentials for physical-router.
        
        :param physical_router_user_credentials: UserCredentials object
        
        """
        self._physical_router_user_credentials = physical_router_user_credentials
    #end physical_router_user_credentials

    def set_physical_router_user_credentials(self, value):
        self.physical_router_user_credentials = value
    #end set_physical_router_user_credentials

    def get_physical_router_user_credentials(self):
        return self.physical_router_user_credentials
    #end get_physical_router_user_credentials

    @property
    def physical_router_snmp_credentials(self):
        """Get physical-router-snmp-credentials for physical-router.
        
        :returns: SNMPCredentials object
        
        """
        return getattr(self, '_physical_router_snmp_credentials', None)
    #end physical_router_snmp_credentials

    @physical_router_snmp_credentials.setter
    def physical_router_snmp_credentials(self, physical_router_snmp_credentials):
        """Set physical-router-snmp-credentials for physical-router.
        
        :param physical_router_snmp_credentials: SNMPCredentials object
        
        """
        self._physical_router_snmp_credentials = physical_router_snmp_credentials
    #end physical_router_snmp_credentials

    def set_physical_router_snmp_credentials(self, value):
        self.physical_router_snmp_credentials = value
    #end set_physical_router_snmp_credentials

    def get_physical_router_snmp_credentials(self):
        return self.physical_router_snmp_credentials
    #end get_physical_router_snmp_credentials

    @property
    def physical_router_junos_service_ports(self):
        """Get physical-router-junos-service-ports for physical-router.
        
        :returns: JunosServicePorts object
        
        """
        return getattr(self, '_physical_router_junos_service_ports', None)
    #end physical_router_junos_service_ports

    @physical_router_junos_service_ports.setter
    def physical_router_junos_service_ports(self, physical_router_junos_service_ports):
        """Set physical-router-junos-service-ports for physical-router.
        
        :param physical_router_junos_service_ports: JunosServicePorts object
        
        """
        self._physical_router_junos_service_ports = physical_router_junos_service_ports
    #end physical_router_junos_service_ports

    def set_physical_router_junos_service_ports(self, value):
        self.physical_router_junos_service_ports = value
    #end set_physical_router_junos_service_ports

    def get_physical_router_junos_service_ports(self):
        return self.physical_router_junos_service_ports
    #end get_physical_router_junos_service_ports

    @property
    def id_perms(self):
        """Get id-perms for physical-router.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for physical-router.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for physical-router.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for physical-router.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_physical_router_management_ip'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_management_ip')
        if hasattr(self, '_physical_router_dataplane_ip'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_dataplane_ip')
        if hasattr(self, '_physical_router_vendor_name'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_vendor_name')
        if hasattr(self, '_physical_router_product_name'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_product_name')
        if hasattr(self, '_physical_router_vnc_managed'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_vnc_managed')
        if hasattr(self, '_physical_router_user_credentials'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_user_credentials')
        if hasattr(self, '_physical_router_snmp_credentials'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_snmp_credentials')
        if hasattr(self, '_physical_router_junos_service_ports'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_junos_service_ports')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_router_refs')
        if hasattr(self, 'bgp_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'bgp_router_refs')
        if hasattr(self, 'virtual_network_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_refs')
        return serialized
    #end serialize_to_json

    def get_physical_interfaces(self):
        return getattr(self, 'physical_interfaces', None)
    #end get_physical_interfaces

    def get_logical_interfaces(self):
        return getattr(self, 'logical_interfaces', None)
    #end get_logical_interfaces

    def set_virtual_router(self, ref_obj):
        """Set virtual-router for physical-router.
        
        :param ref_obj: VirtualRouter object
        
        """
        self.virtual_router_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_router

    def add_virtual_router(self, ref_obj):
        """Add virtual-router to physical-router.
        
        :param ref_obj: VirtualRouter object
        
        """
        refs = getattr(self, 'virtual_router_refs', [])
        if not refs:
            self.virtual_router_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_router_refs.append(ref_info)
    #end add_virtual_router

    def del_virtual_router(self, ref_obj):
        refs = self.get_virtual_router_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_router_refs.remove(ref)
                return
    #end del_virtual_router

    def set_virtual_router_list(self, ref_obj_list):
        """Set virtual-router list for physical-router.
        
        :param ref_obj_list: list of VirtualRouter object
        
        """
        self.virtual_router_refs = ref_obj_list
    #end set_virtual_router_list

    def get_virtual_router_refs(self):
        """Return virtual-router list for physical-router.
        
        :returns: list of <VirtualRouter>
        
        """
        return getattr(self, 'virtual_router_refs', None)
    #end get_virtual_router_refs

    def set_bgp_router(self, ref_obj):
        """Set bgp-router for physical-router.
        
        :param ref_obj: BgpRouter object
        
        """
        self.bgp_router_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.bgp_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_bgp_router

    def add_bgp_router(self, ref_obj):
        """Add bgp-router to physical-router.
        
        :param ref_obj: BgpRouter object
        
        """
        refs = getattr(self, 'bgp_router_refs', [])
        if not refs:
            self.bgp_router_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.bgp_router_refs.append(ref_info)
    #end add_bgp_router

    def del_bgp_router(self, ref_obj):
        refs = self.get_bgp_router_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.bgp_router_refs.remove(ref)
                return
    #end del_bgp_router

    def set_bgp_router_list(self, ref_obj_list):
        """Set bgp-router list for physical-router.
        
        :param ref_obj_list: list of BgpRouter object
        
        """
        self.bgp_router_refs = ref_obj_list
    #end set_bgp_router_list

    def get_bgp_router_refs(self):
        """Return bgp-router list for physical-router.
        
        :returns: list of <BgpRouter>
        
        """
        return getattr(self, 'bgp_router_refs', None)
    #end get_bgp_router_refs

    def set_virtual_network(self, ref_obj):
        """Set virtual-network for physical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self.virtual_network_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_network_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_network

    def add_virtual_network(self, ref_obj):
        """Add virtual-network to physical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        refs = getattr(self, 'virtual_network_refs', [])
        if not refs:
            self.virtual_network_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_network_refs.append(ref_info)
    #end add_virtual_network

    def del_virtual_network(self, ref_obj):
        refs = self.get_virtual_network_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_network_refs.remove(ref)
                return
    #end del_virtual_network

    def set_virtual_network_list(self, ref_obj_list):
        """Set virtual-network list for physical-router.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self.virtual_network_refs = ref_obj_list
    #end set_virtual_network_list

    def get_virtual_network_refs(self):
        """Return virtual-network list for physical-router.
        
        :returns: list of <VirtualNetwork>
        
        """
        return getattr(self, 'virtual_network_refs', None)
    #end get_virtual_network_refs

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this physical-router"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def dump(self):
        """Display physical-router object in compact form."""
        print '------------ physical-router ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P physical_router_management_ip = ', self.get_physical_router_management_ip()
        print 'P physical_router_dataplane_ip = ', self.get_physical_router_dataplane_ip()
        print 'P physical_router_vendor_name = ', self.get_physical_router_vendor_name()
        print 'P physical_router_product_name = ', self.get_physical_router_product_name()
        print 'P physical_router_vnc_managed = ', self.get_physical_router_vnc_managed()
        print 'P physical_router_user_credentials = ', self.get_physical_router_user_credentials()
        print 'P physical_router_snmp_credentials = ', self.get_physical_router_snmp_credentials()
        print 'P physical_router_junos_service_ports = ', self.get_physical_router_junos_service_ports()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_router = ', self.get_virtual_router_refs()
        print 'REF bgp_router = ', self.get_bgp_router_refs()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'HAS physical_interface = ', self.get_physical_interfaces()
        print 'HAS logical_interface = ', self.get_logical_interfaces()
    #end dump

#end class PhysicalRouter

class BgpRouter(object):
    """
    Represents bgp-router configuration representation.

    Child of:
        :class:`.RoutingInstance` object OR

    Properties:
        * bgp-router-parameters (:class:`.BgpRouterParams` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of (:class:`.BgpRouter` object, :class:`.BgpPeeringAttributes` attribute)

    Referred by:
        * list of :class:`.GlobalSystemConfig` objects
        * list of :class:`.PhysicalRouter` objects
        * list of :class:`.VirtualRouter` objects
        * list of :class:`.BgpRouter` objects
    """

    prop_fields = set([u'bgp_router_parameters', u'id_perms', u'display_name'])
    ref_fields = set(['bgp_router_refs'])
    backref_fields = set([u'global_system_config_back_refs', u'physical_router_back_refs', 'virtual_router_back_refs', 'routing_instance_back_refs', 'bgp_router_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, bgp_router_parameters = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'bgp-router'
        if not name:
            name = u'default-bgp-router'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'routing-instance'
            self.fq_name = [u'default-domain', u'default-project', u'default-virtual-network', 'default-routing-instance']
            self.fq_name.append(name)


        # property fields
        if bgp_router_parameters:
            self._bgp_router_parameters = bgp_router_parameters
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (bgp-router)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of bgp-router in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of bgp-router as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of bgp-router's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of bgp-router's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def bgp_router_parameters(self):
        """Get bgp-router-parameters for bgp-router.
        
        :returns: BgpRouterParams object
        
        """
        return getattr(self, '_bgp_router_parameters', None)
    #end bgp_router_parameters

    @bgp_router_parameters.setter
    def bgp_router_parameters(self, bgp_router_parameters):
        """Set bgp-router-parameters for bgp-router.
        
        :param bgp_router_parameters: BgpRouterParams object
        
        """
        self._bgp_router_parameters = bgp_router_parameters
    #end bgp_router_parameters

    def set_bgp_router_parameters(self, value):
        self.bgp_router_parameters = value
    #end set_bgp_router_parameters

    def get_bgp_router_parameters(self):
        return self.bgp_router_parameters
    #end get_bgp_router_parameters

    @property
    def id_perms(self):
        """Get id-perms for bgp-router.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for bgp-router.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for bgp-router.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for bgp-router.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_bgp_router_parameters'):
            self._serialize_field_to_json(serialized, field_names, 'bgp_router_parameters')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'bgp_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'bgp_router_refs')
        return serialized
    #end serialize_to_json

    def set_bgp_router(self, ref_obj, ref_data):
        """Set bgp-router for bgp-router.
        
        :param ref_obj: BgpRouter object
        :param ref_data: BgpPeeringAttributes object
        
        """
        self.bgp_router_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.bgp_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_bgp_router

    def add_bgp_router(self, ref_obj, ref_data):
        """Add bgp-router to bgp-router.
        
        :param ref_obj: BgpRouter object
        :param ref_data: BgpPeeringAttributes object
        
        """
        refs = getattr(self, 'bgp_router_refs', [])
        if not refs:
            self.bgp_router_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.bgp_router_refs.append(ref_info)
    #end add_bgp_router

    def del_bgp_router(self, ref_obj):
        refs = self.get_bgp_router_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.bgp_router_refs.remove(ref)
                return
    #end del_bgp_router

    def set_bgp_router_list(self, ref_obj_list, ref_data_list):
        """Set bgp-router list for bgp-router.
        
        :param ref_obj_list: list of BgpRouter object
        :param ref_data_list: list of BgpPeeringAttributes object
        
        """
        self.bgp_router_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_bgp_router_list

    def get_bgp_router_refs(self):
        """Return bgp-router list for bgp-router.
        
        :returns: list of tuple <BgpRouter, BgpPeeringAttributes>
        
        """
        return getattr(self, 'bgp_router_refs', None)
    #end get_bgp_router_refs

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this bgp-router"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this bgp-router"""
        return getattr(self, 'physical_router_back_refs', None)
    #end get_physical_router_back_refs

    def get_virtual_router_back_refs(self):
        """Return list of all virtual-routers using this bgp-router"""
        return getattr(self, 'virtual_router_back_refs', None)
    #end get_virtual_router_back_refs

    def get_routing_instance_back_refs(self):
        """Return list of all routing-instances using this bgp-router"""
        return getattr(self, 'routing_instance_back_refs', None)
    #end get_routing_instance_back_refs

    def get_bgp_router_back_refs(self):
        """Return list of all bgp-routers using this bgp-router"""
        return getattr(self, 'bgp_router_back_refs', None)
    #end get_bgp_router_back_refs

    def dump(self):
        """Display bgp-router object in compact form."""
        print '------------ bgp-router ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P bgp_router_parameters = ', self.get_bgp_router_parameters()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF bgp_router = ', self.get_bgp_router_refs()
        print 'BCK global_system_config = ', self.get_global_system_config_back_refs()
        print 'BCK physical_router = ', self.get_physical_router_back_refs()
        print 'BCK virtual_router = ', self.get_virtual_router_back_refs()
        print 'BCK bgp_router = ', self.get_bgp_router_back_refs()
    #end dump

#end class BgpRouter

class VirtualRouter(object):
    """
    Represents virtual-router configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * virtual-router-type (VirtualRouterType type)
        * virtual-router-ip-address (IpAddressType type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.BgpRouter` objects
        * list of :class:`.VirtualMachine` objects

    Referred by:
        * list of :class:`.PhysicalRouter` objects
        * list of :class:`.ProviderAttachment` objects
    """

    prop_fields = set([u'virtual_router_type', u'virtual_router_ip_address', u'id_perms', u'display_name'])
    ref_fields = set(['bgp_router_refs', u'virtual_machine_refs'])
    backref_fields = set([u'physical_router_back_refs', u'global_system_config_back_refs', 'provider_attachment_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, virtual_router_type = None, virtual_router_ip_address = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-router'
        if not name:
            name = u'default-virtual-router'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'global-system-config'
            self.fq_name = [u'default-global-system-config']
            self.fq_name.append(name)


        # property fields
        if virtual_router_type:
            self._virtual_router_type = virtual_router_type
        if virtual_router_ip_address:
            self._virtual_router_ip_address = virtual_router_ip_address
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (virtual-router)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of virtual-router in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of virtual-router as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of virtual-router's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of virtual-router's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def virtual_router_type(self):
        """Get virtual-router-type for virtual-router.
        
        :returns: VirtualRouterType object
        
        """
        return getattr(self, '_virtual_router_type', None)
    #end virtual_router_type

    @virtual_router_type.setter
    def virtual_router_type(self, virtual_router_type):
        """Set virtual-router-type for virtual-router.
        
        :param virtual_router_type: VirtualRouterType object
        
        """
        self._virtual_router_type = virtual_router_type
    #end virtual_router_type

    def set_virtual_router_type(self, value):
        self.virtual_router_type = value
    #end set_virtual_router_type

    def get_virtual_router_type(self):
        return self.virtual_router_type
    #end get_virtual_router_type

    @property
    def virtual_router_ip_address(self):
        """Get virtual-router-ip-address for virtual-router.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_virtual_router_ip_address', None)
    #end virtual_router_ip_address

    @virtual_router_ip_address.setter
    def virtual_router_ip_address(self, virtual_router_ip_address):
        """Set virtual-router-ip-address for virtual-router.
        
        :param virtual_router_ip_address: IpAddressType object
        
        """
        self._virtual_router_ip_address = virtual_router_ip_address
    #end virtual_router_ip_address

    def set_virtual_router_ip_address(self, value):
        self.virtual_router_ip_address = value
    #end set_virtual_router_ip_address

    def get_virtual_router_ip_address(self):
        return self.virtual_router_ip_address
    #end get_virtual_router_ip_address

    @property
    def id_perms(self):
        """Get id-perms for virtual-router.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-router.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for virtual-router.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-router.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_virtual_router_type'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_router_type')
        if hasattr(self, '_virtual_router_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_router_ip_address')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'bgp_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'bgp_router_refs')
        if hasattr(self, 'virtual_machine_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_refs')
        return serialized
    #end serialize_to_json

    def set_bgp_router(self, ref_obj):
        """Set bgp-router for virtual-router.
        
        :param ref_obj: BgpRouter object
        
        """
        self.bgp_router_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.bgp_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_bgp_router

    def add_bgp_router(self, ref_obj):
        """Add bgp-router to virtual-router.
        
        :param ref_obj: BgpRouter object
        
        """
        refs = getattr(self, 'bgp_router_refs', [])
        if not refs:
            self.bgp_router_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.bgp_router_refs.append(ref_info)
    #end add_bgp_router

    def del_bgp_router(self, ref_obj):
        refs = self.get_bgp_router_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.bgp_router_refs.remove(ref)
                return
    #end del_bgp_router

    def set_bgp_router_list(self, ref_obj_list):
        """Set bgp-router list for virtual-router.
        
        :param ref_obj_list: list of BgpRouter object
        
        """
        self.bgp_router_refs = ref_obj_list
    #end set_bgp_router_list

    def get_bgp_router_refs(self):
        """Return bgp-router list for virtual-router.
        
        :returns: list of <BgpRouter>
        
        """
        return getattr(self, 'bgp_router_refs', None)
    #end get_bgp_router_refs

    def set_virtual_machine(self, ref_obj):
        """Set virtual-machine for virtual-router.
        
        :param ref_obj: VirtualMachine object
        
        """
        self.virtual_machine_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine

    def add_virtual_machine(self, ref_obj):
        """Add virtual-machine to virtual-router.
        
        :param ref_obj: VirtualMachine object
        
        """
        refs = getattr(self, 'virtual_machine_refs', [])
        if not refs:
            self.virtual_machine_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_refs.append(ref_info)
    #end add_virtual_machine

    def del_virtual_machine(self, ref_obj):
        refs = self.get_virtual_machine_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_refs.remove(ref)
                return
    #end del_virtual_machine

    def set_virtual_machine_list(self, ref_obj_list):
        """Set virtual-machine list for virtual-router.
        
        :param ref_obj_list: list of VirtualMachine object
        
        """
        self.virtual_machine_refs = ref_obj_list
    #end set_virtual_machine_list

    def get_virtual_machine_refs(self):
        """Return virtual-machine list for virtual-router.
        
        :returns: list of <VirtualMachine>
        
        """
        return getattr(self, 'virtual_machine_refs', None)
    #end get_virtual_machine_refs

    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this virtual-router"""
        return getattr(self, 'physical_router_back_refs', None)
    #end get_physical_router_back_refs

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this virtual-router"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def get_provider_attachment_back_refs(self):
        """Return list of all provider-attachments using this virtual-router"""
        return getattr(self, 'provider_attachment_back_refs', None)
    #end get_provider_attachment_back_refs

    def dump(self):
        """Display virtual-router object in compact form."""
        print '------------ virtual-router ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_router_type = ', self.get_virtual_router_type()
        print 'P virtual_router_ip_address = ', self.get_virtual_router_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF bgp_router = ', self.get_bgp_router_refs()
        print 'REF virtual_machine = ', self.get_virtual_machine_refs()
        print 'BCK physical_router = ', self.get_physical_router_back_refs()
        print 'BCK provider_attachment = ', self.get_provider_attachment_back_refs()
    #end dump

#end class VirtualRouter

class ConfigRoot(object):
    """
    Represents config-root configuration representation.

    Properties:
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.GlobalSystemConfig` objects
        * list of :class:`.Domain` objects

    References to:

    Referred by:
    """

    prop_fields = set([u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([u'global_system_configs', u'domains'])

    def __init__(self, name = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'config-root'
        if not name:
            name = u'default-config-root'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (config-root)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of config-root in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of config-root as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def id_perms(self):
        """Get id-perms for config-root.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for config-root.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for config-root.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for config-root.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_global_system_configs(self):
        return getattr(self, 'global_system_configs', None)
    #end get_global_system_configs

    def get_domains(self):
        return getattr(self, 'domains', None)
    #end get_domains

    def dump(self):
        """Display config-root object in compact form."""
        print '------------ config-root ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS global_system_config = ', self.get_global_system_configs()
        print 'HAS domain = ', self.get_domains()
    #end dump

#end class ConfigRoot

class Subnet(object):
    """
    Represents subnet configuration representation.

    Properties:
        * subnet-ip-prefix (:class:`.SubnetType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects

    Referred by:
    """

    prop_fields = set([u'subnet_ip_prefix', u'id_perms', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs'])
    backref_fields = set([])
    children_fields = set([])

    def __init__(self, name = None, subnet_ip_prefix = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'subnet'
        if not name:
            name = u'default-subnet'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if subnet_ip_prefix:
            self._subnet_ip_prefix = subnet_ip_prefix
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (subnet)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of subnet in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of subnet as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def subnet_ip_prefix(self):
        """Get subnet-ip-prefix for subnet.
        
        :returns: SubnetType object
        
        """
        return getattr(self, '_subnet_ip_prefix', None)
    #end subnet_ip_prefix

    @subnet_ip_prefix.setter
    def subnet_ip_prefix(self, subnet_ip_prefix):
        """Set subnet-ip-prefix for subnet.
        
        :param subnet_ip_prefix: SubnetType object
        
        """
        self._subnet_ip_prefix = subnet_ip_prefix
    #end subnet_ip_prefix

    def set_subnet_ip_prefix(self, value):
        self.subnet_ip_prefix = value
    #end set_subnet_ip_prefix

    def get_subnet_ip_prefix(self):
        return self.subnet_ip_prefix
    #end get_subnet_ip_prefix

    @property
    def id_perms(self):
        """Get id-perms for subnet.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for subnet.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for subnet.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for subnet.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_subnet_ip_prefix'):
            self._serialize_field_to_json(serialized, field_names, 'subnet_ip_prefix')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for subnet.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to subnet.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for subnet.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for subnet.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def dump(self):
        """Display subnet object in compact form."""
        print '------------ subnet ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P subnet_ip_prefix = ', self.get_subnet_ip_prefix()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
    #end dump

#end class Subnet

class GlobalSystemConfig(object):
    """
    Represents global-system-config configuration representation.

    Child of:
        :class:`.ConfigRoot` object OR

    Properties:
        * autonomous-system (AutonomousSystemType type)
        * config-version (xsd:string type)
        * plugin-tuning (:class:`.PluginProperties` type)
        * ibgp-auto-mesh (xsd:boolean type)
        * ip-fabric-subnets (:class:`.SubnetListType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.GlobalVrouterConfig` objects
        * list of :class:`.PhysicalRouter` objects
        * list of :class:`.VirtualRouter` objects
        * list of :class:`.ConfigNode` objects
        * list of :class:`.AnalyticsNode` objects
        * list of :class:`.DatabaseNode` objects
        * list of :class:`.ServiceApplianceSet` objects

    References to:
        * list of :class:`.BgpRouter` objects

    Referred by:
    """

    prop_fields = set([u'autonomous_system', u'config_version', u'plugin_tuning', u'ibgp_auto_mesh', u'ip_fabric_subnets', u'id_perms', u'display_name'])
    ref_fields = set(['bgp_router_refs'])
    backref_fields = set([u'config_root_back_refs'])
    children_fields = set([u'global_vrouter_configs', u'physical_routers', 'virtual_routers', u'config_nodes', u'analytics_nodes', u'database_nodes', u'service_appliance_sets'])

    def __init__(self, name = None, parent_obj = None, autonomous_system = None, config_version = None, plugin_tuning = None, ibgp_auto_mesh = None, ip_fabric_subnets = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'global-system-config'
        if not name:
            name = u'default-global-system-config'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.fq_name = [name]

        # property fields
        if autonomous_system:
            self._autonomous_system = autonomous_system
        if config_version:
            self._config_version = config_version
        if plugin_tuning:
            self._plugin_tuning = plugin_tuning
        if ibgp_auto_mesh:
            self._ibgp_auto_mesh = ibgp_auto_mesh
        if ip_fabric_subnets:
            self._ip_fabric_subnets = ip_fabric_subnets
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (global-system-config)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of global-system-config in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of global-system-config as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of global-system-config's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of global-system-config's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def autonomous_system(self):
        """Get autonomous-system for global-system-config.
        
        :returns: AutonomousSystemType object
        
        """
        return getattr(self, '_autonomous_system', None)
    #end autonomous_system

    @autonomous_system.setter
    def autonomous_system(self, autonomous_system):
        """Set autonomous-system for global-system-config.
        
        :param autonomous_system: AutonomousSystemType object
        
        """
        self._autonomous_system = autonomous_system
    #end autonomous_system

    def set_autonomous_system(self, value):
        self.autonomous_system = value
    #end set_autonomous_system

    def get_autonomous_system(self):
        return self.autonomous_system
    #end get_autonomous_system

    @property
    def config_version(self):
        """Get config-version for global-system-config.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_config_version', None)
    #end config_version

    @config_version.setter
    def config_version(self, config_version):
        """Set config-version for global-system-config.
        
        :param config_version: xsd:string object
        
        """
        self._config_version = config_version
    #end config_version

    def set_config_version(self, value):
        self.config_version = value
    #end set_config_version

    def get_config_version(self):
        return self.config_version
    #end get_config_version

    @property
    def plugin_tuning(self):
        """Get plugin-tuning for global-system-config.
        
        :returns: PluginProperties object
        
        """
        return getattr(self, '_plugin_tuning', None)
    #end plugin_tuning

    @plugin_tuning.setter
    def plugin_tuning(self, plugin_tuning):
        """Set plugin-tuning for global-system-config.
        
        :param plugin_tuning: PluginProperties object
        
        """
        self._plugin_tuning = plugin_tuning
    #end plugin_tuning

    def set_plugin_tuning(self, value):
        self.plugin_tuning = value
    #end set_plugin_tuning

    def get_plugin_tuning(self):
        return self.plugin_tuning
    #end get_plugin_tuning

    @property
    def ibgp_auto_mesh(self):
        """Get ibgp-auto-mesh for global-system-config.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_ibgp_auto_mesh', None)
    #end ibgp_auto_mesh

    @ibgp_auto_mesh.setter
    def ibgp_auto_mesh(self, ibgp_auto_mesh):
        """Set ibgp-auto-mesh for global-system-config.
        
        :param ibgp_auto_mesh: xsd:boolean object
        
        """
        self._ibgp_auto_mesh = ibgp_auto_mesh
    #end ibgp_auto_mesh

    def set_ibgp_auto_mesh(self, value):
        self.ibgp_auto_mesh = value
    #end set_ibgp_auto_mesh

    def get_ibgp_auto_mesh(self):
        return self.ibgp_auto_mesh
    #end get_ibgp_auto_mesh

    @property
    def ip_fabric_subnets(self):
        """Get ip-fabric-subnets for global-system-config.
        
        :returns: SubnetListType object
        
        """
        return getattr(self, '_ip_fabric_subnets', None)
    #end ip_fabric_subnets

    @ip_fabric_subnets.setter
    def ip_fabric_subnets(self, ip_fabric_subnets):
        """Set ip-fabric-subnets for global-system-config.
        
        :param ip_fabric_subnets: SubnetListType object
        
        """
        self._ip_fabric_subnets = ip_fabric_subnets
    #end ip_fabric_subnets

    def set_ip_fabric_subnets(self, value):
        self.ip_fabric_subnets = value
    #end set_ip_fabric_subnets

    def get_ip_fabric_subnets(self):
        return self.ip_fabric_subnets
    #end get_ip_fabric_subnets

    @property
    def id_perms(self):
        """Get id-perms for global-system-config.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for global-system-config.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for global-system-config.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for global-system-config.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_autonomous_system'):
            self._serialize_field_to_json(serialized, field_names, 'autonomous_system')
        if hasattr(self, '_config_version'):
            self._serialize_field_to_json(serialized, field_names, 'config_version')
        if hasattr(self, '_plugin_tuning'):
            self._serialize_field_to_json(serialized, field_names, 'plugin_tuning')
        if hasattr(self, '_ibgp_auto_mesh'):
            self._serialize_field_to_json(serialized, field_names, 'ibgp_auto_mesh')
        if hasattr(self, '_ip_fabric_subnets'):
            self._serialize_field_to_json(serialized, field_names, 'ip_fabric_subnets')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'bgp_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'bgp_router_refs')
        return serialized
    #end serialize_to_json

    def get_global_vrouter_configs(self):
        return getattr(self, 'global_vrouter_configs', None)
    #end get_global_vrouter_configs

    def get_physical_routers(self):
        return getattr(self, 'physical_routers', None)
    #end get_physical_routers

    def get_virtual_routers(self):
        return getattr(self, 'virtual_routers', None)
    #end get_virtual_routers

    def get_config_nodes(self):
        return getattr(self, 'config_nodes', None)
    #end get_config_nodes

    def get_analytics_nodes(self):
        return getattr(self, 'analytics_nodes', None)
    #end get_analytics_nodes

    def get_database_nodes(self):
        return getattr(self, 'database_nodes', None)
    #end get_database_nodes

    def get_service_appliance_sets(self):
        return getattr(self, 'service_appliance_sets', None)
    #end get_service_appliance_sets

    def set_bgp_router(self, ref_obj):
        """Set bgp-router for global-system-config.
        
        :param ref_obj: BgpRouter object
        
        """
        self.bgp_router_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.bgp_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_bgp_router

    def add_bgp_router(self, ref_obj):
        """Add bgp-router to global-system-config.
        
        :param ref_obj: BgpRouter object
        
        """
        refs = getattr(self, 'bgp_router_refs', [])
        if not refs:
            self.bgp_router_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.bgp_router_refs.append(ref_info)
    #end add_bgp_router

    def del_bgp_router(self, ref_obj):
        refs = self.get_bgp_router_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.bgp_router_refs.remove(ref)
                return
    #end del_bgp_router

    def set_bgp_router_list(self, ref_obj_list):
        """Set bgp-router list for global-system-config.
        
        :param ref_obj_list: list of BgpRouter object
        
        """
        self.bgp_router_refs = ref_obj_list
    #end set_bgp_router_list

    def get_bgp_router_refs(self):
        """Return bgp-router list for global-system-config.
        
        :returns: list of <BgpRouter>
        
        """
        return getattr(self, 'bgp_router_refs', None)
    #end get_bgp_router_refs

    def get_config_root_back_refs(self):
        """Return list of all config-roots using this global-system-config"""
        return getattr(self, 'config_root_back_refs', None)
    #end get_config_root_back_refs

    def dump(self):
        """Display global-system-config object in compact form."""
        print '------------ global-system-config ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P autonomous_system = ', self.get_autonomous_system()
        print 'P config_version = ', self.get_config_version()
        print 'P plugin_tuning = ', self.get_plugin_tuning()
        print 'P ibgp_auto_mesh = ', self.get_ibgp_auto_mesh()
        print 'P ip_fabric_subnets = ', self.get_ip_fabric_subnets()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF bgp_router = ', self.get_bgp_router_refs()
        print 'HAS global_vrouter_config = ', self.get_global_vrouter_configs()
        print 'HAS physical_router = ', self.get_physical_routers()
        print 'HAS virtual_router = ', self.get_virtual_routers()
        print 'HAS config_node = ', self.get_config_nodes()
        print 'HAS analytics_node = ', self.get_analytics_nodes()
        print 'HAS database_node = ', self.get_database_nodes()
        print 'HAS service_appliance_set = ', self.get_service_appliance_sets()
    #end dump

#end class GlobalSystemConfig

class ServiceAppliance(object):
    """
    Represents service-appliance configuration representation.

    Child of:
        :class:`.ServiceApplianceSet` object OR

    Properties:
        * service-appliance-user-credentials (:class:`.UserCredentials` type)
        * service-appliance-ip-address (IpAddressType type)
        * service-appliance-properties (:class:`.KeyValuePairs` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'service_appliance_user_credentials', u'service_appliance_ip_address', u'service_appliance_properties', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'service_appliance_set_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, service_appliance_user_credentials = None, service_appliance_ip_address = None, service_appliance_properties = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'service-appliance'
        if not name:
            name = u'default-service-appliance'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'service-appliance-set'
            self.fq_name = [u'default-global-system-config', u'default-service-appliance-set']
            self.fq_name.append(name)


        # property fields
        if service_appliance_user_credentials:
            self._service_appliance_user_credentials = service_appliance_user_credentials
        if service_appliance_ip_address:
            self._service_appliance_ip_address = service_appliance_ip_address
        if service_appliance_properties:
            self._service_appliance_properties = service_appliance_properties
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (service-appliance)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of service-appliance in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of service-appliance as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of service-appliance's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of service-appliance's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def service_appliance_user_credentials(self):
        """Get service-appliance-user-credentials for service-appliance.
        
        :returns: UserCredentials object
        
        """
        return getattr(self, '_service_appliance_user_credentials', None)
    #end service_appliance_user_credentials

    @service_appliance_user_credentials.setter
    def service_appliance_user_credentials(self, service_appliance_user_credentials):
        """Set service-appliance-user-credentials for service-appliance.
        
        :param service_appliance_user_credentials: UserCredentials object
        
        """
        self._service_appliance_user_credentials = service_appliance_user_credentials
    #end service_appliance_user_credentials

    def set_service_appliance_user_credentials(self, value):
        self.service_appliance_user_credentials = value
    #end set_service_appliance_user_credentials

    def get_service_appliance_user_credentials(self):
        return self.service_appliance_user_credentials
    #end get_service_appliance_user_credentials

    @property
    def service_appliance_ip_address(self):
        """Get service-appliance-ip-address for service-appliance.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_service_appliance_ip_address', None)
    #end service_appliance_ip_address

    @service_appliance_ip_address.setter
    def service_appliance_ip_address(self, service_appliance_ip_address):
        """Set service-appliance-ip-address for service-appliance.
        
        :param service_appliance_ip_address: IpAddressType object
        
        """
        self._service_appliance_ip_address = service_appliance_ip_address
    #end service_appliance_ip_address

    def set_service_appliance_ip_address(self, value):
        self.service_appliance_ip_address = value
    #end set_service_appliance_ip_address

    def get_service_appliance_ip_address(self):
        return self.service_appliance_ip_address
    #end get_service_appliance_ip_address

    @property
    def service_appliance_properties(self):
        """Get service-appliance-properties for service-appliance.
        
        :returns: KeyValuePairs object
        
        """
        return getattr(self, '_service_appliance_properties', None)
    #end service_appliance_properties

    @service_appliance_properties.setter
    def service_appliance_properties(self, service_appliance_properties):
        """Set service-appliance-properties for service-appliance.
        
        :param service_appliance_properties: KeyValuePairs object
        
        """
        self._service_appliance_properties = service_appliance_properties
    #end service_appliance_properties

    def set_service_appliance_properties(self, value):
        self.service_appliance_properties = value
    #end set_service_appliance_properties

    def get_service_appliance_properties(self):
        return self.service_appliance_properties
    #end get_service_appliance_properties

    @property
    def id_perms(self):
        """Get id-perms for service-appliance.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-appliance.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for service-appliance.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-appliance.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_service_appliance_user_credentials'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_user_credentials')
        if hasattr(self, '_service_appliance_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_ip_address')
        if hasattr(self, '_service_appliance_properties'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_service_appliance_set_back_refs(self):
        """Return list of all service-appliance-sets using this service-appliance"""
        return getattr(self, 'service_appliance_set_back_refs', None)
    #end get_service_appliance_set_back_refs

    def dump(self):
        """Display service-appliance object in compact form."""
        print '------------ service-appliance ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_appliance_user_credentials = ', self.get_service_appliance_user_credentials()
        print 'P service_appliance_ip_address = ', self.get_service_appliance_ip_address()
        print 'P service_appliance_properties = ', self.get_service_appliance_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class ServiceAppliance

class ServiceInstance(object):
    """
    Represents service-instance configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * service-instance-properties (:class:`.ServiceInstanceType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.ServiceTemplate` objects

    Referred by:
        * list of :class:`.VirtualMachine` objects
        * list of :class:`.LogicalRouter` objects
        * list of :class:`.LoadbalancerPool` objects
    """

    prop_fields = set([u'service_instance_properties', u'id_perms', u'display_name'])
    ref_fields = set(['service_template_refs'])
    backref_fields = set([u'project_back_refs', u'virtual_machine_back_refs', u'logical_router_back_refs', u'loadbalancer_pool_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, service_instance_properties = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'service-instance'
        if not name:
            name = u'default-service-instance'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if service_instance_properties:
            self._service_instance_properties = service_instance_properties
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (service-instance)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of service-instance in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of service-instance as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of service-instance's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of service-instance's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def service_instance_properties(self):
        """Get service-instance-properties for service-instance.
        
        :returns: ServiceInstanceType object
        
        """
        return getattr(self, '_service_instance_properties', None)
    #end service_instance_properties

    @service_instance_properties.setter
    def service_instance_properties(self, service_instance_properties):
        """Set service-instance-properties for service-instance.
        
        :param service_instance_properties: ServiceInstanceType object
        
        """
        self._service_instance_properties = service_instance_properties
    #end service_instance_properties

    def set_service_instance_properties(self, value):
        self.service_instance_properties = value
    #end set_service_instance_properties

    def get_service_instance_properties(self):
        return self.service_instance_properties
    #end get_service_instance_properties

    @property
    def id_perms(self):
        """Get id-perms for service-instance.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-instance.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for service-instance.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-instance.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_service_instance_properties'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_template_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_template_refs')
        return serialized
    #end serialize_to_json

    def set_service_template(self, ref_obj):
        """Set service-template for service-instance.
        
        :param ref_obj: ServiceTemplate object
        
        """
        self.service_template_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_template_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_template

    def add_service_template(self, ref_obj):
        """Add service-template to service-instance.
        
        :param ref_obj: ServiceTemplate object
        
        """
        refs = getattr(self, 'service_template_refs', [])
        if not refs:
            self.service_template_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.service_template_refs.append(ref_info)
    #end add_service_template

    def del_service_template(self, ref_obj):
        refs = self.get_service_template_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.service_template_refs.remove(ref)
                return
    #end del_service_template

    def set_service_template_list(self, ref_obj_list):
        """Set service-template list for service-instance.
        
        :param ref_obj_list: list of ServiceTemplate object
        
        """
        self.service_template_refs = ref_obj_list
    #end set_service_template_list

    def get_service_template_refs(self):
        """Return service-template list for service-instance.
        
        :returns: list of <ServiceTemplate>
        
        """
        return getattr(self, 'service_template_refs', None)
    #end get_service_template_refs

    def get_project_back_refs(self):
        """Return list of all projects using this service-instance"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_machine_back_refs(self):
        """Return list of all virtual-machines using this service-instance"""
        return getattr(self, 'virtual_machine_back_refs', None)
    #end get_virtual_machine_back_refs

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this service-instance"""
        return getattr(self, 'logical_router_back_refs', None)
    #end get_logical_router_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this service-instance"""
        return getattr(self, 'loadbalancer_pool_back_refs', None)
    #end get_loadbalancer_pool_back_refs

    def dump(self):
        """Display service-instance object in compact form."""
        print '------------ service-instance ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_instance_properties = ', self.get_service_instance_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_template = ', self.get_service_template_refs()
        print 'BCK virtual_machine = ', self.get_virtual_machine_back_refs()
        print 'BCK logical_router = ', self.get_logical_router_back_refs()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
    #end dump

#end class ServiceInstance

class Namespace(object):
    """
    Represents namespace configuration representation.

    Child of:
        :class:`.Domain` object OR

    Properties:
        * namespace-cidr (:class:`.SubnetType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.Project` objects
    """

    prop_fields = set([u'namespace_cidr', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'domain_back_refs', u'project_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, namespace_cidr = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'namespace'
        if not name:
            name = u'default-namespace'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'domain'
            self.fq_name = [u'default-domain']
            self.fq_name.append(name)


        # property fields
        if namespace_cidr:
            self._namespace_cidr = namespace_cidr
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (namespace)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of namespace in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of namespace as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of namespace's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of namespace's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def namespace_cidr(self):
        """Get namespace-cidr for namespace.
        
        :returns: SubnetType object
        
        """
        return getattr(self, '_namespace_cidr', None)
    #end namespace_cidr

    @namespace_cidr.setter
    def namespace_cidr(self, namespace_cidr):
        """Set namespace-cidr for namespace.
        
        :param namespace_cidr: SubnetType object
        
        """
        self._namespace_cidr = namespace_cidr
    #end namespace_cidr

    def set_namespace_cidr(self, value):
        self.namespace_cidr = value
    #end set_namespace_cidr

    def get_namespace_cidr(self):
        return self.namespace_cidr
    #end get_namespace_cidr

    @property
    def id_perms(self):
        """Get id-perms for namespace.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for namespace.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for namespace.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for namespace.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_namespace_cidr'):
            self._serialize_field_to_json(serialized, field_names, 'namespace_cidr')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_domain_back_refs(self):
        """Return list of all domains using this namespace"""
        return getattr(self, 'domain_back_refs', None)
    #end get_domain_back_refs

    def get_project_back_refs(self):
        """Return list of all projects using this namespace"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def dump(self):
        """Display namespace object in compact form."""
        print '------------ namespace ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P namespace_cidr = ', self.get_namespace_cidr()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK project = ', self.get_project_back_refs()
    #end dump

#end class Namespace

class LogicalInterface(object):
    """
    Represents logical-interface configuration representation.

    Child of:
        :class:`.PhysicalRouter` object OR
        :class:`.PhysicalInterface` object OR

    Properties:
        * logical-interface-vlan-tag (xsd:integer type)
        * logical-interface-type (LogicalInterfaceType type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects

    Referred by:
    """

    prop_fields = set([u'logical_interface_vlan_tag', u'logical_interface_type', u'id_perms', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs'])
    backref_fields = set([u'physical_router_back_refs', u'physical_interface_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, logical_interface_vlan_tag = None, logical_interface_type = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'logical-interface'
        if not name:
            name = u'default-logical-interface'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            # if obj constructed from within server, ignore if parent not specified
            if not kwargs['parent_type']:
                raise AmbiguousParentError("[[u'default-global-system-config', u'default-physical-router'], [u'default-global-system-config', u'default-physical-router', u'default-physical-interface']]")

        # property fields
        if logical_interface_vlan_tag:
            self._logical_interface_vlan_tag = logical_interface_vlan_tag
        if logical_interface_type:
            self._logical_interface_type = logical_interface_type
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (logical-interface)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of logical-interface in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of logical-interface as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of logical-interface's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of logical-interface's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def logical_interface_vlan_tag(self):
        """Get logical-interface-vlan-tag for logical-interface.
        
        :returns: xsd:integer object
        
        """
        return getattr(self, '_logical_interface_vlan_tag', None)
    #end logical_interface_vlan_tag

    @logical_interface_vlan_tag.setter
    def logical_interface_vlan_tag(self, logical_interface_vlan_tag):
        """Set logical-interface-vlan-tag for logical-interface.
        
        :param logical_interface_vlan_tag: xsd:integer object
        
        """
        self._logical_interface_vlan_tag = logical_interface_vlan_tag
    #end logical_interface_vlan_tag

    def set_logical_interface_vlan_tag(self, value):
        self.logical_interface_vlan_tag = value
    #end set_logical_interface_vlan_tag

    def get_logical_interface_vlan_tag(self):
        return self.logical_interface_vlan_tag
    #end get_logical_interface_vlan_tag

    @property
    def logical_interface_type(self):
        """Get logical-interface-type for logical-interface.
        
        :returns: LogicalInterfaceType object
        
        """
        return getattr(self, '_logical_interface_type', None)
    #end logical_interface_type

    @logical_interface_type.setter
    def logical_interface_type(self, logical_interface_type):
        """Set logical-interface-type for logical-interface.
        
        :param logical_interface_type: LogicalInterfaceType object
        
        """
        self._logical_interface_type = logical_interface_type
    #end logical_interface_type

    def set_logical_interface_type(self, value):
        self.logical_interface_type = value
    #end set_logical_interface_type

    def get_logical_interface_type(self):
        return self.logical_interface_type
    #end get_logical_interface_type

    @property
    def id_perms(self):
        """Get id-perms for logical-interface.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for logical-interface.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for logical-interface.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for logical-interface.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_logical_interface_vlan_tag'):
            self._serialize_field_to_json(serialized, field_names, 'logical_interface_vlan_tag')
        if hasattr(self, '_logical_interface_type'):
            self._serialize_field_to_json(serialized, field_names, 'logical_interface_type')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for logical-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to logical-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for logical-interface.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for logical-interface.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this logical-interface"""
        return getattr(self, 'physical_router_back_refs', None)
    #end get_physical_router_back_refs

    def get_physical_interface_back_refs(self):
        """Return list of all physical-interfaces using this logical-interface"""
        return getattr(self, 'physical_interface_back_refs', None)
    #end get_physical_interface_back_refs

    def dump(self):
        """Display logical-interface object in compact form."""
        print '------------ logical-interface ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P logical_interface_vlan_tag = ', self.get_logical_interface_vlan_tag()
        print 'P logical_interface_type = ', self.get_logical_interface_type()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
    #end dump

#end class LogicalInterface

class RouteTable(object):
    """
    Represents route-table configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * routes (:class:`.RouteTableType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.VirtualNetwork` objects
    """

    prop_fields = set([u'routes', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs', u'virtual_network_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, routes = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'route-table'
        if not name:
            name = u'default-route-table'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if routes:
            self._routes = routes
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (route-table)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of route-table in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of route-table as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of route-table's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of route-table's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def routes(self):
        """Get routes for route-table.
        
        :returns: RouteTableType object
        
        """
        return getattr(self, '_routes', None)
    #end routes

    @routes.setter
    def routes(self, routes):
        """Set routes for route-table.
        
        :param routes: RouteTableType object
        
        """
        self._routes = routes
    #end routes

    def set_routes(self, value):
        self.routes = value
    #end set_routes

    def get_routes(self):
        return self.routes
    #end get_routes

    @property
    def id_perms(self):
        """Get id-perms for route-table.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for route-table.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for route-table.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for route-table.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_routes'):
            self._serialize_field_to_json(serialized, field_names, 'routes')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_project_back_refs(self):
        """Return list of all projects using this route-table"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this route-table"""
        return getattr(self, 'virtual_network_back_refs', None)
    #end get_virtual_network_back_refs

    def dump(self):
        """Display route-table object in compact form."""
        print '------------ route-table ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P routes = ', self.get_routes()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK virtual_network = ', self.get_virtual_network_back_refs()
    #end dump

#end class RouteTable

class PhysicalInterface(object):
    """
    Represents physical-interface configuration representation.

    Child of:
        :class:`.PhysicalRouter` object OR

    Properties:
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.LogicalInterface` objects

    References to:

    Referred by:
    """

    prop_fields = set([u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'physical_router_back_refs'])
    children_fields = set([u'logical_interfaces'])

    def __init__(self, name = None, parent_obj = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'physical-interface'
        if not name:
            name = u'default-physical-interface'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'physical-router'
            self.fq_name = [u'default-global-system-config', u'default-physical-router']
            self.fq_name.append(name)


        # property fields
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (physical-interface)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of physical-interface in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of physical-interface as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of physical-interface's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of physical-interface's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def id_perms(self):
        """Get id-perms for physical-interface.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for physical-interface.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for physical-interface.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for physical-interface.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_logical_interfaces(self):
        return getattr(self, 'logical_interfaces', None)
    #end get_logical_interfaces

    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this physical-interface"""
        return getattr(self, 'physical_router_back_refs', None)
    #end get_physical_router_back_refs

    def dump(self):
        """Display physical-interface object in compact form."""
        print '------------ physical-interface ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS logical_interface = ', self.get_logical_interfaces()
    #end dump

#end class PhysicalInterface

class AccessControlList(object):
    """
    Represents access-control-list configuration representation.

    Child of:
        :class:`.VirtualNetwork` object OR
        :class:`.SecurityGroup` object OR

    Properties:
        * access-control-list-entries (:class:`.AclEntriesType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'access_control_list_entries', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'virtual_network_back_refs', u'security_group_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, access_control_list_entries = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'access-control-list'
        if not name:
            name = u'default-access-control-list'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            # if obj constructed from within server, ignore if parent not specified
            if not kwargs['parent_type']:
                raise AmbiguousParentError("[[u'default-domain', u'default-project', u'default-virtual-network'], [u'default-domain', u'default-project', u'default-security-group']]")

        # property fields
        if access_control_list_entries:
            self._access_control_list_entries = access_control_list_entries
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (access-control-list)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of access-control-list in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of access-control-list as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of access-control-list's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of access-control-list's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def access_control_list_entries(self):
        """Get access-control-list-entries for access-control-list.
        
        :returns: AclEntriesType object
        
        """
        return getattr(self, '_access_control_list_entries', None)
    #end access_control_list_entries

    @access_control_list_entries.setter
    def access_control_list_entries(self, access_control_list_entries):
        """Set access-control-list-entries for access-control-list.
        
        :param access_control_list_entries: AclEntriesType object
        
        """
        self._access_control_list_entries = access_control_list_entries
    #end access_control_list_entries

    def set_access_control_list_entries(self, value):
        self.access_control_list_entries = value
    #end set_access_control_list_entries

    def get_access_control_list_entries(self):
        return self.access_control_list_entries
    #end get_access_control_list_entries

    @property
    def id_perms(self):
        """Get id-perms for access-control-list.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for access-control-list.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for access-control-list.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for access-control-list.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_access_control_list_entries'):
            self._serialize_field_to_json(serialized, field_names, 'access_control_list_entries')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this access-control-list"""
        return getattr(self, 'virtual_network_back_refs', None)
    #end get_virtual_network_back_refs

    def get_security_group_back_refs(self):
        """Return list of all security-groups using this access-control-list"""
        return getattr(self, 'security_group_back_refs', None)
    #end get_security_group_back_refs

    def dump(self):
        """Display access-control-list object in compact form."""
        print '------------ access-control-list ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P access_control_list_entries = ', self.get_access_control_list_entries()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class AccessControlList

class AnalyticsNode(object):
    """
    Represents analytics-node configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * analytics-node-ip-address (IpAddressType type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'analytics_node_ip_address', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'global_system_config_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, analytics_node_ip_address = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'analytics-node'
        if not name:
            name = u'default-analytics-node'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'global-system-config'
            self.fq_name = [u'default-global-system-config']
            self.fq_name.append(name)


        # property fields
        if analytics_node_ip_address:
            self._analytics_node_ip_address = analytics_node_ip_address
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (analytics-node)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of analytics-node in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of analytics-node as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of analytics-node's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of analytics-node's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def analytics_node_ip_address(self):
        """Get analytics-node-ip-address for analytics-node.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_analytics_node_ip_address', None)
    #end analytics_node_ip_address

    @analytics_node_ip_address.setter
    def analytics_node_ip_address(self, analytics_node_ip_address):
        """Set analytics-node-ip-address for analytics-node.
        
        :param analytics_node_ip_address: IpAddressType object
        
        """
        self._analytics_node_ip_address = analytics_node_ip_address
    #end analytics_node_ip_address

    def set_analytics_node_ip_address(self, value):
        self.analytics_node_ip_address = value
    #end set_analytics_node_ip_address

    def get_analytics_node_ip_address(self):
        return self.analytics_node_ip_address
    #end get_analytics_node_ip_address

    @property
    def id_perms(self):
        """Get id-perms for analytics-node.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for analytics-node.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for analytics-node.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for analytics-node.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_analytics_node_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'analytics_node_ip_address')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this analytics-node"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def dump(self):
        """Display analytics-node object in compact form."""
        print '------------ analytics-node ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P analytics_node_ip_address = ', self.get_analytics_node_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class AnalyticsNode

class VirtualDns(object):
    """
    Represents virtual-DNS configuration representation.

    Child of:
        :class:`.Domain` object OR

    Properties:
        * virtual-DNS-data (:class:`.VirtualDnsType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.VirtualDnsRecord` objects

    References to:

    Referred by:
        * list of :class:`.NetworkIpam` objects
    """

    prop_fields = set([u'virtual_DNS_data', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'domain_back_refs', u'network_ipam_back_refs'])
    children_fields = set([u'virtual_DNS_records'])

    def __init__(self, name = None, parent_obj = None, virtual_DNS_data = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-DNS'
        if not name:
            name = u'default-virtual-DNS'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'domain'
            self.fq_name = [u'default-domain']
            self.fq_name.append(name)


        # property fields
        if virtual_DNS_data:
            self._virtual_DNS_data = virtual_DNS_data
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (virtual-DNS)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of virtual-DNS in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of virtual-DNS as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of virtual-DNS's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of virtual-DNS's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def virtual_DNS_data(self):
        """Get virtual-DNS-data for virtual-DNS.
        
        :returns: VirtualDnsType object
        
        """
        return getattr(self, '_virtual_DNS_data', None)
    #end virtual_DNS_data

    @virtual_DNS_data.setter
    def virtual_DNS_data(self, virtual_DNS_data):
        """Set virtual-DNS-data for virtual-DNS.
        
        :param virtual_DNS_data: VirtualDnsType object
        
        """
        self._virtual_DNS_data = virtual_DNS_data
    #end virtual_DNS_data

    def set_virtual_DNS_data(self, value):
        self.virtual_DNS_data = value
    #end set_virtual_DNS_data

    def get_virtual_DNS_data(self):
        return self.virtual_DNS_data
    #end get_virtual_DNS_data

    @property
    def id_perms(self):
        """Get id-perms for virtual-DNS.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-DNS.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for virtual-DNS.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-DNS.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_virtual_DNS_data'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_DNS_data')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_virtual_DNS_records(self):
        return getattr(self, 'virtual_DNS_records', None)
    #end get_virtual_DNS_records

    def get_domain_back_refs(self):
        """Return list of all domains using this virtual-DNS"""
        return getattr(self, 'domain_back_refs', None)
    #end get_domain_back_refs

    def get_network_ipam_back_refs(self):
        """Return list of all network-ipams using this virtual-DNS"""
        return getattr(self, 'network_ipam_back_refs', None)
    #end get_network_ipam_back_refs

    def dump(self):
        """Display virtual-DNS object in compact form."""
        print '------------ virtual-DNS ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_DNS_data = ', self.get_virtual_DNS_data()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS virtual_DNS_record = ', self.get_virtual_DNS_records()
        print 'BCK network_ipam = ', self.get_network_ipam_back_refs()
    #end dump

#end class VirtualDns

class CustomerAttachment(object):
    """
    Represents customer-attachment configuration representation.

    Properties:
        * attachment-address (:class:`.AttachmentAddressType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.FloatingIp` objects

    Referred by:
    """

    prop_fields = set([u'attachment_address', u'id_perms', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs', u'floating_ip_refs'])
    backref_fields = set([])
    children_fields = set([])

    def __init__(self, name = None, attachment_address = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'customer-attachment'
        if not name:
            name = u'default-customer-attachment'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if attachment_address:
            self._attachment_address = attachment_address
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (customer-attachment)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of customer-attachment in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of customer-attachment as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def attachment_address(self):
        """Get attachment-address for customer-attachment.
        
        :returns: AttachmentAddressType object
        
        """
        return getattr(self, '_attachment_address', None)
    #end attachment_address

    @attachment_address.setter
    def attachment_address(self, attachment_address):
        """Set attachment-address for customer-attachment.
        
        :param attachment_address: AttachmentAddressType object
        
        """
        self._attachment_address = attachment_address
    #end attachment_address

    def set_attachment_address(self, value):
        self.attachment_address = value
    #end set_attachment_address

    def get_attachment_address(self):
        return self.attachment_address
    #end get_attachment_address

    @property
    def id_perms(self):
        """Get id-perms for customer-attachment.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for customer-attachment.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for customer-attachment.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for customer-attachment.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_attachment_address'):
            self._serialize_field_to_json(serialized, field_names, 'attachment_address')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        if hasattr(self, 'floating_ip_refs'):
            self._serialize_field_to_json(serialized, field_names, 'floating_ip_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for customer-attachment.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to customer-attachment.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for customer-attachment.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for customer-attachment.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def set_floating_ip(self, ref_obj):
        """Set floating-ip for customer-attachment.
        
        :param ref_obj: FloatingIp object
        
        """
        self.floating_ip_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.floating_ip_refs[0]['uuid'] = ref_obj.uuid

    #end set_floating_ip

    def add_floating_ip(self, ref_obj):
        """Add floating-ip to customer-attachment.
        
        :param ref_obj: FloatingIp object
        
        """
        refs = getattr(self, 'floating_ip_refs', [])
        if not refs:
            self.floating_ip_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.floating_ip_refs.append(ref_info)
    #end add_floating_ip

    def del_floating_ip(self, ref_obj):
        refs = self.get_floating_ip_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.floating_ip_refs.remove(ref)
                return
    #end del_floating_ip

    def set_floating_ip_list(self, ref_obj_list):
        """Set floating-ip list for customer-attachment.
        
        :param ref_obj_list: list of FloatingIp object
        
        """
        self.floating_ip_refs = ref_obj_list
    #end set_floating_ip_list

    def get_floating_ip_refs(self):
        """Return floating-ip list for customer-attachment.
        
        :returns: list of <FloatingIp>
        
        """
        return getattr(self, 'floating_ip_refs', None)
    #end get_floating_ip_refs

    def dump(self):
        """Display customer-attachment object in compact form."""
        print '------------ customer-attachment ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P attachment_address = ', self.get_attachment_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF floating_ip = ', self.get_floating_ip_refs()
        print 'HAS routing_instance = ', self.get_routing_instances()
        print 'HAS provider_attachment = ', self.get_provider_attachments()
    #end dump

#end class CustomerAttachment

class ServiceApplianceSet(object):
    """
    Represents service-appliance-set configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * service-appliance-set-properties (:class:`.KeyValuePairs` type)
        * service-appliance-driver (xsd:string type)
        * service-appliance-ha-mode (xsd:string type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.ServiceAppliance` objects

    References to:

    Referred by:
        * list of :class:`.LoadbalancerPool` objects
    """

    prop_fields = set([u'service_appliance_set_properties', u'service_appliance_driver', u'service_appliance_ha_mode', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'global_system_config_back_refs', u'loadbalancer_pool_back_refs'])
    children_fields = set([u'service_appliances'])

    def __init__(self, name = None, parent_obj = None, service_appliance_set_properties = None, service_appliance_driver = None, service_appliance_ha_mode = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'service-appliance-set'
        if not name:
            name = u'default-service-appliance-set'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'global-system-config'
            self.fq_name = [u'default-global-system-config']
            self.fq_name.append(name)


        # property fields
        if service_appliance_set_properties:
            self._service_appliance_set_properties = service_appliance_set_properties
        if service_appliance_driver:
            self._service_appliance_driver = service_appliance_driver
        if service_appliance_ha_mode:
            self._service_appliance_ha_mode = service_appliance_ha_mode
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (service-appliance-set)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of service-appliance-set in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of service-appliance-set as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of service-appliance-set's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of service-appliance-set's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def service_appliance_set_properties(self):
        """Get service-appliance-set-properties for service-appliance-set.
        
        :returns: KeyValuePairs object
        
        """
        return getattr(self, '_service_appliance_set_properties', None)
    #end service_appliance_set_properties

    @service_appliance_set_properties.setter
    def service_appliance_set_properties(self, service_appliance_set_properties):
        """Set service-appliance-set-properties for service-appliance-set.
        
        :param service_appliance_set_properties: KeyValuePairs object
        
        """
        self._service_appliance_set_properties = service_appliance_set_properties
    #end service_appliance_set_properties

    def set_service_appliance_set_properties(self, value):
        self.service_appliance_set_properties = value
    #end set_service_appliance_set_properties

    def get_service_appliance_set_properties(self):
        return self.service_appliance_set_properties
    #end get_service_appliance_set_properties

    @property
    def service_appliance_driver(self):
        """Get service-appliance-driver for service-appliance-set.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_service_appliance_driver', None)
    #end service_appliance_driver

    @service_appliance_driver.setter
    def service_appliance_driver(self, service_appliance_driver):
        """Set service-appliance-driver for service-appliance-set.
        
        :param service_appliance_driver: xsd:string object
        
        """
        self._service_appliance_driver = service_appliance_driver
    #end service_appliance_driver

    def set_service_appliance_driver(self, value):
        self.service_appliance_driver = value
    #end set_service_appliance_driver

    def get_service_appliance_driver(self):
        return self.service_appliance_driver
    #end get_service_appliance_driver

    @property
    def service_appliance_ha_mode(self):
        """Get service-appliance-ha-mode for service-appliance-set.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_service_appliance_ha_mode', None)
    #end service_appliance_ha_mode

    @service_appliance_ha_mode.setter
    def service_appliance_ha_mode(self, service_appliance_ha_mode):
        """Set service-appliance-ha-mode for service-appliance-set.
        
        :param service_appliance_ha_mode: xsd:string object
        
        """
        self._service_appliance_ha_mode = service_appliance_ha_mode
    #end service_appliance_ha_mode

    def set_service_appliance_ha_mode(self, value):
        self.service_appliance_ha_mode = value
    #end set_service_appliance_ha_mode

    def get_service_appliance_ha_mode(self):
        return self.service_appliance_ha_mode
    #end get_service_appliance_ha_mode

    @property
    def id_perms(self):
        """Get id-perms for service-appliance-set.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-appliance-set.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for service-appliance-set.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-appliance-set.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_service_appliance_set_properties'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_set_properties')
        if hasattr(self, '_service_appliance_driver'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_driver')
        if hasattr(self, '_service_appliance_ha_mode'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_ha_mode')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_service_appliances(self):
        return getattr(self, 'service_appliances', None)
    #end get_service_appliances

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this service-appliance-set"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this service-appliance-set"""
        return getattr(self, 'loadbalancer_pool_back_refs', None)
    #end get_loadbalancer_pool_back_refs

    def dump(self):
        """Display service-appliance-set object in compact form."""
        print '------------ service-appliance-set ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_appliance_set_properties = ', self.get_service_appliance_set_properties()
        print 'P service_appliance_driver = ', self.get_service_appliance_driver()
        print 'P service_appliance_ha_mode = ', self.get_service_appliance_ha_mode()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS service_appliance = ', self.get_service_appliances()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
    #end dump

#end class ServiceApplianceSet

class ConfigNode(object):
    """
    Represents config-node configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * config-node-ip-address (IpAddressType type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'config_node_ip_address', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'global_system_config_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, config_node_ip_address = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'config-node'
        if not name:
            name = u'default-config-node'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'global-system-config'
            self.fq_name = [u'default-global-system-config']
            self.fq_name.append(name)


        # property fields
        if config_node_ip_address:
            self._config_node_ip_address = config_node_ip_address
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (config-node)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of config-node in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of config-node as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of config-node's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of config-node's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def config_node_ip_address(self):
        """Get config-node-ip-address for config-node.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_config_node_ip_address', None)
    #end config_node_ip_address

    @config_node_ip_address.setter
    def config_node_ip_address(self, config_node_ip_address):
        """Set config-node-ip-address for config-node.
        
        :param config_node_ip_address: IpAddressType object
        
        """
        self._config_node_ip_address = config_node_ip_address
    #end config_node_ip_address

    def set_config_node_ip_address(self, value):
        self.config_node_ip_address = value
    #end set_config_node_ip_address

    def get_config_node_ip_address(self):
        return self.config_node_ip_address
    #end get_config_node_ip_address

    @property
    def id_perms(self):
        """Get id-perms for config-node.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for config-node.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for config-node.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for config-node.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_config_node_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'config_node_ip_address')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this config-node"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def dump(self):
        """Display config-node object in compact form."""
        print '------------ config-node ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P config_node_ip_address = ', self.get_config_node_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class ConfigNode

class QosQueue(object):
    """
    Represents qos-queue configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * min-bandwidth (xsd:integer type)
        * max-bandwidth (xsd:integer type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.QosForwardingClass` objects
    """

    prop_fields = set([u'min_bandwidth', u'max_bandwidth', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs', u'qos_forwarding_class_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, min_bandwidth = None, max_bandwidth = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'qos-queue'
        if not name:
            name = u'default-qos-queue'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if min_bandwidth:
            self._min_bandwidth = min_bandwidth
        if max_bandwidth:
            self._max_bandwidth = max_bandwidth
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (qos-queue)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of qos-queue in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of qos-queue as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of qos-queue's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of qos-queue's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def min_bandwidth(self):
        """Get min-bandwidth for qos-queue.
        
        :returns: xsd:integer object
        
        """
        return getattr(self, '_min_bandwidth', None)
    #end min_bandwidth

    @min_bandwidth.setter
    def min_bandwidth(self, min_bandwidth):
        """Set min-bandwidth for qos-queue.
        
        :param min_bandwidth: xsd:integer object
        
        """
        self._min_bandwidth = min_bandwidth
    #end min_bandwidth

    def set_min_bandwidth(self, value):
        self.min_bandwidth = value
    #end set_min_bandwidth

    def get_min_bandwidth(self):
        return self.min_bandwidth
    #end get_min_bandwidth

    @property
    def max_bandwidth(self):
        """Get max-bandwidth for qos-queue.
        
        :returns: xsd:integer object
        
        """
        return getattr(self, '_max_bandwidth', None)
    #end max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Set max-bandwidth for qos-queue.
        
        :param max_bandwidth: xsd:integer object
        
        """
        self._max_bandwidth = max_bandwidth
    #end max_bandwidth

    def set_max_bandwidth(self, value):
        self.max_bandwidth = value
    #end set_max_bandwidth

    def get_max_bandwidth(self):
        return self.max_bandwidth
    #end get_max_bandwidth

    @property
    def id_perms(self):
        """Get id-perms for qos-queue.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for qos-queue.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for qos-queue.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for qos-queue.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_min_bandwidth'):
            self._serialize_field_to_json(serialized, field_names, 'min_bandwidth')
        if hasattr(self, '_max_bandwidth'):
            self._serialize_field_to_json(serialized, field_names, 'max_bandwidth')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_project_back_refs(self):
        """Return list of all projects using this qos-queue"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_qos_forwarding_class_back_refs(self):
        """Return list of all qos-forwarding-classs using this qos-queue"""
        return getattr(self, 'qos_forwarding_class_back_refs', None)
    #end get_qos_forwarding_class_back_refs

    def dump(self):
        """Display qos-queue object in compact form."""
        print '------------ qos-queue ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P min_bandwidth = ', self.get_min_bandwidth()
        print 'P max_bandwidth = ', self.get_max_bandwidth()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK qos_forwarding_class = ', self.get_qos_forwarding_class_back_refs()
    #end dump

#end class QosQueue

class VirtualMachine(object):
    """
    Represents virtual-machine configuration representation.

    Properties:
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.VirtualMachineInterface` objects

    References to:
        * list of :class:`.ServiceInstance` objects

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.VirtualRouter` objects
    """

    prop_fields = set([u'id_perms', u'display_name'])
    ref_fields = set([u'service_instance_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs', 'virtual_router_back_refs'])
    children_fields = set(['virtual_machine_interfaces'])

    def __init__(self, name = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-machine'
        if not name:
            name = u'default-virtual-machine'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (virtual-machine)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of virtual-machine in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of virtual-machine as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def id_perms(self):
        """Get id-perms for virtual-machine.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-machine.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for virtual-machine.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-machine.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        return serialized
    #end serialize_to_json

    def get_virtual_machine_interfaces(self):
        return getattr(self, 'virtual_machine_interfaces', None)
    #end get_virtual_machine_interfaces

    def set_service_instance(self, ref_obj):
        """Set service-instance for virtual-machine.
        
        :param ref_obj: ServiceInstance object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj):
        """Add service-instance to virtual-machine.
        
        :param ref_obj: ServiceInstance object
        
        """
        refs = getattr(self, 'service_instance_refs', [])
        if not refs:
            self.service_instance_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.service_instance_refs.append(ref_info)
    #end add_service_instance

    def del_service_instance(self, ref_obj):
        refs = self.get_service_instance_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.service_instance_refs.remove(ref)
                return
    #end del_service_instance

    def set_service_instance_list(self, ref_obj_list):
        """Set service-instance list for virtual-machine.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self.service_instance_refs = ref_obj_list
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for virtual-machine.
        
        :returns: list of <ServiceInstance>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this virtual-machine"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def get_virtual_router_back_refs(self):
        """Return list of all virtual-routers using this virtual-machine"""
        return getattr(self, 'virtual_router_back_refs', None)
    #end get_virtual_router_back_refs

    def dump(self):
        """Display virtual-machine object in compact form."""
        print '------------ virtual-machine ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS virtual_machine_interface = ', self.get_virtual_machine_interfaces()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
        print 'BCK virtual_router = ', self.get_virtual_router_back_refs()
    #end dump

#end class VirtualMachine

class InterfaceRouteTable(object):
    """
    Represents interface-route-table configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * interface-route-table-routes (:class:`.RouteTableType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'interface_route_table_routes', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs', 'virtual_machine_interface_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, interface_route_table_routes = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'interface-route-table'
        if not name:
            name = u'default-interface-route-table'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if interface_route_table_routes:
            self._interface_route_table_routes = interface_route_table_routes
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (interface-route-table)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of interface-route-table in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of interface-route-table as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of interface-route-table's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of interface-route-table's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def interface_route_table_routes(self):
        """Get interface-route-table-routes for interface-route-table.
        
        :returns: RouteTableType object
        
        """
        return getattr(self, '_interface_route_table_routes', None)
    #end interface_route_table_routes

    @interface_route_table_routes.setter
    def interface_route_table_routes(self, interface_route_table_routes):
        """Set interface-route-table-routes for interface-route-table.
        
        :param interface_route_table_routes: RouteTableType object
        
        """
        self._interface_route_table_routes = interface_route_table_routes
    #end interface_route_table_routes

    def set_interface_route_table_routes(self, value):
        self.interface_route_table_routes = value
    #end set_interface_route_table_routes

    def get_interface_route_table_routes(self):
        return self.interface_route_table_routes
    #end get_interface_route_table_routes

    @property
    def id_perms(self):
        """Get id-perms for interface-route-table.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for interface-route-table.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for interface-route-table.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for interface-route-table.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_interface_route_table_routes'):
            self._serialize_field_to_json(serialized, field_names, 'interface_route_table_routes')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_project_back_refs(self):
        """Return list of all projects using this interface-route-table"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this interface-route-table"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def dump(self):
        """Display interface-route-table object in compact form."""
        print '------------ interface-route-table ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P interface_route_table_routes = ', self.get_interface_route_table_routes()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class InterfaceRouteTable

class ServiceTemplate(object):
    """
    Represents service-template configuration representation.

    Child of:
        :class:`.Domain` object OR

    Properties:
        * service-template-properties (:class:`.ServiceTemplateType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.ServiceInstance` objects
    """

    prop_fields = set([u'service_template_properties', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'domain_back_refs', u'service_instance_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, service_template_properties = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'service-template'
        if not name:
            name = u'default-service-template'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'domain'
            self.fq_name = [u'default-domain']
            self.fq_name.append(name)


        # property fields
        if service_template_properties:
            self._service_template_properties = service_template_properties
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (service-template)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of service-template in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of service-template as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of service-template's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of service-template's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def service_template_properties(self):
        """Get service-template-properties for service-template.
        
        :returns: ServiceTemplateType object
        
        """
        return getattr(self, '_service_template_properties', None)
    #end service_template_properties

    @service_template_properties.setter
    def service_template_properties(self, service_template_properties):
        """Set service-template-properties for service-template.
        
        :param service_template_properties: ServiceTemplateType object
        
        """
        self._service_template_properties = service_template_properties
    #end service_template_properties

    def set_service_template_properties(self, value):
        self.service_template_properties = value
    #end set_service_template_properties

    def get_service_template_properties(self):
        return self.service_template_properties
    #end get_service_template_properties

    @property
    def id_perms(self):
        """Get id-perms for service-template.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-template.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for service-template.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-template.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_service_template_properties'):
            self._serialize_field_to_json(serialized, field_names, 'service_template_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_domain_back_refs(self):
        """Return list of all domains using this service-template"""
        return getattr(self, 'domain_back_refs', None)
    #end get_domain_back_refs

    def get_service_instance_back_refs(self):
        """Return list of all service-instances using this service-template"""
        return getattr(self, 'service_instance_back_refs', None)
    #end get_service_instance_back_refs

    def dump(self):
        """Display service-template object in compact form."""
        print '------------ service-template ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_template_properties = ', self.get_service_template_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK service_instance = ', self.get_service_instance_back_refs()
    #end dump

#end class ServiceTemplate

class VirtualIp(object):
    """
    Represents virtual-ip configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * virtual-ip-properties (:class:`.VirtualIpType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.LoadbalancerPool` objects
        * list of :class:`.VirtualMachineInterface` objects

    Referred by:
    """

    prop_fields = set([u'virtual_ip_properties', u'id_perms', u'display_name'])
    ref_fields = set([u'loadbalancer_pool_refs', 'virtual_machine_interface_refs'])
    backref_fields = set([u'project_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, virtual_ip_properties = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-ip'
        if not name:
            name = u'default-virtual-ip'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if virtual_ip_properties:
            self._virtual_ip_properties = virtual_ip_properties
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (virtual-ip)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of virtual-ip in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of virtual-ip as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of virtual-ip's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of virtual-ip's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def virtual_ip_properties(self):
        """Get virtual-ip-properties for virtual-ip.
        
        :returns: VirtualIpType object
        
        """
        return getattr(self, '_virtual_ip_properties', None)
    #end virtual_ip_properties

    @virtual_ip_properties.setter
    def virtual_ip_properties(self, virtual_ip_properties):
        """Set virtual-ip-properties for virtual-ip.
        
        :param virtual_ip_properties: VirtualIpType object
        
        """
        self._virtual_ip_properties = virtual_ip_properties
    #end virtual_ip_properties

    def set_virtual_ip_properties(self, value):
        self.virtual_ip_properties = value
    #end set_virtual_ip_properties

    def get_virtual_ip_properties(self):
        return self.virtual_ip_properties
    #end get_virtual_ip_properties

    @property
    def id_perms(self):
        """Get id-perms for virtual-ip.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-ip.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for virtual-ip.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-ip.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_virtual_ip_properties'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_ip_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'loadbalancer_pool_refs'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_pool_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        return serialized
    #end serialize_to_json

    def set_loadbalancer_pool(self, ref_obj):
        """Set loadbalancer-pool for virtual-ip.
        
        :param ref_obj: LoadbalancerPool object
        
        """
        self.loadbalancer_pool_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.loadbalancer_pool_refs[0]['uuid'] = ref_obj.uuid

    #end set_loadbalancer_pool

    def add_loadbalancer_pool(self, ref_obj):
        """Add loadbalancer-pool to virtual-ip.
        
        :param ref_obj: LoadbalancerPool object
        
        """
        refs = getattr(self, 'loadbalancer_pool_refs', [])
        if not refs:
            self.loadbalancer_pool_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.loadbalancer_pool_refs.append(ref_info)
    #end add_loadbalancer_pool

    def del_loadbalancer_pool(self, ref_obj):
        refs = self.get_loadbalancer_pool_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.loadbalancer_pool_refs.remove(ref)
                return
    #end del_loadbalancer_pool

    def set_loadbalancer_pool_list(self, ref_obj_list):
        """Set loadbalancer-pool list for virtual-ip.
        
        :param ref_obj_list: list of LoadbalancerPool object
        
        """
        self.loadbalancer_pool_refs = ref_obj_list
    #end set_loadbalancer_pool_list

    def get_loadbalancer_pool_refs(self):
        """Return loadbalancer-pool list for virtual-ip.
        
        :returns: list of <LoadbalancerPool>
        
        """
        return getattr(self, 'loadbalancer_pool_refs', None)
    #end get_loadbalancer_pool_refs

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for virtual-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to virtual-ip.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for virtual-ip.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for virtual-ip.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def get_project_back_refs(self):
        """Return list of all projects using this virtual-ip"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def dump(self):
        """Display virtual-ip object in compact form."""
        print '------------ virtual-ip ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_ip_properties = ', self.get_virtual_ip_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF loadbalancer_pool = ', self.get_loadbalancer_pool_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
    #end dump

#end class VirtualIp

class LoadbalancerMember(object):
    """
    Represents loadbalancer-member configuration representation.

    Child of:
        :class:`.LoadbalancerPool` object OR

    Properties:
        * loadbalancer-member-properties (:class:`.LoadbalancerMemberType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'loadbalancer_member_properties', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'loadbalancer_pool_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, loadbalancer_member_properties = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'loadbalancer-member'
        if not name:
            name = u'default-loadbalancer-member'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'loadbalancer-pool'
            self.fq_name = [u'default-domain', u'default-project', u'default-loadbalancer-pool']
            self.fq_name.append(name)


        # property fields
        if loadbalancer_member_properties:
            self._loadbalancer_member_properties = loadbalancer_member_properties
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (loadbalancer-member)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of loadbalancer-member in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of loadbalancer-member as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of loadbalancer-member's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of loadbalancer-member's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def loadbalancer_member_properties(self):
        """Get loadbalancer-member-properties for loadbalancer-member.
        
        :returns: LoadbalancerMemberType object
        
        """
        return getattr(self, '_loadbalancer_member_properties', None)
    #end loadbalancer_member_properties

    @loadbalancer_member_properties.setter
    def loadbalancer_member_properties(self, loadbalancer_member_properties):
        """Set loadbalancer-member-properties for loadbalancer-member.
        
        :param loadbalancer_member_properties: LoadbalancerMemberType object
        
        """
        self._loadbalancer_member_properties = loadbalancer_member_properties
    #end loadbalancer_member_properties

    def set_loadbalancer_member_properties(self, value):
        self.loadbalancer_member_properties = value
    #end set_loadbalancer_member_properties

    def get_loadbalancer_member_properties(self):
        return self.loadbalancer_member_properties
    #end get_loadbalancer_member_properties

    @property
    def id_perms(self):
        """Get id-perms for loadbalancer-member.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-member.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for loadbalancer-member.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-member.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_loadbalancer_member_properties'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_member_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this loadbalancer-member"""
        return getattr(self, 'loadbalancer_pool_back_refs', None)
    #end get_loadbalancer_pool_back_refs

    def dump(self):
        """Display loadbalancer-member object in compact form."""
        print '------------ loadbalancer-member ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P loadbalancer_member_properties = ', self.get_loadbalancer_member_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class LoadbalancerMember

class SecurityGroup(object):
    """
    Represents security-group configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * security-group-id (xsd:string type)
        * configured-security-group-id (xsd:integer type)
        * security-group-entries (:class:`.PolicyEntriesType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.AccessControlList` objects

    References to:

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'security_group_id', u'configured_security_group_id', u'security_group_entries', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs', 'virtual_machine_interface_back_refs'])
    children_fields = set([u'access_control_lists'])

    def __init__(self, name = None, parent_obj = None, security_group_id = None, configured_security_group_id = None, security_group_entries = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'security-group'
        if not name:
            name = u'default-security-group'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if security_group_id:
            self._security_group_id = security_group_id
        if configured_security_group_id:
            self._configured_security_group_id = configured_security_group_id
        if security_group_entries:
            self._security_group_entries = security_group_entries
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (security-group)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of security-group in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of security-group as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of security-group's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of security-group's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def security_group_id(self):
        """Get security-group-id for security-group.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_security_group_id', None)
    #end security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Set security-group-id for security-group.
        
        :param security_group_id: xsd:string object
        
        """
        self._security_group_id = security_group_id
    #end security_group_id

    def set_security_group_id(self, value):
        self.security_group_id = value
    #end set_security_group_id

    def get_security_group_id(self):
        return self.security_group_id
    #end get_security_group_id

    @property
    def configured_security_group_id(self):
        """Get configured-security-group-id for security-group.
        
        :returns: xsd:integer object
        
        """
        return getattr(self, '_configured_security_group_id', None)
    #end configured_security_group_id

    @configured_security_group_id.setter
    def configured_security_group_id(self, configured_security_group_id):
        """Set configured-security-group-id for security-group.
        
        :param configured_security_group_id: xsd:integer object
        
        """
        self._configured_security_group_id = configured_security_group_id
    #end configured_security_group_id

    def set_configured_security_group_id(self, value):
        self.configured_security_group_id = value
    #end set_configured_security_group_id

    def get_configured_security_group_id(self):
        return self.configured_security_group_id
    #end get_configured_security_group_id

    @property
    def security_group_entries(self):
        """Get security-group-entries for security-group.
        
        :returns: PolicyEntriesType object
        
        """
        return getattr(self, '_security_group_entries', None)
    #end security_group_entries

    @security_group_entries.setter
    def security_group_entries(self, security_group_entries):
        """Set security-group-entries for security-group.
        
        :param security_group_entries: PolicyEntriesType object
        
        """
        self._security_group_entries = security_group_entries
    #end security_group_entries

    def set_security_group_entries(self, value):
        self.security_group_entries = value
    #end set_security_group_entries

    def get_security_group_entries(self):
        return self.security_group_entries
    #end get_security_group_entries

    @property
    def id_perms(self):
        """Get id-perms for security-group.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for security-group.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for security-group.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for security-group.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_security_group_id'):
            self._serialize_field_to_json(serialized, field_names, 'security_group_id')
        if hasattr(self, '_configured_security_group_id'):
            self._serialize_field_to_json(serialized, field_names, 'configured_security_group_id')
        if hasattr(self, '_security_group_entries'):
            self._serialize_field_to_json(serialized, field_names, 'security_group_entries')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_access_control_lists(self):
        return getattr(self, 'access_control_lists', None)
    #end get_access_control_lists

    def get_project_back_refs(self):
        """Return list of all projects using this security-group"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this security-group"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def dump(self):
        """Display security-group object in compact form."""
        print '------------ security-group ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P security_group_id = ', self.get_security_group_id()
        print 'P configured_security_group_id = ', self.get_configured_security_group_id()
        print 'P security_group_entries = ', self.get_security_group_entries()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS access_control_list = ', self.get_access_control_lists()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class SecurityGroup

class ProviderAttachment(object):
    """
    Represents provider-attachment configuration representation.

    Properties:
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.VirtualRouter` objects

    Referred by:
    """

    prop_fields = set([u'id_perms', u'display_name'])
    ref_fields = set(['virtual_router_refs'])
    backref_fields = set(['customer_attachment_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'provider-attachment'
        if not name:
            name = u'default-provider-attachment'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (provider-attachment)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of provider-attachment in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of provider-attachment as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def id_perms(self):
        """Get id-perms for provider-attachment.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for provider-attachment.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for provider-attachment.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for provider-attachment.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_router_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_router(self, ref_obj):
        """Set virtual-router for provider-attachment.
        
        :param ref_obj: VirtualRouter object
        
        """
        self.virtual_router_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_router

    def add_virtual_router(self, ref_obj):
        """Add virtual-router to provider-attachment.
        
        :param ref_obj: VirtualRouter object
        
        """
        refs = getattr(self, 'virtual_router_refs', [])
        if not refs:
            self.virtual_router_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_router_refs.append(ref_info)
    #end add_virtual_router

    def del_virtual_router(self, ref_obj):
        refs = self.get_virtual_router_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_router_refs.remove(ref)
                return
    #end del_virtual_router

    def set_virtual_router_list(self, ref_obj_list):
        """Set virtual-router list for provider-attachment.
        
        :param ref_obj_list: list of VirtualRouter object
        
        """
        self.virtual_router_refs = ref_obj_list
    #end set_virtual_router_list

    def get_virtual_router_refs(self):
        """Return virtual-router list for provider-attachment.
        
        :returns: list of <VirtualRouter>
        
        """
        return getattr(self, 'virtual_router_refs', None)
    #end get_virtual_router_refs

    def get_customer_attachment_back_refs(self):
        """Return list of all customer-attachments using this provider-attachment"""
        return getattr(self, 'customer_attachment_back_refs', None)
    #end get_customer_attachment_back_refs

    def dump(self):
        """Display provider-attachment object in compact form."""
        print '------------ provider-attachment ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_router = ', self.get_virtual_router_refs()
    #end dump

#end class ProviderAttachment

class VirtualMachineInterface(object):
    """
    Represents virtual-machine-interface configuration representation.

    Child of:
        :class:`.VirtualMachine` object OR
        :class:`.Project` object OR

    Properties:
        * virtual-machine-interface-mac-addresses (:class:`.MacAddressesType` type)
        * virtual-machine-interface-dhcp-option-list (:class:`.DhcpOptionsListType` type)
        * virtual-machine-interface-host-routes (:class:`.RouteTableType` type)
        * virtual-machine-interface-allowed-address-pairs (:class:`.AllowedAddressPairs` type)
        * vrf-assign-table (:class:`.VrfAssignTableType` type)
        * virtual-machine-interface-device-owner (xsd:string type)
        * virtual-machine-interface-properties (:class:`.VirtualMachineInterfacePropertiesType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.QosForwardingClass` objects
        * list of :class:`.SecurityGroup` objects
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.VirtualMachine` objects
        * list of :class:`.VirtualNetwork` objects
        * list of (:class:`.RoutingInstance` object, :class:`.PolicyBasedForwardingRuleType` attribute)
        * list of :class:`.InterfaceRouteTable` objects

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.InstanceIp` objects
        * list of :class:`.Subnet` objects
        * list of :class:`.FloatingIp` objects
        * list of :class:`.LogicalInterface` objects
        * list of :class:`.CustomerAttachment` objects
        * list of :class:`.LogicalRouter` objects
        * list of :class:`.LoadbalancerPool` objects
        * list of :class:`.VirtualIp` objects
    """

    prop_fields = set([u'virtual_machine_interface_mac_addresses', u'virtual_machine_interface_dhcp_option_list', u'virtual_machine_interface_host_routes', u'virtual_machine_interface_allowed_address_pairs', u'vrf_assign_table', u'virtual_machine_interface_device_owner', u'virtual_machine_interface_properties', u'id_perms', u'display_name'])
    ref_fields = set([u'qos_forwarding_class_refs', u'security_group_refs', 'virtual_machine_interface_refs', u'virtual_machine_refs', u'virtual_network_refs', 'routing_instance_refs', u'interface_route_table_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs', u'virtual_machine_back_refs', u'project_back_refs', u'instance_ip_back_refs', u'subnet_back_refs', u'floating_ip_back_refs', u'logical_interface_back_refs', 'customer_attachment_back_refs', u'logical_router_back_refs', u'loadbalancer_pool_back_refs', u'virtual_ip_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, virtual_machine_interface_mac_addresses = None, virtual_machine_interface_dhcp_option_list = None, virtual_machine_interface_host_routes = None, virtual_machine_interface_allowed_address_pairs = None, vrf_assign_table = None, virtual_machine_interface_device_owner = None, virtual_machine_interface_properties = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-machine-interface'
        if not name:
            name = u'default-virtual-machine-interface'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            # if obj constructed from within server, ignore if parent not specified
            if not kwargs['parent_type']:
                raise AmbiguousParentError("[[u'default-virtual-machine'], [u'default-domain', u'default-project']]")

        # property fields
        if virtual_machine_interface_mac_addresses:
            self._virtual_machine_interface_mac_addresses = virtual_machine_interface_mac_addresses
        if virtual_machine_interface_dhcp_option_list:
            self._virtual_machine_interface_dhcp_option_list = virtual_machine_interface_dhcp_option_list
        if virtual_machine_interface_host_routes:
            self._virtual_machine_interface_host_routes = virtual_machine_interface_host_routes
        if virtual_machine_interface_allowed_address_pairs:
            self._virtual_machine_interface_allowed_address_pairs = virtual_machine_interface_allowed_address_pairs
        if vrf_assign_table:
            self._vrf_assign_table = vrf_assign_table
        if virtual_machine_interface_device_owner:
            self._virtual_machine_interface_device_owner = virtual_machine_interface_device_owner
        if virtual_machine_interface_properties:
            self._virtual_machine_interface_properties = virtual_machine_interface_properties
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (virtual-machine-interface)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of virtual-machine-interface in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of virtual-machine-interface as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of virtual-machine-interface's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of virtual-machine-interface's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def virtual_machine_interface_mac_addresses(self):
        """Get virtual-machine-interface-mac-addresses for virtual-machine-interface.
        
        :returns: MacAddressesType object
        
        """
        return getattr(self, '_virtual_machine_interface_mac_addresses', None)
    #end virtual_machine_interface_mac_addresses

    @virtual_machine_interface_mac_addresses.setter
    def virtual_machine_interface_mac_addresses(self, virtual_machine_interface_mac_addresses):
        """Set virtual-machine-interface-mac-addresses for virtual-machine-interface.
        
        :param virtual_machine_interface_mac_addresses: MacAddressesType object
        
        """
        self._virtual_machine_interface_mac_addresses = virtual_machine_interface_mac_addresses
    #end virtual_machine_interface_mac_addresses

    def set_virtual_machine_interface_mac_addresses(self, value):
        self.virtual_machine_interface_mac_addresses = value
    #end set_virtual_machine_interface_mac_addresses

    def get_virtual_machine_interface_mac_addresses(self):
        return self.virtual_machine_interface_mac_addresses
    #end get_virtual_machine_interface_mac_addresses

    @property
    def virtual_machine_interface_dhcp_option_list(self):
        """Get virtual-machine-interface-dhcp-option-list for virtual-machine-interface.
        
        :returns: DhcpOptionsListType object
        
        """
        return getattr(self, '_virtual_machine_interface_dhcp_option_list', None)
    #end virtual_machine_interface_dhcp_option_list

    @virtual_machine_interface_dhcp_option_list.setter
    def virtual_machine_interface_dhcp_option_list(self, virtual_machine_interface_dhcp_option_list):
        """Set virtual-machine-interface-dhcp-option-list for virtual-machine-interface.
        
        :param virtual_machine_interface_dhcp_option_list: DhcpOptionsListType object
        
        """
        self._virtual_machine_interface_dhcp_option_list = virtual_machine_interface_dhcp_option_list
    #end virtual_machine_interface_dhcp_option_list

    def set_virtual_machine_interface_dhcp_option_list(self, value):
        self.virtual_machine_interface_dhcp_option_list = value
    #end set_virtual_machine_interface_dhcp_option_list

    def get_virtual_machine_interface_dhcp_option_list(self):
        return self.virtual_machine_interface_dhcp_option_list
    #end get_virtual_machine_interface_dhcp_option_list

    @property
    def virtual_machine_interface_host_routes(self):
        """Get virtual-machine-interface-host-routes for virtual-machine-interface.
        
        :returns: RouteTableType object
        
        """
        return getattr(self, '_virtual_machine_interface_host_routes', None)
    #end virtual_machine_interface_host_routes

    @virtual_machine_interface_host_routes.setter
    def virtual_machine_interface_host_routes(self, virtual_machine_interface_host_routes):
        """Set virtual-machine-interface-host-routes for virtual-machine-interface.
        
        :param virtual_machine_interface_host_routes: RouteTableType object
        
        """
        self._virtual_machine_interface_host_routes = virtual_machine_interface_host_routes
    #end virtual_machine_interface_host_routes

    def set_virtual_machine_interface_host_routes(self, value):
        self.virtual_machine_interface_host_routes = value
    #end set_virtual_machine_interface_host_routes

    def get_virtual_machine_interface_host_routes(self):
        return self.virtual_machine_interface_host_routes
    #end get_virtual_machine_interface_host_routes

    @property
    def virtual_machine_interface_allowed_address_pairs(self):
        """Get virtual-machine-interface-allowed-address-pairs for virtual-machine-interface.
        
        :returns: AllowedAddressPairs object
        
        """
        return getattr(self, '_virtual_machine_interface_allowed_address_pairs', None)
    #end virtual_machine_interface_allowed_address_pairs

    @virtual_machine_interface_allowed_address_pairs.setter
    def virtual_machine_interface_allowed_address_pairs(self, virtual_machine_interface_allowed_address_pairs):
        """Set virtual-machine-interface-allowed-address-pairs for virtual-machine-interface.
        
        :param virtual_machine_interface_allowed_address_pairs: AllowedAddressPairs object
        
        """
        self._virtual_machine_interface_allowed_address_pairs = virtual_machine_interface_allowed_address_pairs
    #end virtual_machine_interface_allowed_address_pairs

    def set_virtual_machine_interface_allowed_address_pairs(self, value):
        self.virtual_machine_interface_allowed_address_pairs = value
    #end set_virtual_machine_interface_allowed_address_pairs

    def get_virtual_machine_interface_allowed_address_pairs(self):
        return self.virtual_machine_interface_allowed_address_pairs
    #end get_virtual_machine_interface_allowed_address_pairs

    @property
    def vrf_assign_table(self):
        """Get vrf-assign-table for virtual-machine-interface.
        
        :returns: VrfAssignTableType object
        
        """
        return getattr(self, '_vrf_assign_table', None)
    #end vrf_assign_table

    @vrf_assign_table.setter
    def vrf_assign_table(self, vrf_assign_table):
        """Set vrf-assign-table for virtual-machine-interface.
        
        :param vrf_assign_table: VrfAssignTableType object
        
        """
        self._vrf_assign_table = vrf_assign_table
    #end vrf_assign_table

    def set_vrf_assign_table(self, value):
        self.vrf_assign_table = value
    #end set_vrf_assign_table

    def get_vrf_assign_table(self):
        return self.vrf_assign_table
    #end get_vrf_assign_table

    @property
    def virtual_machine_interface_device_owner(self):
        """Get virtual-machine-interface-device-owner for virtual-machine-interface.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_virtual_machine_interface_device_owner', None)
    #end virtual_machine_interface_device_owner

    @virtual_machine_interface_device_owner.setter
    def virtual_machine_interface_device_owner(self, virtual_machine_interface_device_owner):
        """Set virtual-machine-interface-device-owner for virtual-machine-interface.
        
        :param virtual_machine_interface_device_owner: xsd:string object
        
        """
        self._virtual_machine_interface_device_owner = virtual_machine_interface_device_owner
    #end virtual_machine_interface_device_owner

    def set_virtual_machine_interface_device_owner(self, value):
        self.virtual_machine_interface_device_owner = value
    #end set_virtual_machine_interface_device_owner

    def get_virtual_machine_interface_device_owner(self):
        return self.virtual_machine_interface_device_owner
    #end get_virtual_machine_interface_device_owner

    @property
    def virtual_machine_interface_properties(self):
        """Get virtual-machine-interface-properties for virtual-machine-interface.
        
        :returns: VirtualMachineInterfacePropertiesType object
        
        """
        return getattr(self, '_virtual_machine_interface_properties', None)
    #end virtual_machine_interface_properties

    @virtual_machine_interface_properties.setter
    def virtual_machine_interface_properties(self, virtual_machine_interface_properties):
        """Set virtual-machine-interface-properties for virtual-machine-interface.
        
        :param virtual_machine_interface_properties: VirtualMachineInterfacePropertiesType object
        
        """
        self._virtual_machine_interface_properties = virtual_machine_interface_properties
    #end virtual_machine_interface_properties

    def set_virtual_machine_interface_properties(self, value):
        self.virtual_machine_interface_properties = value
    #end set_virtual_machine_interface_properties

    def get_virtual_machine_interface_properties(self):
        return self.virtual_machine_interface_properties
    #end get_virtual_machine_interface_properties

    @property
    def id_perms(self):
        """Get id-perms for virtual-machine-interface.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-machine-interface.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for virtual-machine-interface.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-machine-interface.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_virtual_machine_interface_mac_addresses'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_mac_addresses')
        if hasattr(self, '_virtual_machine_interface_dhcp_option_list'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_dhcp_option_list')
        if hasattr(self, '_virtual_machine_interface_host_routes'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_host_routes')
        if hasattr(self, '_virtual_machine_interface_allowed_address_pairs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_allowed_address_pairs')
        if hasattr(self, '_vrf_assign_table'):
            self._serialize_field_to_json(serialized, field_names, 'vrf_assign_table')
        if hasattr(self, '_virtual_machine_interface_device_owner'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_device_owner')
        if hasattr(self, '_virtual_machine_interface_properties'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'qos_forwarding_class_refs'):
            self._serialize_field_to_json(serialized, field_names, 'qos_forwarding_class_refs')
        if hasattr(self, 'security_group_refs'):
            self._serialize_field_to_json(serialized, field_names, 'security_group_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        if hasattr(self, 'virtual_machine_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_refs')
        if hasattr(self, 'virtual_network_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_refs')
        if hasattr(self, 'routing_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'routing_instance_refs')
        if hasattr(self, 'interface_route_table_refs'):
            self._serialize_field_to_json(serialized, field_names, 'interface_route_table_refs')
        return serialized
    #end serialize_to_json

    def set_qos_forwarding_class(self, ref_obj):
        """Set qos-forwarding-class for virtual-machine-interface.
        
        :param ref_obj: QosForwardingClass object
        
        """
        self.qos_forwarding_class_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.qos_forwarding_class_refs[0]['uuid'] = ref_obj.uuid

    #end set_qos_forwarding_class

    def add_qos_forwarding_class(self, ref_obj):
        """Add qos-forwarding-class to virtual-machine-interface.
        
        :param ref_obj: QosForwardingClass object
        
        """
        refs = getattr(self, 'qos_forwarding_class_refs', [])
        if not refs:
            self.qos_forwarding_class_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.qos_forwarding_class_refs.append(ref_info)
    #end add_qos_forwarding_class

    def del_qos_forwarding_class(self, ref_obj):
        refs = self.get_qos_forwarding_class_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.qos_forwarding_class_refs.remove(ref)
                return
    #end del_qos_forwarding_class

    def set_qos_forwarding_class_list(self, ref_obj_list):
        """Set qos-forwarding-class list for virtual-machine-interface.
        
        :param ref_obj_list: list of QosForwardingClass object
        
        """
        self.qos_forwarding_class_refs = ref_obj_list
    #end set_qos_forwarding_class_list

    def get_qos_forwarding_class_refs(self):
        """Return qos-forwarding-class list for virtual-machine-interface.
        
        :returns: list of <QosForwardingClass>
        
        """
        return getattr(self, 'qos_forwarding_class_refs', None)
    #end get_qos_forwarding_class_refs

    def set_security_group(self, ref_obj):
        """Set security-group for virtual-machine-interface.
        
        :param ref_obj: SecurityGroup object
        
        """
        self.security_group_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.security_group_refs[0]['uuid'] = ref_obj.uuid

    #end set_security_group

    def add_security_group(self, ref_obj):
        """Add security-group to virtual-machine-interface.
        
        :param ref_obj: SecurityGroup object
        
        """
        refs = getattr(self, 'security_group_refs', [])
        if not refs:
            self.security_group_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.security_group_refs.append(ref_info)
    #end add_security_group

    def del_security_group(self, ref_obj):
        refs = self.get_security_group_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.security_group_refs.remove(ref)
                return
    #end del_security_group

    def set_security_group_list(self, ref_obj_list):
        """Set security-group list for virtual-machine-interface.
        
        :param ref_obj_list: list of SecurityGroup object
        
        """
        self.security_group_refs = ref_obj_list
    #end set_security_group_list

    def get_security_group_refs(self):
        """Return security-group list for virtual-machine-interface.
        
        :returns: list of <SecurityGroup>
        
        """
        return getattr(self, 'security_group_refs', None)
    #end get_security_group_refs

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for virtual-machine-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to virtual-machine-interface.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for virtual-machine-interface.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for virtual-machine-interface.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def set_virtual_machine(self, ref_obj):
        """Set virtual-machine for virtual-machine-interface.
        
        :param ref_obj: VirtualMachine object
        
        """
        self.virtual_machine_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine

    def add_virtual_machine(self, ref_obj):
        """Add virtual-machine to virtual-machine-interface.
        
        :param ref_obj: VirtualMachine object
        
        """
        refs = getattr(self, 'virtual_machine_refs', [])
        if not refs:
            self.virtual_machine_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_refs.append(ref_info)
    #end add_virtual_machine

    def del_virtual_machine(self, ref_obj):
        refs = self.get_virtual_machine_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_refs.remove(ref)
                return
    #end del_virtual_machine

    def set_virtual_machine_list(self, ref_obj_list):
        """Set virtual-machine list for virtual-machine-interface.
        
        :param ref_obj_list: list of VirtualMachine object
        
        """
        self.virtual_machine_refs = ref_obj_list
    #end set_virtual_machine_list

    def get_virtual_machine_refs(self):
        """Return virtual-machine list for virtual-machine-interface.
        
        :returns: list of <VirtualMachine>
        
        """
        return getattr(self, 'virtual_machine_refs', None)
    #end get_virtual_machine_refs

    def set_virtual_network(self, ref_obj):
        """Set virtual-network for virtual-machine-interface.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self.virtual_network_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_network_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_network

    def add_virtual_network(self, ref_obj):
        """Add virtual-network to virtual-machine-interface.
        
        :param ref_obj: VirtualNetwork object
        
        """
        refs = getattr(self, 'virtual_network_refs', [])
        if not refs:
            self.virtual_network_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_network_refs.append(ref_info)
    #end add_virtual_network

    def del_virtual_network(self, ref_obj):
        refs = self.get_virtual_network_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_network_refs.remove(ref)
                return
    #end del_virtual_network

    def set_virtual_network_list(self, ref_obj_list):
        """Set virtual-network list for virtual-machine-interface.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self.virtual_network_refs = ref_obj_list
    #end set_virtual_network_list

    def get_virtual_network_refs(self):
        """Return virtual-network list for virtual-machine-interface.
        
        :returns: list of <VirtualNetwork>
        
        """
        return getattr(self, 'virtual_network_refs', None)
    #end get_virtual_network_refs

    def set_routing_instance(self, ref_obj, ref_data):
        """Set routing-instance for virtual-machine-interface.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: PolicyBasedForwardingRuleType object
        
        """
        self.routing_instance_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.routing_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_routing_instance

    def add_routing_instance(self, ref_obj, ref_data):
        """Add routing-instance to virtual-machine-interface.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: PolicyBasedForwardingRuleType object
        
        """
        refs = getattr(self, 'routing_instance_refs', [])
        if not refs:
            self.routing_instance_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.routing_instance_refs.append(ref_info)
    #end add_routing_instance

    def del_routing_instance(self, ref_obj):
        refs = self.get_routing_instance_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.routing_instance_refs.remove(ref)
                return
    #end del_routing_instance

    def set_routing_instance_list(self, ref_obj_list, ref_data_list):
        """Set routing-instance list for virtual-machine-interface.
        
        :param ref_obj_list: list of RoutingInstance object
        :param ref_data_list: list of PolicyBasedForwardingRuleType object
        
        """
        self.routing_instance_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_routing_instance_list

    def get_routing_instance_refs(self):
        """Return routing-instance list for virtual-machine-interface.
        
        :returns: list of tuple <RoutingInstance, PolicyBasedForwardingRuleType>
        
        """
        return getattr(self, 'routing_instance_refs', None)
    #end get_routing_instance_refs

    def set_interface_route_table(self, ref_obj):
        """Set interface-route-table for virtual-machine-interface.
        
        :param ref_obj: InterfaceRouteTable object
        
        """
        self.interface_route_table_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.interface_route_table_refs[0]['uuid'] = ref_obj.uuid

    #end set_interface_route_table

    def add_interface_route_table(self, ref_obj):
        """Add interface-route-table to virtual-machine-interface.
        
        :param ref_obj: InterfaceRouteTable object
        
        """
        refs = getattr(self, 'interface_route_table_refs', [])
        if not refs:
            self.interface_route_table_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.interface_route_table_refs.append(ref_info)
    #end add_interface_route_table

    def del_interface_route_table(self, ref_obj):
        refs = self.get_interface_route_table_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.interface_route_table_refs.remove(ref)
                return
    #end del_interface_route_table

    def set_interface_route_table_list(self, ref_obj_list):
        """Set interface-route-table list for virtual-machine-interface.
        
        :param ref_obj_list: list of InterfaceRouteTable object
        
        """
        self.interface_route_table_refs = ref_obj_list
    #end set_interface_route_table_list

    def get_interface_route_table_refs(self):
        """Return interface-route-table list for virtual-machine-interface.
        
        :returns: list of <InterfaceRouteTable>
        
        """
        return getattr(self, 'interface_route_table_refs', None)
    #end get_interface_route_table_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this virtual-machine-interface"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def get_virtual_machine_back_refs(self):
        """Return list of all virtual-machines using this virtual-machine-interface"""
        return getattr(self, 'virtual_machine_back_refs', None)
    #end get_virtual_machine_back_refs

    def get_project_back_refs(self):
        """Return list of all projects using this virtual-machine-interface"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_instance_ip_back_refs(self):
        """Return list of all instance-ips using this virtual-machine-interface"""
        return getattr(self, 'instance_ip_back_refs', None)
    #end get_instance_ip_back_refs

    def get_subnet_back_refs(self):
        """Return list of all subnets using this virtual-machine-interface"""
        return getattr(self, 'subnet_back_refs', None)
    #end get_subnet_back_refs

    def get_floating_ip_back_refs(self):
        """Return list of all floating-ips using this virtual-machine-interface"""
        return getattr(self, 'floating_ip_back_refs', None)
    #end get_floating_ip_back_refs

    def get_logical_interface_back_refs(self):
        """Return list of all logical-interfaces using this virtual-machine-interface"""
        return getattr(self, 'logical_interface_back_refs', None)
    #end get_logical_interface_back_refs

    def get_customer_attachment_back_refs(self):
        """Return list of all customer-attachments using this virtual-machine-interface"""
        return getattr(self, 'customer_attachment_back_refs', None)
    #end get_customer_attachment_back_refs

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this virtual-machine-interface"""
        return getattr(self, 'logical_router_back_refs', None)
    #end get_logical_router_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this virtual-machine-interface"""
        return getattr(self, 'loadbalancer_pool_back_refs', None)
    #end get_loadbalancer_pool_back_refs

    def get_virtual_ip_back_refs(self):
        """Return list of all virtual-ips using this virtual-machine-interface"""
        return getattr(self, 'virtual_ip_back_refs', None)
    #end get_virtual_ip_back_refs

    def dump(self):
        """Display virtual-machine-interface object in compact form."""
        print '------------ virtual-machine-interface ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_machine_interface_mac_addresses = ', self.get_virtual_machine_interface_mac_addresses()
        print 'P virtual_machine_interface_dhcp_option_list = ', self.get_virtual_machine_interface_dhcp_option_list()
        print 'P virtual_machine_interface_host_routes = ', self.get_virtual_machine_interface_host_routes()
        print 'P virtual_machine_interface_allowed_address_pairs = ', self.get_virtual_machine_interface_allowed_address_pairs()
        print 'P vrf_assign_table = ', self.get_vrf_assign_table()
        print 'P virtual_machine_interface_device_owner = ', self.get_virtual_machine_interface_device_owner()
        print 'P virtual_machine_interface_properties = ', self.get_virtual_machine_interface_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF qos_forwarding_class = ', self.get_qos_forwarding_class_refs()
        print 'REF security_group = ', self.get_security_group_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF virtual_machine = ', self.get_virtual_machine_refs()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'REF routing_instance = ', self.get_routing_instance_refs()
        print 'REF interface_route_table = ', self.get_interface_route_table_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
        print 'BCK instance_ip = ', self.get_instance_ip_back_refs()
        print 'BCK subnet = ', self.get_subnet_back_refs()
        print 'BCK floating_ip = ', self.get_floating_ip_back_refs()
        print 'BCK logical_interface = ', self.get_logical_interface_back_refs()
        print 'BCK customer_attachment = ', self.get_customer_attachment_back_refs()
        print 'BCK logical_router = ', self.get_logical_router_back_refs()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
        print 'BCK virtual_ip = ', self.get_virtual_ip_back_refs()
    #end dump

#end class VirtualMachineInterface

class LoadbalancerHealthmonitor(object):
    """
    Represents loadbalancer-healthmonitor configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * loadbalancer-healthmonitor-properties (:class:`.LoadbalancerHealthmonitorType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
        * list of :class:`.LoadbalancerPool` objects
    """

    prop_fields = set([u'loadbalancer_healthmonitor_properties', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs', u'loadbalancer_pool_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, loadbalancer_healthmonitor_properties = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'loadbalancer-healthmonitor'
        if not name:
            name = u'default-loadbalancer-healthmonitor'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if loadbalancer_healthmonitor_properties:
            self._loadbalancer_healthmonitor_properties = loadbalancer_healthmonitor_properties
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (loadbalancer-healthmonitor)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of loadbalancer-healthmonitor in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of loadbalancer-healthmonitor as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of loadbalancer-healthmonitor's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of loadbalancer-healthmonitor's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def loadbalancer_healthmonitor_properties(self):
        """Get loadbalancer-healthmonitor-properties for loadbalancer-healthmonitor.
        
        :returns: LoadbalancerHealthmonitorType object
        
        """
        return getattr(self, '_loadbalancer_healthmonitor_properties', None)
    #end loadbalancer_healthmonitor_properties

    @loadbalancer_healthmonitor_properties.setter
    def loadbalancer_healthmonitor_properties(self, loadbalancer_healthmonitor_properties):
        """Set loadbalancer-healthmonitor-properties for loadbalancer-healthmonitor.
        
        :param loadbalancer_healthmonitor_properties: LoadbalancerHealthmonitorType object
        
        """
        self._loadbalancer_healthmonitor_properties = loadbalancer_healthmonitor_properties
    #end loadbalancer_healthmonitor_properties

    def set_loadbalancer_healthmonitor_properties(self, value):
        self.loadbalancer_healthmonitor_properties = value
    #end set_loadbalancer_healthmonitor_properties

    def get_loadbalancer_healthmonitor_properties(self):
        return self.loadbalancer_healthmonitor_properties
    #end get_loadbalancer_healthmonitor_properties

    @property
    def id_perms(self):
        """Get id-perms for loadbalancer-healthmonitor.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-healthmonitor.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for loadbalancer-healthmonitor.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-healthmonitor.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_loadbalancer_healthmonitor_properties'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_healthmonitor_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_project_back_refs(self):
        """Return list of all projects using this loadbalancer-healthmonitor"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this loadbalancer-healthmonitor"""
        return getattr(self, 'loadbalancer_pool_back_refs', None)
    #end get_loadbalancer_pool_back_refs

    def dump(self):
        """Display loadbalancer-healthmonitor object in compact form."""
        print '------------ loadbalancer-healthmonitor ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P loadbalancer_healthmonitor_properties = ', self.get_loadbalancer_healthmonitor_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
    #end dump

#end class LoadbalancerHealthmonitor

class VirtualNetwork(object):
    """
    Represents virtual-network configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * virtual-network-properties (:class:`.VirtualNetworkType` type)
        * virtual-network-network-id (xsd:integer type)
        * route-target-list (:class:`.RouteTargetList` type)
        * router-external (xsd:boolean type)
        * is-shared (xsd:boolean type)
        * external-ipam (xsd:boolean type)
        * flood-unknown-unicast (xsd:boolean type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.AccessControlList` objects
        * list of :class:`.FloatingIpPool` objects
        * list of :class:`.RoutingInstance` objects

    References to:
        * list of :class:`.QosForwardingClass` objects
        * list of (:class:`.NetworkIpam` object, :class:`.VnSubnetsType` attribute)
        * list of (:class:`.NetworkPolicy` object, :class:`.VirtualNetworkPolicyType` attribute)
        * list of :class:`.RouteTable` objects

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.InstanceIp` objects
        * list of :class:`.PhysicalRouter` objects
        * list of :class:`.LogicalRouter` objects
    """

    prop_fields = set([u'virtual_network_properties', u'virtual_network_network_id', u'route_target_list', u'router_external', u'is_shared', u'external_ipam', u'flood_unknown_unicast', u'id_perms', u'display_name'])
    ref_fields = set([u'qos_forwarding_class_refs', u'network_ipam_refs', u'network_policy_refs', u'route_table_refs'])
    backref_fields = set([u'project_back_refs', 'virtual_machine_interface_back_refs', u'instance_ip_back_refs', u'physical_router_back_refs', u'logical_router_back_refs'])
    children_fields = set([u'access_control_lists', u'floating_ip_pools', 'routing_instances'])

    def __init__(self, name = None, parent_obj = None, virtual_network_properties = None, virtual_network_network_id = None, route_target_list = None, router_external = None, is_shared = None, external_ipam = None, flood_unknown_unicast = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-network'
        if not name:
            name = u'default-virtual-network'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if virtual_network_properties:
            self._virtual_network_properties = virtual_network_properties
        if virtual_network_network_id:
            self._virtual_network_network_id = virtual_network_network_id
        if route_target_list:
            self._route_target_list = route_target_list
        if router_external:
            self._router_external = router_external
        if is_shared:
            self._is_shared = is_shared
        if external_ipam:
            self._external_ipam = external_ipam
        if flood_unknown_unicast:
            self._flood_unknown_unicast = flood_unknown_unicast
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (virtual-network)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of virtual-network in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of virtual-network as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of virtual-network's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of virtual-network's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def virtual_network_properties(self):
        """Get virtual-network-properties for virtual-network.
        
        :returns: VirtualNetworkType object
        
        """
        return getattr(self, '_virtual_network_properties', None)
    #end virtual_network_properties

    @virtual_network_properties.setter
    def virtual_network_properties(self, virtual_network_properties):
        """Set virtual-network-properties for virtual-network.
        
        :param virtual_network_properties: VirtualNetworkType object
        
        """
        self._virtual_network_properties = virtual_network_properties
    #end virtual_network_properties

    def set_virtual_network_properties(self, value):
        self.virtual_network_properties = value
    #end set_virtual_network_properties

    def get_virtual_network_properties(self):
        return self.virtual_network_properties
    #end get_virtual_network_properties

    @property
    def virtual_network_network_id(self):
        """Get virtual-network-network-id for virtual-network.
        
        :returns: xsd:integer object
        
        """
        return getattr(self, '_virtual_network_network_id', None)
    #end virtual_network_network_id

    @virtual_network_network_id.setter
    def virtual_network_network_id(self, virtual_network_network_id):
        """Set virtual-network-network-id for virtual-network.
        
        :param virtual_network_network_id: xsd:integer object
        
        """
        self._virtual_network_network_id = virtual_network_network_id
    #end virtual_network_network_id

    def set_virtual_network_network_id(self, value):
        self.virtual_network_network_id = value
    #end set_virtual_network_network_id

    def get_virtual_network_network_id(self):
        return self.virtual_network_network_id
    #end get_virtual_network_network_id

    @property
    def route_target_list(self):
        """Get route-target-list for virtual-network.
        
        :returns: RouteTargetList object
        
        """
        return getattr(self, '_route_target_list', None)
    #end route_target_list

    @route_target_list.setter
    def route_target_list(self, route_target_list):
        """Set route-target-list for virtual-network.
        
        :param route_target_list: RouteTargetList object
        
        """
        self._route_target_list = route_target_list
    #end route_target_list

    def set_route_target_list(self, value):
        self.route_target_list = value
    #end set_route_target_list

    def get_route_target_list(self):
        return self.route_target_list
    #end get_route_target_list

    @property
    def router_external(self):
        """Get router-external for virtual-network.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_router_external', None)
    #end router_external

    @router_external.setter
    def router_external(self, router_external):
        """Set router-external for virtual-network.
        
        :param router_external: xsd:boolean object
        
        """
        self._router_external = router_external
    #end router_external

    def set_router_external(self, value):
        self.router_external = value
    #end set_router_external

    def get_router_external(self):
        return self.router_external
    #end get_router_external

    @property
    def is_shared(self):
        """Get is-shared for virtual-network.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_is_shared', None)
    #end is_shared

    @is_shared.setter
    def is_shared(self, is_shared):
        """Set is-shared for virtual-network.
        
        :param is_shared: xsd:boolean object
        
        """
        self._is_shared = is_shared
    #end is_shared

    def set_is_shared(self, value):
        self.is_shared = value
    #end set_is_shared

    def get_is_shared(self):
        return self.is_shared
    #end get_is_shared

    @property
    def external_ipam(self):
        """Get external-ipam for virtual-network.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_external_ipam', None)
    #end external_ipam

    @external_ipam.setter
    def external_ipam(self, external_ipam):
        """Set external-ipam for virtual-network.
        
        :param external_ipam: xsd:boolean object
        
        """
        self._external_ipam = external_ipam
    #end external_ipam

    def set_external_ipam(self, value):
        self.external_ipam = value
    #end set_external_ipam

    def get_external_ipam(self):
        return self.external_ipam
    #end get_external_ipam

    @property
    def flood_unknown_unicast(self):
        """Get flood-unknown-unicast for virtual-network.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_flood_unknown_unicast', None)
    #end flood_unknown_unicast

    @flood_unknown_unicast.setter
    def flood_unknown_unicast(self, flood_unknown_unicast):
        """Set flood-unknown-unicast for virtual-network.
        
        :param flood_unknown_unicast: xsd:boolean object
        
        """
        self._flood_unknown_unicast = flood_unknown_unicast
    #end flood_unknown_unicast

    def set_flood_unknown_unicast(self, value):
        self.flood_unknown_unicast = value
    #end set_flood_unknown_unicast

    def get_flood_unknown_unicast(self):
        return self.flood_unknown_unicast
    #end get_flood_unknown_unicast

    @property
    def id_perms(self):
        """Get id-perms for virtual-network.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for virtual-network.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for virtual-network.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for virtual-network.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_virtual_network_properties'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_properties')
        if hasattr(self, '_virtual_network_network_id'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_network_id')
        if hasattr(self, '_route_target_list'):
            self._serialize_field_to_json(serialized, field_names, 'route_target_list')
        if hasattr(self, '_router_external'):
            self._serialize_field_to_json(serialized, field_names, 'router_external')
        if hasattr(self, '_is_shared'):
            self._serialize_field_to_json(serialized, field_names, 'is_shared')
        if hasattr(self, '_external_ipam'):
            self._serialize_field_to_json(serialized, field_names, 'external_ipam')
        if hasattr(self, '_flood_unknown_unicast'):
            self._serialize_field_to_json(serialized, field_names, 'flood_unknown_unicast')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'qos_forwarding_class_refs'):
            self._serialize_field_to_json(serialized, field_names, 'qos_forwarding_class_refs')
        if hasattr(self, 'network_ipam_refs'):
            self._serialize_field_to_json(serialized, field_names, 'network_ipam_refs')
        if hasattr(self, 'network_policy_refs'):
            self._serialize_field_to_json(serialized, field_names, 'network_policy_refs')
        if hasattr(self, 'route_table_refs'):
            self._serialize_field_to_json(serialized, field_names, 'route_table_refs')
        return serialized
    #end serialize_to_json

    def get_access_control_lists(self):
        return getattr(self, 'access_control_lists', None)
    #end get_access_control_lists

    def get_floating_ip_pools(self):
        return getattr(self, 'floating_ip_pools', None)
    #end get_floating_ip_pools

    def get_routing_instances(self):
        return getattr(self, 'routing_instances', None)
    #end get_routing_instances

    def set_qos_forwarding_class(self, ref_obj):
        """Set qos-forwarding-class for virtual-network.
        
        :param ref_obj: QosForwardingClass object
        
        """
        self.qos_forwarding_class_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.qos_forwarding_class_refs[0]['uuid'] = ref_obj.uuid

    #end set_qos_forwarding_class

    def add_qos_forwarding_class(self, ref_obj):
        """Add qos-forwarding-class to virtual-network.
        
        :param ref_obj: QosForwardingClass object
        
        """
        refs = getattr(self, 'qos_forwarding_class_refs', [])
        if not refs:
            self.qos_forwarding_class_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.qos_forwarding_class_refs.append(ref_info)
    #end add_qos_forwarding_class

    def del_qos_forwarding_class(self, ref_obj):
        refs = self.get_qos_forwarding_class_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.qos_forwarding_class_refs.remove(ref)
                return
    #end del_qos_forwarding_class

    def set_qos_forwarding_class_list(self, ref_obj_list):
        """Set qos-forwarding-class list for virtual-network.
        
        :param ref_obj_list: list of QosForwardingClass object
        
        """
        self.qos_forwarding_class_refs = ref_obj_list
    #end set_qos_forwarding_class_list

    def get_qos_forwarding_class_refs(self):
        """Return qos-forwarding-class list for virtual-network.
        
        :returns: list of <QosForwardingClass>
        
        """
        return getattr(self, 'qos_forwarding_class_refs', None)
    #end get_qos_forwarding_class_refs

    def set_network_ipam(self, ref_obj, ref_data):
        """Set network-ipam for virtual-network.
        
        :param ref_obj: NetworkIpam object
        :param ref_data: VnSubnetsType object
        
        """
        self.network_ipam_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.network_ipam_refs[0]['uuid'] = ref_obj.uuid

    #end set_network_ipam

    def add_network_ipam(self, ref_obj, ref_data):
        """Add network-ipam to virtual-network.
        
        :param ref_obj: NetworkIpam object
        :param ref_data: VnSubnetsType object
        
        """
        refs = getattr(self, 'network_ipam_refs', [])
        if not refs:
            self.network_ipam_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.network_ipam_refs.append(ref_info)
    #end add_network_ipam

    def del_network_ipam(self, ref_obj):
        refs = self.get_network_ipam_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.network_ipam_refs.remove(ref)
                return
    #end del_network_ipam

    def set_network_ipam_list(self, ref_obj_list, ref_data_list):
        """Set network-ipam list for virtual-network.
        
        :param ref_obj_list: list of NetworkIpam object
        :param ref_data_list: list of VnSubnetsType object
        
        """
        self.network_ipam_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_network_ipam_list

    def get_network_ipam_refs(self):
        """Return network-ipam list for virtual-network.
        
        :returns: list of tuple <NetworkIpam, VnSubnetsType>
        
        """
        return getattr(self, 'network_ipam_refs', None)
    #end get_network_ipam_refs

    def set_network_policy(self, ref_obj, ref_data):
        """Set network-policy for virtual-network.
        
        :param ref_obj: NetworkPolicy object
        :param ref_data: VirtualNetworkPolicyType object
        
        """
        self.network_policy_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.network_policy_refs[0]['uuid'] = ref_obj.uuid

    #end set_network_policy

    def add_network_policy(self, ref_obj, ref_data):
        """Add network-policy to virtual-network.
        
        :param ref_obj: NetworkPolicy object
        :param ref_data: VirtualNetworkPolicyType object
        
        """
        refs = getattr(self, 'network_policy_refs', [])
        if not refs:
            self.network_policy_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.network_policy_refs.append(ref_info)
    #end add_network_policy

    def del_network_policy(self, ref_obj):
        refs = self.get_network_policy_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.network_policy_refs.remove(ref)
                return
    #end del_network_policy

    def set_network_policy_list(self, ref_obj_list, ref_data_list):
        """Set network-policy list for virtual-network.
        
        :param ref_obj_list: list of NetworkPolicy object
        :param ref_data_list: list of VirtualNetworkPolicyType object
        
        """
        self.network_policy_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_network_policy_list

    def get_network_policy_refs(self):
        """Return network-policy list for virtual-network.
        
        :returns: list of tuple <NetworkPolicy, VirtualNetworkPolicyType>
        
        """
        return getattr(self, 'network_policy_refs', None)
    #end get_network_policy_refs

    def set_route_table(self, ref_obj):
        """Set route-table for virtual-network.
        
        :param ref_obj: RouteTable object
        
        """
        self.route_table_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.route_table_refs[0]['uuid'] = ref_obj.uuid

    #end set_route_table

    def add_route_table(self, ref_obj):
        """Add route-table to virtual-network.
        
        :param ref_obj: RouteTable object
        
        """
        refs = getattr(self, 'route_table_refs', [])
        if not refs:
            self.route_table_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.route_table_refs.append(ref_info)
    #end add_route_table

    def del_route_table(self, ref_obj):
        refs = self.get_route_table_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.route_table_refs.remove(ref)
                return
    #end del_route_table

    def set_route_table_list(self, ref_obj_list):
        """Set route-table list for virtual-network.
        
        :param ref_obj_list: list of RouteTable object
        
        """
        self.route_table_refs = ref_obj_list
    #end set_route_table_list

    def get_route_table_refs(self):
        """Return route-table list for virtual-network.
        
        :returns: list of <RouteTable>
        
        """
        return getattr(self, 'route_table_refs', None)
    #end get_route_table_refs

    def get_project_back_refs(self):
        """Return list of all projects using this virtual-network"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this virtual-network"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def get_instance_ip_back_refs(self):
        """Return list of all instance-ips using this virtual-network"""
        return getattr(self, 'instance_ip_back_refs', None)
    #end get_instance_ip_back_refs

    def get_physical_router_back_refs(self):
        """Return list of all physical-routers using this virtual-network"""
        return getattr(self, 'physical_router_back_refs', None)
    #end get_physical_router_back_refs

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this virtual-network"""
        return getattr(self, 'logical_router_back_refs', None)
    #end get_logical_router_back_refs

    def dump(self):
        """Display virtual-network object in compact form."""
        print '------------ virtual-network ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_network_properties = ', self.get_virtual_network_properties()
        print 'P virtual_network_network_id = ', self.get_virtual_network_network_id()
        print 'P route_target_list = ', self.get_route_target_list()
        print 'P router_external = ', self.get_router_external()
        print 'P is_shared = ', self.get_is_shared()
        print 'P external_ipam = ', self.get_external_ipam()
        print 'P flood_unknown_unicast = ', self.get_flood_unknown_unicast()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF qos_forwarding_class = ', self.get_qos_forwarding_class_refs()
        print 'REF network_ipam = ', self.get_network_ipam_refs()
        print 'REF network_policy = ', self.get_network_policy_refs()
        print 'HAS access_control_list = ', self.get_access_control_lists()
        print 'HAS floating_ip_pool = ', self.get_floating_ip_pools()
        print 'HAS routing_instance = ', self.get_routing_instances()
        print 'REF route_table = ', self.get_route_table_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
        print 'BCK instance_ip = ', self.get_instance_ip_back_refs()
        print 'BCK physical_router = ', self.get_physical_router_back_refs()
        print 'BCK logical_router = ', self.get_logical_router_back_refs()
    #end dump

#end class VirtualNetwork

class Project(object):
    """
    Represents project configuration representation.

    Child of:
        :class:`.Domain` object OR

    Properties:
        * quota (:class:`.QuotaType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.SecurityGroup` objects
        * list of :class:`.VirtualNetwork` objects
        * list of :class:`.QosQueue` objects
        * list of :class:`.QosForwardingClass` objects
        * list of :class:`.NetworkIpam` objects
        * list of :class:`.NetworkPolicy` objects
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.ServiceInstance` objects
        * list of :class:`.RouteTable` objects
        * list of :class:`.InterfaceRouteTable` objects
        * list of :class:`.LogicalRouter` objects
        * list of :class:`.LoadbalancerPool` objects
        * list of :class:`.LoadbalancerHealthmonitor` objects
        * list of :class:`.VirtualIp` objects

    References to:
        * list of (:class:`.Namespace` object, :class:`.SubnetType` attribute)
        * list of :class:`.FloatingIpPool` objects

    Referred by:
        * list of :class:`.FloatingIp` objects
    """

    prop_fields = set([u'quota', u'id_perms', u'display_name'])
    ref_fields = set([u'namespace_refs', u'floating_ip_pool_refs'])
    backref_fields = set([u'domain_back_refs', u'floating_ip_back_refs'])
    children_fields = set([u'security_groups', u'virtual_networks', u'qos_queues', u'qos_forwarding_classs', u'network_ipams', u'network_policys', 'virtual_machine_interfaces', u'service_instances', u'route_tables', u'interface_route_tables', u'logical_routers', u'loadbalancer_pools', u'loadbalancer_healthmonitors', u'virtual_ips'])

    def __init__(self, name = None, parent_obj = None, quota = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'project'
        if not name:
            name = u'default-project'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'domain'
            self.fq_name = [u'default-domain']
            self.fq_name.append(name)


        # property fields
        if quota:
            self._quota = quota
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (project)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of project in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of project as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of project's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of project's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def quota(self):
        """Get quota for project.
        
        :returns: QuotaType object
        
        """
        return getattr(self, '_quota', None)
    #end quota

    @quota.setter
    def quota(self, quota):
        """Set quota for project.
        
        :param quota: QuotaType object
        
        """
        self._quota = quota
    #end quota

    def set_quota(self, value):
        self.quota = value
    #end set_quota

    def get_quota(self):
        return self.quota
    #end get_quota

    @property
    def id_perms(self):
        """Get id-perms for project.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for project.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for project.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for project.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_quota'):
            self._serialize_field_to_json(serialized, field_names, 'quota')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'namespace_refs'):
            self._serialize_field_to_json(serialized, field_names, 'namespace_refs')
        if hasattr(self, 'floating_ip_pool_refs'):
            self._serialize_field_to_json(serialized, field_names, 'floating_ip_pool_refs')
        return serialized
    #end serialize_to_json

    def get_security_groups(self):
        return getattr(self, 'security_groups', None)
    #end get_security_groups

    def get_virtual_networks(self):
        return getattr(self, 'virtual_networks', None)
    #end get_virtual_networks

    def get_qos_queues(self):
        return getattr(self, 'qos_queues', None)
    #end get_qos_queues

    def get_qos_forwarding_classs(self):
        return getattr(self, 'qos_forwarding_classs', None)
    #end get_qos_forwarding_classs

    def get_network_ipams(self):
        return getattr(self, 'network_ipams', None)
    #end get_network_ipams

    def get_network_policys(self):
        return getattr(self, 'network_policys', None)
    #end get_network_policys

    def get_virtual_machine_interfaces(self):
        return getattr(self, 'virtual_machine_interfaces', None)
    #end get_virtual_machine_interfaces

    def get_service_instances(self):
        return getattr(self, 'service_instances', None)
    #end get_service_instances

    def get_route_tables(self):
        return getattr(self, 'route_tables', None)
    #end get_route_tables

    def get_interface_route_tables(self):
        return getattr(self, 'interface_route_tables', None)
    #end get_interface_route_tables

    def get_logical_routers(self):
        return getattr(self, 'logical_routers', None)
    #end get_logical_routers

    def get_loadbalancer_pools(self):
        return getattr(self, 'loadbalancer_pools', None)
    #end get_loadbalancer_pools

    def get_loadbalancer_healthmonitors(self):
        return getattr(self, 'loadbalancer_healthmonitors', None)
    #end get_loadbalancer_healthmonitors

    def get_virtual_ips(self):
        return getattr(self, 'virtual_ips', None)
    #end get_virtual_ips

    def set_namespace(self, ref_obj, ref_data):
        """Set namespace for project.
        
        :param ref_obj: Namespace object
        :param ref_data: SubnetType object
        
        """
        self.namespace_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.namespace_refs[0]['uuid'] = ref_obj.uuid

    #end set_namespace

    def add_namespace(self, ref_obj, ref_data):
        """Add namespace to project.
        
        :param ref_obj: Namespace object
        :param ref_data: SubnetType object
        
        """
        refs = getattr(self, 'namespace_refs', [])
        if not refs:
            self.namespace_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.namespace_refs.append(ref_info)
    #end add_namespace

    def del_namespace(self, ref_obj):
        refs = self.get_namespace_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.namespace_refs.remove(ref)
                return
    #end del_namespace

    def set_namespace_list(self, ref_obj_list, ref_data_list):
        """Set namespace list for project.
        
        :param ref_obj_list: list of Namespace object
        :param ref_data_list: list of SubnetType object
        
        """
        self.namespace_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_namespace_list

    def get_namespace_refs(self):
        """Return namespace list for project.
        
        :returns: list of tuple <Namespace, SubnetType>
        
        """
        return getattr(self, 'namespace_refs', None)
    #end get_namespace_refs

    def set_floating_ip_pool(self, ref_obj):
        """Set floating-ip-pool for project.
        
        :param ref_obj: FloatingIpPool object
        
        """
        self.floating_ip_pool_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.floating_ip_pool_refs[0]['uuid'] = ref_obj.uuid

    #end set_floating_ip_pool

    def add_floating_ip_pool(self, ref_obj):
        """Add floating-ip-pool to project.
        
        :param ref_obj: FloatingIpPool object
        
        """
        refs = getattr(self, 'floating_ip_pool_refs', [])
        if not refs:
            self.floating_ip_pool_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.floating_ip_pool_refs.append(ref_info)
    #end add_floating_ip_pool

    def del_floating_ip_pool(self, ref_obj):
        refs = self.get_floating_ip_pool_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.floating_ip_pool_refs.remove(ref)
                return
    #end del_floating_ip_pool

    def set_floating_ip_pool_list(self, ref_obj_list):
        """Set floating-ip-pool list for project.
        
        :param ref_obj_list: list of FloatingIpPool object
        
        """
        self.floating_ip_pool_refs = ref_obj_list
    #end set_floating_ip_pool_list

    def get_floating_ip_pool_refs(self):
        """Return floating-ip-pool list for project.
        
        :returns: list of <FloatingIpPool>
        
        """
        return getattr(self, 'floating_ip_pool_refs', None)
    #end get_floating_ip_pool_refs

    def get_domain_back_refs(self):
        """Return list of all domains using this project"""
        return getattr(self, 'domain_back_refs', None)
    #end get_domain_back_refs

    def get_floating_ip_back_refs(self):
        """Return list of all floating-ips using this project"""
        return getattr(self, 'floating_ip_back_refs', None)
    #end get_floating_ip_back_refs

    def dump(self):
        """Display project object in compact form."""
        print '------------ project ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P quota = ', self.get_quota()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF namespace = ', self.get_namespace_refs()
        print 'HAS security_group = ', self.get_security_groups()
        print 'HAS virtual_network = ', self.get_virtual_networks()
        print 'HAS qos_queue = ', self.get_qos_queues()
        print 'HAS qos_forwarding_class = ', self.get_qos_forwarding_classs()
        print 'HAS network_ipam = ', self.get_network_ipams()
        print 'HAS network_policy = ', self.get_network_policys()
        print 'HAS virtual_machine_interface = ', self.get_virtual_machine_interfaces()
        print 'REF floating_ip_pool = ', self.get_floating_ip_pool_refs()
        print 'HAS service_instance = ', self.get_service_instances()
        print 'HAS route_table = ', self.get_route_tables()
        print 'HAS interface_route_table = ', self.get_interface_route_tables()
        print 'HAS logical_router = ', self.get_logical_routers()
        print 'HAS loadbalancer_pool = ', self.get_loadbalancer_pools()
        print 'HAS loadbalancer_healthmonitor = ', self.get_loadbalancer_healthmonitors()
        print 'HAS virtual_ip = ', self.get_virtual_ips()
        print 'BCK floating_ip = ', self.get_floating_ip_back_refs()
    #end dump

#end class Project

class QosForwardingClass(object):
    """
    Represents qos-forwarding-class configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * dscp (xsd:integer type)
        * trusted (xsd:boolean type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.QosQueue` objects

    Referred by:
        * list of :class:`.VirtualNetwork` objects
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'dscp', u'trusted', u'id_perms', u'display_name'])
    ref_fields = set([u'qos_queue_refs'])
    backref_fields = set([u'project_back_refs', u'virtual_network_back_refs', 'virtual_machine_interface_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, dscp = None, trusted = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'qos-forwarding-class'
        if not name:
            name = u'default-qos-forwarding-class'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if dscp:
            self._dscp = dscp
        if trusted:
            self._trusted = trusted
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (qos-forwarding-class)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of qos-forwarding-class in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of qos-forwarding-class as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of qos-forwarding-class's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of qos-forwarding-class's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def dscp(self):
        """Get dscp for qos-forwarding-class.
        
        :returns: xsd:integer object
        
        """
        return getattr(self, '_dscp', None)
    #end dscp

    @dscp.setter
    def dscp(self, dscp):
        """Set dscp for qos-forwarding-class.
        
        :param dscp: xsd:integer object
        
        """
        self._dscp = dscp
    #end dscp

    def set_dscp(self, value):
        self.dscp = value
    #end set_dscp

    def get_dscp(self):
        return self.dscp
    #end get_dscp

    @property
    def trusted(self):
        """Get trusted for qos-forwarding-class.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_trusted', None)
    #end trusted

    @trusted.setter
    def trusted(self, trusted):
        """Set trusted for qos-forwarding-class.
        
        :param trusted: xsd:boolean object
        
        """
        self._trusted = trusted
    #end trusted

    def set_trusted(self, value):
        self.trusted = value
    #end set_trusted

    def get_trusted(self):
        return self.trusted
    #end get_trusted

    @property
    def id_perms(self):
        """Get id-perms for qos-forwarding-class.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for qos-forwarding-class.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for qos-forwarding-class.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for qos-forwarding-class.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_dscp'):
            self._serialize_field_to_json(serialized, field_names, 'dscp')
        if hasattr(self, '_trusted'):
            self._serialize_field_to_json(serialized, field_names, 'trusted')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'qos_queue_refs'):
            self._serialize_field_to_json(serialized, field_names, 'qos_queue_refs')
        return serialized
    #end serialize_to_json

    def set_qos_queue(self, ref_obj):
        """Set qos-queue for qos-forwarding-class.
        
        :param ref_obj: QosQueue object
        
        """
        self.qos_queue_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.qos_queue_refs[0]['uuid'] = ref_obj.uuid

    #end set_qos_queue

    def add_qos_queue(self, ref_obj):
        """Add qos-queue to qos-forwarding-class.
        
        :param ref_obj: QosQueue object
        
        """
        refs = getattr(self, 'qos_queue_refs', [])
        if not refs:
            self.qos_queue_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.qos_queue_refs.append(ref_info)
    #end add_qos_queue

    def del_qos_queue(self, ref_obj):
        refs = self.get_qos_queue_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.qos_queue_refs.remove(ref)
                return
    #end del_qos_queue

    def set_qos_queue_list(self, ref_obj_list):
        """Set qos-queue list for qos-forwarding-class.
        
        :param ref_obj_list: list of QosQueue object
        
        """
        self.qos_queue_refs = ref_obj_list
    #end set_qos_queue_list

    def get_qos_queue_refs(self):
        """Return qos-queue list for qos-forwarding-class.
        
        :returns: list of <QosQueue>
        
        """
        return getattr(self, 'qos_queue_refs', None)
    #end get_qos_queue_refs

    def get_project_back_refs(self):
        """Return list of all projects using this qos-forwarding-class"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this qos-forwarding-class"""
        return getattr(self, 'virtual_network_back_refs', None)
    #end get_virtual_network_back_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this qos-forwarding-class"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def dump(self):
        """Display qos-forwarding-class object in compact form."""
        print '------------ qos-forwarding-class ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P dscp = ', self.get_dscp()
        print 'P trusted = ', self.get_trusted()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF qos_queue = ', self.get_qos_queue_refs()
        print 'BCK virtual_network = ', self.get_virtual_network_back_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class QosForwardingClass

class DatabaseNode(object):
    """
    Represents database-node configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * database-node-ip-address (IpAddressType type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'database_node_ip_address', u'id_perms', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'global_system_config_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, database_node_ip_address = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'database-node'
        if not name:
            name = u'default-database-node'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'global-system-config'
            self.fq_name = [u'default-global-system-config']
            self.fq_name.append(name)


        # property fields
        if database_node_ip_address:
            self._database_node_ip_address = database_node_ip_address
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (database-node)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of database-node in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of database-node as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of database-node's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of database-node's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def database_node_ip_address(self):
        """Get database-node-ip-address for database-node.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_database_node_ip_address', None)
    #end database_node_ip_address

    @database_node_ip_address.setter
    def database_node_ip_address(self, database_node_ip_address):
        """Set database-node-ip-address for database-node.
        
        :param database_node_ip_address: IpAddressType object
        
        """
        self._database_node_ip_address = database_node_ip_address
    #end database_node_ip_address

    def set_database_node_ip_address(self, value):
        self.database_node_ip_address = value
    #end set_database_node_ip_address

    def get_database_node_ip_address(self):
        return self.database_node_ip_address
    #end get_database_node_ip_address

    @property
    def id_perms(self):
        """Get id-perms for database-node.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for database-node.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for database-node.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for database-node.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_database_node_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'database_node_ip_address')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_global_system_config_back_refs(self):
        """Return list of all global-system-configs using this database-node"""
        return getattr(self, 'global_system_config_back_refs', None)
    #end get_global_system_config_back_refs

    def dump(self):
        """Display database-node object in compact form."""
        print '------------ database-node ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P database_node_ip_address = ', self.get_database_node_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class DatabaseNode

class RoutingInstance(object):
    """
    Represents routing-instance configuration representation.

    Child of:
        :class:`.VirtualNetwork` object OR

    Properties:
        * service-chain-information (:class:`.ServiceChainInfo` type)
        * routing-instance-is-default (xsd:boolean type)
        * static-route-entries (:class:`.StaticRouteEntriesType` type)
        * default-ce-protocol (:class:`.DefaultProtocolType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:
        * list of :class:`.BgpRouter` objects

    References to:
        * list of (:class:`.RoutingInstance` object, :class:`.ConnectionType` attribute)
        * list of (:class:`.RouteTarget` object, :class:`.InstanceTargetType` attribute)

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.RoutingInstance` objects
    """

    prop_fields = set([u'service_chain_information', u'routing_instance_is_default', u'static_route_entries', u'default_ce_protocol', u'id_perms', u'display_name'])
    ref_fields = set(['routing_instance_refs', 'route_target_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs', u'virtual_network_back_refs', 'routing_instance_back_refs', 'customer_attachment_back_refs'])
    children_fields = set(['bgp_routers'])

    def __init__(self, name = None, parent_obj = None, service_chain_information = None, routing_instance_is_default = None, static_route_entries = None, default_ce_protocol = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'routing-instance'
        if not name:
            name = u'default-routing-instance'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'virtual-network'
            self.fq_name = [u'default-domain', u'default-project', u'default-virtual-network']
            self.fq_name.append(name)


        # property fields
        if service_chain_information:
            self._service_chain_information = service_chain_information
        if routing_instance_is_default:
            self._routing_instance_is_default = routing_instance_is_default
        if static_route_entries:
            self._static_route_entries = static_route_entries
        if default_ce_protocol:
            self._default_ce_protocol = default_ce_protocol
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (routing-instance)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of routing-instance in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of routing-instance as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of routing-instance's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of routing-instance's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def service_chain_information(self):
        """Get service-chain-information for routing-instance.
        
        :returns: ServiceChainInfo object
        
        """
        return getattr(self, '_service_chain_information', None)
    #end service_chain_information

    @service_chain_information.setter
    def service_chain_information(self, service_chain_information):
        """Set service-chain-information for routing-instance.
        
        :param service_chain_information: ServiceChainInfo object
        
        """
        self._service_chain_information = service_chain_information
    #end service_chain_information

    def set_service_chain_information(self, value):
        self.service_chain_information = value
    #end set_service_chain_information

    def get_service_chain_information(self):
        return self.service_chain_information
    #end get_service_chain_information

    @property
    def routing_instance_is_default(self):
        """Get routing-instance-is-default for routing-instance.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_routing_instance_is_default', None)
    #end routing_instance_is_default

    @routing_instance_is_default.setter
    def routing_instance_is_default(self, routing_instance_is_default):
        """Set routing-instance-is-default for routing-instance.
        
        :param routing_instance_is_default: xsd:boolean object
        
        """
        self._routing_instance_is_default = routing_instance_is_default
    #end routing_instance_is_default

    def set_routing_instance_is_default(self, value):
        self.routing_instance_is_default = value
    #end set_routing_instance_is_default

    def get_routing_instance_is_default(self):
        return self.routing_instance_is_default
    #end get_routing_instance_is_default

    @property
    def static_route_entries(self):
        """Get static-route-entries for routing-instance.
        
        :returns: StaticRouteEntriesType object
        
        """
        return getattr(self, '_static_route_entries', None)
    #end static_route_entries

    @static_route_entries.setter
    def static_route_entries(self, static_route_entries):
        """Set static-route-entries for routing-instance.
        
        :param static_route_entries: StaticRouteEntriesType object
        
        """
        self._static_route_entries = static_route_entries
    #end static_route_entries

    def set_static_route_entries(self, value):
        self.static_route_entries = value
    #end set_static_route_entries

    def get_static_route_entries(self):
        return self.static_route_entries
    #end get_static_route_entries

    @property
    def default_ce_protocol(self):
        """Get default-ce-protocol for routing-instance.
        
        :returns: DefaultProtocolType object
        
        """
        return getattr(self, '_default_ce_protocol', None)
    #end default_ce_protocol

    @default_ce_protocol.setter
    def default_ce_protocol(self, default_ce_protocol):
        """Set default-ce-protocol for routing-instance.
        
        :param default_ce_protocol: DefaultProtocolType object
        
        """
        self._default_ce_protocol = default_ce_protocol
    #end default_ce_protocol

    def set_default_ce_protocol(self, value):
        self.default_ce_protocol = value
    #end set_default_ce_protocol

    def get_default_ce_protocol(self):
        return self.default_ce_protocol
    #end get_default_ce_protocol

    @property
    def id_perms(self):
        """Get id-perms for routing-instance.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for routing-instance.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for routing-instance.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for routing-instance.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_service_chain_information'):
            self._serialize_field_to_json(serialized, field_names, 'service_chain_information')
        if hasattr(self, '_routing_instance_is_default'):
            self._serialize_field_to_json(serialized, field_names, 'routing_instance_is_default')
        if hasattr(self, '_static_route_entries'):
            self._serialize_field_to_json(serialized, field_names, 'static_route_entries')
        if hasattr(self, '_default_ce_protocol'):
            self._serialize_field_to_json(serialized, field_names, 'default_ce_protocol')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'routing_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'routing_instance_refs')
        if hasattr(self, 'route_target_refs'):
            self._serialize_field_to_json(serialized, field_names, 'route_target_refs')
        return serialized
    #end serialize_to_json

    def get_bgp_routers(self):
        return getattr(self, 'bgp_routers', None)
    #end get_bgp_routers

    def set_routing_instance(self, ref_obj, ref_data):
        """Set routing-instance for routing-instance.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: ConnectionType object
        
        """
        self.routing_instance_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.routing_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_routing_instance

    def add_routing_instance(self, ref_obj, ref_data):
        """Add routing-instance to routing-instance.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: ConnectionType object
        
        """
        refs = getattr(self, 'routing_instance_refs', [])
        if not refs:
            self.routing_instance_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.routing_instance_refs.append(ref_info)
    #end add_routing_instance

    def del_routing_instance(self, ref_obj):
        refs = self.get_routing_instance_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.routing_instance_refs.remove(ref)
                return
    #end del_routing_instance

    def set_routing_instance_list(self, ref_obj_list, ref_data_list):
        """Set routing-instance list for routing-instance.
        
        :param ref_obj_list: list of RoutingInstance object
        :param ref_data_list: list of ConnectionType object
        
        """
        self.routing_instance_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_routing_instance_list

    def get_routing_instance_refs(self):
        """Return routing-instance list for routing-instance.
        
        :returns: list of tuple <RoutingInstance, ConnectionType>
        
        """
        return getattr(self, 'routing_instance_refs', None)
    #end get_routing_instance_refs

    def set_route_target(self, ref_obj, ref_data):
        """Set route-target for routing-instance.
        
        :param ref_obj: RouteTarget object
        :param ref_data: InstanceTargetType object
        
        """
        self.route_target_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.route_target_refs[0]['uuid'] = ref_obj.uuid

    #end set_route_target

    def add_route_target(self, ref_obj, ref_data):
        """Add route-target to routing-instance.
        
        :param ref_obj: RouteTarget object
        :param ref_data: InstanceTargetType object
        
        """
        refs = getattr(self, 'route_target_refs', [])
        if not refs:
            self.route_target_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name(), 'attr':ref_data}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.route_target_refs.append(ref_info)
    #end add_route_target

    def del_route_target(self, ref_obj):
        refs = self.get_route_target_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.route_target_refs.remove(ref)
                return
    #end del_route_target

    def set_route_target_list(self, ref_obj_list, ref_data_list):
        """Set route-target list for routing-instance.
        
        :param ref_obj_list: list of RouteTarget object
        :param ref_data_list: list of InstanceTargetType object
        
        """
        self.route_target_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_route_target_list

    def get_route_target_refs(self):
        """Return route-target list for routing-instance.
        
        :returns: list of tuple <RouteTarget, InstanceTargetType>
        
        """
        return getattr(self, 'route_target_refs', None)
    #end get_route_target_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this routing-instance"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this routing-instance"""
        return getattr(self, 'virtual_network_back_refs', None)
    #end get_virtual_network_back_refs

    def get_routing_instance_back_refs(self):
        """Return list of all routing-instances using this routing-instance"""
        return getattr(self, 'routing_instance_back_refs', None)
    #end get_routing_instance_back_refs

    def get_customer_attachment_back_refs(self):
        """Return list of all customer-attachments using this routing-instance"""
        return getattr(self, 'customer_attachment_back_refs', None)
    #end get_customer_attachment_back_refs

    def dump(self):
        """Display routing-instance object in compact form."""
        print '------------ routing-instance ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_chain_information = ', self.get_service_chain_information()
        print 'P routing_instance_is_default = ', self.get_routing_instance_is_default()
        print 'P static_route_entries = ', self.get_static_route_entries()
        print 'P default_ce_protocol = ', self.get_default_ce_protocol()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'HAS bgp_router = ', self.get_bgp_routers()
        print 'REF routing_instance = ', self.get_routing_instance_refs()
        print 'REF route_target = ', self.get_route_target_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
        print 'BCK routing_instance = ', self.get_routing_instance_back_refs()
    #end dump

#end class RoutingInstance

class NetworkIpam(object):
    """
    Represents network-ipam configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * network-ipam-mgmt (:class:`.IpamType` type)
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.VirtualDns` objects

    Referred by:
        * list of :class:`.VirtualNetwork` objects
    """

    prop_fields = set([u'network_ipam_mgmt', u'id_perms', u'display_name'])
    ref_fields = set([u'virtual_DNS_refs'])
    backref_fields = set([u'project_back_refs', u'virtual_network_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, network_ipam_mgmt = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'network-ipam'
        if not name:
            name = u'default-network-ipam'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if network_ipam_mgmt:
            self._network_ipam_mgmt = network_ipam_mgmt
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (network-ipam)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of network-ipam in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of network-ipam as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of network-ipam's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of network-ipam's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def network_ipam_mgmt(self):
        """Get network-ipam-mgmt for network-ipam.
        
        :returns: IpamType object
        
        """
        return getattr(self, '_network_ipam_mgmt', None)
    #end network_ipam_mgmt

    @network_ipam_mgmt.setter
    def network_ipam_mgmt(self, network_ipam_mgmt):
        """Set network-ipam-mgmt for network-ipam.
        
        :param network_ipam_mgmt: IpamType object
        
        """
        self._network_ipam_mgmt = network_ipam_mgmt
    #end network_ipam_mgmt

    def set_network_ipam_mgmt(self, value):
        self.network_ipam_mgmt = value
    #end set_network_ipam_mgmt

    def get_network_ipam_mgmt(self):
        return self.network_ipam_mgmt
    #end get_network_ipam_mgmt

    @property
    def id_perms(self):
        """Get id-perms for network-ipam.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for network-ipam.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for network-ipam.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for network-ipam.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_network_ipam_mgmt'):
            self._serialize_field_to_json(serialized, field_names, 'network_ipam_mgmt')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_DNS_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_DNS_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_DNS(self, ref_obj):
        """Set virtual-DNS for network-ipam.
        
        :param ref_obj: VirtualDns object
        
        """
        self.virtual_DNS_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_DNS_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_DNS

    def add_virtual_DNS(self, ref_obj):
        """Add virtual-DNS to network-ipam.
        
        :param ref_obj: VirtualDns object
        
        """
        refs = getattr(self, 'virtual_DNS_refs', [])
        if not refs:
            self.virtual_DNS_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_DNS_refs.append(ref_info)
    #end add_virtual_DNS

    def del_virtual_DNS(self, ref_obj):
        refs = self.get_virtual_DNS_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_DNS_refs.remove(ref)
                return
    #end del_virtual_DNS

    def set_virtual_DNS_list(self, ref_obj_list):
        """Set virtual-DNS list for network-ipam.
        
        :param ref_obj_list: list of VirtualDns object
        
        """
        self.virtual_DNS_refs = ref_obj_list
    #end set_virtual_DNS_list

    def get_virtual_DNS_refs(self):
        """Return virtual-DNS list for network-ipam.
        
        :returns: list of <VirtualDns>
        
        """
        return getattr(self, 'virtual_DNS_refs', None)
    #end get_virtual_DNS_refs

    def get_project_back_refs(self):
        """Return list of all projects using this network-ipam"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def get_virtual_network_back_refs(self):
        """Return list of all virtual-networks using this network-ipam"""
        return getattr(self, 'virtual_network_back_refs', None)
    #end get_virtual_network_back_refs

    def dump(self):
        """Display network-ipam object in compact form."""
        print '------------ network-ipam ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P network_ipam_mgmt = ', self.get_network_ipam_mgmt()
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_DNS = ', self.get_virtual_DNS_refs()
        print 'BCK virtual_network = ', self.get_virtual_network_back_refs()
    #end dump

#end class NetworkIpam

class LogicalRouter(object):
    """
    Represents logical-router configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * id-perms (:class:`.IdPermsType` type)
        * display-name (xsd:string type)

    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.RouteTarget` objects
        * list of :class:`.VirtualNetwork` objects
        * list of :class:`.ServiceInstance` objects

    Referred by:
    """

    prop_fields = set([u'id_perms', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs', 'route_target_refs', u'virtual_network_refs', u'service_instance_refs'])
    backref_fields = set([u'project_back_refs'])
    children_fields = set([])

    def __init__(self, name = None, parent_obj = None, id_perms = None, display_name = None, *args, **kwargs):
        # type-independent fields
        self._type = 'logical-router'
        if not name:
            name = u'default-logical-router'
        self.name = name
        self._uuid = None
        # Determine parent type and fq_name
        kwargs_parent_type = kwargs.get('parent_type', None)
        kwargs_fq_name = kwargs.get('fq_name', None)
        if parent_obj:
            self.parent_type = parent_obj._type
            # copy parent's fq_name
            self.fq_name = list(parent_obj.fq_name)
            self.fq_name.append(name)
        elif kwargs_parent_type and kwargs_fq_name:
            self.parent_type = kwargs_parent_type
            self.fq_name = kwargs_fq_name
        else: # No parent obj specified
            self.parent_type = 'project'
            self.fq_name = [u'default-domain', u'default-project']
            self.fq_name.append(name)


        # property fields
        if id_perms:
            self._id_perms = id_perms
        if display_name:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (logical-router)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of logical-router in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of logical-router as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of logical-router's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of logical-router's parent as colon delimted string."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return ':'.join(self.fq_name[:-1])
    #end get_parent_fq_name_str

    @property
    def uuid(self):
        return getattr(self, '_uuid', None)
    #end uuid

    @uuid.setter
    def uuid(self, uuid_val):
        self._uuid = uuid_val
    #end uuid

    def set_uuid(self, uuid_val):
        self.uuid = uuid_val
    #end set_uuid

    def get_uuid(self):
        return self.uuid
    #end get_uuid

    @property
    def id_perms(self):
        """Get id-perms for logical-router.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for logical-router.
        
        :param id_perms: IdPermsType object
        
        """
        self._id_perms = id_perms
    #end id_perms

    def set_id_perms(self, value):
        self.id_perms = value
    #end set_id_perms

    def get_id_perms(self):
        return self.id_perms
    #end get_id_perms

    @property
    def display_name(self):
        """Get display-name for logical-router.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for logical-router.
        
        :param display_name: xsd:string object
        
        """
        self._display_name = display_name
    #end display_name

    def set_display_name(self, value):
        self.display_name = value
    #end set_display_name

    def get_display_name(self):
        return self.display_name
    #end get_display_name

    def _serialize_field_to_json(self, serialized, fields_to_serialize, field_name):
        if fields_to_serialize is None: # all fields are serialized
            serialized[field_name] = getattr(self, field_name)
        elif field_name in fields_to_serialize:
            serialized[field_name] = getattr(self, field_name)
    #end _serialize_field_to_json

    def serialize_to_json(self, field_names = None):
        serialized = {}

        # serialize common fields
        self._serialize_field_to_json(serialized, ['uuid'], 'uuid')
        self._serialize_field_to_json(serialized, field_names, 'fq_name')
        if hasattr(self, 'parent_type'):
            self._serialize_field_to_json(serialized, field_names, 'parent_type')

        # serialize property fields
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        if hasattr(self, 'route_target_refs'):
            self._serialize_field_to_json(serialized, field_names, 'route_target_refs')
        if hasattr(self, 'virtual_network_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_refs')
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for logical-router.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to logical-router.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        refs = getattr(self, 'virtual_machine_interface_refs', [])
        if not refs:
            self.virtual_machine_interface_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_machine_interface_refs.append(ref_info)
    #end add_virtual_machine_interface

    def del_virtual_machine_interface(self, ref_obj):
        refs = self.get_virtual_machine_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_machine_interface_refs.remove(ref)
                return
    #end del_virtual_machine_interface

    def set_virtual_machine_interface_list(self, ref_obj_list):
        """Set virtual-machine-interface list for logical-router.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for logical-router.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def set_route_target(self, ref_obj):
        """Set route-target for logical-router.
        
        :param ref_obj: RouteTarget object
        
        """
        self.route_target_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.route_target_refs[0]['uuid'] = ref_obj.uuid

    #end set_route_target

    def add_route_target(self, ref_obj):
        """Add route-target to logical-router.
        
        :param ref_obj: RouteTarget object
        
        """
        refs = getattr(self, 'route_target_refs', [])
        if not refs:
            self.route_target_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.route_target_refs.append(ref_info)
    #end add_route_target

    def del_route_target(self, ref_obj):
        refs = self.get_route_target_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.route_target_refs.remove(ref)
                return
    #end del_route_target

    def set_route_target_list(self, ref_obj_list):
        """Set route-target list for logical-router.
        
        :param ref_obj_list: list of RouteTarget object
        
        """
        self.route_target_refs = ref_obj_list
    #end set_route_target_list

    def get_route_target_refs(self):
        """Return route-target list for logical-router.
        
        :returns: list of <RouteTarget>
        
        """
        return getattr(self, 'route_target_refs', None)
    #end get_route_target_refs

    def set_virtual_network(self, ref_obj):
        """Set virtual-network for logical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        self.virtual_network_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_network_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_network

    def add_virtual_network(self, ref_obj):
        """Add virtual-network to logical-router.
        
        :param ref_obj: VirtualNetwork object
        
        """
        refs = getattr(self, 'virtual_network_refs', [])
        if not refs:
            self.virtual_network_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.virtual_network_refs.append(ref_info)
    #end add_virtual_network

    def del_virtual_network(self, ref_obj):
        refs = self.get_virtual_network_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.virtual_network_refs.remove(ref)
                return
    #end del_virtual_network

    def set_virtual_network_list(self, ref_obj_list):
        """Set virtual-network list for logical-router.
        
        :param ref_obj_list: list of VirtualNetwork object
        
        """
        self.virtual_network_refs = ref_obj_list
    #end set_virtual_network_list

    def get_virtual_network_refs(self):
        """Return virtual-network list for logical-router.
        
        :returns: list of <VirtualNetwork>
        
        """
        return getattr(self, 'virtual_network_refs', None)
    #end get_virtual_network_refs

    def set_service_instance(self, ref_obj):
        """Set service-instance for logical-router.
        
        :param ref_obj: ServiceInstance object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj):
        """Add service-instance to logical-router.
        
        :param ref_obj: ServiceInstance object
        
        """
        refs = getattr(self, 'service_instance_refs', [])
        if not refs:
            self.service_instance_refs = []

        # if ref already exists, update any attr with it
        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                ref = {'to':ref_obj.get_fq_name()}
                if ref_obj.uuid:
                    ref['uuid'] = ref_obj.uuid
                return

        # ref didn't exist before
        ref_info = {'to':ref_obj.get_fq_name()}
        if ref_obj.uuid:
            ref_info['uuid'] = ref_obj.uuid

        self.service_instance_refs.append(ref_info)
    #end add_service_instance

    def del_service_instance(self, ref_obj):
        refs = self.get_service_instance_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.service_instance_refs.remove(ref)
                return
    #end del_service_instance

    def set_service_instance_list(self, ref_obj_list):
        """Set service-instance list for logical-router.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self.service_instance_refs = ref_obj_list
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for logical-router.
        
        :returns: list of <ServiceInstance>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

    def get_project_back_refs(self):
        """Return list of all projects using this logical-router"""
        return getattr(self, 'project_back_refs', None)
    #end get_project_back_refs

    def dump(self):
        """Display logical-router object in compact form."""
        print '------------ logical-router ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P id_perms = ', self.get_id_perms()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF route_target = ', self.get_route_target_refs()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'REF service_instance = ', self.get_service_instance_refs()
    #end dump

#end class LogicalRouter

