
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

import abc

class ConnectionDriverBase(object):
    """
    This class provides type specific methods to create,
    read, update, delete and list objects from the server
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        pass
    #end __init__
    def domain_create(self, obj):
        """Create new domain.
        
        :param obj: :class:`.Domain` object
        
        """
        raise NotImplementedError, 'domain_create is %s\'s responsibility' % (str(type (self)))
    #end domain_create

    def domain_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return domain information.
        
        :param fq_name: Fully qualified name of domain
        :param fq_name_str: Fully qualified name string of domain
        :param id: UUID of domain
        :param ifmap_id: IFMAP id of domain
        :returns: :class:`.Domain` object
        
        """
        raise NotImplementedError, 'domain_read is %s\'s responsibility' % (str(type (self)))
    #end domain_read

    def domain_update(self, obj):
        """Update domain.
        
        :param obj: :class:`.Domain` object
        
        """
        raise NotImplementedError, 'domain_update is %s\'s responsibility' % (str(type (self)))
    #end domain_update

    def domains_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all domains.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Domain` objects
        
        """
        raise NotImplementedError, 'domains_list is %s\'s responsibility' % (str(type (self)))
    #end domains_list

    def domain_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete domain from the system.
        
        :param fq_name: Fully qualified name of domain
        :param id: UUID of domain
        :param ifmap_id: IFMAP id of domain
        
        """
        raise NotImplementedError, 'domain_delete is %s\'s responsibility' % (str(type (self)))
    #end domain_delete

    def get_default_domain_id(self):
        """Return UUID of default domain."""
        raise NotImplementedError, 'get_default_domain_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_domain_delete

    def global_vrouter_config_create(self, obj):
        """Create new global-vrouter-config.
        
        :param obj: :class:`.GlobalVrouterConfig` object
        
        """
        raise NotImplementedError, 'global_vrouter_config_create is %s\'s responsibility' % (str(type (self)))
    #end global_vrouter_config_create

    def global_vrouter_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return global-vrouter-config information.
        
        :param fq_name: Fully qualified name of global-vrouter-config
        :param fq_name_str: Fully qualified name string of global-vrouter-config
        :param id: UUID of global-vrouter-config
        :param ifmap_id: IFMAP id of global-vrouter-config
        :returns: :class:`.GlobalVrouterConfig` object
        
        """
        raise NotImplementedError, 'global_vrouter_config_read is %s\'s responsibility' % (str(type (self)))
    #end global_vrouter_config_read

    def global_vrouter_config_update(self, obj):
        """Update global-vrouter-config.
        
        :param obj: :class:`.GlobalVrouterConfig` object
        
        """
        raise NotImplementedError, 'global_vrouter_config_update is %s\'s responsibility' % (str(type (self)))
    #end global_vrouter_config_update

    def global_vrouter_configs_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all global-vrouter-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalVrouterConfig` objects
        
        """
        raise NotImplementedError, 'global_vrouter_configs_list is %s\'s responsibility' % (str(type (self)))
    #end global_vrouter_configs_list

    def global_vrouter_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-vrouter-config from the system.
        
        :param fq_name: Fully qualified name of global-vrouter-config
        :param id: UUID of global-vrouter-config
        :param ifmap_id: IFMAP id of global-vrouter-config
        
        """
        raise NotImplementedError, 'global_vrouter_config_delete is %s\'s responsibility' % (str(type (self)))
    #end global_vrouter_config_delete

    def get_default_global_vrouter_config_id(self):
        """Return UUID of default global-vrouter-config."""
        raise NotImplementedError, 'get_default_global_vrouter_config_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_global_vrouter_config_delete

    def instance_ip_create(self, obj):
        """Create new instance-ip.
        
        :param obj: :class:`.InstanceIp` object
        
        """
        raise NotImplementedError, 'instance_ip_create is %s\'s responsibility' % (str(type (self)))
    #end instance_ip_create

    def instance_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return instance-ip information.
        
        :param fq_name: Fully qualified name of instance-ip
        :param fq_name_str: Fully qualified name string of instance-ip
        :param id: UUID of instance-ip
        :param ifmap_id: IFMAP id of instance-ip
        :returns: :class:`.InstanceIp` object
        
        """
        raise NotImplementedError, 'instance_ip_read is %s\'s responsibility' % (str(type (self)))
    #end instance_ip_read

    def instance_ip_update(self, obj):
        """Update instance-ip.
        
        :param obj: :class:`.InstanceIp` object
        
        """
        raise NotImplementedError, 'instance_ip_update is %s\'s responsibility' % (str(type (self)))
    #end instance_ip_update

    def instance_ips_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all instance-ips."""
        raise NotImplementedError, 'instance_ips_list is %s\'s responsibility' % (str(type (self)))
    #end instance_ips_list

    def instance_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete instance-ip from the system.
        
        :param fq_name: Fully qualified name of instance-ip
        :param id: UUID of instance-ip
        :param ifmap_id: IFMAP id of instance-ip
        
        """
        raise NotImplementedError, 'instance_ip_delete is %s\'s responsibility' % (str(type (self)))
    #end instance_ip_delete

    def get_default_instance_ip_id(self):
        """Return UUID of default instance-ip."""
        raise NotImplementedError, 'get_default_instance_ip_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_instance_ip_delete

    def network_policy_create(self, obj):
        """Create new network-policy.
        
        :param obj: :class:`.NetworkPolicy` object
        
        """
        raise NotImplementedError, 'network_policy_create is %s\'s responsibility' % (str(type (self)))
    #end network_policy_create

    def network_policy_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return network-policy information.
        
        :param fq_name: Fully qualified name of network-policy
        :param fq_name_str: Fully qualified name string of network-policy
        :param id: UUID of network-policy
        :param ifmap_id: IFMAP id of network-policy
        :returns: :class:`.NetworkPolicy` object
        
        """
        raise NotImplementedError, 'network_policy_read is %s\'s responsibility' % (str(type (self)))
    #end network_policy_read

    def network_policy_update(self, obj):
        """Update network-policy.
        
        :param obj: :class:`.NetworkPolicy` object
        
        """
        raise NotImplementedError, 'network_policy_update is %s\'s responsibility' % (str(type (self)))
    #end network_policy_update

    def network_policys_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all network-policys.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.NetworkPolicy` objects
        
        """
        raise NotImplementedError, 'network_policys_list is %s\'s responsibility' % (str(type (self)))
    #end network_policys_list

    def network_policy_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete network-policy from the system.
        
        :param fq_name: Fully qualified name of network-policy
        :param id: UUID of network-policy
        :param ifmap_id: IFMAP id of network-policy
        
        """
        raise NotImplementedError, 'network_policy_delete is %s\'s responsibility' % (str(type (self)))
    #end network_policy_delete

    def get_default_network_policy_id(self):
        """Return UUID of default network-policy."""
        raise NotImplementedError, 'get_default_network_policy_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_network_policy_delete

    def loadbalancer_pool_create(self, obj):
        """Create new loadbalancer-pool.
        
        :param obj: :class:`.LoadbalancerPool` object
        
        """
        raise NotImplementedError, 'loadbalancer_pool_create is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_pool_create

    def loadbalancer_pool_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer-pool information.
        
        :param fq_name: Fully qualified name of loadbalancer-pool
        :param fq_name_str: Fully qualified name string of loadbalancer-pool
        :param id: UUID of loadbalancer-pool
        :param ifmap_id: IFMAP id of loadbalancer-pool
        :returns: :class:`.LoadbalancerPool` object
        
        """
        raise NotImplementedError, 'loadbalancer_pool_read is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_pool_read

    def loadbalancer_pool_update(self, obj):
        """Update loadbalancer-pool.
        
        :param obj: :class:`.LoadbalancerPool` object
        
        """
        raise NotImplementedError, 'loadbalancer_pool_update is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_pool_update

    def loadbalancer_pools_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancer-pools.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerPool` objects
        
        """
        raise NotImplementedError, 'loadbalancer_pools_list is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_pools_list

    def loadbalancer_pool_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-pool from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-pool
        :param id: UUID of loadbalancer-pool
        :param ifmap_id: IFMAP id of loadbalancer-pool
        
        """
        raise NotImplementedError, 'loadbalancer_pool_delete is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_pool_delete

    def get_default_loadbalancer_pool_id(self):
        """Return UUID of default loadbalancer-pool."""
        raise NotImplementedError, 'get_default_loadbalancer_pool_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_loadbalancer_pool_delete

    def virtual_DNS_record_create(self, obj):
        """Create new virtual-DNS-record.
        
        :param obj: :class:`.VirtualDnsRecord` object
        
        """
        raise NotImplementedError, 'virtual_DNS_record_create is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_record_create

    def virtual_DNS_record_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-DNS-record information.
        
        :param fq_name: Fully qualified name of virtual-DNS-record
        :param fq_name_str: Fully qualified name string of virtual-DNS-record
        :param id: UUID of virtual-DNS-record
        :param ifmap_id: IFMAP id of virtual-DNS-record
        :returns: :class:`.VirtualDnsRecord` object
        
        """
        raise NotImplementedError, 'virtual_DNS_record_read is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_record_read

    def virtual_DNS_record_update(self, obj):
        """Update virtual-DNS-record.
        
        :param obj: :class:`.VirtualDnsRecord` object
        
        """
        raise NotImplementedError, 'virtual_DNS_record_update is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_record_update

    def virtual_DNS_records_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-DNS-records.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualDnsRecord` objects
        
        """
        raise NotImplementedError, 'virtual_DNS_records_list is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_records_list

    def virtual_DNS_record_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-DNS-record from the system.
        
        :param fq_name: Fully qualified name of virtual-DNS-record
        :param id: UUID of virtual-DNS-record
        :param ifmap_id: IFMAP id of virtual-DNS-record
        
        """
        raise NotImplementedError, 'virtual_DNS_record_delete is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_record_delete

    def get_default_virtual_DNS_record_id(self):
        """Return UUID of default virtual-DNS-record."""
        raise NotImplementedError, 'get_default_virtual_DNS_record_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_virtual_DNS_record_delete

    def route_target_create(self, obj):
        """Create new route-target.
        
        :param obj: :class:`.RouteTarget` object
        
        """
        raise NotImplementedError, 'route_target_create is %s\'s responsibility' % (str(type (self)))
    #end route_target_create

    def route_target_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return route-target information.
        
        :param fq_name: Fully qualified name of route-target
        :param fq_name_str: Fully qualified name string of route-target
        :param id: UUID of route-target
        :param ifmap_id: IFMAP id of route-target
        :returns: :class:`.RouteTarget` object
        
        """
        raise NotImplementedError, 'route_target_read is %s\'s responsibility' % (str(type (self)))
    #end route_target_read

    def route_target_update(self, obj):
        """Update route-target.
        
        :param obj: :class:`.RouteTarget` object
        
        """
        raise NotImplementedError, 'route_target_update is %s\'s responsibility' % (str(type (self)))
    #end route_target_update

    def route_targets_list(self, obj_uuids = None, fields = None, detail = False, count = False):
        """List all route-targets."""
        raise NotImplementedError, 'route_targets_list is %s\'s responsibility' % (str(type (self)))
    #end route_targets_list

    def route_target_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete route-target from the system.
        
        :param fq_name: Fully qualified name of route-target
        :param id: UUID of route-target
        :param ifmap_id: IFMAP id of route-target
        
        """
        raise NotImplementedError, 'route_target_delete is %s\'s responsibility' % (str(type (self)))
    #end route_target_delete

    def get_default_route_target_id(self):
        """Return UUID of default route-target."""
        raise NotImplementedError, 'get_default_route_target_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_route_target_delete

    def floating_ip_create(self, obj):
        """Create new floating-ip.
        
        :param obj: :class:`.FloatingIp` object
        
        """
        raise NotImplementedError, 'floating_ip_create is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_create

    def floating_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return floating-ip information.
        
        :param fq_name: Fully qualified name of floating-ip
        :param fq_name_str: Fully qualified name string of floating-ip
        :param id: UUID of floating-ip
        :param ifmap_id: IFMAP id of floating-ip
        :returns: :class:`.FloatingIp` object
        
        """
        raise NotImplementedError, 'floating_ip_read is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_read

    def floating_ip_update(self, obj):
        """Update floating-ip.
        
        :param obj: :class:`.FloatingIp` object
        
        """
        raise NotImplementedError, 'floating_ip_update is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_update

    def floating_ips_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all floating-ips.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FloatingIp` objects
        
        """
        raise NotImplementedError, 'floating_ips_list is %s\'s responsibility' % (str(type (self)))
    #end floating_ips_list

    def floating_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete floating-ip from the system.
        
        :param fq_name: Fully qualified name of floating-ip
        :param id: UUID of floating-ip
        :param ifmap_id: IFMAP id of floating-ip
        
        """
        raise NotImplementedError, 'floating_ip_delete is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_delete

    def get_default_floating_ip_id(self):
        """Return UUID of default floating-ip."""
        raise NotImplementedError, 'get_default_floating_ip_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_floating_ip_delete

    def floating_ip_pool_create(self, obj):
        """Create new floating-ip-pool.
        
        :param obj: :class:`.FloatingIpPool` object
        
        """
        raise NotImplementedError, 'floating_ip_pool_create is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_pool_create

    def floating_ip_pool_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return floating-ip-pool information.
        
        :param fq_name: Fully qualified name of floating-ip-pool
        :param fq_name_str: Fully qualified name string of floating-ip-pool
        :param id: UUID of floating-ip-pool
        :param ifmap_id: IFMAP id of floating-ip-pool
        :returns: :class:`.FloatingIpPool` object
        
        """
        raise NotImplementedError, 'floating_ip_pool_read is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_pool_read

    def floating_ip_pool_update(self, obj):
        """Update floating-ip-pool.
        
        :param obj: :class:`.FloatingIpPool` object
        
        """
        raise NotImplementedError, 'floating_ip_pool_update is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_pool_update

    def floating_ip_pools_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all floating-ip-pools.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.FloatingIpPool` objects
        
        """
        raise NotImplementedError, 'floating_ip_pools_list is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_pools_list

    def floating_ip_pool_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete floating-ip-pool from the system.
        
        :param fq_name: Fully qualified name of floating-ip-pool
        :param id: UUID of floating-ip-pool
        :param ifmap_id: IFMAP id of floating-ip-pool
        
        """
        raise NotImplementedError, 'floating_ip_pool_delete is %s\'s responsibility' % (str(type (self)))
    #end floating_ip_pool_delete

    def get_default_floating_ip_pool_id(self):
        """Return UUID of default floating-ip-pool."""
        raise NotImplementedError, 'get_default_floating_ip_pool_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_floating_ip_pool_delete

    def physical_router_create(self, obj):
        """Create new physical-router.
        
        :param obj: :class:`.PhysicalRouter` object
        
        """
        raise NotImplementedError, 'physical_router_create is %s\'s responsibility' % (str(type (self)))
    #end physical_router_create

    def physical_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return physical-router information.
        
        :param fq_name: Fully qualified name of physical-router
        :param fq_name_str: Fully qualified name string of physical-router
        :param id: UUID of physical-router
        :param ifmap_id: IFMAP id of physical-router
        :returns: :class:`.PhysicalRouter` object
        
        """
        raise NotImplementedError, 'physical_router_read is %s\'s responsibility' % (str(type (self)))
    #end physical_router_read

    def physical_router_update(self, obj):
        """Update physical-router.
        
        :param obj: :class:`.PhysicalRouter` object
        
        """
        raise NotImplementedError, 'physical_router_update is %s\'s responsibility' % (str(type (self)))
    #end physical_router_update

    def physical_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all physical-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PhysicalRouter` objects
        
        """
        raise NotImplementedError, 'physical_routers_list is %s\'s responsibility' % (str(type (self)))
    #end physical_routers_list

    def physical_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete physical-router from the system.
        
        :param fq_name: Fully qualified name of physical-router
        :param id: UUID of physical-router
        :param ifmap_id: IFMAP id of physical-router
        
        """
        raise NotImplementedError, 'physical_router_delete is %s\'s responsibility' % (str(type (self)))
    #end physical_router_delete

    def get_default_physical_router_id(self):
        """Return UUID of default physical-router."""
        raise NotImplementedError, 'get_default_physical_router_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_physical_router_delete

    def bgp_router_create(self, obj):
        """Create new bgp-router.
        
        :param obj: :class:`.BgpRouter` object
        
        """
        raise NotImplementedError, 'bgp_router_create is %s\'s responsibility' % (str(type (self)))
    #end bgp_router_create

    def bgp_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return bgp-router information.
        
        :param fq_name: Fully qualified name of bgp-router
        :param fq_name_str: Fully qualified name string of bgp-router
        :param id: UUID of bgp-router
        :param ifmap_id: IFMAP id of bgp-router
        :returns: :class:`.BgpRouter` object
        
        """
        raise NotImplementedError, 'bgp_router_read is %s\'s responsibility' % (str(type (self)))
    #end bgp_router_read

    def bgp_router_update(self, obj):
        """Update bgp-router.
        
        :param obj: :class:`.BgpRouter` object
        
        """
        raise NotImplementedError, 'bgp_router_update is %s\'s responsibility' % (str(type (self)))
    #end bgp_router_update

    def bgp_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all bgp-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.BgpRouter` objects
        
        """
        raise NotImplementedError, 'bgp_routers_list is %s\'s responsibility' % (str(type (self)))
    #end bgp_routers_list

    def bgp_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete bgp-router from the system.
        
        :param fq_name: Fully qualified name of bgp-router
        :param id: UUID of bgp-router
        :param ifmap_id: IFMAP id of bgp-router
        
        """
        raise NotImplementedError, 'bgp_router_delete is %s\'s responsibility' % (str(type (self)))
    #end bgp_router_delete

    def get_default_bgp_router_id(self):
        """Return UUID of default bgp-router."""
        raise NotImplementedError, 'get_default_bgp_router_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_bgp_router_delete

    def virtual_router_create(self, obj):
        """Create new virtual-router.
        
        :param obj: :class:`.VirtualRouter` object
        
        """
        raise NotImplementedError, 'virtual_router_create is %s\'s responsibility' % (str(type (self)))
    #end virtual_router_create

    def virtual_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-router information.
        
        :param fq_name: Fully qualified name of virtual-router
        :param fq_name_str: Fully qualified name string of virtual-router
        :param id: UUID of virtual-router
        :param ifmap_id: IFMAP id of virtual-router
        :returns: :class:`.VirtualRouter` object
        
        """
        raise NotImplementedError, 'virtual_router_read is %s\'s responsibility' % (str(type (self)))
    #end virtual_router_read

    def virtual_router_update(self, obj):
        """Update virtual-router.
        
        :param obj: :class:`.VirtualRouter` object
        
        """
        raise NotImplementedError, 'virtual_router_update is %s\'s responsibility' % (str(type (self)))
    #end virtual_router_update

    def virtual_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualRouter` objects
        
        """
        raise NotImplementedError, 'virtual_routers_list is %s\'s responsibility' % (str(type (self)))
    #end virtual_routers_list

    def virtual_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-router from the system.
        
        :param fq_name: Fully qualified name of virtual-router
        :param id: UUID of virtual-router
        :param ifmap_id: IFMAP id of virtual-router
        
        """
        raise NotImplementedError, 'virtual_router_delete is %s\'s responsibility' % (str(type (self)))
    #end virtual_router_delete

    def get_default_virtual_router_id(self):
        """Return UUID of default virtual-router."""
        raise NotImplementedError, 'get_default_virtual_router_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_virtual_router_delete

    def config_root_create(self, obj):
        """Create new config-root.
        
        :param obj: :class:`.ConfigRoot` object
        
        """
        raise NotImplementedError, 'config_root_create is %s\'s responsibility' % (str(type (self)))
    #end config_root_create

    def config_root_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return config-root information.
        
        :param fq_name: Fully qualified name of config-root
        :param fq_name_str: Fully qualified name string of config-root
        :param id: UUID of config-root
        :param ifmap_id: IFMAP id of config-root
        :returns: :class:`.ConfigRoot` object
        
        """
        raise NotImplementedError, 'config_root_read is %s\'s responsibility' % (str(type (self)))
    #end config_root_read

    def config_root_update(self, obj):
        """Update config-root.
        
        :param obj: :class:`.ConfigRoot` object
        
        """
        raise NotImplementedError, 'config_root_update is %s\'s responsibility' % (str(type (self)))
    #end config_root_update

    def config_roots_list(self, obj_uuids = None, fields = None, detail = False, count = False):
        """List all config-roots."""
        raise NotImplementedError, 'config_roots_list is %s\'s responsibility' % (str(type (self)))
    #end config_roots_list

    def config_root_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete config-root from the system.
        
        :param fq_name: Fully qualified name of config-root
        :param id: UUID of config-root
        :param ifmap_id: IFMAP id of config-root
        
        """
        raise NotImplementedError, 'config_root_delete is %s\'s responsibility' % (str(type (self)))
    #end config_root_delete

    def get_default_config_root_id(self):
        """Return UUID of default config-root."""
        raise NotImplementedError, 'get_default_config_root_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_config_root_delete

    def subnet_create(self, obj):
        """Create new subnet.
        
        :param obj: :class:`.Subnet` object
        
        """
        raise NotImplementedError, 'subnet_create is %s\'s responsibility' % (str(type (self)))
    #end subnet_create

    def subnet_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return subnet information.
        
        :param fq_name: Fully qualified name of subnet
        :param fq_name_str: Fully qualified name string of subnet
        :param id: UUID of subnet
        :param ifmap_id: IFMAP id of subnet
        :returns: :class:`.Subnet` object
        
        """
        raise NotImplementedError, 'subnet_read is %s\'s responsibility' % (str(type (self)))
    #end subnet_read

    def subnet_update(self, obj):
        """Update subnet.
        
        :param obj: :class:`.Subnet` object
        
        """
        raise NotImplementedError, 'subnet_update is %s\'s responsibility' % (str(type (self)))
    #end subnet_update

    def subnets_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all subnets."""
        raise NotImplementedError, 'subnets_list is %s\'s responsibility' % (str(type (self)))
    #end subnets_list

    def subnet_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete subnet from the system.
        
        :param fq_name: Fully qualified name of subnet
        :param id: UUID of subnet
        :param ifmap_id: IFMAP id of subnet
        
        """
        raise NotImplementedError, 'subnet_delete is %s\'s responsibility' % (str(type (self)))
    #end subnet_delete

    def get_default_subnet_id(self):
        """Return UUID of default subnet."""
        raise NotImplementedError, 'get_default_subnet_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_subnet_delete

    def global_system_config_create(self, obj):
        """Create new global-system-config.
        
        :param obj: :class:`.GlobalSystemConfig` object
        
        """
        raise NotImplementedError, 'global_system_config_create is %s\'s responsibility' % (str(type (self)))
    #end global_system_config_create

    def global_system_config_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return global-system-config information.
        
        :param fq_name: Fully qualified name of global-system-config
        :param fq_name_str: Fully qualified name string of global-system-config
        :param id: UUID of global-system-config
        :param ifmap_id: IFMAP id of global-system-config
        :returns: :class:`.GlobalSystemConfig` object
        
        """
        raise NotImplementedError, 'global_system_config_read is %s\'s responsibility' % (str(type (self)))
    #end global_system_config_read

    def global_system_config_update(self, obj):
        """Update global-system-config.
        
        :param obj: :class:`.GlobalSystemConfig` object
        
        """
        raise NotImplementedError, 'global_system_config_update is %s\'s responsibility' % (str(type (self)))
    #end global_system_config_update

    def global_system_configs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all global-system-configs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.GlobalSystemConfig` objects
        
        """
        raise NotImplementedError, 'global_system_configs_list is %s\'s responsibility' % (str(type (self)))
    #end global_system_configs_list

    def global_system_config_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete global-system-config from the system.
        
        :param fq_name: Fully qualified name of global-system-config
        :param id: UUID of global-system-config
        :param ifmap_id: IFMAP id of global-system-config
        
        """
        raise NotImplementedError, 'global_system_config_delete is %s\'s responsibility' % (str(type (self)))
    #end global_system_config_delete

    def get_default_global_system_config_id(self):
        """Return UUID of default global-system-config."""
        raise NotImplementedError, 'get_default_global_system_config_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_global_system_config_delete

    def service_appliance_create(self, obj):
        """Create new service-appliance.
        
        :param obj: :class:`.ServiceAppliance` object
        
        """
        raise NotImplementedError, 'service_appliance_create is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_create

    def service_appliance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-appliance information.
        
        :param fq_name: Fully qualified name of service-appliance
        :param fq_name_str: Fully qualified name string of service-appliance
        :param id: UUID of service-appliance
        :param ifmap_id: IFMAP id of service-appliance
        :returns: :class:`.ServiceAppliance` object
        
        """
        raise NotImplementedError, 'service_appliance_read is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_read

    def service_appliance_update(self, obj):
        """Update service-appliance.
        
        :param obj: :class:`.ServiceAppliance` object
        
        """
        raise NotImplementedError, 'service_appliance_update is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_update

    def service_appliances_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-appliances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceAppliance` objects
        
        """
        raise NotImplementedError, 'service_appliances_list is %s\'s responsibility' % (str(type (self)))
    #end service_appliances_list

    def service_appliance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-appliance from the system.
        
        :param fq_name: Fully qualified name of service-appliance
        :param id: UUID of service-appliance
        :param ifmap_id: IFMAP id of service-appliance
        
        """
        raise NotImplementedError, 'service_appliance_delete is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_delete

    def get_default_service_appliance_id(self):
        """Return UUID of default service-appliance."""
        raise NotImplementedError, 'get_default_service_appliance_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_service_appliance_delete

    def service_instance_create(self, obj):
        """Create new service-instance.
        
        :param obj: :class:`.ServiceInstance` object
        
        """
        raise NotImplementedError, 'service_instance_create is %s\'s responsibility' % (str(type (self)))
    #end service_instance_create

    def service_instance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-instance information.
        
        :param fq_name: Fully qualified name of service-instance
        :param fq_name_str: Fully qualified name string of service-instance
        :param id: UUID of service-instance
        :param ifmap_id: IFMAP id of service-instance
        :returns: :class:`.ServiceInstance` object
        
        """
        raise NotImplementedError, 'service_instance_read is %s\'s responsibility' % (str(type (self)))
    #end service_instance_read

    def service_instance_update(self, obj):
        """Update service-instance.
        
        :param obj: :class:`.ServiceInstance` object
        
        """
        raise NotImplementedError, 'service_instance_update is %s\'s responsibility' % (str(type (self)))
    #end service_instance_update

    def service_instances_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-instances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceInstance` objects
        
        """
        raise NotImplementedError, 'service_instances_list is %s\'s responsibility' % (str(type (self)))
    #end service_instances_list

    def service_instance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-instance from the system.
        
        :param fq_name: Fully qualified name of service-instance
        :param id: UUID of service-instance
        :param ifmap_id: IFMAP id of service-instance
        
        """
        raise NotImplementedError, 'service_instance_delete is %s\'s responsibility' % (str(type (self)))
    #end service_instance_delete

    def get_default_service_instance_id(self):
        """Return UUID of default service-instance."""
        raise NotImplementedError, 'get_default_service_instance_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_service_instance_delete

    def namespace_create(self, obj):
        """Create new namespace.
        
        :param obj: :class:`.Namespace` object
        
        """
        raise NotImplementedError, 'namespace_create is %s\'s responsibility' % (str(type (self)))
    #end namespace_create

    def namespace_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return namespace information.
        
        :param fq_name: Fully qualified name of namespace
        :param fq_name_str: Fully qualified name string of namespace
        :param id: UUID of namespace
        :param ifmap_id: IFMAP id of namespace
        :returns: :class:`.Namespace` object
        
        """
        raise NotImplementedError, 'namespace_read is %s\'s responsibility' % (str(type (self)))
    #end namespace_read

    def namespace_update(self, obj):
        """Update namespace.
        
        :param obj: :class:`.Namespace` object
        
        """
        raise NotImplementedError, 'namespace_update is %s\'s responsibility' % (str(type (self)))
    #end namespace_update

    def namespaces_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all namespaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Namespace` objects
        
        """
        raise NotImplementedError, 'namespaces_list is %s\'s responsibility' % (str(type (self)))
    #end namespaces_list

    def namespace_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete namespace from the system.
        
        :param fq_name: Fully qualified name of namespace
        :param id: UUID of namespace
        :param ifmap_id: IFMAP id of namespace
        
        """
        raise NotImplementedError, 'namespace_delete is %s\'s responsibility' % (str(type (self)))
    #end namespace_delete

    def get_default_namespace_id(self):
        """Return UUID of default namespace."""
        raise NotImplementedError, 'get_default_namespace_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_namespace_delete

    def logical_interface_create(self, obj):
        """Create new logical-interface.
        
        :param obj: :class:`.LogicalInterface` object
        
        """
        raise NotImplementedError, 'logical_interface_create is %s\'s responsibility' % (str(type (self)))
    #end logical_interface_create

    def logical_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return logical-interface information.
        
        :param fq_name: Fully qualified name of logical-interface
        :param fq_name_str: Fully qualified name string of logical-interface
        :param id: UUID of logical-interface
        :param ifmap_id: IFMAP id of logical-interface
        :returns: :class:`.LogicalInterface` object
        
        """
        raise NotImplementedError, 'logical_interface_read is %s\'s responsibility' % (str(type (self)))
    #end logical_interface_read

    def logical_interface_update(self, obj):
        """Update logical-interface.
        
        :param obj: :class:`.LogicalInterface` object
        
        """
        raise NotImplementedError, 'logical_interface_update is %s\'s responsibility' % (str(type (self)))
    #end logical_interface_update

    def logical_interfaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all logical-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LogicalInterface` objects
        
        """
        raise NotImplementedError, 'logical_interfaces_list is %s\'s responsibility' % (str(type (self)))
    #end logical_interfaces_list

    def logical_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete logical-interface from the system.
        
        :param fq_name: Fully qualified name of logical-interface
        :param id: UUID of logical-interface
        :param ifmap_id: IFMAP id of logical-interface
        
        """
        raise NotImplementedError, 'logical_interface_delete is %s\'s responsibility' % (str(type (self)))
    #end logical_interface_delete

    def get_default_logical_interface_id(self):
        """Return UUID of default logical-interface."""
        raise NotImplementedError, 'get_default_logical_interface_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_logical_interface_delete

    def route_table_create(self, obj):
        """Create new route-table.
        
        :param obj: :class:`.RouteTable` object
        
        """
        raise NotImplementedError, 'route_table_create is %s\'s responsibility' % (str(type (self)))
    #end route_table_create

    def route_table_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return route-table information.
        
        :param fq_name: Fully qualified name of route-table
        :param fq_name_str: Fully qualified name string of route-table
        :param id: UUID of route-table
        :param ifmap_id: IFMAP id of route-table
        :returns: :class:`.RouteTable` object
        
        """
        raise NotImplementedError, 'route_table_read is %s\'s responsibility' % (str(type (self)))
    #end route_table_read

    def route_table_update(self, obj):
        """Update route-table.
        
        :param obj: :class:`.RouteTable` object
        
        """
        raise NotImplementedError, 'route_table_update is %s\'s responsibility' % (str(type (self)))
    #end route_table_update

    def route_tables_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all route-tables.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RouteTable` objects
        
        """
        raise NotImplementedError, 'route_tables_list is %s\'s responsibility' % (str(type (self)))
    #end route_tables_list

    def route_table_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete route-table from the system.
        
        :param fq_name: Fully qualified name of route-table
        :param id: UUID of route-table
        :param ifmap_id: IFMAP id of route-table
        
        """
        raise NotImplementedError, 'route_table_delete is %s\'s responsibility' % (str(type (self)))
    #end route_table_delete

    def get_default_route_table_id(self):
        """Return UUID of default route-table."""
        raise NotImplementedError, 'get_default_route_table_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_route_table_delete

    def physical_interface_create(self, obj):
        """Create new physical-interface.
        
        :param obj: :class:`.PhysicalInterface` object
        
        """
        raise NotImplementedError, 'physical_interface_create is %s\'s responsibility' % (str(type (self)))
    #end physical_interface_create

    def physical_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return physical-interface information.
        
        :param fq_name: Fully qualified name of physical-interface
        :param fq_name_str: Fully qualified name string of physical-interface
        :param id: UUID of physical-interface
        :param ifmap_id: IFMAP id of physical-interface
        :returns: :class:`.PhysicalInterface` object
        
        """
        raise NotImplementedError, 'physical_interface_read is %s\'s responsibility' % (str(type (self)))
    #end physical_interface_read

    def physical_interface_update(self, obj):
        """Update physical-interface.
        
        :param obj: :class:`.PhysicalInterface` object
        
        """
        raise NotImplementedError, 'physical_interface_update is %s\'s responsibility' % (str(type (self)))
    #end physical_interface_update

    def physical_interfaces_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all physical-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.PhysicalInterface` objects
        
        """
        raise NotImplementedError, 'physical_interfaces_list is %s\'s responsibility' % (str(type (self)))
    #end physical_interfaces_list

    def physical_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete physical-interface from the system.
        
        :param fq_name: Fully qualified name of physical-interface
        :param id: UUID of physical-interface
        :param ifmap_id: IFMAP id of physical-interface
        
        """
        raise NotImplementedError, 'physical_interface_delete is %s\'s responsibility' % (str(type (self)))
    #end physical_interface_delete

    def get_default_physical_interface_id(self):
        """Return UUID of default physical-interface."""
        raise NotImplementedError, 'get_default_physical_interface_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_physical_interface_delete

    def access_control_list_create(self, obj):
        """Create new access-control-list.
        
        :param obj: :class:`.AccessControlList` object
        
        """
        raise NotImplementedError, 'access_control_list_create is %s\'s responsibility' % (str(type (self)))
    #end access_control_list_create

    def access_control_list_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return access-control-list information.
        
        :param fq_name: Fully qualified name of access-control-list
        :param fq_name_str: Fully qualified name string of access-control-list
        :param id: UUID of access-control-list
        :param ifmap_id: IFMAP id of access-control-list
        :returns: :class:`.AccessControlList` object
        
        """
        raise NotImplementedError, 'access_control_list_read is %s\'s responsibility' % (str(type (self)))
    #end access_control_list_read

    def access_control_list_update(self, obj):
        """Update access-control-list.
        
        :param obj: :class:`.AccessControlList` object
        
        """
        raise NotImplementedError, 'access_control_list_update is %s\'s responsibility' % (str(type (self)))
    #end access_control_list_update

    def access_control_lists_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all access-control-lists.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AccessControlList` objects
        
        """
        raise NotImplementedError, 'access_control_lists_list is %s\'s responsibility' % (str(type (self)))
    #end access_control_lists_list

    def access_control_list_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete access-control-list from the system.
        
        :param fq_name: Fully qualified name of access-control-list
        :param id: UUID of access-control-list
        :param ifmap_id: IFMAP id of access-control-list
        
        """
        raise NotImplementedError, 'access_control_list_delete is %s\'s responsibility' % (str(type (self)))
    #end access_control_list_delete

    def get_default_access_control_list_id(self):
        """Return UUID of default access-control-list."""
        raise NotImplementedError, 'get_default_access_control_list_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_access_control_list_delete

    def analytics_node_create(self, obj):
        """Create new analytics-node.
        
        :param obj: :class:`.AnalyticsNode` object
        
        """
        raise NotImplementedError, 'analytics_node_create is %s\'s responsibility' % (str(type (self)))
    #end analytics_node_create

    def analytics_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return analytics-node information.
        
        :param fq_name: Fully qualified name of analytics-node
        :param fq_name_str: Fully qualified name string of analytics-node
        :param id: UUID of analytics-node
        :param ifmap_id: IFMAP id of analytics-node
        :returns: :class:`.AnalyticsNode` object
        
        """
        raise NotImplementedError, 'analytics_node_read is %s\'s responsibility' % (str(type (self)))
    #end analytics_node_read

    def analytics_node_update(self, obj):
        """Update analytics-node.
        
        :param obj: :class:`.AnalyticsNode` object
        
        """
        raise NotImplementedError, 'analytics_node_update is %s\'s responsibility' % (str(type (self)))
    #end analytics_node_update

    def analytics_nodes_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all analytics-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.AnalyticsNode` objects
        
        """
        raise NotImplementedError, 'analytics_nodes_list is %s\'s responsibility' % (str(type (self)))
    #end analytics_nodes_list

    def analytics_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete analytics-node from the system.
        
        :param fq_name: Fully qualified name of analytics-node
        :param id: UUID of analytics-node
        :param ifmap_id: IFMAP id of analytics-node
        
        """
        raise NotImplementedError, 'analytics_node_delete is %s\'s responsibility' % (str(type (self)))
    #end analytics_node_delete

    def get_default_analytics_node_id(self):
        """Return UUID of default analytics-node."""
        raise NotImplementedError, 'get_default_analytics_node_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_analytics_node_delete

    def virtual_DNS_create(self, obj):
        """Create new virtual-DNS.
        
        :param obj: :class:`.VirtualDns` object
        
        """
        raise NotImplementedError, 'virtual_DNS_create is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_create

    def virtual_DNS_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-DNS information.
        
        :param fq_name: Fully qualified name of virtual-DNS
        :param fq_name_str: Fully qualified name string of virtual-DNS
        :param id: UUID of virtual-DNS
        :param ifmap_id: IFMAP id of virtual-DNS
        :returns: :class:`.VirtualDns` object
        
        """
        raise NotImplementedError, 'virtual_DNS_read is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_read

    def virtual_DNS_update(self, obj):
        """Update virtual-DNS.
        
        :param obj: :class:`.VirtualDns` object
        
        """
        raise NotImplementedError, 'virtual_DNS_update is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_update

    def virtual_DNSs_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-DNSs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualDns` objects
        
        """
        raise NotImplementedError, 'virtual_DNSs_list is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNSs_list

    def virtual_DNS_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-DNS from the system.
        
        :param fq_name: Fully qualified name of virtual-DNS
        :param id: UUID of virtual-DNS
        :param ifmap_id: IFMAP id of virtual-DNS
        
        """
        raise NotImplementedError, 'virtual_DNS_delete is %s\'s responsibility' % (str(type (self)))
    #end virtual_DNS_delete

    def get_default_virtual_DNS_id(self):
        """Return UUID of default virtual-DNS."""
        raise NotImplementedError, 'get_default_virtual_DNS_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_virtual_DNS_delete

    def customer_attachment_create(self, obj):
        """Create new customer-attachment.
        
        :param obj: :class:`.CustomerAttachment` object
        
        """
        raise NotImplementedError, 'customer_attachment_create is %s\'s responsibility' % (str(type (self)))
    #end customer_attachment_create

    def customer_attachment_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return customer-attachment information.
        
        :param fq_name: Fully qualified name of customer-attachment
        :param fq_name_str: Fully qualified name string of customer-attachment
        :param id: UUID of customer-attachment
        :param ifmap_id: IFMAP id of customer-attachment
        :returns: :class:`.CustomerAttachment` object
        
        """
        raise NotImplementedError, 'customer_attachment_read is %s\'s responsibility' % (str(type (self)))
    #end customer_attachment_read

    def customer_attachment_update(self, obj):
        """Update customer-attachment.
        
        :param obj: :class:`.CustomerAttachment` object
        
        """
        raise NotImplementedError, 'customer_attachment_update is %s\'s responsibility' % (str(type (self)))
    #end customer_attachment_update

    def customer_attachments_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all customer-attachments."""
        raise NotImplementedError, 'customer_attachments_list is %s\'s responsibility' % (str(type (self)))
    #end customer_attachments_list

    def customer_attachment_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete customer-attachment from the system.
        
        :param fq_name: Fully qualified name of customer-attachment
        :param id: UUID of customer-attachment
        :param ifmap_id: IFMAP id of customer-attachment
        
        """
        raise NotImplementedError, 'customer_attachment_delete is %s\'s responsibility' % (str(type (self)))
    #end customer_attachment_delete

    def get_default_customer_attachment_id(self):
        """Return UUID of default customer-attachment."""
        raise NotImplementedError, 'get_default_customer_attachment_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_customer_attachment_delete

    def service_appliance_set_create(self, obj):
        """Create new service-appliance-set.
        
        :param obj: :class:`.ServiceApplianceSet` object
        
        """
        raise NotImplementedError, 'service_appliance_set_create is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_set_create

    def service_appliance_set_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-appliance-set information.
        
        :param fq_name: Fully qualified name of service-appliance-set
        :param fq_name_str: Fully qualified name string of service-appliance-set
        :param id: UUID of service-appliance-set
        :param ifmap_id: IFMAP id of service-appliance-set
        :returns: :class:`.ServiceApplianceSet` object
        
        """
        raise NotImplementedError, 'service_appliance_set_read is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_set_read

    def service_appliance_set_update(self, obj):
        """Update service-appliance-set.
        
        :param obj: :class:`.ServiceApplianceSet` object
        
        """
        raise NotImplementedError, 'service_appliance_set_update is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_set_update

    def service_appliance_sets_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-appliance-sets.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceApplianceSet` objects
        
        """
        raise NotImplementedError, 'service_appliance_sets_list is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_sets_list

    def service_appliance_set_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-appliance-set from the system.
        
        :param fq_name: Fully qualified name of service-appliance-set
        :param id: UUID of service-appliance-set
        :param ifmap_id: IFMAP id of service-appliance-set
        
        """
        raise NotImplementedError, 'service_appliance_set_delete is %s\'s responsibility' % (str(type (self)))
    #end service_appliance_set_delete

    def get_default_service_appliance_set_id(self):
        """Return UUID of default service-appliance-set."""
        raise NotImplementedError, 'get_default_service_appliance_set_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_service_appliance_set_delete

    def config_node_create(self, obj):
        """Create new config-node.
        
        :param obj: :class:`.ConfigNode` object
        
        """
        raise NotImplementedError, 'config_node_create is %s\'s responsibility' % (str(type (self)))
    #end config_node_create

    def config_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return config-node information.
        
        :param fq_name: Fully qualified name of config-node
        :param fq_name_str: Fully qualified name string of config-node
        :param id: UUID of config-node
        :param ifmap_id: IFMAP id of config-node
        :returns: :class:`.ConfigNode` object
        
        """
        raise NotImplementedError, 'config_node_read is %s\'s responsibility' % (str(type (self)))
    #end config_node_read

    def config_node_update(self, obj):
        """Update config-node.
        
        :param obj: :class:`.ConfigNode` object
        
        """
        raise NotImplementedError, 'config_node_update is %s\'s responsibility' % (str(type (self)))
    #end config_node_update

    def config_nodes_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all config-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ConfigNode` objects
        
        """
        raise NotImplementedError, 'config_nodes_list is %s\'s responsibility' % (str(type (self)))
    #end config_nodes_list

    def config_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete config-node from the system.
        
        :param fq_name: Fully qualified name of config-node
        :param id: UUID of config-node
        :param ifmap_id: IFMAP id of config-node
        
        """
        raise NotImplementedError, 'config_node_delete is %s\'s responsibility' % (str(type (self)))
    #end config_node_delete

    def get_default_config_node_id(self):
        """Return UUID of default config-node."""
        raise NotImplementedError, 'get_default_config_node_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_config_node_delete

    def qos_queue_create(self, obj):
        """Create new qos-queue.
        
        :param obj: :class:`.QosQueue` object
        
        """
        raise NotImplementedError, 'qos_queue_create is %s\'s responsibility' % (str(type (self)))
    #end qos_queue_create

    def qos_queue_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return qos-queue information.
        
        :param fq_name: Fully qualified name of qos-queue
        :param fq_name_str: Fully qualified name string of qos-queue
        :param id: UUID of qos-queue
        :param ifmap_id: IFMAP id of qos-queue
        :returns: :class:`.QosQueue` object
        
        """
        raise NotImplementedError, 'qos_queue_read is %s\'s responsibility' % (str(type (self)))
    #end qos_queue_read

    def qos_queue_update(self, obj):
        """Update qos-queue.
        
        :param obj: :class:`.QosQueue` object
        
        """
        raise NotImplementedError, 'qos_queue_update is %s\'s responsibility' % (str(type (self)))
    #end qos_queue_update

    def qos_queues_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all qos-queues.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.QosQueue` objects
        
        """
        raise NotImplementedError, 'qos_queues_list is %s\'s responsibility' % (str(type (self)))
    #end qos_queues_list

    def qos_queue_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete qos-queue from the system.
        
        :param fq_name: Fully qualified name of qos-queue
        :param id: UUID of qos-queue
        :param ifmap_id: IFMAP id of qos-queue
        
        """
        raise NotImplementedError, 'qos_queue_delete is %s\'s responsibility' % (str(type (self)))
    #end qos_queue_delete

    def get_default_qos_queue_id(self):
        """Return UUID of default qos-queue."""
        raise NotImplementedError, 'get_default_qos_queue_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_qos_queue_delete

    def virtual_machine_create(self, obj):
        """Create new virtual-machine.
        
        :param obj: :class:`.VirtualMachine` object
        
        """
        raise NotImplementedError, 'virtual_machine_create is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_create

    def virtual_machine_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-machine information.
        
        :param fq_name: Fully qualified name of virtual-machine
        :param fq_name_str: Fully qualified name string of virtual-machine
        :param id: UUID of virtual-machine
        :param ifmap_id: IFMAP id of virtual-machine
        :returns: :class:`.VirtualMachine` object
        
        """
        raise NotImplementedError, 'virtual_machine_read is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_read

    def virtual_machine_update(self, obj):
        """Update virtual-machine.
        
        :param obj: :class:`.VirtualMachine` object
        
        """
        raise NotImplementedError, 'virtual_machine_update is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_update

    def virtual_machines_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-machines."""
        raise NotImplementedError, 'virtual_machines_list is %s\'s responsibility' % (str(type (self)))
    #end virtual_machines_list

    def virtual_machine_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-machine from the system.
        
        :param fq_name: Fully qualified name of virtual-machine
        :param id: UUID of virtual-machine
        :param ifmap_id: IFMAP id of virtual-machine
        
        """
        raise NotImplementedError, 'virtual_machine_delete is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_delete

    def get_default_virtual_machine_id(self):
        """Return UUID of default virtual-machine."""
        raise NotImplementedError, 'get_default_virtual_machine_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_virtual_machine_delete

    def interface_route_table_create(self, obj):
        """Create new interface-route-table.
        
        :param obj: :class:`.InterfaceRouteTable` object
        
        """
        raise NotImplementedError, 'interface_route_table_create is %s\'s responsibility' % (str(type (self)))
    #end interface_route_table_create

    def interface_route_table_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return interface-route-table information.
        
        :param fq_name: Fully qualified name of interface-route-table
        :param fq_name_str: Fully qualified name string of interface-route-table
        :param id: UUID of interface-route-table
        :param ifmap_id: IFMAP id of interface-route-table
        :returns: :class:`.InterfaceRouteTable` object
        
        """
        raise NotImplementedError, 'interface_route_table_read is %s\'s responsibility' % (str(type (self)))
    #end interface_route_table_read

    def interface_route_table_update(self, obj):
        """Update interface-route-table.
        
        :param obj: :class:`.InterfaceRouteTable` object
        
        """
        raise NotImplementedError, 'interface_route_table_update is %s\'s responsibility' % (str(type (self)))
    #end interface_route_table_update

    def interface_route_tables_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all interface-route-tables.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.InterfaceRouteTable` objects
        
        """
        raise NotImplementedError, 'interface_route_tables_list is %s\'s responsibility' % (str(type (self)))
    #end interface_route_tables_list

    def interface_route_table_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete interface-route-table from the system.
        
        :param fq_name: Fully qualified name of interface-route-table
        :param id: UUID of interface-route-table
        :param ifmap_id: IFMAP id of interface-route-table
        
        """
        raise NotImplementedError, 'interface_route_table_delete is %s\'s responsibility' % (str(type (self)))
    #end interface_route_table_delete

    def get_default_interface_route_table_id(self):
        """Return UUID of default interface-route-table."""
        raise NotImplementedError, 'get_default_interface_route_table_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_interface_route_table_delete

    def service_template_create(self, obj):
        """Create new service-template.
        
        :param obj: :class:`.ServiceTemplate` object
        
        """
        raise NotImplementedError, 'service_template_create is %s\'s responsibility' % (str(type (self)))
    #end service_template_create

    def service_template_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return service-template information.
        
        :param fq_name: Fully qualified name of service-template
        :param fq_name_str: Fully qualified name string of service-template
        :param id: UUID of service-template
        :param ifmap_id: IFMAP id of service-template
        :returns: :class:`.ServiceTemplate` object
        
        """
        raise NotImplementedError, 'service_template_read is %s\'s responsibility' % (str(type (self)))
    #end service_template_read

    def service_template_update(self, obj):
        """Update service-template.
        
        :param obj: :class:`.ServiceTemplate` object
        
        """
        raise NotImplementedError, 'service_template_update is %s\'s responsibility' % (str(type (self)))
    #end service_template_update

    def service_templates_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all service-templates.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.ServiceTemplate` objects
        
        """
        raise NotImplementedError, 'service_templates_list is %s\'s responsibility' % (str(type (self)))
    #end service_templates_list

    def service_template_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete service-template from the system.
        
        :param fq_name: Fully qualified name of service-template
        :param id: UUID of service-template
        :param ifmap_id: IFMAP id of service-template
        
        """
        raise NotImplementedError, 'service_template_delete is %s\'s responsibility' % (str(type (self)))
    #end service_template_delete

    def get_default_service_template_id(self):
        """Return UUID of default service-template."""
        raise NotImplementedError, 'get_default_service_template_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_service_template_delete

    def virtual_ip_create(self, obj):
        """Create new virtual-ip.
        
        :param obj: :class:`.VirtualIp` object
        
        """
        raise NotImplementedError, 'virtual_ip_create is %s\'s responsibility' % (str(type (self)))
    #end virtual_ip_create

    def virtual_ip_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-ip information.
        
        :param fq_name: Fully qualified name of virtual-ip
        :param fq_name_str: Fully qualified name string of virtual-ip
        :param id: UUID of virtual-ip
        :param ifmap_id: IFMAP id of virtual-ip
        :returns: :class:`.VirtualIp` object
        
        """
        raise NotImplementedError, 'virtual_ip_read is %s\'s responsibility' % (str(type (self)))
    #end virtual_ip_read

    def virtual_ip_update(self, obj):
        """Update virtual-ip.
        
        :param obj: :class:`.VirtualIp` object
        
        """
        raise NotImplementedError, 'virtual_ip_update is %s\'s responsibility' % (str(type (self)))
    #end virtual_ip_update

    def virtual_ips_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-ips.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualIp` objects
        
        """
        raise NotImplementedError, 'virtual_ips_list is %s\'s responsibility' % (str(type (self)))
    #end virtual_ips_list

    def virtual_ip_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-ip from the system.
        
        :param fq_name: Fully qualified name of virtual-ip
        :param id: UUID of virtual-ip
        :param ifmap_id: IFMAP id of virtual-ip
        
        """
        raise NotImplementedError, 'virtual_ip_delete is %s\'s responsibility' % (str(type (self)))
    #end virtual_ip_delete

    def get_default_virtual_ip_id(self):
        """Return UUID of default virtual-ip."""
        raise NotImplementedError, 'get_default_virtual_ip_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_virtual_ip_delete

    def loadbalancer_member_create(self, obj):
        """Create new loadbalancer-member.
        
        :param obj: :class:`.LoadbalancerMember` object
        
        """
        raise NotImplementedError, 'loadbalancer_member_create is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_member_create

    def loadbalancer_member_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer-member information.
        
        :param fq_name: Fully qualified name of loadbalancer-member
        :param fq_name_str: Fully qualified name string of loadbalancer-member
        :param id: UUID of loadbalancer-member
        :param ifmap_id: IFMAP id of loadbalancer-member
        :returns: :class:`.LoadbalancerMember` object
        
        """
        raise NotImplementedError, 'loadbalancer_member_read is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_member_read

    def loadbalancer_member_update(self, obj):
        """Update loadbalancer-member.
        
        :param obj: :class:`.LoadbalancerMember` object
        
        """
        raise NotImplementedError, 'loadbalancer_member_update is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_member_update

    def loadbalancer_members_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancer-members.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerMember` objects
        
        """
        raise NotImplementedError, 'loadbalancer_members_list is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_members_list

    def loadbalancer_member_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-member from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-member
        :param id: UUID of loadbalancer-member
        :param ifmap_id: IFMAP id of loadbalancer-member
        
        """
        raise NotImplementedError, 'loadbalancer_member_delete is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_member_delete

    def get_default_loadbalancer_member_id(self):
        """Return UUID of default loadbalancer-member."""
        raise NotImplementedError, 'get_default_loadbalancer_member_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_loadbalancer_member_delete

    def security_group_create(self, obj):
        """Create new security-group.
        
        :param obj: :class:`.SecurityGroup` object
        
        """
        raise NotImplementedError, 'security_group_create is %s\'s responsibility' % (str(type (self)))
    #end security_group_create

    def security_group_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return security-group information.
        
        :param fq_name: Fully qualified name of security-group
        :param fq_name_str: Fully qualified name string of security-group
        :param id: UUID of security-group
        :param ifmap_id: IFMAP id of security-group
        :returns: :class:`.SecurityGroup` object
        
        """
        raise NotImplementedError, 'security_group_read is %s\'s responsibility' % (str(type (self)))
    #end security_group_read

    def security_group_update(self, obj):
        """Update security-group.
        
        :param obj: :class:`.SecurityGroup` object
        
        """
        raise NotImplementedError, 'security_group_update is %s\'s responsibility' % (str(type (self)))
    #end security_group_update

    def security_groups_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all security-groups.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.SecurityGroup` objects
        
        """
        raise NotImplementedError, 'security_groups_list is %s\'s responsibility' % (str(type (self)))
    #end security_groups_list

    def security_group_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete security-group from the system.
        
        :param fq_name: Fully qualified name of security-group
        :param id: UUID of security-group
        :param ifmap_id: IFMAP id of security-group
        
        """
        raise NotImplementedError, 'security_group_delete is %s\'s responsibility' % (str(type (self)))
    #end security_group_delete

    def get_default_security_group_id(self):
        """Return UUID of default security-group."""
        raise NotImplementedError, 'get_default_security_group_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_security_group_delete

    def provider_attachment_create(self, obj):
        """Create new provider-attachment.
        
        :param obj: :class:`.ProviderAttachment` object
        
        """
        raise NotImplementedError, 'provider_attachment_create is %s\'s responsibility' % (str(type (self)))
    #end provider_attachment_create

    def provider_attachment_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return provider-attachment information.
        
        :param fq_name: Fully qualified name of provider-attachment
        :param fq_name_str: Fully qualified name string of provider-attachment
        :param id: UUID of provider-attachment
        :param ifmap_id: IFMAP id of provider-attachment
        :returns: :class:`.ProviderAttachment` object
        
        """
        raise NotImplementedError, 'provider_attachment_read is %s\'s responsibility' % (str(type (self)))
    #end provider_attachment_read

    def provider_attachment_update(self, obj):
        """Update provider-attachment.
        
        :param obj: :class:`.ProviderAttachment` object
        
        """
        raise NotImplementedError, 'provider_attachment_update is %s\'s responsibility' % (str(type (self)))
    #end provider_attachment_update

    def provider_attachments_list(self, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all provider-attachments."""
        raise NotImplementedError, 'provider_attachments_list is %s\'s responsibility' % (str(type (self)))
    #end provider_attachments_list

    def provider_attachment_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete provider-attachment from the system.
        
        :param fq_name: Fully qualified name of provider-attachment
        :param id: UUID of provider-attachment
        :param ifmap_id: IFMAP id of provider-attachment
        
        """
        raise NotImplementedError, 'provider_attachment_delete is %s\'s responsibility' % (str(type (self)))
    #end provider_attachment_delete

    def get_default_provider_attachment_id(self):
        """Return UUID of default provider-attachment."""
        raise NotImplementedError, 'get_default_provider_attachment_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_provider_attachment_delete

    def virtual_machine_interface_create(self, obj):
        """Create new virtual-machine-interface.
        
        :param obj: :class:`.VirtualMachineInterface` object
        
        """
        raise NotImplementedError, 'virtual_machine_interface_create is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_interface_create

    def virtual_machine_interface_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-machine-interface information.
        
        :param fq_name: Fully qualified name of virtual-machine-interface
        :param fq_name_str: Fully qualified name string of virtual-machine-interface
        :param id: UUID of virtual-machine-interface
        :param ifmap_id: IFMAP id of virtual-machine-interface
        :returns: :class:`.VirtualMachineInterface` object
        
        """
        raise NotImplementedError, 'virtual_machine_interface_read is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_interface_read

    def virtual_machine_interface_update(self, obj):
        """Update virtual-machine-interface.
        
        :param obj: :class:`.VirtualMachineInterface` object
        
        """
        raise NotImplementedError, 'virtual_machine_interface_update is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_interface_update

    def virtual_machine_interfaces_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-machine-interfaces.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualMachineInterface` objects
        
        """
        raise NotImplementedError, 'virtual_machine_interfaces_list is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_interfaces_list

    def virtual_machine_interface_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-machine-interface from the system.
        
        :param fq_name: Fully qualified name of virtual-machine-interface
        :param id: UUID of virtual-machine-interface
        :param ifmap_id: IFMAP id of virtual-machine-interface
        
        """
        raise NotImplementedError, 'virtual_machine_interface_delete is %s\'s responsibility' % (str(type (self)))
    #end virtual_machine_interface_delete

    def get_default_virtual_machine_interface_id(self):
        """Return UUID of default virtual-machine-interface."""
        raise NotImplementedError, 'get_default_virtual_machine_interface_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_virtual_machine_interface_delete

    def loadbalancer_healthmonitor_create(self, obj):
        """Create new loadbalancer-healthmonitor.
        
        :param obj: :class:`.LoadbalancerHealthmonitor` object
        
        """
        raise NotImplementedError, 'loadbalancer_healthmonitor_create is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_healthmonitor_create

    def loadbalancer_healthmonitor_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return loadbalancer-healthmonitor information.
        
        :param fq_name: Fully qualified name of loadbalancer-healthmonitor
        :param fq_name_str: Fully qualified name string of loadbalancer-healthmonitor
        :param id: UUID of loadbalancer-healthmonitor
        :param ifmap_id: IFMAP id of loadbalancer-healthmonitor
        :returns: :class:`.LoadbalancerHealthmonitor` object
        
        """
        raise NotImplementedError, 'loadbalancer_healthmonitor_read is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_healthmonitor_read

    def loadbalancer_healthmonitor_update(self, obj):
        """Update loadbalancer-healthmonitor.
        
        :param obj: :class:`.LoadbalancerHealthmonitor` object
        
        """
        raise NotImplementedError, 'loadbalancer_healthmonitor_update is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_healthmonitor_update

    def loadbalancer_healthmonitors_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all loadbalancer-healthmonitors.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LoadbalancerHealthmonitor` objects
        
        """
        raise NotImplementedError, 'loadbalancer_healthmonitors_list is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_healthmonitors_list

    def loadbalancer_healthmonitor_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete loadbalancer-healthmonitor from the system.
        
        :param fq_name: Fully qualified name of loadbalancer-healthmonitor
        :param id: UUID of loadbalancer-healthmonitor
        :param ifmap_id: IFMAP id of loadbalancer-healthmonitor
        
        """
        raise NotImplementedError, 'loadbalancer_healthmonitor_delete is %s\'s responsibility' % (str(type (self)))
    #end loadbalancer_healthmonitor_delete

    def get_default_loadbalancer_healthmonitor_id(self):
        """Return UUID of default loadbalancer-healthmonitor."""
        raise NotImplementedError, 'get_default_loadbalancer_healthmonitor_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_loadbalancer_healthmonitor_delete

    def virtual_network_create(self, obj):
        """Create new virtual-network.
        
        :param obj: :class:`.VirtualNetwork` object
        
        """
        raise NotImplementedError, 'virtual_network_create is %s\'s responsibility' % (str(type (self)))
    #end virtual_network_create

    def virtual_network_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return virtual-network information.
        
        :param fq_name: Fully qualified name of virtual-network
        :param fq_name_str: Fully qualified name string of virtual-network
        :param id: UUID of virtual-network
        :param ifmap_id: IFMAP id of virtual-network
        :returns: :class:`.VirtualNetwork` object
        
        """
        raise NotImplementedError, 'virtual_network_read is %s\'s responsibility' % (str(type (self)))
    #end virtual_network_read

    def virtual_network_update(self, obj):
        """Update virtual-network.
        
        :param obj: :class:`.VirtualNetwork` object
        
        """
        raise NotImplementedError, 'virtual_network_update is %s\'s responsibility' % (str(type (self)))
    #end virtual_network_update

    def virtual_networks_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all virtual-networks.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.VirtualNetwork` objects
        
        """
        raise NotImplementedError, 'virtual_networks_list is %s\'s responsibility' % (str(type (self)))
    #end virtual_networks_list

    def virtual_network_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete virtual-network from the system.
        
        :param fq_name: Fully qualified name of virtual-network
        :param id: UUID of virtual-network
        :param ifmap_id: IFMAP id of virtual-network
        
        """
        raise NotImplementedError, 'virtual_network_delete is %s\'s responsibility' % (str(type (self)))
    #end virtual_network_delete

    def get_default_virtual_network_id(self):
        """Return UUID of default virtual-network."""
        raise NotImplementedError, 'get_default_virtual_network_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_virtual_network_delete

    def project_create(self, obj):
        """Create new project.
        
        :param obj: :class:`.Project` object
        
        """
        raise NotImplementedError, 'project_create is %s\'s responsibility' % (str(type (self)))
    #end project_create

    def project_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return project information.
        
        :param fq_name: Fully qualified name of project
        :param fq_name_str: Fully qualified name string of project
        :param id: UUID of project
        :param ifmap_id: IFMAP id of project
        :returns: :class:`.Project` object
        
        """
        raise NotImplementedError, 'project_read is %s\'s responsibility' % (str(type (self)))
    #end project_read

    def project_update(self, obj):
        """Update project.
        
        :param obj: :class:`.Project` object
        
        """
        raise NotImplementedError, 'project_update is %s\'s responsibility' % (str(type (self)))
    #end project_update

    def projects_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all projects.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.Project` objects
        
        """
        raise NotImplementedError, 'projects_list is %s\'s responsibility' % (str(type (self)))
    #end projects_list

    def project_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete project from the system.
        
        :param fq_name: Fully qualified name of project
        :param id: UUID of project
        :param ifmap_id: IFMAP id of project
        
        """
        raise NotImplementedError, 'project_delete is %s\'s responsibility' % (str(type (self)))
    #end project_delete

    def get_default_project_id(self):
        """Return UUID of default project."""
        raise NotImplementedError, 'get_default_project_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_project_delete

    def qos_forwarding_class_create(self, obj):
        """Create new qos-forwarding-class.
        
        :param obj: :class:`.QosForwardingClass` object
        
        """
        raise NotImplementedError, 'qos_forwarding_class_create is %s\'s responsibility' % (str(type (self)))
    #end qos_forwarding_class_create

    def qos_forwarding_class_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return qos-forwarding-class information.
        
        :param fq_name: Fully qualified name of qos-forwarding-class
        :param fq_name_str: Fully qualified name string of qos-forwarding-class
        :param id: UUID of qos-forwarding-class
        :param ifmap_id: IFMAP id of qos-forwarding-class
        :returns: :class:`.QosForwardingClass` object
        
        """
        raise NotImplementedError, 'qos_forwarding_class_read is %s\'s responsibility' % (str(type (self)))
    #end qos_forwarding_class_read

    def qos_forwarding_class_update(self, obj):
        """Update qos-forwarding-class.
        
        :param obj: :class:`.QosForwardingClass` object
        
        """
        raise NotImplementedError, 'qos_forwarding_class_update is %s\'s responsibility' % (str(type (self)))
    #end qos_forwarding_class_update

    def qos_forwarding_classs_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all qos-forwarding-classs.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.QosForwardingClass` objects
        
        """
        raise NotImplementedError, 'qos_forwarding_classs_list is %s\'s responsibility' % (str(type (self)))
    #end qos_forwarding_classs_list

    def qos_forwarding_class_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete qos-forwarding-class from the system.
        
        :param fq_name: Fully qualified name of qos-forwarding-class
        :param id: UUID of qos-forwarding-class
        :param ifmap_id: IFMAP id of qos-forwarding-class
        
        """
        raise NotImplementedError, 'qos_forwarding_class_delete is %s\'s responsibility' % (str(type (self)))
    #end qos_forwarding_class_delete

    def get_default_qos_forwarding_class_id(self):
        """Return UUID of default qos-forwarding-class."""
        raise NotImplementedError, 'get_default_qos_forwarding_class_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_qos_forwarding_class_delete

    def database_node_create(self, obj):
        """Create new database-node.
        
        :param obj: :class:`.DatabaseNode` object
        
        """
        raise NotImplementedError, 'database_node_create is %s\'s responsibility' % (str(type (self)))
    #end database_node_create

    def database_node_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return database-node information.
        
        :param fq_name: Fully qualified name of database-node
        :param fq_name_str: Fully qualified name string of database-node
        :param id: UUID of database-node
        :param ifmap_id: IFMAP id of database-node
        :returns: :class:`.DatabaseNode` object
        
        """
        raise NotImplementedError, 'database_node_read is %s\'s responsibility' % (str(type (self)))
    #end database_node_read

    def database_node_update(self, obj):
        """Update database-node.
        
        :param obj: :class:`.DatabaseNode` object
        
        """
        raise NotImplementedError, 'database_node_update is %s\'s responsibility' % (str(type (self)))
    #end database_node_update

    def database_nodes_list(self, parent_id = None, parent_fq_name = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all database-nodes.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.DatabaseNode` objects
        
        """
        raise NotImplementedError, 'database_nodes_list is %s\'s responsibility' % (str(type (self)))
    #end database_nodes_list

    def database_node_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete database-node from the system.
        
        :param fq_name: Fully qualified name of database-node
        :param id: UUID of database-node
        :param ifmap_id: IFMAP id of database-node
        
        """
        raise NotImplementedError, 'database_node_delete is %s\'s responsibility' % (str(type (self)))
    #end database_node_delete

    def get_default_database_node_id(self):
        """Return UUID of default database-node."""
        raise NotImplementedError, 'get_default_database_node_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_database_node_delete

    def routing_instance_create(self, obj):
        """Create new routing-instance.
        
        :param obj: :class:`.RoutingInstance` object
        
        """
        raise NotImplementedError, 'routing_instance_create is %s\'s responsibility' % (str(type (self)))
    #end routing_instance_create

    def routing_instance_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return routing-instance information.
        
        :param fq_name: Fully qualified name of routing-instance
        :param fq_name_str: Fully qualified name string of routing-instance
        :param id: UUID of routing-instance
        :param ifmap_id: IFMAP id of routing-instance
        :returns: :class:`.RoutingInstance` object
        
        """
        raise NotImplementedError, 'routing_instance_read is %s\'s responsibility' % (str(type (self)))
    #end routing_instance_read

    def routing_instance_update(self, obj):
        """Update routing-instance.
        
        :param obj: :class:`.RoutingInstance` object
        
        """
        raise NotImplementedError, 'routing_instance_update is %s\'s responsibility' % (str(type (self)))
    #end routing_instance_update

    def routing_instances_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all routing-instances.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.RoutingInstance` objects
        
        """
        raise NotImplementedError, 'routing_instances_list is %s\'s responsibility' % (str(type (self)))
    #end routing_instances_list

    def routing_instance_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete routing-instance from the system.
        
        :param fq_name: Fully qualified name of routing-instance
        :param id: UUID of routing-instance
        :param ifmap_id: IFMAP id of routing-instance
        
        """
        raise NotImplementedError, 'routing_instance_delete is %s\'s responsibility' % (str(type (self)))
    #end routing_instance_delete

    def get_default_routing_instance_id(self):
        """Return UUID of default routing-instance."""
        raise NotImplementedError, 'get_default_routing_instance_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_routing_instance_delete

    def network_ipam_create(self, obj):
        """Create new network-ipam.
        
        :param obj: :class:`.NetworkIpam` object
        
        """
        raise NotImplementedError, 'network_ipam_create is %s\'s responsibility' % (str(type (self)))
    #end network_ipam_create

    def network_ipam_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return network-ipam information.
        
        :param fq_name: Fully qualified name of network-ipam
        :param fq_name_str: Fully qualified name string of network-ipam
        :param id: UUID of network-ipam
        :param ifmap_id: IFMAP id of network-ipam
        :returns: :class:`.NetworkIpam` object
        
        """
        raise NotImplementedError, 'network_ipam_read is %s\'s responsibility' % (str(type (self)))
    #end network_ipam_read

    def network_ipam_update(self, obj):
        """Update network-ipam.
        
        :param obj: :class:`.NetworkIpam` object
        
        """
        raise NotImplementedError, 'network_ipam_update is %s\'s responsibility' % (str(type (self)))
    #end network_ipam_update

    def network_ipams_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all network-ipams.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.NetworkIpam` objects
        
        """
        raise NotImplementedError, 'network_ipams_list is %s\'s responsibility' % (str(type (self)))
    #end network_ipams_list

    def network_ipam_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete network-ipam from the system.
        
        :param fq_name: Fully qualified name of network-ipam
        :param id: UUID of network-ipam
        :param ifmap_id: IFMAP id of network-ipam
        
        """
        raise NotImplementedError, 'network_ipam_delete is %s\'s responsibility' % (str(type (self)))
    #end network_ipam_delete

    def get_default_network_ipam_id(self):
        """Return UUID of default network-ipam."""
        raise NotImplementedError, 'get_default_network_ipam_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_network_ipam_delete

    def logical_router_create(self, obj):
        """Create new logical-router.
        
        :param obj: :class:`.LogicalRouter` object
        
        """
        raise NotImplementedError, 'logical_router_create is %s\'s responsibility' % (str(type (self)))
    #end logical_router_create

    def logical_router_read(self, fq_name = None, fq_name_str = None, id = None, ifmap_id = None):
        """Return logical-router information.
        
        :param fq_name: Fully qualified name of logical-router
        :param fq_name_str: Fully qualified name string of logical-router
        :param id: UUID of logical-router
        :param ifmap_id: IFMAP id of logical-router
        :returns: :class:`.LogicalRouter` object
        
        """
        raise NotImplementedError, 'logical_router_read is %s\'s responsibility' % (str(type (self)))
    #end logical_router_read

    def logical_router_update(self, obj):
        """Update logical-router.
        
        :param obj: :class:`.LogicalRouter` object
        
        """
        raise NotImplementedError, 'logical_router_update is %s\'s responsibility' % (str(type (self)))
    #end logical_router_update

    def logical_routers_list(self, parent_id = None, parent_fq_name = None, back_ref_id = None, obj_uuids = None, fields = None, detail = False, count = False):
        """List all logical-routers.
        
        :param parent_id: UUID of parent as optional search filter
        :param parent_fq_name: full qualified name of parent as optional search filter
        :returns: list of :class:`.LogicalRouter` objects
        
        """
        raise NotImplementedError, 'logical_routers_list is %s\'s responsibility' % (str(type (self)))
    #end logical_routers_list

    def logical_router_delete(self, fq_name = None, id = None, ifmap_id = None):
        """Delete logical-router from the system.
        
        :param fq_name: Fully qualified name of logical-router
        :param id: UUID of logical-router
        :param ifmap_id: IFMAP id of logical-router
        
        """
        raise NotImplementedError, 'logical_router_delete is %s\'s responsibility' % (str(type (self)))
    #end logical_router_delete

    def get_default_logical_router_id(self):
        """Return UUID of default logical-router."""
        raise NotImplementedError, 'get_default_logical_router_delete is %s\'s responsibility' % (str(type (self)))
    #end get_default_logical_router_delete

#end class ConnectionDriverBase

