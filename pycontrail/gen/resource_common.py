
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
        * domain_limits
            Type: :class:`.DomainLimitsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.Project` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.Namespace` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ServiceTemplate` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualDns` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ApiAccessList` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:

    Referred by:
    """

    prop_fields = set([u'domain_limits', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([u'projects', u'namespaces', 'service_templates', u'virtual_DNSs', u'api_access_lists'])

    prop_field_types = {
        'domain_limits': {'xsd_type': u'DomainLimitsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}
    children_field_types['projects'] = ('project', False)
    children_field_types['namespaces'] = ('namespace', False)
    children_field_types['service_templates'] = ('service-template', False)
    children_field_types['virtual_DNSs'] = ('virtual-DNS', False)
    children_field_types['api_access_lists'] = ('api-access-list', False)

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['domain_limits'] = 'domain-limits'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}
    children_field_metas['projects'] = 'domain-project'
    children_field_metas['namespaces'] = 'domain-namespace'
    children_field_metas['service_templates'] = 'domain-service-template'
    children_field_metas['virtual_DNSs'] = 'domain-virtual-DNS'
    children_field_metas['api_access_lists'] = 'domain-api-access-list'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, domain_limits=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if domain_limits is not None:
            self._domain_limits = domain_limits
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for domain.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for domain.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def get_api_access_lists(self):
        return getattr(self, 'api_access_lists', None)
    #end get_api_access_lists

    def dump(self):
        """Display domain object in compact form."""
        print '------------ domain ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P domain_limits = ', self.get_domain_limits()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS project = ', self.get_projects()
        print 'HAS namespace = ', self.get_namespaces()
        print 'HAS service_template = ', self.get_service_templates()
        print 'HAS virtual_DNS = ', self.get_virtual_DNSs()
        print 'HAS api_access_list = ', self.get_api_access_lists()
    #end dump

#end class Domain

class GlobalVrouterConfig(object):
    """
    Represents global-vrouter-config configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * ecmp_hashing_include_fields
            Type: :class:`.EcmpHashingIncludeFields`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * linklocal_services
            Type: :class:`.LinklocalServicesTypes`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * encapsulation_priorities
            Type: :class:`.EncapsulationPrioritiesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * vxlan_network_identifier_mode
            Type: string, *one-of* [u'configured', u'automatic']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * flow_export_rate
            Type: int

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * flow_aging_timeout_list
            Type: :class:`.FlowAgingTimeoutList`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * forwarding_mode
            Type: string, *one-of* [u'l2_l3', u'l2', u'l3']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'ecmp_hashing_include_fields', u'linklocal_services', u'encapsulation_priorities', u'vxlan_network_identifier_mode', u'flow_export_rate', u'flow_aging_timeout_list', u'forwarding_mode', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'ecmp_hashing_include_fields': {'xsd_type': u'EcmpHashingIncludeFields', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'linklocal_services': {'xsd_type': u'LinklocalServicesTypes', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'encapsulation_priorities': {'xsd_type': u'EncapsulationPrioritiesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'vxlan_network_identifier_mode': {'xsd_type': u'string', 'restrictions': [u'configured', u'automatic'], 'simple_type': u'VxlanNetworkIdentifierModeType', 'is_complex': False},
        'flow_export_rate': {'xsd_type': u'integer', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'flow_aging_timeout_list': {'xsd_type': u'FlowAgingTimeoutList', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'forwarding_mode': {'xsd_type': u'string', 'restrictions': [u'l2_l3', u'l2', u'l3'], 'simple_type': u'ForwardingModeType', 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'global-system-config']

    prop_field_metas = {}
    prop_field_metas['ecmp_hashing_include_fields'] = 'ecmp-hashing-include-fields'
    prop_field_metas['linklocal_services'] = 'linklocal-services'
    prop_field_metas['encapsulation_priorities'] = 'encapsulation-priorities'
    prop_field_metas['vxlan_network_identifier_mode'] = 'vxlan-network-identifier-mode'
    prop_field_metas['flow_export_rate'] = 'flow-export-rate'
    prop_field_metas['flow_aging_timeout_list'] = 'flow-aging-timeout-list'
    prop_field_metas['forwarding_mode'] = 'forwarding-mode'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, ecmp_hashing_include_fields=None, linklocal_services=None, encapsulation_priorities=None, vxlan_network_identifier_mode=None, flow_export_rate=None, flow_aging_timeout_list=None, forwarding_mode=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if ecmp_hashing_include_fields is not None:
            self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
        if linklocal_services is not None:
            self._linklocal_services = linklocal_services
        if encapsulation_priorities is not None:
            self._encapsulation_priorities = encapsulation_priorities
        if vxlan_network_identifier_mode is not None:
            self._vxlan_network_identifier_mode = vxlan_network_identifier_mode
        if flow_export_rate is not None:
            self._flow_export_rate = flow_export_rate
        if flow_aging_timeout_list is not None:
            self._flow_aging_timeout_list = flow_aging_timeout_list
        if forwarding_mode is not None:
            self._forwarding_mode = forwarding_mode
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def ecmp_hashing_include_fields(self):
        """Get ecmp-hashing-include-fields for global-vrouter-config.
        
        :returns: EcmpHashingIncludeFields object
        
        """
        return getattr(self, '_ecmp_hashing_include_fields', None)
    #end ecmp_hashing_include_fields

    @ecmp_hashing_include_fields.setter
    def ecmp_hashing_include_fields(self, ecmp_hashing_include_fields):
        """Set ecmp-hashing-include-fields for global-vrouter-config.
        
        :param ecmp_hashing_include_fields: EcmpHashingIncludeFields object
        
        """
        self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
    #end ecmp_hashing_include_fields

    def set_ecmp_hashing_include_fields(self, value):
        self.ecmp_hashing_include_fields = value
    #end set_ecmp_hashing_include_fields

    def get_ecmp_hashing_include_fields(self):
        return self.ecmp_hashing_include_fields
    #end get_ecmp_hashing_include_fields

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
    def flow_export_rate(self):
        """Get flow-export-rate for global-vrouter-config.
        
        :returns: xsd:integer object
        
        """
        return getattr(self, '_flow_export_rate', None)
    #end flow_export_rate

    @flow_export_rate.setter
    def flow_export_rate(self, flow_export_rate):
        """Set flow-export-rate for global-vrouter-config.
        
        :param flow_export_rate: xsd:integer object
        
        """
        self._flow_export_rate = flow_export_rate
    #end flow_export_rate

    def set_flow_export_rate(self, value):
        self.flow_export_rate = value
    #end set_flow_export_rate

    def get_flow_export_rate(self):
        return self.flow_export_rate
    #end get_flow_export_rate

    @property
    def flow_aging_timeout_list(self):
        """Get flow-aging-timeout-list for global-vrouter-config.
        
        :returns: FlowAgingTimeoutList object
        
        """
        return getattr(self, '_flow_aging_timeout_list', None)
    #end flow_aging_timeout_list

    @flow_aging_timeout_list.setter
    def flow_aging_timeout_list(self, flow_aging_timeout_list):
        """Set flow-aging-timeout-list for global-vrouter-config.
        
        :param flow_aging_timeout_list: FlowAgingTimeoutList object
        
        """
        self._flow_aging_timeout_list = flow_aging_timeout_list
    #end flow_aging_timeout_list

    def set_flow_aging_timeout_list(self, value):
        self.flow_aging_timeout_list = value
    #end set_flow_aging_timeout_list

    def get_flow_aging_timeout_list(self):
        return self.flow_aging_timeout_list
    #end get_flow_aging_timeout_list

    @property
    def forwarding_mode(self):
        """Get forwarding-mode for global-vrouter-config.
        
        :returns: ForwardingModeType object
        
        """
        return getattr(self, '_forwarding_mode', None)
    #end forwarding_mode

    @forwarding_mode.setter
    def forwarding_mode(self, forwarding_mode):
        """Set forwarding-mode for global-vrouter-config.
        
        :param forwarding_mode: ForwardingModeType object
        
        """
        self._forwarding_mode = forwarding_mode
    #end forwarding_mode

    def set_forwarding_mode(self, value):
        self.forwarding_mode = value
    #end set_forwarding_mode

    def get_forwarding_mode(self):
        return self.forwarding_mode
    #end get_forwarding_mode

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
    def perms2(self):
        """Get perms2 for global-vrouter-config.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for global-vrouter-config.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_ecmp_hashing_include_fields'):
            self._serialize_field_to_json(serialized, field_names, 'ecmp_hashing_include_fields')
        if hasattr(self, '_linklocal_services'):
            self._serialize_field_to_json(serialized, field_names, 'linklocal_services')
        if hasattr(self, '_encapsulation_priorities'):
            self._serialize_field_to_json(serialized, field_names, 'encapsulation_priorities')
        if hasattr(self, '_vxlan_network_identifier_mode'):
            self._serialize_field_to_json(serialized, field_names, 'vxlan_network_identifier_mode')
        if hasattr(self, '_flow_export_rate'):
            self._serialize_field_to_json(serialized, field_names, 'flow_export_rate')
        if hasattr(self, '_flow_aging_timeout_list'):
            self._serialize_field_to_json(serialized, field_names, 'flow_aging_timeout_list')
        if hasattr(self, '_forwarding_mode'):
            self._serialize_field_to_json(serialized, field_names, 'forwarding_mode')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display global-vrouter-config object in compact form."""
        print '------------ global-vrouter-config ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P ecmp_hashing_include_fields = ', self.get_ecmp_hashing_include_fields()
        print 'P linklocal_services = ', self.get_linklocal_services()
        print 'P encapsulation_priorities = ', self.get_encapsulation_priorities()
        print 'P vxlan_network_identifier_mode = ', self.get_vxlan_network_identifier_mode()
        print 'P flow_export_rate = ', self.get_flow_export_rate()
        print 'P flow_aging_timeout_list = ', self.get_flow_aging_timeout_list()
        print 'P forwarding_mode = ', self.get_forwarding_mode()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class GlobalVrouterConfig

class InstanceIp(object):
    """
    Represents instance-ip configuration representation.

    Properties:
        * instance_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * instance_ip_family
            Type: string, *one-of* [u'v4', u'v6']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * instance_ip_mode
            Type: string, *one-of* [u'active-active', u'active-standby']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * secondary_ip_tracking_ip
            Type: :class:`.SubnetType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * subnet_uuid
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * instance_ip_secondary
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * service_instance_ip
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualNetwork` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.PhysicalRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.ServiceInstance` objects
    """

    prop_fields = set([u'instance_ip_address', u'instance_ip_family', u'instance_ip_mode', u'secondary_ip_tracking_ip', u'subnet_uuid', u'instance_ip_secondary', u'service_instance_ip', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_network_refs', 'virtual_machine_interface_refs', 'physical_router_refs'])
    backref_fields = set([u'service_instance_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'instance_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'instance_ip_family': {'xsd_type': u'string', 'restrictions': [u'v4', u'v6'], 'simple_type': u'IpAddressFamilyType', 'is_complex': False},
        'instance_ip_mode': {'xsd_type': u'string', 'restrictions': [u'active-active', u'active-standby'], 'simple_type': u'AddressMode', 'is_complex': False},
        'secondary_ip_tracking_ip': {'xsd_type': u'SubnetType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'subnet_uuid': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'instance_ip_secondary': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'service_instance_ip': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_network_refs'] = ('virtual-network', 'None', False)
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)
    ref_field_types['physical_router_refs'] = ('physical-router', 'None', False)

    backref_field_types = {}
    backref_field_types['service_instance_back_refs'] = ('service-instance', 'ServiceInterfaceTag', False)

    children_field_types = {}

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['instance_ip_address'] = 'instance-ip-address'
    prop_field_metas['instance_ip_family'] = 'instance-ip-family'
    prop_field_metas['instance_ip_mode'] = 'instance-ip-mode'
    prop_field_metas['secondary_ip_tracking_ip'] = 'secondary-ip-tracking-ip'
    prop_field_metas['subnet_uuid'] = 'subnet-uuid'
    prop_field_metas['instance_ip_secondary'] = 'instance-ip-secondary'
    prop_field_metas['service_instance_ip'] = 'service-instance-ip'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_network_refs'] = 'instance-ip-virtual-network'
    ref_field_metas['virtual_machine_interface_refs'] = 'instance-ip-virtual-machine-interface'
    ref_field_metas['physical_router_refs'] = 'instance-ip-physical-router'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, instance_ip_address=None, instance_ip_family=None, instance_ip_mode=None, secondary_ip_tracking_ip=None, subnet_uuid=None, instance_ip_secondary=False, service_instance_ip=False, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'instance-ip'
        if not name:
            name = u'default-instance-ip'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if instance_ip_address is not None:
            self._instance_ip_address = instance_ip_address
        if instance_ip_family is not None:
            self._instance_ip_family = instance_ip_family
        if instance_ip_mode is not None:
            self._instance_ip_mode = instance_ip_mode
        if secondary_ip_tracking_ip is not None:
            self._secondary_ip_tracking_ip = secondary_ip_tracking_ip
        if subnet_uuid is not None:
            self._subnet_uuid = subnet_uuid
        if instance_ip_secondary is not None:
            self._instance_ip_secondary = instance_ip_secondary
        if service_instance_ip is not None:
            self._service_instance_ip = service_instance_ip
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def secondary_ip_tracking_ip(self):
        """Get secondary-ip-tracking-ip for instance-ip.
        
        :returns: SubnetType object
        
        """
        return getattr(self, '_secondary_ip_tracking_ip', None)
    #end secondary_ip_tracking_ip

    @secondary_ip_tracking_ip.setter
    def secondary_ip_tracking_ip(self, secondary_ip_tracking_ip):
        """Set secondary-ip-tracking-ip for instance-ip.
        
        :param secondary_ip_tracking_ip: SubnetType object
        
        """
        self._secondary_ip_tracking_ip = secondary_ip_tracking_ip
    #end secondary_ip_tracking_ip

    def set_secondary_ip_tracking_ip(self, value):
        self.secondary_ip_tracking_ip = value
    #end set_secondary_ip_tracking_ip

    def get_secondary_ip_tracking_ip(self):
        return self.secondary_ip_tracking_ip
    #end get_secondary_ip_tracking_ip

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
    def instance_ip_secondary(self):
        """Get instance-ip-secondary for instance-ip.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_instance_ip_secondary', None)
    #end instance_ip_secondary

    @instance_ip_secondary.setter
    def instance_ip_secondary(self, instance_ip_secondary):
        """Set instance-ip-secondary for instance-ip.
        
        :param instance_ip_secondary: xsd:boolean object
        
        """
        self._instance_ip_secondary = instance_ip_secondary
    #end instance_ip_secondary

    def set_instance_ip_secondary(self, value):
        self.instance_ip_secondary = value
    #end set_instance_ip_secondary

    def get_instance_ip_secondary(self):
        return self.instance_ip_secondary
    #end get_instance_ip_secondary

    @property
    def service_instance_ip(self):
        """Get service-instance-ip for instance-ip.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_service_instance_ip', None)
    #end service_instance_ip

    @service_instance_ip.setter
    def service_instance_ip(self, service_instance_ip):
        """Set service-instance-ip for instance-ip.
        
        :param service_instance_ip: xsd:boolean object
        
        """
        self._service_instance_ip = service_instance_ip
    #end service_instance_ip

    def set_service_instance_ip(self, value):
        self.service_instance_ip = value
    #end set_service_instance_ip

    def get_service_instance_ip(self):
        return self.service_instance_ip
    #end get_service_instance_ip

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
    def perms2(self):
        """Get perms2 for instance-ip.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for instance-ip.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_secondary_ip_tracking_ip'):
            self._serialize_field_to_json(serialized, field_names, 'secondary_ip_tracking_ip')
        if hasattr(self, '_subnet_uuid'):
            self._serialize_field_to_json(serialized, field_names, 'subnet_uuid')
        if hasattr(self, '_instance_ip_secondary'):
            self._serialize_field_to_json(serialized, field_names, 'instance_ip_secondary')
        if hasattr(self, '_service_instance_ip'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_ip')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_network_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        if hasattr(self, 'physical_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'physical_router_refs')
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

    def set_physical_router(self, ref_obj):
        """Set physical-router for instance-ip.
        
        :param ref_obj: PhysicalRouter object
        
        """
        self.physical_router_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.physical_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_physical_router

    def add_physical_router(self, ref_obj):
        """Add physical-router to instance-ip.
        
        :param ref_obj: PhysicalRouter object
        
        """
        refs = getattr(self, 'physical_router_refs', [])
        if not refs:
            self.physical_router_refs = []

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

        self.physical_router_refs.append(ref_info)
    #end add_physical_router

    def del_physical_router(self, ref_obj):
        refs = self.get_physical_router_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.physical_router_refs.remove(ref)
                return
    #end del_physical_router

    def set_physical_router_list(self, ref_obj_list):
        """Set physical-router list for instance-ip.
        
        :param ref_obj_list: list of PhysicalRouter object
        
        """
        self.physical_router_refs = ref_obj_list
    #end set_physical_router_list

    def get_physical_router_refs(self):
        """Return physical-router list for instance-ip.
        
        :returns: list of <PhysicalRouter>
        
        """
        return getattr(self, 'physical_router_refs', None)
    #end get_physical_router_refs

    def get_service_instance_back_refs(self):
        """Return list of all service-instances using this instance-ip"""
        return getattr(self, 'service_instance_back_refs', None)
    #end get_service_instance_back_refs

    def dump(self):
        """Display instance-ip object in compact form."""
        print '------------ instance-ip ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P instance_ip_address = ', self.get_instance_ip_address()
        print 'P instance_ip_family = ', self.get_instance_ip_family()
        print 'P instance_ip_mode = ', self.get_instance_ip_mode()
        print 'P secondary_ip_tracking_ip = ', self.get_secondary_ip_tracking_ip()
        print 'P subnet_uuid = ', self.get_subnet_uuid()
        print 'P instance_ip_secondary = ', self.get_instance_ip_secondary()
        print 'P service_instance_ip = ', self.get_service_instance_ip()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF physical_router = ', self.get_physical_router_refs()
        print 'BCK service_instance = ', self.get_service_instance_back_refs()
    #end dump

#end class InstanceIp

class FloatingIpPool(object):
    """
    Represents floating-ip-pool configuration representation.

    Child of:
        :class:`.VirtualNetwork` object OR

    Properties:
        * floating_ip_pool_prefixes
            Type: :class:`.FloatingIpPoolType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.FloatingIp` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:

    Referred by:
        * list of :class:`.Project` objects
    """

    prop_fields = set([u'floating_ip_pool_prefixes', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs'])
    children_fields = set([u'floating_ips'])

    prop_field_types = {
        'floating_ip_pool_prefixes': {'xsd_type': u'FloatingIpPoolType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['project_back_refs'] = ('project', 'None', False)

    children_field_types = {}
    children_field_types['floating_ips'] = ('floating-ip', False)

    parent_types = ['virtual-network']

    prop_field_metas = {}
    prop_field_metas['floating_ip_pool_prefixes'] = 'floating-ip-pool-prefixes'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}
    children_field_metas['floating_ips'] = 'floating-ip-pool-floating-ip'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, floating_ip_pool_prefixes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
            self.fq_name = [u'default-domain', u'default-project', 'default-virtual-network']
            self.fq_name.append(name)


        # property fields
        if floating_ip_pool_prefixes is not None:
            self._floating_ip_pool_prefixes = floating_ip_pool_prefixes
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for floating-ip-pool.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for floating-ip-pool.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_floating_ips(self):
        return getattr(self, 'floating_ips', None)
    #end get_floating_ips

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS floating_ip = ', self.get_floating_ips()
        print 'BCK project = ', self.get_project_back_refs()
    #end dump

#end class FloatingIpPool

class LoadbalancerPool(object):
    """
    Represents loadbalancer-pool configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * loadbalancer_pool_properties
            Type: :class:`.LoadbalancerPoolType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * loadbalancer_pool_provider
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * loadbalancer_pool_custom_attributes
            Type: :class:`.KeyValuePairs`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.LoadbalancerMember` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of :class:`.ServiceInstance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.LoadbalancerListener` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ServiceApplianceSet` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.LoadbalancerHealthmonitor` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualIp` objects
    """

    prop_fields = set([u'loadbalancer_pool_properties', u'loadbalancer_pool_provider', u'loadbalancer_pool_custom_attributes', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_instance_refs', 'virtual_machine_interface_refs', 'loadbalancer_listener_refs', u'service_appliance_set_refs', u'loadbalancer_healthmonitor_refs'])
    backref_fields = set([u'virtual_ip_back_refs'])
    children_fields = set([u'loadbalancer_members'])

    prop_field_types = {
        'loadbalancer_pool_properties': {'xsd_type': u'LoadbalancerPoolType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'loadbalancer_pool_provider': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'loadbalancer_pool_custom_attributes': {'xsd_type': u'KeyValuePairs', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_instance_refs'] = ('service-instance', 'None', False)
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)
    ref_field_types['loadbalancer_listener_refs'] = ('loadbalancer-listener', 'None', False)
    ref_field_types['service_appliance_set_refs'] = ('service-appliance-set', 'None', False)
    ref_field_types['loadbalancer_healthmonitor_refs'] = ('loadbalancer-healthmonitor', 'None', False)

    backref_field_types = {}
    backref_field_types['virtual_ip_back_refs'] = ('virtual-ip', 'None', False)

    children_field_types = {}
    children_field_types['loadbalancer_members'] = ('loadbalancer-member', False)

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['loadbalancer_pool_properties'] = 'loadbalancer-pool-properties'
    prop_field_metas['loadbalancer_pool_provider'] = 'loadbalancer-pool-provider'
    prop_field_metas['loadbalancer_pool_custom_attributes'] = 'loadbalancer-pool-custom-attributes'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_instance_refs'] = 'loadbalancer-pool-service-instance'
    ref_field_metas['virtual_machine_interface_refs'] = 'loadbalancer-pool-virtual-machine-interface'
    ref_field_metas['loadbalancer_listener_refs'] = 'loadbalancer-pool-loadbalancer-listener'
    ref_field_metas['service_appliance_set_refs'] = 'loadbalancer-pool-service-appliance-set'
    ref_field_metas['loadbalancer_healthmonitor_refs'] = 'loadbalancer-pool-loadbalancer-healthmonitor'

    children_field_metas = {}
    children_field_metas['loadbalancer_members'] = 'loadbalancer-pool-loadbalancer-member'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, loadbalancer_pool_properties=None, loadbalancer_pool_provider=None, loadbalancer_pool_custom_attributes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if loadbalancer_pool_properties is not None:
            self._loadbalancer_pool_properties = loadbalancer_pool_properties
        if loadbalancer_pool_provider is not None:
            self._loadbalancer_pool_provider = loadbalancer_pool_provider
        if loadbalancer_pool_custom_attributes is not None:
            self._loadbalancer_pool_custom_attributes = loadbalancer_pool_custom_attributes
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def loadbalancer_pool_custom_attributes(self):
        """Get loadbalancer-pool-custom-attributes for loadbalancer-pool.
        
        :returns: KeyValuePairs object
        
        """
        return getattr(self, '_loadbalancer_pool_custom_attributes', None)
    #end loadbalancer_pool_custom_attributes

    @loadbalancer_pool_custom_attributes.setter
    def loadbalancer_pool_custom_attributes(self, loadbalancer_pool_custom_attributes):
        """Set loadbalancer-pool-custom-attributes for loadbalancer-pool.
        
        :param loadbalancer_pool_custom_attributes: KeyValuePairs object
        
        """
        self._loadbalancer_pool_custom_attributes = loadbalancer_pool_custom_attributes
    #end loadbalancer_pool_custom_attributes

    def set_loadbalancer_pool_custom_attributes(self, value):
        self.loadbalancer_pool_custom_attributes = value
    #end set_loadbalancer_pool_custom_attributes

    def get_loadbalancer_pool_custom_attributes(self):
        return self.loadbalancer_pool_custom_attributes
    #end get_loadbalancer_pool_custom_attributes

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
    def perms2(self):
        """Get perms2 for loadbalancer-pool.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-pool.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_loadbalancer_pool_custom_attributes'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_pool_custom_attributes')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        if hasattr(self, 'loadbalancer_listener_refs'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_listener_refs')
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

    def set_loadbalancer_listener(self, ref_obj):
        """Set loadbalancer-listener for loadbalancer-pool.
        
        :param ref_obj: LoadbalancerListener object
        
        """
        self.loadbalancer_listener_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.loadbalancer_listener_refs[0]['uuid'] = ref_obj.uuid

    #end set_loadbalancer_listener

    def add_loadbalancer_listener(self, ref_obj):
        """Add loadbalancer-listener to loadbalancer-pool.
        
        :param ref_obj: LoadbalancerListener object
        
        """
        refs = getattr(self, 'loadbalancer_listener_refs', [])
        if not refs:
            self.loadbalancer_listener_refs = []

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

        self.loadbalancer_listener_refs.append(ref_info)
    #end add_loadbalancer_listener

    def del_loadbalancer_listener(self, ref_obj):
        refs = self.get_loadbalancer_listener_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.loadbalancer_listener_refs.remove(ref)
                return
    #end del_loadbalancer_listener

    def set_loadbalancer_listener_list(self, ref_obj_list):
        """Set loadbalancer-listener list for loadbalancer-pool.
        
        :param ref_obj_list: list of LoadbalancerListener object
        
        """
        self.loadbalancer_listener_refs = ref_obj_list
    #end set_loadbalancer_listener_list

    def get_loadbalancer_listener_refs(self):
        """Return loadbalancer-listener list for loadbalancer-pool.
        
        :returns: list of <LoadbalancerListener>
        
        """
        return getattr(self, 'loadbalancer_listener_refs', None)
    #end get_loadbalancer_listener_refs

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
        print 'P loadbalancer_pool_custom_attributes = ', self.get_loadbalancer_pool_custom_attributes()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF loadbalancer_listener = ', self.get_loadbalancer_listener_refs()
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
        * virtual_DNS_record_data
            Type: :class:`.VirtualDnsRecordType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'virtual_DNS_record_data', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'virtual_DNS_record_data': {'xsd_type': u'VirtualDnsRecordType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'virtual-DNS']

    prop_field_metas = {}
    prop_field_metas['virtual_DNS_record_data'] = 'virtual-DNS-record-data'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, virtual_DNS_record_data=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if virtual_DNS_record_data is not None:
            self._virtual_DNS_record_data = virtual_DNS_record_data
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for virtual-DNS-record.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-DNS-record.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display virtual-DNS-record object in compact form."""
        print '------------ virtual-DNS-record ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_DNS_record_data = ', self.get_virtual_DNS_record_data()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class VirtualDnsRecord

class RouteTarget(object):
    """
    Represents route-target configuration representation.

    Properties:
        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
        * list of :class:`.LogicalRouter` objects
        * list of :class:`.RoutingInstance` objects
    """

    prop_fields = set([u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set(['logical_router_back_refs', 'routing_instance_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['logical_router_back_refs'] = ('logical-router', 'None', False)
    backref_field_types['routing_instance_back_refs'] = ('routing-instance', 'InstanceTargetType', False)

    children_field_types = {}

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'route-target'
        if not name:
            name = u'default-route-target'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for route-target.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for route-target.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'BCK logical_router = ', self.get_logical_router_back_refs()
        print 'BCK routing_instance = ', self.get_routing_instance_back_refs()
    #end dump

#end class RouteTarget

class DiscoveryServiceAssignment(object):
    """
    Represents discovery-service-assignment configuration representation.

    Properties:
        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.DsaRule` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:

    Referred by:
    """

    prop_fields = set([u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set(['dsa_rules'])

    prop_field_types = {
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}
    children_field_types['dsa_rules'] = ('dsa-rule', False)

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}
    children_field_metas['dsa_rules'] = 'discovery-service-assignment-dsa-rule'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'discovery-service-assignment'
        if not name:
            name = u'default-discovery-service-assignment'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (discovery-service-assignment)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of discovery-service-assignment in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of discovery-service-assignment as colon delimited string."""
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
        """Get id-perms for discovery-service-assignment.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for discovery-service-assignment.
        
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
    def perms2(self):
        """Get perms2 for discovery-service-assignment.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for discovery-service-assignment.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for discovery-service-assignment.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for discovery-service-assignment.
        
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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_dsa_rules(self):
        return getattr(self, 'dsa_rules', None)
    #end get_dsa_rules

    def dump(self):
        """Display discovery-service-assignment object in compact form."""
        print '------------ discovery-service-assignment ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS dsa_rule = ', self.get_dsa_rules()
    #end dump

#end class DiscoveryServiceAssignment

class FloatingIp(object):
    """
    Represents floating-ip configuration representation.

    Child of:
        :class:`.FloatingIpPool` object OR

    Properties:
        * floating_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * floating_ip_is_virtual_ip
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * floating_ip_fixed_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * floating_ip_address_family
            Type: string, *one-of* [u'v4', u'v6']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.Project` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.CustomerAttachment` objects
    """

    prop_fields = set([u'floating_ip_address', u'floating_ip_is_virtual_ip', u'floating_ip_fixed_ip_address', u'floating_ip_address_family', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'project_refs', 'virtual_machine_interface_refs'])
    backref_fields = set(['customer_attachment_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'floating_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'floating_ip_is_virtual_ip': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'floating_ip_fixed_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'floating_ip_address_family': {'xsd_type': u'string', 'restrictions': [u'v4', u'v6'], 'simple_type': u'IpAddressFamilyType', 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['project_refs'] = ('project', 'None', False)
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)

    backref_field_types = {}
    backref_field_types['customer_attachment_back_refs'] = ('customer-attachment', 'None', False)

    children_field_types = {}

    parent_types = [u'floating-ip-pool']

    prop_field_metas = {}
    prop_field_metas['floating_ip_address'] = 'floating-ip-address'
    prop_field_metas['floating_ip_is_virtual_ip'] = 'floating-ip-is-virtual-ip'
    prop_field_metas['floating_ip_fixed_ip_address'] = 'floating-ip-fixed-ip-address'
    prop_field_metas['floating_ip_address_family'] = 'floating-ip-address-family'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['project_refs'] = 'floating-ip-project'
    ref_field_metas['virtual_machine_interface_refs'] = 'floating-ip-virtual-machine-interface'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, floating_ip_address=None, floating_ip_is_virtual_ip=None, floating_ip_fixed_ip_address=None, floating_ip_address_family=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
            self.fq_name = [u'default-domain', u'default-project', 'default-virtual-network', u'default-floating-ip-pool']
            self.fq_name.append(name)


        # property fields
        if floating_ip_address is not None:
            self._floating_ip_address = floating_ip_address
        if floating_ip_is_virtual_ip is not None:
            self._floating_ip_is_virtual_ip = floating_ip_is_virtual_ip
        if floating_ip_fixed_ip_address is not None:
            self._floating_ip_fixed_ip_address = floating_ip_fixed_ip_address
        if floating_ip_address_family is not None:
            self._floating_ip_address_family = floating_ip_address_family
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for floating-ip.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for floating-ip.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF project = ', self.get_project_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'BCK customer_attachment = ', self.get_customer_attachment_back_refs()
    #end dump

#end class FloatingIp

class NetworkPolicy(object):
    """
    Represents network-policy configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * network_policy_entries
            Type: :class:`.PolicyEntriesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
        * list of :class:`.VirtualNetwork` objects
    """

    prop_fields = set([u'network_policy_entries', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set(['virtual_network_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'network_policy_entries': {'xsd_type': u'PolicyEntriesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['virtual_network_back_refs'] = ('virtual-network', 'VirtualNetworkPolicyType', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['network_policy_entries'] = 'network-policy-entries'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, network_policy_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if network_policy_entries is not None:
            self._network_policy_entries = network_policy_entries
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for network-policy.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for network-policy.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'BCK virtual_network = ', self.get_virtual_network_back_refs()
    #end dump

#end class NetworkPolicy

class PhysicalRouter(object):
    """
    Represents physical-router configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * physical_router_management_ip
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * physical_router_dataplane_ip
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * physical_router_vendor_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * physical_router_product_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * physical_router_vnc_managed
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * physical_router_user_credentials
            Type: :class:`.UserCredentials`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * physical_router_snmp_credentials
            Type: :class:`.SNMPCredentials`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * physical_router_junos_service_ports
            Type: :class:`.JunosServicePorts`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.PhysicalInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.LogicalInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of :class:`.VirtualRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.BgpRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualNetwork` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.InstanceIp` objects
    """

    prop_fields = set([u'physical_router_management_ip', u'physical_router_dataplane_ip', u'physical_router_vendor_name', u'physical_router_product_name', u'physical_router_vnc_managed', u'physical_router_user_credentials', u'physical_router_snmp_credentials', u'physical_router_junos_service_ports', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_router_refs', 'bgp_router_refs', 'virtual_network_refs'])
    backref_fields = set([u'instance_ip_back_refs'])
    children_fields = set([u'physical_interfaces', u'logical_interfaces'])

    prop_field_types = {
        'physical_router_management_ip': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddress', 'is_complex': False},
        'physical_router_dataplane_ip': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddress', 'is_complex': False},
        'physical_router_vendor_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'physical_router_product_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'physical_router_vnc_managed': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'physical_router_user_credentials': {'xsd_type': u'UserCredentials', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'physical_router_snmp_credentials': {'xsd_type': u'SNMPCredentials', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'physical_router_junos_service_ports': {'xsd_type': u'JunosServicePorts', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_router_refs'] = ('virtual-router', 'None', False)
    ref_field_types['bgp_router_refs'] = ('bgp-router', 'None', False)
    ref_field_types['virtual_network_refs'] = ('virtual-network', 'None', False)

    backref_field_types = {}
    backref_field_types['instance_ip_back_refs'] = ('instance-ip', 'None', False)

    children_field_types = {}
    children_field_types['physical_interfaces'] = ('physical-interface', False)
    children_field_types['logical_interfaces'] = ('logical-interface', False)

    parent_types = [u'global-system-config']

    prop_field_metas = {}
    prop_field_metas['physical_router_management_ip'] = 'physical-router-management-ip'
    prop_field_metas['physical_router_dataplane_ip'] = 'physical-router-dataplane-ip'
    prop_field_metas['physical_router_vendor_name'] = 'physical-router-vendor-name'
    prop_field_metas['physical_router_product_name'] = 'physical-router-product-name'
    prop_field_metas['physical_router_vnc_managed'] = 'physical-router-vnc-managed'
    prop_field_metas['physical_router_user_credentials'] = 'physical-router-user-credentials'
    prop_field_metas['physical_router_snmp_credentials'] = 'physical-router-snmp-credentials'
    prop_field_metas['physical_router_junos_service_ports'] = 'physical-router-junos-service-ports'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_router_refs'] = 'physical-router-virtual-router'
    ref_field_metas['bgp_router_refs'] = 'physical-router-bgp-router'
    ref_field_metas['virtual_network_refs'] = 'physical-router-virtual-network'

    children_field_metas = {}
    children_field_metas['physical_interfaces'] = 'physical-router-physical-interface'
    children_field_metas['logical_interfaces'] = 'physical-router-logical-interface'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, physical_router_management_ip=None, physical_router_dataplane_ip=None, physical_router_vendor_name=None, physical_router_product_name=None, physical_router_vnc_managed=None, physical_router_user_credentials=None, physical_router_snmp_credentials=None, physical_router_junos_service_ports=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if physical_router_management_ip is not None:
            self._physical_router_management_ip = physical_router_management_ip
        if physical_router_dataplane_ip is not None:
            self._physical_router_dataplane_ip = physical_router_dataplane_ip
        if physical_router_vendor_name is not None:
            self._physical_router_vendor_name = physical_router_vendor_name
        if physical_router_product_name is not None:
            self._physical_router_product_name = physical_router_product_name
        if physical_router_vnc_managed is not None:
            self._physical_router_vnc_managed = physical_router_vnc_managed
        if physical_router_user_credentials is not None:
            self._physical_router_user_credentials = physical_router_user_credentials
        if physical_router_snmp_credentials is not None:
            self._physical_router_snmp_credentials = physical_router_snmp_credentials
        if physical_router_junos_service_ports is not None:
            self._physical_router_junos_service_ports = physical_router_junos_service_ports
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for physical-router.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for physical-router.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def get_instance_ip_back_refs(self):
        """Return list of all instance-ips using this physical-router"""
        return getattr(self, 'instance_ip_back_refs', None)
    #end get_instance_ip_back_refs

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_router = ', self.get_virtual_router_refs()
        print 'REF bgp_router = ', self.get_bgp_router_refs()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'HAS physical_interface = ', self.get_physical_interfaces()
        print 'HAS logical_interface = ', self.get_logical_interfaces()
        print 'BCK instance_ip = ', self.get_instance_ip_back_refs()
    #end dump

#end class PhysicalRouter

class BgpRouter(object):
    """
    Represents bgp-router configuration representation.

    Child of:
        :class:`.RoutingInstance` object OR

    Properties:
        * bgp_router_parameters
            Type: :class:`.BgpRouterParams`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of (:class:`.BgpRouter` object, :class:`.BgpPeeringAttributes` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.GlobalSystemConfig` objects
        * list of :class:`.PhysicalRouter` objects
        * list of :class:`.BgpAsAService` objects
        * list of :class:`.BgpRouter` objects
    """

    prop_fields = set([u'bgp_router_parameters', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['bgp_router_refs'])
    backref_fields = set([u'global_system_config_back_refs', 'physical_router_back_refs', 'bgp_as_a_service_back_refs', 'bgp_router_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'bgp_router_parameters': {'xsd_type': u'BgpRouterParams', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['bgp_router_refs'] = ('bgp-router', 'BgpPeeringAttributes', False)

    backref_field_types = {}
    backref_field_types['global_system_config_back_refs'] = ('global-system-config', 'None', False)
    backref_field_types['physical_router_back_refs'] = ('physical-router', 'None', False)
    backref_field_types['bgp_as_a_service_back_refs'] = ('bgp-as-a-service', 'None', False)
    backref_field_types['bgp_router_back_refs'] = ('bgp-router', 'BgpPeeringAttributes', False)

    children_field_types = {}

    parent_types = ['routing-instance']

    prop_field_metas = {}
    prop_field_metas['bgp_router_parameters'] = 'bgp-router-parameters'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['bgp_router_refs'] = 'bgp-peering'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, bgp_router_parameters=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
            self.fq_name = [u'default-domain', u'default-project', 'default-virtual-network', 'default-routing-instance']
            self.fq_name.append(name)


        # property fields
        if bgp_router_parameters is not None:
            self._bgp_router_parameters = bgp_router_parameters
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for bgp-router.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for bgp-router.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def get_bgp_as_a_service_back_refs(self):
        """Return list of all bgp-as-a-services using this bgp-router"""
        return getattr(self, 'bgp_as_a_service_back_refs', None)
    #end get_bgp_as_a_service_back_refs

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF bgp_router = ', self.get_bgp_router_refs()
        print 'BCK global_system_config = ', self.get_global_system_config_back_refs()
        print 'BCK physical_router = ', self.get_physical_router_back_refs()
        print 'BCK bgp_as_a_service = ', self.get_bgp_as_a_service_back_refs()
        print 'BCK bgp_router = ', self.get_bgp_router_back_refs()
    #end dump

#end class BgpRouter

class ApiAccessList(object):
    """
    Represents api-access-list configuration representation.

    Child of:
        :class:`.Domain` object OR
        :class:`.Project` object OR

    Properties:
        * api_access_list_entries
            Type: :class:`.RbacRuleEntriesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'api_access_list_entries', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'api_access_list_entries': {'xsd_type': u'RbacRuleEntriesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'domain', u'project']

    prop_field_metas = {}
    prop_field_metas['api_access_list_entries'] = 'api-access-list-entries'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, api_access_list_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'api-access-list'
        if not name:
            name = u'default-api-access-list'
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
                raise AmbiguousParentError("[[u'default-domain'], [u'default-domain', u'default-project']]")

        # property fields
        if api_access_list_entries is not None:
            self._api_access_list_entries = api_access_list_entries
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (api-access-list)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of api-access-list in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of api-access-list as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of api-access-list's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of api-access-list's parent as colon delimted string."""
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
    def api_access_list_entries(self):
        """Get api-access-list-entries for api-access-list.
        
        :returns: RbacRuleEntriesType object
        
        """
        return getattr(self, '_api_access_list_entries', None)
    #end api_access_list_entries

    @api_access_list_entries.setter
    def api_access_list_entries(self, api_access_list_entries):
        """Set api-access-list-entries for api-access-list.
        
        :param api_access_list_entries: RbacRuleEntriesType object
        
        """
        self._api_access_list_entries = api_access_list_entries
    #end api_access_list_entries

    def set_api_access_list_entries(self, value):
        self.api_access_list_entries = value
    #end set_api_access_list_entries

    def get_api_access_list_entries(self):
        return self.api_access_list_entries
    #end get_api_access_list_entries

    @property
    def id_perms(self):
        """Get id-perms for api-access-list.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for api-access-list.
        
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
    def perms2(self):
        """Get perms2 for api-access-list.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for api-access-list.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for api-access-list.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for api-access-list.
        
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
        if hasattr(self, '_api_access_list_entries'):
            self._serialize_field_to_json(serialized, field_names, 'api_access_list_entries')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display api-access-list object in compact form."""
        print '------------ api-access-list ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P api_access_list_entries = ', self.get_api_access_list_entries()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class ApiAccessList

class VirtualRouter(object):
    """
    Represents virtual-router configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * virtual_router_type
            Type: string, *one-of* [u'embedded', u'tor-agent', u'tor-service-node']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_router_dpdk_enabled
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_router_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualMachine` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.PhysicalRouter` objects
        * list of :class:`.ProviderAttachment` objects
    """

    prop_fields = set([u'virtual_router_type', u'virtual_router_dpdk_enabled', u'virtual_router_ip_address', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'virtual_machine_refs'])
    backref_fields = set(['physical_router_back_refs', 'provider_attachment_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'virtual_router_type': {'xsd_type': u'string', 'restrictions': [u'embedded', u'tor-agent', u'tor-service-node'], 'simple_type': u'VirtualRouterType', 'is_complex': False},
        'virtual_router_dpdk_enabled': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'virtual_router_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_machine_refs'] = ('virtual-machine', 'None', False)

    backref_field_types = {}
    backref_field_types['physical_router_back_refs'] = ('physical-router', 'None', False)
    backref_field_types['provider_attachment_back_refs'] = ('provider-attachment', 'None', False)

    children_field_types = {}

    parent_types = [u'global-system-config']

    prop_field_metas = {}
    prop_field_metas['virtual_router_type'] = 'virtual-router-type'
    prop_field_metas['virtual_router_dpdk_enabled'] = 'virtual-router-dpdk-enabled'
    prop_field_metas['virtual_router_ip_address'] = 'virtual-router-ip-address'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_machine_refs'] = 'virtual-router-virtual-machine'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, virtual_router_type=None, virtual_router_dpdk_enabled=None, virtual_router_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if virtual_router_type is not None:
            self._virtual_router_type = virtual_router_type
        if virtual_router_dpdk_enabled is not None:
            self._virtual_router_dpdk_enabled = virtual_router_dpdk_enabled
        if virtual_router_ip_address is not None:
            self._virtual_router_ip_address = virtual_router_ip_address
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def virtual_router_dpdk_enabled(self):
        """Get virtual-router-dpdk-enabled for virtual-router.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_virtual_router_dpdk_enabled', None)
    #end virtual_router_dpdk_enabled

    @virtual_router_dpdk_enabled.setter
    def virtual_router_dpdk_enabled(self, virtual_router_dpdk_enabled):
        """Set virtual-router-dpdk-enabled for virtual-router.
        
        :param virtual_router_dpdk_enabled: xsd:boolean object
        
        """
        self._virtual_router_dpdk_enabled = virtual_router_dpdk_enabled
    #end virtual_router_dpdk_enabled

    def set_virtual_router_dpdk_enabled(self, value):
        self.virtual_router_dpdk_enabled = value
    #end set_virtual_router_dpdk_enabled

    def get_virtual_router_dpdk_enabled(self):
        return self.virtual_router_dpdk_enabled
    #end get_virtual_router_dpdk_enabled

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
    def perms2(self):
        """Get perms2 for virtual-router.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-router.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_virtual_router_dpdk_enabled'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_router_dpdk_enabled')
        if hasattr(self, '_virtual_router_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_router_ip_address')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_machine_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_refs')
        return serialized
    #end serialize_to_json

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
        print 'P virtual_router_dpdk_enabled = ', self.get_virtual_router_dpdk_enabled()
        print 'P virtual_router_ip_address = ', self.get_virtual_router_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine = ', self.get_virtual_machine_refs()
        print 'BCK physical_router = ', self.get_physical_router_back_refs()
        print 'BCK provider_attachment = ', self.get_provider_attachment_back_refs()
    #end dump

#end class VirtualRouter

class ConfigRoot(object):
    """
    Represents config-root configuration representation.

    Properties:
        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.GlobalSystemConfig` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.Domain` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:

    Referred by:
    """

    prop_fields = set([u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([u'global_system_configs', u'domains'])

    prop_field_types = {
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}
    children_field_types['global_system_configs'] = ('global-system-config', False)
    children_field_types['domains'] = ('domain', False)

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}
    children_field_metas['global_system_configs'] = 'config-root-global-system-config'
    children_field_metas['domains'] = 'config-root-domain'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'config-root'
        if not name:
            name = u'default-config-root'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for config-root.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for config-root.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS global_system_config = ', self.get_global_system_configs()
        print 'HAS domain = ', self.get_domains()
    #end dump

#end class ConfigRoot

class Subnet(object):
    """
    Represents subnet configuration representation.

    Properties:
        * subnet_ip_prefix
            Type: :class:`.SubnetType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'subnet_ip_prefix', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'subnet_ip_prefix': {'xsd_type': u'SubnetType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['subnet_ip_prefix'] = 'subnet-ip-prefix'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_machine_interface_refs'] = 'subnet-virtual-machine-interface'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, subnet_ip_prefix=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'subnet'
        if not name:
            name = u'default-subnet'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if subnet_ip_prefix is not None:
            self._subnet_ip_prefix = subnet_ip_prefix
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for subnet.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for subnet.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
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
        * autonomous_system
            Type: int, *one-of* [u'1', u'65534']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * config_version
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * plugin_tuning
            Type: :class:`.PluginProperties`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * ibgp_auto_mesh
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * ip_fabric_subnets
            Type: :class:`.SubnetListType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.GlobalVrouterConfig` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.PhysicalRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ConfigNode` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.AnalyticsNode` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.DatabaseNode` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ServiceApplianceSet` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of :class:`.BgpRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'autonomous_system', u'config_version', u'plugin_tuning', u'ibgp_auto_mesh', u'ip_fabric_subnets', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['bgp_router_refs'])
    backref_fields = set([])
    children_fields = set([u'global_vrouter_configs', 'physical_routers', 'virtual_routers', u'config_nodes', u'analytics_nodes', u'database_nodes', u'service_appliance_sets'])

    prop_field_types = {
        'autonomous_system': {'xsd_type': u'integer', 'restrictions': [u'1', u'65534'], 'simple_type': u'AutonomousSystemType', 'is_complex': False},
        'config_version': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'plugin_tuning': {'xsd_type': u'PluginProperties', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'ibgp_auto_mesh': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'ip_fabric_subnets': {'xsd_type': u'SubnetListType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['bgp_router_refs'] = ('bgp-router', 'None', False)

    backref_field_types = {}

    children_field_types = {}
    children_field_types['global_vrouter_configs'] = ('global-vrouter-config', False)
    children_field_types['physical_routers'] = ('physical-router', False)
    children_field_types['virtual_routers'] = ('virtual-router', False)
    children_field_types['config_nodes'] = ('config-node', False)
    children_field_types['analytics_nodes'] = ('analytics-node', False)
    children_field_types['database_nodes'] = ('database-node', False)
    children_field_types['service_appliance_sets'] = ('service-appliance-set', False)

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['autonomous_system'] = 'autonomous-system'
    prop_field_metas['config_version'] = 'config-version'
    prop_field_metas['plugin_tuning'] = 'plugin-tuning'
    prop_field_metas['ibgp_auto_mesh'] = 'ibgp-auto-mesh'
    prop_field_metas['ip_fabric_subnets'] = 'ip-fabric-subnets'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['bgp_router_refs'] = 'global-system-config-bgp-router'

    children_field_metas = {}
    children_field_metas['global_vrouter_configs'] = 'global-system-config-global-vrouter-config'
    children_field_metas['physical_routers'] = 'global-system-config-physical-router'
    children_field_metas['virtual_routers'] = 'global-system-config-virtual-router'
    children_field_metas['config_nodes'] = 'global-system-config-config-node'
    children_field_metas['analytics_nodes'] = 'global-system-config-analytics-node'
    children_field_metas['database_nodes'] = 'global-system-config-database-node'
    children_field_metas['service_appliance_sets'] = 'global-system-config-service-appliance-set'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, autonomous_system=None, config_version=None, plugin_tuning=None, ibgp_auto_mesh=None, ip_fabric_subnets=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if autonomous_system is not None:
            self._autonomous_system = autonomous_system
        if config_version is not None:
            self._config_version = config_version
        if plugin_tuning is not None:
            self._plugin_tuning = plugin_tuning
        if ibgp_auto_mesh is not None:
            self._ibgp_auto_mesh = ibgp_auto_mesh
        if ip_fabric_subnets is not None:
            self._ip_fabric_subnets = ip_fabric_subnets
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for global-system-config.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for global-system-config.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
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
        * service_appliance_user_credentials
            Type: :class:`.UserCredentials`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * service_appliance_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * service_appliance_properties
            Type: :class:`.KeyValuePairs`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of (:class:`.PhysicalInterface` object, :class:`.ServiceApplianceInterfaceType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'service_appliance_user_credentials', u'service_appliance_ip_address', u'service_appliance_properties', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'physical_interface_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'service_appliance_user_credentials': {'xsd_type': u'UserCredentials', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'service_appliance_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'service_appliance_properties': {'xsd_type': u'KeyValuePairs', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['physical_interface_refs'] = ('physical-interface', 'ServiceApplianceInterfaceType', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'service-appliance-set']

    prop_field_metas = {}
    prop_field_metas['service_appliance_user_credentials'] = 'service-appliance-user-credentials'
    prop_field_metas['service_appliance_ip_address'] = 'service-appliance-ip-address'
    prop_field_metas['service_appliance_properties'] = 'service-appliance-properties'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['physical_interface_refs'] = 'service-appliance-interface'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, service_appliance_user_credentials=None, service_appliance_ip_address=None, service_appliance_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if service_appliance_user_credentials is not None:
            self._service_appliance_user_credentials = service_appliance_user_credentials
        if service_appliance_ip_address is not None:
            self._service_appliance_ip_address = service_appliance_ip_address
        if service_appliance_properties is not None:
            self._service_appliance_properties = service_appliance_properties
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for service-appliance.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-appliance.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'physical_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'physical_interface_refs')
        return serialized
    #end serialize_to_json

    def set_physical_interface(self, ref_obj, ref_data):
        """Set physical-interface for service-appliance.
        
        :param ref_obj: PhysicalInterface object
        :param ref_data: ServiceApplianceInterfaceType object
        
        """
        self.physical_interface_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.physical_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_physical_interface

    def add_physical_interface(self, ref_obj, ref_data):
        """Add physical-interface to service-appliance.
        
        :param ref_obj: PhysicalInterface object
        :param ref_data: ServiceApplianceInterfaceType object
        
        """
        refs = getattr(self, 'physical_interface_refs', [])
        if not refs:
            self.physical_interface_refs = []

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

        self.physical_interface_refs.append(ref_info)
    #end add_physical_interface

    def del_physical_interface(self, ref_obj):
        refs = self.get_physical_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.physical_interface_refs.remove(ref)
                return
    #end del_physical_interface

    def set_physical_interface_list(self, ref_obj_list, ref_data_list):
        """Set physical-interface list for service-appliance.
        
        :param ref_obj_list: list of PhysicalInterface object
        :param ref_data_list: list of ServiceApplianceInterfaceType object
        
        """
        self.physical_interface_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_physical_interface_list

    def get_physical_interface_refs(self):
        """Return physical-interface list for service-appliance.
        
        :returns: list of tuple <PhysicalInterface, ServiceApplianceInterfaceType>
        
        """
        return getattr(self, 'physical_interface_refs', None)
    #end get_physical_interface_refs

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF physical_interface = ', self.get_physical_interface_refs()
    #end dump

#end class ServiceAppliance

class RoutingPolicy(object):
    """
    Represents routing-policy configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * routing_policy_entries
            Type: :class:`.PolicyStatementType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of (:class:`.ServiceInstance` object, :class:`.RoutingPolicyServiceInstanceType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of (:class:`.RoutingInstance` object, :class:`.RoutingPolicyType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'routing_policy_entries', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_instance_refs', 'routing_instance_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'routing_policy_entries': {'xsd_type': u'PolicyStatementType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_instance_refs'] = ('service-instance', 'RoutingPolicyServiceInstanceType', False)
    ref_field_types['routing_instance_refs'] = ('routing-instance', 'RoutingPolicyType', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['routing_policy_entries'] = 'routing-policy-entries'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_instance_refs'] = 'routing-policy-service-instance'
    ref_field_metas['routing_instance_refs'] = 'routing-policy-routing-instance'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, routing_policy_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'routing-policy'
        if not name:
            name = u'default-routing-policy'
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
        if routing_policy_entries is not None:
            self._routing_policy_entries = routing_policy_entries
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (routing-policy)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of routing-policy in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of routing-policy as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of routing-policy's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of routing-policy's parent as colon delimted string."""
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
    def routing_policy_entries(self):
        """Get routing-policy-entries for routing-policy.
        
        :returns: PolicyStatementType object
        
        """
        return getattr(self, '_routing_policy_entries', None)
    #end routing_policy_entries

    @routing_policy_entries.setter
    def routing_policy_entries(self, routing_policy_entries):
        """Set routing-policy-entries for routing-policy.
        
        :param routing_policy_entries: PolicyStatementType object
        
        """
        self._routing_policy_entries = routing_policy_entries
    #end routing_policy_entries

    def set_routing_policy_entries(self, value):
        self.routing_policy_entries = value
    #end set_routing_policy_entries

    def get_routing_policy_entries(self):
        return self.routing_policy_entries
    #end get_routing_policy_entries

    @property
    def id_perms(self):
        """Get id-perms for routing-policy.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for routing-policy.
        
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
    def perms2(self):
        """Get perms2 for routing-policy.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for routing-policy.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for routing-policy.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for routing-policy.
        
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
        if hasattr(self, '_routing_policy_entries'):
            self._serialize_field_to_json(serialized, field_names, 'routing_policy_entries')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        if hasattr(self, 'routing_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'routing_instance_refs')
        return serialized
    #end serialize_to_json

    def set_service_instance(self, ref_obj, ref_data):
        """Set service-instance for routing-policy.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: RoutingPolicyServiceInstanceType object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj, ref_data):
        """Add service-instance to routing-policy.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: RoutingPolicyServiceInstanceType object
        
        """
        refs = getattr(self, 'service_instance_refs', [])
        if not refs:
            self.service_instance_refs = []

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

    def set_service_instance_list(self, ref_obj_list, ref_data_list):
        """Set service-instance list for routing-policy.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of RoutingPolicyServiceInstanceType object
        
        """
        self.service_instance_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for routing-policy.
        
        :returns: list of tuple <ServiceInstance, RoutingPolicyServiceInstanceType>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

    def set_routing_instance(self, ref_obj, ref_data):
        """Set routing-instance for routing-policy.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: RoutingPolicyType object
        
        """
        self.routing_instance_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.routing_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_routing_instance

    def add_routing_instance(self, ref_obj, ref_data):
        """Add routing-instance to routing-policy.
        
        :param ref_obj: RoutingInstance object
        :param ref_data: RoutingPolicyType object
        
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
        """Set routing-instance list for routing-policy.
        
        :param ref_obj_list: list of RoutingInstance object
        :param ref_data_list: list of RoutingPolicyType object
        
        """
        self.routing_instance_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_routing_instance_list

    def get_routing_instance_refs(self):
        """Return routing-instance list for routing-policy.
        
        :returns: list of tuple <RoutingInstance, RoutingPolicyType>
        
        """
        return getattr(self, 'routing_instance_refs', None)
    #end get_routing_instance_refs

    def dump(self):
        """Display routing-policy object in compact form."""
        print '------------ routing-policy ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P routing_policy_entries = ', self.get_routing_policy_entries()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'REF routing_instance = ', self.get_routing_instance_refs()
    #end dump

#end class RoutingPolicy

class Namespace(object):
    """
    Represents namespace configuration representation.

    Child of:
        :class:`.Domain` object OR

    Properties:
        * namespace_cidr
            Type: :class:`.SubnetType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
        * list of :class:`.Project` objects
    """

    prop_fields = set([u'namespace_cidr', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'project_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'namespace_cidr': {'xsd_type': u'SubnetType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['project_back_refs'] = ('project', 'SubnetType', False)

    children_field_types = {}

    parent_types = [u'domain']

    prop_field_metas = {}
    prop_field_metas['namespace_cidr'] = 'namespace-cidr'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, namespace_cidr=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if namespace_cidr is not None:
            self._namespace_cidr = namespace_cidr
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for namespace.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for namespace.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

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
        print 'P perms2 = ', self.get_perms2()
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
        * logical_interface_vlan_tag
            Type: int

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * logical_interface_type
            Type: string, *one-of* [u'l2', u'l3']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'logical_interface_vlan_tag', u'logical_interface_type', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'logical_interface_vlan_tag': {'xsd_type': u'integer', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'logical_interface_type': {'xsd_type': u'string', 'restrictions': [u'l2', u'l3'], 'simple_type': u'LogicalInterfaceType', 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = ['physical-router', u'physical-interface']

    prop_field_metas = {}
    prop_field_metas['logical_interface_vlan_tag'] = 'logical-interface-vlan-tag'
    prop_field_metas['logical_interface_type'] = 'logical-interface-type'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_machine_interface_refs'] = 'logical-interface-virtual-machine-interface'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, logical_interface_vlan_tag=None, logical_interface_type=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
                raise AmbiguousParentError("[[u'default-global-system-config', 'default-physical-router'], [u'default-global-system-config', 'default-physical-router', u'default-physical-interface']]")

        # property fields
        if logical_interface_vlan_tag is not None:
            self._logical_interface_vlan_tag = logical_interface_vlan_tag
        if logical_interface_type is not None:
            self._logical_interface_type = logical_interface_type
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for logical-interface.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for logical-interface.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
    #end dump

#end class LogicalInterface

class ServiceInstance(object):
    """
    Represents service-instance configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * service_instance_properties
            Type: :class:`.ServiceInstanceType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * service_instance_bindings
            Type: :class:`.KeyValuePairs`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.PortTuple` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of :class:`.ServiceTemplate` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of (:class:`.InstanceIp` object, :class:`.ServiceInterfaceTag` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualMachine` objects
        * list of :class:`.ServiceHealthCheck` objects
        * list of :class:`.InterfaceRouteTable` objects
        * list of :class:`.RoutingPolicy` objects
        * list of :class:`.RouteAggregate` objects
        * list of :class:`.LogicalRouter` objects
        * list of :class:`.LoadbalancerPool` objects
        * list of :class:`.Loadbalancer` objects
    """

    prop_fields = set([u'service_instance_properties', u'service_instance_bindings', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['service_template_refs', u'instance_ip_refs'])
    backref_fields = set([u'virtual_machine_back_refs', 'service_health_check_back_refs', 'interface_route_table_back_refs', 'routing_policy_back_refs', 'route_aggregate_back_refs', 'logical_router_back_refs', u'loadbalancer_pool_back_refs', 'loadbalancer_back_refs'])
    children_fields = set([u'port_tuples'])

    prop_field_types = {
        'service_instance_properties': {'xsd_type': u'ServiceInstanceType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'service_instance_bindings': {'xsd_type': u'KeyValuePairs', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_template_refs'] = ('service-template', 'None', False)
    ref_field_types['instance_ip_refs'] = ('instance-ip', 'ServiceInterfaceTag', False)

    backref_field_types = {}
    backref_field_types['virtual_machine_back_refs'] = ('virtual-machine', 'None', True)
    backref_field_types['service_health_check_back_refs'] = ('service-health-check', 'ServiceInterfaceTag', True)
    backref_field_types['interface_route_table_back_refs'] = ('interface-route-table', 'ServiceInterfaceTag', True)
    backref_field_types['routing_policy_back_refs'] = ('routing-policy', 'RoutingPolicyServiceInstanceType', False)
    backref_field_types['route_aggregate_back_refs'] = ('route-aggregate', 'ServiceInterfaceTag', False)
    backref_field_types['logical_router_back_refs'] = ('logical-router', 'None', False)
    backref_field_types['loadbalancer_pool_back_refs'] = ('loadbalancer-pool', 'None', False)
    backref_field_types['loadbalancer_back_refs'] = ('loadbalancer', 'None', False)

    children_field_types = {}
    children_field_types['port_tuples'] = ('port-tuple', True)

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['service_instance_properties'] = 'service-instance-properties'
    prop_field_metas['service_instance_bindings'] = 'service-instance-bindings'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_template_refs'] = 'service-instance-service-template'
    ref_field_metas['instance_ip_refs'] = 'service-instance-shared-ip'

    children_field_metas = {}
    children_field_metas['port_tuples'] = 'service-instance-port-tuple'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([u'service_instance_bindings'])

    prop_map_field_has_wrappers = {}
    prop_map_field_has_wrappers['service_instance_bindings'] = True

    prop_map_field_key_names = {}
    prop_map_field_key_names['service_instance_bindings'] = 'key'

    def __init__(self, name = None, parent_obj = None, service_instance_properties=None, service_instance_bindings=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if service_instance_properties is not None:
            self._service_instance_properties = service_instance_properties
        if service_instance_bindings is not None:
            self._service_instance_bindings = service_instance_bindings
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def service_instance_bindings(self):
        """Get service-instance-bindings for service-instance.
        
        :returns: KeyValuePairs object
        
        """
        return getattr(self, '_service_instance_bindings', None)
    #end service_instance_bindings

    @service_instance_bindings.setter
    def service_instance_bindings(self, service_instance_bindings):
        """Set service-instance-bindings for service-instance.
        
        :param service_instance_bindings: KeyValuePairs object
        
        """
        self._service_instance_bindings = service_instance_bindings
    #end service_instance_bindings

    def set_service_instance_bindings(self, value):
        self.service_instance_bindings = value
    #end set_service_instance_bindings

    def get_service_instance_bindings(self):
        return self.service_instance_bindings
    #end get_service_instance_bindings

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
    def perms2(self):
        """Get perms2 for service-instance.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-instance.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_service_instance_bindings'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_bindings')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_template_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_template_refs')
        if hasattr(self, 'instance_ip_refs'):
            self._serialize_field_to_json(serialized, field_names, 'instance_ip_refs')
        return serialized
    #end serialize_to_json

    def get_port_tuples(self):
        return getattr(self, 'port_tuples', None)
    #end get_port_tuples

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

    def set_instance_ip(self, ref_obj, ref_data):
        """Set instance-ip for service-instance.
        
        :param ref_obj: InstanceIp object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self.instance_ip_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.instance_ip_refs[0]['uuid'] = ref_obj.uuid

    #end set_instance_ip

    def add_instance_ip(self, ref_obj, ref_data):
        """Add instance-ip to service-instance.
        
        :param ref_obj: InstanceIp object
        :param ref_data: ServiceInterfaceTag object
        
        """
        refs = getattr(self, 'instance_ip_refs', [])
        if not refs:
            self.instance_ip_refs = []

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

        self.instance_ip_refs.append(ref_info)
    #end add_instance_ip

    def del_instance_ip(self, ref_obj):
        refs = self.get_instance_ip_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.instance_ip_refs.remove(ref)
                return
    #end del_instance_ip

    def set_instance_ip_list(self, ref_obj_list, ref_data_list):
        """Set instance-ip list for service-instance.
        
        :param ref_obj_list: list of InstanceIp object
        :param ref_data_list: list of ServiceInterfaceTag object
        
        """
        self.instance_ip_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_instance_ip_list

    def get_instance_ip_refs(self):
        """Return instance-ip list for service-instance.
        
        :returns: list of tuple <InstanceIp, ServiceInterfaceTag>
        
        """
        return getattr(self, 'instance_ip_refs', None)
    #end get_instance_ip_refs

    def get_virtual_machine_back_refs(self):
        """Return list of all virtual-machines using this service-instance"""
        return getattr(self, 'virtual_machine_back_refs', None)
    #end get_virtual_machine_back_refs

    def get_service_health_check_back_refs(self):
        """Return list of all service-health-checks using this service-instance"""
        return getattr(self, 'service_health_check_back_refs', None)
    #end get_service_health_check_back_refs

    def get_interface_route_table_back_refs(self):
        """Return list of all interface-route-tables using this service-instance"""
        return getattr(self, 'interface_route_table_back_refs', None)
    #end get_interface_route_table_back_refs

    def get_routing_policy_back_refs(self):
        """Return list of all routing-policys using this service-instance"""
        return getattr(self, 'routing_policy_back_refs', None)
    #end get_routing_policy_back_refs

    def get_route_aggregate_back_refs(self):
        """Return list of all route-aggregates using this service-instance"""
        return getattr(self, 'route_aggregate_back_refs', None)
    #end get_route_aggregate_back_refs

    def get_logical_router_back_refs(self):
        """Return list of all logical-routers using this service-instance"""
        return getattr(self, 'logical_router_back_refs', None)
    #end get_logical_router_back_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this service-instance"""
        return getattr(self, 'loadbalancer_pool_back_refs', None)
    #end get_loadbalancer_pool_back_refs

    def get_loadbalancer_back_refs(self):
        """Return list of all loadbalancers using this service-instance"""
        return getattr(self, 'loadbalancer_back_refs', None)
    #end get_loadbalancer_back_refs

    def dump(self):
        """Display service-instance object in compact form."""
        print '------------ service-instance ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_instance_properties = ', self.get_service_instance_properties()
        print 'P service_instance_bindings = ', self.get_service_instance_bindings()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_template = ', self.get_service_template_refs()
        print 'REF instance_ip = ', self.get_instance_ip_refs()
        print 'HAS port_tuple = ', self.get_port_tuples()
        print 'BCK virtual_machine = ', self.get_virtual_machine_back_refs()
        print 'BCK service_health_check = ', self.get_service_health_check_back_refs()
        print 'BCK interface_route_table = ', self.get_interface_route_table_back_refs()
        print 'BCK routing_policy = ', self.get_routing_policy_back_refs()
        print 'BCK route_aggregate = ', self.get_route_aggregate_back_refs()
        print 'BCK logical_router = ', self.get_logical_router_back_refs()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
        print 'BCK loadbalancer = ', self.get_loadbalancer_back_refs()
    #end dump

#end class ServiceInstance

class RouteTable(object):
    """
    Represents route-table configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * routes
            Type: :class:`.RouteTableType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
        * list of :class:`.VirtualNetwork` objects
    """

    prop_fields = set([u'routes', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set(['virtual_network_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'routes': {'xsd_type': u'RouteTableType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['virtual_network_back_refs'] = ('virtual-network', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['routes'] = 'routes'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, routes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if routes is not None:
            self._routes = routes
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for route-table.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for route-table.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

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
        print 'P perms2 = ', self.get_perms2()
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
        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.LogicalInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of :class:`.PhysicalInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.ServiceAppliance` objects
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.PhysicalInterface` objects
    """

    prop_fields = set([u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'physical_interface_refs'])
    backref_fields = set([u'service_appliance_back_refs', 'virtual_machine_interface_back_refs', u'physical_interface_back_refs'])
    children_fields = set([u'logical_interfaces'])

    prop_field_types = {
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['physical_interface_refs'] = ('physical-interface', 'None', False)

    backref_field_types = {}
    backref_field_types['service_appliance_back_refs'] = ('service-appliance', 'ServiceApplianceInterfaceType', False)
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)
    backref_field_types['physical_interface_back_refs'] = ('physical-interface', 'None', False)

    children_field_types = {}
    children_field_types['logical_interfaces'] = ('logical-interface', False)

    parent_types = ['physical-router']

    prop_field_metas = {}
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['physical_interface_refs'] = 'physical-interface-connection'

    children_field_metas = {}
    children_field_metas['logical_interfaces'] = 'physical-interface-logical-interface'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
            self.fq_name = [u'default-global-system-config', 'default-physical-router']
            self.fq_name.append(name)


        # property fields
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for physical-interface.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for physical-interface.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'physical_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'physical_interface_refs')
        return serialized
    #end serialize_to_json

    def get_logical_interfaces(self):
        return getattr(self, 'logical_interfaces', None)
    #end get_logical_interfaces

    def set_physical_interface(self, ref_obj):
        """Set physical-interface for physical-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        self.physical_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.physical_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_physical_interface

    def add_physical_interface(self, ref_obj):
        """Add physical-interface to physical-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        refs = getattr(self, 'physical_interface_refs', [])
        if not refs:
            self.physical_interface_refs = []

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

        self.physical_interface_refs.append(ref_info)
    #end add_physical_interface

    def del_physical_interface(self, ref_obj):
        refs = self.get_physical_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.physical_interface_refs.remove(ref)
                return
    #end del_physical_interface

    def set_physical_interface_list(self, ref_obj_list):
        """Set physical-interface list for physical-interface.
        
        :param ref_obj_list: list of PhysicalInterface object
        
        """
        self.physical_interface_refs = ref_obj_list
    #end set_physical_interface_list

    def get_physical_interface_refs(self):
        """Return physical-interface list for physical-interface.
        
        :returns: list of <PhysicalInterface>
        
        """
        return getattr(self, 'physical_interface_refs', None)
    #end get_physical_interface_refs

    def get_service_appliance_back_refs(self):
        """Return list of all service-appliances using this physical-interface"""
        return getattr(self, 'service_appliance_back_refs', None)
    #end get_service_appliance_back_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this physical-interface"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def get_physical_interface_back_refs(self):
        """Return list of all physical-interfaces using this physical-interface"""
        return getattr(self, 'physical_interface_back_refs', None)
    #end get_physical_interface_back_refs

    def dump(self):
        """Display physical-interface object in compact form."""
        print '------------ physical-interface ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS logical_interface = ', self.get_logical_interfaces()
        print 'REF physical_interface = ', self.get_physical_interface_refs()
        print 'BCK service_appliance = ', self.get_service_appliance_back_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
        print 'BCK physical_interface = ', self.get_physical_interface_back_refs()
    #end dump

#end class PhysicalInterface

class AccessControlList(object):
    """
    Represents access-control-list configuration representation.

    Child of:
        :class:`.VirtualNetwork` object OR
        :class:`.SecurityGroup` object OR

    Properties:
        * access_control_list_entries
            Type: :class:`.AclEntriesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'access_control_list_entries', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'access_control_list_entries': {'xsd_type': u'AclEntriesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = ['virtual-network', u'security-group']

    prop_field_metas = {}
    prop_field_metas['access_control_list_entries'] = 'access-control-list-entries'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, access_control_list_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
                raise AmbiguousParentError("[[u'default-domain', u'default-project', 'default-virtual-network'], [u'default-domain', u'default-project', u'default-security-group']]")

        # property fields
        if access_control_list_entries is not None:
            self._access_control_list_entries = access_control_list_entries
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for access-control-list.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for access-control-list.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display access-control-list object in compact form."""
        print '------------ access-control-list ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P access_control_list_entries = ', self.get_access_control_list_entries()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class AccessControlList

class BgpAsAService(object):
    """
    Represents bgp-as-a-service configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * autonomous_system
            Type: int, *one-of* [u'1', u'65534']

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * bgpaas_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * bgpaas_session_attributes
            Type: :class:`.BgpSessionAttributes`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.BgpRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'autonomous_system', u'bgpaas_ip_address', u'bgpaas_session_attributes', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs', 'bgp_router_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'autonomous_system': {'xsd_type': u'integer', 'restrictions': [u'1', u'65534'], 'simple_type': u'AutonomousSystemType', 'is_complex': False},
        'bgpaas_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'bgpaas_session_attributes': {'xsd_type': u'BgpSessionAttributes', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)
    ref_field_types['bgp_router_refs'] = ('bgp-router', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['autonomous_system'] = 'autonomous-system'
    prop_field_metas['bgpaas_ip_address'] = 'bgpaas-ip-address'
    prop_field_metas['bgpaas_session_attributes'] = 'bgpaas-session-attributes'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_machine_interface_refs'] = 'bgpaas-virtual-machine-interface'
    ref_field_metas['bgp_router_refs'] = 'bgpaas-bgp-router'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, autonomous_system=None, bgpaas_ip_address=None, bgpaas_session_attributes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'bgp-as-a-service'
        if not name:
            name = u'default-bgp-as-a-service'
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
        if autonomous_system is not None:
            self._autonomous_system = autonomous_system
        if bgpaas_ip_address is not None:
            self._bgpaas_ip_address = bgpaas_ip_address
        if bgpaas_session_attributes is not None:
            self._bgpaas_session_attributes = bgpaas_session_attributes
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (bgp-as-a-service)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of bgp-as-a-service in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of bgp-as-a-service as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of bgp-as-a-service's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of bgp-as-a-service's parent as colon delimted string."""
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
        """Get autonomous-system for bgp-as-a-service.
        
        :returns: AutonomousSystemType object
        
        """
        return getattr(self, '_autonomous_system', None)
    #end autonomous_system

    @autonomous_system.setter
    def autonomous_system(self, autonomous_system):
        """Set autonomous-system for bgp-as-a-service.
        
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
    def bgpaas_ip_address(self):
        """Get bgpaas-ip-address for bgp-as-a-service.
        
        :returns: IpAddressType object
        
        """
        return getattr(self, '_bgpaas_ip_address', None)
    #end bgpaas_ip_address

    @bgpaas_ip_address.setter
    def bgpaas_ip_address(self, bgpaas_ip_address):
        """Set bgpaas-ip-address for bgp-as-a-service.
        
        :param bgpaas_ip_address: IpAddressType object
        
        """
        self._bgpaas_ip_address = bgpaas_ip_address
    #end bgpaas_ip_address

    def set_bgpaas_ip_address(self, value):
        self.bgpaas_ip_address = value
    #end set_bgpaas_ip_address

    def get_bgpaas_ip_address(self):
        return self.bgpaas_ip_address
    #end get_bgpaas_ip_address

    @property
    def bgpaas_session_attributes(self):
        """Get bgpaas-session-attributes for bgp-as-a-service.
        
        :returns: BgpSessionAttributes object
        
        """
        return getattr(self, '_bgpaas_session_attributes', None)
    #end bgpaas_session_attributes

    @bgpaas_session_attributes.setter
    def bgpaas_session_attributes(self, bgpaas_session_attributes):
        """Set bgpaas-session-attributes for bgp-as-a-service.
        
        :param bgpaas_session_attributes: BgpSessionAttributes object
        
        """
        self._bgpaas_session_attributes = bgpaas_session_attributes
    #end bgpaas_session_attributes

    def set_bgpaas_session_attributes(self, value):
        self.bgpaas_session_attributes = value
    #end set_bgpaas_session_attributes

    def get_bgpaas_session_attributes(self):
        return self.bgpaas_session_attributes
    #end get_bgpaas_session_attributes

    @property
    def id_perms(self):
        """Get id-perms for bgp-as-a-service.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for bgp-as-a-service.
        
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
    def perms2(self):
        """Get perms2 for bgp-as-a-service.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for bgp-as-a-service.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for bgp-as-a-service.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for bgp-as-a-service.
        
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
        if hasattr(self, '_bgpaas_ip_address'):
            self._serialize_field_to_json(serialized, field_names, 'bgpaas_ip_address')
        if hasattr(self, '_bgpaas_session_attributes'):
            self._serialize_field_to_json(serialized, field_names, 'bgpaas_session_attributes')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        if hasattr(self, 'bgp_router_refs'):
            self._serialize_field_to_json(serialized, field_names, 'bgp_router_refs')
        return serialized
    #end serialize_to_json

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for bgp-as-a-service.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to bgp-as-a-service.
        
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
        """Set virtual-machine-interface list for bgp-as-a-service.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for bgp-as-a-service.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def set_bgp_router(self, ref_obj):
        """Set bgp-router for bgp-as-a-service.
        
        :param ref_obj: BgpRouter object
        
        """
        self.bgp_router_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.bgp_router_refs[0]['uuid'] = ref_obj.uuid

    #end set_bgp_router

    def add_bgp_router(self, ref_obj):
        """Add bgp-router to bgp-as-a-service.
        
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
        """Set bgp-router list for bgp-as-a-service.
        
        :param ref_obj_list: list of BgpRouter object
        
        """
        self.bgp_router_refs = ref_obj_list
    #end set_bgp_router_list

    def get_bgp_router_refs(self):
        """Return bgp-router list for bgp-as-a-service.
        
        :returns: list of <BgpRouter>
        
        """
        return getattr(self, 'bgp_router_refs', None)
    #end get_bgp_router_refs

    def dump(self):
        """Display bgp-as-a-service object in compact form."""
        print '------------ bgp-as-a-service ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P autonomous_system = ', self.get_autonomous_system()
        print 'P bgpaas_ip_address = ', self.get_bgpaas_ip_address()
        print 'P bgpaas_session_attributes = ', self.get_bgpaas_session_attributes()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF bgp_router = ', self.get_bgp_router_refs()
    #end dump

#end class BgpAsAService

class PortTuple(object):
    """
    Represents port-tuple configuration representation.

    Child of:
        :class:`.ServiceInstance` object OR

    Properties:
        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set(['virtual_machine_interface_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)

    children_field_types = {}

    parent_types = [u'service-instance']

    prop_field_metas = {}
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'port-tuple'
        if not name:
            name = u'default-port-tuple'
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
            self.parent_type = 'service-instance'
            self.fq_name = [u'default-domain', u'default-project', u'default-service-instance']
            self.fq_name.append(name)


        # property fields
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (port-tuple)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of port-tuple in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of port-tuple as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of port-tuple's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of port-tuple's parent as colon delimted string."""
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
        """Get id-perms for port-tuple.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for port-tuple.
        
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
    def perms2(self):
        """Get perms2 for port-tuple.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for port-tuple.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for port-tuple.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for port-tuple.
        
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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this port-tuple"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def dump(self):
        """Display port-tuple object in compact form."""
        print '------------ port-tuple ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class PortTuple

class AnalyticsNode(object):
    """
    Represents analytics-node configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * analytics_node_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'analytics_node_ip_address', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'analytics_node_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'global-system-config']

    prop_field_metas = {}
    prop_field_metas['analytics_node_ip_address'] = 'analytics-node-ip-address'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, analytics_node_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if analytics_node_ip_address is not None:
            self._analytics_node_ip_address = analytics_node_ip_address
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for analytics-node.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for analytics-node.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display analytics-node object in compact form."""
        print '------------ analytics-node ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P analytics_node_ip_address = ', self.get_analytics_node_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class AnalyticsNode

class VirtualDns(object):
    """
    Represents virtual-DNS configuration representation.

    Child of:
        :class:`.Domain` object OR

    Properties:
        * virtual_DNS_data
            Type: :class:`.VirtualDnsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.VirtualDnsRecord` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:

    Referred by:
        * list of :class:`.NetworkIpam` objects
    """

    prop_fields = set([u'virtual_DNS_data', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'network_ipam_back_refs'])
    children_fields = set([u'virtual_DNS_records'])

    prop_field_types = {
        'virtual_DNS_data': {'xsd_type': u'VirtualDnsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['network_ipam_back_refs'] = ('network-ipam', 'None', False)

    children_field_types = {}
    children_field_types['virtual_DNS_records'] = ('virtual-DNS-record', False)

    parent_types = [u'domain']

    prop_field_metas = {}
    prop_field_metas['virtual_DNS_data'] = 'virtual-DNS-data'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}
    children_field_metas['virtual_DNS_records'] = 'virtual-DNS-virtual-DNS-record'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, virtual_DNS_data=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if virtual_DNS_data is not None:
            self._virtual_DNS_data = virtual_DNS_data
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for virtual-DNS.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-DNS.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_virtual_DNS_records(self):
        return getattr(self, 'virtual_DNS_records', None)
    #end get_virtual_DNS_records

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS virtual_DNS_record = ', self.get_virtual_DNS_records()
        print 'BCK network_ipam = ', self.get_network_ipam_back_refs()
    #end dump

#end class VirtualDns

class CustomerAttachment(object):
    """
    Represents customer-attachment configuration representation.

    Properties:
        * attachment_address
            Type: :class:`.AttachmentAddressType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.FloatingIp` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'attachment_address', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs', u'floating_ip_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'attachment_address': {'xsd_type': u'AttachmentAddressType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)
    ref_field_types['floating_ip_refs'] = ('floating-ip', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['attachment_address'] = 'attachment-address'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_machine_interface_refs'] = 'customer-attachment-virtual-machine-interface'
    ref_field_metas['floating_ip_refs'] = 'customer-attachment-floating-ip'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, attachment_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'customer-attachment'
        if not name:
            name = u'default-customer-attachment'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if attachment_address is not None:
            self._attachment_address = attachment_address
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for customer-attachment.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for customer-attachment.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
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
        * service_appliance_set_properties
            Type: :class:`.KeyValuePairs`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * service_appliance_driver
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * service_appliance_ha_mode
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.ServiceAppliance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:

    Referred by:
        * list of :class:`.ServiceTemplate` objects
        * list of :class:`.LoadbalancerPool` objects
    """

    prop_fields = set([u'service_appliance_set_properties', u'service_appliance_driver', u'service_appliance_ha_mode', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set(['service_template_back_refs', u'loadbalancer_pool_back_refs'])
    children_fields = set([u'service_appliances'])

    prop_field_types = {
        'service_appliance_set_properties': {'xsd_type': u'KeyValuePairs', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'service_appliance_driver': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'service_appliance_ha_mode': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['service_template_back_refs'] = ('service-template', 'None', False)
    backref_field_types['loadbalancer_pool_back_refs'] = ('loadbalancer-pool', 'None', False)

    children_field_types = {}
    children_field_types['service_appliances'] = ('service-appliance', False)

    parent_types = [u'global-system-config']

    prop_field_metas = {}
    prop_field_metas['service_appliance_set_properties'] = 'service-appliance-set-properties'
    prop_field_metas['service_appliance_driver'] = 'service-appliance-driver'
    prop_field_metas['service_appliance_ha_mode'] = 'service-appliance-ha-mode'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}
    children_field_metas['service_appliances'] = 'service-appliance-set-service-appliance'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, service_appliance_set_properties=None, service_appliance_driver=None, service_appliance_ha_mode=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if service_appliance_set_properties is not None:
            self._service_appliance_set_properties = service_appliance_set_properties
        if service_appliance_driver is not None:
            self._service_appliance_driver = service_appliance_driver
        if service_appliance_ha_mode is not None:
            self._service_appliance_ha_mode = service_appliance_ha_mode
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for service-appliance-set.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-appliance-set.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_service_appliances(self):
        return getattr(self, 'service_appliances', None)
    #end get_service_appliances

    def get_service_template_back_refs(self):
        """Return list of all service-templates using this service-appliance-set"""
        return getattr(self, 'service_template_back_refs', None)
    #end get_service_template_back_refs

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS service_appliance = ', self.get_service_appliances()
        print 'BCK service_template = ', self.get_service_template_back_refs()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
    #end dump

#end class ServiceApplianceSet

class ConfigNode(object):
    """
    Represents config-node configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * config_node_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'config_node_ip_address', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'config_node_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'global-system-config']

    prop_field_metas = {}
    prop_field_metas['config_node_ip_address'] = 'config-node-ip-address'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, config_node_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if config_node_ip_address is not None:
            self._config_node_ip_address = config_node_ip_address
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for config-node.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for config-node.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display config-node object in compact form."""
        print '------------ config-node ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P config_node_ip_address = ', self.get_config_node_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class ConfigNode

class QosQueue(object):
    """
    Represents qos-queue configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * min_bandwidth
            Type: int

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * max_bandwidth
            Type: int

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
        * list of :class:`.QosForwardingClass` objects
    """

    prop_fields = set([u'min_bandwidth', u'max_bandwidth', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'qos_forwarding_class_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'min_bandwidth': {'xsd_type': u'integer', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'max_bandwidth': {'xsd_type': u'integer', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['qos_forwarding_class_back_refs'] = ('qos-forwarding-class', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['min_bandwidth'] = 'min-bandwidth'
    prop_field_metas['max_bandwidth'] = 'max-bandwidth'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, min_bandwidth=None, max_bandwidth=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if min_bandwidth is not None:
            self._min_bandwidth = min_bandwidth
        if max_bandwidth is not None:
            self._max_bandwidth = max_bandwidth
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for qos-queue.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for qos-queue.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'BCK qos_forwarding_class = ', self.get_qos_forwarding_class_back_refs()
    #end dump

#end class QosQueue

class VirtualMachine(object):
    """
    Represents virtual-machine configuration representation.

    Properties:
        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of :class:`.ServiceInstance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.VirtualRouter` objects
    """

    prop_fields = set([u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_instance_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs', 'virtual_router_back_refs'])
    children_fields = set(['virtual_machine_interfaces'])

    prop_field_types = {
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_instance_refs'] = ('service-instance', 'None', True)

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)
    backref_field_types['virtual_router_back_refs'] = ('virtual-router', 'None', False)

    children_field_types = {}
    children_field_types['virtual_machine_interfaces'] = ('virtual-machine-interface', False)

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_instance_refs'] = 'virtual-machine-service-instance'

    children_field_metas = {}
    children_field_metas['virtual_machine_interfaces'] = 'virtual-machine-virtual-machine-interface'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'virtual-machine'
        if not name:
            name = u'default-virtual-machine'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for virtual-machine.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-machine.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
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
        * interface_route_table_routes
            Type: :class:`.RouteTableType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of (:class:`.ServiceInstance` object, :class:`.ServiceInterfaceTag` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'interface_route_table_routes', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_instance_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'interface_route_table_routes': {'xsd_type': u'RouteTableType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_instance_refs'] = ('service-instance', 'ServiceInterfaceTag', True)

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['interface_route_table_routes'] = 'interface-route-table-routes'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_instance_refs'] = 'interface-route-table-service-instance'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, interface_route_table_routes=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if interface_route_table_routes is not None:
            self._interface_route_table_routes = interface_route_table_routes
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for interface-route-table.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for interface-route-table.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        return serialized
    #end serialize_to_json

    def set_service_instance(self, ref_obj, ref_data):
        """Set service-instance for interface-route-table.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj, ref_data):
        """Add service-instance to interface-route-table.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        refs = getattr(self, 'service_instance_refs', [])
        if not refs:
            self.service_instance_refs = []

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

    def set_service_instance_list(self, ref_obj_list, ref_data_list):
        """Set service-instance list for interface-route-table.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of ServiceInterfaceTag object
        
        """
        self.service_instance_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for interface-route-table.
        
        :returns: list of tuple <ServiceInstance, ServiceInterfaceTag>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class InterfaceRouteTable

class ServiceTemplate(object):
    """
    Represents service-template configuration representation.

    Child of:
        :class:`.Domain` object OR

    Properties:
        * service_template_properties
            Type: :class:`.ServiceTemplateType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.ServiceApplianceSet` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.ServiceInstance` objects
    """

    prop_fields = set([u'service_template_properties', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_appliance_set_refs'])
    backref_fields = set([u'service_instance_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'service_template_properties': {'xsd_type': u'ServiceTemplateType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_appliance_set_refs'] = ('service-appliance-set', 'None', False)

    backref_field_types = {}
    backref_field_types['service_instance_back_refs'] = ('service-instance', 'None', False)

    children_field_types = {}

    parent_types = [u'domain']

    prop_field_metas = {}
    prop_field_metas['service_template_properties'] = 'service-template-properties'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_appliance_set_refs'] = 'service-template-service-appliance-set'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, service_template_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if service_template_properties is not None:
            self._service_template_properties = service_template_properties
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for service-template.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-template.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_appliance_set_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_appliance_set_refs')
        return serialized
    #end serialize_to_json

    def set_service_appliance_set(self, ref_obj):
        """Set service-appliance-set for service-template.
        
        :param ref_obj: ServiceApplianceSet object
        
        """
        self.service_appliance_set_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_appliance_set_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_appliance_set

    def add_service_appliance_set(self, ref_obj):
        """Add service-appliance-set to service-template.
        
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
        """Set service-appliance-set list for service-template.
        
        :param ref_obj_list: list of ServiceApplianceSet object
        
        """
        self.service_appliance_set_refs = ref_obj_list
    #end set_service_appliance_set_list

    def get_service_appliance_set_refs(self):
        """Return service-appliance-set list for service-template.
        
        :returns: list of <ServiceApplianceSet>
        
        """
        return getattr(self, 'service_appliance_set_refs', None)
    #end get_service_appliance_set_refs

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_appliance_set = ', self.get_service_appliance_set_refs()
        print 'BCK service_instance = ', self.get_service_instance_back_refs()
    #end dump

#end class ServiceTemplate

class DsaRule(object):
    """
    Represents dsa-rule configuration representation.

    Child of:
        :class:`.DiscoveryServiceAssignment` object OR

    Properties:
        * dsa_rule_entry
            Type: :class:`.DiscoveryServiceAssignmentType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'dsa_rule_entry', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'dsa_rule_entry': {'xsd_type': u'DiscoveryServiceAssignmentType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'discovery-service-assignment']

    prop_field_metas = {}
    prop_field_metas['dsa_rule_entry'] = 'dsa-rule-entry'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, dsa_rule_entry=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'dsa-rule'
        if not name:
            name = u'default-dsa-rule'
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
            self.parent_type = 'discovery-service-assignment'
            self.fq_name = [u'default-discovery-service-assignment']
            self.fq_name.append(name)


        # property fields
        if dsa_rule_entry is not None:
            self._dsa_rule_entry = dsa_rule_entry
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (dsa-rule)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of dsa-rule in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of dsa-rule as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of dsa-rule's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of dsa-rule's parent as colon delimted string."""
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
    def dsa_rule_entry(self):
        """Get dsa-rule-entry for dsa-rule.
        
        :returns: DiscoveryServiceAssignmentType object
        
        """
        return getattr(self, '_dsa_rule_entry', None)
    #end dsa_rule_entry

    @dsa_rule_entry.setter
    def dsa_rule_entry(self, dsa_rule_entry):
        """Set dsa-rule-entry for dsa-rule.
        
        :param dsa_rule_entry: DiscoveryServiceAssignmentType object
        
        """
        self._dsa_rule_entry = dsa_rule_entry
    #end dsa_rule_entry

    def set_dsa_rule_entry(self, value):
        self.dsa_rule_entry = value
    #end set_dsa_rule_entry

    def get_dsa_rule_entry(self):
        return self.dsa_rule_entry
    #end get_dsa_rule_entry

    @property
    def id_perms(self):
        """Get id-perms for dsa-rule.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for dsa-rule.
        
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
    def perms2(self):
        """Get perms2 for dsa-rule.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for dsa-rule.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for dsa-rule.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for dsa-rule.
        
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
        if hasattr(self, '_dsa_rule_entry'):
            self._serialize_field_to_json(serialized, field_names, 'dsa_rule_entry')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display dsa-rule object in compact form."""
        print '------------ dsa-rule ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P dsa_rule_entry = ', self.get_dsa_rule_entry()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class DsaRule

class VirtualIp(object):
    """
    Represents virtual-ip configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * virtual_ip_properties
            Type: :class:`.VirtualIpType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.LoadbalancerPool` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'virtual_ip_properties', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'loadbalancer_pool_refs', 'virtual_machine_interface_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'virtual_ip_properties': {'xsd_type': u'VirtualIpType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['loadbalancer_pool_refs'] = ('loadbalancer-pool', 'None', False)
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['virtual_ip_properties'] = 'virtual-ip-properties'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['loadbalancer_pool_refs'] = 'virtual-ip-loadbalancer-pool'
    ref_field_metas['virtual_machine_interface_refs'] = 'virtual-ip-virtual-machine-interface'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, virtual_ip_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if virtual_ip_properties is not None:
            self._virtual_ip_properties = virtual_ip_properties
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for virtual-ip.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-ip.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def dump(self):
        """Display virtual-ip object in compact form."""
        print '------------ virtual-ip ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P virtual_ip_properties = ', self.get_virtual_ip_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
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
        * loadbalancer_member_properties
            Type: :class:`.LoadbalancerMemberType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'loadbalancer_member_properties', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'loadbalancer_member_properties': {'xsd_type': u'LoadbalancerMemberType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'loadbalancer-pool']

    prop_field_metas = {}
    prop_field_metas['loadbalancer_member_properties'] = 'loadbalancer-member-properties'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, loadbalancer_member_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if loadbalancer_member_properties is not None:
            self._loadbalancer_member_properties = loadbalancer_member_properties
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for loadbalancer-member.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-member.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display loadbalancer-member object in compact form."""
        print '------------ loadbalancer-member ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P loadbalancer_member_properties = ', self.get_loadbalancer_member_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class LoadbalancerMember

class SecurityGroup(object):
    """
    Represents security-group configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * security_group_id
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * configured_security_group_id
            Type: int

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * security_group_entries
            Type: :class:`.PolicyEntriesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.AccessControlList` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:

    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'security_group_id', u'configured_security_group_id', u'security_group_entries', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set(['virtual_machine_interface_back_refs'])
    children_fields = set([u'access_control_lists'])

    prop_field_types = {
        'security_group_id': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'configured_security_group_id': {'xsd_type': u'integer', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'security_group_entries': {'xsd_type': u'PolicyEntriesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)

    children_field_types = {}
    children_field_types['access_control_lists'] = ('access-control-list', True)

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['security_group_id'] = 'security-group-id'
    prop_field_metas['configured_security_group_id'] = 'configured-security-group-id'
    prop_field_metas['security_group_entries'] = 'security-group-entries'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}
    children_field_metas['access_control_lists'] = 'security-group-access-control-list'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, security_group_id=None, configured_security_group_id=None, security_group_entries=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if security_group_id is not None:
            self._security_group_id = security_group_id
        if configured_security_group_id is not None:
            self._configured_security_group_id = configured_security_group_id
        if security_group_entries is not None:
            self._security_group_entries = security_group_entries
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for security-group.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for security-group.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def get_access_control_lists(self):
        return getattr(self, 'access_control_lists', None)
    #end get_access_control_lists

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS access_control_list = ', self.get_access_control_lists()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class SecurityGroup

class ServiceHealthCheck(object):
    """
    Represents service-health-check configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * service_health_check_properties
            Type: :class:`.ServiceHealthCheckType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of (:class:`.ServiceInstance` object, :class:`.ServiceInterfaceTag` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'service_health_check_properties', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_instance_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'service_health_check_properties': {'xsd_type': u'ServiceHealthCheckType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_instance_refs'] = ('service-instance', 'ServiceInterfaceTag', True)

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['service_health_check_properties'] = 'service-health-check-properties'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_instance_refs'] = 'service-health-check-service-instance'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, service_health_check_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'service-health-check'
        if not name:
            name = u'default-service-health-check'
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
        if service_health_check_properties is not None:
            self._service_health_check_properties = service_health_check_properties
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (service-health-check)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of service-health-check in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of service-health-check as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of service-health-check's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of service-health-check's parent as colon delimted string."""
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
    def service_health_check_properties(self):
        """Get service-health-check-properties for service-health-check.
        
        :returns: ServiceHealthCheckType object
        
        """
        return getattr(self, '_service_health_check_properties', None)
    #end service_health_check_properties

    @service_health_check_properties.setter
    def service_health_check_properties(self, service_health_check_properties):
        """Set service-health-check-properties for service-health-check.
        
        :param service_health_check_properties: ServiceHealthCheckType object
        
        """
        self._service_health_check_properties = service_health_check_properties
    #end service_health_check_properties

    def set_service_health_check_properties(self, value):
        self.service_health_check_properties = value
    #end set_service_health_check_properties

    def get_service_health_check_properties(self):
        return self.service_health_check_properties
    #end get_service_health_check_properties

    @property
    def id_perms(self):
        """Get id-perms for service-health-check.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for service-health-check.
        
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
    def perms2(self):
        """Get perms2 for service-health-check.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for service-health-check.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for service-health-check.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for service-health-check.
        
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
        if hasattr(self, '_service_health_check_properties'):
            self._serialize_field_to_json(serialized, field_names, 'service_health_check_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        return serialized
    #end serialize_to_json

    def set_service_instance(self, ref_obj, ref_data):
        """Set service-instance for service-health-check.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj, ref_data):
        """Add service-instance to service-health-check.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        refs = getattr(self, 'service_instance_refs', [])
        if not refs:
            self.service_instance_refs = []

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

    def set_service_instance_list(self, ref_obj_list, ref_data_list):
        """Set service-instance list for service-health-check.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of ServiceInterfaceTag object
        
        """
        self.service_instance_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for service-health-check.
        
        :returns: list of tuple <ServiceInstance, ServiceInterfaceTag>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this service-health-check"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

    def dump(self):
        """Display service-health-check object in compact form."""
        print '------------ service-health-check ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_health_check_properties = ', self.get_service_health_check_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class ServiceHealthCheck

class ProviderAttachment(object):
    """
    Represents provider-attachment configuration representation.

    Properties:
        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_router_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_router_refs'] = ('virtual-router', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = []

    prop_field_metas = {}
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_router_refs'] = 'provider-attachment-virtual-router'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'provider-attachment'
        if not name:
            name = u'default-provider-attachment'
        self.name = name
        self._uuid = None
        self.fq_name = [name]

        # property fields
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for provider-attachment.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for provider-attachment.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def dump(self):
        """Display provider-attachment object in compact form."""
        print '------------ provider-attachment ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
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
        * ecmp_hashing_include_fields
            Type: :class:`.EcmpHashingIncludeFields`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_mac_addresses
            Type: :class:`.MacAddressesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_dhcp_option_list
            Type: :class:`.DhcpOptionsListType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_host_routes
            Type: :class:`.RouteTableType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_allowed_address_pairs
            Type: :class:`.AllowedAddressPairs`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * vrf_assign_table
            Type: :class:`.VrfAssignTableType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_device_owner
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_disable_policy
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_properties
            Type: :class:`.VirtualMachineInterfacePropertiesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_bindings
            Type: :class:`.KeyValuePairs`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_machine_interface_fat_flow_protocols
            Type: :class:`.FatFlowProtocols`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.QosForwardingClass` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.SecurityGroup` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachine` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualNetwork` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of (:class:`.RoutingInstance` object, :class:`.PolicyBasedForwardingRuleType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.PortTuple` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ServiceHealthCheck` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.InterfaceRouteTable` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.PhysicalInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.InstanceIp` objects
        * list of :class:`.Subnet` objects
        * list of :class:`.FloatingIp` objects
        * list of :class:`.LogicalInterface` objects
        * list of :class:`.BgpAsAService` objects
        * list of :class:`.CustomerAttachment` objects
        * list of :class:`.LogicalRouter` objects
        * list of :class:`.LoadbalancerPool` objects
        * list of :class:`.VirtualIp` objects
        * list of :class:`.Loadbalancer` objects
    """

    prop_fields = set([u'ecmp_hashing_include_fields', u'virtual_machine_interface_mac_addresses', u'virtual_machine_interface_dhcp_option_list', u'virtual_machine_interface_host_routes', u'virtual_machine_interface_allowed_address_pairs', u'vrf_assign_table', u'virtual_machine_interface_device_owner', u'virtual_machine_interface_disable_policy', u'virtual_machine_interface_properties', u'virtual_machine_interface_bindings', u'virtual_machine_interface_fat_flow_protocols', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'qos_forwarding_class_refs', u'security_group_refs', 'virtual_machine_interface_refs', u'virtual_machine_refs', 'virtual_network_refs', 'routing_instance_refs', u'port_tuple_refs', 'service_health_check_refs', 'interface_route_table_refs', u'physical_interface_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs', u'instance_ip_back_refs', u'subnet_back_refs', u'floating_ip_back_refs', u'logical_interface_back_refs', 'bgp_as_a_service_back_refs', 'customer_attachment_back_refs', 'logical_router_back_refs', u'loadbalancer_pool_back_refs', u'virtual_ip_back_refs', 'loadbalancer_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'ecmp_hashing_include_fields': {'xsd_type': u'EcmpHashingIncludeFields', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_machine_interface_mac_addresses': {'xsd_type': u'MacAddressesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_machine_interface_dhcp_option_list': {'xsd_type': u'DhcpOptionsListType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_machine_interface_host_routes': {'xsd_type': u'RouteTableType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_machine_interface_allowed_address_pairs': {'xsd_type': u'AllowedAddressPairs', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'vrf_assign_table': {'xsd_type': u'VrfAssignTableType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_machine_interface_device_owner': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'virtual_machine_interface_disable_policy': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'virtual_machine_interface_properties': {'xsd_type': u'VirtualMachineInterfacePropertiesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_machine_interface_bindings': {'xsd_type': u'KeyValuePairs', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_machine_interface_fat_flow_protocols': {'xsd_type': u'FatFlowProtocols', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['qos_forwarding_class_refs'] = ('qos-forwarding-class', 'None', False)
    ref_field_types['security_group_refs'] = ('security-group', 'None', False)
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)
    ref_field_types['virtual_machine_refs'] = ('virtual-machine', 'None', False)
    ref_field_types['virtual_network_refs'] = ('virtual-network', 'None', False)
    ref_field_types['routing_instance_refs'] = ('routing-instance', 'PolicyBasedForwardingRuleType', False)
    ref_field_types['port_tuple_refs'] = ('port-tuple', 'None', False)
    ref_field_types['service_health_check_refs'] = ('service-health-check', 'None', False)
    ref_field_types['interface_route_table_refs'] = ('interface-route-table', 'None', False)
    ref_field_types['physical_interface_refs'] = ('physical-interface', 'None', False)

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)
    backref_field_types['instance_ip_back_refs'] = ('instance-ip', 'None', False)
    backref_field_types['subnet_back_refs'] = ('subnet', 'None', False)
    backref_field_types['floating_ip_back_refs'] = ('floating-ip', 'None', False)
    backref_field_types['logical_interface_back_refs'] = ('logical-interface', 'None', False)
    backref_field_types['bgp_as_a_service_back_refs'] = ('bgp-as-a-service', 'None', False)
    backref_field_types['customer_attachment_back_refs'] = ('customer-attachment', 'None', False)
    backref_field_types['logical_router_back_refs'] = ('logical-router', 'None', False)
    backref_field_types['loadbalancer_pool_back_refs'] = ('loadbalancer-pool', 'None', False)
    backref_field_types['virtual_ip_back_refs'] = ('virtual-ip', 'None', False)
    backref_field_types['loadbalancer_back_refs'] = ('loadbalancer', 'None', False)

    children_field_types = {}

    parent_types = [u'virtual-machine', u'project']

    prop_field_metas = {}
    prop_field_metas['ecmp_hashing_include_fields'] = 'ecmp-hashing-include-fields'
    prop_field_metas['virtual_machine_interface_mac_addresses'] = 'virtual-machine-interface-mac-addresses'
    prop_field_metas['virtual_machine_interface_dhcp_option_list'] = 'virtual-machine-interface-dhcp-option-list'
    prop_field_metas['virtual_machine_interface_host_routes'] = 'virtual-machine-interface-host-routes'
    prop_field_metas['virtual_machine_interface_allowed_address_pairs'] = 'virtual-machine-interface-allowed-address-pairs'
    prop_field_metas['vrf_assign_table'] = 'vrf-assign-table'
    prop_field_metas['virtual_machine_interface_device_owner'] = 'virtual-machine-interface-device-owner'
    prop_field_metas['virtual_machine_interface_disable_policy'] = 'virtual-machine-interface-disable-policy'
    prop_field_metas['virtual_machine_interface_properties'] = 'virtual-machine-interface-properties'
    prop_field_metas['virtual_machine_interface_bindings'] = 'virtual-machine-interface-bindings'
    prop_field_metas['virtual_machine_interface_fat_flow_protocols'] = 'virtual-machine-interface-fat-flow-protocols'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['qos_forwarding_class_refs'] = 'virtual-machine-interface-qos-forwarding-class'
    ref_field_metas['security_group_refs'] = 'virtual-machine-interface-security-group'
    ref_field_metas['virtual_machine_interface_refs'] = 'virtual-machine-interface-sub-interface'
    ref_field_metas['virtual_machine_refs'] = 'virtual-machine-interface-virtual-machine'
    ref_field_metas['virtual_network_refs'] = 'virtual-machine-interface-virtual-network'
    ref_field_metas['routing_instance_refs'] = 'virtual-machine-interface-routing-instance'
    ref_field_metas['port_tuple_refs'] = 'port-tuple-interface'
    ref_field_metas['service_health_check_refs'] = 'service-port-health-check'
    ref_field_metas['interface_route_table_refs'] = 'virtual-machine-interface-route-table'
    ref_field_metas['physical_interface_refs'] = 'virtual-machine-interface-physical-interface'

    children_field_metas = {}

    prop_list_fields = set([u'virtual_machine_interface_fat_flow_protocols'])

    prop_list_field_has_wrappers = {}
    prop_list_field_has_wrappers['virtual_machine_interface_fat_flow_protocols'] = True

    prop_map_fields = set([u'virtual_machine_interface_bindings'])

    prop_map_field_has_wrappers = {}
    prop_map_field_has_wrappers['virtual_machine_interface_bindings'] = True

    prop_map_field_key_names = {}
    prop_map_field_key_names['virtual_machine_interface_bindings'] = 'key'

    def __init__(self, name = None, parent_obj = None, ecmp_hashing_include_fields=None, virtual_machine_interface_mac_addresses=None, virtual_machine_interface_dhcp_option_list=None, virtual_machine_interface_host_routes=None, virtual_machine_interface_allowed_address_pairs=None, vrf_assign_table=None, virtual_machine_interface_device_owner=None, virtual_machine_interface_disable_policy=False, virtual_machine_interface_properties=None, virtual_machine_interface_bindings=None, virtual_machine_interface_fat_flow_protocols=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if ecmp_hashing_include_fields is not None:
            self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
        if virtual_machine_interface_mac_addresses is not None:
            self._virtual_machine_interface_mac_addresses = virtual_machine_interface_mac_addresses
        if virtual_machine_interface_dhcp_option_list is not None:
            self._virtual_machine_interface_dhcp_option_list = virtual_machine_interface_dhcp_option_list
        if virtual_machine_interface_host_routes is not None:
            self._virtual_machine_interface_host_routes = virtual_machine_interface_host_routes
        if virtual_machine_interface_allowed_address_pairs is not None:
            self._virtual_machine_interface_allowed_address_pairs = virtual_machine_interface_allowed_address_pairs
        if vrf_assign_table is not None:
            self._vrf_assign_table = vrf_assign_table
        if virtual_machine_interface_device_owner is not None:
            self._virtual_machine_interface_device_owner = virtual_machine_interface_device_owner
        if virtual_machine_interface_disable_policy is not None:
            self._virtual_machine_interface_disable_policy = virtual_machine_interface_disable_policy
        if virtual_machine_interface_properties is not None:
            self._virtual_machine_interface_properties = virtual_machine_interface_properties
        if virtual_machine_interface_bindings is not None:
            self._virtual_machine_interface_bindings = virtual_machine_interface_bindings
        if virtual_machine_interface_fat_flow_protocols is not None:
            self._virtual_machine_interface_fat_flow_protocols = virtual_machine_interface_fat_flow_protocols
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def ecmp_hashing_include_fields(self):
        """Get ecmp-hashing-include-fields for virtual-machine-interface.
        
        :returns: EcmpHashingIncludeFields object
        
        """
        return getattr(self, '_ecmp_hashing_include_fields', None)
    #end ecmp_hashing_include_fields

    @ecmp_hashing_include_fields.setter
    def ecmp_hashing_include_fields(self, ecmp_hashing_include_fields):
        """Set ecmp-hashing-include-fields for virtual-machine-interface.
        
        :param ecmp_hashing_include_fields: EcmpHashingIncludeFields object
        
        """
        self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
    #end ecmp_hashing_include_fields

    def set_ecmp_hashing_include_fields(self, value):
        self.ecmp_hashing_include_fields = value
    #end set_ecmp_hashing_include_fields

    def get_ecmp_hashing_include_fields(self):
        return self.ecmp_hashing_include_fields
    #end get_ecmp_hashing_include_fields

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
    def virtual_machine_interface_disable_policy(self):
        """Get virtual-machine-interface-disable-policy for virtual-machine-interface.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_virtual_machine_interface_disable_policy', None)
    #end virtual_machine_interface_disable_policy

    @virtual_machine_interface_disable_policy.setter
    def virtual_machine_interface_disable_policy(self, virtual_machine_interface_disable_policy):
        """Set virtual-machine-interface-disable-policy for virtual-machine-interface.
        
        :param virtual_machine_interface_disable_policy: xsd:boolean object
        
        """
        self._virtual_machine_interface_disable_policy = virtual_machine_interface_disable_policy
    #end virtual_machine_interface_disable_policy

    def set_virtual_machine_interface_disable_policy(self, value):
        self.virtual_machine_interface_disable_policy = value
    #end set_virtual_machine_interface_disable_policy

    def get_virtual_machine_interface_disable_policy(self):
        return self.virtual_machine_interface_disable_policy
    #end get_virtual_machine_interface_disable_policy

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
    def virtual_machine_interface_bindings(self):
        """Get virtual-machine-interface-bindings for virtual-machine-interface.
        
        :returns: KeyValuePairs object
        
        """
        return getattr(self, '_virtual_machine_interface_bindings', None)
    #end virtual_machine_interface_bindings

    @virtual_machine_interface_bindings.setter
    def virtual_machine_interface_bindings(self, virtual_machine_interface_bindings):
        """Set virtual-machine-interface-bindings for virtual-machine-interface.
        
        :param virtual_machine_interface_bindings: KeyValuePairs object
        
        """
        self._virtual_machine_interface_bindings = virtual_machine_interface_bindings
    #end virtual_machine_interface_bindings

    def set_virtual_machine_interface_bindings(self, value):
        self.virtual_machine_interface_bindings = value
    #end set_virtual_machine_interface_bindings

    def get_virtual_machine_interface_bindings(self):
        return self.virtual_machine_interface_bindings
    #end get_virtual_machine_interface_bindings

    @property
    def virtual_machine_interface_fat_flow_protocols(self):
        """Get virtual-machine-interface-fat-flow-protocols for virtual-machine-interface.
        
        :returns: FatFlowProtocols object
        
        """
        return getattr(self, '_virtual_machine_interface_fat_flow_protocols', None)
    #end virtual_machine_interface_fat_flow_protocols

    @virtual_machine_interface_fat_flow_protocols.setter
    def virtual_machine_interface_fat_flow_protocols(self, virtual_machine_interface_fat_flow_protocols):
        """Set virtual-machine-interface-fat-flow-protocols for virtual-machine-interface.
        
        :param virtual_machine_interface_fat_flow_protocols: FatFlowProtocols object
        
        """
        self._virtual_machine_interface_fat_flow_protocols = virtual_machine_interface_fat_flow_protocols
    #end virtual_machine_interface_fat_flow_protocols

    def set_virtual_machine_interface_fat_flow_protocols(self, value):
        self.virtual_machine_interface_fat_flow_protocols = value
    #end set_virtual_machine_interface_fat_flow_protocols

    def get_virtual_machine_interface_fat_flow_protocols(self):
        return self.virtual_machine_interface_fat_flow_protocols
    #end get_virtual_machine_interface_fat_flow_protocols

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
    def perms2(self):
        """Get perms2 for virtual-machine-interface.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-machine-interface.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_ecmp_hashing_include_fields'):
            self._serialize_field_to_json(serialized, field_names, 'ecmp_hashing_include_fields')
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
        if hasattr(self, '_virtual_machine_interface_disable_policy'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_disable_policy')
        if hasattr(self, '_virtual_machine_interface_properties'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_properties')
        if hasattr(self, '_virtual_machine_interface_bindings'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_bindings')
        if hasattr(self, '_virtual_machine_interface_fat_flow_protocols'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_fat_flow_protocols')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        if hasattr(self, 'port_tuple_refs'):
            self._serialize_field_to_json(serialized, field_names, 'port_tuple_refs')
        if hasattr(self, 'service_health_check_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_health_check_refs')
        if hasattr(self, 'interface_route_table_refs'):
            self._serialize_field_to_json(serialized, field_names, 'interface_route_table_refs')
        if hasattr(self, 'physical_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'physical_interface_refs')
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

    def set_port_tuple(self, ref_obj):
        """Set port-tuple for virtual-machine-interface.
        
        :param ref_obj: PortTuple object
        
        """
        self.port_tuple_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.port_tuple_refs[0]['uuid'] = ref_obj.uuid

    #end set_port_tuple

    def add_port_tuple(self, ref_obj):
        """Add port-tuple to virtual-machine-interface.
        
        :param ref_obj: PortTuple object
        
        """
        refs = getattr(self, 'port_tuple_refs', [])
        if not refs:
            self.port_tuple_refs = []

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

        self.port_tuple_refs.append(ref_info)
    #end add_port_tuple

    def del_port_tuple(self, ref_obj):
        refs = self.get_port_tuple_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.port_tuple_refs.remove(ref)
                return
    #end del_port_tuple

    def set_port_tuple_list(self, ref_obj_list):
        """Set port-tuple list for virtual-machine-interface.
        
        :param ref_obj_list: list of PortTuple object
        
        """
        self.port_tuple_refs = ref_obj_list
    #end set_port_tuple_list

    def get_port_tuple_refs(self):
        """Return port-tuple list for virtual-machine-interface.
        
        :returns: list of <PortTuple>
        
        """
        return getattr(self, 'port_tuple_refs', None)
    #end get_port_tuple_refs

    def set_service_health_check(self, ref_obj):
        """Set service-health-check for virtual-machine-interface.
        
        :param ref_obj: ServiceHealthCheck object
        
        """
        self.service_health_check_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_health_check_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_health_check

    def add_service_health_check(self, ref_obj):
        """Add service-health-check to virtual-machine-interface.
        
        :param ref_obj: ServiceHealthCheck object
        
        """
        refs = getattr(self, 'service_health_check_refs', [])
        if not refs:
            self.service_health_check_refs = []

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

        self.service_health_check_refs.append(ref_info)
    #end add_service_health_check

    def del_service_health_check(self, ref_obj):
        refs = self.get_service_health_check_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.service_health_check_refs.remove(ref)
                return
    #end del_service_health_check

    def set_service_health_check_list(self, ref_obj_list):
        """Set service-health-check list for virtual-machine-interface.
        
        :param ref_obj_list: list of ServiceHealthCheck object
        
        """
        self.service_health_check_refs = ref_obj_list
    #end set_service_health_check_list

    def get_service_health_check_refs(self):
        """Return service-health-check list for virtual-machine-interface.
        
        :returns: list of <ServiceHealthCheck>
        
        """
        return getattr(self, 'service_health_check_refs', None)
    #end get_service_health_check_refs

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

    def set_physical_interface(self, ref_obj):
        """Set physical-interface for virtual-machine-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        self.physical_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.physical_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_physical_interface

    def add_physical_interface(self, ref_obj):
        """Add physical-interface to virtual-machine-interface.
        
        :param ref_obj: PhysicalInterface object
        
        """
        refs = getattr(self, 'physical_interface_refs', [])
        if not refs:
            self.physical_interface_refs = []

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

        self.physical_interface_refs.append(ref_info)
    #end add_physical_interface

    def del_physical_interface(self, ref_obj):
        refs = self.get_physical_interface_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.physical_interface_refs.remove(ref)
                return
    #end del_physical_interface

    def set_physical_interface_list(self, ref_obj_list):
        """Set physical-interface list for virtual-machine-interface.
        
        :param ref_obj_list: list of PhysicalInterface object
        
        """
        self.physical_interface_refs = ref_obj_list
    #end set_physical_interface_list

    def get_physical_interface_refs(self):
        """Return physical-interface list for virtual-machine-interface.
        
        :returns: list of <PhysicalInterface>
        
        """
        return getattr(self, 'physical_interface_refs', None)
    #end get_physical_interface_refs

    def get_virtual_machine_interface_back_refs(self):
        """Return list of all virtual-machine-interfaces using this virtual-machine-interface"""
        return getattr(self, 'virtual_machine_interface_back_refs', None)
    #end get_virtual_machine_interface_back_refs

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

    def get_bgp_as_a_service_back_refs(self):
        """Return list of all bgp-as-a-services using this virtual-machine-interface"""
        return getattr(self, 'bgp_as_a_service_back_refs', None)
    #end get_bgp_as_a_service_back_refs

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

    def get_loadbalancer_back_refs(self):
        """Return list of all loadbalancers using this virtual-machine-interface"""
        return getattr(self, 'loadbalancer_back_refs', None)
    #end get_loadbalancer_back_refs

    def dump(self):
        """Display virtual-machine-interface object in compact form."""
        print '------------ virtual-machine-interface ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P ecmp_hashing_include_fields = ', self.get_ecmp_hashing_include_fields()
        print 'P virtual_machine_interface_mac_addresses = ', self.get_virtual_machine_interface_mac_addresses()
        print 'P virtual_machine_interface_dhcp_option_list = ', self.get_virtual_machine_interface_dhcp_option_list()
        print 'P virtual_machine_interface_host_routes = ', self.get_virtual_machine_interface_host_routes()
        print 'P virtual_machine_interface_allowed_address_pairs = ', self.get_virtual_machine_interface_allowed_address_pairs()
        print 'P vrf_assign_table = ', self.get_vrf_assign_table()
        print 'P virtual_machine_interface_device_owner = ', self.get_virtual_machine_interface_device_owner()
        print 'P virtual_machine_interface_disable_policy = ', self.get_virtual_machine_interface_disable_policy()
        print 'P virtual_machine_interface_properties = ', self.get_virtual_machine_interface_properties()
        print 'P virtual_machine_interface_bindings = ', self.get_virtual_machine_interface_bindings()
        print 'P virtual_machine_interface_fat_flow_protocols = ', self.get_virtual_machine_interface_fat_flow_protocols()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF qos_forwarding_class = ', self.get_qos_forwarding_class_refs()
        print 'REF security_group = ', self.get_security_group_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF virtual_machine = ', self.get_virtual_machine_refs()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'REF routing_instance = ', self.get_routing_instance_refs()
        print 'REF port_tuple = ', self.get_port_tuple_refs()
        print 'REF service_health_check = ', self.get_service_health_check_refs()
        print 'REF interface_route_table = ', self.get_interface_route_table_refs()
        print 'REF physical_interface = ', self.get_physical_interface_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
        print 'BCK instance_ip = ', self.get_instance_ip_back_refs()
        print 'BCK subnet = ', self.get_subnet_back_refs()
        print 'BCK floating_ip = ', self.get_floating_ip_back_refs()
        print 'BCK logical_interface = ', self.get_logical_interface_back_refs()
        print 'BCK bgp_as_a_service = ', self.get_bgp_as_a_service_back_refs()
        print 'BCK customer_attachment = ', self.get_customer_attachment_back_refs()
        print 'BCK logical_router = ', self.get_logical_router_back_refs()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
        print 'BCK virtual_ip = ', self.get_virtual_ip_back_refs()
        print 'BCK loadbalancer = ', self.get_loadbalancer_back_refs()
    #end dump

#end class VirtualMachineInterface

class LoadbalancerHealthmonitor(object):
    """
    Represents loadbalancer-healthmonitor configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * loadbalancer_healthmonitor_properties
            Type: :class:`.LoadbalancerHealthmonitorType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
        * list of :class:`.LoadbalancerPool` objects
    """

    prop_fields = set([u'loadbalancer_healthmonitor_properties', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([u'loadbalancer_pool_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'loadbalancer_healthmonitor_properties': {'xsd_type': u'LoadbalancerHealthmonitorType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}
    backref_field_types['loadbalancer_pool_back_refs'] = ('loadbalancer-pool', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['loadbalancer_healthmonitor_properties'] = 'loadbalancer-healthmonitor-properties'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, loadbalancer_healthmonitor_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if loadbalancer_healthmonitor_properties is not None:
            self._loadbalancer_healthmonitor_properties = loadbalancer_healthmonitor_properties
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for loadbalancer-healthmonitor.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-healthmonitor.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
    #end dump

#end class LoadbalancerHealthmonitor

class LoadbalancerListener(object):
    """
    Represents loadbalancer-listener configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * loadbalancer_listener_properties
            Type: :class:`.LoadbalancerListenerType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.Loadbalancer` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.LoadbalancerPool` objects
    """

    prop_fields = set([u'loadbalancer_listener_properties', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['loadbalancer_refs'])
    backref_fields = set([u'loadbalancer_pool_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'loadbalancer_listener_properties': {'xsd_type': u'LoadbalancerListenerType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['loadbalancer_refs'] = ('loadbalancer', 'None', False)

    backref_field_types = {}
    backref_field_types['loadbalancer_pool_back_refs'] = ('loadbalancer-pool', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['loadbalancer_listener_properties'] = 'loadbalancer-listener-properties'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['loadbalancer_refs'] = 'loadbalancer-listener-loadbalancer'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, loadbalancer_listener_properties=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'loadbalancer-listener'
        if not name:
            name = u'default-loadbalancer-listener'
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
        if loadbalancer_listener_properties is not None:
            self._loadbalancer_listener_properties = loadbalancer_listener_properties
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (loadbalancer-listener)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of loadbalancer-listener in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of loadbalancer-listener as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of loadbalancer-listener's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of loadbalancer-listener's parent as colon delimted string."""
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
    def loadbalancer_listener_properties(self):
        """Get loadbalancer-listener-properties for loadbalancer-listener.
        
        :returns: LoadbalancerListenerType object
        
        """
        return getattr(self, '_loadbalancer_listener_properties', None)
    #end loadbalancer_listener_properties

    @loadbalancer_listener_properties.setter
    def loadbalancer_listener_properties(self, loadbalancer_listener_properties):
        """Set loadbalancer-listener-properties for loadbalancer-listener.
        
        :param loadbalancer_listener_properties: LoadbalancerListenerType object
        
        """
        self._loadbalancer_listener_properties = loadbalancer_listener_properties
    #end loadbalancer_listener_properties

    def set_loadbalancer_listener_properties(self, value):
        self.loadbalancer_listener_properties = value
    #end set_loadbalancer_listener_properties

    def get_loadbalancer_listener_properties(self):
        return self.loadbalancer_listener_properties
    #end get_loadbalancer_listener_properties

    @property
    def id_perms(self):
        """Get id-perms for loadbalancer-listener.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer-listener.
        
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
    def perms2(self):
        """Get perms2 for loadbalancer-listener.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer-listener.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for loadbalancer-listener.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer-listener.
        
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
        if hasattr(self, '_loadbalancer_listener_properties'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_listener_properties')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'loadbalancer_refs'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_refs')
        return serialized
    #end serialize_to_json

    def set_loadbalancer(self, ref_obj):
        """Set loadbalancer for loadbalancer-listener.
        
        :param ref_obj: Loadbalancer object
        
        """
        self.loadbalancer_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.loadbalancer_refs[0]['uuid'] = ref_obj.uuid

    #end set_loadbalancer

    def add_loadbalancer(self, ref_obj):
        """Add loadbalancer to loadbalancer-listener.
        
        :param ref_obj: Loadbalancer object
        
        """
        refs = getattr(self, 'loadbalancer_refs', [])
        if not refs:
            self.loadbalancer_refs = []

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

        self.loadbalancer_refs.append(ref_info)
    #end add_loadbalancer

    def del_loadbalancer(self, ref_obj):
        refs = self.get_loadbalancer_refs()
        if not refs:
            return

        for ref in refs:
            if ref['to'] == ref_obj.get_fq_name():
                self.loadbalancer_refs.remove(ref)
                return
    #end del_loadbalancer

    def set_loadbalancer_list(self, ref_obj_list):
        """Set loadbalancer list for loadbalancer-listener.
        
        :param ref_obj_list: list of Loadbalancer object
        
        """
        self.loadbalancer_refs = ref_obj_list
    #end set_loadbalancer_list

    def get_loadbalancer_refs(self):
        """Return loadbalancer list for loadbalancer-listener.
        
        :returns: list of <Loadbalancer>
        
        """
        return getattr(self, 'loadbalancer_refs', None)
    #end get_loadbalancer_refs

    def get_loadbalancer_pool_back_refs(self):
        """Return list of all loadbalancer-pools using this loadbalancer-listener"""
        return getattr(self, 'loadbalancer_pool_back_refs', None)
    #end get_loadbalancer_pool_back_refs

    def dump(self):
        """Display loadbalancer-listener object in compact form."""
        print '------------ loadbalancer-listener ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P loadbalancer_listener_properties = ', self.get_loadbalancer_listener_properties()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF loadbalancer = ', self.get_loadbalancer_refs()
        print 'BCK loadbalancer_pool = ', self.get_loadbalancer_pool_back_refs()
    #end dump

#end class LoadbalancerListener

class VirtualNetwork(object):
    """
    Represents virtual-network configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * ecmp_hashing_include_fields
            Type: :class:`.EcmpHashingIncludeFields`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_network_properties
            Type: :class:`.VirtualNetworkType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * provider_properties
            Type: :class:`.ProviderDetails`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * virtual_network_network_id
            Type: int

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * route_target_list
            Type: :class:`.RouteTargetList`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * import_route_target_list
            Type: :class:`.RouteTargetList`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * export_route_target_list
            Type: :class:`.RouteTargetList`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * router_external
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * is_shared
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * external_ipam
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * flood_unknown_unicast
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * multi_policy_service_chains_enabled
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.AccessControlList` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.FloatingIpPool` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.RoutingInstance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of :class:`.QosForwardingClass` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of (:class:`.NetworkIpam` object, :class:`.VnSubnetsType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of (:class:`.NetworkPolicy` object, :class:`.VirtualNetworkPolicyType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.RouteTable` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.InstanceIp` objects
        * list of :class:`.PhysicalRouter` objects
        * list of :class:`.LogicalRouter` objects
    """

    prop_fields = set([u'ecmp_hashing_include_fields', u'virtual_network_properties', u'provider_properties', u'virtual_network_network_id', u'route_target_list', u'import_route_target_list', u'export_route_target_list', u'router_external', u'is_shared', u'external_ipam', u'flood_unknown_unicast', u'multi_policy_service_chains_enabled', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'qos_forwarding_class_refs', u'network_ipam_refs', u'network_policy_refs', u'route_table_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs', u'instance_ip_back_refs', 'physical_router_back_refs', 'logical_router_back_refs'])
    children_fields = set([u'access_control_lists', u'floating_ip_pools', 'routing_instances'])

    prop_field_types = {
        'ecmp_hashing_include_fields': {'xsd_type': u'EcmpHashingIncludeFields', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_network_properties': {'xsd_type': u'VirtualNetworkType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'provider_properties': {'xsd_type': u'ProviderDetails', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'virtual_network_network_id': {'xsd_type': u'integer', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'route_target_list': {'xsd_type': u'RouteTargetList', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'import_route_target_list': {'xsd_type': u'RouteTargetList', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'export_route_target_list': {'xsd_type': u'RouteTargetList', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'router_external': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'is_shared': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'external_ipam': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'flood_unknown_unicast': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'multi_policy_service_chains_enabled': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['qos_forwarding_class_refs'] = ('qos-forwarding-class', 'None', False)
    ref_field_types['network_ipam_refs'] = ('network-ipam', 'VnSubnetsType', False)
    ref_field_types['network_policy_refs'] = ('network-policy', 'VirtualNetworkPolicyType', False)
    ref_field_types['route_table_refs'] = ('route-table', 'None', False)

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)
    backref_field_types['instance_ip_back_refs'] = ('instance-ip', 'None', False)
    backref_field_types['physical_router_back_refs'] = ('physical-router', 'None', False)
    backref_field_types['logical_router_back_refs'] = ('logical-router', 'None', False)

    children_field_types = {}
    children_field_types['access_control_lists'] = ('access-control-list', True)
    children_field_types['floating_ip_pools'] = ('floating-ip-pool', False)
    children_field_types['routing_instances'] = ('routing-instance', True)

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['ecmp_hashing_include_fields'] = 'ecmp-hashing-include-fields'
    prop_field_metas['virtual_network_properties'] = 'virtual-network-properties'
    prop_field_metas['provider_properties'] = 'provider-properties'
    prop_field_metas['virtual_network_network_id'] = 'virtual-network-network-id'
    prop_field_metas['route_target_list'] = 'route-target-list'
    prop_field_metas['import_route_target_list'] = 'import-route-target-list'
    prop_field_metas['export_route_target_list'] = 'export-route-target-list'
    prop_field_metas['router_external'] = 'router-external'
    prop_field_metas['is_shared'] = 'is-shared'
    prop_field_metas['external_ipam'] = 'external-ipam'
    prop_field_metas['flood_unknown_unicast'] = 'flood-unknown-unicast'
    prop_field_metas['multi_policy_service_chains_enabled'] = 'multi-policy-service-chains-enabled'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['qos_forwarding_class_refs'] = 'virtual-network-qos-forwarding-class'
    ref_field_metas['network_ipam_refs'] = 'virtual-network-network-ipam'
    ref_field_metas['network_policy_refs'] = 'virtual-network-network-policy'
    ref_field_metas['route_table_refs'] = 'virtual-network-route-table'

    children_field_metas = {}
    children_field_metas['access_control_lists'] = 'virtual-network-access-control-list'
    children_field_metas['floating_ip_pools'] = 'virtual-network-floating-ip-pool'
    children_field_metas['routing_instances'] = 'virtual-network-routing-instance'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, ecmp_hashing_include_fields=None, virtual_network_properties=None, provider_properties=None, virtual_network_network_id=None, route_target_list=None, import_route_target_list=None, export_route_target_list=None, router_external=None, is_shared=None, external_ipam=None, flood_unknown_unicast=False, multi_policy_service_chains_enabled=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if ecmp_hashing_include_fields is not None:
            self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
        if virtual_network_properties is not None:
            self._virtual_network_properties = virtual_network_properties
        if provider_properties is not None:
            self._provider_properties = provider_properties
        if virtual_network_network_id is not None:
            self._virtual_network_network_id = virtual_network_network_id
        if route_target_list is not None:
            self._route_target_list = route_target_list
        if import_route_target_list is not None:
            self._import_route_target_list = import_route_target_list
        if export_route_target_list is not None:
            self._export_route_target_list = export_route_target_list
        if router_external is not None:
            self._router_external = router_external
        if is_shared is not None:
            self._is_shared = is_shared
        if external_ipam is not None:
            self._external_ipam = external_ipam
        if flood_unknown_unicast is not None:
            self._flood_unknown_unicast = flood_unknown_unicast
        if multi_policy_service_chains_enabled is not None:
            self._multi_policy_service_chains_enabled = multi_policy_service_chains_enabled
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def ecmp_hashing_include_fields(self):
        """Get ecmp-hashing-include-fields for virtual-network.
        
        :returns: EcmpHashingIncludeFields object
        
        """
        return getattr(self, '_ecmp_hashing_include_fields', None)
    #end ecmp_hashing_include_fields

    @ecmp_hashing_include_fields.setter
    def ecmp_hashing_include_fields(self, ecmp_hashing_include_fields):
        """Set ecmp-hashing-include-fields for virtual-network.
        
        :param ecmp_hashing_include_fields: EcmpHashingIncludeFields object
        
        """
        self._ecmp_hashing_include_fields = ecmp_hashing_include_fields
    #end ecmp_hashing_include_fields

    def set_ecmp_hashing_include_fields(self, value):
        self.ecmp_hashing_include_fields = value
    #end set_ecmp_hashing_include_fields

    def get_ecmp_hashing_include_fields(self):
        return self.ecmp_hashing_include_fields
    #end get_ecmp_hashing_include_fields

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
    def provider_properties(self):
        """Get provider-properties for virtual-network.
        
        :returns: ProviderDetails object
        
        """
        return getattr(self, '_provider_properties', None)
    #end provider_properties

    @provider_properties.setter
    def provider_properties(self, provider_properties):
        """Set provider-properties for virtual-network.
        
        :param provider_properties: ProviderDetails object
        
        """
        self._provider_properties = provider_properties
    #end provider_properties

    def set_provider_properties(self, value):
        self.provider_properties = value
    #end set_provider_properties

    def get_provider_properties(self):
        return self.provider_properties
    #end get_provider_properties

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
    def import_route_target_list(self):
        """Get import-route-target-list for virtual-network.
        
        :returns: RouteTargetList object
        
        """
        return getattr(self, '_import_route_target_list', None)
    #end import_route_target_list

    @import_route_target_list.setter
    def import_route_target_list(self, import_route_target_list):
        """Set import-route-target-list for virtual-network.
        
        :param import_route_target_list: RouteTargetList object
        
        """
        self._import_route_target_list = import_route_target_list
    #end import_route_target_list

    def set_import_route_target_list(self, value):
        self.import_route_target_list = value
    #end set_import_route_target_list

    def get_import_route_target_list(self):
        return self.import_route_target_list
    #end get_import_route_target_list

    @property
    def export_route_target_list(self):
        """Get export-route-target-list for virtual-network.
        
        :returns: RouteTargetList object
        
        """
        return getattr(self, '_export_route_target_list', None)
    #end export_route_target_list

    @export_route_target_list.setter
    def export_route_target_list(self, export_route_target_list):
        """Set export-route-target-list for virtual-network.
        
        :param export_route_target_list: RouteTargetList object
        
        """
        self._export_route_target_list = export_route_target_list
    #end export_route_target_list

    def set_export_route_target_list(self, value):
        self.export_route_target_list = value
    #end set_export_route_target_list

    def get_export_route_target_list(self):
        return self.export_route_target_list
    #end get_export_route_target_list

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
    def multi_policy_service_chains_enabled(self):
        """Get multi-policy-service-chains-enabled for virtual-network.
        
        :returns: xsd:Boolean object
        
        """
        return getattr(self, '_multi_policy_service_chains_enabled', None)
    #end multi_policy_service_chains_enabled

    @multi_policy_service_chains_enabled.setter
    def multi_policy_service_chains_enabled(self, multi_policy_service_chains_enabled):
        """Set multi-policy-service-chains-enabled for virtual-network.
        
        :param multi_policy_service_chains_enabled: xsd:Boolean object
        
        """
        self._multi_policy_service_chains_enabled = multi_policy_service_chains_enabled
    #end multi_policy_service_chains_enabled

    def set_multi_policy_service_chains_enabled(self, value):
        self.multi_policy_service_chains_enabled = value
    #end set_multi_policy_service_chains_enabled

    def get_multi_policy_service_chains_enabled(self):
        return self.multi_policy_service_chains_enabled
    #end get_multi_policy_service_chains_enabled

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
    def perms2(self):
        """Get perms2 for virtual-network.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for virtual-network.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_ecmp_hashing_include_fields'):
            self._serialize_field_to_json(serialized, field_names, 'ecmp_hashing_include_fields')
        if hasattr(self, '_virtual_network_properties'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_properties')
        if hasattr(self, '_provider_properties'):
            self._serialize_field_to_json(serialized, field_names, 'provider_properties')
        if hasattr(self, '_virtual_network_network_id'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_network_network_id')
        if hasattr(self, '_route_target_list'):
            self._serialize_field_to_json(serialized, field_names, 'route_target_list')
        if hasattr(self, '_import_route_target_list'):
            self._serialize_field_to_json(serialized, field_names, 'import_route_target_list')
        if hasattr(self, '_export_route_target_list'):
            self._serialize_field_to_json(serialized, field_names, 'export_route_target_list')
        if hasattr(self, '_router_external'):
            self._serialize_field_to_json(serialized, field_names, 'router_external')
        if hasattr(self, '_is_shared'):
            self._serialize_field_to_json(serialized, field_names, 'is_shared')
        if hasattr(self, '_external_ipam'):
            self._serialize_field_to_json(serialized, field_names, 'external_ipam')
        if hasattr(self, '_flood_unknown_unicast'):
            self._serialize_field_to_json(serialized, field_names, 'flood_unknown_unicast')
        if hasattr(self, '_multi_policy_service_chains_enabled'):
            self._serialize_field_to_json(serialized, field_names, 'multi_policy_service_chains_enabled')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P ecmp_hashing_include_fields = ', self.get_ecmp_hashing_include_fields()
        print 'P virtual_network_properties = ', self.get_virtual_network_properties()
        print 'P provider_properties = ', self.get_provider_properties()
        print 'P virtual_network_network_id = ', self.get_virtual_network_network_id()
        print 'P route_target_list = ', self.get_route_target_list()
        print 'P import_route_target_list = ', self.get_import_route_target_list()
        print 'P export_route_target_list = ', self.get_export_route_target_list()
        print 'P router_external = ', self.get_router_external()
        print 'P is_shared = ', self.get_is_shared()
        print 'P external_ipam = ', self.get_external_ipam()
        print 'P flood_unknown_unicast = ', self.get_flood_unknown_unicast()
        print 'P multi_policy_service_chains_enabled = ', self.get_multi_policy_service_chains_enabled()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
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
        * quota
            Type: :class:`.QuotaType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.SecurityGroup` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualNetwork` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.QosQueue` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.QosForwardingClass` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.NetworkIpam` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.NetworkPolicy` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.BgpAsAService` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.RoutingPolicy` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.RouteAggregate` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ServiceInstance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ServiceHealthCheck` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.RouteTable` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.InterfaceRouteTable` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.LogicalRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ApiAccessList` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.LoadbalancerPool` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.LoadbalancerHealthmonitor` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualIp` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.LoadbalancerListener` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.Loadbalancer` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of (:class:`.Namespace` object, :class:`.SubnetType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.FloatingIpPool` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.FloatingIp` objects
    """

    prop_fields = set([u'quota', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'namespace_refs', u'floating_ip_pool_refs'])
    backref_fields = set([u'floating_ip_back_refs'])
    children_fields = set([u'security_groups', 'virtual_networks', u'qos_queues', u'qos_forwarding_classs', u'network_ipams', u'network_policys', 'virtual_machine_interfaces', 'bgp_as_a_services', 'routing_policys', 'route_aggregates', u'service_instances', 'service_health_checks', u'route_tables', 'interface_route_tables', 'logical_routers', u'api_access_lists', u'loadbalancer_pools', u'loadbalancer_healthmonitors', u'virtual_ips', 'loadbalancer_listeners', 'loadbalancers'])

    prop_field_types = {
        'quota': {'xsd_type': u'QuotaType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['namespace_refs'] = ('namespace', 'SubnetType', False)
    ref_field_types['floating_ip_pool_refs'] = ('floating-ip-pool', 'None', False)

    backref_field_types = {}
    backref_field_types['floating_ip_back_refs'] = ('floating-ip', 'None', False)

    children_field_types = {}
    children_field_types['security_groups'] = ('security-group', False)
    children_field_types['virtual_networks'] = ('virtual-network', False)
    children_field_types['qos_queues'] = ('qos-queue', False)
    children_field_types['qos_forwarding_classs'] = ('qos-forwarding-class', False)
    children_field_types['network_ipams'] = ('network-ipam', False)
    children_field_types['network_policys'] = ('network-policy', False)
    children_field_types['virtual_machine_interfaces'] = ('virtual-machine-interface', False)
    children_field_types['bgp_as_a_services'] = ('bgp-as-a-service', False)
    children_field_types['routing_policys'] = ('routing-policy', False)
    children_field_types['route_aggregates'] = ('route-aggregate', False)
    children_field_types['service_instances'] = ('service-instance', False)
    children_field_types['service_health_checks'] = ('service-health-check', True)
    children_field_types['route_tables'] = ('route-table', False)
    children_field_types['interface_route_tables'] = ('interface-route-table', True)
    children_field_types['logical_routers'] = ('logical-router', False)
    children_field_types['api_access_lists'] = ('api-access-list', False)
    children_field_types['loadbalancer_pools'] = ('loadbalancer-pool', False)
    children_field_types['loadbalancer_healthmonitors'] = ('loadbalancer-healthmonitor', False)
    children_field_types['virtual_ips'] = ('virtual-ip', False)
    children_field_types['loadbalancer_listeners'] = ('loadbalancer-listener', False)
    children_field_types['loadbalancers'] = ('loadbalancer', False)

    parent_types = [u'domain']

    prop_field_metas = {}
    prop_field_metas['quota'] = 'quota'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['namespace_refs'] = 'project-namespace'
    ref_field_metas['floating_ip_pool_refs'] = 'project-floating-ip-pool'

    children_field_metas = {}
    children_field_metas['security_groups'] = 'project-security-group'
    children_field_metas['virtual_networks'] = 'project-virtual-network'
    children_field_metas['qos_queues'] = 'project-qos-queue'
    children_field_metas['qos_forwarding_classs'] = 'project-qos-forwarding-class'
    children_field_metas['network_ipams'] = 'project-network-ipam'
    children_field_metas['network_policys'] = 'project-network-policy'
    children_field_metas['virtual_machine_interfaces'] = 'project-virtual-machine-interface'
    children_field_metas['bgp_as_a_services'] = 'project-bgpaas'
    children_field_metas['routing_policys'] = 'project-routing-policy'
    children_field_metas['route_aggregates'] = 'project-route-aggregate'
    children_field_metas['service_instances'] = 'project-service-instance'
    children_field_metas['service_health_checks'] = 'project-service-health-check'
    children_field_metas['route_tables'] = 'project-route-table'
    children_field_metas['interface_route_tables'] = 'project-interface-route-table'
    children_field_metas['logical_routers'] = 'project-logical-router'
    children_field_metas['api_access_lists'] = 'project-api-access-list'
    children_field_metas['loadbalancer_pools'] = 'project-loadbalancer-pool'
    children_field_metas['loadbalancer_healthmonitors'] = 'project-loadbalancer-healthmonitor'
    children_field_metas['virtual_ips'] = 'project-virtual-ip'
    children_field_metas['loadbalancer_listeners'] = 'project-loadbalancer-listener'
    children_field_metas['loadbalancers'] = 'project-loadbalancer'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, quota=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if quota is not None:
            self._quota = quota
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for project.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for project.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def get_bgp_as_a_services(self):
        return getattr(self, 'bgp_as_a_services', None)
    #end get_bgp_as_a_services

    def get_routing_policys(self):
        return getattr(self, 'routing_policys', None)
    #end get_routing_policys

    def get_route_aggregates(self):
        return getattr(self, 'route_aggregates', None)
    #end get_route_aggregates

    def get_service_instances(self):
        return getattr(self, 'service_instances', None)
    #end get_service_instances

    def get_service_health_checks(self):
        return getattr(self, 'service_health_checks', None)
    #end get_service_health_checks

    def get_route_tables(self):
        return getattr(self, 'route_tables', None)
    #end get_route_tables

    def get_interface_route_tables(self):
        return getattr(self, 'interface_route_tables', None)
    #end get_interface_route_tables

    def get_logical_routers(self):
        return getattr(self, 'logical_routers', None)
    #end get_logical_routers

    def get_api_access_lists(self):
        return getattr(self, 'api_access_lists', None)
    #end get_api_access_lists

    def get_loadbalancer_pools(self):
        return getattr(self, 'loadbalancer_pools', None)
    #end get_loadbalancer_pools

    def get_loadbalancer_healthmonitors(self):
        return getattr(self, 'loadbalancer_healthmonitors', None)
    #end get_loadbalancer_healthmonitors

    def get_virtual_ips(self):
        return getattr(self, 'virtual_ips', None)
    #end get_virtual_ips

    def get_loadbalancer_listeners(self):
        return getattr(self, 'loadbalancer_listeners', None)
    #end get_loadbalancer_listeners

    def get_loadbalancers(self):
        return getattr(self, 'loadbalancers', None)
    #end get_loadbalancers

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
        print 'P perms2 = ', self.get_perms2()
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
        print 'HAS bgp_as_a_service = ', self.get_bgp_as_a_services()
        print 'HAS routing_policy = ', self.get_routing_policys()
        print 'HAS route_aggregate = ', self.get_route_aggregates()
        print 'HAS service_instance = ', self.get_service_instances()
        print 'HAS service_health_check = ', self.get_service_health_checks()
        print 'HAS route_table = ', self.get_route_tables()
        print 'HAS interface_route_table = ', self.get_interface_route_tables()
        print 'HAS logical_router = ', self.get_logical_routers()
        print 'HAS api_access_list = ', self.get_api_access_lists()
        print 'HAS loadbalancer_pool = ', self.get_loadbalancer_pools()
        print 'HAS loadbalancer_healthmonitor = ', self.get_loadbalancer_healthmonitors()
        print 'HAS virtual_ip = ', self.get_virtual_ips()
        print 'HAS loadbalancer_listener = ', self.get_loadbalancer_listeners()
        print 'HAS loadbalancer = ', self.get_loadbalancers()
        print 'BCK floating_ip = ', self.get_floating_ip_back_refs()
    #end dump

#end class Project

class QosForwardingClass(object):
    """
    Represents qos-forwarding-class configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * dscp
            Type: int

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * trusted
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.QosQueue` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualNetwork` objects
        * list of :class:`.VirtualMachineInterface` objects
    """

    prop_fields = set([u'dscp', u'trusted', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'qos_queue_refs'])
    backref_fields = set(['virtual_network_back_refs', 'virtual_machine_interface_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'dscp': {'xsd_type': u'integer', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'trusted': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['qos_queue_refs'] = ('qos-queue', 'None', False)

    backref_field_types = {}
    backref_field_types['virtual_network_back_refs'] = ('virtual-network', 'None', False)
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['dscp'] = 'dscp'
    prop_field_metas['trusted'] = 'trusted'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['qos_queue_refs'] = 'qos-forwarding-class-qos-queue'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, dscp=None, trusted=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if dscp is not None:
            self._dscp = dscp
        if trusted is not None:
            self._trusted = trusted
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for qos-forwarding-class.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for qos-forwarding-class.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF qos_queue = ', self.get_qos_queue_refs()
        print 'BCK virtual_network = ', self.get_virtual_network_back_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
    #end dump

#end class QosForwardingClass

class Loadbalancer(object):
    """
    Represents loadbalancer configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * loadbalancer_properties
            Type: :class:`.LoadbalancerType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * loadbalancer_provider
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.ServiceInstance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.LoadbalancerListener` objects
    """

    prop_fields = set([u'loadbalancer_properties', u'loadbalancer_provider', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_instance_refs', 'virtual_machine_interface_refs'])
    backref_fields = set(['loadbalancer_listener_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'loadbalancer_properties': {'xsd_type': u'LoadbalancerType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'loadbalancer_provider': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_instance_refs'] = ('service-instance', 'None', False)
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)

    backref_field_types = {}
    backref_field_types['loadbalancer_listener_back_refs'] = ('loadbalancer-listener', 'None', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['loadbalancer_properties'] = 'loadbalancer-properties'
    prop_field_metas['loadbalancer_provider'] = 'loadbalancer-provider'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_instance_refs'] = 'loadbalancer-service-instance'
    ref_field_metas['virtual_machine_interface_refs'] = 'loadbalancer-virtual-machine-interface'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, loadbalancer_properties=None, loadbalancer_provider=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'loadbalancer'
        if not name:
            name = u'default-loadbalancer'
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
        if loadbalancer_properties is not None:
            self._loadbalancer_properties = loadbalancer_properties
        if loadbalancer_provider is not None:
            self._loadbalancer_provider = loadbalancer_provider
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (loadbalancer)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of loadbalancer in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of loadbalancer as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of loadbalancer's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of loadbalancer's parent as colon delimted string."""
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
    def loadbalancer_properties(self):
        """Get loadbalancer-properties for loadbalancer.
        
        :returns: LoadbalancerType object
        
        """
        return getattr(self, '_loadbalancer_properties', None)
    #end loadbalancer_properties

    @loadbalancer_properties.setter
    def loadbalancer_properties(self, loadbalancer_properties):
        """Set loadbalancer-properties for loadbalancer.
        
        :param loadbalancer_properties: LoadbalancerType object
        
        """
        self._loadbalancer_properties = loadbalancer_properties
    #end loadbalancer_properties

    def set_loadbalancer_properties(self, value):
        self.loadbalancer_properties = value
    #end set_loadbalancer_properties

    def get_loadbalancer_properties(self):
        return self.loadbalancer_properties
    #end get_loadbalancer_properties

    @property
    def loadbalancer_provider(self):
        """Get loadbalancer-provider for loadbalancer.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_loadbalancer_provider', None)
    #end loadbalancer_provider

    @loadbalancer_provider.setter
    def loadbalancer_provider(self, loadbalancer_provider):
        """Set loadbalancer-provider for loadbalancer.
        
        :param loadbalancer_provider: xsd:string object
        
        """
        self._loadbalancer_provider = loadbalancer_provider
    #end loadbalancer_provider

    def set_loadbalancer_provider(self, value):
        self.loadbalancer_provider = value
    #end set_loadbalancer_provider

    def get_loadbalancer_provider(self):
        return self.loadbalancer_provider
    #end get_loadbalancer_provider

    @property
    def id_perms(self):
        """Get id-perms for loadbalancer.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for loadbalancer.
        
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
    def perms2(self):
        """Get perms2 for loadbalancer.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for loadbalancer.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for loadbalancer.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for loadbalancer.
        
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
        if hasattr(self, '_loadbalancer_properties'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_properties')
        if hasattr(self, '_loadbalancer_provider'):
            self._serialize_field_to_json(serialized, field_names, 'loadbalancer_provider')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        if hasattr(self, 'virtual_machine_interface_refs'):
            self._serialize_field_to_json(serialized, field_names, 'virtual_machine_interface_refs')
        return serialized
    #end serialize_to_json

    def set_service_instance(self, ref_obj):
        """Set service-instance for loadbalancer.
        
        :param ref_obj: ServiceInstance object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj):
        """Add service-instance to loadbalancer.
        
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
        """Set service-instance list for loadbalancer.
        
        :param ref_obj_list: list of ServiceInstance object
        
        """
        self.service_instance_refs = ref_obj_list
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for loadbalancer.
        
        :returns: list of <ServiceInstance>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

    def set_virtual_machine_interface(self, ref_obj):
        """Set virtual-machine-interface for loadbalancer.
        
        :param ref_obj: VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.virtual_machine_interface_refs[0]['uuid'] = ref_obj.uuid

    #end set_virtual_machine_interface

    def add_virtual_machine_interface(self, ref_obj):
        """Add virtual-machine-interface to loadbalancer.
        
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
        """Set virtual-machine-interface list for loadbalancer.
        
        :param ref_obj_list: list of VirtualMachineInterface object
        
        """
        self.virtual_machine_interface_refs = ref_obj_list
    #end set_virtual_machine_interface_list

    def get_virtual_machine_interface_refs(self):
        """Return virtual-machine-interface list for loadbalancer.
        
        :returns: list of <VirtualMachineInterface>
        
        """
        return getattr(self, 'virtual_machine_interface_refs', None)
    #end get_virtual_machine_interface_refs

    def get_loadbalancer_listener_back_refs(self):
        """Return list of all loadbalancer-listeners using this loadbalancer"""
        return getattr(self, 'loadbalancer_listener_back_refs', None)
    #end get_loadbalancer_listener_back_refs

    def dump(self):
        """Display loadbalancer object in compact form."""
        print '------------ loadbalancer ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P loadbalancer_properties = ', self.get_loadbalancer_properties()
        print 'P loadbalancer_provider = ', self.get_loadbalancer_provider()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'BCK loadbalancer_listener = ', self.get_loadbalancer_listener_back_refs()
    #end dump

#end class Loadbalancer

class DatabaseNode(object):
    """
    Represents database-node configuration representation.

    Child of:
        :class:`.GlobalSystemConfig` object OR

    Properties:
        * database_node_ip_address
            Type: string, *one-of* []

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:

    Referred by:
    """

    prop_fields = set([u'database_node_ip_address', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'database_node_ip_address': {'xsd_type': u'string', 'restrictions': [], 'simple_type': u'IpAddressType', 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'global-system-config']

    prop_field_metas = {}
    prop_field_metas['database_node_ip_address'] = 'database-node-ip-address'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, database_node_ip_address=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if database_node_ip_address is not None:
            self._database_node_ip_address = database_node_ip_address
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for database-node.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for database-node.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        return serialized
    #end serialize_to_json

    def dump(self):
        """Display database-node object in compact form."""
        print '------------ database-node ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P database_node_ip_address = ', self.get_database_node_ip_address()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
    #end dump

#end class DatabaseNode

class RoutingInstance(object):
    """
    Represents routing-instance configuration representation.

    Child of:
        :class:`.VirtualNetwork` object OR

    Properties:
        * service_chain_information
            Type: :class:`.ServiceChainInfo`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * ipv6_service_chain_information
            Type: :class:`.ServiceChainInfo`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * routing_instance_is_default
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * routing_instance_has_pnf
            Type: bool

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * static_route_entries
            Type: :class:`.StaticRouteEntriesType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * default_ce_protocol
            Type: :class:`.DefaultProtocolType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:
        * list of :class:`.BgpRouter` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    References to:
        * list of (:class:`.RoutingInstance` object, :class:`.ConnectionType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of (:class:`.RouteTarget` object, :class:`.InstanceTargetType` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualMachineInterface` objects
        * list of :class:`.RouteAggregate` objects
        * list of :class:`.RoutingPolicy` objects
        * list of :class:`.RoutingInstance` objects
    """

    prop_fields = set([u'service_chain_information', u'ipv6_service_chain_information', u'routing_instance_is_default', u'routing_instance_has_pnf', u'static_route_entries', u'default_ce_protocol', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['routing_instance_refs', 'route_target_refs'])
    backref_fields = set(['virtual_machine_interface_back_refs', 'route_aggregate_back_refs', 'routing_policy_back_refs', 'routing_instance_back_refs'])
    children_fields = set(['bgp_routers'])

    prop_field_types = {
        'service_chain_information': {'xsd_type': u'ServiceChainInfo', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'ipv6_service_chain_information': {'xsd_type': u'ServiceChainInfo', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'routing_instance_is_default': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'routing_instance_has_pnf': {'xsd_type': u'boolean', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'static_route_entries': {'xsd_type': u'StaticRouteEntriesType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'default_ce_protocol': {'xsd_type': u'DefaultProtocolType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['routing_instance_refs'] = ('routing-instance', 'ConnectionType', False)
    ref_field_types['route_target_refs'] = ('route-target', 'InstanceTargetType', False)

    backref_field_types = {}
    backref_field_types['virtual_machine_interface_back_refs'] = ('virtual-machine-interface', 'PolicyBasedForwardingRuleType', False)
    backref_field_types['route_aggregate_back_refs'] = ('route-aggregate', 'None', False)
    backref_field_types['routing_policy_back_refs'] = ('routing-policy', 'RoutingPolicyType', False)
    backref_field_types['routing_instance_back_refs'] = ('routing-instance', 'ConnectionType', False)

    children_field_types = {}
    children_field_types['bgp_routers'] = ('bgp-router', False)

    parent_types = ['virtual-network']

    prop_field_metas = {}
    prop_field_metas['service_chain_information'] = 'service-chain-information'
    prop_field_metas['ipv6_service_chain_information'] = 'ipv6-service-chain-information'
    prop_field_metas['routing_instance_is_default'] = 'routing-instance-is-default'
    prop_field_metas['routing_instance_has_pnf'] = 'routing-instance-has-pnf'
    prop_field_metas['static_route_entries'] = 'static-route-entries'
    prop_field_metas['default_ce_protocol'] = 'default-ce-protocol'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['routing_instance_refs'] = 'connection'
    ref_field_metas['route_target_refs'] = 'instance-target'

    children_field_metas = {}
    children_field_metas['bgp_routers'] = 'instance-bgp-router'

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, service_chain_information=None, ipv6_service_chain_information=None, routing_instance_is_default=False, routing_instance_has_pnf=False, static_route_entries=None, default_ce_protocol=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
            self.fq_name = [u'default-domain', u'default-project', 'default-virtual-network']
            self.fq_name.append(name)


        # property fields
        if service_chain_information is not None:
            self._service_chain_information = service_chain_information
        if ipv6_service_chain_information is not None:
            self._ipv6_service_chain_information = ipv6_service_chain_information
        if routing_instance_is_default is not None:
            self._routing_instance_is_default = routing_instance_is_default
        if routing_instance_has_pnf is not None:
            self._routing_instance_has_pnf = routing_instance_has_pnf
        if static_route_entries is not None:
            self._static_route_entries = static_route_entries
        if default_ce_protocol is not None:
            self._default_ce_protocol = default_ce_protocol
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def ipv6_service_chain_information(self):
        """Get ipv6-service-chain-information for routing-instance.
        
        :returns: ServiceChainInfo object
        
        """
        return getattr(self, '_ipv6_service_chain_information', None)
    #end ipv6_service_chain_information

    @ipv6_service_chain_information.setter
    def ipv6_service_chain_information(self, ipv6_service_chain_information):
        """Set ipv6-service-chain-information for routing-instance.
        
        :param ipv6_service_chain_information: ServiceChainInfo object
        
        """
        self._ipv6_service_chain_information = ipv6_service_chain_information
    #end ipv6_service_chain_information

    def set_ipv6_service_chain_information(self, value):
        self.ipv6_service_chain_information = value
    #end set_ipv6_service_chain_information

    def get_ipv6_service_chain_information(self):
        return self.ipv6_service_chain_information
    #end get_ipv6_service_chain_information

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
    def routing_instance_has_pnf(self):
        """Get routing-instance-has-pnf for routing-instance.
        
        :returns: xsd:boolean object
        
        """
        return getattr(self, '_routing_instance_has_pnf', None)
    #end routing_instance_has_pnf

    @routing_instance_has_pnf.setter
    def routing_instance_has_pnf(self, routing_instance_has_pnf):
        """Set routing-instance-has-pnf for routing-instance.
        
        :param routing_instance_has_pnf: xsd:boolean object
        
        """
        self._routing_instance_has_pnf = routing_instance_has_pnf
    #end routing_instance_has_pnf

    def set_routing_instance_has_pnf(self, value):
        self.routing_instance_has_pnf = value
    #end set_routing_instance_has_pnf

    def get_routing_instance_has_pnf(self):
        return self.routing_instance_has_pnf
    #end get_routing_instance_has_pnf

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
    def perms2(self):
        """Get perms2 for routing-instance.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for routing-instance.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_ipv6_service_chain_information'):
            self._serialize_field_to_json(serialized, field_names, 'ipv6_service_chain_information')
        if hasattr(self, '_routing_instance_is_default'):
            self._serialize_field_to_json(serialized, field_names, 'routing_instance_is_default')
        if hasattr(self, '_routing_instance_has_pnf'):
            self._serialize_field_to_json(serialized, field_names, 'routing_instance_has_pnf')
        if hasattr(self, '_static_route_entries'):
            self._serialize_field_to_json(serialized, field_names, 'static_route_entries')
        if hasattr(self, '_default_ce_protocol'):
            self._serialize_field_to_json(serialized, field_names, 'default_ce_protocol')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def get_route_aggregate_back_refs(self):
        """Return list of all route-aggregates using this routing-instance"""
        return getattr(self, 'route_aggregate_back_refs', None)
    #end get_route_aggregate_back_refs

    def get_routing_policy_back_refs(self):
        """Return list of all routing-policys using this routing-instance"""
        return getattr(self, 'routing_policy_back_refs', None)
    #end get_routing_policy_back_refs

    def get_routing_instance_back_refs(self):
        """Return list of all routing-instances using this routing-instance"""
        return getattr(self, 'routing_instance_back_refs', None)
    #end get_routing_instance_back_refs

    def dump(self):
        """Display routing-instance object in compact form."""
        print '------------ routing-instance ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P service_chain_information = ', self.get_service_chain_information()
        print 'P ipv6_service_chain_information = ', self.get_ipv6_service_chain_information()
        print 'P routing_instance_is_default = ', self.get_routing_instance_is_default()
        print 'P routing_instance_has_pnf = ', self.get_routing_instance_has_pnf()
        print 'P static_route_entries = ', self.get_static_route_entries()
        print 'P default_ce_protocol = ', self.get_default_ce_protocol()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'HAS bgp_router = ', self.get_bgp_routers()
        print 'REF routing_instance = ', self.get_routing_instance_refs()
        print 'REF route_target = ', self.get_route_target_refs()
        print 'BCK virtual_machine_interface = ', self.get_virtual_machine_interface_back_refs()
        print 'BCK route_aggregate = ', self.get_route_aggregate_back_refs()
        print 'BCK routing_policy = ', self.get_routing_policy_back_refs()
        print 'BCK routing_instance = ', self.get_routing_instance_back_refs()
    #end dump

#end class RoutingInstance

class NetworkIpam(object):
    """
    Represents network-ipam configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * network_ipam_mgmt
            Type: :class:`.IpamType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualDns` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
        * list of :class:`.VirtualNetwork` objects
    """

    prop_fields = set([u'network_ipam_mgmt', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'virtual_DNS_refs'])
    backref_fields = set(['virtual_network_back_refs'])
    children_fields = set([])

    prop_field_types = {
        'network_ipam_mgmt': {'xsd_type': u'IpamType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_DNS_refs'] = ('virtual-DNS', 'None', False)

    backref_field_types = {}
    backref_field_types['virtual_network_back_refs'] = ('virtual-network', 'VnSubnetsType', False)

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['network_ipam_mgmt'] = 'network-ipam-mgmt'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_DNS_refs'] = 'network-ipam-virtual-DNS'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, network_ipam_mgmt=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if network_ipam_mgmt is not None:
            self._network_ipam_mgmt = network_ipam_mgmt
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def perms2(self):
        """Get perms2 for network-ipam.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for network-ipam.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_DNS = ', self.get_virtual_DNS_refs()
        print 'BCK virtual_network = ', self.get_virtual_network_back_refs()
    #end dump

#end class NetworkIpam

class RouteAggregate(object):
    """
    Represents route-aggregate configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * aggregate_route_entries
            Type: :class:`.RouteListType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * aggregate_route_nexthop
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of (:class:`.ServiceInstance` object, :class:`.ServiceInterfaceTag` attribute)
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.RoutingInstance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'aggregate_route_entries', u'aggregate_route_nexthop', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set([u'service_instance_refs', 'routing_instance_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'aggregate_route_entries': {'xsd_type': u'RouteListType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'aggregate_route_nexthop': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['service_instance_refs'] = ('service-instance', 'ServiceInterfaceTag', False)
    ref_field_types['routing_instance_refs'] = ('routing-instance', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['aggregate_route_entries'] = 'aggregate-route-entries'
    prop_field_metas['aggregate_route_nexthop'] = 'aggregate-route-nexthop'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['service_instance_refs'] = 'route-aggregate-service-instance'
    ref_field_metas['routing_instance_refs'] = 'route-aggregate-routing-instance'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, aggregate_route_entries=None, aggregate_route_nexthop=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
        # type-independent fields
        self._type = 'route-aggregate'
        if not name:
            name = u'default-route-aggregate'
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
        if aggregate_route_entries is not None:
            self._aggregate_route_entries = aggregate_route_entries
        if aggregate_route_nexthop is not None:
            self._aggregate_route_nexthop = aggregate_route_nexthop
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
            self._display_name = display_name
    #end __init__

    def get_type(self):
        """Return object type (route-aggregate)."""
        return self._type
    #end get_type

    def get_fq_name(self):
        """Return FQN of route-aggregate in list form."""
        return self.fq_name
    #end get_fq_name

    def get_fq_name_str(self):
        """Return FQN of route-aggregate as colon delimited string."""
        return ':'.join(self.fq_name)
    #end get_fq_name_str

    @property
    def parent_name(self):
        return self.fq_name[:-1][-1]
    #end parent_name

    def get_parent_fq_name(self):
        """Return FQN of route-aggregate's parent in list form."""
        if not hasattr(self, 'parent_type'):
            # child of config-root
            return None

        return self.fq_name[:-1]
    #end get_parent_fq_name

    def get_parent_fq_name_str(self):
        """Return FQN of route-aggregate's parent as colon delimted string."""
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
    def aggregate_route_entries(self):
        """Get aggregate-route-entries for route-aggregate.
        
        :returns: RouteListType object
        
        """
        return getattr(self, '_aggregate_route_entries', None)
    #end aggregate_route_entries

    @aggregate_route_entries.setter
    def aggregate_route_entries(self, aggregate_route_entries):
        """Set aggregate-route-entries for route-aggregate.
        
        :param aggregate_route_entries: RouteListType object
        
        """
        self._aggregate_route_entries = aggregate_route_entries
    #end aggregate_route_entries

    def set_aggregate_route_entries(self, value):
        self.aggregate_route_entries = value
    #end set_aggregate_route_entries

    def get_aggregate_route_entries(self):
        return self.aggregate_route_entries
    #end get_aggregate_route_entries

    @property
    def aggregate_route_nexthop(self):
        """Get aggregate-route-nexthop for route-aggregate.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_aggregate_route_nexthop', None)
    #end aggregate_route_nexthop

    @aggregate_route_nexthop.setter
    def aggregate_route_nexthop(self, aggregate_route_nexthop):
        """Set aggregate-route-nexthop for route-aggregate.
        
        :param aggregate_route_nexthop: xsd:string object
        
        """
        self._aggregate_route_nexthop = aggregate_route_nexthop
    #end aggregate_route_nexthop

    def set_aggregate_route_nexthop(self, value):
        self.aggregate_route_nexthop = value
    #end set_aggregate_route_nexthop

    def get_aggregate_route_nexthop(self):
        return self.aggregate_route_nexthop
    #end get_aggregate_route_nexthop

    @property
    def id_perms(self):
        """Get id-perms for route-aggregate.
        
        :returns: IdPermsType object
        
        """
        return getattr(self, '_id_perms', None)
    #end id_perms

    @id_perms.setter
    def id_perms(self, id_perms):
        """Set id-perms for route-aggregate.
        
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
    def perms2(self):
        """Get perms2 for route-aggregate.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for route-aggregate.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

    @property
    def display_name(self):
        """Get display-name for route-aggregate.
        
        :returns: xsd:string object
        
        """
        return getattr(self, '_display_name', None)
    #end display_name

    @display_name.setter
    def display_name(self, display_name):
        """Set display-name for route-aggregate.
        
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
        if hasattr(self, '_aggregate_route_entries'):
            self._serialize_field_to_json(serialized, field_names, 'aggregate_route_entries')
        if hasattr(self, '_aggregate_route_nexthop'):
            self._serialize_field_to_json(serialized, field_names, 'aggregate_route_nexthop')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
        if hasattr(self, '_display_name'):
            self._serialize_field_to_json(serialized, field_names, 'display_name')

        # serialize reference fields
        if hasattr(self, 'service_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'service_instance_refs')
        if hasattr(self, 'routing_instance_refs'):
            self._serialize_field_to_json(serialized, field_names, 'routing_instance_refs')
        return serialized
    #end serialize_to_json

    def set_service_instance(self, ref_obj, ref_data):
        """Set service-instance for route-aggregate.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        self.service_instance_refs = [{'to':ref_obj.get_fq_name(), 'attr':ref_data}]
        if ref_obj.uuid:
            self.service_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_service_instance

    def add_service_instance(self, ref_obj, ref_data):
        """Add service-instance to route-aggregate.
        
        :param ref_obj: ServiceInstance object
        :param ref_data: ServiceInterfaceTag object
        
        """
        refs = getattr(self, 'service_instance_refs', [])
        if not refs:
            self.service_instance_refs = []

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

    def set_service_instance_list(self, ref_obj_list, ref_data_list):
        """Set service-instance list for route-aggregate.
        
        :param ref_obj_list: list of ServiceInstance object
        :param ref_data_list: list of ServiceInterfaceTag object
        
        """
        self.service_instance_refs = [{'to':ref_obj_list[i], 'attr':ref_data_list[i]} for i in range(len(ref_obj_list))]
    #end set_service_instance_list

    def get_service_instance_refs(self):
        """Return service-instance list for route-aggregate.
        
        :returns: list of tuple <ServiceInstance, ServiceInterfaceTag>
        
        """
        return getattr(self, 'service_instance_refs', None)
    #end get_service_instance_refs

    def set_routing_instance(self, ref_obj):
        """Set routing-instance for route-aggregate.
        
        :param ref_obj: RoutingInstance object
        
        """
        self.routing_instance_refs = [{'to':ref_obj.get_fq_name()}]
        if ref_obj.uuid:
            self.routing_instance_refs[0]['uuid'] = ref_obj.uuid

    #end set_routing_instance

    def add_routing_instance(self, ref_obj):
        """Add routing-instance to route-aggregate.
        
        :param ref_obj: RoutingInstance object
        
        """
        refs = getattr(self, 'routing_instance_refs', [])
        if not refs:
            self.routing_instance_refs = []

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

    def set_routing_instance_list(self, ref_obj_list):
        """Set routing-instance list for route-aggregate.
        
        :param ref_obj_list: list of RoutingInstance object
        
        """
        self.routing_instance_refs = ref_obj_list
    #end set_routing_instance_list

    def get_routing_instance_refs(self):
        """Return routing-instance list for route-aggregate.
        
        :returns: list of <RoutingInstance>
        
        """
        return getattr(self, 'routing_instance_refs', None)
    #end get_routing_instance_refs

    def dump(self):
        """Display route-aggregate object in compact form."""
        print '------------ route-aggregate ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P aggregate_route_entries = ', self.get_aggregate_route_entries()
        print 'P aggregate_route_nexthop = ', self.get_aggregate_route_nexthop()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF service_instance = ', self.get_service_instance_refs()
        print 'REF routing_instance = ', self.get_routing_instance_refs()
    #end dump

#end class RouteAggregate

class LogicalRouter(object):
    """
    Represents logical-router configuration representation.

    Child of:
        :class:`.Project` object OR

    Properties:
        * configured_route_target_list
            Type: :class:`.RouteTargetList`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * id_perms
            Type: :class:`.IdPermsType`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * perms2
            Type: :class:`.PermType2`

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * display_name
            Type: string

            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Children:

    References to:
        * list of :class:`.VirtualMachineInterface` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.RouteTarget` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.VirtualNetwork` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:

        * list of :class:`.ServiceInstance` objects
            Created By: User (optional)

            Operations Allowed: CRUD

            Description:


    Referred by:
    """

    prop_fields = set([u'configured_route_target_list', u'id_perms', u'perms2', u'display_name'])
    ref_fields = set(['virtual_machine_interface_refs', 'route_target_refs', 'virtual_network_refs', u'service_instance_refs'])
    backref_fields = set([])
    children_fields = set([])

    prop_field_types = {
        'configured_route_target_list': {'xsd_type': u'RouteTargetList', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'id_perms': {'xsd_type': u'IdPermsType', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'perms2': {'xsd_type': u'PermType2', 'restrictions': None, 'simple_type': None, 'is_complex': True},
        'display_name': {'xsd_type': u'string', 'restrictions': None, 'simple_type': None, 'is_complex': False}
    }


    ref_field_types = {}
    ref_field_types['virtual_machine_interface_refs'] = ('virtual-machine-interface', 'None', False)
    ref_field_types['route_target_refs'] = ('route-target', 'None', False)
    ref_field_types['virtual_network_refs'] = ('virtual-network', 'None', False)
    ref_field_types['service_instance_refs'] = ('service-instance', 'None', False)

    backref_field_types = {}

    children_field_types = {}

    parent_types = [u'project']

    prop_field_metas = {}
    prop_field_metas['configured_route_target_list'] = 'configured-route-target-list'
    prop_field_metas['id_perms'] = 'id-perms'
    prop_field_metas['perms2'] = 'perms2'
    prop_field_metas['display_name'] = 'display-name'

    ref_field_metas = {}
    ref_field_metas['virtual_machine_interface_refs'] = 'logical-router-interface'
    ref_field_metas['route_target_refs'] = 'logical-router-target'
    ref_field_metas['virtual_network_refs'] = 'logical-router-gateway'
    ref_field_metas['service_instance_refs'] = 'logical-router-service-instance'

    children_field_metas = {}

    prop_list_fields = set([])

    prop_list_field_has_wrappers = {}

    prop_map_fields = set([])

    prop_map_field_has_wrappers = {}

    prop_map_field_key_names = {}

    def __init__(self, name = None, parent_obj = None, configured_route_target_list=None, id_perms=None, perms2=None, display_name=None, *args, **kwargs):
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
        if configured_route_target_list is not None:
            self._configured_route_target_list = configured_route_target_list
        if id_perms is not None:
            self._id_perms = id_perms
        if perms2 is not None:
            self._perms2 = perms2
        if display_name is not None:
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
    def configured_route_target_list(self):
        """Get configured-route-target-list for logical-router.
        
        :returns: RouteTargetList object
        
        """
        return getattr(self, '_configured_route_target_list', None)
    #end configured_route_target_list

    @configured_route_target_list.setter
    def configured_route_target_list(self, configured_route_target_list):
        """Set configured-route-target-list for logical-router.
        
        :param configured_route_target_list: RouteTargetList object
        
        """
        self._configured_route_target_list = configured_route_target_list
    #end configured_route_target_list

    def set_configured_route_target_list(self, value):
        self.configured_route_target_list = value
    #end set_configured_route_target_list

    def get_configured_route_target_list(self):
        return self.configured_route_target_list
    #end get_configured_route_target_list

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
    def perms2(self):
        """Get perms2 for logical-router.
        
        :returns: PermType2 object
        
        """
        return getattr(self, '_perms2', None)
    #end perms2

    @perms2.setter
    def perms2(self, perms2):
        """Set perms2 for logical-router.
        
        :param perms2: PermType2 object
        
        """
        self._perms2 = perms2
    #end perms2

    def set_perms2(self, value):
        self.perms2 = value
    #end set_perms2

    def get_perms2(self):
        return self.perms2
    #end get_perms2

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
        if hasattr(self, '_configured_route_target_list'):
            self._serialize_field_to_json(serialized, field_names, 'configured_route_target_list')
        if hasattr(self, '_id_perms'):
            self._serialize_field_to_json(serialized, field_names, 'id_perms')
        if hasattr(self, '_perms2'):
            self._serialize_field_to_json(serialized, field_names, 'perms2')
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

    def dump(self):
        """Display logical-router object in compact form."""
        print '------------ logical-router ------------'
        print 'Name = ', self.get_fq_name()
        print 'Uuid = ', self.uuid
        if hasattr(self, 'parent_type'): # non config-root children
            print 'Parent Type = ', self.parent_type
        print 'P configured_route_target_list = ', self.get_configured_route_target_list()
        print 'P id_perms = ', self.get_id_perms()
        print 'P perms2 = ', self.get_perms2()
        print 'P display_name = ', self.get_display_name()
        print 'REF virtual_machine_interface = ', self.get_virtual_machine_interface_refs()
        print 'REF route_target = ', self.get_route_target_refs()
        print 'REF virtual_network = ', self.get_virtual_network_refs()
        print 'REF service_instance = ', self.get_service_instance_refs()
    #end dump

#end class LogicalRouter

