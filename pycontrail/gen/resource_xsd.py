"""
This module defines the classes for types defined in :doc:`vnc_cfg.xsd`
"""
import json
from generatedssuper import *
class MacAddressesType(GeneratedsSuper):
    """
    MacAddressesType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, mac_address=None, **kwargs):
        if (mac_address is None) or (mac_address == []):
            self.mac_address = []
        else:
            self.mac_address = mac_address
    def factory(*args_, **kwargs_):
        if MacAddressesType.subclass:
            return MacAddressesType.subclass(*args_, **kwargs_)
        else:
            return MacAddressesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_mac_address(self): return self.mac_address
    def set_mac_address(self, mac_address): self.mac_address = mac_address
    def add_mac_address(self, value): self.mac_address.append(value)
    def insert_mac_address(self, index, value): self.mac_address[index] = value
    def delete_mac_address(self, value): self.mac_address.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.mac_address == other.mac_address)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_mac_address ([obj.populate_string ("mac_address")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='MacAddressesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MacAddressesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MacAddressesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='MacAddressesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for mac_address_ in self.mac_address:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smac-address>%s</%smac-address>%s' % (namespace_, self.gds_format_string(quote_xml(mac_address_).encode(ExternalEncoding), input_name='mac-address'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.mac_address
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='MacAddressesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('mac_address=[\n')
        level += 1
        for mac_address_ in self.mac_address:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(mac_address_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='MacAddressesType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'mac-address':
            mac_address_ = child_.text
            mac_address_ = self.gds_validate_string(mac_address_, node, 'mac_address')
            self.mac_address.append(mac_address_)
# end class MacAddressesType


class IpAddressesType(GeneratedsSuper):
    """
    IpAddressesType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, ip_address=None, **kwargs):
        if (ip_address is None) or (ip_address == []):
            self.ip_address = []
        else:
            self.ip_address = ip_address
    def factory(*args_, **kwargs_):
        if IpAddressesType.subclass:
            return IpAddressesType.subclass(*args_, **kwargs_)
        else:
            return IpAddressesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ip_address(self): return self.ip_address
    def set_ip_address(self, ip_address): self.ip_address = ip_address
    def add_ip_address(self, value): self.ip_address.append(value)
    def insert_ip_address(self, index, value): self.ip_address[index] = value
    def delete_ip_address(self, value): self.ip_address.remove(value)
    def validate_IpAddressType(self, value):
        # Validate type IpAddressType, a restriction on xsd:string.
        pass
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.ip_address == other.ip_address)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_ip_address ([obj.populate_string ("ip_address")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='IpAddressesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IpAddressesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IpAddressesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='IpAddressesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ip_address_ in self.ip_address:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sip-address>%s</%sip-address>%s' % (namespace_, self.gds_format_string(quote_xml(ip_address_).encode(ExternalEncoding), input_name='ip-address'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.ip_address
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IpAddressesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('ip_address=[\n')
        level += 1
        for ip_address_ in self.ip_address:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(ip_address_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='IpAddressesType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ip-address':
            ip_address_ = child_.text
            ip_address_ = self.gds_validate_string(ip_address_, node, 'ip_address')
            self.ip_address.append(ip_address_)
            self.validate_IpAddressType(self.ip_address)    # validate type IpAddressType
# end class IpAddressesType


class AllocationPoolType(GeneratedsSuper):
    """
    AllocationPoolType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, start=None, end=None, **kwargs):
        self.start = start
        self.end = end
    def factory(*args_, **kwargs_):
        if AllocationPoolType.subclass:
            return AllocationPoolType.subclass(*args_, **kwargs_)
        else:
            return AllocationPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_start(self): return self.start
    def set_start(self, start): self.start = start
    def get_end(self): return self.end
    def set_end(self, end): self.end = end
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.start == other.start and
                self.end == other.end)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_start (obj.populate_string ("start"))
        obj.set_end (obj.populate_string ("end"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AllocationPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AllocationPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AllocationPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AllocationPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.start is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstart>%s</%sstart>%s' % (namespace_, self.gds_format_string(quote_xml(self.start).encode(ExternalEncoding), input_name='start'), namespace_, eol_))
        if self.end is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%send>%s</%send>%s' % (namespace_, self.gds_format_string(quote_xml(self.end).encode(ExternalEncoding), input_name='end'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.start is not None or
            self.end is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AllocationPoolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.start is not None:
            showIndent(outfile, level)
            outfile.write('start=%s,\n' % quote_python(self.start).encode(ExternalEncoding))
        if self.end is not None:
            showIndent(outfile, level)
            outfile.write('end=%s,\n' % quote_python(self.end).encode(ExternalEncoding))
    def exportDict(self, name_='AllocationPoolType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'start':
            start_ = child_.text
            start_ = self.gds_validate_string(start_, node, 'start')
            self.start = start_
        elif nodeName_ == 'end':
            end_ = child_.text
            end_ = self.gds_validate_string(end_, node, 'end')
            self.end = end_
# end class AllocationPoolType


class SubnetType(GeneratedsSuper):
    """
    SubnetType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, ip_prefix=None, ip_prefix_len=None, **kwargs):
        self.ip_prefix = ip_prefix
        self.ip_prefix_len = ip_prefix_len
    def factory(*args_, **kwargs_):
        if SubnetType.subclass:
            return SubnetType.subclass(*args_, **kwargs_)
        else:
            return SubnetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ip_prefix(self): return self.ip_prefix
    def set_ip_prefix(self, ip_prefix): self.ip_prefix = ip_prefix
    def get_ip_prefix_len(self): return self.ip_prefix_len
    def set_ip_prefix_len(self, ip_prefix_len): self.ip_prefix_len = ip_prefix_len
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.ip_prefix == other.ip_prefix and
                self.ip_prefix_len == other.ip_prefix_len)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_ip_prefix (obj.populate_string ("ip_prefix"))
        obj.set_ip_prefix_len (obj.populate_integer ("ip_prefix_len"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='SubnetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SubnetType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SubnetType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='SubnetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ip_prefix is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sip-prefix>%s</%sip-prefix>%s' % (namespace_, self.gds_format_string(quote_xml(self.ip_prefix).encode(ExternalEncoding), input_name='ip-prefix'), namespace_, eol_))
        if self.ip_prefix_len is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sip-prefix-len>%s</%sip-prefix-len>%s' % (namespace_, self.gds_format_integer(self.ip_prefix_len, input_name='ip-prefix-len'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.ip_prefix is not None or
            self.ip_prefix_len is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='SubnetType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ip_prefix is not None:
            showIndent(outfile, level)
            outfile.write('ip_prefix=%s,\n' % quote_python(self.ip_prefix).encode(ExternalEncoding))
        if self.ip_prefix_len is not None:
            showIndent(outfile, level)
            outfile.write('ip_prefix_len=%d,\n' % self.ip_prefix_len)
    def exportDict(self, name_='SubnetType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ip-prefix':
            ip_prefix_ = child_.text
            ip_prefix_ = self.gds_validate_string(ip_prefix_, node, 'ip_prefix')
            self.ip_prefix = ip_prefix_
        elif nodeName_ == 'ip-prefix-len':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'ip_prefix_len')
            self.ip_prefix_len = ival_
# end class SubnetType


class AllowedAddressPair(GeneratedsSuper):
    """
    AllowedAddressPair class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, ip=None, mac=None, address_mode=None, **kwargs):
        if isinstance(ip, dict):
            obj = SubnetType(**ip)
            self.ip = obj
        else:
            self.ip = ip
        self.mac = mac
        self.address_mode = address_mode
    def factory(*args_, **kwargs_):
        if AllowedAddressPair.subclass:
            return AllowedAddressPair.subclass(*args_, **kwargs_)
        else:
            return AllowedAddressPair(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ip(self): return self.ip
    def set_ip(self, ip): self.ip = ip
    def get_mac(self): return self.mac
    def set_mac(self, mac): self.mac = mac
    def get_address_mode(self): return self.address_mode
    def set_address_mode(self, address_mode): self.address_mode = address_mode
    def validate_AddressMode(self, value):
        # Validate type AddressMode, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'active-active', u'active-standby'])
        else:
            error = value not in [u'active-active', u'active-standby']
        if error:
            raise ValueError("AddressMode must be one of [u'active-active', u'active-standby']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.ip == other.ip and
                self.mac == other.mac and
                self.address_mode == other.address_mode)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_ip (SubnetType.populate ())
        obj.set_mac (obj.populate_string ("mac"))
        obj.set_address_mode (obj.populate_string ("address_mode"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AllowedAddressPair', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AllowedAddressPair')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AllowedAddressPair'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AllowedAddressPair', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ip is not None:
            self.ip.export(outfile, level, namespace_, name_='ip', pretty_print=pretty_print)
        if self.mac is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smac>%s</%smac>%s' % (namespace_, self.gds_format_string(quote_xml(self.mac).encode(ExternalEncoding), input_name='mac'), namespace_, eol_))
        if self.address_mode is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress-mode>%s</%saddress-mode>%s' % (namespace_, self.gds_format_string(quote_xml(self.address_mode).encode(ExternalEncoding), input_name='address-mode'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.ip is not None or
            self.mac is not None or
            self.address_mode is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AllowedAddressPair'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ip is not None:
            showIndent(outfile, level)
            outfile.write('ip=model_.SubnetType(\n')
            self.ip.exportLiteral(outfile, level, name_='ip')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.mac is not None:
            showIndent(outfile, level)
            outfile.write('mac=%s,\n' % quote_python(self.mac).encode(ExternalEncoding))
        if self.address_mode is not None:
            showIndent(outfile, level)
            outfile.write('address_mode=%s,\n' % quote_python(self.address_mode).encode(ExternalEncoding))
    def exportDict(self, name_='AllowedAddressPair'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ip':
            obj_ = SubnetType.factory()
            obj_.build(child_)
            self.set_ip(obj_)
        elif nodeName_ == 'mac':
            mac_ = child_.text
            mac_ = self.gds_validate_string(mac_, node, 'mac')
            self.mac = mac_
        elif nodeName_ == 'address-mode':
            address_mode_ = child_.text
            address_mode_ = self.gds_validate_string(address_mode_, node, 'address_mode')
            self.address_mode = address_mode_
            self.validate_AddressMode(self.address_mode)    # validate type AddressMode
# end class AllowedAddressPair


class AllowedAddressPairs(GeneratedsSuper):
    """
    AllowedAddressPairs class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, allowed_address_pair=None, **kwargs):
        if (allowed_address_pair is None) or (allowed_address_pair == []):
            self.allowed_address_pair = []
        else:
            if isinstance(allowed_address_pair[0], dict):
                objs = [AllowedAddressPair(**elem) for elem in allowed_address_pair]
                self.allowed_address_pair = objs
            else:
                self.allowed_address_pair = allowed_address_pair
    def factory(*args_, **kwargs_):
        if AllowedAddressPairs.subclass:
            return AllowedAddressPairs.subclass(*args_, **kwargs_)
        else:
            return AllowedAddressPairs(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_allowed_address_pair(self): return self.allowed_address_pair
    def set_allowed_address_pair(self, allowed_address_pair): self.allowed_address_pair = allowed_address_pair
    def add_allowed_address_pair(self, value): self.allowed_address_pair.append(value)
    def insert_allowed_address_pair(self, index, value): self.allowed_address_pair[index] = value
    def delete_allowed_address_pair(self, value): self.allowed_address_pair.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.allowed_address_pair == other.allowed_address_pair)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_allowed_address_pair ([AllowedAddressPair.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AllowedAddressPairs', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AllowedAddressPairs')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AllowedAddressPairs'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AllowedAddressPairs', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for allowed_address_pair_ in self.allowed_address_pair:
            if isinstance(allowed_address_pair_, dict):
                allowed_address_pair_ = AllowedAddressPair(**allowed_address_pair_)
            allowed_address_pair_.export(outfile, level, namespace_, name_='allowed-address-pair', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.allowed_address_pair
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AllowedAddressPairs'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('allowed_address_pair=[\n')
        level += 1
        for allowed_address_pair_ in self.allowed_address_pair:
            showIndent(outfile, level)
            outfile.write('model_.AllowedAddressPair(\n')
            allowed_address_pair_.exportLiteral(outfile, level, name_='AllowedAddressPair')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='AllowedAddressPairs'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'allowed-address-pair':
            obj_ = AllowedAddressPair.factory()
            obj_.build(child_)
            self.allowed_address_pair.append(obj_)
# end class AllowedAddressPairs


class UuidType(GeneratedsSuper):
    """
    UuidType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, uuid_mslong=None, uuid_lslong=None, **kwargs):
        self.uuid_mslong = uuid_mslong
        self.uuid_lslong = uuid_lslong
    def factory(*args_, **kwargs_):
        if UuidType.subclass:
            return UuidType.subclass(*args_, **kwargs_)
        else:
            return UuidType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_uuid_mslong(self): return self.uuid_mslong
    def set_uuid_mslong(self, uuid_mslong): self.uuid_mslong = uuid_mslong
    def get_uuid_lslong(self): return self.uuid_lslong
    def set_uuid_lslong(self, uuid_lslong): self.uuid_lslong = uuid_lslong
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.uuid_mslong == other.uuid_mslong and
                self.uuid_lslong == other.uuid_lslong)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_uuid_mslong (obj.populate_unsignedLong ("uuid_mslong"))
        obj.set_uuid_lslong (obj.populate_unsignedLong ("uuid_lslong"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='UuidType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UuidType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='UuidType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='UuidType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.uuid_mslong is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suuid-mslong>%s</%suuid-mslong>%s' % (namespace_, self.gds_format_integer(self.uuid_mslong, input_name='uuid-mslong'), namespace_, eol_))
        if self.uuid_lslong is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suuid-lslong>%s</%suuid-lslong>%s' % (namespace_, self.gds_format_integer(self.uuid_lslong, input_name='uuid-lslong'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.uuid_mslong is not None or
            self.uuid_lslong is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='UuidType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.uuid_mslong is not None:
            showIndent(outfile, level)
            outfile.write('uuid_mslong=%d,\n' % self.uuid_mslong)
        if self.uuid_lslong is not None:
            showIndent(outfile, level)
            outfile.write('uuid_lslong=%d,\n' % self.uuid_lslong)
    def exportDict(self, name_='UuidType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'uuid-mslong':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'uuid_mslong')
            self.uuid_mslong = ival_
        elif nodeName_ == 'uuid-lslong':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'uuid_lslong')
            self.uuid_lslong = ival_
# end class UuidType


class SequenceType(GeneratedsSuper):
    """
    SequenceType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, major=None, minor=None, **kwargs):
        self.major = major
        self.minor = minor
    def factory(*args_, **kwargs_):
        if SequenceType.subclass:
            return SequenceType.subclass(*args_, **kwargs_)
        else:
            return SequenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_major(self): return self.major
    def set_major(self, major): self.major = major
    def get_minor(self): return self.minor
    def set_minor(self, minor): self.minor = minor
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.major == other.major and
                self.minor == other.minor)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_major (obj.populate_integer ("major"))
        obj.set_minor (obj.populate_integer ("minor"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='SequenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SequenceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SequenceType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='SequenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.major is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smajor>%s</%smajor>%s' % (namespace_, self.gds_format_integer(self.major, input_name='major'), namespace_, eol_))
        if self.minor is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sminor>%s</%sminor>%s' % (namespace_, self.gds_format_integer(self.minor, input_name='minor'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.major is not None or
            self.minor is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='SequenceType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.major is not None:
            showIndent(outfile, level)
            outfile.write('major=%d,\n' % self.major)
        if self.minor is not None:
            showIndent(outfile, level)
            outfile.write('minor=%d,\n' % self.minor)
    def exportDict(self, name_='SequenceType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'major':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'major')
            self.major = ival_
        elif nodeName_ == 'minor':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'minor')
            self.minor = ival_
# end class SequenceType


class TimerType(GeneratedsSuper):
    """
    TimerType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, start_time=None, on_interval=None, off_interval=None, end_time=None, **kwargs):
        self.start_time = start_time
        self.on_interval = on_interval
        self.off_interval = off_interval
        self.end_time = end_time
    def factory(*args_, **kwargs_):
        if TimerType.subclass:
            return TimerType.subclass(*args_, **kwargs_)
        else:
            return TimerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_start_time(self): return self.start_time
    def set_start_time(self, start_time): self.start_time = start_time
    def get_on_interval(self): return self.on_interval
    def set_on_interval(self, on_interval): self.on_interval = on_interval
    def get_off_interval(self): return self.off_interval
    def set_off_interval(self, off_interval): self.off_interval = off_interval
    def get_end_time(self): return self.end_time
    def set_end_time(self, end_time): self.end_time = end_time
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.start_time == other.start_time and
                self.on_interval == other.on_interval and
                self.off_interval == other.off_interval and
                self.end_time == other.end_time)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_start_time (obj.populate_dateTime ("start_time"))
        obj.set_on_interval (obj.populate_time ("on_interval"))
        obj.set_off_interval (obj.populate_time ("off_interval"))
        obj.set_end_time (obj.populate_dateTime ("end_time"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='TimerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='TimerType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='TimerType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='TimerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.start_time is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstart-time>%s</%sstart-time>%s' % (namespace_, self.gds_format_string(quote_xml(self.start_time).encode(ExternalEncoding), input_name='start-time'), namespace_, eol_))
        if self.on_interval is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%son-interval>%s</%son-interval>%s' % (namespace_, self.gds_format_string(quote_xml(self.on_interval).encode(ExternalEncoding), input_name='on-interval'), namespace_, eol_))
        if self.off_interval is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%soff-interval>%s</%soff-interval>%s' % (namespace_, self.gds_format_string(quote_xml(self.off_interval).encode(ExternalEncoding), input_name='off-interval'), namespace_, eol_))
        if self.end_time is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%send-time>%s</%send-time>%s' % (namespace_, self.gds_format_string(quote_xml(self.end_time).encode(ExternalEncoding), input_name='end-time'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.start_time is not None or
            self.on_interval is not None or
            self.off_interval is not None or
            self.end_time is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='TimerType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.start_time is not None:
            showIndent(outfile, level)
            outfile.write('start_time=%s,\n' % quote_python(self.start_time).encode(ExternalEncoding))
        if self.on_interval is not None:
            showIndent(outfile, level)
            outfile.write('on_interval=%s,\n' % quote_python(self.on_interval).encode(ExternalEncoding))
        if self.off_interval is not None:
            showIndent(outfile, level)
            outfile.write('off_interval=%s,\n' % quote_python(self.off_interval).encode(ExternalEncoding))
        if self.end_time is not None:
            showIndent(outfile, level)
            outfile.write('end_time=%s,\n' % quote_python(self.end_time).encode(ExternalEncoding))
    def exportDict(self, name_='TimerType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'start-time':
            start_time_ = child_.text
            start_time_ = self.gds_validate_string(start_time_, node, 'start_time')
            self.start_time = start_time_
        elif nodeName_ == 'on-interval':
            on_interval_ = child_.text
            on_interval_ = self.gds_validate_string(on_interval_, node, 'on_interval')
            self.on_interval = on_interval_
        elif nodeName_ == 'off-interval':
            off_interval_ = child_.text
            off_interval_ = self.gds_validate_string(off_interval_, node, 'off_interval')
            self.off_interval = off_interval_
        elif nodeName_ == 'end-time':
            end_time_ = child_.text
            end_time_ = self.gds_validate_string(end_time_, node, 'end_time')
            self.end_time = end_time_
# end class TimerType


class VirtualNetworkPolicyType(GeneratedsSuper):
    """
    VirtualNetworkPolicyType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, sequence=None, timer=None, **kwargs):
        if isinstance(sequence, dict):
            obj = SequenceType(**sequence)
            self.sequence = obj
        else:
            self.sequence = sequence
        if isinstance(timer, dict):
            obj = TimerType(**timer)
            self.timer = obj
        else:
            self.timer = timer
    def factory(*args_, **kwargs_):
        if VirtualNetworkPolicyType.subclass:
            return VirtualNetworkPolicyType.subclass(*args_, **kwargs_)
        else:
            return VirtualNetworkPolicyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_sequence(self): return self.sequence
    def set_sequence(self, sequence): self.sequence = sequence
    def get_timer(self): return self.timer
    def set_timer(self, timer): self.timer = timer
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.sequence == other.sequence and
                self.timer == other.timer)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_sequence (SequenceType.populate ())
        obj.set_timer (TimerType.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VirtualNetworkPolicyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VirtualNetworkPolicyType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VirtualNetworkPolicyType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VirtualNetworkPolicyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.sequence is not None:
            self.sequence.export(outfile, level, namespace_, name_='sequence', pretty_print=pretty_print)
        if self.timer is not None:
            self.timer.export(outfile, level, namespace_, name_='timer', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.sequence is not None or
            self.timer is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VirtualNetworkPolicyType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.sequence is not None:
            showIndent(outfile, level)
            outfile.write('sequence=model_.SequenceType(\n')
            self.sequence.exportLiteral(outfile, level, name_='sequence')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.timer is not None:
            showIndent(outfile, level)
            outfile.write('timer=model_.TimerType(\n')
            self.timer.exportLiteral(outfile, level, name_='timer')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='VirtualNetworkPolicyType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'sequence':
            obj_ = SequenceType.factory()
            obj_.build(child_)
            self.set_sequence(obj_)
        elif nodeName_ == 'timer':
            obj_ = TimerType.factory()
            obj_.build(child_)
            self.set_timer(obj_)
# end class VirtualNetworkPolicyType


class AddressType(GeneratedsSuper):
    """
    AddressType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, subnet=None, virtual_network=None, security_group=None, network_policy=None, **kwargs):
        if isinstance(subnet, dict):
            obj = SubnetType(**subnet)
            self.subnet = obj
        else:
            self.subnet = subnet
        self.virtual_network = virtual_network
        self.security_group = security_group
        self.network_policy = network_policy
    def factory(*args_, **kwargs_):
        if AddressType.subclass:
            return AddressType.subclass(*args_, **kwargs_)
        else:
            return AddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_subnet(self): return self.subnet
    def set_subnet(self, subnet): self.subnet = subnet
    def get_virtual_network(self): return self.virtual_network
    def set_virtual_network(self, virtual_network): self.virtual_network = virtual_network
    def get_security_group(self): return self.security_group
    def set_security_group(self, security_group): self.security_group = security_group
    def get_network_policy(self): return self.network_policy
    def set_network_policy(self, network_policy): self.network_policy = network_policy
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.subnet == other.subnet and
                self.virtual_network == other.virtual_network and
                self.security_group == other.security_group and
                self.network_policy == other.network_policy)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_subnet (SubnetType.populate ())
        obj.set_virtual_network (obj.populate_string ("virtual_network"))
        obj.set_security_group (obj.populate_string ("security_group"))
        obj.set_network_policy (obj.populate_string ("network_policy"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AddressType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AddressType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AddressType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.subnet is not None:
            self.subnet.export(outfile, level, namespace_, name_='subnet', pretty_print=pretty_print)
        if self.virtual_network is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-network>%s</%svirtual-network>%s' % (namespace_, self.gds_format_string(quote_xml(self.virtual_network).encode(ExternalEncoding), input_name='virtual-network'), namespace_, eol_))
        if self.security_group is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssecurity-group>%s</%ssecurity-group>%s' % (namespace_, self.gds_format_string(quote_xml(self.security_group).encode(ExternalEncoding), input_name='security-group'), namespace_, eol_))
        if self.network_policy is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snetwork-policy>%s</%snetwork-policy>%s' % (namespace_, self.gds_format_string(quote_xml(self.network_policy).encode(ExternalEncoding), input_name='network-policy'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.subnet is not None or
            self.virtual_network is not None or
            self.security_group is not None or
            self.network_policy is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AddressType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.subnet is not None:
            showIndent(outfile, level)
            outfile.write('subnet=model_.SubnetType(\n')
            self.subnet.exportLiteral(outfile, level, name_='subnet')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.virtual_network is not None:
            showIndent(outfile, level)
            outfile.write('virtual_network=%s,\n' % quote_python(self.virtual_network).encode(ExternalEncoding))
        if self.security_group is not None:
            showIndent(outfile, level)
            outfile.write('security_group=%s,\n' % quote_python(self.security_group).encode(ExternalEncoding))
        if self.network_policy is not None:
            showIndent(outfile, level)
            outfile.write('network_policy=%s,\n' % quote_python(self.network_policy).encode(ExternalEncoding))
    def exportDict(self, name_='AddressType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'subnet':
            obj_ = SubnetType.factory()
            obj_.build(child_)
            self.set_subnet(obj_)
        elif nodeName_ == 'virtual-network':
            virtual_network_ = child_.text
            virtual_network_ = self.gds_validate_string(virtual_network_, node, 'virtual_network')
            self.virtual_network = virtual_network_
        elif nodeName_ == 'security-group':
            security_group_ = child_.text
            security_group_ = self.gds_validate_string(security_group_, node, 'security_group')
            self.security_group = security_group_
        elif nodeName_ == 'network-policy':
            network_policy_ = child_.text
            network_policy_ = self.gds_validate_string(network_policy_, node, 'network_policy')
            self.network_policy = network_policy_
# end class AddressType


class PortType(GeneratedsSuper):
    """
    PortType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, start_port=None, end_port=None, **kwargs):
        self.start_port = start_port
        self.end_port = end_port
    def factory(*args_, **kwargs_):
        if PortType.subclass:
            return PortType.subclass(*args_, **kwargs_)
        else:
            return PortType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_start_port(self): return self.start_port
    def set_start_port(self, start_port): self.start_port = start_port
    def validate_L4PortType(self, value):
        # Validate type L4PortType, a restriction on xsd:integer.
        error = False
        if isinstance(value, list):
            v_int = map(int, value)
            v1, v2 = min(v_int), max(v_int)
        else:
            v1, v2 = int(value), int(value)
        error = (-1 > v1)
        error |= (v2 > 65535)
        if error:
            raise ValueError("L4PortType must be in the range -1-65535")
    def get_end_port(self): return self.end_port
    def set_end_port(self, end_port): self.end_port = end_port
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.start_port == other.start_port and
                self.end_port == other.end_port)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_start_port (obj.populate_integer ("start_port"))
        obj.set_end_port (obj.populate_integer ("end_port"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='PortType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PortType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PortType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PortType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.start_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstart-port>%s</%sstart-port>%s' % (namespace_, self.gds_format_integer(self.start_port, input_name='start-port'), namespace_, eol_))
        if self.end_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%send-port>%s</%send-port>%s' % (namespace_, self.gds_format_integer(self.end_port, input_name='end-port'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.start_port is not None or
            self.end_port is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PortType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.start_port is not None:
            showIndent(outfile, level)
            outfile.write('start_port=%d,\n' % self.start_port)
        if self.end_port is not None:
            showIndent(outfile, level)
            outfile.write('end_port=%d,\n' % self.end_port)
    def exportDict(self, name_='PortType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'start-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'start_port')
            self.start_port = ival_
            self.validate_L4PortType(self.start_port)    # validate type L4PortType
        elif nodeName_ == 'end-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'end_port')
            self.end_port = ival_
            self.validate_L4PortType(self.end_port)    # validate type L4PortType
# end class PortType


class MatchConditionType(GeneratedsSuper):
    """
    MatchConditionType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, protocol=None, src_address=None, src_port=None, dst_address=None, dst_port=None, ethertype=None, **kwargs):
        self.protocol = protocol
        if isinstance(src_address, dict):
            obj = AddressType(**src_address)
            self.src_address = obj
        else:
            self.src_address = src_address
        if isinstance(src_port, dict):
            obj = PortType(**src_port)
            self.src_port = obj
        else:
            self.src_port = src_port
        if isinstance(dst_address, dict):
            obj = AddressType(**dst_address)
            self.dst_address = obj
        else:
            self.dst_address = dst_address
        if isinstance(dst_port, dict):
            obj = PortType(**dst_port)
            self.dst_port = obj
        else:
            self.dst_port = dst_port
        self.ethertype = ethertype
    def factory(*args_, **kwargs_):
        if MatchConditionType.subclass:
            return MatchConditionType.subclass(*args_, **kwargs_)
        else:
            return MatchConditionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_protocol(self): return self.protocol
    def set_protocol(self, protocol): self.protocol = protocol
    def get_src_address(self): return self.src_address
    def set_src_address(self, src_address): self.src_address = src_address
    def get_src_port(self): return self.src_port
    def set_src_port(self, src_port): self.src_port = src_port
    def get_dst_address(self): return self.dst_address
    def set_dst_address(self, dst_address): self.dst_address = dst_address
    def get_dst_port(self): return self.dst_port
    def set_dst_port(self, dst_port): self.dst_port = dst_port
    def get_ethertype(self): return self.ethertype
    def set_ethertype(self, ethertype): self.ethertype = ethertype
    def validate_EtherType(self, value):
        # Validate type EtherType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'IPv4', u'IPv6'])
        else:
            error = value not in [u'IPv4', u'IPv6']
        if error:
            raise ValueError("EtherType must be one of [u'IPv4', u'IPv6']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.protocol == other.protocol and
                self.src_address == other.src_address and
                self.src_port == other.src_port and
                self.dst_address == other.dst_address and
                self.dst_port == other.dst_port and
                self.ethertype == other.ethertype)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_protocol (obj.populate_string ("protocol"))
        obj.set_src_address (AddressType.populate ())
        obj.set_src_port (PortType.populate ())
        obj.set_dst_address (AddressType.populate ())
        obj.set_dst_port (PortType.populate ())
        obj.set_ethertype (obj.populate_string ("ethertype"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='MatchConditionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MatchConditionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MatchConditionType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='MatchConditionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.protocol is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprotocol>%s</%sprotocol>%s' % (namespace_, self.gds_format_string(quote_xml(self.protocol).encode(ExternalEncoding), input_name='protocol'), namespace_, eol_))
        if self.src_address is not None:
            self.src_address.export(outfile, level, namespace_, name_='src-address', pretty_print=pretty_print)
        if self.src_port is not None:
            self.src_port.export(outfile, level, namespace_, name_='src-port', pretty_print=pretty_print)
        if self.dst_address is not None:
            self.dst_address.export(outfile, level, namespace_, name_='dst-address', pretty_print=pretty_print)
        if self.dst_port is not None:
            self.dst_port.export(outfile, level, namespace_, name_='dst-port', pretty_print=pretty_print)
        if self.ethertype is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sethertype>%s</%sethertype>%s' % (namespace_, self.gds_format_string(quote_xml(self.ethertype).encode(ExternalEncoding), input_name='ethertype'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.protocol is not None or
            self.src_address is not None or
            self.src_port is not None or
            self.dst_address is not None or
            self.dst_port is not None or
            self.ethertype is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='MatchConditionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.protocol is not None:
            showIndent(outfile, level)
            outfile.write('protocol=%s,\n' % quote_python(self.protocol).encode(ExternalEncoding))
        if self.src_address is not None:
            showIndent(outfile, level)
            outfile.write('src_address=model_.AddressType(\n')
            self.src_address.exportLiteral(outfile, level, name_='src_address')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.src_port is not None:
            showIndent(outfile, level)
            outfile.write('src_port=model_.PortType(\n')
            self.src_port.exportLiteral(outfile, level, name_='src_port')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dst_address is not None:
            showIndent(outfile, level)
            outfile.write('dst_address=model_.AddressType(\n')
            self.dst_address.exportLiteral(outfile, level, name_='dst_address')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dst_port is not None:
            showIndent(outfile, level)
            outfile.write('dst_port=model_.PortType(\n')
            self.dst_port.exportLiteral(outfile, level, name_='dst_port')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ethertype is not None:
            showIndent(outfile, level)
            outfile.write('ethertype=%s,\n' % quote_python(self.ethertype).encode(ExternalEncoding))
    def exportDict(self, name_='MatchConditionType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'protocol':
            protocol_ = child_.text
            protocol_ = self.gds_validate_string(protocol_, node, 'protocol')
            self.protocol = protocol_
        elif nodeName_ == 'src-address':
            obj_ = AddressType.factory()
            obj_.build(child_)
            self.set_src_address(obj_)
        elif nodeName_ == 'src-port':
            obj_ = PortType.factory()
            obj_.build(child_)
            self.set_src_port(obj_)
        elif nodeName_ == 'dst-address':
            obj_ = AddressType.factory()
            obj_.build(child_)
            self.set_dst_address(obj_)
        elif nodeName_ == 'dst-port':
            obj_ = PortType.factory()
            obj_.build(child_)
            self.set_dst_port(obj_)
        elif nodeName_ == 'ethertype':
            ethertype_ = child_.text
            ethertype_ = self.gds_validate_string(ethertype_, node, 'ethertype')
            self.ethertype = ethertype_
            self.validate_EtherType(self.ethertype)    # validate type EtherType
# end class MatchConditionType


class MirrorActionType(GeneratedsSuper):
    """
    MirrorActionType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, analyzer_name=None, encapsulation=None, analyzer_ip_address=None, routing_instance=None, udp_port=None, **kwargs):
        self.analyzer_name = analyzer_name
        self.encapsulation = encapsulation
        self.analyzer_ip_address = analyzer_ip_address
        self.routing_instance = routing_instance
        self.udp_port = udp_port
    def factory(*args_, **kwargs_):
        if MirrorActionType.subclass:
            return MirrorActionType.subclass(*args_, **kwargs_)
        else:
            return MirrorActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_analyzer_name(self): return self.analyzer_name
    def set_analyzer_name(self, analyzer_name): self.analyzer_name = analyzer_name
    def get_encapsulation(self): return self.encapsulation
    def set_encapsulation(self, encapsulation): self.encapsulation = encapsulation
    def get_analyzer_ip_address(self): return self.analyzer_ip_address
    def set_analyzer_ip_address(self, analyzer_ip_address): self.analyzer_ip_address = analyzer_ip_address
    def validate_IpAddress(self, value):
        # Validate type IpAddress, a restriction on xsd:string.
        pass
    def get_routing_instance(self): return self.routing_instance
    def set_routing_instance(self, routing_instance): self.routing_instance = routing_instance
    def get_udp_port(self): return self.udp_port
    def set_udp_port(self, udp_port): self.udp_port = udp_port
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.analyzer_name == other.analyzer_name and
                self.encapsulation == other.encapsulation and
                self.analyzer_ip_address == other.analyzer_ip_address and
                self.routing_instance == other.routing_instance and
                self.udp_port == other.udp_port)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_analyzer_name (obj.populate_string ("analyzer_name"))
        obj.set_encapsulation (obj.populate_string ("encapsulation"))
        obj.set_analyzer_ip_address (obj.populate_string ("analyzer_ip_address"))
        obj.set_routing_instance (obj.populate_string ("routing_instance"))
        obj.set_udp_port (obj.populate_integer ("udp_port"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='MirrorActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='MirrorActionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='MirrorActionType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='MirrorActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.analyzer_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sanalyzer-name>%s</%sanalyzer-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.analyzer_name).encode(ExternalEncoding), input_name='analyzer-name'), namespace_, eol_))
        if self.encapsulation is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sencapsulation>%s</%sencapsulation>%s' % (namespace_, self.gds_format_string(quote_xml(self.encapsulation).encode(ExternalEncoding), input_name='encapsulation'), namespace_, eol_))
        if self.analyzer_ip_address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sanalyzer-ip-address>%s</%sanalyzer-ip-address>%s' % (namespace_, self.gds_format_string(quote_xml(self.analyzer_ip_address).encode(ExternalEncoding), input_name='analyzer-ip-address'), namespace_, eol_))
        if self.routing_instance is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srouting-instance>%s</%srouting-instance>%s' % (namespace_, self.gds_format_string(quote_xml(self.routing_instance).encode(ExternalEncoding), input_name='routing-instance'), namespace_, eol_))
        if self.udp_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sudp-port>%s</%sudp-port>%s' % (namespace_, self.gds_format_integer(self.udp_port, input_name='udp-port'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.analyzer_name is not None or
            self.encapsulation is not None or
            self.analyzer_ip_address is not None or
            self.routing_instance is not None or
            self.udp_port is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='MirrorActionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.analyzer_name is not None:
            showIndent(outfile, level)
            outfile.write('analyzer_name=%s,\n' % quote_python(self.analyzer_name).encode(ExternalEncoding))
        if self.encapsulation is not None:
            showIndent(outfile, level)
            outfile.write('encapsulation=%s,\n' % quote_python(self.encapsulation).encode(ExternalEncoding))
        if self.analyzer_ip_address is not None:
            showIndent(outfile, level)
            outfile.write('analyzer_ip_address=%s,\n' % quote_python(self.analyzer_ip_address).encode(ExternalEncoding))
        if self.routing_instance is not None:
            showIndent(outfile, level)
            outfile.write('routing_instance=%s,\n' % quote_python(self.routing_instance).encode(ExternalEncoding))
        if self.udp_port is not None:
            showIndent(outfile, level)
            outfile.write('udp_port=%d,\n' % self.udp_port)
    def exportDict(self, name_='MirrorActionType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'analyzer-name':
            analyzer_name_ = child_.text
            analyzer_name_ = self.gds_validate_string(analyzer_name_, node, 'analyzer_name')
            self.analyzer_name = analyzer_name_
        elif nodeName_ == 'encapsulation':
            encapsulation_ = child_.text
            encapsulation_ = self.gds_validate_string(encapsulation_, node, 'encapsulation')
            self.encapsulation = encapsulation_
        elif nodeName_ == 'analyzer-ip-address':
            analyzer_ip_address_ = child_.text
            analyzer_ip_address_ = self.gds_validate_string(analyzer_ip_address_, node, 'analyzer_ip_address')
            self.analyzer_ip_address = analyzer_ip_address_
            self.validate_IpAddress(self.analyzer_ip_address)    # validate type IpAddress
        elif nodeName_ == 'routing-instance':
            routing_instance_ = child_.text
            routing_instance_ = self.gds_validate_string(routing_instance_, node, 'routing_instance')
            self.routing_instance = routing_instance_
        elif nodeName_ == 'udp-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'udp_port')
            self.udp_port = ival_
# end class MirrorActionType


class ActionListType(GeneratedsSuper):
    """
    ActionListType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, simple_action=None, gateway_name=None, apply_service=None, mirror_to=None, assign_routing_instance=None, **kwargs):
        self.simple_action = simple_action
        self.gateway_name = gateway_name
        if (apply_service is None) or (apply_service == []):
            self.apply_service = []
        else:
            self.apply_service = apply_service
        if isinstance(mirror_to, dict):
            obj = MirrorActionType(**mirror_to)
            self.mirror_to = obj
        else:
            self.mirror_to = mirror_to
        self.assign_routing_instance = assign_routing_instance
    def factory(*args_, **kwargs_):
        if ActionListType.subclass:
            return ActionListType.subclass(*args_, **kwargs_)
        else:
            return ActionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_simple_action(self): return self.simple_action
    def set_simple_action(self, simple_action): self.simple_action = simple_action
    def validate_SimpleActionType(self, value):
        # Validate type SimpleActionType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'alert', u'drop', u'deny', u'log', u'pass', u'reject'])
        else:
            error = value not in [u'alert', u'drop', u'deny', u'log', u'pass', u'reject']
        if error:
            raise ValueError("SimpleActionType must be one of [u'alert', u'drop', u'deny', u'log', u'pass', u'reject']")
    def get_gateway_name(self): return self.gateway_name
    def set_gateway_name(self, gateway_name): self.gateway_name = gateway_name
    def get_apply_service(self): return self.apply_service
    def set_apply_service(self, apply_service): self.apply_service = apply_service
    def add_apply_service(self, value): self.apply_service.append(value)
    def insert_apply_service(self, index, value): self.apply_service[index] = value
    def delete_apply_service(self, value): self.apply_service.remove(value)
    def get_mirror_to(self): return self.mirror_to
    def set_mirror_to(self, mirror_to): self.mirror_to = mirror_to
    def get_assign_routing_instance(self): return self.assign_routing_instance
    def set_assign_routing_instance(self, assign_routing_instance): self.assign_routing_instance = assign_routing_instance
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.simple_action == other.simple_action and
                self.gateway_name == other.gateway_name and
                self.apply_service == other.apply_service and
                self.mirror_to == other.mirror_to and
                self.assign_routing_instance == other.assign_routing_instance)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_simple_action (obj.populate_string ("simple_action"))
        obj.set_gateway_name (obj.populate_string ("gateway_name"))
        obj.set_apply_service ([obj.populate_string ("apply_service")])
        obj.set_mirror_to (MirrorActionType.populate ())
        obj.set_assign_routing_instance (obj.populate_string ("assign_routing_instance"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ActionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ActionListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ActionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.simple_action is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssimple-action>%s</%ssimple-action>%s' % (namespace_, self.gds_format_string(quote_xml(self.simple_action).encode(ExternalEncoding), input_name='simple-action'), namespace_, eol_))
        if self.gateway_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgateway-name>%s</%sgateway-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.gateway_name).encode(ExternalEncoding), input_name='gateway-name'), namespace_, eol_))
        for apply_service_ in self.apply_service:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sapply-service>%s</%sapply-service>%s' % (namespace_, self.gds_format_string(quote_xml(apply_service_).encode(ExternalEncoding), input_name='apply-service'), namespace_, eol_))
        if self.mirror_to is not None:
            self.mirror_to.export(outfile, level, namespace_, name_='mirror-to', pretty_print=pretty_print)
        if self.assign_routing_instance is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sassign-routing-instance>%s</%sassign-routing-instance>%s' % (namespace_, self.gds_format_string(quote_xml(self.assign_routing_instance).encode(ExternalEncoding), input_name='assign-routing-instance'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.simple_action is not None or
            self.gateway_name is not None or
            self.apply_service or
            self.mirror_to is not None or
            self.assign_routing_instance is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.simple_action is not None:
            showIndent(outfile, level)
            outfile.write('simple_action=%s,\n' % quote_python(self.simple_action).encode(ExternalEncoding))
        if self.gateway_name is not None:
            showIndent(outfile, level)
            outfile.write('gateway_name=%s,\n' % quote_python(self.gateway_name).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('apply_service=[\n')
        level += 1
        for apply_service_ in self.apply_service:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(apply_service_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.mirror_to is not None:
            showIndent(outfile, level)
            outfile.write('mirror_to=model_.MirrorActionType(\n')
            self.mirror_to.exportLiteral(outfile, level, name_='mirror_to')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.assign_routing_instance is not None:
            showIndent(outfile, level)
            outfile.write('assign_routing_instance=%s,\n' % quote_python(self.assign_routing_instance).encode(ExternalEncoding))
    def exportDict(self, name_='ActionListType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'simple-action':
            simple_action_ = child_.text
            simple_action_ = self.gds_validate_string(simple_action_, node, 'simple_action')
            self.simple_action = simple_action_
            self.validate_SimpleActionType(self.simple_action)    # validate type SimpleActionType
        elif nodeName_ == 'gateway-name':
            gateway_name_ = child_.text
            gateway_name_ = self.gds_validate_string(gateway_name_, node, 'gateway_name')
            self.gateway_name = gateway_name_
        elif nodeName_ == 'apply-service':
            apply_service_ = child_.text
            apply_service_ = self.gds_validate_string(apply_service_, node, 'apply_service')
            self.apply_service.append(apply_service_)
        elif nodeName_ == 'mirror-to':
            obj_ = MirrorActionType.factory()
            obj_.build(child_)
            self.set_mirror_to(obj_)
        elif nodeName_ == 'assign-routing-instance':
            assign_routing_instance_ = child_.text
            assign_routing_instance_ = self.gds_validate_string(assign_routing_instance_, node, 'assign_routing_instance')
            self.assign_routing_instance = assign_routing_instance_
# end class ActionListType


class AclRuleType(GeneratedsSuper):
    """
    AclRuleType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, match_condition=None, action_list=None, rule_uuid=None, **kwargs):
        if isinstance(match_condition, dict):
            obj = MatchConditionType(**match_condition)
            self.match_condition = obj
        else:
            self.match_condition = match_condition
        if isinstance(action_list, dict):
            obj = ActionListType(**action_list)
            self.action_list = obj
        else:
            self.action_list = action_list
        self.rule_uuid = rule_uuid
    def factory(*args_, **kwargs_):
        if AclRuleType.subclass:
            return AclRuleType.subclass(*args_, **kwargs_)
        else:
            return AclRuleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_match_condition(self): return self.match_condition
    def set_match_condition(self, match_condition): self.match_condition = match_condition
    def get_action_list(self): return self.action_list
    def set_action_list(self, action_list): self.action_list = action_list
    def get_rule_uuid(self): return self.rule_uuid
    def set_rule_uuid(self, rule_uuid): self.rule_uuid = rule_uuid
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.match_condition == other.match_condition and
                self.action_list == other.action_list and
                self.rule_uuid == other.rule_uuid)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_match_condition (MatchConditionType.populate ())
        obj.set_action_list (ActionListType.populate ())
        obj.set_rule_uuid (obj.populate_string ("rule_uuid"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AclRuleType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AclRuleType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AclRuleType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AclRuleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.match_condition is not None:
            self.match_condition.export(outfile, level, namespace_, name_='match-condition', pretty_print=pretty_print)
        if self.action_list is not None:
            self.action_list.export(outfile, level, namespace_, name_='action-list', pretty_print=pretty_print)
        if self.rule_uuid is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srule-uuid>%s</%srule-uuid>%s' % (namespace_, self.gds_format_string(quote_xml(self.rule_uuid).encode(ExternalEncoding), input_name='rule-uuid'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.match_condition is not None or
            self.action_list is not None or
            self.rule_uuid is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AclRuleType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.match_condition is not None:
            showIndent(outfile, level)
            outfile.write('match_condition=model_.MatchConditionType(\n')
            self.match_condition.exportLiteral(outfile, level, name_='match_condition')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.action_list is not None:
            showIndent(outfile, level)
            outfile.write('action_list=model_.ActionListType(\n')
            self.action_list.exportLiteral(outfile, level, name_='action_list')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rule_uuid is not None:
            showIndent(outfile, level)
            outfile.write('rule_uuid=%s,\n' % quote_python(self.rule_uuid).encode(ExternalEncoding))
    def exportDict(self, name_='AclRuleType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'match-condition':
            obj_ = MatchConditionType.factory()
            obj_.build(child_)
            self.set_match_condition(obj_)
        elif nodeName_ == 'action-list':
            obj_ = ActionListType.factory()
            obj_.build(child_)
            self.set_action_list(obj_)
        elif nodeName_ == 'rule-uuid':
            rule_uuid_ = child_.text
            rule_uuid_ = self.gds_validate_string(rule_uuid_, node, 'rule_uuid')
            self.rule_uuid = rule_uuid_
# end class AclRuleType


class AclEntriesType(GeneratedsSuper):
    """
    AclEntriesType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, dynamic=None, acl_rule=None, **kwargs):
        self.dynamic = dynamic
        if (acl_rule is None) or (acl_rule == []):
            self.acl_rule = []
        else:
            if isinstance(acl_rule[0], dict):
                objs = [AclRuleType(**elem) for elem in acl_rule]
                self.acl_rule = objs
            else:
                self.acl_rule = acl_rule
    def factory(*args_, **kwargs_):
        if AclEntriesType.subclass:
            return AclEntriesType.subclass(*args_, **kwargs_)
        else:
            return AclEntriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_dynamic(self): return self.dynamic
    def set_dynamic(self, dynamic): self.dynamic = dynamic
    def get_acl_rule(self): return self.acl_rule
    def set_acl_rule(self, acl_rule): self.acl_rule = acl_rule
    def add_acl_rule(self, value): self.acl_rule.append(value)
    def insert_acl_rule(self, index, value): self.acl_rule[index] = value
    def delete_acl_rule(self, value): self.acl_rule.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.dynamic == other.dynamic and
                self.acl_rule == other.acl_rule)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_dynamic (obj.populate_boolean ("dynamic"))
        obj.set_acl_rule ([AclRuleType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AclEntriesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AclEntriesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AclEntriesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AclEntriesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dynamic is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdynamic>%s</%sdynamic>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.dynamic)), input_name='dynamic'), namespace_, eol_))
        for acl_rule_ in self.acl_rule:
            if isinstance(acl_rule_, dict):
                acl_rule_ = AclRuleType(**acl_rule_)
            acl_rule_.export(outfile, level, namespace_, name_='acl-rule', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.dynamic is not None or
            self.acl_rule
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AclEntriesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dynamic is not None:
            showIndent(outfile, level)
            outfile.write('dynamic=%s,\n' % self.dynamic)
        showIndent(outfile, level)
        outfile.write('acl_rule=[\n')
        level += 1
        for acl_rule_ in self.acl_rule:
            showIndent(outfile, level)
            outfile.write('model_.AclRuleType(\n')
            acl_rule_.exportLiteral(outfile, level, name_='AclRuleType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='AclEntriesType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'dynamic':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'dynamic')
            self.dynamic = ival_
        elif nodeName_ == 'acl-rule':
            obj_ = AclRuleType.factory()
            obj_.build(child_)
            self.acl_rule.append(obj_)
# end class AclEntriesType


class PolicyRuleType(GeneratedsSuper):
    """
    PolicyRuleType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, rule_sequence=None, rule_uuid=None, direction=None, protocol=None, src_addresses=None, src_ports=None, application=None, dst_addresses=None, dst_ports=None, action_list=None, ethertype=None, **kwargs):
        if isinstance(rule_sequence, dict):
            obj = SequenceType(**rule_sequence)
            self.rule_sequence = obj
        else:
            self.rule_sequence = rule_sequence
        self.rule_uuid = rule_uuid
        self.direction = direction
        self.protocol = protocol
        if (src_addresses is None) or (src_addresses == []):
            self.src_addresses = []
        else:
            if isinstance(src_addresses[0], dict):
                objs = [AddressType(**elem) for elem in src_addresses]
                self.src_addresses = objs
            else:
                self.src_addresses = src_addresses
        if (src_ports is None) or (src_ports == []):
            self.src_ports = []
        else:
            if isinstance(src_ports[0], dict):
                objs = [PortType(**elem) for elem in src_ports]
                self.src_ports = objs
            else:
                self.src_ports = src_ports
        if (application is None) or (application == []):
            self.application = []
        else:
            self.application = application
        if (dst_addresses is None) or (dst_addresses == []):
            self.dst_addresses = []
        else:
            if isinstance(dst_addresses[0], dict):
                objs = [AddressType(**elem) for elem in dst_addresses]
                self.dst_addresses = objs
            else:
                self.dst_addresses = dst_addresses
        if (dst_ports is None) or (dst_ports == []):
            self.dst_ports = []
        else:
            if isinstance(dst_ports[0], dict):
                objs = [PortType(**elem) for elem in dst_ports]
                self.dst_ports = objs
            else:
                self.dst_ports = dst_ports
        if isinstance(action_list, dict):
            obj = ActionListType(**action_list)
            self.action_list = obj
        else:
            self.action_list = action_list
        self.ethertype = ethertype
    def factory(*args_, **kwargs_):
        if PolicyRuleType.subclass:
            return PolicyRuleType.subclass(*args_, **kwargs_)
        else:
            return PolicyRuleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_rule_sequence(self): return self.rule_sequence
    def set_rule_sequence(self, rule_sequence): self.rule_sequence = rule_sequence
    def get_rule_uuid(self): return self.rule_uuid
    def set_rule_uuid(self, rule_uuid): self.rule_uuid = rule_uuid
    def get_direction(self): return self.direction
    def set_direction(self, direction): self.direction = direction
    def validate_DirectionType(self, value):
        # Validate type DirectionType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'>', u'<>'])
        else:
            error = value not in [u'>', u'<>']
        if error:
            raise ValueError("DirectionType must be one of [u'>', u'<>']")
    def get_protocol(self): return self.protocol
    def set_protocol(self, protocol): self.protocol = protocol
    def validate_ProtocolType(self, value):
        # Validate type ProtocolType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'tcp', u'udp', u'icmp', u'any', u'1', u'6', u'17'])
        else:
            error = value not in [u'tcp', u'udp', u'icmp', u'any', u'1', u'6', u'17']
        if error:
            raise ValueError("ProtocolType must be one of [u'tcp', u'udp', u'icmp', u'any', u'1', u'6', u'17']")
    def get_src_addresses(self): return self.src_addresses
    def set_src_addresses(self, src_addresses): self.src_addresses = src_addresses
    def add_src_addresses(self, value): self.src_addresses.append(value)
    def insert_src_addresses(self, index, value): self.src_addresses[index] = value
    def delete_src_addresses(self, value): self.src_addresses.remove(value)
    def get_src_ports(self): return self.src_ports
    def set_src_ports(self, src_ports): self.src_ports = src_ports
    def add_src_ports(self, value): self.src_ports.append(value)
    def insert_src_ports(self, index, value): self.src_ports[index] = value
    def delete_src_ports(self, value): self.src_ports.remove(value)
    def get_application(self): return self.application
    def set_application(self, application): self.application = application
    def add_application(self, value): self.application.append(value)
    def insert_application(self, index, value): self.application[index] = value
    def delete_application(self, value): self.application.remove(value)
    def get_dst_addresses(self): return self.dst_addresses
    def set_dst_addresses(self, dst_addresses): self.dst_addresses = dst_addresses
    def add_dst_addresses(self, value): self.dst_addresses.append(value)
    def insert_dst_addresses(self, index, value): self.dst_addresses[index] = value
    def delete_dst_addresses(self, value): self.dst_addresses.remove(value)
    def get_dst_ports(self): return self.dst_ports
    def set_dst_ports(self, dst_ports): self.dst_ports = dst_ports
    def add_dst_ports(self, value): self.dst_ports.append(value)
    def insert_dst_ports(self, index, value): self.dst_ports[index] = value
    def delete_dst_ports(self, value): self.dst_ports.remove(value)
    def get_action_list(self): return self.action_list
    def set_action_list(self, action_list): self.action_list = action_list
    def get_ethertype(self): return self.ethertype
    def set_ethertype(self, ethertype): self.ethertype = ethertype
    def validate_EtherType(self, value):
        # Validate type EtherType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'IPv4', u'IPv6'])
        else:
            error = value not in [u'IPv4', u'IPv6']
        if error:
            raise ValueError("EtherType must be one of [u'IPv4', u'IPv6']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.rule_sequence == other.rule_sequence and
                self.rule_uuid == other.rule_uuid and
                self.direction == other.direction and
                self.protocol == other.protocol and
                self.src_addresses == other.src_addresses and
                self.src_ports == other.src_ports and
                self.application == other.application and
                self.dst_addresses == other.dst_addresses and
                self.dst_ports == other.dst_ports and
                self.action_list == other.action_list and
                self.ethertype == other.ethertype)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_rule_sequence (SequenceType.populate ())
        obj.set_rule_uuid (obj.populate_string ("rule_uuid"))
        obj.set_direction (obj.populate_string ("direction"))
        obj.set_protocol (obj.populate_string ("protocol"))
        obj.set_src_addresses ([AddressType.populate ()])
        obj.set_src_ports ([PortType.populate ()])
        obj.set_application ([obj.populate_string ("application")])
        obj.set_dst_addresses ([AddressType.populate ()])
        obj.set_dst_ports ([PortType.populate ()])
        obj.set_action_list (ActionListType.populate ())
        obj.set_ethertype (obj.populate_string ("ethertype"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='PolicyRuleType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PolicyRuleType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PolicyRuleType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PolicyRuleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.rule_sequence is not None:
            self.rule_sequence.export(outfile, level, namespace_, name_='rule-sequence', pretty_print=pretty_print)
        if self.rule_uuid is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srule-uuid>%s</%srule-uuid>%s' % (namespace_, self.gds_format_string(quote_xml(self.rule_uuid).encode(ExternalEncoding), input_name='rule-uuid'), namespace_, eol_))
        if self.direction is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdirection>%s</%sdirection>%s' % (namespace_, self.gds_format_string(quote_xml(self.direction).encode(ExternalEncoding), input_name='direction'), namespace_, eol_))
        if self.protocol is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprotocol>%s</%sprotocol>%s' % (namespace_, self.gds_format_string(quote_xml(self.protocol).encode(ExternalEncoding), input_name='protocol'), namespace_, eol_))
        for src_addresses_ in self.src_addresses:
            if isinstance(src_addresses_, dict):
                src_addresses_ = AddressType(**src_addresses_)
            src_addresses_.export(outfile, level, namespace_, name_='src-addresses', pretty_print=pretty_print)
        for src_ports_ in self.src_ports:
            if isinstance(src_ports_, dict):
                src_ports_ = PortType(**src_ports_)
            src_ports_.export(outfile, level, namespace_, name_='src-ports', pretty_print=pretty_print)
        for application_ in self.application:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sapplication>%s</%sapplication>%s' % (namespace_, self.gds_format_string(quote_xml(application_).encode(ExternalEncoding), input_name='application'), namespace_, eol_))
        for dst_addresses_ in self.dst_addresses:
            if isinstance(dst_addresses_, dict):
                dst_addresses_ = AddressType(**dst_addresses_)
            dst_addresses_.export(outfile, level, namespace_, name_='dst-addresses', pretty_print=pretty_print)
        for dst_ports_ in self.dst_ports:
            if isinstance(dst_ports_, dict):
                dst_ports_ = PortType(**dst_ports_)
            dst_ports_.export(outfile, level, namespace_, name_='dst-ports', pretty_print=pretty_print)
        if self.action_list is not None:
            self.action_list.export(outfile, level, namespace_, name_='action-list', pretty_print=pretty_print)
        if self.ethertype is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sethertype>%s</%sethertype>%s' % (namespace_, self.gds_format_string(quote_xml(self.ethertype).encode(ExternalEncoding), input_name='ethertype'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.rule_sequence is not None or
            self.rule_uuid is not None or
            self.direction is not None or
            self.protocol is not None or
            self.src_addresses or
            self.src_ports or
            self.application or
            self.dst_addresses or
            self.dst_ports or
            self.action_list is not None or
            self.ethertype is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PolicyRuleType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.rule_sequence is not None:
            showIndent(outfile, level)
            outfile.write('rule_sequence=model_.SequenceType(\n')
            self.rule_sequence.exportLiteral(outfile, level, name_='rule_sequence')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.rule_uuid is not None:
            showIndent(outfile, level)
            outfile.write('rule_uuid=%s,\n' % quote_python(self.rule_uuid).encode(ExternalEncoding))
        if self.direction is not None:
            showIndent(outfile, level)
            outfile.write('direction=%s,\n' % quote_python(self.direction).encode(ExternalEncoding))
        if self.protocol is not None:
            showIndent(outfile, level)
            outfile.write('protocol=%s,\n' % quote_python(self.protocol).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('src_addresses=[\n')
        level += 1
        for src_addresses_ in self.src_addresses:
            showIndent(outfile, level)
            outfile.write('model_.AddressType(\n')
            src_addresses_.exportLiteral(outfile, level, name_='AddressType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('src_ports=[\n')
        level += 1
        for src_ports_ in self.src_ports:
            showIndent(outfile, level)
            outfile.write('model_.PortType(\n')
            src_ports_.exportLiteral(outfile, level, name_='PortType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('application=[\n')
        level += 1
        for application_ in self.application:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(application_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('dst_addresses=[\n')
        level += 1
        for dst_addresses_ in self.dst_addresses:
            showIndent(outfile, level)
            outfile.write('model_.AddressType(\n')
            dst_addresses_.exportLiteral(outfile, level, name_='AddressType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('dst_ports=[\n')
        level += 1
        for dst_ports_ in self.dst_ports:
            showIndent(outfile, level)
            outfile.write('model_.PortType(\n')
            dst_ports_.exportLiteral(outfile, level, name_='PortType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.action_list is not None:
            showIndent(outfile, level)
            outfile.write('action_list=model_.ActionListType(\n')
            self.action_list.exportLiteral(outfile, level, name_='action_list')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ethertype is not None:
            showIndent(outfile, level)
            outfile.write('ethertype=%s,\n' % quote_python(self.ethertype).encode(ExternalEncoding))
    def exportDict(self, name_='PolicyRuleType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'rule-sequence':
            obj_ = SequenceType.factory()
            obj_.build(child_)
            self.set_rule_sequence(obj_)
        elif nodeName_ == 'rule-uuid':
            rule_uuid_ = child_.text
            rule_uuid_ = self.gds_validate_string(rule_uuid_, node, 'rule_uuid')
            self.rule_uuid = rule_uuid_
        elif nodeName_ == 'direction':
            direction_ = child_.text
            direction_ = self.gds_validate_string(direction_, node, 'direction')
            self.direction = direction_
            self.validate_DirectionType(self.direction)    # validate type DirectionType
        elif nodeName_ == 'protocol':
            protocol_ = child_.text
            protocol_ = self.gds_validate_string(protocol_, node, 'protocol')
            self.protocol = protocol_
            self.validate_ProtocolType(self.protocol)    # validate type ProtocolType
        elif nodeName_ == 'src-addresses':
            obj_ = AddressType.factory()
            obj_.build(child_)
            self.src_addresses.append(obj_)
        elif nodeName_ == 'src-ports':
            obj_ = PortType.factory()
            obj_.build(child_)
            self.src_ports.append(obj_)
        elif nodeName_ == 'application':
            application_ = child_.text
            application_ = self.gds_validate_string(application_, node, 'application')
            self.application.append(application_)
        elif nodeName_ == 'dst-addresses':
            obj_ = AddressType.factory()
            obj_.build(child_)
            self.dst_addresses.append(obj_)
        elif nodeName_ == 'dst-ports':
            obj_ = PortType.factory()
            obj_.build(child_)
            self.dst_ports.append(obj_)
        elif nodeName_ == 'action-list':
            obj_ = ActionListType.factory()
            obj_.build(child_)
            self.set_action_list(obj_)
        elif nodeName_ == 'ethertype':
            ethertype_ = child_.text
            ethertype_ = self.gds_validate_string(ethertype_, node, 'ethertype')
            self.ethertype = ethertype_
            self.validate_EtherType(self.ethertype)    # validate type EtherType
# end class PolicyRuleType


class PolicyEntriesType(GeneratedsSuper):
    """
    PolicyEntriesType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, policy_rule=None, **kwargs):
        if (policy_rule is None) or (policy_rule == []):
            self.policy_rule = []
        else:
            if isinstance(policy_rule[0], dict):
                objs = [PolicyRuleType(**elem) for elem in policy_rule]
                self.policy_rule = objs
            else:
                self.policy_rule = policy_rule
    def factory(*args_, **kwargs_):
        if PolicyEntriesType.subclass:
            return PolicyEntriesType.subclass(*args_, **kwargs_)
        else:
            return PolicyEntriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_policy_rule(self): return self.policy_rule
    def set_policy_rule(self, policy_rule): self.policy_rule = policy_rule
    def add_policy_rule(self, value): self.policy_rule.append(value)
    def insert_policy_rule(self, index, value): self.policy_rule[index] = value
    def delete_policy_rule(self, value): self.policy_rule.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.policy_rule == other.policy_rule)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_policy_rule ([PolicyRuleType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='PolicyEntriesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PolicyEntriesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PolicyEntriesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PolicyEntriesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for policy_rule_ in self.policy_rule:
            if isinstance(policy_rule_, dict):
                policy_rule_ = PolicyRuleType(**policy_rule_)
            policy_rule_.export(outfile, level, namespace_, name_='policy-rule', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.policy_rule
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PolicyEntriesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('policy_rule=[\n')
        level += 1
        for policy_rule_ in self.policy_rule:
            showIndent(outfile, level)
            outfile.write('model_.PolicyRuleType(\n')
            policy_rule_.exportLiteral(outfile, level, name_='PolicyRuleType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='PolicyEntriesType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'policy-rule':
            obj_ = PolicyRuleType.factory()
            obj_.build(child_)
            self.policy_rule.append(obj_)
# end class PolicyEntriesType


class ApiAccessType(GeneratedsSuper):
    """
    ApiAccessType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, api_name=None, permissions=None, **kwargs):
        self.api_name = api_name
        if isinstance(permissions, dict):
            obj = PermType(**permissions)
            self.permissions = obj
        else:
            self.permissions = permissions
    def factory(*args_, **kwargs_):
        if ApiAccessType.subclass:
            return ApiAccessType.subclass(*args_, **kwargs_)
        else:
            return ApiAccessType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_api_name(self): return self.api_name
    def set_api_name(self, api_name): self.api_name = api_name
    def get_permissions(self): return self.permissions
    def set_permissions(self, permissions): self.permissions = permissions
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.api_name == other.api_name and
                self.permissions == other.permissions)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_api_name (obj.populate_string ("api_name"))
        obj.set_permissions (PermType.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ApiAccessType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ApiAccessType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ApiAccessType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ApiAccessType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.api_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sapi-name>%s</%sapi-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.api_name).encode(ExternalEncoding), input_name='api-name'), namespace_, eol_))
        if self.permissions is not None:
            self.permissions.export(outfile, level, namespace_, name_='permissions', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.api_name is not None or
            self.permissions is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ApiAccessType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.api_name is not None:
            showIndent(outfile, level)
            outfile.write('api_name=%s,\n' % quote_python(self.api_name).encode(ExternalEncoding))
        if self.permissions is not None:
            showIndent(outfile, level)
            outfile.write('permissions=model_.PermType(\n')
            self.permissions.exportLiteral(outfile, level, name_='permissions')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='ApiAccessType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'api-name':
            api_name_ = child_.text
            api_name_ = self.gds_validate_string(api_name_, node, 'api_name')
            self.api_name = api_name_
        elif nodeName_ == 'permissions':
            obj_ = PermType.factory()
            obj_.build(child_)
            self.set_permissions(obj_)
# end class ApiAccessType


class ApiAccessListType(GeneratedsSuper):
    """
    ApiAccessListType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, api_access=None, **kwargs):
        if (api_access is None) or (api_access == []):
            self.api_access = []
        else:
            if isinstance(api_access[0], dict):
                objs = [ApiAccessType(**elem) for elem in api_access]
                self.api_access = objs
            else:
                self.api_access = api_access
    def factory(*args_, **kwargs_):
        if ApiAccessListType.subclass:
            return ApiAccessListType.subclass(*args_, **kwargs_)
        else:
            return ApiAccessListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_api_access(self): return self.api_access
    def set_api_access(self, api_access): self.api_access = api_access
    def add_api_access(self, value): self.api_access.append(value)
    def insert_api_access(self, index, value): self.api_access[index] = value
    def delete_api_access(self, value): self.api_access.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.api_access == other.api_access)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_api_access ([ApiAccessType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ApiAccessListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ApiAccessListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ApiAccessListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ApiAccessListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for api_access_ in self.api_access:
            if isinstance(api_access_, dict):
                api_access_ = ApiAccessType(**api_access_)
            api_access_.export(outfile, level, namespace_, name_='api-access', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.api_access
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ApiAccessListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('api_access=[\n')
        level += 1
        for api_access_ in self.api_access:
            showIndent(outfile, level)
            outfile.write('model_.ApiAccessType(\n')
            api_access_.exportLiteral(outfile, level, name_='ApiAccessType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='ApiAccessListType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'api-access':
            obj_ = ApiAccessType.factory()
            obj_.build(child_)
            self.api_access.append(obj_)
# end class ApiAccessListType


class DhcpOptionType(GeneratedsSuper):
    """
    DhcpOptionType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, dhcp_option_name=None, dhcp_option_value=None, **kwargs):
        self.dhcp_option_name = dhcp_option_name
        self.dhcp_option_value = dhcp_option_value
    def factory(*args_, **kwargs_):
        if DhcpOptionType.subclass:
            return DhcpOptionType.subclass(*args_, **kwargs_)
        else:
            return DhcpOptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_dhcp_option_name(self): return self.dhcp_option_name
    def set_dhcp_option_name(self, dhcp_option_name): self.dhcp_option_name = dhcp_option_name
    def get_dhcp_option_value(self): return self.dhcp_option_value
    def set_dhcp_option_value(self, dhcp_option_value): self.dhcp_option_value = dhcp_option_value
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.dhcp_option_name == other.dhcp_option_name and
                self.dhcp_option_value == other.dhcp_option_value)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_dhcp_option_name (obj.populate_string ("dhcp_option_name"))
        obj.set_dhcp_option_value (obj.populate_string ("dhcp_option_value"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='DhcpOptionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DhcpOptionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DhcpOptionType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='DhcpOptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dhcp_option_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhcp-option-name>%s</%sdhcp-option-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.dhcp_option_name).encode(ExternalEncoding), input_name='dhcp-option-name'), namespace_, eol_))
        if self.dhcp_option_value is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhcp-option-value>%s</%sdhcp-option-value>%s' % (namespace_, self.gds_format_string(quote_xml(self.dhcp_option_value).encode(ExternalEncoding), input_name='dhcp-option-value'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.dhcp_option_name is not None or
            self.dhcp_option_value is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DhcpOptionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.dhcp_option_name is not None:
            showIndent(outfile, level)
            outfile.write('dhcp_option_name=%s,\n' % quote_python(self.dhcp_option_name).encode(ExternalEncoding))
        if self.dhcp_option_value is not None:
            showIndent(outfile, level)
            outfile.write('dhcp_option_value=%s,\n' % quote_python(self.dhcp_option_value).encode(ExternalEncoding))
    def exportDict(self, name_='DhcpOptionType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'dhcp-option-name':
            dhcp_option_name_ = child_.text
            dhcp_option_name_ = self.gds_validate_string(dhcp_option_name_, node, 'dhcp_option_name')
            self.dhcp_option_name = dhcp_option_name_
        elif nodeName_ == 'dhcp-option-value':
            dhcp_option_value_ = child_.text
            dhcp_option_value_ = self.gds_validate_string(dhcp_option_value_, node, 'dhcp_option_value')
            self.dhcp_option_value = dhcp_option_value_
# end class DhcpOptionType


class DhcpOptionsListType(GeneratedsSuper):
    """
    DhcpOptionsListType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, dhcp_option=None, **kwargs):
        if (dhcp_option is None) or (dhcp_option == []):
            self.dhcp_option = []
        else:
            if isinstance(dhcp_option[0], dict):
                objs = [DhcpOptionType(**elem) for elem in dhcp_option]
                self.dhcp_option = objs
            else:
                self.dhcp_option = dhcp_option
    def factory(*args_, **kwargs_):
        if DhcpOptionsListType.subclass:
            return DhcpOptionsListType.subclass(*args_, **kwargs_)
        else:
            return DhcpOptionsListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_dhcp_option(self): return self.dhcp_option
    def set_dhcp_option(self, dhcp_option): self.dhcp_option = dhcp_option
    def add_dhcp_option(self, value): self.dhcp_option.append(value)
    def insert_dhcp_option(self, index, value): self.dhcp_option[index] = value
    def delete_dhcp_option(self, value): self.dhcp_option.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.dhcp_option == other.dhcp_option)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_dhcp_option ([DhcpOptionType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='DhcpOptionsListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DhcpOptionsListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DhcpOptionsListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='DhcpOptionsListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for dhcp_option_ in self.dhcp_option:
            if isinstance(dhcp_option_, dict):
                dhcp_option_ = DhcpOptionType(**dhcp_option_)
            dhcp_option_.export(outfile, level, namespace_, name_='dhcp-option', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.dhcp_option
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DhcpOptionsListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('dhcp_option=[\n')
        level += 1
        for dhcp_option_ in self.dhcp_option:
            showIndent(outfile, level)
            outfile.write('model_.DhcpOptionType(\n')
            dhcp_option_.exportLiteral(outfile, level, name_='DhcpOptionType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='DhcpOptionsListType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'dhcp-option':
            obj_ = DhcpOptionType.factory()
            obj_.build(child_)
            self.dhcp_option.append(obj_)
# end class DhcpOptionsListType


class IpamDnsAddressType(GeneratedsSuper):
    """
    IpamDnsAddressType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, tenant_dns_server_address=None, virtual_dns_server_name=None, **kwargs):
        if isinstance(tenant_dns_server_address, dict):
            obj = IpAddressesType(**tenant_dns_server_address)
            self.tenant_dns_server_address = obj
        else:
            self.tenant_dns_server_address = tenant_dns_server_address
        self.virtual_dns_server_name = virtual_dns_server_name
    def factory(*args_, **kwargs_):
        if IpamDnsAddressType.subclass:
            return IpamDnsAddressType.subclass(*args_, **kwargs_)
        else:
            return IpamDnsAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_tenant_dns_server_address(self): return self.tenant_dns_server_address
    def set_tenant_dns_server_address(self, tenant_dns_server_address): self.tenant_dns_server_address = tenant_dns_server_address
    def get_virtual_dns_server_name(self): return self.virtual_dns_server_name
    def set_virtual_dns_server_name(self, virtual_dns_server_name): self.virtual_dns_server_name = virtual_dns_server_name
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.tenant_dns_server_address == other.tenant_dns_server_address and
                self.virtual_dns_server_name == other.virtual_dns_server_name)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_tenant_dns_server_address (IpAddressesType.populate ())
        obj.set_virtual_dns_server_name (obj.populate_string ("virtual_dns_server_name"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='IpamDnsAddressType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IpamDnsAddressType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IpamDnsAddressType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='IpamDnsAddressType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tenant_dns_server_address is not None:
            self.tenant_dns_server_address.export(outfile, level, namespace_, name_='tenant-dns-server-address', pretty_print=pretty_print)
        if self.virtual_dns_server_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-dns-server-name>%s</%svirtual-dns-server-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.virtual_dns_server_name).encode(ExternalEncoding), input_name='virtual-dns-server-name'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.tenant_dns_server_address is not None or
            self.virtual_dns_server_name is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IpamDnsAddressType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.tenant_dns_server_address is not None:
            showIndent(outfile, level)
            outfile.write('tenant_dns_server_address=model_.IpAddressesType(\n')
            self.tenant_dns_server_address.exportLiteral(outfile, level, name_='tenant_dns_server_address')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.virtual_dns_server_name is not None:
            showIndent(outfile, level)
            outfile.write('virtual_dns_server_name=%s,\n' % quote_python(self.virtual_dns_server_name).encode(ExternalEncoding))
    def exportDict(self, name_='IpamDnsAddressType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'tenant-dns-server-address':
            obj_ = IpAddressesType.factory()
            obj_.build(child_)
            self.set_tenant_dns_server_address(obj_)
        elif nodeName_ == 'virtual-dns-server-name':
            virtual_dns_server_name_ = child_.text
            virtual_dns_server_name_ = self.gds_validate_string(virtual_dns_server_name_, node, 'virtual_dns_server_name')
            self.virtual_dns_server_name = virtual_dns_server_name_
# end class IpamDnsAddressType


class IpamType(GeneratedsSuper):
    """
    IpamType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, ipam_method=None, ipam_dns_method=None, ipam_dns_server=None, dhcp_option_list=None, cidr_block=None, host_routes=None, **kwargs):
        self.ipam_method = ipam_method
        self.ipam_dns_method = ipam_dns_method
        if isinstance(ipam_dns_server, dict):
            obj = IpamDnsAddressType(**ipam_dns_server)
            self.ipam_dns_server = obj
        else:
            self.ipam_dns_server = ipam_dns_server
        if isinstance(dhcp_option_list, dict):
            obj = DhcpOptionsListType(**dhcp_option_list)
            self.dhcp_option_list = obj
        else:
            self.dhcp_option_list = dhcp_option_list
        if isinstance(cidr_block, dict):
            obj = SubnetType(**cidr_block)
            self.cidr_block = obj
        else:
            self.cidr_block = cidr_block
        if isinstance(host_routes, dict):
            obj = RouteTableType(**host_routes)
            self.host_routes = obj
        else:
            self.host_routes = host_routes
    def factory(*args_, **kwargs_):
        if IpamType.subclass:
            return IpamType.subclass(*args_, **kwargs_)
        else:
            return IpamType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ipam_method(self): return self.ipam_method
    def set_ipam_method(self, ipam_method): self.ipam_method = ipam_method
    def validate_IpamMethodType(self, value):
        # Validate type IpamMethodType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'dhcp', u'fixed'])
        else:
            error = value not in [u'dhcp', u'fixed']
        if error:
            raise ValueError("IpamMethodType must be one of [u'dhcp', u'fixed']")
    def get_ipam_dns_method(self): return self.ipam_dns_method
    def set_ipam_dns_method(self, ipam_dns_method): self.ipam_dns_method = ipam_dns_method
    def validate_IpamDnsMethodType(self, value):
        # Validate type IpamDnsMethodType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'none', u'default-dns-server', u'tenant-dns-server', u'virtual-dns-server'])
        else:
            error = value not in [u'none', u'default-dns-server', u'tenant-dns-server', u'virtual-dns-server']
        if error:
            raise ValueError("IpamDnsMethodType must be one of [u'none', u'default-dns-server', u'tenant-dns-server', u'virtual-dns-server']")
    def get_ipam_dns_server(self): return self.ipam_dns_server
    def set_ipam_dns_server(self, ipam_dns_server): self.ipam_dns_server = ipam_dns_server
    def get_dhcp_option_list(self): return self.dhcp_option_list
    def set_dhcp_option_list(self, dhcp_option_list): self.dhcp_option_list = dhcp_option_list
    def get_cidr_block(self): return self.cidr_block
    def set_cidr_block(self, cidr_block): self.cidr_block = cidr_block
    def get_host_routes(self): return self.host_routes
    def set_host_routes(self, host_routes): self.host_routes = host_routes
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.ipam_method == other.ipam_method and
                self.ipam_dns_method == other.ipam_dns_method and
                self.ipam_dns_server == other.ipam_dns_server and
                self.dhcp_option_list == other.dhcp_option_list and
                self.cidr_block == other.cidr_block and
                self.host_routes == other.host_routes)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_ipam_method (obj.populate_string ("ipam_method"))
        obj.set_ipam_dns_method (obj.populate_string ("ipam_dns_method"))
        obj.set_ipam_dns_server (IpamDnsAddressType.populate ())
        obj.set_dhcp_option_list (DhcpOptionsListType.populate ())
        obj.set_cidr_block (SubnetType.populate ())
        obj.set_host_routes (RouteTableType.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='IpamType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IpamType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IpamType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='IpamType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ipam_method is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sipam-method>%s</%sipam-method>%s' % (namespace_, self.gds_format_string(quote_xml(self.ipam_method).encode(ExternalEncoding), input_name='ipam-method'), namespace_, eol_))
        if self.ipam_dns_method is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sipam-dns-method>%s</%sipam-dns-method>%s' % (namespace_, self.gds_format_string(quote_xml(self.ipam_dns_method).encode(ExternalEncoding), input_name='ipam-dns-method'), namespace_, eol_))
        if self.ipam_dns_server is not None:
            self.ipam_dns_server.export(outfile, level, namespace_, name_='ipam-dns-server', pretty_print=pretty_print)
        if self.dhcp_option_list is not None:
            self.dhcp_option_list.export(outfile, level, namespace_, name_='dhcp-option-list', pretty_print=pretty_print)
        if self.cidr_block is not None:
            self.cidr_block.export(outfile, level, namespace_, name_='cidr-block', pretty_print=pretty_print)
        if self.host_routes is not None:
            self.host_routes.export(outfile, level, namespace_, name_='host-routes', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.ipam_method is not None or
            self.ipam_dns_method is not None or
            self.ipam_dns_server is not None or
            self.dhcp_option_list is not None or
            self.cidr_block is not None or
            self.host_routes is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IpamType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.ipam_method is not None:
            showIndent(outfile, level)
            outfile.write('ipam_method=%s,\n' % quote_python(self.ipam_method).encode(ExternalEncoding))
        if self.ipam_dns_method is not None:
            showIndent(outfile, level)
            outfile.write('ipam_dns_method=%s,\n' % quote_python(self.ipam_dns_method).encode(ExternalEncoding))
        if self.ipam_dns_server is not None:
            showIndent(outfile, level)
            outfile.write('ipam_dns_server=model_.IpamDnsAddressType(\n')
            self.ipam_dns_server.exportLiteral(outfile, level, name_='ipam_dns_server')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dhcp_option_list is not None:
            showIndent(outfile, level)
            outfile.write('dhcp_option_list=model_.DhcpOptionsListType(\n')
            self.dhcp_option_list.exportLiteral(outfile, level, name_='dhcp_option_list')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.cidr_block is not None:
            showIndent(outfile, level)
            outfile.write('cidr_block=model_.SubnetType(\n')
            self.cidr_block.exportLiteral(outfile, level, name_='cidr_block')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.host_routes is not None:
            showIndent(outfile, level)
            outfile.write('host_routes=model_.RouteTableType(\n')
            self.host_routes.exportLiteral(outfile, level, name_='host_routes')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='IpamType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ipam-method':
            ipam_method_ = child_.text
            ipam_method_ = self.gds_validate_string(ipam_method_, node, 'ipam_method')
            self.ipam_method = ipam_method_
            self.validate_IpamMethodType(self.ipam_method)    # validate type IpamMethodType
        elif nodeName_ == 'ipam-dns-method':
            ipam_dns_method_ = child_.text
            ipam_dns_method_ = self.gds_validate_string(ipam_dns_method_, node, 'ipam_dns_method')
            self.ipam_dns_method = ipam_dns_method_
            self.validate_IpamDnsMethodType(self.ipam_dns_method)    # validate type IpamDnsMethodType
        elif nodeName_ == 'ipam-dns-server':
            obj_ = IpamDnsAddressType.factory()
            obj_.build(child_)
            self.set_ipam_dns_server(obj_)
        elif nodeName_ == 'dhcp-option-list':
            obj_ = DhcpOptionsListType.factory()
            obj_.build(child_)
            self.set_dhcp_option_list(obj_)
        elif nodeName_ == 'cidr-block':
            obj_ = SubnetType.factory()
            obj_.build(child_)
            self.set_cidr_block(obj_)
        elif nodeName_ == 'host-routes':
            obj_ = RouteTableType.factory()
            obj_.build(child_)
            self.set_host_routes(obj_)
# end class IpamType


class EncapsulationPrioritiesType(GeneratedsSuper):
    """
    EncapsulationPrioritiesType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, encapsulation=None, **kwargs):
        if (encapsulation is None) or (encapsulation == []):
            self.encapsulation = []
        else:
            self.encapsulation = encapsulation
    def factory(*args_, **kwargs_):
        if EncapsulationPrioritiesType.subclass:
            return EncapsulationPrioritiesType.subclass(*args_, **kwargs_)
        else:
            return EncapsulationPrioritiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_encapsulation(self): return self.encapsulation
    def set_encapsulation(self, encapsulation): self.encapsulation = encapsulation
    def add_encapsulation(self, value): self.encapsulation.append(value)
    def insert_encapsulation(self, index, value): self.encapsulation[index] = value
    def delete_encapsulation(self, value): self.encapsulation.remove(value)
    def validate_EncapsulationType(self, value):
        # Validate type EncapsulationType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'MPLSoGRE', u'MPLSoUDP', u'VXLAN'])
        else:
            error = value not in [u'MPLSoGRE', u'MPLSoUDP', u'VXLAN']
        if error:
            raise ValueError("EncapsulationType must be one of [u'MPLSoGRE', u'MPLSoUDP', u'VXLAN']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.encapsulation == other.encapsulation)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_encapsulation ([obj.populate_string ("encapsulation")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='EncapsulationPrioritiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EncapsulationPrioritiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='EncapsulationPrioritiesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='EncapsulationPrioritiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for encapsulation_ in self.encapsulation:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sencapsulation>%s</%sencapsulation>%s' % (namespace_, self.gds_format_string(quote_xml(encapsulation_).encode(ExternalEncoding), input_name='encapsulation'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.encapsulation
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='EncapsulationPrioritiesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('encapsulation=[\n')
        level += 1
        for encapsulation_ in self.encapsulation:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(encapsulation_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='EncapsulationPrioritiesType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'encapsulation':
            encapsulation_ = child_.text
            encapsulation_ = self.gds_validate_string(encapsulation_, node, 'encapsulation')
            self.encapsulation.append(encapsulation_)
            self.validate_EncapsulationType(self.encapsulation)    # validate type EncapsulationType
# end class EncapsulationPrioritiesType


class LinklocalServiceEntryType(GeneratedsSuper):
    """
    LinklocalServiceEntryType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, linklocal_service_name=None, linklocal_service_ip=None, linklocal_service_port=None, ip_fabric_DNS_service_name=None, ip_fabric_service_port=None, ip_fabric_service_ip=None, **kwargs):
        self.linklocal_service_name = linklocal_service_name
        self.linklocal_service_ip = linklocal_service_ip
        self.linklocal_service_port = linklocal_service_port
        self.ip_fabric_DNS_service_name = ip_fabric_DNS_service_name
        self.ip_fabric_service_port = ip_fabric_service_port
        if (ip_fabric_service_ip is None) or (ip_fabric_service_ip == []):
            self.ip_fabric_service_ip = []
        else:
            self.ip_fabric_service_ip = ip_fabric_service_ip
    def factory(*args_, **kwargs_):
        if LinklocalServiceEntryType.subclass:
            return LinklocalServiceEntryType.subclass(*args_, **kwargs_)
        else:
            return LinklocalServiceEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_linklocal_service_name(self): return self.linklocal_service_name
    def set_linklocal_service_name(self, linklocal_service_name): self.linklocal_service_name = linklocal_service_name
    def get_linklocal_service_ip(self): return self.linklocal_service_ip
    def set_linklocal_service_ip(self, linklocal_service_ip): self.linklocal_service_ip = linklocal_service_ip
    def validate_IpAddress(self, value):
        # Validate type IpAddress, a restriction on xsd:string.
        pass
    def get_linklocal_service_port(self): return self.linklocal_service_port
    def set_linklocal_service_port(self, linklocal_service_port): self.linklocal_service_port = linklocal_service_port
    def get_ip_fabric_DNS_service_name(self): return self.ip_fabric_DNS_service_name
    def set_ip_fabric_DNS_service_name(self, ip_fabric_DNS_service_name): self.ip_fabric_DNS_service_name = ip_fabric_DNS_service_name
    def get_ip_fabric_service_port(self): return self.ip_fabric_service_port
    def set_ip_fabric_service_port(self, ip_fabric_service_port): self.ip_fabric_service_port = ip_fabric_service_port
    def get_ip_fabric_service_ip(self): return self.ip_fabric_service_ip
    def set_ip_fabric_service_ip(self, ip_fabric_service_ip): self.ip_fabric_service_ip = ip_fabric_service_ip
    def add_ip_fabric_service_ip(self, value): self.ip_fabric_service_ip.append(value)
    def insert_ip_fabric_service_ip(self, index, value): self.ip_fabric_service_ip[index] = value
    def delete_ip_fabric_service_ip(self, value): self.ip_fabric_service_ip.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.linklocal_service_name == other.linklocal_service_name and
                self.linklocal_service_ip == other.linklocal_service_ip and
                self.linklocal_service_port == other.linklocal_service_port and
                self.ip_fabric_DNS_service_name == other.ip_fabric_DNS_service_name and
                self.ip_fabric_service_port == other.ip_fabric_service_port and
                self.ip_fabric_service_ip == other.ip_fabric_service_ip)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_linklocal_service_name (obj.populate_string ("linklocal_service_name"))
        obj.set_linklocal_service_ip (obj.populate_string ("linklocal_service_ip"))
        obj.set_linklocal_service_port (obj.populate_integer ("linklocal_service_port"))
        obj.set_ip_fabric_DNS_service_name (obj.populate_string ("ip_fabric_DNS_service_name"))
        obj.set_ip_fabric_service_port (obj.populate_integer ("ip_fabric_service_port"))
        obj.set_ip_fabric_service_ip ([obj.populate_string ("ip_fabric_service_ip")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='LinklocalServiceEntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LinklocalServiceEntryType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LinklocalServiceEntryType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='LinklocalServiceEntryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.linklocal_service_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slinklocal-service-name>%s</%slinklocal-service-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.linklocal_service_name).encode(ExternalEncoding), input_name='linklocal-service-name'), namespace_, eol_))
        if self.linklocal_service_ip is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slinklocal-service-ip>%s</%slinklocal-service-ip>%s' % (namespace_, self.gds_format_string(quote_xml(self.linklocal_service_ip).encode(ExternalEncoding), input_name='linklocal-service-ip'), namespace_, eol_))
        if self.linklocal_service_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slinklocal-service-port>%s</%slinklocal-service-port>%s' % (namespace_, self.gds_format_integer(self.linklocal_service_port, input_name='linklocal-service-port'), namespace_, eol_))
        if self.ip_fabric_DNS_service_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sip-fabric-DNS-service-name>%s</%sip-fabric-DNS-service-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.ip_fabric_DNS_service_name).encode(ExternalEncoding), input_name='ip-fabric-DNS-service-name'), namespace_, eol_))
        if self.ip_fabric_service_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sip-fabric-service-port>%s</%sip-fabric-service-port>%s' % (namespace_, self.gds_format_integer(self.ip_fabric_service_port, input_name='ip-fabric-service-port'), namespace_, eol_))
        for ip_fabric_service_ip_ in self.ip_fabric_service_ip:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sip-fabric-service-ip>%s</%sip-fabric-service-ip>%s' % (namespace_, self.gds_format_string(quote_xml(ip_fabric_service_ip_).encode(ExternalEncoding), input_name='ip-fabric-service-ip'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.linklocal_service_name is not None or
            self.linklocal_service_ip is not None or
            self.linklocal_service_port is not None or
            self.ip_fabric_DNS_service_name is not None or
            self.ip_fabric_service_port is not None or
            self.ip_fabric_service_ip
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LinklocalServiceEntryType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.linklocal_service_name is not None:
            showIndent(outfile, level)
            outfile.write('linklocal_service_name=%s,\n' % quote_python(self.linklocal_service_name).encode(ExternalEncoding))
        if self.linklocal_service_ip is not None:
            showIndent(outfile, level)
            outfile.write('linklocal_service_ip=%s,\n' % quote_python(self.linklocal_service_ip).encode(ExternalEncoding))
        if self.linklocal_service_port is not None:
            showIndent(outfile, level)
            outfile.write('linklocal_service_port=%d,\n' % self.linklocal_service_port)
        if self.ip_fabric_DNS_service_name is not None:
            showIndent(outfile, level)
            outfile.write('ip_fabric_DNS_service_name=%s,\n' % quote_python(self.ip_fabric_DNS_service_name).encode(ExternalEncoding))
        if self.ip_fabric_service_port is not None:
            showIndent(outfile, level)
            outfile.write('ip_fabric_service_port=%d,\n' % self.ip_fabric_service_port)
        showIndent(outfile, level)
        outfile.write('ip_fabric_service_ip=[\n')
        level += 1
        for ip_fabric_service_ip_ in self.ip_fabric_service_ip:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(ip_fabric_service_ip_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='LinklocalServiceEntryType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'linklocal-service-name':
            linklocal_service_name_ = child_.text
            linklocal_service_name_ = self.gds_validate_string(linklocal_service_name_, node, 'linklocal_service_name')
            self.linklocal_service_name = linklocal_service_name_
        elif nodeName_ == 'linklocal-service-ip':
            linklocal_service_ip_ = child_.text
            linklocal_service_ip_ = self.gds_validate_string(linklocal_service_ip_, node, 'linklocal_service_ip')
            self.linklocal_service_ip = linklocal_service_ip_
            self.validate_IpAddress(self.linklocal_service_ip)    # validate type IpAddress
        elif nodeName_ == 'linklocal-service-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'linklocal_service_port')
            self.linklocal_service_port = ival_
        elif nodeName_ == 'ip-fabric-DNS-service-name':
            ip_fabric_DNS_service_name_ = child_.text
            ip_fabric_DNS_service_name_ = self.gds_validate_string(ip_fabric_DNS_service_name_, node, 'ip_fabric_DNS_service_name')
            self.ip_fabric_DNS_service_name = ip_fabric_DNS_service_name_
        elif nodeName_ == 'ip-fabric-service-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'ip_fabric_service_port')
            self.ip_fabric_service_port = ival_
        elif nodeName_ == 'ip-fabric-service-ip':
            ip_fabric_service_ip_ = child_.text
            ip_fabric_service_ip_ = self.gds_validate_string(ip_fabric_service_ip_, node, 'ip_fabric_service_ip')
            self.ip_fabric_service_ip.append(ip_fabric_service_ip_)
            self.validate_IpAddress(self.ip_fabric_service_ip)    # validate type IpAddress
# end class LinklocalServiceEntryType


class LinklocalServicesTypes(GeneratedsSuper):
    """
    LinklocalServicesTypes class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, linklocal_service_entry=None, **kwargs):
        if (linklocal_service_entry is None) or (linklocal_service_entry == []):
            self.linklocal_service_entry = []
        else:
            if isinstance(linklocal_service_entry[0], dict):
                objs = [LinklocalServiceEntryType(**elem) for elem in linklocal_service_entry]
                self.linklocal_service_entry = objs
            else:
                self.linklocal_service_entry = linklocal_service_entry
    def factory(*args_, **kwargs_):
        if LinklocalServicesTypes.subclass:
            return LinklocalServicesTypes.subclass(*args_, **kwargs_)
        else:
            return LinklocalServicesTypes(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_linklocal_service_entry(self): return self.linklocal_service_entry
    def set_linklocal_service_entry(self, linklocal_service_entry): self.linklocal_service_entry = linklocal_service_entry
    def add_linklocal_service_entry(self, value): self.linklocal_service_entry.append(value)
    def insert_linklocal_service_entry(self, index, value): self.linklocal_service_entry[index] = value
    def delete_linklocal_service_entry(self, value): self.linklocal_service_entry.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.linklocal_service_entry == other.linklocal_service_entry)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_linklocal_service_entry ([LinklocalServiceEntryType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='LinklocalServicesTypes', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LinklocalServicesTypes')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LinklocalServicesTypes'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='LinklocalServicesTypes', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for linklocal_service_entry_ in self.linklocal_service_entry:
            if isinstance(linklocal_service_entry_, dict):
                linklocal_service_entry_ = LinklocalServiceEntryType(**linklocal_service_entry_)
            linklocal_service_entry_.export(outfile, level, namespace_, name_='linklocal-service-entry', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.linklocal_service_entry
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LinklocalServicesTypes'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('linklocal_service_entry=[\n')
        level += 1
        for linklocal_service_entry_ in self.linklocal_service_entry:
            showIndent(outfile, level)
            outfile.write('model_.LinklocalServiceEntryType(\n')
            linklocal_service_entry_.exportLiteral(outfile, level, name_='LinklocalServiceEntryType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='LinklocalServicesTypes'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'linklocal-service-entry':
            obj_ = LinklocalServiceEntryType.factory()
            obj_.build(child_)
            self.linklocal_service_entry.append(obj_)
# end class LinklocalServicesTypes


class VirtualDnsType(GeneratedsSuper):
    """
    VirtualDnsType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, domain_name=None, dynamic_records_from_client=None, record_order=None, default_ttl_seconds=None, next_virtual_DNS=None, floating_ip_record=None, **kwargs):
        self.domain_name = domain_name
        self.dynamic_records_from_client = dynamic_records_from_client
        self.record_order = record_order
        self.default_ttl_seconds = default_ttl_seconds
        self.next_virtual_DNS = next_virtual_DNS
        self.floating_ip_record = floating_ip_record
    def factory(*args_, **kwargs_):
        if VirtualDnsType.subclass:
            return VirtualDnsType.subclass(*args_, **kwargs_)
        else:
            return VirtualDnsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_domain_name(self): return self.domain_name
    def set_domain_name(self, domain_name): self.domain_name = domain_name
    def get_dynamic_records_from_client(self): return self.dynamic_records_from_client
    def set_dynamic_records_from_client(self, dynamic_records_from_client): self.dynamic_records_from_client = dynamic_records_from_client
    def get_record_order(self): return self.record_order
    def set_record_order(self, record_order): self.record_order = record_order
    def validate_DnsRecordOrderType(self, value):
        # Validate type DnsRecordOrderType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'fixed', u'random', u'round-robin'])
        else:
            error = value not in [u'fixed', u'random', u'round-robin']
        if error:
            raise ValueError("DnsRecordOrderType must be one of [u'fixed', u'random', u'round-robin']")
    def get_default_ttl_seconds(self): return self.default_ttl_seconds
    def set_default_ttl_seconds(self, default_ttl_seconds): self.default_ttl_seconds = default_ttl_seconds
    def get_next_virtual_DNS(self): return self.next_virtual_DNS
    def set_next_virtual_DNS(self, next_virtual_DNS): self.next_virtual_DNS = next_virtual_DNS
    def get_floating_ip_record(self): return self.floating_ip_record
    def set_floating_ip_record(self, floating_ip_record): self.floating_ip_record = floating_ip_record
    def validate_FloatingIpDnsNotation(self, value):
        # Validate type FloatingIpDnsNotation, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'dashed-ip', u'dashed-ip-tenant-name', u'vm-name', u'vm-name-tenant-name'])
        else:
            error = value not in [u'dashed-ip', u'dashed-ip-tenant-name', u'vm-name', u'vm-name-tenant-name']
        if error:
            raise ValueError("FloatingIpDnsNotation must be one of [u'dashed-ip', u'dashed-ip-tenant-name', u'vm-name', u'vm-name-tenant-name']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.domain_name == other.domain_name and
                self.dynamic_records_from_client == other.dynamic_records_from_client and
                self.record_order == other.record_order and
                self.default_ttl_seconds == other.default_ttl_seconds and
                self.next_virtual_DNS == other.next_virtual_DNS and
                self.floating_ip_record == other.floating_ip_record)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_domain_name (obj.populate_string ("domain_name"))
        obj.set_dynamic_records_from_client (obj.populate_boolean ("dynamic_records_from_client"))
        obj.set_record_order (obj.populate_string ("record_order"))
        obj.set_default_ttl_seconds (obj.populate_integer ("default_ttl_seconds"))
        obj.set_next_virtual_DNS (obj.populate_string ("next_virtual_DNS"))
        obj.set_floating_ip_record (obj.populate_string ("floating_ip_record"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VirtualDnsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VirtualDnsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VirtualDnsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VirtualDnsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.domain_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdomain-name>%s</%sdomain-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.domain_name).encode(ExternalEncoding), input_name='domain-name'), namespace_, eol_))
        if self.dynamic_records_from_client is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdynamic-records-from-client>%s</%sdynamic-records-from-client>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.dynamic_records_from_client)), input_name='dynamic-records-from-client'), namespace_, eol_))
        if self.record_order is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srecord-order>%s</%srecord-order>%s' % (namespace_, self.gds_format_string(quote_xml(self.record_order).encode(ExternalEncoding), input_name='record-order'), namespace_, eol_))
        if self.default_ttl_seconds is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdefault-ttl-seconds>%s</%sdefault-ttl-seconds>%s' % (namespace_, self.gds_format_integer(self.default_ttl_seconds, input_name='default-ttl-seconds'), namespace_, eol_))
        if self.next_virtual_DNS is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snext-virtual-DNS>%s</%snext-virtual-DNS>%s' % (namespace_, self.gds_format_string(quote_xml(self.next_virtual_DNS).encode(ExternalEncoding), input_name='next-virtual-DNS'), namespace_, eol_))
        if self.floating_ip_record is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfloating-ip-record>%s</%sfloating-ip-record>%s' % (namespace_, self.gds_format_string(quote_xml(self.floating_ip_record).encode(ExternalEncoding), input_name='floating-ip-record'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.domain_name is not None or
            self.dynamic_records_from_client is not None or
            self.record_order is not None or
            self.default_ttl_seconds is not None or
            self.next_virtual_DNS is not None or
            self.floating_ip_record is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VirtualDnsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.domain_name is not None:
            showIndent(outfile, level)
            outfile.write('domain_name=%s,\n' % quote_python(self.domain_name).encode(ExternalEncoding))
        if self.dynamic_records_from_client is not None:
            showIndent(outfile, level)
            outfile.write('dynamic_records_from_client=%s,\n' % self.dynamic_records_from_client)
        if self.record_order is not None:
            showIndent(outfile, level)
            outfile.write('record_order=%s,\n' % quote_python(self.record_order).encode(ExternalEncoding))
        if self.default_ttl_seconds is not None:
            showIndent(outfile, level)
            outfile.write('default_ttl_seconds=%d,\n' % self.default_ttl_seconds)
        if self.next_virtual_DNS is not None:
            showIndent(outfile, level)
            outfile.write('next_virtual_DNS=%s,\n' % quote_python(self.next_virtual_DNS).encode(ExternalEncoding))
        if self.floating_ip_record is not None:
            showIndent(outfile, level)
            outfile.write('floating_ip_record=%s,\n' % quote_python(self.floating_ip_record).encode(ExternalEncoding))
    def exportDict(self, name_='VirtualDnsType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'domain-name':
            domain_name_ = child_.text
            domain_name_ = self.gds_validate_string(domain_name_, node, 'domain_name')
            self.domain_name = domain_name_
        elif nodeName_ == 'dynamic-records-from-client':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'dynamic_records_from_client')
            self.dynamic_records_from_client = ival_
        elif nodeName_ == 'record-order':
            record_order_ = child_.text
            record_order_ = self.gds_validate_string(record_order_, node, 'record_order')
            self.record_order = record_order_
            self.validate_DnsRecordOrderType(self.record_order)    # validate type DnsRecordOrderType
        elif nodeName_ == 'default-ttl-seconds':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'default_ttl_seconds')
            self.default_ttl_seconds = ival_
        elif nodeName_ == 'next-virtual-DNS':
            next_virtual_DNS_ = child_.text
            next_virtual_DNS_ = self.gds_validate_string(next_virtual_DNS_, node, 'next_virtual_DNS')
            self.next_virtual_DNS = next_virtual_DNS_
        elif nodeName_ == 'floating-ip-record':
            floating_ip_record_ = child_.text
            floating_ip_record_ = self.gds_validate_string(floating_ip_record_, node, 'floating_ip_record')
            self.floating_ip_record = floating_ip_record_
            self.validate_FloatingIpDnsNotation(self.floating_ip_record)    # validate type FloatingIpDnsNotation
# end class VirtualDnsType


class VirtualDnsRecordType(GeneratedsSuper):
    """
    VirtualDnsRecordType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, record_name=None, record_type=None, record_class=None, record_data=None, record_ttl_seconds=None, record_mx_preference=None, **kwargs):
        self.record_name = record_name
        self.record_type = record_type
        self.record_class = record_class
        self.record_data = record_data
        self.record_ttl_seconds = record_ttl_seconds
        self.record_mx_preference = record_mx_preference
    def factory(*args_, **kwargs_):
        if VirtualDnsRecordType.subclass:
            return VirtualDnsRecordType.subclass(*args_, **kwargs_)
        else:
            return VirtualDnsRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_record_name(self): return self.record_name
    def set_record_name(self, record_name): self.record_name = record_name
    def get_record_type(self): return self.record_type
    def set_record_type(self, record_type): self.record_type = record_type
    def validate_DnsRecordTypeType(self, value):
        # Validate type DnsRecordTypeType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'A', u'AAAA', u'CNAME', u'PTR', u'NS', u'MX'])
        else:
            error = value not in [u'A', u'AAAA', u'CNAME', u'PTR', u'NS', u'MX']
        if error:
            raise ValueError("DnsRecordTypeType must be one of [u'A', u'AAAA', u'CNAME', u'PTR', u'NS', u'MX']")
    def get_record_class(self): return self.record_class
    def set_record_class(self, record_class): self.record_class = record_class
    def validate_DnsRecordClassType(self, value):
        # Validate type DnsRecordClassType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'IN'])
        else:
            error = value not in [u'IN']
        if error:
            raise ValueError("DnsRecordClassType must be one of [u'IN']")
    def get_record_data(self): return self.record_data
    def set_record_data(self, record_data): self.record_data = record_data
    def get_record_ttl_seconds(self): return self.record_ttl_seconds
    def set_record_ttl_seconds(self, record_ttl_seconds): self.record_ttl_seconds = record_ttl_seconds
    def get_record_mx_preference(self): return self.record_mx_preference
    def set_record_mx_preference(self, record_mx_preference): self.record_mx_preference = record_mx_preference
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.record_name == other.record_name and
                self.record_type == other.record_type and
                self.record_class == other.record_class and
                self.record_data == other.record_data and
                self.record_ttl_seconds == other.record_ttl_seconds and
                self.record_mx_preference == other.record_mx_preference)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_record_name (obj.populate_string ("record_name"))
        obj.set_record_type (obj.populate_string ("record_type"))
        obj.set_record_class (obj.populate_string ("record_class"))
        obj.set_record_data (obj.populate_string ("record_data"))
        obj.set_record_ttl_seconds (obj.populate_integer ("record_ttl_seconds"))
        obj.set_record_mx_preference (obj.populate_integer ("record_mx_preference"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VirtualDnsRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VirtualDnsRecordType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VirtualDnsRecordType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VirtualDnsRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.record_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srecord-name>%s</%srecord-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.record_name).encode(ExternalEncoding), input_name='record-name'), namespace_, eol_))
        if self.record_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srecord-type>%s</%srecord-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.record_type).encode(ExternalEncoding), input_name='record-type'), namespace_, eol_))
        if self.record_class is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srecord-class>%s</%srecord-class>%s' % (namespace_, self.gds_format_string(quote_xml(self.record_class).encode(ExternalEncoding), input_name='record-class'), namespace_, eol_))
        if self.record_data is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srecord-data>%s</%srecord-data>%s' % (namespace_, self.gds_format_string(quote_xml(self.record_data).encode(ExternalEncoding), input_name='record-data'), namespace_, eol_))
        if self.record_ttl_seconds is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srecord-ttl-seconds>%s</%srecord-ttl-seconds>%s' % (namespace_, self.gds_format_integer(self.record_ttl_seconds, input_name='record-ttl-seconds'), namespace_, eol_))
        if self.record_mx_preference is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srecord-mx-preference>%s</%srecord-mx-preference>%s' % (namespace_, self.gds_format_integer(self.record_mx_preference, input_name='record-mx-preference'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.record_name is not None or
            self.record_type is not None or
            self.record_class is not None or
            self.record_data is not None or
            self.record_ttl_seconds is not None or
            self.record_mx_preference is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VirtualDnsRecordType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.record_name is not None:
            showIndent(outfile, level)
            outfile.write('record_name=%s,\n' % quote_python(self.record_name).encode(ExternalEncoding))
        if self.record_type is not None:
            showIndent(outfile, level)
            outfile.write('record_type=%s,\n' % quote_python(self.record_type).encode(ExternalEncoding))
        if self.record_class is not None:
            showIndent(outfile, level)
            outfile.write('record_class=%s,\n' % quote_python(self.record_class).encode(ExternalEncoding))
        if self.record_data is not None:
            showIndent(outfile, level)
            outfile.write('record_data=%s,\n' % quote_python(self.record_data).encode(ExternalEncoding))
        if self.record_ttl_seconds is not None:
            showIndent(outfile, level)
            outfile.write('record_ttl_seconds=%d,\n' % self.record_ttl_seconds)
        if self.record_mx_preference is not None:
            showIndent(outfile, level)
            outfile.write('record_mx_preference=%d,\n' % self.record_mx_preference)
    def exportDict(self, name_='VirtualDnsRecordType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'record-name':
            record_name_ = child_.text
            record_name_ = self.gds_validate_string(record_name_, node, 'record_name')
            self.record_name = record_name_
        elif nodeName_ == 'record-type':
            record_type_ = child_.text
            record_type_ = self.gds_validate_string(record_type_, node, 'record_type')
            self.record_type = record_type_
            self.validate_DnsRecordTypeType(self.record_type)    # validate type DnsRecordTypeType
        elif nodeName_ == 'record-class':
            record_class_ = child_.text
            record_class_ = self.gds_validate_string(record_class_, node, 'record_class')
            self.record_class = record_class_
            self.validate_DnsRecordClassType(self.record_class)    # validate type DnsRecordClassType
        elif nodeName_ == 'record-data':
            record_data_ = child_.text
            record_data_ = self.gds_validate_string(record_data_, node, 'record_data')
            self.record_data = record_data_
        elif nodeName_ == 'record-ttl-seconds':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'record_ttl_seconds')
            self.record_ttl_seconds = ival_
        elif nodeName_ == 'record-mx-preference':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'record_mx_preference')
            self.record_mx_preference = ival_
# end class VirtualDnsRecordType


class FloatingIpPoolType(GeneratedsSuper):
    """
    FloatingIpPoolType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, subnet=None, **kwargs):
        if (subnet is None) or (subnet == []):
            self.subnet = []
        else:
            if isinstance(subnet[0], dict):
                objs = [SubnetType(**elem) for elem in subnet]
                self.subnet = objs
            else:
                self.subnet = subnet
    def factory(*args_, **kwargs_):
        if FloatingIpPoolType.subclass:
            return FloatingIpPoolType.subclass(*args_, **kwargs_)
        else:
            return FloatingIpPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_subnet(self): return self.subnet
    def set_subnet(self, subnet): self.subnet = subnet
    def add_subnet(self, value): self.subnet.append(value)
    def insert_subnet(self, index, value): self.subnet[index] = value
    def delete_subnet(self, value): self.subnet.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.subnet == other.subnet)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_subnet ([SubnetType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='FloatingIpPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FloatingIpPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='FloatingIpPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='FloatingIpPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for subnet_ in self.subnet:
            if isinstance(subnet_, dict):
                subnet_ = SubnetType(**subnet_)
            subnet_.export(outfile, level, namespace_, name_='subnet', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.subnet
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='FloatingIpPoolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('subnet=[\n')
        level += 1
        for subnet_ in self.subnet:
            showIndent(outfile, level)
            outfile.write('model_.SubnetType(\n')
            subnet_.exportLiteral(outfile, level, name_='SubnetType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='FloatingIpPoolType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'subnet':
            obj_ = SubnetType.factory()
            obj_.build(child_)
            self.subnet.append(obj_)
# end class FloatingIpPoolType


class SubnetListType(GeneratedsSuper):
    """
    SubnetListType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, subnet=None, **kwargs):
        if (subnet is None) or (subnet == []):
            self.subnet = []
        else:
            if isinstance(subnet[0], dict):
                objs = [SubnetType(**elem) for elem in subnet]
                self.subnet = objs
            else:
                self.subnet = subnet
    def factory(*args_, **kwargs_):
        if SubnetListType.subclass:
            return SubnetListType.subclass(*args_, **kwargs_)
        else:
            return SubnetListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_subnet(self): return self.subnet
    def set_subnet(self, subnet): self.subnet = subnet
    def add_subnet(self, value): self.subnet.append(value)
    def insert_subnet(self, index, value): self.subnet[index] = value
    def delete_subnet(self, value): self.subnet.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.subnet == other.subnet)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_subnet ([SubnetType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='SubnetListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SubnetListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SubnetListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='SubnetListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for subnet_ in self.subnet:
            if isinstance(subnet_, dict):
                subnet_ = SubnetType(**subnet_)
            subnet_.export(outfile, level, namespace_, name_='subnet', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.subnet
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='SubnetListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('subnet=[\n')
        level += 1
        for subnet_ in self.subnet:
            showIndent(outfile, level)
            outfile.write('model_.SubnetType(\n')
            subnet_.exportLiteral(outfile, level, name_='SubnetType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='SubnetListType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'subnet':
            obj_ = SubnetType.factory()
            obj_.build(child_)
            self.subnet.append(obj_)
# end class SubnetListType


class IpamSubnetType(GeneratedsSuper):
    """
    IpamSubnetType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, subnet=None, default_gateway=None, dns_server_address=None, subnet_uuid=None, enable_dhcp=True, dns_nameservers=None, allocation_pools=None, addr_from_start=None, dhcp_option_list=None, host_routes=None, subnet_name=None, **kwargs):
        if isinstance(subnet, dict):
            obj = SubnetType(**subnet)
            self.subnet = obj
        else:
            self.subnet = subnet
        self.default_gateway = default_gateway
        self.dns_server_address = dns_server_address
        self.subnet_uuid = subnet_uuid
        self.enable_dhcp = enable_dhcp
        if (dns_nameservers is None) or (dns_nameservers == []):
            self.dns_nameservers = []
        else:
            self.dns_nameservers = dns_nameservers
        if (allocation_pools is None) or (allocation_pools == []):
            self.allocation_pools = []
        else:
            if isinstance(allocation_pools[0], dict):
                objs = [AllocationPoolType(**elem) for elem in allocation_pools]
                self.allocation_pools = objs
            else:
                self.allocation_pools = allocation_pools
        self.addr_from_start = addr_from_start
        if isinstance(dhcp_option_list, dict):
            obj = DhcpOptionsListType(**dhcp_option_list)
            self.dhcp_option_list = obj
        else:
            self.dhcp_option_list = dhcp_option_list
        if isinstance(host_routes, dict):
            obj = RouteTableType(**host_routes)
            self.host_routes = obj
        else:
            self.host_routes = host_routes
        self.subnet_name = subnet_name
    def factory(*args_, **kwargs_):
        if IpamSubnetType.subclass:
            return IpamSubnetType.subclass(*args_, **kwargs_)
        else:
            return IpamSubnetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_subnet(self): return self.subnet
    def set_subnet(self, subnet): self.subnet = subnet
    def get_default_gateway(self): return self.default_gateway
    def set_default_gateway(self, default_gateway): self.default_gateway = default_gateway
    def validate_IpAddressType(self, value):
        # Validate type IpAddressType, a restriction on xsd:string.
        pass
    def get_dns_server_address(self): return self.dns_server_address
    def set_dns_server_address(self, dns_server_address): self.dns_server_address = dns_server_address
    def get_subnet_uuid(self): return self.subnet_uuid
    def set_subnet_uuid(self, subnet_uuid): self.subnet_uuid = subnet_uuid
    def get_enable_dhcp(self): return self.enable_dhcp
    def set_enable_dhcp(self, enable_dhcp): self.enable_dhcp = enable_dhcp
    def get_dns_nameservers(self): return self.dns_nameservers
    def set_dns_nameservers(self, dns_nameservers): self.dns_nameservers = dns_nameservers
    def add_dns_nameservers(self, value): self.dns_nameservers.append(value)
    def insert_dns_nameservers(self, index, value): self.dns_nameservers[index] = value
    def delete_dns_nameservers(self, value): self.dns_nameservers.remove(value)
    def get_allocation_pools(self): return self.allocation_pools
    def set_allocation_pools(self, allocation_pools): self.allocation_pools = allocation_pools
    def add_allocation_pools(self, value): self.allocation_pools.append(value)
    def insert_allocation_pools(self, index, value): self.allocation_pools[index] = value
    def delete_allocation_pools(self, value): self.allocation_pools.remove(value)
    def get_addr_from_start(self): return self.addr_from_start
    def set_addr_from_start(self, addr_from_start): self.addr_from_start = addr_from_start
    def get_dhcp_option_list(self): return self.dhcp_option_list
    def set_dhcp_option_list(self, dhcp_option_list): self.dhcp_option_list = dhcp_option_list
    def get_host_routes(self): return self.host_routes
    def set_host_routes(self, host_routes): self.host_routes = host_routes
    def get_subnet_name(self): return self.subnet_name
    def set_subnet_name(self, subnet_name): self.subnet_name = subnet_name
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.subnet == other.subnet and
                self.default_gateway == other.default_gateway and
                self.dns_server_address == other.dns_server_address and
                self.subnet_uuid == other.subnet_uuid and
                self.enable_dhcp == other.enable_dhcp and
                self.dns_nameservers == other.dns_nameservers and
                self.allocation_pools == other.allocation_pools and
                self.addr_from_start == other.addr_from_start and
                self.dhcp_option_list == other.dhcp_option_list and
                self.host_routes == other.host_routes and
                self.subnet_name == other.subnet_name)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_subnet (SubnetType.populate ())
        obj.set_default_gateway (obj.populate_string ("default_gateway"))
        obj.set_dns_server_address (obj.populate_string ("dns_server_address"))
        obj.set_subnet_uuid (obj.populate_string ("subnet_uuid"))
        obj.set_enable_dhcp (obj.populate_boolean ("enable_dhcp"))
        obj.set_dns_nameservers ([obj.populate_string ("dns_nameservers")])
        obj.set_allocation_pools ([AllocationPoolType.populate ()])
        obj.set_addr_from_start (obj.populate_boolean ("addr_from_start"))
        obj.set_dhcp_option_list (DhcpOptionsListType.populate ())
        obj.set_host_routes (RouteTableType.populate ())
        obj.set_subnet_name (obj.populate_string ("subnet_name"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='IpamSubnetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IpamSubnetType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IpamSubnetType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='IpamSubnetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.subnet is not None:
            self.subnet.export(outfile, level, namespace_, name_='subnet', pretty_print=pretty_print)
        if self.default_gateway is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdefault-gateway>%s</%sdefault-gateway>%s' % (namespace_, self.gds_format_string(quote_xml(self.default_gateway).encode(ExternalEncoding), input_name='default-gateway'), namespace_, eol_))
        if self.dns_server_address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdns-server-address>%s</%sdns-server-address>%s' % (namespace_, self.gds_format_string(quote_xml(self.dns_server_address).encode(ExternalEncoding), input_name='dns-server-address'), namespace_, eol_))
        if self.subnet_uuid is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssubnet-uuid>%s</%ssubnet-uuid>%s' % (namespace_, self.gds_format_string(quote_xml(self.subnet_uuid).encode(ExternalEncoding), input_name='subnet-uuid'), namespace_, eol_))
        if self.enable_dhcp is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%senable-dhcp>%s</%senable-dhcp>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.enable_dhcp)), input_name='enable-dhcp'), namespace_, eol_))
        for dns_nameservers_ in self.dns_nameservers:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdns-nameservers>%s</%sdns-nameservers>%s' % (namespace_, self.gds_format_string(quote_xml(dns_nameservers_).encode(ExternalEncoding), input_name='dns-nameservers'), namespace_, eol_))
        for allocation_pools_ in self.allocation_pools:
            if isinstance(allocation_pools_, dict):
                allocation_pools_ = AllocationPoolType(**allocation_pools_)
            allocation_pools_.export(outfile, level, namespace_, name_='allocation-pools', pretty_print=pretty_print)
        if self.addr_from_start is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddr_from_start>%s</%saddr_from_start>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.addr_from_start)), input_name='addr_from_start'), namespace_, eol_))
        if self.dhcp_option_list is not None:
            self.dhcp_option_list.export(outfile, level, namespace_, name_='dhcp-option-list', pretty_print=pretty_print)
        if self.host_routes is not None:
            self.host_routes.export(outfile, level, namespace_, name_='host-routes', pretty_print=pretty_print)
        if self.subnet_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssubnet-name>%s</%ssubnet-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.subnet_name).encode(ExternalEncoding), input_name='subnet-name'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.subnet is not None or
            self.default_gateway is not None or
            self.dns_server_address is not None or
            self.subnet_uuid is not None or
            self.enable_dhcp is not None or
            self.dns_nameservers or
            self.allocation_pools or
            self.addr_from_start is not None or
            self.dhcp_option_list is not None or
            self.host_routes is not None or
            self.subnet_name is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IpamSubnetType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.subnet is not None:
            showIndent(outfile, level)
            outfile.write('subnet=model_.SubnetType(\n')
            self.subnet.exportLiteral(outfile, level, name_='subnet')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.default_gateway is not None:
            showIndent(outfile, level)
            outfile.write('default_gateway=%s,\n' % quote_python(self.default_gateway).encode(ExternalEncoding))
        if self.dns_server_address is not None:
            showIndent(outfile, level)
            outfile.write('dns_server_address=%s,\n' % quote_python(self.dns_server_address).encode(ExternalEncoding))
        if self.subnet_uuid is not None:
            showIndent(outfile, level)
            outfile.write('subnet_uuid=%s,\n' % quote_python(self.subnet_uuid).encode(ExternalEncoding))
        if self.enable_dhcp is not None:
            showIndent(outfile, level)
            outfile.write('enable_dhcp=%s,\n' % self.enable_dhcp)
        showIndent(outfile, level)
        outfile.write('dns_nameservers=[\n')
        level += 1
        for dns_nameservers_ in self.dns_nameservers:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(dns_nameservers_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('allocation_pools=[\n')
        level += 1
        for allocation_pools_ in self.allocation_pools:
            showIndent(outfile, level)
            outfile.write('model_.AllocationPoolType(\n')
            allocation_pools_.exportLiteral(outfile, level, name_='AllocationPoolType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.addr_from_start is not None:
            showIndent(outfile, level)
            outfile.write('addr_from_start=%s,\n' % self.addr_from_start)
        if self.dhcp_option_list is not None:
            showIndent(outfile, level)
            outfile.write('dhcp_option_list=model_.DhcpOptionsListType(\n')
            self.dhcp_option_list.exportLiteral(outfile, level, name_='dhcp_option_list')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.host_routes is not None:
            showIndent(outfile, level)
            outfile.write('host_routes=model_.RouteTableType(\n')
            self.host_routes.exportLiteral(outfile, level, name_='host_routes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.subnet_name is not None:
            showIndent(outfile, level)
            outfile.write('subnet_name=%s,\n' % quote_python(self.subnet_name).encode(ExternalEncoding))
    def exportDict(self, name_='IpamSubnetType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'subnet':
            obj_ = SubnetType.factory()
            obj_.build(child_)
            self.set_subnet(obj_)
        elif nodeName_ == 'default-gateway':
            default_gateway_ = child_.text
            default_gateway_ = self.gds_validate_string(default_gateway_, node, 'default_gateway')
            self.default_gateway = default_gateway_
            self.validate_IpAddressType(self.default_gateway)    # validate type IpAddressType
        elif nodeName_ == 'dns-server-address':
            dns_server_address_ = child_.text
            dns_server_address_ = self.gds_validate_string(dns_server_address_, node, 'dns_server_address')
            self.dns_server_address = dns_server_address_
            self.validate_IpAddressType(self.dns_server_address)    # validate type IpAddressType
        elif nodeName_ == 'subnet-uuid':
            subnet_uuid_ = child_.text
            subnet_uuid_ = self.gds_validate_string(subnet_uuid_, node, 'subnet_uuid')
            self.subnet_uuid = subnet_uuid_
        elif nodeName_ == 'enable-dhcp':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'enable_dhcp')
            self.enable_dhcp = ival_
        elif nodeName_ == 'dns-nameservers':
            dns_nameservers_ = child_.text
            dns_nameservers_ = self.gds_validate_string(dns_nameservers_, node, 'dns_nameservers')
            self.dns_nameservers.append(dns_nameservers_)
        elif nodeName_ == 'allocation-pools':
            obj_ = AllocationPoolType.factory()
            obj_.build(child_)
            self.allocation_pools.append(obj_)
        elif nodeName_ == 'addr_from_start':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'addr_from_start')
            self.addr_from_start = ival_
        elif nodeName_ == 'dhcp-option-list':
            obj_ = DhcpOptionsListType.factory()
            obj_.build(child_)
            self.set_dhcp_option_list(obj_)
        elif nodeName_ == 'host-routes':
            obj_ = RouteTableType.factory()
            obj_.build(child_)
            self.set_host_routes(obj_)
        elif nodeName_ == 'subnet-name':
            subnet_name_ = child_.text
            subnet_name_ = self.gds_validate_string(subnet_name_, node, 'subnet_name')
            self.subnet_name = subnet_name_
# end class IpamSubnetType


class VnSubnetsType(GeneratedsSuper):
    """
    VnSubnetsType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, ipam_subnets=None, host_routes=None, **kwargs):
        if (ipam_subnets is None) or (ipam_subnets == []):
            self.ipam_subnets = []
        else:
            if isinstance(ipam_subnets[0], dict):
                objs = [IpamSubnetType(**elem) for elem in ipam_subnets]
                self.ipam_subnets = objs
            else:
                self.ipam_subnets = ipam_subnets
        if isinstance(host_routes, dict):
            obj = RouteTableType(**host_routes)
            self.host_routes = obj
        else:
            self.host_routes = host_routes
    def factory(*args_, **kwargs_):
        if VnSubnetsType.subclass:
            return VnSubnetsType.subclass(*args_, **kwargs_)
        else:
            return VnSubnetsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ipam_subnets(self): return self.ipam_subnets
    def set_ipam_subnets(self, ipam_subnets): self.ipam_subnets = ipam_subnets
    def add_ipam_subnets(self, value): self.ipam_subnets.append(value)
    def insert_ipam_subnets(self, index, value): self.ipam_subnets[index] = value
    def delete_ipam_subnets(self, value): self.ipam_subnets.remove(value)
    def get_host_routes(self): return self.host_routes
    def set_host_routes(self, host_routes): self.host_routes = host_routes
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.ipam_subnets == other.ipam_subnets and
                self.host_routes == other.host_routes)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_ipam_subnets ([IpamSubnetType.populate ()])
        obj.set_host_routes (RouteTableType.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VnSubnetsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VnSubnetsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VnSubnetsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VnSubnetsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for ipam_subnets_ in self.ipam_subnets:
            if isinstance(ipam_subnets_, dict):
                ipam_subnets_ = IpamSubnetType(**ipam_subnets_)
            ipam_subnets_.export(outfile, level, namespace_, name_='ipam-subnets', pretty_print=pretty_print)
        if self.host_routes is not None:
            self.host_routes.export(outfile, level, namespace_, name_='host-routes', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.ipam_subnets or
            self.host_routes is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VnSubnetsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('ipam_subnets=[\n')
        level += 1
        for ipam_subnets_ in self.ipam_subnets:
            showIndent(outfile, level)
            outfile.write('model_.IpamSubnetType(\n')
            ipam_subnets_.exportLiteral(outfile, level, name_='IpamSubnetType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.host_routes is not None:
            showIndent(outfile, level)
            outfile.write('host_routes=model_.RouteTableType(\n')
            self.host_routes.exportLiteral(outfile, level, name_='host_routes')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='VnSubnetsType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ipam-subnets':
            obj_ = IpamSubnetType.factory()
            obj_.build(child_)
            self.ipam_subnets.append(obj_)
        elif nodeName_ == 'host-routes':
            obj_ = RouteTableType.factory()
            obj_.build(child_)
            self.set_host_routes(obj_)
# end class VnSubnetsType


class DomainLimitsType(GeneratedsSuper):
    """
    DomainLimitsType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, project_limit=None, virtual_network_limit=None, security_group_limit=None, **kwargs):
        self.project_limit = project_limit
        self.virtual_network_limit = virtual_network_limit
        self.security_group_limit = security_group_limit
    def factory(*args_, **kwargs_):
        if DomainLimitsType.subclass:
            return DomainLimitsType.subclass(*args_, **kwargs_)
        else:
            return DomainLimitsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_project_limit(self): return self.project_limit
    def set_project_limit(self, project_limit): self.project_limit = project_limit
    def get_virtual_network_limit(self): return self.virtual_network_limit
    def set_virtual_network_limit(self, virtual_network_limit): self.virtual_network_limit = virtual_network_limit
    def get_security_group_limit(self): return self.security_group_limit
    def set_security_group_limit(self, security_group_limit): self.security_group_limit = security_group_limit
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.project_limit == other.project_limit and
                self.virtual_network_limit == other.virtual_network_limit and
                self.security_group_limit == other.security_group_limit)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_project_limit (obj.populate_integer ("project_limit"))
        obj.set_virtual_network_limit (obj.populate_integer ("virtual_network_limit"))
        obj.set_security_group_limit (obj.populate_integer ("security_group_limit"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='DomainLimitsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DomainLimitsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DomainLimitsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='DomainLimitsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.project_limit is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproject-limit>%s</%sproject-limit>%s' % (namespace_, self.gds_format_integer(self.project_limit, input_name='project-limit'), namespace_, eol_))
        if self.virtual_network_limit is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-network-limit>%s</%svirtual-network-limit>%s' % (namespace_, self.gds_format_integer(self.virtual_network_limit, input_name='virtual-network-limit'), namespace_, eol_))
        if self.security_group_limit is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssecurity-group-limit>%s</%ssecurity-group-limit>%s' % (namespace_, self.gds_format_integer(self.security_group_limit, input_name='security-group-limit'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.project_limit is not None or
            self.virtual_network_limit is not None or
            self.security_group_limit is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DomainLimitsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.project_limit is not None:
            showIndent(outfile, level)
            outfile.write('project_limit=%d,\n' % self.project_limit)
        if self.virtual_network_limit is not None:
            showIndent(outfile, level)
            outfile.write('virtual_network_limit=%d,\n' % self.virtual_network_limit)
        if self.security_group_limit is not None:
            showIndent(outfile, level)
            outfile.write('security_group_limit=%d,\n' % self.security_group_limit)
    def exportDict(self, name_='DomainLimitsType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'project-limit':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'project_limit')
            self.project_limit = ival_
        elif nodeName_ == 'virtual-network-limit':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'virtual_network_limit')
            self.virtual_network_limit = ival_
        elif nodeName_ == 'security-group-limit':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'security_group_limit')
            self.security_group_limit = ival_
# end class DomainLimitsType


class PermType(GeneratedsSuper):
    """
    PermType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, owner=None, owner_access=None, group=None, group_access=None, other_access=None, **kwargs):
        self.owner = owner
        self.owner_access = owner_access
        self.group = group
        self.group_access = group_access
        self.other_access = other_access
    def factory(*args_, **kwargs_):
        if PermType.subclass:
            return PermType.subclass(*args_, **kwargs_)
        else:
            return PermType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_owner(self): return self.owner
    def set_owner(self, owner): self.owner = owner
    def get_owner_access(self): return self.owner_access
    def set_owner_access(self, owner_access): self.owner_access = owner_access
    def validate_AccessType(self, value):
        # Validate type AccessType, a restriction on xsd:integer.
        error = False
        if isinstance(value, list):
            v_int = map(int, value)
            v1, v2 = min(v_int), max(v_int)
        else:
            v1, v2 = int(value), int(value)
        error = (0 > v1)
        error |= (v2 > 7)
        if error:
            raise ValueError("AccessType must be in the range 0-7")
    def get_group(self): return self.group
    def set_group(self, group): self.group = group
    def get_group_access(self): return self.group_access
    def set_group_access(self, group_access): self.group_access = group_access
    def get_other_access(self): return self.other_access
    def set_other_access(self, other_access): self.other_access = other_access
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.owner == other.owner and
                self.owner_access == other.owner_access and
                self.group == other.group and
                self.group_access == other.group_access and
                self.other_access == other.other_access)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_owner (obj.populate_string ("owner"))
        obj.set_owner_access (obj.populate_integer ("owner_access"))
        obj.set_group (obj.populate_string ("group"))
        obj.set_group_access (obj.populate_integer ("group_access"))
        obj.set_other_access (obj.populate_integer ("other_access"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='PermType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PermType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PermType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PermType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.owner is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sowner>%s</%sowner>%s' % (namespace_, self.gds_format_string(quote_xml(self.owner).encode(ExternalEncoding), input_name='owner'), namespace_, eol_))
        if self.owner_access is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sowner-access>%s</%sowner-access>%s' % (namespace_, self.gds_format_integer(self.owner_access, input_name='owner-access'), namespace_, eol_))
        if self.group is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgroup>%s</%sgroup>%s' % (namespace_, self.gds_format_string(quote_xml(self.group).encode(ExternalEncoding), input_name='group'), namespace_, eol_))
        if self.group_access is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sgroup-access>%s</%sgroup-access>%s' % (namespace_, self.gds_format_integer(self.group_access, input_name='group-access'), namespace_, eol_))
        if self.other_access is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sother-access>%s</%sother-access>%s' % (namespace_, self.gds_format_integer(self.other_access, input_name='other-access'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.owner is not None or
            self.owner_access is not None or
            self.group is not None or
            self.group_access is not None or
            self.other_access is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PermType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.owner is not None:
            showIndent(outfile, level)
            outfile.write('owner=%s,\n' % quote_python(self.owner).encode(ExternalEncoding))
        if self.owner_access is not None:
            showIndent(outfile, level)
            outfile.write('owner_access=%d,\n' % self.owner_access)
        if self.group is not None:
            showIndent(outfile, level)
            outfile.write('group=%s,\n' % quote_python(self.group).encode(ExternalEncoding))
        if self.group_access is not None:
            showIndent(outfile, level)
            outfile.write('group_access=%d,\n' % self.group_access)
        if self.other_access is not None:
            showIndent(outfile, level)
            outfile.write('other_access=%d,\n' % self.other_access)
    def exportDict(self, name_='PermType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'owner':
            owner_ = child_.text
            owner_ = self.gds_validate_string(owner_, node, 'owner')
            self.owner = owner_
        elif nodeName_ == 'owner-access':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'owner_access')
            self.owner_access = ival_
            self.validate_AccessType(self.owner_access)    # validate type AccessType
        elif nodeName_ == 'group':
            group_ = child_.text
            group_ = self.gds_validate_string(group_, node, 'group')
            self.group = group_
        elif nodeName_ == 'group-access':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'group_access')
            self.group_access = ival_
            self.validate_AccessType(self.group_access)    # validate type AccessType
        elif nodeName_ == 'other-access':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'other_access')
            self.other_access = ival_
            self.validate_AccessType(self.other_access)    # validate type AccessType
# end class PermType


class IdPermsType(GeneratedsSuper):
    """
    IdPermsType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, permissions=None, uuid=None, enable=None, created=None, last_modified=None, description=None, user_visible=True, creator=None, **kwargs):
        if isinstance(permissions, dict):
            obj = PermType(**permissions)
            self.permissions = obj
        else:
            self.permissions = permissions
        if isinstance(uuid, dict):
            obj = UuidType(**uuid)
            self.uuid = obj
        else:
            self.uuid = uuid
        self.enable = enable
        self.created = created
        self.last_modified = last_modified
        self.description = description
        self.user_visible = user_visible
        self.creator = creator
    def factory(*args_, **kwargs_):
        if IdPermsType.subclass:
            return IdPermsType.subclass(*args_, **kwargs_)
        else:
            return IdPermsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_permissions(self): return self.permissions
    def set_permissions(self, permissions): self.permissions = permissions
    def get_uuid(self): return self.uuid
    def set_uuid(self, uuid): self.uuid = uuid
    def get_enable(self): return self.enable
    def set_enable(self, enable): self.enable = enable
    def get_created(self): return self.created
    def set_created(self, created): self.created = created
    def get_last_modified(self): return self.last_modified
    def set_last_modified(self, last_modified): self.last_modified = last_modified
    def get_description(self): return self.description
    def set_description(self, description): self.description = description
    def get_user_visible(self): return self.user_visible
    def set_user_visible(self, user_visible): self.user_visible = user_visible
    def get_creator(self): return self.creator
    def set_creator(self, creator): self.creator = creator
    def validate_CreatorType(self, value):
        # Validate type CreatorType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'vcenter-plugin', u'test'])
        else:
            error = value not in [u'vcenter-plugin', u'test']
        if error:
            raise ValueError("CreatorType must be one of [u'vcenter-plugin', u'test']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.permissions == other.permissions and
                self.uuid == other.uuid and
                self.enable == other.enable and
                self.created == other.created and
                self.last_modified == other.last_modified and
                self.description == other.description and
                self.user_visible == other.user_visible and
                self.creator == other.creator)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_permissions (PermType.populate ())
        obj.set_uuid (UuidType.populate ())
        obj.set_enable (obj.populate_boolean ("enable"))
        obj.set_created (obj.populate_dateTime ("created"))
        obj.set_last_modified (obj.populate_dateTime ("last_modified"))
        obj.set_description (obj.populate_string ("description"))
        obj.set_user_visible (obj.populate_boolean ("user_visible"))
        obj.set_creator (obj.populate_string ("creator"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='IdPermsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IdPermsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IdPermsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='IdPermsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.permissions is not None:
            self.permissions.export(outfile, level, namespace_, name_='permissions', pretty_print=pretty_print)
        if self.uuid is not None:
            self.uuid.export(outfile, level, namespace_, name_='uuid', pretty_print=pretty_print)
        if self.enable is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%senable>%s</%senable>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.enable)), input_name='enable'), namespace_, eol_))
        if self.created is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%screated>%s</%screated>%s' % (namespace_, self.gds_format_string(quote_xml(self.created).encode(ExternalEncoding), input_name='created'), namespace_, eol_))
        if self.last_modified is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slast-modified>%s</%slast-modified>%s' % (namespace_, self.gds_format_string(quote_xml(self.last_modified).encode(ExternalEncoding), input_name='last-modified'), namespace_, eol_))
        if self.description is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdescription>%s</%sdescription>%s' % (namespace_, self.gds_format_string(quote_xml(self.description).encode(ExternalEncoding), input_name='description'), namespace_, eol_))
        if self.user_visible is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suser-visible>%s</%suser-visible>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.user_visible)), input_name='user-visible'), namespace_, eol_))
        if self.creator is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%screator>%s</%screator>%s' % (namespace_, self.gds_format_string(quote_xml(self.creator).encode(ExternalEncoding), input_name='creator'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.permissions is not None or
            self.uuid is not None or
            self.enable is not None or
            self.created is not None or
            self.last_modified is not None or
            self.description is not None or
            self.user_visible is not None or
            self.creator is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IdPermsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.permissions is not None:
            showIndent(outfile, level)
            outfile.write('permissions=model_.PermType(\n')
            self.permissions.exportLiteral(outfile, level, name_='permissions')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.uuid is not None:
            showIndent(outfile, level)
            outfile.write('uuid=model_.UuidType(\n')
            self.uuid.exportLiteral(outfile, level, name_='uuid')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.enable is not None:
            showIndent(outfile, level)
            outfile.write('enable=%s,\n' % self.enable)
        if self.created is not None:
            showIndent(outfile, level)
            outfile.write('created=%s,\n' % quote_python(self.created).encode(ExternalEncoding))
        if self.last_modified is not None:
            showIndent(outfile, level)
            outfile.write('last_modified=%s,\n' % quote_python(self.last_modified).encode(ExternalEncoding))
        if self.description is not None:
            showIndent(outfile, level)
            outfile.write('description=%s,\n' % quote_python(self.description).encode(ExternalEncoding))
        if self.user_visible is not None:
            showIndent(outfile, level)
            outfile.write('user_visible=%s,\n' % self.user_visible)
        if self.creator is not None:
            showIndent(outfile, level)
            outfile.write('creator=%s,\n' % quote_python(self.creator).encode(ExternalEncoding))
    def exportDict(self, name_='IdPermsType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'permissions':
            obj_ = PermType.factory()
            obj_.build(child_)
            self.set_permissions(obj_)
        elif nodeName_ == 'uuid':
            obj_ = UuidType.factory()
            obj_.build(child_)
            self.set_uuid(obj_)
        elif nodeName_ == 'enable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'enable')
            self.enable = ival_
        elif nodeName_ == 'created':
            created_ = child_.text
            created_ = self.gds_validate_string(created_, node, 'created')
            self.created = created_
        elif nodeName_ == 'last-modified':
            last_modified_ = child_.text
            last_modified_ = self.gds_validate_string(last_modified_, node, 'last_modified')
            self.last_modified = last_modified_
        elif nodeName_ == 'description':
            description_ = child_.text
            description_ = self.gds_validate_string(description_, node, 'description')
            self.description = description_
        elif nodeName_ == 'user-visible':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'user_visible')
            self.user_visible = ival_
        elif nodeName_ == 'creator':
            creator_ = child_.text
            creator_ = self.gds_validate_string(creator_, node, 'creator')
            self.creator = creator_
            self.validate_CreatorType(self.creator)    # validate type CreatorType
# end class IdPermsType


class PluginProperty(GeneratedsSuper):
    """
    PluginProperty class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, property=None, value=None, **kwargs):
        self.property = property
        self.value = value
    def factory(*args_, **kwargs_):
        if PluginProperty.subclass:
            return PluginProperty.subclass(*args_, **kwargs_)
        else:
            return PluginProperty(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_property(self): return self.property
    def set_property(self, property): self.property = property
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.property == other.property and
                self.value == other.value)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_property (obj.populate_string ("property"))
        obj.set_value (obj.populate_string ("value"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='PluginProperty', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PluginProperty')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PluginProperty'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PluginProperty', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.property is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sproperty>%s</%sproperty>%s' % (namespace_, self.gds_format_string(quote_xml(self.property).encode(ExternalEncoding), input_name='property'), namespace_, eol_))
        if self.value is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespace_, self.gds_format_string(quote_xml(self.value).encode(ExternalEncoding), input_name='value'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.property is not None or
            self.value is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PluginProperty'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.property is not None:
            showIndent(outfile, level)
            outfile.write('property=%s,\n' % quote_python(self.property).encode(ExternalEncoding))
        if self.value is not None:
            showIndent(outfile, level)
            outfile.write('value=%s,\n' % quote_python(self.value).encode(ExternalEncoding))
    def exportDict(self, name_='PluginProperty'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'property':
            property_ = child_.text
            property_ = self.gds_validate_string(property_, node, 'property')
            self.property = property_
        elif nodeName_ == 'value':
            value_ = child_.text
            value_ = self.gds_validate_string(value_, node, 'value')
            self.value = value_
# end class PluginProperty


class PluginProperties(GeneratedsSuper):
    """
    PluginProperties class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, plugin_property=None, **kwargs):
        if (plugin_property is None) or (plugin_property == []):
            self.plugin_property = []
        else:
            if isinstance(plugin_property[0], dict):
                objs = [PluginProperty(**elem) for elem in plugin_property]
                self.plugin_property = objs
            else:
                self.plugin_property = plugin_property
    def factory(*args_, **kwargs_):
        if PluginProperties.subclass:
            return PluginProperties.subclass(*args_, **kwargs_)
        else:
            return PluginProperties(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_plugin_property(self): return self.plugin_property
    def set_plugin_property(self, plugin_property): self.plugin_property = plugin_property
    def add_plugin_property(self, value): self.plugin_property.append(value)
    def insert_plugin_property(self, index, value): self.plugin_property[index] = value
    def delete_plugin_property(self, value): self.plugin_property.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.plugin_property == other.plugin_property)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_plugin_property ([PluginProperty.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='PluginProperties', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PluginProperties')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PluginProperties'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PluginProperties', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for plugin_property_ in self.plugin_property:
            if isinstance(plugin_property_, dict):
                plugin_property_ = PluginProperty(**plugin_property_)
            plugin_property_.export(outfile, level, namespace_, name_='plugin-property', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.plugin_property
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PluginProperties'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('plugin_property=[\n')
        level += 1
        for plugin_property_ in self.plugin_property:
            showIndent(outfile, level)
            outfile.write('model_.PluginProperty(\n')
            plugin_property_.exportLiteral(outfile, level, name_='PluginProperty')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='PluginProperties'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'plugin-property':
            obj_ = PluginProperty.factory()
            obj_.build(child_)
            self.plugin_property.append(obj_)
# end class PluginProperties


class QuotaType(GeneratedsSuper):
    """
    QuotaType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, defaults=None, floating_ip=None, instance_ip=None, virtual_machine_interface=None, virtual_network=None, virtual_router=None, virtual_DNS=None, virtual_DNS_record=None, bgp_router=None, network_ipam=None, access_control_list=None, floating_ip_pool=None, service_template=None, service_instance=None, logical_router=None, security_group=None, security_group_rule=None, subnet=None, global_vrouter_config=None, loadbalancer_pool=None, loadbalancer_member=None, loadbalancer_healthmonitor=None, virtual_ip=None, **kwargs):
        self.defaults = defaults
        self.floating_ip = floating_ip
        self.instance_ip = instance_ip
        self.virtual_machine_interface = virtual_machine_interface
        self.virtual_network = virtual_network
        self.virtual_router = virtual_router
        self.virtual_DNS = virtual_DNS
        self.virtual_DNS_record = virtual_DNS_record
        self.bgp_router = bgp_router
        self.network_ipam = network_ipam
        self.access_control_list = access_control_list
        self.floating_ip_pool = floating_ip_pool
        self.service_template = service_template
        self.service_instance = service_instance
        self.logical_router = logical_router
        self.security_group = security_group
        self.security_group_rule = security_group_rule
        self.subnet = subnet
        self.global_vrouter_config = global_vrouter_config
        self.loadbalancer_pool = loadbalancer_pool
        self.loadbalancer_member = loadbalancer_member
        self.loadbalancer_healthmonitor = loadbalancer_healthmonitor
        self.virtual_ip = virtual_ip
    def factory(*args_, **kwargs_):
        if QuotaType.subclass:
            return QuotaType.subclass(*args_, **kwargs_)
        else:
            return QuotaType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_defaults(self): return self.defaults
    def set_defaults(self, defaults): self.defaults = defaults
    def get_floating_ip(self): return self.floating_ip
    def set_floating_ip(self, floating_ip): self.floating_ip = floating_ip
    def get_instance_ip(self): return self.instance_ip
    def set_instance_ip(self, instance_ip): self.instance_ip = instance_ip
    def get_virtual_machine_interface(self): return self.virtual_machine_interface
    def set_virtual_machine_interface(self, virtual_machine_interface): self.virtual_machine_interface = virtual_machine_interface
    def get_virtual_network(self): return self.virtual_network
    def set_virtual_network(self, virtual_network): self.virtual_network = virtual_network
    def get_virtual_router(self): return self.virtual_router
    def set_virtual_router(self, virtual_router): self.virtual_router = virtual_router
    def get_virtual_DNS(self): return self.virtual_DNS
    def set_virtual_DNS(self, virtual_DNS): self.virtual_DNS = virtual_DNS
    def get_virtual_DNS_record(self): return self.virtual_DNS_record
    def set_virtual_DNS_record(self, virtual_DNS_record): self.virtual_DNS_record = virtual_DNS_record
    def get_bgp_router(self): return self.bgp_router
    def set_bgp_router(self, bgp_router): self.bgp_router = bgp_router
    def get_network_ipam(self): return self.network_ipam
    def set_network_ipam(self, network_ipam): self.network_ipam = network_ipam
    def get_access_control_list(self): return self.access_control_list
    def set_access_control_list(self, access_control_list): self.access_control_list = access_control_list
    def get_floating_ip_pool(self): return self.floating_ip_pool
    def set_floating_ip_pool(self, floating_ip_pool): self.floating_ip_pool = floating_ip_pool
    def get_service_template(self): return self.service_template
    def set_service_template(self, service_template): self.service_template = service_template
    def get_service_instance(self): return self.service_instance
    def set_service_instance(self, service_instance): self.service_instance = service_instance
    def get_logical_router(self): return self.logical_router
    def set_logical_router(self, logical_router): self.logical_router = logical_router
    def get_security_group(self): return self.security_group
    def set_security_group(self, security_group): self.security_group = security_group
    def get_security_group_rule(self): return self.security_group_rule
    def set_security_group_rule(self, security_group_rule): self.security_group_rule = security_group_rule
    def get_subnet(self): return self.subnet
    def set_subnet(self, subnet): self.subnet = subnet
    def get_global_vrouter_config(self): return self.global_vrouter_config
    def set_global_vrouter_config(self, global_vrouter_config): self.global_vrouter_config = global_vrouter_config
    def get_loadbalancer_pool(self): return self.loadbalancer_pool
    def set_loadbalancer_pool(self, loadbalancer_pool): self.loadbalancer_pool = loadbalancer_pool
    def get_loadbalancer_member(self): return self.loadbalancer_member
    def set_loadbalancer_member(self, loadbalancer_member): self.loadbalancer_member = loadbalancer_member
    def get_loadbalancer_healthmonitor(self): return self.loadbalancer_healthmonitor
    def set_loadbalancer_healthmonitor(self, loadbalancer_healthmonitor): self.loadbalancer_healthmonitor = loadbalancer_healthmonitor
    def get_virtual_ip(self): return self.virtual_ip
    def set_virtual_ip(self, virtual_ip): self.virtual_ip = virtual_ip
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.defaults == other.defaults and
                self.floating_ip == other.floating_ip and
                self.instance_ip == other.instance_ip and
                self.virtual_machine_interface == other.virtual_machine_interface and
                self.virtual_network == other.virtual_network and
                self.virtual_router == other.virtual_router and
                self.virtual_DNS == other.virtual_DNS and
                self.virtual_DNS_record == other.virtual_DNS_record and
                self.bgp_router == other.bgp_router and
                self.network_ipam == other.network_ipam and
                self.access_control_list == other.access_control_list and
                self.floating_ip_pool == other.floating_ip_pool and
                self.service_template == other.service_template and
                self.service_instance == other.service_instance and
                self.logical_router == other.logical_router and
                self.security_group == other.security_group and
                self.security_group_rule == other.security_group_rule and
                self.subnet == other.subnet and
                self.global_vrouter_config == other.global_vrouter_config and
                self.loadbalancer_pool == other.loadbalancer_pool and
                self.loadbalancer_member == other.loadbalancer_member and
                self.loadbalancer_healthmonitor == other.loadbalancer_healthmonitor and
                self.virtual_ip == other.virtual_ip)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_defaults (obj.populate_integer ("defaults"))
        obj.set_floating_ip (obj.populate_integer ("floating_ip"))
        obj.set_instance_ip (obj.populate_integer ("instance_ip"))
        obj.set_virtual_machine_interface (obj.populate_integer ("virtual_machine_interface"))
        obj.set_virtual_network (obj.populate_integer ("virtual_network"))
        obj.set_virtual_router (obj.populate_integer ("virtual_router"))
        obj.set_virtual_DNS (obj.populate_integer ("virtual_DNS"))
        obj.set_virtual_DNS_record (obj.populate_integer ("virtual_DNS_record"))
        obj.set_bgp_router (obj.populate_integer ("bgp_router"))
        obj.set_network_ipam (obj.populate_integer ("network_ipam"))
        obj.set_access_control_list (obj.populate_integer ("access_control_list"))
        obj.set_floating_ip_pool (obj.populate_integer ("floating_ip_pool"))
        obj.set_service_template (obj.populate_integer ("service_template"))
        obj.set_service_instance (obj.populate_integer ("service_instance"))
        obj.set_logical_router (obj.populate_integer ("logical_router"))
        obj.set_security_group (obj.populate_integer ("security_group"))
        obj.set_security_group_rule (obj.populate_integer ("security_group_rule"))
        obj.set_subnet (obj.populate_integer ("subnet"))
        obj.set_global_vrouter_config (obj.populate_integer ("global_vrouter_config"))
        obj.set_loadbalancer_pool (obj.populate_integer ("loadbalancer_pool"))
        obj.set_loadbalancer_member (obj.populate_integer ("loadbalancer_member"))
        obj.set_loadbalancer_healthmonitor (obj.populate_integer ("loadbalancer_healthmonitor"))
        obj.set_virtual_ip (obj.populate_integer ("virtual_ip"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='QuotaType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='QuotaType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='QuotaType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='QuotaType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.defaults is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdefaults>%s</%sdefaults>%s' % (namespace_, self.gds_format_integer(self.defaults, input_name='defaults'), namespace_, eol_))
        if self.floating_ip is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfloating-ip>%s</%sfloating-ip>%s' % (namespace_, self.gds_format_integer(self.floating_ip, input_name='floating-ip'), namespace_, eol_))
        if self.instance_ip is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinstance-ip>%s</%sinstance-ip>%s' % (namespace_, self.gds_format_integer(self.instance_ip, input_name='instance-ip'), namespace_, eol_))
        if self.virtual_machine_interface is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-machine-interface>%s</%svirtual-machine-interface>%s' % (namespace_, self.gds_format_integer(self.virtual_machine_interface, input_name='virtual-machine-interface'), namespace_, eol_))
        if self.virtual_network is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-network>%s</%svirtual-network>%s' % (namespace_, self.gds_format_integer(self.virtual_network, input_name='virtual-network'), namespace_, eol_))
        if self.virtual_router is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-router>%s</%svirtual-router>%s' % (namespace_, self.gds_format_integer(self.virtual_router, input_name='virtual-router'), namespace_, eol_))
        if self.virtual_DNS is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-DNS>%s</%svirtual-DNS>%s' % (namespace_, self.gds_format_integer(self.virtual_DNS, input_name='virtual-DNS'), namespace_, eol_))
        if self.virtual_DNS_record is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-DNS-record>%s</%svirtual-DNS-record>%s' % (namespace_, self.gds_format_integer(self.virtual_DNS_record, input_name='virtual-DNS-record'), namespace_, eol_))
        if self.bgp_router is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbgp-router>%s</%sbgp-router>%s' % (namespace_, self.gds_format_integer(self.bgp_router, input_name='bgp-router'), namespace_, eol_))
        if self.network_ipam is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snetwork-ipam>%s</%snetwork-ipam>%s' % (namespace_, self.gds_format_integer(self.network_ipam, input_name='network-ipam'), namespace_, eol_))
        if self.access_control_list is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saccess-control-list>%s</%saccess-control-list>%s' % (namespace_, self.gds_format_integer(self.access_control_list, input_name='access-control-list'), namespace_, eol_))
        if self.floating_ip_pool is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfloating-ip-pool>%s</%sfloating-ip-pool>%s' % (namespace_, self.gds_format_integer(self.floating_ip_pool, input_name='floating-ip-pool'), namespace_, eol_))
        if self.service_template is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-template>%s</%sservice-template>%s' % (namespace_, self.gds_format_integer(self.service_template, input_name='service-template'), namespace_, eol_))
        if self.service_instance is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-instance>%s</%sservice-instance>%s' % (namespace_, self.gds_format_integer(self.service_instance, input_name='service-instance'), namespace_, eol_))
        if self.logical_router is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slogical-router>%s</%slogical-router>%s' % (namespace_, self.gds_format_integer(self.logical_router, input_name='logical-router'), namespace_, eol_))
        if self.security_group is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssecurity-group>%s</%ssecurity-group>%s' % (namespace_, self.gds_format_integer(self.security_group, input_name='security-group'), namespace_, eol_))
        if self.security_group_rule is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssecurity-group-rule>%s</%ssecurity-group-rule>%s' % (namespace_, self.gds_format_integer(self.security_group_rule, input_name='security-group-rule'), namespace_, eol_))
        if self.subnet is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssubnet>%s</%ssubnet>%s' % (namespace_, self.gds_format_integer(self.subnet, input_name='subnet'), namespace_, eol_))
        if self.global_vrouter_config is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sglobal-vrouter-config>%s</%sglobal-vrouter-config>%s' % (namespace_, self.gds_format_integer(self.global_vrouter_config, input_name='global-vrouter-config'), namespace_, eol_))
        if self.loadbalancer_pool is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sloadbalancer-pool>%s</%sloadbalancer-pool>%s' % (namespace_, self.gds_format_integer(self.loadbalancer_pool, input_name='loadbalancer-pool'), namespace_, eol_))
        if self.loadbalancer_member is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sloadbalancer-member>%s</%sloadbalancer-member>%s' % (namespace_, self.gds_format_integer(self.loadbalancer_member, input_name='loadbalancer-member'), namespace_, eol_))
        if self.loadbalancer_healthmonitor is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sloadbalancer-healthmonitor>%s</%sloadbalancer-healthmonitor>%s' % (namespace_, self.gds_format_integer(self.loadbalancer_healthmonitor, input_name='loadbalancer-healthmonitor'), namespace_, eol_))
        if self.virtual_ip is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-ip>%s</%svirtual-ip>%s' % (namespace_, self.gds_format_integer(self.virtual_ip, input_name='virtual-ip'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.defaults is not None or
            self.floating_ip is not None or
            self.instance_ip is not None or
            self.virtual_machine_interface is not None or
            self.virtual_network is not None or
            self.virtual_router is not None or
            self.virtual_DNS is not None or
            self.virtual_DNS_record is not None or
            self.bgp_router is not None or
            self.network_ipam is not None or
            self.access_control_list is not None or
            self.floating_ip_pool is not None or
            self.service_template is not None or
            self.service_instance is not None or
            self.logical_router is not None or
            self.security_group is not None or
            self.security_group_rule is not None or
            self.subnet is not None or
            self.global_vrouter_config is not None or
            self.loadbalancer_pool is not None or
            self.loadbalancer_member is not None or
            self.loadbalancer_healthmonitor is not None or
            self.virtual_ip is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='QuotaType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.defaults is not None:
            showIndent(outfile, level)
            outfile.write('defaults=%d,\n' % self.defaults)
        if self.floating_ip is not None:
            showIndent(outfile, level)
            outfile.write('floating_ip=%d,\n' % self.floating_ip)
        if self.instance_ip is not None:
            showIndent(outfile, level)
            outfile.write('instance_ip=%d,\n' % self.instance_ip)
        if self.virtual_machine_interface is not None:
            showIndent(outfile, level)
            outfile.write('virtual_machine_interface=%d,\n' % self.virtual_machine_interface)
        if self.virtual_network is not None:
            showIndent(outfile, level)
            outfile.write('virtual_network=%d,\n' % self.virtual_network)
        if self.virtual_router is not None:
            showIndent(outfile, level)
            outfile.write('virtual_router=%d,\n' % self.virtual_router)
        if self.virtual_DNS is not None:
            showIndent(outfile, level)
            outfile.write('virtual_DNS=%d,\n' % self.virtual_DNS)
        if self.virtual_DNS_record is not None:
            showIndent(outfile, level)
            outfile.write('virtual_DNS_record=%d,\n' % self.virtual_DNS_record)
        if self.bgp_router is not None:
            showIndent(outfile, level)
            outfile.write('bgp_router=%d,\n' % self.bgp_router)
        if self.network_ipam is not None:
            showIndent(outfile, level)
            outfile.write('network_ipam=%d,\n' % self.network_ipam)
        if self.access_control_list is not None:
            showIndent(outfile, level)
            outfile.write('access_control_list=%d,\n' % self.access_control_list)
        if self.floating_ip_pool is not None:
            showIndent(outfile, level)
            outfile.write('floating_ip_pool=%d,\n' % self.floating_ip_pool)
        if self.service_template is not None:
            showIndent(outfile, level)
            outfile.write('service_template=%d,\n' % self.service_template)
        if self.service_instance is not None:
            showIndent(outfile, level)
            outfile.write('service_instance=%d,\n' % self.service_instance)
        if self.logical_router is not None:
            showIndent(outfile, level)
            outfile.write('logical_router=%d,\n' % self.logical_router)
        if self.security_group is not None:
            showIndent(outfile, level)
            outfile.write('security_group=%d,\n' % self.security_group)
        if self.security_group_rule is not None:
            showIndent(outfile, level)
            outfile.write('security_group_rule=%d,\n' % self.security_group_rule)
        if self.subnet is not None:
            showIndent(outfile, level)
            outfile.write('subnet=%d,\n' % self.subnet)
        if self.global_vrouter_config is not None:
            showIndent(outfile, level)
            outfile.write('global_vrouter_config=%d,\n' % self.global_vrouter_config)
        if self.loadbalancer_pool is not None:
            showIndent(outfile, level)
            outfile.write('loadbalancer_pool=%d,\n' % self.loadbalancer_pool)
        if self.loadbalancer_member is not None:
            showIndent(outfile, level)
            outfile.write('loadbalancer_member=%d,\n' % self.loadbalancer_member)
        if self.loadbalancer_healthmonitor is not None:
            showIndent(outfile, level)
            outfile.write('loadbalancer_healthmonitor=%d,\n' % self.loadbalancer_healthmonitor)
        if self.virtual_ip is not None:
            showIndent(outfile, level)
            outfile.write('virtual_ip=%d,\n' % self.virtual_ip)
    def exportDict(self, name_='QuotaType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'defaults':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'defaults')
            self.defaults = ival_
        elif nodeName_ == 'floating-ip':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'floating_ip')
            self.floating_ip = ival_
        elif nodeName_ == 'instance-ip':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'instance_ip')
            self.instance_ip = ival_
        elif nodeName_ == 'virtual-machine-interface':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'virtual_machine_interface')
            self.virtual_machine_interface = ival_
        elif nodeName_ == 'virtual-network':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'virtual_network')
            self.virtual_network = ival_
        elif nodeName_ == 'virtual-router':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'virtual_router')
            self.virtual_router = ival_
        elif nodeName_ == 'virtual-DNS':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'virtual_DNS')
            self.virtual_DNS = ival_
        elif nodeName_ == 'virtual-DNS-record':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'virtual_DNS_record')
            self.virtual_DNS_record = ival_
        elif nodeName_ == 'bgp-router':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'bgp_router')
            self.bgp_router = ival_
        elif nodeName_ == 'network-ipam':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'network_ipam')
            self.network_ipam = ival_
        elif nodeName_ == 'access-control-list':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'access_control_list')
            self.access_control_list = ival_
        elif nodeName_ == 'floating-ip-pool':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'floating_ip_pool')
            self.floating_ip_pool = ival_
        elif nodeName_ == 'service-template':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'service_template')
            self.service_template = ival_
        elif nodeName_ == 'service-instance':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'service_instance')
            self.service_instance = ival_
        elif nodeName_ == 'logical-router':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'logical_router')
            self.logical_router = ival_
        elif nodeName_ == 'security-group':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'security_group')
            self.security_group = ival_
        elif nodeName_ == 'security-group-rule':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'security_group_rule')
            self.security_group_rule = ival_
        elif nodeName_ == 'subnet':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'subnet')
            self.subnet = ival_
        elif nodeName_ == 'global-vrouter-config':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'global_vrouter_config')
            self.global_vrouter_config = ival_
        elif nodeName_ == 'loadbalancer-pool':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'loadbalancer_pool')
            self.loadbalancer_pool = ival_
        elif nodeName_ == 'loadbalancer-member':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'loadbalancer_member')
            self.loadbalancer_member = ival_
        elif nodeName_ == 'loadbalancer-healthmonitor':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'loadbalancer_healthmonitor')
            self.loadbalancer_healthmonitor = ival_
        elif nodeName_ == 'virtual-ip':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'virtual_ip')
            self.virtual_ip = ival_
# end class QuotaType


class config_root_global_system_config(GeneratedsSuper):
    """
    config_root_global_system_config class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if config_root_global_system_config.subclass:
            return config_root_global_system_config.subclass(*args_, **kwargs_)
        else:
            return config_root_global_system_config(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='config-root-global-system-config', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='config-root-global-system-config')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='config-root-global-system-config'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='config-root-global-system-config', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='config-root-global-system-config'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='config-root-global-system-config'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class config_root_global_system_config


class global_system_config_bgp_router(GeneratedsSuper):
    """
    global_system_config_bgp_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_bgp_router.subclass:
            return global_system_config_bgp_router.subclass(*args_, **kwargs_)
        else:
            return global_system_config_bgp_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-bgp-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-bgp-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-bgp-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-bgp-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-bgp-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-bgp-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_bgp_router


class global_system_config_global_vrouter_config(GeneratedsSuper):
    """
    global_system_config_global_vrouter_config class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_global_vrouter_config.subclass:
            return global_system_config_global_vrouter_config.subclass(*args_, **kwargs_)
        else:
            return global_system_config_global_vrouter_config(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-global-vrouter-config', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-global-vrouter-config')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-global-vrouter-config'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-global-vrouter-config', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-global-vrouter-config'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-global-vrouter-config'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_global_vrouter_config


class config_root_domain(GeneratedsSuper):
    """
    config_root_domain class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if config_root_domain.subclass:
            return config_root_domain.subclass(*args_, **kwargs_)
        else:
            return config_root_domain(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='config-root-domain', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='config-root-domain')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='config-root-domain'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='config-root-domain', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='config-root-domain'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='config-root-domain'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class config_root_domain


class domain_project(GeneratedsSuper):
    """
    domain_project class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if domain_project.subclass:
            return domain_project.subclass(*args_, **kwargs_)
        else:
            return domain_project(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='domain-project', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='domain-project')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='domain-project'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='domain-project', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='domain-project'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='domain-project'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class domain_project


class domain_namespace(GeneratedsSuper):
    """
    domain_namespace class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if domain_namespace.subclass:
            return domain_namespace.subclass(*args_, **kwargs_)
        else:
            return domain_namespace(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='domain-namespace', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='domain-namespace')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='domain-namespace'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='domain-namespace', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='domain-namespace'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='domain-namespace'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class domain_namespace


class project_security_group(GeneratedsSuper):
    """
    project_security_group class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_security_group.subclass:
            return project_security_group.subclass(*args_, **kwargs_)
        else:
            return project_security_group(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-security-group', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-security-group')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-security-group'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-security-group', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-security-group'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-security-group'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_security_group


class project_virtual_network(GeneratedsSuper):
    """
    project_virtual_network class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_virtual_network.subclass:
            return project_virtual_network.subclass(*args_, **kwargs_)
        else:
            return project_virtual_network(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-virtual-network', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-virtual-network')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-virtual-network'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-virtual-network', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-virtual-network'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-virtual-network'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_virtual_network


class project_qos_queue(GeneratedsSuper):
    """
    project_qos_queue class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_qos_queue.subclass:
            return project_qos_queue.subclass(*args_, **kwargs_)
        else:
            return project_qos_queue(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-qos-queue', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-qos-queue')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-qos-queue'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-qos-queue', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-qos-queue'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-qos-queue'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_qos_queue


class project_qos_forwarding_class(GeneratedsSuper):
    """
    project_qos_forwarding_class class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_qos_forwarding_class.subclass:
            return project_qos_forwarding_class.subclass(*args_, **kwargs_)
        else:
            return project_qos_forwarding_class(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-qos-forwarding-class', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-qos-forwarding-class')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-qos-forwarding-class'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-qos-forwarding-class', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-qos-forwarding-class'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-qos-forwarding-class'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_qos_forwarding_class


class qos_forwarding_class_qos_queue(GeneratedsSuper):
    """
    qos_forwarding_class_qos_queue class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if qos_forwarding_class_qos_queue.subclass:
            return qos_forwarding_class_qos_queue.subclass(*args_, **kwargs_)
        else:
            return qos_forwarding_class_qos_queue(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='qos-forwarding-class-qos-queue', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='qos-forwarding-class-qos-queue')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='qos-forwarding-class-qos-queue'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='qos-forwarding-class-qos-queue', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='qos-forwarding-class-qos-queue'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='qos-forwarding-class-qos-queue'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class qos_forwarding_class_qos_queue


class virtual_network_qos_forwarding_class(GeneratedsSuper):
    """
    virtual_network_qos_forwarding_class class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_network_qos_forwarding_class.subclass:
            return virtual_network_qos_forwarding_class.subclass(*args_, **kwargs_)
        else:
            return virtual_network_qos_forwarding_class(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-network-qos-forwarding-class', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-network-qos-forwarding-class')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-network-qos-forwarding-class'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-network-qos-forwarding-class', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-network-qos-forwarding-class'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-network-qos-forwarding-class'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_network_qos_forwarding_class


class virtual_machine_interface_qos_forwarding_class(GeneratedsSuper):
    """
    virtual_machine_interface_qos_forwarding_class class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_interface_qos_forwarding_class.subclass:
            return virtual_machine_interface_qos_forwarding_class.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_interface_qos_forwarding_class(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-interface-qos-forwarding-class', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-interface-qos-forwarding-class')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-interface-qos-forwarding-class'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-interface-qos-forwarding-class', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-interface-qos-forwarding-class'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-interface-qos-forwarding-class'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_interface_qos_forwarding_class


class VirtualNetworkType(GeneratedsSuper):
    """
    VirtualNetworkType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, allow_transit=None, network_id=None, vxlan_network_identifier=None, forwarding_mode=None, rpf=None, **kwargs):
        self.allow_transit = allow_transit
        self.network_id = network_id
        self.vxlan_network_identifier = vxlan_network_identifier
        self.forwarding_mode = forwarding_mode
        self.rpf = rpf
    def factory(*args_, **kwargs_):
        if VirtualNetworkType.subclass:
            return VirtualNetworkType.subclass(*args_, **kwargs_)
        else:
            return VirtualNetworkType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_allow_transit(self): return self.allow_transit
    def set_allow_transit(self, allow_transit): self.allow_transit = allow_transit
    def get_network_id(self): return self.network_id
    def set_network_id(self, network_id): self.network_id = network_id
    def get_vxlan_network_identifier(self): return self.vxlan_network_identifier
    def set_vxlan_network_identifier(self, vxlan_network_identifier): self.vxlan_network_identifier = vxlan_network_identifier
    def validate_VxlanNetworkIdentifierType(self, value):
        # Validate type VxlanNetworkIdentifierType, a restriction on xsd:integer.
        error = False
        if isinstance(value, list):
            v_int = map(int, value)
            v1, v2 = min(v_int), max(v_int)
        else:
            v1, v2 = int(value), int(value)
        error = (1 > v1)
        error |= (v2 > 1048575)
        if error:
            raise ValueError("VxlanNetworkIdentifierType must be in the range 1-1048575")
    def get_forwarding_mode(self): return self.forwarding_mode
    def set_forwarding_mode(self, forwarding_mode): self.forwarding_mode = forwarding_mode
    def validate_ForwardingModeType(self, value):
        # Validate type ForwardingModeType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'l2_l3', u'l2'])
        else:
            error = value not in [u'l2_l3', u'l2']
        if error:
            raise ValueError("ForwardingModeType must be one of [u'l2_l3', u'l2']")
    def get_rpf(self): return self.rpf
    def set_rpf(self, rpf): self.rpf = rpf
    def validate_RpfModeType(self, value):
        # Validate type RpfModeType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'enable', u'disable'])
        else:
            error = value not in [u'enable', u'disable']
        if error:
            raise ValueError("RpfModeType must be one of [u'enable', u'disable']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.allow_transit == other.allow_transit and
                self.network_id == other.network_id and
                self.vxlan_network_identifier == other.vxlan_network_identifier and
                self.forwarding_mode == other.forwarding_mode and
                self.rpf == other.rpf)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_allow_transit (obj.populate_boolean ("allow_transit"))
        obj.set_network_id (obj.populate_integer ("network_id"))
        obj.set_vxlan_network_identifier (obj.populate_integer ("vxlan_network_identifier"))
        obj.set_forwarding_mode (obj.populate_string ("forwarding_mode"))
        obj.set_rpf (obj.populate_string ("rpf"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VirtualNetworkType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VirtualNetworkType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VirtualNetworkType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VirtualNetworkType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.allow_transit is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sallow-transit>%s</%sallow-transit>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.allow_transit)), input_name='allow-transit'), namespace_, eol_))
        if self.network_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snetwork-id>%s</%snetwork-id>%s' % (namespace_, self.gds_format_integer(self.network_id, input_name='network-id'), namespace_, eol_))
        if self.vxlan_network_identifier is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svxlan-network-identifier>%s</%svxlan-network-identifier>%s' % (namespace_, self.gds_format_integer(self.vxlan_network_identifier, input_name='vxlan-network-identifier'), namespace_, eol_))
        if self.forwarding_mode is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sforwarding-mode>%s</%sforwarding-mode>%s' % (namespace_, self.gds_format_string(quote_xml(self.forwarding_mode).encode(ExternalEncoding), input_name='forwarding-mode'), namespace_, eol_))
        if self.rpf is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srpf>%s</%srpf>%s' % (namespace_, self.gds_format_string(quote_xml(self.rpf).encode(ExternalEncoding), input_name='rpf'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.allow_transit is not None or
            self.network_id is not None or
            self.vxlan_network_identifier is not None or
            self.forwarding_mode is not None or
            self.rpf is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VirtualNetworkType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.allow_transit is not None:
            showIndent(outfile, level)
            outfile.write('allow_transit=%s,\n' % self.allow_transit)
        if self.network_id is not None:
            showIndent(outfile, level)
            outfile.write('network_id=%d,\n' % self.network_id)
        if self.vxlan_network_identifier is not None:
            showIndent(outfile, level)
            outfile.write('vxlan_network_identifier=%d,\n' % self.vxlan_network_identifier)
        if self.forwarding_mode is not None:
            showIndent(outfile, level)
            outfile.write('forwarding_mode=%s,\n' % quote_python(self.forwarding_mode).encode(ExternalEncoding))
        if self.rpf is not None:
            showIndent(outfile, level)
            outfile.write('rpf=%s,\n' % quote_python(self.rpf).encode(ExternalEncoding))
    def exportDict(self, name_='VirtualNetworkType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'allow-transit':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'allow_transit')
            self.allow_transit = ival_
        elif nodeName_ == 'network-id':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'network_id')
            self.network_id = ival_
        elif nodeName_ == 'vxlan-network-identifier':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'vxlan_network_identifier')
            self.vxlan_network_identifier = ival_
            self.validate_VxlanNetworkIdentifierType(self.vxlan_network_identifier)    # validate type VxlanNetworkIdentifierType
        elif nodeName_ == 'forwarding-mode':
            forwarding_mode_ = child_.text
            forwarding_mode_ = self.gds_validate_string(forwarding_mode_, node, 'forwarding_mode')
            self.forwarding_mode = forwarding_mode_
            self.validate_ForwardingModeType(self.forwarding_mode)    # validate type ForwardingModeType
        elif nodeName_ == 'rpf':
            rpf_ = child_.text
            rpf_ = self.gds_validate_string(rpf_, node, 'rpf')
            self.rpf = rpf_
            self.validate_RpfModeType(self.rpf)    # validate type RpfModeType
# end class VirtualNetworkType


class RouteTargetList(GeneratedsSuper):
    """
    RouteTargetList class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, route_target=None, **kwargs):
        if (route_target is None) or (route_target == []):
            self.route_target = []
        else:
            self.route_target = route_target
    def factory(*args_, **kwargs_):
        if RouteTargetList.subclass:
            return RouteTargetList.subclass(*args_, **kwargs_)
        else:
            return RouteTargetList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_route_target(self): return self.route_target
    def set_route_target(self, route_target): self.route_target = route_target
    def add_route_target(self, value): self.route_target.append(value)
    def insert_route_target(self, index, value): self.route_target[index] = value
    def delete_route_target(self, value): self.route_target.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.route_target == other.route_target)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_route_target ([obj.populate_string ("route_target")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='RouteTargetList', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RouteTargetList')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RouteTargetList'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='RouteTargetList', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for route_target_ in self.route_target:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sroute-target>%s</%sroute-target>%s' % (namespace_, self.gds_format_string(quote_xml(route_target_).encode(ExternalEncoding), input_name='route-target'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.route_target
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='RouteTargetList'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('route_target=[\n')
        level += 1
        for route_target_ in self.route_target:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(route_target_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='RouteTargetList'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'route-target':
            route_target_ = child_.text
            route_target_ = self.gds_validate_string(route_target_, node, 'route_target')
            self.route_target.append(route_target_)
# end class RouteTargetList


class project_network_ipam(GeneratedsSuper):
    """
    project_network_ipam class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_network_ipam.subclass:
            return project_network_ipam.subclass(*args_, **kwargs_)
        else:
            return project_network_ipam(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-network-ipam', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-network-ipam')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-network-ipam'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-network-ipam', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-network-ipam'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-network-ipam'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_network_ipam


class project_network_policy(GeneratedsSuper):
    """
    project_network_policy class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_network_policy.subclass:
            return project_network_policy.subclass(*args_, **kwargs_)
        else:
            return project_network_policy(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-network-policy', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-network-policy')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-network-policy'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-network-policy', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-network-policy'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-network-policy'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_network_policy


class virtual_network_access_control_list(GeneratedsSuper):
    """
    virtual_network_access_control_list class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_network_access_control_list.subclass:
            return virtual_network_access_control_list.subclass(*args_, **kwargs_)
        else:
            return virtual_network_access_control_list(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-network-access-control-list', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-network-access-control-list')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-network-access-control-list'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-network-access-control-list', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-network-access-control-list'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-network-access-control-list'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_network_access_control_list


class security_group_access_control_list(GeneratedsSuper):
    """
    security_group_access_control_list class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if security_group_access_control_list.subclass:
            return security_group_access_control_list.subclass(*args_, **kwargs_)
        else:
            return security_group_access_control_list(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='security-group-access-control-list', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='security-group-access-control-list')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='security-group-access-control-list'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='security-group-access-control-list', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='security-group-access-control-list'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='security-group-access-control-list'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class security_group_access_control_list


class virtual_machine_interface_security_group(GeneratedsSuper):
    """
    virtual_machine_interface_security_group class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_interface_security_group.subclass:
            return virtual_machine_interface_security_group.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_interface_security_group(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-interface-security-group', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-interface-security-group')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-interface-security-group'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-interface-security-group', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-interface-security-group'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-interface-security-group'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_interface_security_group


class VrfAssignRuleType(GeneratedsSuper):
    """
    VrfAssignRuleType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, match_condition=None, vlan_tag=None, routing_instance=None, ignore_acl=None, **kwargs):
        if isinstance(match_condition, dict):
            obj = MatchConditionType(**match_condition)
            self.match_condition = obj
        else:
            self.match_condition = match_condition
        self.vlan_tag = vlan_tag
        self.routing_instance = routing_instance
        self.ignore_acl = ignore_acl
    def factory(*args_, **kwargs_):
        if VrfAssignRuleType.subclass:
            return VrfAssignRuleType.subclass(*args_, **kwargs_)
        else:
            return VrfAssignRuleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_match_condition(self): return self.match_condition
    def set_match_condition(self, match_condition): self.match_condition = match_condition
    def get_vlan_tag(self): return self.vlan_tag
    def set_vlan_tag(self, vlan_tag): self.vlan_tag = vlan_tag
    def get_routing_instance(self): return self.routing_instance
    def set_routing_instance(self, routing_instance): self.routing_instance = routing_instance
    def get_ignore_acl(self): return self.ignore_acl
    def set_ignore_acl(self, ignore_acl): self.ignore_acl = ignore_acl
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.match_condition == other.match_condition and
                self.vlan_tag == other.vlan_tag and
                self.routing_instance == other.routing_instance and
                self.ignore_acl == other.ignore_acl)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_match_condition (MatchConditionType.populate ())
        obj.set_vlan_tag (obj.populate_integer ("vlan_tag"))
        obj.set_routing_instance (obj.populate_string ("routing_instance"))
        obj.set_ignore_acl (obj.populate_boolean ("ignore_acl"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VrfAssignRuleType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VrfAssignRuleType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VrfAssignRuleType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VrfAssignRuleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.match_condition is not None:
            self.match_condition.export(outfile, level, namespace_, name_='match-condition', pretty_print=pretty_print)
        if self.vlan_tag is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svlan-tag>%s</%svlan-tag>%s' % (namespace_, self.gds_format_integer(self.vlan_tag, input_name='vlan-tag'), namespace_, eol_))
        if self.routing_instance is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srouting-instance>%s</%srouting-instance>%s' % (namespace_, self.gds_format_string(quote_xml(self.routing_instance).encode(ExternalEncoding), input_name='routing-instance'), namespace_, eol_))
        if self.ignore_acl is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%signore-acl>%s</%signore-acl>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.ignore_acl)), input_name='ignore-acl'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.match_condition is not None or
            self.vlan_tag is not None or
            self.routing_instance is not None or
            self.ignore_acl is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VrfAssignRuleType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.match_condition is not None:
            showIndent(outfile, level)
            outfile.write('match_condition=model_.MatchConditionType(\n')
            self.match_condition.exportLiteral(outfile, level, name_='match_condition')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.vlan_tag is not None:
            showIndent(outfile, level)
            outfile.write('vlan_tag=%d,\n' % self.vlan_tag)
        if self.routing_instance is not None:
            showIndent(outfile, level)
            outfile.write('routing_instance=%s,\n' % quote_python(self.routing_instance).encode(ExternalEncoding))
        if self.ignore_acl is not None:
            showIndent(outfile, level)
            outfile.write('ignore_acl=%s,\n' % self.ignore_acl)
    def exportDict(self, name_='VrfAssignRuleType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'match-condition':
            obj_ = MatchConditionType.factory()
            obj_.build(child_)
            self.set_match_condition(obj_)
        elif nodeName_ == 'vlan-tag':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'vlan_tag')
            self.vlan_tag = ival_
        elif nodeName_ == 'routing-instance':
            routing_instance_ = child_.text
            routing_instance_ = self.gds_validate_string(routing_instance_, node, 'routing_instance')
            self.routing_instance = routing_instance_
        elif nodeName_ == 'ignore-acl':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'ignore_acl')
            self.ignore_acl = ival_
# end class VrfAssignRuleType


class VrfAssignTableType(GeneratedsSuper):
    """
    VrfAssignTableType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, vrf_assign_rule=None, **kwargs):
        if (vrf_assign_rule is None) or (vrf_assign_rule == []):
            self.vrf_assign_rule = []
        else:
            if isinstance(vrf_assign_rule[0], dict):
                objs = [VrfAssignRuleType(**elem) for elem in vrf_assign_rule]
                self.vrf_assign_rule = objs
            else:
                self.vrf_assign_rule = vrf_assign_rule
    def factory(*args_, **kwargs_):
        if VrfAssignTableType.subclass:
            return VrfAssignTableType.subclass(*args_, **kwargs_)
        else:
            return VrfAssignTableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_vrf_assign_rule(self): return self.vrf_assign_rule
    def set_vrf_assign_rule(self, vrf_assign_rule): self.vrf_assign_rule = vrf_assign_rule
    def add_vrf_assign_rule(self, value): self.vrf_assign_rule.append(value)
    def insert_vrf_assign_rule(self, index, value): self.vrf_assign_rule[index] = value
    def delete_vrf_assign_rule(self, value): self.vrf_assign_rule.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.vrf_assign_rule == other.vrf_assign_rule)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_vrf_assign_rule ([VrfAssignRuleType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VrfAssignTableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VrfAssignTableType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VrfAssignTableType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VrfAssignTableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for vrf_assign_rule_ in self.vrf_assign_rule:
            if isinstance(vrf_assign_rule_, dict):
                vrf_assign_rule_ = VrfAssignRuleType(**vrf_assign_rule_)
            vrf_assign_rule_.export(outfile, level, namespace_, name_='vrf-assign-rule', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.vrf_assign_rule
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VrfAssignTableType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('vrf_assign_rule=[\n')
        level += 1
        for vrf_assign_rule_ in self.vrf_assign_rule:
            showIndent(outfile, level)
            outfile.write('model_.VrfAssignRuleType(\n')
            vrf_assign_rule_.exportLiteral(outfile, level, name_='VrfAssignRuleType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='VrfAssignTableType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'vrf-assign-rule':
            obj_ = VrfAssignRuleType.factory()
            obj_.build(child_)
            self.vrf_assign_rule.append(obj_)
# end class VrfAssignTableType


class InterfaceMirrorType(GeneratedsSuper):
    """
    InterfaceMirrorType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, traffic_direction=None, mirror_to=None, **kwargs):
        self.traffic_direction = traffic_direction
        if isinstance(mirror_to, dict):
            obj = MirrorActionType(**mirror_to)
            self.mirror_to = obj
        else:
            self.mirror_to = mirror_to
    def factory(*args_, **kwargs_):
        if InterfaceMirrorType.subclass:
            return InterfaceMirrorType.subclass(*args_, **kwargs_)
        else:
            return InterfaceMirrorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_traffic_direction(self): return self.traffic_direction
    def set_traffic_direction(self, traffic_direction): self.traffic_direction = traffic_direction
    def validate_TrafficDirectionType(self, value):
        # Validate type TrafficDirectionType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'ingress', u'egress', u'both'])
        else:
            error = value not in [u'ingress', u'egress', u'both']
        if error:
            raise ValueError("TrafficDirectionType must be one of [u'ingress', u'egress', u'both']")
    def get_mirror_to(self): return self.mirror_to
    def set_mirror_to(self, mirror_to): self.mirror_to = mirror_to
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.traffic_direction == other.traffic_direction and
                self.mirror_to == other.mirror_to)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_traffic_direction (obj.populate_string ("traffic_direction"))
        obj.set_mirror_to (MirrorActionType.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='InterfaceMirrorType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='InterfaceMirrorType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='InterfaceMirrorType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='InterfaceMirrorType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.traffic_direction is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%straffic-direction>%s</%straffic-direction>%s' % (namespace_, self.gds_format_string(quote_xml(self.traffic_direction).encode(ExternalEncoding), input_name='traffic-direction'), namespace_, eol_))
        if self.mirror_to is not None:
            self.mirror_to.export(outfile, level, namespace_, name_='mirror-to', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.traffic_direction is not None or
            self.mirror_to is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='InterfaceMirrorType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.traffic_direction is not None:
            showIndent(outfile, level)
            outfile.write('traffic_direction=%s,\n' % quote_python(self.traffic_direction).encode(ExternalEncoding))
        if self.mirror_to is not None:
            showIndent(outfile, level)
            outfile.write('mirror_to=model_.MirrorActionType(\n')
            self.mirror_to.exportLiteral(outfile, level, name_='mirror_to')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='InterfaceMirrorType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'traffic-direction':
            traffic_direction_ = child_.text
            traffic_direction_ = self.gds_validate_string(traffic_direction_, node, 'traffic_direction')
            self.traffic_direction = traffic_direction_
            self.validate_TrafficDirectionType(self.traffic_direction)    # validate type TrafficDirectionType
        elif nodeName_ == 'mirror-to':
            obj_ = MirrorActionType.factory()
            obj_.build(child_)
            self.set_mirror_to(obj_)
# end class InterfaceMirrorType


class VirtualMachineInterfacePropertiesType(GeneratedsSuper):
    """
    VirtualMachineInterfacePropertiesType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, service_interface_type=None, interface_mirror=None, local_preference=None, sub_interface_vlan_tag=None, **kwargs):
        self.service_interface_type = service_interface_type
        if isinstance(interface_mirror, dict):
            obj = InterfaceMirrorType(**interface_mirror)
            self.interface_mirror = obj
        else:
            self.interface_mirror = interface_mirror
        self.local_preference = local_preference
        self.sub_interface_vlan_tag = sub_interface_vlan_tag
    def factory(*args_, **kwargs_):
        if VirtualMachineInterfacePropertiesType.subclass:
            return VirtualMachineInterfacePropertiesType.subclass(*args_, **kwargs_)
        else:
            return VirtualMachineInterfacePropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_service_interface_type(self): return self.service_interface_type
    def set_service_interface_type(self, service_interface_type): self.service_interface_type = service_interface_type
    def validate_ServiceInterfaceType(self, value):
        # Validate type ServiceInterfaceType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'management', u'left', u'right', u'other'])
        else:
            error = value not in [u'management', u'left', u'right', u'other']
        if error:
            raise ValueError("ServiceInterfaceType must be one of [u'management', u'left', u'right', u'other']")
    def get_interface_mirror(self): return self.interface_mirror
    def set_interface_mirror(self, interface_mirror): self.interface_mirror = interface_mirror
    def get_local_preference(self): return self.local_preference
    def set_local_preference(self, local_preference): self.local_preference = local_preference
    def get_sub_interface_vlan_tag(self): return self.sub_interface_vlan_tag
    def set_sub_interface_vlan_tag(self, sub_interface_vlan_tag): self.sub_interface_vlan_tag = sub_interface_vlan_tag
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.service_interface_type == other.service_interface_type and
                self.interface_mirror == other.interface_mirror and
                self.local_preference == other.local_preference and
                self.sub_interface_vlan_tag == other.sub_interface_vlan_tag)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_service_interface_type (obj.populate_string ("service_interface_type"))
        obj.set_interface_mirror (InterfaceMirrorType.populate ())
        obj.set_local_preference (obj.populate_integer ("local_preference"))
        obj.set_sub_interface_vlan_tag (obj.populate_integer ("sub_interface_vlan_tag"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VirtualMachineInterfacePropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VirtualMachineInterfacePropertiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VirtualMachineInterfacePropertiesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VirtualMachineInterfacePropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_interface_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-interface-type>%s</%sservice-interface-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_interface_type).encode(ExternalEncoding), input_name='service-interface-type'), namespace_, eol_))
        if self.interface_mirror is not None:
            self.interface_mirror.export(outfile, level, namespace_, name_='interface-mirror', pretty_print=pretty_print)
        if self.local_preference is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocal-preference>%s</%slocal-preference>%s' % (namespace_, self.gds_format_integer(self.local_preference, input_name='local-preference'), namespace_, eol_))
        if self.sub_interface_vlan_tag is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssub-interface-vlan-tag>%s</%ssub-interface-vlan-tag>%s' % (namespace_, self.gds_format_integer(self.sub_interface_vlan_tag, input_name='sub-interface-vlan-tag'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.service_interface_type is not None or
            self.interface_mirror is not None or
            self.local_preference is not None or
            self.sub_interface_vlan_tag is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VirtualMachineInterfacePropertiesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.service_interface_type is not None:
            showIndent(outfile, level)
            outfile.write('service_interface_type=%s,\n' % quote_python(self.service_interface_type).encode(ExternalEncoding))
        if self.interface_mirror is not None:
            showIndent(outfile, level)
            outfile.write('interface_mirror=model_.InterfaceMirrorType(\n')
            self.interface_mirror.exportLiteral(outfile, level, name_='interface_mirror')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.local_preference is not None:
            showIndent(outfile, level)
            outfile.write('local_preference=%d,\n' % self.local_preference)
        if self.sub_interface_vlan_tag is not None:
            showIndent(outfile, level)
            outfile.write('sub_interface_vlan_tag=%d,\n' % self.sub_interface_vlan_tag)
    def exportDict(self, name_='VirtualMachineInterfacePropertiesType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'service-interface-type':
            service_interface_type_ = child_.text
            service_interface_type_ = self.gds_validate_string(service_interface_type_, node, 'service_interface_type')
            self.service_interface_type = service_interface_type_
            self.validate_ServiceInterfaceType(self.service_interface_type)    # validate type ServiceInterfaceType
        elif nodeName_ == 'interface-mirror':
            obj_ = InterfaceMirrorType.factory()
            obj_.build(child_)
            self.set_interface_mirror(obj_)
        elif nodeName_ == 'local-preference':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'local_preference')
            self.local_preference = ival_
        elif nodeName_ == 'sub-interface-vlan-tag':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'sub_interface_vlan_tag')
            self.sub_interface_vlan_tag = ival_
# end class VirtualMachineInterfacePropertiesType


class ServiceTemplateInterfaceType(GeneratedsSuper):
    """
    ServiceTemplateInterfaceType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, service_interface_type=None, shared_ip=False, static_route_enable=False, **kwargs):
        self.service_interface_type = service_interface_type
        self.shared_ip = shared_ip
        self.static_route_enable = static_route_enable
    def factory(*args_, **kwargs_):
        if ServiceTemplateInterfaceType.subclass:
            return ServiceTemplateInterfaceType.subclass(*args_, **kwargs_)
        else:
            return ServiceTemplateInterfaceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_service_interface_type(self): return self.service_interface_type
    def set_service_interface_type(self, service_interface_type): self.service_interface_type = service_interface_type
    def validate_ServiceInterfaceType(self, value):
        # Validate type ServiceInterfaceType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'management', u'left', u'right', u'other'])
        else:
            error = value not in [u'management', u'left', u'right', u'other']
        if error:
            raise ValueError("ServiceInterfaceType must be one of [u'management', u'left', u'right', u'other']")
    def get_shared_ip(self): return self.shared_ip
    def set_shared_ip(self, shared_ip): self.shared_ip = shared_ip
    def get_static_route_enable(self): return self.static_route_enable
    def set_static_route_enable(self, static_route_enable): self.static_route_enable = static_route_enable
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.service_interface_type == other.service_interface_type and
                self.shared_ip == other.shared_ip and
                self.static_route_enable == other.static_route_enable)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_service_interface_type (obj.populate_string ("service_interface_type"))
        obj.set_shared_ip (obj.populate_boolean ("shared_ip"))
        obj.set_static_route_enable (obj.populate_boolean ("static_route_enable"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ServiceTemplateInterfaceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ServiceTemplateInterfaceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ServiceTemplateInterfaceType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ServiceTemplateInterfaceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_interface_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-interface-type>%s</%sservice-interface-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_interface_type).encode(ExternalEncoding), input_name='service-interface-type'), namespace_, eol_))
        if self.shared_ip is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sshared-ip>%s</%sshared-ip>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.shared_ip)), input_name='shared-ip'), namespace_, eol_))
        if self.static_route_enable is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatic-route-enable>%s</%sstatic-route-enable>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.static_route_enable)), input_name='static-route-enable'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.service_interface_type is not None or
            self.shared_ip is not None or
            self.static_route_enable is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ServiceTemplateInterfaceType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.service_interface_type is not None:
            showIndent(outfile, level)
            outfile.write('service_interface_type=%s,\n' % quote_python(self.service_interface_type).encode(ExternalEncoding))
        if self.shared_ip is not None:
            showIndent(outfile, level)
            outfile.write('shared_ip=%s,\n' % self.shared_ip)
        if self.static_route_enable is not None:
            showIndent(outfile, level)
            outfile.write('static_route_enable=%s,\n' % self.static_route_enable)
    def exportDict(self, name_='ServiceTemplateInterfaceType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'service-interface-type':
            service_interface_type_ = child_.text
            service_interface_type_ = self.gds_validate_string(service_interface_type_, node, 'service_interface_type')
            self.service_interface_type = service_interface_type_
            self.validate_ServiceInterfaceType(self.service_interface_type)    # validate type ServiceInterfaceType
        elif nodeName_ == 'shared-ip':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'shared_ip')
            self.shared_ip = ival_
        elif nodeName_ == 'static-route-enable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'static_route_enable')
            self.static_route_enable = ival_
# end class ServiceTemplateInterfaceType


class ServiceInstanceInterfaceType(GeneratedsSuper):
    """
    ServiceInstanceInterfaceType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, virtual_network=None, ip_address=None, static_routes=None, **kwargs):
        self.virtual_network = virtual_network
        self.ip_address = ip_address
        if isinstance(static_routes, dict):
            obj = RouteTableType(**static_routes)
            self.static_routes = obj
        else:
            self.static_routes = static_routes
    def factory(*args_, **kwargs_):
        if ServiceInstanceInterfaceType.subclass:
            return ServiceInstanceInterfaceType.subclass(*args_, **kwargs_)
        else:
            return ServiceInstanceInterfaceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_virtual_network(self): return self.virtual_network
    def set_virtual_network(self, virtual_network): self.virtual_network = virtual_network
    def get_ip_address(self): return self.ip_address
    def set_ip_address(self, ip_address): self.ip_address = ip_address
    def validate_IpAddressType(self, value):
        # Validate type IpAddressType, a restriction on xsd:string.
        pass
    def get_static_routes(self): return self.static_routes
    def set_static_routes(self, static_routes): self.static_routes = static_routes
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.virtual_network == other.virtual_network and
                self.ip_address == other.ip_address and
                self.static_routes == other.static_routes)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_virtual_network (obj.populate_string ("virtual_network"))
        obj.set_ip_address (obj.populate_string ("ip_address"))
        obj.set_static_routes (RouteTableType.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ServiceInstanceInterfaceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ServiceInstanceInterfaceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ServiceInstanceInterfaceType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ServiceInstanceInterfaceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.virtual_network is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-network>%s</%svirtual-network>%s' % (namespace_, self.gds_format_string(quote_xml(self.virtual_network).encode(ExternalEncoding), input_name='virtual-network'), namespace_, eol_))
        if self.ip_address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sip-address>%s</%sip-address>%s' % (namespace_, self.gds_format_string(quote_xml(self.ip_address).encode(ExternalEncoding), input_name='ip-address'), namespace_, eol_))
        if self.static_routes is not None:
            self.static_routes.export(outfile, level, namespace_, name_='static-routes', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.virtual_network is not None or
            self.ip_address is not None or
            self.static_routes is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ServiceInstanceInterfaceType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.virtual_network is not None:
            showIndent(outfile, level)
            outfile.write('virtual_network=%s,\n' % quote_python(self.virtual_network).encode(ExternalEncoding))
        if self.ip_address is not None:
            showIndent(outfile, level)
            outfile.write('ip_address=%s,\n' % quote_python(self.ip_address).encode(ExternalEncoding))
        if self.static_routes is not None:
            showIndent(outfile, level)
            outfile.write('static_routes=model_.RouteTableType(\n')
            self.static_routes.exportLiteral(outfile, level, name_='static_routes')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='ServiceInstanceInterfaceType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'virtual-network':
            virtual_network_ = child_.text
            virtual_network_ = self.gds_validate_string(virtual_network_, node, 'virtual_network')
            self.virtual_network = virtual_network_
        elif nodeName_ == 'ip-address':
            ip_address_ = child_.text
            ip_address_ = self.gds_validate_string(ip_address_, node, 'ip_address')
            self.ip_address = ip_address_
            self.validate_IpAddressType(self.ip_address)    # validate type IpAddressType
        elif nodeName_ == 'static-routes':
            obj_ = RouteTableType.factory()
            obj_.build(child_)
            self.set_static_routes(obj_)
# end class ServiceInstanceInterfaceType


class virtual_machine_interface_sub_interface(GeneratedsSuper):
    """
    virtual_machine_interface_sub_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_interface_sub_interface.subclass:
            return virtual_machine_interface_sub_interface.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_interface_sub_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-interface-sub-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-interface-sub-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-interface-sub-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-interface-sub-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-interface-sub-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-interface-sub-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_interface_sub_interface


class virtual_machine_virtual_machine_interface(GeneratedsSuper):
    """
    virtual_machine_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_virtual_machine_interface.subclass:
            return virtual_machine_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_virtual_machine_interface


class project_virtual_machine_interface(GeneratedsSuper):
    """
    project_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_virtual_machine_interface.subclass:
            return project_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return project_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_virtual_machine_interface


class virtual_machine_interface_virtual_machine(GeneratedsSuper):
    """
    virtual_machine_interface_virtual_machine class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_interface_virtual_machine.subclass:
            return virtual_machine_interface_virtual_machine.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_interface_virtual_machine(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-interface-virtual-machine', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-interface-virtual-machine')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-interface-virtual-machine'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-interface-virtual-machine', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-interface-virtual-machine'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-interface-virtual-machine'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_interface_virtual_machine


class virtual_machine_interface_virtual_network(GeneratedsSuper):
    """
    virtual_machine_interface_virtual_network class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_interface_virtual_network.subclass:
            return virtual_machine_interface_virtual_network.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_interface_virtual_network(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-interface-virtual-network', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-interface-virtual-network')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-interface-virtual-network'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-interface-virtual-network', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-interface-virtual-network'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-interface-virtual-network'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_interface_virtual_network


class PolicyBasedForwardingRuleType(GeneratedsSuper):
    """
    PolicyBasedForwardingRuleType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, direction=None, vlan_tag=None, src_mac=None, dst_mac=None, mpls_label=None, service_chain_address=None, protocol=None, **kwargs):
        self.direction = direction
        self.vlan_tag = vlan_tag
        self.src_mac = src_mac
        self.dst_mac = dst_mac
        self.mpls_label = mpls_label
        self.service_chain_address = service_chain_address
        self.protocol = protocol
    def factory(*args_, **kwargs_):
        if PolicyBasedForwardingRuleType.subclass:
            return PolicyBasedForwardingRuleType.subclass(*args_, **kwargs_)
        else:
            return PolicyBasedForwardingRuleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_direction(self): return self.direction
    def set_direction(self, direction): self.direction = direction
    def validate_TrafficDirectionType(self, value):
        # Validate type TrafficDirectionType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'ingress', u'egress', u'both'])
        else:
            error = value not in [u'ingress', u'egress', u'both']
        if error:
            raise ValueError("TrafficDirectionType must be one of [u'ingress', u'egress', u'both']")
    def get_vlan_tag(self): return self.vlan_tag
    def set_vlan_tag(self, vlan_tag): self.vlan_tag = vlan_tag
    def get_src_mac(self): return self.src_mac
    def set_src_mac(self, src_mac): self.src_mac = src_mac
    def get_dst_mac(self): return self.dst_mac
    def set_dst_mac(self, dst_mac): self.dst_mac = dst_mac
    def get_mpls_label(self): return self.mpls_label
    def set_mpls_label(self, mpls_label): self.mpls_label = mpls_label
    def get_service_chain_address(self): return self.service_chain_address
    def set_service_chain_address(self, service_chain_address): self.service_chain_address = service_chain_address
    def validate_IpAddress(self, value):
        # Validate type IpAddress, a restriction on xsd:string.
        pass
    def get_protocol(self): return self.protocol
    def set_protocol(self, protocol): self.protocol = protocol
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.direction == other.direction and
                self.vlan_tag == other.vlan_tag and
                self.src_mac == other.src_mac and
                self.dst_mac == other.dst_mac and
                self.mpls_label == other.mpls_label and
                self.service_chain_address == other.service_chain_address and
                self.protocol == other.protocol)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_direction (obj.populate_string ("direction"))
        obj.set_vlan_tag (obj.populate_integer ("vlan_tag"))
        obj.set_src_mac (obj.populate_string ("src_mac"))
        obj.set_dst_mac (obj.populate_string ("dst_mac"))
        obj.set_mpls_label (obj.populate_integer ("mpls_label"))
        obj.set_service_chain_address (obj.populate_string ("service_chain_address"))
        obj.set_protocol (obj.populate_string ("protocol"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='PolicyBasedForwardingRuleType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PolicyBasedForwardingRuleType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='PolicyBasedForwardingRuleType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='PolicyBasedForwardingRuleType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.direction is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdirection>%s</%sdirection>%s' % (namespace_, self.gds_format_string(quote_xml(self.direction).encode(ExternalEncoding), input_name='direction'), namespace_, eol_))
        if self.vlan_tag is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svlan-tag>%s</%svlan-tag>%s' % (namespace_, self.gds_format_integer(self.vlan_tag, input_name='vlan-tag'), namespace_, eol_))
        if self.src_mac is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssrc-mac>%s</%ssrc-mac>%s' % (namespace_, self.gds_format_string(quote_xml(self.src_mac).encode(ExternalEncoding), input_name='src-mac'), namespace_, eol_))
        if self.dst_mac is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdst-mac>%s</%sdst-mac>%s' % (namespace_, self.gds_format_string(quote_xml(self.dst_mac).encode(ExternalEncoding), input_name='dst-mac'), namespace_, eol_))
        if self.mpls_label is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smpls-label>%s</%smpls-label>%s' % (namespace_, self.gds_format_integer(self.mpls_label, input_name='mpls-label'), namespace_, eol_))
        if self.service_chain_address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-chain-address>%s</%sservice-chain-address>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_chain_address).encode(ExternalEncoding), input_name='service-chain-address'), namespace_, eol_))
        if self.protocol is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprotocol>%s</%sprotocol>%s' % (namespace_, self.gds_format_string(quote_xml(self.protocol).encode(ExternalEncoding), input_name='protocol'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.direction is not None or
            self.vlan_tag is not None or
            self.src_mac is not None or
            self.dst_mac is not None or
            self.mpls_label is not None or
            self.service_chain_address is not None or
            self.protocol is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PolicyBasedForwardingRuleType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.direction is not None:
            showIndent(outfile, level)
            outfile.write('direction=%s,\n' % quote_python(self.direction).encode(ExternalEncoding))
        if self.vlan_tag is not None:
            showIndent(outfile, level)
            outfile.write('vlan_tag=%d,\n' % self.vlan_tag)
        if self.src_mac is not None:
            showIndent(outfile, level)
            outfile.write('src_mac=%s,\n' % quote_python(self.src_mac).encode(ExternalEncoding))
        if self.dst_mac is not None:
            showIndent(outfile, level)
            outfile.write('dst_mac=%s,\n' % quote_python(self.dst_mac).encode(ExternalEncoding))
        if self.mpls_label is not None:
            showIndent(outfile, level)
            outfile.write('mpls_label=%d,\n' % self.mpls_label)
        if self.service_chain_address is not None:
            showIndent(outfile, level)
            outfile.write('service_chain_address=%s,\n' % quote_python(self.service_chain_address).encode(ExternalEncoding))
        if self.protocol is not None:
            showIndent(outfile, level)
            outfile.write('protocol=%s,\n' % quote_python(self.protocol).encode(ExternalEncoding))
    def exportDict(self, name_='PolicyBasedForwardingRuleType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'direction':
            direction_ = child_.text
            direction_ = self.gds_validate_string(direction_, node, 'direction')
            self.direction = direction_
            self.validate_TrafficDirectionType(self.direction)    # validate type TrafficDirectionType
        elif nodeName_ == 'vlan-tag':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'vlan_tag')
            self.vlan_tag = ival_
        elif nodeName_ == 'src-mac':
            src_mac_ = child_.text
            src_mac_ = self.gds_validate_string(src_mac_, node, 'src_mac')
            self.src_mac = src_mac_
        elif nodeName_ == 'dst-mac':
            dst_mac_ = child_.text
            dst_mac_ = self.gds_validate_string(dst_mac_, node, 'dst_mac')
            self.dst_mac = dst_mac_
        elif nodeName_ == 'mpls-label':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'mpls_label')
            self.mpls_label = ival_
        elif nodeName_ == 'service-chain-address':
            service_chain_address_ = child_.text
            service_chain_address_ = self.gds_validate_string(service_chain_address_, node, 'service_chain_address')
            self.service_chain_address = service_chain_address_
            self.validate_IpAddress(self.service_chain_address)    # validate type IpAddress
        elif nodeName_ == 'protocol':
            protocol_ = child_.text
            protocol_ = self.gds_validate_string(protocol_, node, 'protocol')
            self.protocol = protocol_
# end class PolicyBasedForwardingRuleType


class instance_ip_virtual_network(GeneratedsSuper):
    """
    instance_ip_virtual_network class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if instance_ip_virtual_network.subclass:
            return instance_ip_virtual_network.subclass(*args_, **kwargs_)
        else:
            return instance_ip_virtual_network(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='instance-ip-virtual-network', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='instance-ip-virtual-network')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='instance-ip-virtual-network'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='instance-ip-virtual-network', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='instance-ip-virtual-network'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='instance-ip-virtual-network'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class instance_ip_virtual_network


class instance_ip_virtual_machine_interface(GeneratedsSuper):
    """
    instance_ip_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if instance_ip_virtual_machine_interface.subclass:
            return instance_ip_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return instance_ip_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='instance-ip-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='instance-ip-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='instance-ip-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='instance-ip-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='instance-ip-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='instance-ip-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class instance_ip_virtual_machine_interface


class subnet_virtual_machine_interface(GeneratedsSuper):
    """
    subnet_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if subnet_virtual_machine_interface.subclass:
            return subnet_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return subnet_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='subnet-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='subnet-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='subnet-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='subnet-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='subnet-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='subnet-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class subnet_virtual_machine_interface


class virtual_network_floating_ip_pool(GeneratedsSuper):
    """
    virtual_network_floating_ip_pool class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_network_floating_ip_pool.subclass:
            return virtual_network_floating_ip_pool.subclass(*args_, **kwargs_)
        else:
            return virtual_network_floating_ip_pool(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-network-floating-ip-pool', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-network-floating-ip-pool')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-network-floating-ip-pool'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-network-floating-ip-pool', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-network-floating-ip-pool'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-network-floating-ip-pool'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_network_floating_ip_pool


class project_floating_ip_pool(GeneratedsSuper):
    """
    project_floating_ip_pool class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_floating_ip_pool.subclass:
            return project_floating_ip_pool.subclass(*args_, **kwargs_)
        else:
            return project_floating_ip_pool(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-floating-ip-pool', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-floating-ip-pool')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-floating-ip-pool'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-floating-ip-pool', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-floating-ip-pool'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-floating-ip-pool'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_floating_ip_pool


class floating_ip_project(GeneratedsSuper):
    """
    floating_ip_project class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if floating_ip_project.subclass:
            return floating_ip_project.subclass(*args_, **kwargs_)
        else:
            return floating_ip_project(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='floating-ip-project', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='floating-ip-project')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='floating-ip-project'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='floating-ip-project', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='floating-ip-project'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='floating-ip-project'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class floating_ip_project


class floating_ip_pool_floating_ip(GeneratedsSuper):
    """
    floating_ip_pool_floating_ip class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if floating_ip_pool_floating_ip.subclass:
            return floating_ip_pool_floating_ip.subclass(*args_, **kwargs_)
        else:
            return floating_ip_pool_floating_ip(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='floating-ip-pool-floating-ip', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='floating-ip-pool-floating-ip')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='floating-ip-pool-floating-ip'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='floating-ip-pool-floating-ip', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='floating-ip-pool-floating-ip'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='floating-ip-pool-floating-ip'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class floating_ip_pool_floating_ip


class floating_ip_virtual_machine_interface(GeneratedsSuper):
    """
    floating_ip_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if floating_ip_virtual_machine_interface.subclass:
            return floating_ip_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return floating_ip_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='floating-ip-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='floating-ip-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='floating-ip-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='floating-ip-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='floating-ip-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='floating-ip-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class floating_ip_virtual_machine_interface


class global_system_config_physical_router(GeneratedsSuper):
    """
    global_system_config_physical_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_physical_router.subclass:
            return global_system_config_physical_router.subclass(*args_, **kwargs_)
        else:
            return global_system_config_physical_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-physical-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-physical-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-physical-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-physical-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-physical-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-physical-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_physical_router


class physical_router_virtual_router(GeneratedsSuper):
    """
    physical_router_virtual_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if physical_router_virtual_router.subclass:
            return physical_router_virtual_router.subclass(*args_, **kwargs_)
        else:
            return physical_router_virtual_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='physical-router-virtual-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='physical-router-virtual-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='physical-router-virtual-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='physical-router-virtual-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='physical-router-virtual-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='physical-router-virtual-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class physical_router_virtual_router


class physical_router_bgp_router(GeneratedsSuper):
    """
    physical_router_bgp_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if physical_router_bgp_router.subclass:
            return physical_router_bgp_router.subclass(*args_, **kwargs_)
        else:
            return physical_router_bgp_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='physical-router-bgp-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='physical-router-bgp-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='physical-router-bgp-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='physical-router-bgp-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='physical-router-bgp-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='physical-router-bgp-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class physical_router_bgp_router


class physical_router_virtual_network(GeneratedsSuper):
    """
    physical_router_virtual_network class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if physical_router_virtual_network.subclass:
            return physical_router_virtual_network.subclass(*args_, **kwargs_)
        else:
            return physical_router_virtual_network(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='physical-router-virtual-network', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='physical-router-virtual-network')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='physical-router-virtual-network'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='physical-router-virtual-network', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='physical-router-virtual-network'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='physical-router-virtual-network'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class physical_router_virtual_network


class physical_router_physical_interface(GeneratedsSuper):
    """
    physical_router_physical_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if physical_router_physical_interface.subclass:
            return physical_router_physical_interface.subclass(*args_, **kwargs_)
        else:
            return physical_router_physical_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='physical-router-physical-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='physical-router-physical-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='physical-router-physical-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='physical-router-physical-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='physical-router-physical-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='physical-router-physical-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class physical_router_physical_interface


class physical_router_logical_interface(GeneratedsSuper):
    """
    physical_router_logical_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if physical_router_logical_interface.subclass:
            return physical_router_logical_interface.subclass(*args_, **kwargs_)
        else:
            return physical_router_logical_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='physical-router-logical-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='physical-router-logical-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='physical-router-logical-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='physical-router-logical-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='physical-router-logical-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='physical-router-logical-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class physical_router_logical_interface


class physical_interface_logical_interface(GeneratedsSuper):
    """
    physical_interface_logical_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if physical_interface_logical_interface.subclass:
            return physical_interface_logical_interface.subclass(*args_, **kwargs_)
        else:
            return physical_interface_logical_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='physical-interface-logical-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='physical-interface-logical-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='physical-interface-logical-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='physical-interface-logical-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='physical-interface-logical-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='physical-interface-logical-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class physical_interface_logical_interface


class UserCredentials(GeneratedsSuper):
    """
    UserCredentials class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, username=None, password=None, **kwargs):
        self.username = username
        self.password = password
    def factory(*args_, **kwargs_):
        if UserCredentials.subclass:
            return UserCredentials.subclass(*args_, **kwargs_)
        else:
            return UserCredentials(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_username(self): return self.username
    def set_username(self, username): self.username = username
    def get_password(self): return self.password
    def set_password(self, password): self.password = password
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.username == other.username and
                self.password == other.password)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_username (obj.populate_string ("username"))
        obj.set_password (obj.populate_string ("password"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='UserCredentials', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='UserCredentials')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='UserCredentials'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='UserCredentials', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.username is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%susername>%s</%susername>%s' % (namespace_, self.gds_format_string(quote_xml(self.username).encode(ExternalEncoding), input_name='username'), namespace_, eol_))
        if self.password is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spassword>%s</%spassword>%s' % (namespace_, self.gds_format_string(quote_xml(self.password).encode(ExternalEncoding), input_name='password'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.username is not None or
            self.password is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='UserCredentials'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.username is not None:
            showIndent(outfile, level)
            outfile.write('username=%s,\n' % quote_python(self.username).encode(ExternalEncoding))
        if self.password is not None:
            showIndent(outfile, level)
            outfile.write('password=%s,\n' % quote_python(self.password).encode(ExternalEncoding))
    def exportDict(self, name_='UserCredentials'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'username':
            username_ = child_.text
            username_ = self.gds_validate_string(username_, node, 'username')
            self.username = username_
        elif nodeName_ == 'password':
            password_ = child_.text
            password_ = self.gds_validate_string(password_, node, 'password')
            self.password = password_
# end class UserCredentials


class SNMPCredentials(GeneratedsSuper):
    """
    SNMPCredentials class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, version=2, local_port=None, retries=None, timeout=None, v2_community=None, v3_security_name=None, v3_security_level=None, v3_security_engine_id=None, v3_context=None, v3_context_engine_id=None, v3_authentication_protocol=None, v3_authentication_password=None, v3_privacy_protocol=None, v3_privacy_password=None, v3_engine_id=None, v3_engine_boots=None, v3_engine_time=None, **kwargs):
        self.version = version
        self.local_port = local_port
        self.retries = retries
        self.timeout = timeout
        self.v2_community = v2_community
        self.v3_security_name = v3_security_name
        self.v3_security_level = v3_security_level
        self.v3_security_engine_id = v3_security_engine_id
        self.v3_context = v3_context
        self.v3_context_engine_id = v3_context_engine_id
        self.v3_authentication_protocol = v3_authentication_protocol
        self.v3_authentication_password = v3_authentication_password
        self.v3_privacy_protocol = v3_privacy_protocol
        self.v3_privacy_password = v3_privacy_password
        self.v3_engine_id = v3_engine_id
        self.v3_engine_boots = v3_engine_boots
        self.v3_engine_time = v3_engine_time
    def factory(*args_, **kwargs_):
        if SNMPCredentials.subclass:
            return SNMPCredentials.subclass(*args_, **kwargs_)
        else:
            return SNMPCredentials(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_local_port(self): return self.local_port
    def set_local_port(self, local_port): self.local_port = local_port
    def get_retries(self): return self.retries
    def set_retries(self, retries): self.retries = retries
    def get_timeout(self): return self.timeout
    def set_timeout(self, timeout): self.timeout = timeout
    def get_v2_community(self): return self.v2_community
    def set_v2_community(self, v2_community): self.v2_community = v2_community
    def get_v3_security_name(self): return self.v3_security_name
    def set_v3_security_name(self, v3_security_name): self.v3_security_name = v3_security_name
    def get_v3_security_level(self): return self.v3_security_level
    def set_v3_security_level(self, v3_security_level): self.v3_security_level = v3_security_level
    def get_v3_security_engine_id(self): return self.v3_security_engine_id
    def set_v3_security_engine_id(self, v3_security_engine_id): self.v3_security_engine_id = v3_security_engine_id
    def get_v3_context(self): return self.v3_context
    def set_v3_context(self, v3_context): self.v3_context = v3_context
    def get_v3_context_engine_id(self): return self.v3_context_engine_id
    def set_v3_context_engine_id(self, v3_context_engine_id): self.v3_context_engine_id = v3_context_engine_id
    def get_v3_authentication_protocol(self): return self.v3_authentication_protocol
    def set_v3_authentication_protocol(self, v3_authentication_protocol): self.v3_authentication_protocol = v3_authentication_protocol
    def get_v3_authentication_password(self): return self.v3_authentication_password
    def set_v3_authentication_password(self, v3_authentication_password): self.v3_authentication_password = v3_authentication_password
    def get_v3_privacy_protocol(self): return self.v3_privacy_protocol
    def set_v3_privacy_protocol(self, v3_privacy_protocol): self.v3_privacy_protocol = v3_privacy_protocol
    def get_v3_privacy_password(self): return self.v3_privacy_password
    def set_v3_privacy_password(self, v3_privacy_password): self.v3_privacy_password = v3_privacy_password
    def get_v3_engine_id(self): return self.v3_engine_id
    def set_v3_engine_id(self, v3_engine_id): self.v3_engine_id = v3_engine_id
    def get_v3_engine_boots(self): return self.v3_engine_boots
    def set_v3_engine_boots(self, v3_engine_boots): self.v3_engine_boots = v3_engine_boots
    def get_v3_engine_time(self): return self.v3_engine_time
    def set_v3_engine_time(self, v3_engine_time): self.v3_engine_time = v3_engine_time
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.version == other.version and
                self.local_port == other.local_port and
                self.retries == other.retries and
                self.timeout == other.timeout and
                self.v2_community == other.v2_community and
                self.v3_security_name == other.v3_security_name and
                self.v3_security_level == other.v3_security_level and
                self.v3_security_engine_id == other.v3_security_engine_id and
                self.v3_context == other.v3_context and
                self.v3_context_engine_id == other.v3_context_engine_id and
                self.v3_authentication_protocol == other.v3_authentication_protocol and
                self.v3_authentication_password == other.v3_authentication_password and
                self.v3_privacy_protocol == other.v3_privacy_protocol and
                self.v3_privacy_password == other.v3_privacy_password and
                self.v3_engine_id == other.v3_engine_id and
                self.v3_engine_boots == other.v3_engine_boots and
                self.v3_engine_time == other.v3_engine_time)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_version (obj.populate_integer ("version"))
        obj.set_local_port (obj.populate_integer ("local_port"))
        obj.set_retries (obj.populate_integer ("retries"))
        obj.set_timeout (obj.populate_integer ("timeout"))
        obj.set_v2_community (obj.populate_string ("v2_community"))
        obj.set_v3_security_name (obj.populate_string ("v3_security_name"))
        obj.set_v3_security_level (obj.populate_string ("v3_security_level"))
        obj.set_v3_security_engine_id (obj.populate_string ("v3_security_engine_id"))
        obj.set_v3_context (obj.populate_string ("v3_context"))
        obj.set_v3_context_engine_id (obj.populate_string ("v3_context_engine_id"))
        obj.set_v3_authentication_protocol (obj.populate_string ("v3_authentication_protocol"))
        obj.set_v3_authentication_password (obj.populate_string ("v3_authentication_password"))
        obj.set_v3_privacy_protocol (obj.populate_string ("v3_privacy_protocol"))
        obj.set_v3_privacy_password (obj.populate_string ("v3_privacy_password"))
        obj.set_v3_engine_id (obj.populate_string ("v3_engine_id"))
        obj.set_v3_engine_boots (obj.populate_integer ("v3_engine_boots"))
        obj.set_v3_engine_time (obj.populate_integer ("v3_engine_time"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='SNMPCredentials', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SNMPCredentials')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='SNMPCredentials'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='SNMPCredentials', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.version is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sversion>%s</%sversion>%s' % (namespace_, self.gds_format_integer(self.version, input_name='version'), namespace_, eol_))
        if self.local_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocal-port>%s</%slocal-port>%s' % (namespace_, self.gds_format_integer(self.local_port, input_name='local-port'), namespace_, eol_))
        if self.retries is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sretries>%s</%sretries>%s' % (namespace_, self.gds_format_integer(self.retries, input_name='retries'), namespace_, eol_))
        if self.timeout is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stimeout>%s</%stimeout>%s' % (namespace_, self.gds_format_integer(self.timeout, input_name='timeout'), namespace_, eol_))
        if self.v2_community is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv2-community>%s</%sv2-community>%s' % (namespace_, self.gds_format_string(quote_xml(self.v2_community).encode(ExternalEncoding), input_name='v2-community'), namespace_, eol_))
        if self.v3_security_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-security-name>%s</%sv3-security-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_security_name).encode(ExternalEncoding), input_name='v3-security-name'), namespace_, eol_))
        if self.v3_security_level is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-security-level>%s</%sv3-security-level>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_security_level).encode(ExternalEncoding), input_name='v3-security-level'), namespace_, eol_))
        if self.v3_security_engine_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-security-engine-id>%s</%sv3-security-engine-id>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_security_engine_id).encode(ExternalEncoding), input_name='v3-security-engine-id'), namespace_, eol_))
        if self.v3_context is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-context>%s</%sv3-context>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_context).encode(ExternalEncoding), input_name='v3-context'), namespace_, eol_))
        if self.v3_context_engine_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-context-engine-id>%s</%sv3-context-engine-id>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_context_engine_id).encode(ExternalEncoding), input_name='v3-context-engine-id'), namespace_, eol_))
        if self.v3_authentication_protocol is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-authentication-protocol>%s</%sv3-authentication-protocol>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_authentication_protocol).encode(ExternalEncoding), input_name='v3-authentication-protocol'), namespace_, eol_))
        if self.v3_authentication_password is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-authentication-password>%s</%sv3-authentication-password>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_authentication_password).encode(ExternalEncoding), input_name='v3-authentication-password'), namespace_, eol_))
        if self.v3_privacy_protocol is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-privacy-protocol>%s</%sv3-privacy-protocol>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_privacy_protocol).encode(ExternalEncoding), input_name='v3-privacy-protocol'), namespace_, eol_))
        if self.v3_privacy_password is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-privacy-password>%s</%sv3-privacy-password>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_privacy_password).encode(ExternalEncoding), input_name='v3-privacy-password'), namespace_, eol_))
        if self.v3_engine_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-engine-id>%s</%sv3-engine-id>%s' % (namespace_, self.gds_format_string(quote_xml(self.v3_engine_id).encode(ExternalEncoding), input_name='v3-engine-id'), namespace_, eol_))
        if self.v3_engine_boots is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-engine-boots>%s</%sv3-engine-boots>%s' % (namespace_, self.gds_format_integer(self.v3_engine_boots, input_name='v3-engine-boots'), namespace_, eol_))
        if self.v3_engine_time is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sv3-engine-time>%s</%sv3-engine-time>%s' % (namespace_, self.gds_format_integer(self.v3_engine_time, input_name='v3-engine-time'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.version is not None or
            self.local_port is not None or
            self.retries is not None or
            self.timeout is not None or
            self.v2_community is not None or
            self.v3_security_name is not None or
            self.v3_security_level is not None or
            self.v3_security_engine_id is not None or
            self.v3_context is not None or
            self.v3_context_engine_id is not None or
            self.v3_authentication_protocol is not None or
            self.v3_authentication_password is not None or
            self.v3_privacy_protocol is not None or
            self.v3_privacy_password is not None or
            self.v3_engine_id is not None or
            self.v3_engine_boots is not None or
            self.v3_engine_time is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='SNMPCredentials'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.version is not None:
            showIndent(outfile, level)
            outfile.write('version=%d,\n' % self.version)
        if self.local_port is not None:
            showIndent(outfile, level)
            outfile.write('local_port=%d,\n' % self.local_port)
        if self.retries is not None:
            showIndent(outfile, level)
            outfile.write('retries=%d,\n' % self.retries)
        if self.timeout is not None:
            showIndent(outfile, level)
            outfile.write('timeout=%d,\n' % self.timeout)
        if self.v2_community is not None:
            showIndent(outfile, level)
            outfile.write('v2_community=%s,\n' % quote_python(self.v2_community).encode(ExternalEncoding))
        if self.v3_security_name is not None:
            showIndent(outfile, level)
            outfile.write('v3_security_name=%s,\n' % quote_python(self.v3_security_name).encode(ExternalEncoding))
        if self.v3_security_level is not None:
            showIndent(outfile, level)
            outfile.write('v3_security_level=%s,\n' % quote_python(self.v3_security_level).encode(ExternalEncoding))
        if self.v3_security_engine_id is not None:
            showIndent(outfile, level)
            outfile.write('v3_security_engine_id=%s,\n' % quote_python(self.v3_security_engine_id).encode(ExternalEncoding))
        if self.v3_context is not None:
            showIndent(outfile, level)
            outfile.write('v3_context=%s,\n' % quote_python(self.v3_context).encode(ExternalEncoding))
        if self.v3_context_engine_id is not None:
            showIndent(outfile, level)
            outfile.write('v3_context_engine_id=%s,\n' % quote_python(self.v3_context_engine_id).encode(ExternalEncoding))
        if self.v3_authentication_protocol is not None:
            showIndent(outfile, level)
            outfile.write('v3_authentication_protocol=%s,\n' % quote_python(self.v3_authentication_protocol).encode(ExternalEncoding))
        if self.v3_authentication_password is not None:
            showIndent(outfile, level)
            outfile.write('v3_authentication_password=%s,\n' % quote_python(self.v3_authentication_password).encode(ExternalEncoding))
        if self.v3_privacy_protocol is not None:
            showIndent(outfile, level)
            outfile.write('v3_privacy_protocol=%s,\n' % quote_python(self.v3_privacy_protocol).encode(ExternalEncoding))
        if self.v3_privacy_password is not None:
            showIndent(outfile, level)
            outfile.write('v3_privacy_password=%s,\n' % quote_python(self.v3_privacy_password).encode(ExternalEncoding))
        if self.v3_engine_id is not None:
            showIndent(outfile, level)
            outfile.write('v3_engine_id=%s,\n' % quote_python(self.v3_engine_id).encode(ExternalEncoding))
        if self.v3_engine_boots is not None:
            showIndent(outfile, level)
            outfile.write('v3_engine_boots=%d,\n' % self.v3_engine_boots)
        if self.v3_engine_time is not None:
            showIndent(outfile, level)
            outfile.write('v3_engine_time=%d,\n' % self.v3_engine_time)
    def exportDict(self, name_='SNMPCredentials'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'version':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'version')
            self.version = ival_
        elif nodeName_ == 'local-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'local_port')
            self.local_port = ival_
        elif nodeName_ == 'retries':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'retries')
            self.retries = ival_
        elif nodeName_ == 'timeout':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'timeout')
            self.timeout = ival_
        elif nodeName_ == 'v2-community':
            v2_community_ = child_.text
            v2_community_ = self.gds_validate_string(v2_community_, node, 'v2_community')
            self.v2_community = v2_community_
        elif nodeName_ == 'v3-security-name':
            v3_security_name_ = child_.text
            v3_security_name_ = self.gds_validate_string(v3_security_name_, node, 'v3_security_name')
            self.v3_security_name = v3_security_name_
        elif nodeName_ == 'v3-security-level':
            v3_security_level_ = child_.text
            v3_security_level_ = self.gds_validate_string(v3_security_level_, node, 'v3_security_level')
            self.v3_security_level = v3_security_level_
        elif nodeName_ == 'v3-security-engine-id':
            v3_security_engine_id_ = child_.text
            v3_security_engine_id_ = self.gds_validate_string(v3_security_engine_id_, node, 'v3_security_engine_id')
            self.v3_security_engine_id = v3_security_engine_id_
        elif nodeName_ == 'v3-context':
            v3_context_ = child_.text
            v3_context_ = self.gds_validate_string(v3_context_, node, 'v3_context')
            self.v3_context = v3_context_
        elif nodeName_ == 'v3-context-engine-id':
            v3_context_engine_id_ = child_.text
            v3_context_engine_id_ = self.gds_validate_string(v3_context_engine_id_, node, 'v3_context_engine_id')
            self.v3_context_engine_id = v3_context_engine_id_
        elif nodeName_ == 'v3-authentication-protocol':
            v3_authentication_protocol_ = child_.text
            v3_authentication_protocol_ = self.gds_validate_string(v3_authentication_protocol_, node, 'v3_authentication_protocol')
            self.v3_authentication_protocol = v3_authentication_protocol_
        elif nodeName_ == 'v3-authentication-password':
            v3_authentication_password_ = child_.text
            v3_authentication_password_ = self.gds_validate_string(v3_authentication_password_, node, 'v3_authentication_password')
            self.v3_authentication_password = v3_authentication_password_
        elif nodeName_ == 'v3-privacy-protocol':
            v3_privacy_protocol_ = child_.text
            v3_privacy_protocol_ = self.gds_validate_string(v3_privacy_protocol_, node, 'v3_privacy_protocol')
            self.v3_privacy_protocol = v3_privacy_protocol_
        elif nodeName_ == 'v3-privacy-password':
            v3_privacy_password_ = child_.text
            v3_privacy_password_ = self.gds_validate_string(v3_privacy_password_, node, 'v3_privacy_password')
            self.v3_privacy_password = v3_privacy_password_
        elif nodeName_ == 'v3-engine-id':
            v3_engine_id_ = child_.text
            v3_engine_id_ = self.gds_validate_string(v3_engine_id_, node, 'v3_engine_id')
            self.v3_engine_id = v3_engine_id_
        elif nodeName_ == 'v3-engine-boots':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'v3_engine_boots')
            self.v3_engine_boots = ival_
        elif nodeName_ == 'v3-engine-time':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'v3_engine_time')
            self.v3_engine_time = ival_
# end class SNMPCredentials


class JunosServicePorts(GeneratedsSuper):
    """
    JunosServicePorts class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, service_port=None, **kwargs):
        if (service_port is None) or (service_port == []):
            self.service_port = []
        else:
            self.service_port = service_port
    def factory(*args_, **kwargs_):
        if JunosServicePorts.subclass:
            return JunosServicePorts.subclass(*args_, **kwargs_)
        else:
            return JunosServicePorts(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_service_port(self): return self.service_port
    def set_service_port(self, service_port): self.service_port = service_port
    def add_service_port(self, value): self.service_port.append(value)
    def insert_service_port(self, index, value): self.service_port[index] = value
    def delete_service_port(self, value): self.service_port.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.service_port == other.service_port)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_service_port ([obj.populate_string ("service_port")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='JunosServicePorts', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='JunosServicePorts')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='JunosServicePorts'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='JunosServicePorts', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for service_port_ in self.service_port:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-port>%s</%sservice-port>%s' % (namespace_, self.gds_format_string(quote_xml(service_port_).encode(ExternalEncoding), input_name='service-port'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.service_port
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='JunosServicePorts'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('service_port=[\n')
        level += 1
        for service_port_ in self.service_port:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(service_port_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='JunosServicePorts'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'service-port':
            service_port_ = child_.text
            service_port_ = self.gds_validate_string(service_port_, node, 'service_port')
            self.service_port.append(service_port_)
# end class JunosServicePorts


class logical_interface_virtual_machine_interface(GeneratedsSuper):
    """
    logical_interface_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if logical_interface_virtual_machine_interface.subclass:
            return logical_interface_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return logical_interface_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='logical-interface-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='logical-interface-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='logical-interface-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='logical-interface-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='logical-interface-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='logical-interface-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class logical_interface_virtual_machine_interface


class global_system_config_virtual_router(GeneratedsSuper):
    """
    global_system_config_virtual_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_virtual_router.subclass:
            return global_system_config_virtual_router.subclass(*args_, **kwargs_)
        else:
            return global_system_config_virtual_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-virtual-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-virtual-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-virtual-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-virtual-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-virtual-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-virtual-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_virtual_router


class virtual_router_bgp_router(GeneratedsSuper):
    """
    virtual_router_bgp_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_router_bgp_router.subclass:
            return virtual_router_bgp_router.subclass(*args_, **kwargs_)
        else:
            return virtual_router_bgp_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-router-bgp-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-router-bgp-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-router-bgp-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-router-bgp-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-router-bgp-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-router-bgp-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_router_bgp_router


class virtual_router_virtual_machine(GeneratedsSuper):
    """
    virtual_router_virtual_machine class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_router_virtual_machine.subclass:
            return virtual_router_virtual_machine.subclass(*args_, **kwargs_)
        else:
            return virtual_router_virtual_machine(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-router-virtual-machine', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-router-virtual-machine')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-router-virtual-machine'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-router-virtual-machine', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-router-virtual-machine'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-router-virtual-machine'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_router_virtual_machine


class virtual_network_routing_instance(GeneratedsSuper):
    """
    virtual_network_routing_instance class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_network_routing_instance.subclass:
            return virtual_network_routing_instance.subclass(*args_, **kwargs_)
        else:
            return virtual_network_routing_instance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-network-routing-instance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-network-routing-instance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-network-routing-instance'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-network-routing-instance', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-network-routing-instance'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-network-routing-instance'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_network_routing_instance


class customer_attachment_virtual_machine_interface(GeneratedsSuper):
    """
    customer_attachment_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if customer_attachment_virtual_machine_interface.subclass:
            return customer_attachment_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return customer_attachment_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='customer-attachment-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='customer-attachment-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='customer-attachment-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='customer-attachment-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='customer-attachment-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='customer-attachment-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class customer_attachment_virtual_machine_interface


class customer_attachment_floating_ip(GeneratedsSuper):
    """
    customer_attachment_floating_ip class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if customer_attachment_floating_ip.subclass:
            return customer_attachment_floating_ip.subclass(*args_, **kwargs_)
        else:
            return customer_attachment_floating_ip(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='customer-attachment-floating-ip', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='customer-attachment-floating-ip')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='customer-attachment-floating-ip'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='customer-attachment-floating-ip', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='customer-attachment-floating-ip'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='customer-attachment-floating-ip'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class customer_attachment_floating_ip


class provider_attachment_virtual_router(GeneratedsSuper):
    """
    provider_attachment_virtual_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if provider_attachment_virtual_router.subclass:
            return provider_attachment_virtual_router.subclass(*args_, **kwargs_)
        else:
            return provider_attachment_virtual_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='provider-attachment-virtual-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='provider-attachment-virtual-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='provider-attachment-virtual-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='provider-attachment-virtual-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='provider-attachment-virtual-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='provider-attachment-virtual-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class provider_attachment_virtual_router


class ServiceScaleOutType(GeneratedsSuper):
    """
    ServiceScaleOutType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, max_instances=1, auto_scale=False, **kwargs):
        self.max_instances = max_instances
        self.auto_scale = auto_scale
    def factory(*args_, **kwargs_):
        if ServiceScaleOutType.subclass:
            return ServiceScaleOutType.subclass(*args_, **kwargs_)
        else:
            return ServiceScaleOutType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_max_instances(self): return self.max_instances
    def set_max_instances(self, max_instances): self.max_instances = max_instances
    def get_auto_scale(self): return self.auto_scale
    def set_auto_scale(self, auto_scale): self.auto_scale = auto_scale
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.max_instances == other.max_instances and
                self.auto_scale == other.auto_scale)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_max_instances (obj.populate_integer ("max_instances"))
        obj.set_auto_scale (obj.populate_boolean ("auto_scale"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ServiceScaleOutType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ServiceScaleOutType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ServiceScaleOutType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ServiceScaleOutType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.max_instances is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smax-instances>%s</%smax-instances>%s' % (namespace_, self.gds_format_integer(self.max_instances, input_name='max-instances'), namespace_, eol_))
        if self.auto_scale is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauto-scale>%s</%sauto-scale>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.auto_scale)), input_name='auto-scale'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.max_instances is not None or
            self.auto_scale is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ServiceScaleOutType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.max_instances is not None:
            showIndent(outfile, level)
            outfile.write('max_instances=%d,\n' % self.max_instances)
        if self.auto_scale is not None:
            showIndent(outfile, level)
            outfile.write('auto_scale=%s,\n' % self.auto_scale)
    def exportDict(self, name_='ServiceScaleOutType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'max-instances':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'max_instances')
            self.max_instances = ival_
        elif nodeName_ == 'auto-scale':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'auto_scale')
            self.auto_scale = ival_
# end class ServiceScaleOutType


class ServiceTemplateType(GeneratedsSuper):
    """
    ServiceTemplateType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, service_mode=None, service_type=None, image_name=None, service_scaling=False, interface_type=None, flavor=None, ordered_interfaces=False, service_virtualization_type=None, availability_zone_enable=False, vrouter_instance_type=None, instance_data=None, **kwargs):
        self.service_mode = service_mode
        self.service_type = service_type
        self.image_name = image_name
        self.service_scaling = service_scaling
        if (interface_type is None) or (interface_type == []):
            self.interface_type = []
        else:
            if isinstance(interface_type[0], dict):
                objs = [ServiceTemplateInterfaceType(**elem) for elem in interface_type]
                self.interface_type = objs
            else:
                self.interface_type = interface_type
        self.flavor = flavor
        self.ordered_interfaces = ordered_interfaces
        self.service_virtualization_type = service_virtualization_type
        self.availability_zone_enable = availability_zone_enable
        self.vrouter_instance_type = vrouter_instance_type
        self.instance_data = instance_data
    def factory(*args_, **kwargs_):
        if ServiceTemplateType.subclass:
            return ServiceTemplateType.subclass(*args_, **kwargs_)
        else:
            return ServiceTemplateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_service_mode(self): return self.service_mode
    def set_service_mode(self, service_mode): self.service_mode = service_mode
    def validate_ServiceModeType(self, value):
        # Validate type ServiceModeType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'transparent', u'in-network', u'in-network-nat'])
        else:
            error = value not in [u'transparent', u'in-network', u'in-network-nat']
        if error:
            raise ValueError("ServiceModeType must be one of [u'transparent', u'in-network', u'in-network-nat']")
    def get_service_type(self): return self.service_type
    def set_service_type(self, service_type): self.service_type = service_type
    def validate_ServiceType(self, value):
        # Validate type ServiceType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'firewall', u'analyzer', u'source-nat', u'loadbalancer'])
        else:
            error = value not in [u'firewall', u'analyzer', u'source-nat', u'loadbalancer']
        if error:
            raise ValueError("ServiceType must be one of [u'firewall', u'analyzer', u'source-nat', u'loadbalancer']")
    def get_image_name(self): return self.image_name
    def set_image_name(self, image_name): self.image_name = image_name
    def get_service_scaling(self): return self.service_scaling
    def set_service_scaling(self, service_scaling): self.service_scaling = service_scaling
    def get_interface_type(self): return self.interface_type
    def set_interface_type(self, interface_type): self.interface_type = interface_type
    def add_interface_type(self, value): self.interface_type.append(value)
    def insert_interface_type(self, index, value): self.interface_type[index] = value
    def delete_interface_type(self, value): self.interface_type.remove(value)
    def get_flavor(self): return self.flavor
    def set_flavor(self, flavor): self.flavor = flavor
    def get_ordered_interfaces(self): return self.ordered_interfaces
    def set_ordered_interfaces(self, ordered_interfaces): self.ordered_interfaces = ordered_interfaces
    def get_service_virtualization_type(self): return self.service_virtualization_type
    def set_service_virtualization_type(self, service_virtualization_type): self.service_virtualization_type = service_virtualization_type
    def validate_ServiceVirtualizationType(self, value):
        # Validate type ServiceVirtualizationType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'virtual-machine', u'network-namespace', u'vrouter-instance'])
        else:
            error = value not in [u'virtual-machine', u'network-namespace', u'vrouter-instance']
        if error:
            raise ValueError("ServiceVirtualizationType must be one of [u'virtual-machine', u'network-namespace', u'vrouter-instance']")
    def get_availability_zone_enable(self): return self.availability_zone_enable
    def set_availability_zone_enable(self, availability_zone_enable): self.availability_zone_enable = availability_zone_enable
    def get_vrouter_instance_type(self): return self.vrouter_instance_type
    def set_vrouter_instance_type(self, vrouter_instance_type): self.vrouter_instance_type = vrouter_instance_type
    def validate_VRouterInstanceType(self, value):
        # Validate type VRouterInstanceType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'libvirt-qemu', u'docker'])
        else:
            error = value not in [u'libvirt-qemu', u'docker']
        if error:
            raise ValueError("VRouterInstanceType must be one of [u'libvirt-qemu', u'docker']")
    def get_instance_data(self): return self.instance_data
    def set_instance_data(self, instance_data): self.instance_data = instance_data
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.service_mode == other.service_mode and
                self.service_type == other.service_type and
                self.image_name == other.image_name and
                self.service_scaling == other.service_scaling and
                self.interface_type == other.interface_type and
                self.flavor == other.flavor and
                self.ordered_interfaces == other.ordered_interfaces and
                self.service_virtualization_type == other.service_virtualization_type and
                self.availability_zone_enable == other.availability_zone_enable and
                self.vrouter_instance_type == other.vrouter_instance_type and
                self.instance_data == other.instance_data)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_service_mode (obj.populate_string ("service_mode"))
        obj.set_service_type (obj.populate_string ("service_type"))
        obj.set_image_name (obj.populate_string ("image_name"))
        obj.set_service_scaling (obj.populate_boolean ("service_scaling"))
        obj.set_interface_type ([ServiceTemplateInterfaceType.populate ()])
        obj.set_flavor (obj.populate_string ("flavor"))
        obj.set_ordered_interfaces (obj.populate_boolean ("ordered_interfaces"))
        obj.set_service_virtualization_type (obj.populate_string ("service_virtualization_type"))
        obj.set_availability_zone_enable (obj.populate_boolean ("availability_zone_enable"))
        obj.set_vrouter_instance_type (obj.populate_string ("vrouter_instance_type"))
        obj.set_instance_data (obj.populate_string ("instance_data"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ServiceTemplateType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ServiceTemplateType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ServiceTemplateType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ServiceTemplateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.service_mode is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-mode>%s</%sservice-mode>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_mode).encode(ExternalEncoding), input_name='service-mode'), namespace_, eol_))
        if self.service_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-type>%s</%sservice-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_type).encode(ExternalEncoding), input_name='service-type'), namespace_, eol_))
        if self.image_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%simage-name>%s</%simage-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.image_name).encode(ExternalEncoding), input_name='image-name'), namespace_, eol_))
        if self.service_scaling is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-scaling>%s</%sservice-scaling>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.service_scaling)), input_name='service-scaling'), namespace_, eol_))
        for interface_type_ in self.interface_type:
            if isinstance(interface_type_, dict):
                interface_type_ = ServiceTemplateInterfaceType(**interface_type_)
            interface_type_.export(outfile, level, namespace_, name_='interface-type', pretty_print=pretty_print)
        if self.flavor is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sflavor>%s</%sflavor>%s' % (namespace_, self.gds_format_string(quote_xml(self.flavor).encode(ExternalEncoding), input_name='flavor'), namespace_, eol_))
        if self.ordered_interfaces is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sordered-interfaces>%s</%sordered-interfaces>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.ordered_interfaces)), input_name='ordered-interfaces'), namespace_, eol_))
        if self.service_virtualization_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-virtualization-type>%s</%sservice-virtualization-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_virtualization_type).encode(ExternalEncoding), input_name='service-virtualization-type'), namespace_, eol_))
        if self.availability_zone_enable is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%savailability-zone-enable>%s</%savailability-zone-enable>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.availability_zone_enable)), input_name='availability-zone-enable'), namespace_, eol_))
        if self.vrouter_instance_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svrouter-instance-type>%s</%svrouter-instance-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.vrouter_instance_type).encode(ExternalEncoding), input_name='vrouter-instance-type'), namespace_, eol_))
        if self.instance_data is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinstance-data>%s</%sinstance-data>%s' % (namespace_, self.gds_format_string(quote_xml(self.instance_data).encode(ExternalEncoding), input_name='instance-data'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.service_mode is not None or
            self.service_type is not None or
            self.image_name is not None or
            self.service_scaling is not None or
            self.interface_type or
            self.flavor is not None or
            self.ordered_interfaces is not None or
            self.service_virtualization_type is not None or
            self.availability_zone_enable is not None or
            self.vrouter_instance_type is not None or
            self.instance_data is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ServiceTemplateType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.service_mode is not None:
            showIndent(outfile, level)
            outfile.write('service_mode=%s,\n' % quote_python(self.service_mode).encode(ExternalEncoding))
        if self.service_type is not None:
            showIndent(outfile, level)
            outfile.write('service_type=%s,\n' % quote_python(self.service_type).encode(ExternalEncoding))
        if self.image_name is not None:
            showIndent(outfile, level)
            outfile.write('image_name=%s,\n' % quote_python(self.image_name).encode(ExternalEncoding))
        if self.service_scaling is not None:
            showIndent(outfile, level)
            outfile.write('service_scaling=%s,\n' % self.service_scaling)
        showIndent(outfile, level)
        outfile.write('interface_type=[\n')
        level += 1
        for interface_type_ in self.interface_type:
            showIndent(outfile, level)
            outfile.write('model_.ServiceTemplateInterfaceType(\n')
            interface_type_.exportLiteral(outfile, level, name_='ServiceTemplateInterfaceType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.flavor is not None:
            showIndent(outfile, level)
            outfile.write('flavor=%s,\n' % quote_python(self.flavor).encode(ExternalEncoding))
        if self.ordered_interfaces is not None:
            showIndent(outfile, level)
            outfile.write('ordered_interfaces=%s,\n' % self.ordered_interfaces)
        if self.service_virtualization_type is not None:
            showIndent(outfile, level)
            outfile.write('service_virtualization_type=%s,\n' % quote_python(self.service_virtualization_type).encode(ExternalEncoding))
        if self.availability_zone_enable is not None:
            showIndent(outfile, level)
            outfile.write('availability_zone_enable=%s,\n' % self.availability_zone_enable)
        if self.vrouter_instance_type is not None:
            showIndent(outfile, level)
            outfile.write('vrouter_instance_type=%s,\n' % quote_python(self.vrouter_instance_type).encode(ExternalEncoding))
        if self.instance_data is not None:
            showIndent(outfile, level)
            outfile.write('instance_data=%s,\n' % quote_python(self.instance_data).encode(ExternalEncoding))
    def exportDict(self, name_='ServiceTemplateType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'service-mode':
            service_mode_ = child_.text
            service_mode_ = self.gds_validate_string(service_mode_, node, 'service_mode')
            self.service_mode = service_mode_
            self.validate_ServiceModeType(self.service_mode)    # validate type ServiceModeType
        elif nodeName_ == 'service-type':
            service_type_ = child_.text
            service_type_ = self.gds_validate_string(service_type_, node, 'service_type')
            self.service_type = service_type_
            self.validate_ServiceType(self.service_type)    # validate type ServiceType
        elif nodeName_ == 'image-name':
            image_name_ = child_.text
            image_name_ = self.gds_validate_string(image_name_, node, 'image_name')
            self.image_name = image_name_
        elif nodeName_ == 'service-scaling':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'service_scaling')
            self.service_scaling = ival_
        elif nodeName_ == 'interface-type':
            obj_ = ServiceTemplateInterfaceType.factory()
            obj_.build(child_)
            self.interface_type.append(obj_)
        elif nodeName_ == 'flavor':
            flavor_ = child_.text
            flavor_ = self.gds_validate_string(flavor_, node, 'flavor')
            self.flavor = flavor_
        elif nodeName_ == 'ordered-interfaces':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'ordered_interfaces')
            self.ordered_interfaces = ival_
        elif nodeName_ == 'service-virtualization-type':
            service_virtualization_type_ = child_.text
            service_virtualization_type_ = self.gds_validate_string(service_virtualization_type_, node, 'service_virtualization_type')
            self.service_virtualization_type = service_virtualization_type_
            self.validate_ServiceVirtualizationType(self.service_virtualization_type)    # validate type ServiceVirtualizationType
        elif nodeName_ == 'availability-zone-enable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'availability_zone_enable')
            self.availability_zone_enable = ival_
        elif nodeName_ == 'vrouter-instance-type':
            vrouter_instance_type_ = child_.text
            vrouter_instance_type_ = self.gds_validate_string(vrouter_instance_type_, node, 'vrouter_instance_type')
            self.vrouter_instance_type = vrouter_instance_type_
            self.validate_VRouterInstanceType(self.vrouter_instance_type)    # validate type VRouterInstanceType
        elif nodeName_ == 'instance-data':
            instance_data_ = child_.text
            instance_data_ = self.gds_validate_string(instance_data_, node, 'instance_data')
            self.instance_data = instance_data_
# end class ServiceTemplateType


class ServiceInstanceType(GeneratedsSuper):
    """
    ServiceInstanceType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, auto_policy=False, availability_zone=None, management_virtual_network=None, left_virtual_network=None, left_ip_address=None, right_virtual_network=None, right_ip_address=None, interface_list=None, scale_out=None, ha_mode=None, virtual_router_id=None, **kwargs):
        self.auto_policy = auto_policy
        self.availability_zone = availability_zone
        self.management_virtual_network = management_virtual_network
        self.left_virtual_network = left_virtual_network
        self.left_ip_address = left_ip_address
        self.right_virtual_network = right_virtual_network
        self.right_ip_address = right_ip_address
        if (interface_list is None) or (interface_list == []):
            self.interface_list = []
        else:
            if isinstance(interface_list[0], dict):
                objs = [ServiceInstanceInterfaceType(**elem) for elem in interface_list]
                self.interface_list = objs
            else:
                self.interface_list = interface_list
        if isinstance(scale_out, dict):
            obj = ServiceScaleOutType(**scale_out)
            self.scale_out = obj
        else:
            self.scale_out = scale_out
        self.ha_mode = ha_mode
        self.virtual_router_id = virtual_router_id
    def factory(*args_, **kwargs_):
        if ServiceInstanceType.subclass:
            return ServiceInstanceType.subclass(*args_, **kwargs_)
        else:
            return ServiceInstanceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_auto_policy(self): return self.auto_policy
    def set_auto_policy(self, auto_policy): self.auto_policy = auto_policy
    def get_availability_zone(self): return self.availability_zone
    def set_availability_zone(self, availability_zone): self.availability_zone = availability_zone
    def get_management_virtual_network(self): return self.management_virtual_network
    def set_management_virtual_network(self, management_virtual_network): self.management_virtual_network = management_virtual_network
    def get_left_virtual_network(self): return self.left_virtual_network
    def set_left_virtual_network(self, left_virtual_network): self.left_virtual_network = left_virtual_network
    def get_left_ip_address(self): return self.left_ip_address
    def set_left_ip_address(self, left_ip_address): self.left_ip_address = left_ip_address
    def validate_IpAddressType(self, value):
        # Validate type IpAddressType, a restriction on xsd:string.
        pass
    def get_right_virtual_network(self): return self.right_virtual_network
    def set_right_virtual_network(self, right_virtual_network): self.right_virtual_network = right_virtual_network
    def get_right_ip_address(self): return self.right_ip_address
    def set_right_ip_address(self, right_ip_address): self.right_ip_address = right_ip_address
    def get_interface_list(self): return self.interface_list
    def set_interface_list(self, interface_list): self.interface_list = interface_list
    def add_interface_list(self, value): self.interface_list.append(value)
    def insert_interface_list(self, index, value): self.interface_list[index] = value
    def delete_interface_list(self, value): self.interface_list.remove(value)
    def get_scale_out(self): return self.scale_out
    def set_scale_out(self, scale_out): self.scale_out = scale_out
    def get_ha_mode(self): return self.ha_mode
    def set_ha_mode(self, ha_mode): self.ha_mode = ha_mode
    def validate_AddressMode(self, value):
        # Validate type AddressMode, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'active-active', u'active-standby'])
        else:
            error = value not in [u'active-active', u'active-standby']
        if error:
            raise ValueError("AddressMode must be one of [u'active-active', u'active-standby']")
    def get_virtual_router_id(self): return self.virtual_router_id
    def set_virtual_router_id(self, virtual_router_id): self.virtual_router_id = virtual_router_id
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.auto_policy == other.auto_policy and
                self.availability_zone == other.availability_zone and
                self.management_virtual_network == other.management_virtual_network and
                self.left_virtual_network == other.left_virtual_network and
                self.left_ip_address == other.left_ip_address and
                self.right_virtual_network == other.right_virtual_network and
                self.right_ip_address == other.right_ip_address and
                self.interface_list == other.interface_list and
                self.scale_out == other.scale_out and
                self.ha_mode == other.ha_mode and
                self.virtual_router_id == other.virtual_router_id)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_auto_policy (obj.populate_boolean ("auto_policy"))
        obj.set_availability_zone (obj.populate_string ("availability_zone"))
        obj.set_management_virtual_network (obj.populate_string ("management_virtual_network"))
        obj.set_left_virtual_network (obj.populate_string ("left_virtual_network"))
        obj.set_left_ip_address (obj.populate_string ("left_ip_address"))
        obj.set_right_virtual_network (obj.populate_string ("right_virtual_network"))
        obj.set_right_ip_address (obj.populate_string ("right_ip_address"))
        obj.set_interface_list ([ServiceInstanceInterfaceType.populate ()])
        obj.set_scale_out (ServiceScaleOutType.populate ())
        obj.set_ha_mode (obj.populate_string ("ha_mode"))
        obj.set_virtual_router_id (obj.populate_string ("virtual_router_id"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ServiceInstanceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ServiceInstanceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ServiceInstanceType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ServiceInstanceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.auto_policy is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sauto-policy>%s</%sauto-policy>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.auto_policy)), input_name='auto-policy'), namespace_, eol_))
        if self.availability_zone is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%savailability-zone>%s</%savailability-zone>%s' % (namespace_, self.gds_format_string(quote_xml(self.availability_zone).encode(ExternalEncoding), input_name='availability-zone'), namespace_, eol_))
        if self.management_virtual_network is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smanagement-virtual-network>%s</%smanagement-virtual-network>%s' % (namespace_, self.gds_format_string(quote_xml(self.management_virtual_network).encode(ExternalEncoding), input_name='management-virtual-network'), namespace_, eol_))
        if self.left_virtual_network is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sleft-virtual-network>%s</%sleft-virtual-network>%s' % (namespace_, self.gds_format_string(quote_xml(self.left_virtual_network).encode(ExternalEncoding), input_name='left-virtual-network'), namespace_, eol_))
        if self.left_ip_address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sleft-ip-address>%s</%sleft-ip-address>%s' % (namespace_, self.gds_format_string(quote_xml(self.left_ip_address).encode(ExternalEncoding), input_name='left-ip-address'), namespace_, eol_))
        if self.right_virtual_network is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sright-virtual-network>%s</%sright-virtual-network>%s' % (namespace_, self.gds_format_string(quote_xml(self.right_virtual_network).encode(ExternalEncoding), input_name='right-virtual-network'), namespace_, eol_))
        if self.right_ip_address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sright-ip-address>%s</%sright-ip-address>%s' % (namespace_, self.gds_format_string(quote_xml(self.right_ip_address).encode(ExternalEncoding), input_name='right-ip-address'), namespace_, eol_))
        for interface_list_ in self.interface_list:
            if isinstance(interface_list_, dict):
                interface_list_ = ServiceInstanceInterfaceType(**interface_list_)
            interface_list_.export(outfile, level, namespace_, name_='interface-list', pretty_print=pretty_print)
        if self.scale_out is not None:
            self.scale_out.export(outfile, level, namespace_, name_='scale-out', pretty_print=pretty_print)
        if self.ha_mode is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sha-mode>%s</%sha-mode>%s' % (namespace_, self.gds_format_string(quote_xml(self.ha_mode).encode(ExternalEncoding), input_name='ha-mode'), namespace_, eol_))
        if self.virtual_router_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svirtual-router-id>%s</%svirtual-router-id>%s' % (namespace_, self.gds_format_string(quote_xml(self.virtual_router_id).encode(ExternalEncoding), input_name='virtual-router-id'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.auto_policy is not None or
            self.availability_zone is not None or
            self.management_virtual_network is not None or
            self.left_virtual_network is not None or
            self.left_ip_address is not None or
            self.right_virtual_network is not None or
            self.right_ip_address is not None or
            self.interface_list or
            self.scale_out is not None or
            self.ha_mode is not None or
            self.virtual_router_id is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ServiceInstanceType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.auto_policy is not None:
            showIndent(outfile, level)
            outfile.write('auto_policy=%s,\n' % self.auto_policy)
        if self.availability_zone is not None:
            showIndent(outfile, level)
            outfile.write('availability_zone=%s,\n' % quote_python(self.availability_zone).encode(ExternalEncoding))
        if self.management_virtual_network is not None:
            showIndent(outfile, level)
            outfile.write('management_virtual_network=%s,\n' % quote_python(self.management_virtual_network).encode(ExternalEncoding))
        if self.left_virtual_network is not None:
            showIndent(outfile, level)
            outfile.write('left_virtual_network=%s,\n' % quote_python(self.left_virtual_network).encode(ExternalEncoding))
        if self.left_ip_address is not None:
            showIndent(outfile, level)
            outfile.write('left_ip_address=%s,\n' % quote_python(self.left_ip_address).encode(ExternalEncoding))
        if self.right_virtual_network is not None:
            showIndent(outfile, level)
            outfile.write('right_virtual_network=%s,\n' % quote_python(self.right_virtual_network).encode(ExternalEncoding))
        if self.right_ip_address is not None:
            showIndent(outfile, level)
            outfile.write('right_ip_address=%s,\n' % quote_python(self.right_ip_address).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('interface_list=[\n')
        level += 1
        for interface_list_ in self.interface_list:
            showIndent(outfile, level)
            outfile.write('model_.ServiceInstanceInterfaceType(\n')
            interface_list_.exportLiteral(outfile, level, name_='ServiceInstanceInterfaceType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.scale_out is not None:
            showIndent(outfile, level)
            outfile.write('scale_out=model_.ServiceScaleOutType(\n')
            self.scale_out.exportLiteral(outfile, level, name_='scale_out')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ha_mode is not None:
            showIndent(outfile, level)
            outfile.write('ha_mode=%s,\n' % quote_python(self.ha_mode).encode(ExternalEncoding))
        if self.virtual_router_id is not None:
            showIndent(outfile, level)
            outfile.write('virtual_router_id=%s,\n' % quote_python(self.virtual_router_id).encode(ExternalEncoding))
    def exportDict(self, name_='ServiceInstanceType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'auto-policy':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'auto_policy')
            self.auto_policy = ival_
        elif nodeName_ == 'availability-zone':
            availability_zone_ = child_.text
            availability_zone_ = self.gds_validate_string(availability_zone_, node, 'availability_zone')
            self.availability_zone = availability_zone_
        elif nodeName_ == 'management-virtual-network':
            management_virtual_network_ = child_.text
            management_virtual_network_ = self.gds_validate_string(management_virtual_network_, node, 'management_virtual_network')
            self.management_virtual_network = management_virtual_network_
        elif nodeName_ == 'left-virtual-network':
            left_virtual_network_ = child_.text
            left_virtual_network_ = self.gds_validate_string(left_virtual_network_, node, 'left_virtual_network')
            self.left_virtual_network = left_virtual_network_
        elif nodeName_ == 'left-ip-address':
            left_ip_address_ = child_.text
            left_ip_address_ = self.gds_validate_string(left_ip_address_, node, 'left_ip_address')
            self.left_ip_address = left_ip_address_
            self.validate_IpAddressType(self.left_ip_address)    # validate type IpAddressType
        elif nodeName_ == 'right-virtual-network':
            right_virtual_network_ = child_.text
            right_virtual_network_ = self.gds_validate_string(right_virtual_network_, node, 'right_virtual_network')
            self.right_virtual_network = right_virtual_network_
        elif nodeName_ == 'right-ip-address':
            right_ip_address_ = child_.text
            right_ip_address_ = self.gds_validate_string(right_ip_address_, node, 'right_ip_address')
            self.right_ip_address = right_ip_address_
            self.validate_IpAddressType(self.right_ip_address)    # validate type IpAddressType
        elif nodeName_ == 'interface-list':
            obj_ = ServiceInstanceInterfaceType.factory()
            obj_.build(child_)
            self.interface_list.append(obj_)
        elif nodeName_ == 'scale-out':
            obj_ = ServiceScaleOutType.factory()
            obj_.build(child_)
            self.set_scale_out(obj_)
        elif nodeName_ == 'ha-mode':
            ha_mode_ = child_.text
            ha_mode_ = self.gds_validate_string(ha_mode_, node, 'ha_mode')
            self.ha_mode = ha_mode_
            self.validate_AddressMode(self.ha_mode)    # validate type AddressMode
        elif nodeName_ == 'virtual-router-id':
            virtual_router_id_ = child_.text
            virtual_router_id_ = self.gds_validate_string(virtual_router_id_, node, 'virtual_router_id')
            self.virtual_router_id = virtual_router_id_
# end class ServiceInstanceType


class project_service_instance(GeneratedsSuper):
    """
    project_service_instance class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_service_instance.subclass:
            return project_service_instance.subclass(*args_, **kwargs_)
        else:
            return project_service_instance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-service-instance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-service-instance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-service-instance'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-service-instance', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-service-instance'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-service-instance'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_service_instance


class domain_service_template(GeneratedsSuper):
    """
    domain_service_template class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if domain_service_template.subclass:
            return domain_service_template.subclass(*args_, **kwargs_)
        else:
            return domain_service_template(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='domain-service-template', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='domain-service-template')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='domain-service-template'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='domain-service-template', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='domain-service-template'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='domain-service-template'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class domain_service_template


class service_instance_service_template(GeneratedsSuper):
    """
    service_instance_service_template class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if service_instance_service_template.subclass:
            return service_instance_service_template.subclass(*args_, **kwargs_)
        else:
            return service_instance_service_template(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='service-instance-service-template', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='service-instance-service-template')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='service-instance-service-template'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='service-instance-service-template', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='service-instance-service-template'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='service-instance-service-template'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class service_instance_service_template


class virtual_machine_service_instance(GeneratedsSuper):
    """
    virtual_machine_service_instance class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_service_instance.subclass:
            return virtual_machine_service_instance.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_service_instance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-service-instance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-service-instance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-service-instance'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-service-instance', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-service-instance'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-service-instance'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_service_instance


class domain_virtual_DNS(GeneratedsSuper):
    """
    domain_virtual_DNS class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if domain_virtual_DNS.subclass:
            return domain_virtual_DNS.subclass(*args_, **kwargs_)
        else:
            return domain_virtual_DNS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='domain-virtual-DNS', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='domain-virtual-DNS')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='domain-virtual-DNS'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='domain-virtual-DNS', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='domain-virtual-DNS'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='domain-virtual-DNS'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class domain_virtual_DNS


class virtual_DNS_virtual_DNS_record(GeneratedsSuper):
    """
    virtual_DNS_virtual_DNS_record class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_DNS_virtual_DNS_record.subclass:
            return virtual_DNS_virtual_DNS_record.subclass(*args_, **kwargs_)
        else:
            return virtual_DNS_virtual_DNS_record(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-DNS-virtual-DNS-record', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-DNS-virtual-DNS-record')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-DNS-virtual-DNS-record'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-DNS-virtual-DNS-record', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-DNS-virtual-DNS-record'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-DNS-virtual-DNS-record'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_DNS_virtual_DNS_record


class network_ipam_virtual_DNS(GeneratedsSuper):
    """
    network_ipam_virtual_DNS class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if network_ipam_virtual_DNS.subclass:
            return network_ipam_virtual_DNS.subclass(*args_, **kwargs_)
        else:
            return network_ipam_virtual_DNS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='network-ipam-virtual-DNS', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='network-ipam-virtual-DNS')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='network-ipam-virtual-DNS'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='network-ipam-virtual-DNS', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='network-ipam-virtual-DNS'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='network-ipam-virtual-DNS'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class network_ipam_virtual_DNS


class RouteType(GeneratedsSuper):
    """
    RouteType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, prefix=None, next_hop=None, next_hop_type=None, **kwargs):
        self.prefix = prefix
        self.next_hop = next_hop
        self.next_hop_type = next_hop_type
    def factory(*args_, **kwargs_):
        if RouteType.subclass:
            return RouteType.subclass(*args_, **kwargs_)
        else:
            return RouteType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_prefix(self): return self.prefix
    def set_prefix(self, prefix): self.prefix = prefix
    def get_next_hop(self): return self.next_hop
    def set_next_hop(self, next_hop): self.next_hop = next_hop
    def get_next_hop_type(self): return self.next_hop_type
    def set_next_hop_type(self, next_hop_type): self.next_hop_type = next_hop_type
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.prefix == other.prefix and
                self.next_hop == other.next_hop and
                self.next_hop_type == other.next_hop_type)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_prefix (obj.populate_string ("prefix"))
        obj.set_next_hop (obj.populate_string ("next_hop"))
        obj.set_next_hop_type (obj.populate_string ("next_hop_type"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='RouteType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RouteType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RouteType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='RouteType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.prefix is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprefix>%s</%sprefix>%s' % (namespace_, self.gds_format_string(quote_xml(self.prefix).encode(ExternalEncoding), input_name='prefix'), namespace_, eol_))
        if self.next_hop is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snext-hop>%s</%snext-hop>%s' % (namespace_, self.gds_format_string(quote_xml(self.next_hop).encode(ExternalEncoding), input_name='next-hop'), namespace_, eol_))
        if self.next_hop_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snext-hop-type>%s</%snext-hop-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.next_hop_type).encode(ExternalEncoding), input_name='next-hop-type'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.prefix is not None or
            self.next_hop is not None or
            self.next_hop_type is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='RouteType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.prefix is not None:
            showIndent(outfile, level)
            outfile.write('prefix=%s,\n' % quote_python(self.prefix).encode(ExternalEncoding))
        if self.next_hop is not None:
            showIndent(outfile, level)
            outfile.write('next_hop=%s,\n' % quote_python(self.next_hop).encode(ExternalEncoding))
        if self.next_hop_type is not None:
            showIndent(outfile, level)
            outfile.write('next_hop_type=%s,\n' % quote_python(self.next_hop_type).encode(ExternalEncoding))
    def exportDict(self, name_='RouteType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'prefix':
            prefix_ = child_.text
            prefix_ = self.gds_validate_string(prefix_, node, 'prefix')
            self.prefix = prefix_
        elif nodeName_ == 'next-hop':
            next_hop_ = child_.text
            next_hop_ = self.gds_validate_string(next_hop_, node, 'next_hop')
            self.next_hop = next_hop_
        elif nodeName_ == 'next-hop-type':
            next_hop_type_ = child_.text
            next_hop_type_ = self.gds_validate_string(next_hop_type_, node, 'next_hop_type')
            self.next_hop_type = next_hop_type_
# end class RouteType


class RouteTableType(GeneratedsSuper):
    """
    RouteTableType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, route=None, **kwargs):
        if (route is None) or (route == []):
            self.route = []
        else:
            if isinstance(route[0], dict):
                objs = [RouteType(**elem) for elem in route]
                self.route = objs
            else:
                self.route = route
    def factory(*args_, **kwargs_):
        if RouteTableType.subclass:
            return RouteTableType.subclass(*args_, **kwargs_)
        else:
            return RouteTableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_route(self): return self.route
    def set_route(self, route): self.route = route
    def add_route(self, value): self.route.append(value)
    def insert_route(self, index, value): self.route[index] = value
    def delete_route(self, value): self.route.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.route == other.route)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_route ([RouteType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='RouteTableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RouteTableType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='RouteTableType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='RouteTableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for route_ in self.route:
            if isinstance(route_, dict):
                route_ = RouteType(**route_)
            route_.export(outfile, level, namespace_, name_='route', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.route
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='RouteTableType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('route=[\n')
        level += 1
        for route_ in self.route:
            showIndent(outfile, level)
            outfile.write('model_.RouteType(\n')
            route_.exportLiteral(outfile, level, name_='RouteType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='RouteTableType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'route':
            obj_ = RouteType.factory()
            obj_.build(child_)
            self.route.append(obj_)
# end class RouteTableType


class project_route_table(GeneratedsSuper):
    """
    project_route_table class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_route_table.subclass:
            return project_route_table.subclass(*args_, **kwargs_)
        else:
            return project_route_table(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-route-table', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-route-table')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-route-table'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-route-table', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-route-table'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-route-table'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_route_table


class virtual_network_route_table(GeneratedsSuper):
    """
    virtual_network_route_table class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_network_route_table.subclass:
            return virtual_network_route_table.subclass(*args_, **kwargs_)
        else:
            return virtual_network_route_table(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-network-route-table', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-network-route-table')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-network-route-table'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-network-route-table', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-network-route-table'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-network-route-table'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_network_route_table


class project_interface_route_table(GeneratedsSuper):
    """
    project_interface_route_table class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_interface_route_table.subclass:
            return project_interface_route_table.subclass(*args_, **kwargs_)
        else:
            return project_interface_route_table(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-interface-route-table', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-interface-route-table')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-interface-route-table'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-interface-route-table', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-interface-route-table'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-interface-route-table'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_interface_route_table


class virtual_machine_interface_route_table(GeneratedsSuper):
    """
    virtual_machine_interface_route_table class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_machine_interface_route_table.subclass:
            return virtual_machine_interface_route_table.subclass(*args_, **kwargs_)
        else:
            return virtual_machine_interface_route_table(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-machine-interface-route-table', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-machine-interface-route-table')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-machine-interface-route-table'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-machine-interface-route-table', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-machine-interface-route-table'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-machine-interface-route-table'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_machine_interface_route_table


class project_logical_router(GeneratedsSuper):
    """
    project_logical_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_logical_router.subclass:
            return project_logical_router.subclass(*args_, **kwargs_)
        else:
            return project_logical_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-logical-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-logical-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-logical-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-logical-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-logical-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-logical-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_logical_router


class logical_router_interface(GeneratedsSuper):
    """
    logical_router_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if logical_router_interface.subclass:
            return logical_router_interface.subclass(*args_, **kwargs_)
        else:
            return logical_router_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='logical-router-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='logical-router-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='logical-router-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='logical-router-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='logical-router-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='logical-router-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class logical_router_interface


class logical_router_target(GeneratedsSuper):
    """
    logical_router_target class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if logical_router_target.subclass:
            return logical_router_target.subclass(*args_, **kwargs_)
        else:
            return logical_router_target(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='logical-router-target', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='logical-router-target')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='logical-router-target'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='logical-router-target', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='logical-router-target'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='logical-router-target'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class logical_router_target


class logical_router_gateway(GeneratedsSuper):
    """
    logical_router_gateway class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if logical_router_gateway.subclass:
            return logical_router_gateway.subclass(*args_, **kwargs_)
        else:
            return logical_router_gateway(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='logical-router-gateway', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='logical-router-gateway')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='logical-router-gateway'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='logical-router-gateway', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='logical-router-gateway'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='logical-router-gateway'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class logical_router_gateway


class logical_router_service_instance(GeneratedsSuper):
    """
    logical_router_service_instance class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if logical_router_service_instance.subclass:
            return logical_router_service_instance.subclass(*args_, **kwargs_)
        else:
            return logical_router_service_instance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='logical-router-service-instance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='logical-router-service-instance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='logical-router-service-instance'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='logical-router-service-instance', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='logical-router-service-instance'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='logical-router-service-instance'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class logical_router_service_instance


class global_system_config_config_node(GeneratedsSuper):
    """
    global_system_config_config_node class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_config_node.subclass:
            return global_system_config_config_node.subclass(*args_, **kwargs_)
        else:
            return global_system_config_config_node(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-config-node', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-config-node')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-config-node'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-config-node', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-config-node'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-config-node'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_config_node


class global_system_config_analytics_node(GeneratedsSuper):
    """
    global_system_config_analytics_node class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_analytics_node.subclass:
            return global_system_config_analytics_node.subclass(*args_, **kwargs_)
        else:
            return global_system_config_analytics_node(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-analytics-node', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-analytics-node')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-analytics-node'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-analytics-node', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-analytics-node'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-analytics-node'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_analytics_node


class global_system_config_database_node(GeneratedsSuper):
    """
    global_system_config_database_node class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_database_node.subclass:
            return global_system_config_database_node.subclass(*args_, **kwargs_)
        else:
            return global_system_config_database_node(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-database-node', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-database-node')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-database-node'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-database-node', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-database-node'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-database-node'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_database_node


class KeyValuePair(GeneratedsSuper):
    """
    KeyValuePair class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, key=None, value=None, **kwargs):
        self.key = key
        self.value = value
    def factory(*args_, **kwargs_):
        if KeyValuePair.subclass:
            return KeyValuePair.subclass(*args_, **kwargs_)
        else:
            return KeyValuePair(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_key(self): return self.key
    def set_key(self, key): self.key = key
    def get_value(self): return self.value
    def set_value(self, value): self.value = value
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.key == other.key and
                self.value == other.value)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_key (obj.populate_string ("key"))
        obj.set_value (obj.populate_string ("value"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='KeyValuePair', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='KeyValuePair')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='KeyValuePair'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='KeyValuePair', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.key is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%skey>%s</%skey>%s' % (namespace_, self.gds_format_string(quote_xml(self.key).encode(ExternalEncoding), input_name='key'), namespace_, eol_))
        if self.value is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespace_, self.gds_format_string(quote_xml(self.value).encode(ExternalEncoding), input_name='value'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.key is not None or
            self.value is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='KeyValuePair'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.key is not None:
            showIndent(outfile, level)
            outfile.write('key=%s,\n' % quote_python(self.key).encode(ExternalEncoding))
        if self.value is not None:
            showIndent(outfile, level)
            outfile.write('value=%s,\n' % quote_python(self.value).encode(ExternalEncoding))
    def exportDict(self, name_='KeyValuePair'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'key':
            key_ = child_.text
            key_ = self.gds_validate_string(key_, node, 'key')
            self.key = key_
        elif nodeName_ == 'value':
            value_ = child_.text
            value_ = self.gds_validate_string(value_, node, 'value')
            self.value = value_
# end class KeyValuePair


class KeyValuePairs(GeneratedsSuper):
    """
    KeyValuePairs class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, key_value_pair=None, **kwargs):
        if (key_value_pair is None) or (key_value_pair == []):
            self.key_value_pair = []
        else:
            if isinstance(key_value_pair[0], dict):
                objs = [KeyValuePair(**elem) for elem in key_value_pair]
                self.key_value_pair = objs
            else:
                self.key_value_pair = key_value_pair
    def factory(*args_, **kwargs_):
        if KeyValuePairs.subclass:
            return KeyValuePairs.subclass(*args_, **kwargs_)
        else:
            return KeyValuePairs(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_key_value_pair(self): return self.key_value_pair
    def set_key_value_pair(self, key_value_pair): self.key_value_pair = key_value_pair
    def add_key_value_pair(self, value): self.key_value_pair.append(value)
    def insert_key_value_pair(self, index, value): self.key_value_pair[index] = value
    def delete_key_value_pair(self, value): self.key_value_pair.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.key_value_pair == other.key_value_pair)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_key_value_pair ([KeyValuePair.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='KeyValuePairs', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='KeyValuePairs')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='KeyValuePairs'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='KeyValuePairs', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for key_value_pair_ in self.key_value_pair:
            if isinstance(key_value_pair_, dict):
                key_value_pair_ = KeyValuePair(**key_value_pair_)
            key_value_pair_.export(outfile, level, namespace_, name_='key-value-pair', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.key_value_pair
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='KeyValuePairs'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('key_value_pair=[\n')
        level += 1
        for key_value_pair_ in self.key_value_pair:
            showIndent(outfile, level)
            outfile.write('model_.KeyValuePair(\n')
            key_value_pair_.exportLiteral(outfile, level, name_='KeyValuePair')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='KeyValuePairs'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'key-value-pair':
            obj_ = KeyValuePair.factory()
            obj_.build(child_)
            self.key_value_pair.append(obj_)
# end class KeyValuePairs


class global_system_config_service_appliance_set(GeneratedsSuper):
    """
    global_system_config_service_appliance_set class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if global_system_config_service_appliance_set.subclass:
            return global_system_config_service_appliance_set.subclass(*args_, **kwargs_)
        else:
            return global_system_config_service_appliance_set(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='global-system-config-service-appliance-set', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='global-system-config-service-appliance-set')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='global-system-config-service-appliance-set'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='global-system-config-service-appliance-set', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='global-system-config-service-appliance-set'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='global-system-config-service-appliance-set'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class global_system_config_service_appliance_set


class service_appliance_set_service_appliance(GeneratedsSuper):
    """
    service_appliance_set_service_appliance class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if service_appliance_set_service_appliance.subclass:
            return service_appliance_set_service_appliance.subclass(*args_, **kwargs_)
        else:
            return service_appliance_set_service_appliance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='service-appliance-set-service-appliance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='service-appliance-set-service-appliance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='service-appliance-set-service-appliance'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='service-appliance-set-service-appliance', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='service-appliance-set-service-appliance'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='service-appliance-set-service-appliance'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class service_appliance_set_service_appliance


class project_loadbalancer_pool(GeneratedsSuper):
    """
    project_loadbalancer_pool class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_loadbalancer_pool.subclass:
            return project_loadbalancer_pool.subclass(*args_, **kwargs_)
        else:
            return project_loadbalancer_pool(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-loadbalancer-pool', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-loadbalancer-pool')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-loadbalancer-pool'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-loadbalancer-pool', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-loadbalancer-pool'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-loadbalancer-pool'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_loadbalancer_pool


class loadbalancer_pool_service_instance(GeneratedsSuper):
    """
    loadbalancer_pool_service_instance class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if loadbalancer_pool_service_instance.subclass:
            return loadbalancer_pool_service_instance.subclass(*args_, **kwargs_)
        else:
            return loadbalancer_pool_service_instance(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='loadbalancer-pool-service-instance', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='loadbalancer-pool-service-instance')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='loadbalancer-pool-service-instance'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='loadbalancer-pool-service-instance', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='loadbalancer-pool-service-instance'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='loadbalancer-pool-service-instance'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class loadbalancer_pool_service_instance


class loadbalancer_pool_virtual_machine_interface(GeneratedsSuper):
    """
    loadbalancer_pool_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if loadbalancer_pool_virtual_machine_interface.subclass:
            return loadbalancer_pool_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return loadbalancer_pool_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='loadbalancer-pool-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='loadbalancer-pool-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='loadbalancer-pool-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='loadbalancer-pool-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='loadbalancer-pool-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='loadbalancer-pool-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class loadbalancer_pool_virtual_machine_interface


class LoadbalancerPoolType(GeneratedsSuper):
    """
    LoadbalancerPoolType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, status=None, status_description=None, admin_state=True, protocol=None, loadbalancer_method=None, subnet_id=None, **kwargs):
        self.status = status
        self.status_description = status_description
        self.admin_state = admin_state
        self.protocol = protocol
        self.loadbalancer_method = loadbalancer_method
        self.subnet_id = subnet_id
    def factory(*args_, **kwargs_):
        if LoadbalancerPoolType.subclass:
            return LoadbalancerPoolType.subclass(*args_, **kwargs_)
        else:
            return LoadbalancerPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_status_description(self): return self.status_description
    def set_status_description(self, status_description): self.status_description = status_description
    def get_admin_state(self): return self.admin_state
    def set_admin_state(self, admin_state): self.admin_state = admin_state
    def get_protocol(self): return self.protocol
    def set_protocol(self, protocol): self.protocol = protocol
    def validate_LoadbalancerProtocolType(self, value):
        # Validate type LoadbalancerProtocolType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'HTTP', u'HTTPS', u'TCP'])
        else:
            error = value not in [u'HTTP', u'HTTPS', u'TCP']
        if error:
            raise ValueError("LoadbalancerProtocolType must be one of [u'HTTP', u'HTTPS', u'TCP']")
    def get_loadbalancer_method(self): return self.loadbalancer_method
    def set_loadbalancer_method(self, loadbalancer_method): self.loadbalancer_method = loadbalancer_method
    def validate_LoadbalancerMethodType(self, value):
        # Validate type LoadbalancerMethodType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'ROUND_ROBIN', u'LEAST_CONNECTIONS', u'SOURCE_IP'])
        else:
            error = value not in [u'ROUND_ROBIN', u'LEAST_CONNECTIONS', u'SOURCE_IP']
        if error:
            raise ValueError("LoadbalancerMethodType must be one of [u'ROUND_ROBIN', u'LEAST_CONNECTIONS', u'SOURCE_IP']")
    def get_subnet_id(self): return self.subnet_id
    def set_subnet_id(self, subnet_id): self.subnet_id = subnet_id
    def validate_UuidStringType(self, value):
        # Validate type UuidStringType, a restriction on xsd:string.
        pass
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.status == other.status and
                self.status_description == other.status_description and
                self.admin_state == other.admin_state and
                self.protocol == other.protocol and
                self.loadbalancer_method == other.loadbalancer_method and
                self.subnet_id == other.subnet_id)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_status (obj.populate_string ("status"))
        obj.set_status_description (obj.populate_string ("status_description"))
        obj.set_admin_state (obj.populate_boolean ("admin_state"))
        obj.set_protocol (obj.populate_string ("protocol"))
        obj.set_loadbalancer_method (obj.populate_string ("loadbalancer_method"))
        obj.set_subnet_id (obj.populate_string ("subnet_id"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='LoadbalancerPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LoadbalancerPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LoadbalancerPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='LoadbalancerPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.status is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespace_, self.gds_format_string(quote_xml(self.status).encode(ExternalEncoding), input_name='status'), namespace_, eol_))
        if self.status_description is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus-description>%s</%sstatus-description>%s' % (namespace_, self.gds_format_string(quote_xml(self.status_description).encode(ExternalEncoding), input_name='status-description'), namespace_, eol_))
        if self.admin_state is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadmin-state>%s</%sadmin-state>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.admin_state)), input_name='admin-state'), namespace_, eol_))
        if self.protocol is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprotocol>%s</%sprotocol>%s' % (namespace_, self.gds_format_string(quote_xml(self.protocol).encode(ExternalEncoding), input_name='protocol'), namespace_, eol_))
        if self.loadbalancer_method is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sloadbalancer-method>%s</%sloadbalancer-method>%s' % (namespace_, self.gds_format_string(quote_xml(self.loadbalancer_method).encode(ExternalEncoding), input_name='loadbalancer-method'), namespace_, eol_))
        if self.subnet_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssubnet-id>%s</%ssubnet-id>%s' % (namespace_, self.gds_format_string(quote_xml(self.subnet_id).encode(ExternalEncoding), input_name='subnet-id'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.status is not None or
            self.status_description is not None or
            self.admin_state is not None or
            self.protocol is not None or
            self.loadbalancer_method is not None or
            self.subnet_id is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LoadbalancerPoolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.status is not None:
            showIndent(outfile, level)
            outfile.write('status=%s,\n' % quote_python(self.status).encode(ExternalEncoding))
        if self.status_description is not None:
            showIndent(outfile, level)
            outfile.write('status_description=%s,\n' % quote_python(self.status_description).encode(ExternalEncoding))
        if self.admin_state is not None:
            showIndent(outfile, level)
            outfile.write('admin_state=%s,\n' % self.admin_state)
        if self.protocol is not None:
            showIndent(outfile, level)
            outfile.write('protocol=%s,\n' % quote_python(self.protocol).encode(ExternalEncoding))
        if self.loadbalancer_method is not None:
            showIndent(outfile, level)
            outfile.write('loadbalancer_method=%s,\n' % quote_python(self.loadbalancer_method).encode(ExternalEncoding))
        if self.subnet_id is not None:
            showIndent(outfile, level)
            outfile.write('subnet_id=%s,\n' % quote_python(self.subnet_id).encode(ExternalEncoding))
    def exportDict(self, name_='LoadbalancerPoolType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'status':
            status_ = child_.text
            status_ = self.gds_validate_string(status_, node, 'status')
            self.status = status_
        elif nodeName_ == 'status-description':
            status_description_ = child_.text
            status_description_ = self.gds_validate_string(status_description_, node, 'status_description')
            self.status_description = status_description_
        elif nodeName_ == 'admin-state':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'admin_state')
            self.admin_state = ival_
        elif nodeName_ == 'protocol':
            protocol_ = child_.text
            protocol_ = self.gds_validate_string(protocol_, node, 'protocol')
            self.protocol = protocol_
            self.validate_LoadbalancerProtocolType(self.protocol)    # validate type LoadbalancerProtocolType
        elif nodeName_ == 'loadbalancer-method':
            loadbalancer_method_ = child_.text
            loadbalancer_method_ = self.gds_validate_string(loadbalancer_method_, node, 'loadbalancer_method')
            self.loadbalancer_method = loadbalancer_method_
            self.validate_LoadbalancerMethodType(self.loadbalancer_method)    # validate type LoadbalancerMethodType
        elif nodeName_ == 'subnet-id':
            subnet_id_ = child_.text
            subnet_id_ = self.gds_validate_string(subnet_id_, node, 'subnet_id')
            self.subnet_id = subnet_id_
            self.validate_UuidStringType(self.subnet_id)    # validate type UuidStringType
# end class LoadbalancerPoolType


class loadbalancer_pool_service_appliance_set(GeneratedsSuper):
    """
    loadbalancer_pool_service_appliance_set class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if loadbalancer_pool_service_appliance_set.subclass:
            return loadbalancer_pool_service_appliance_set.subclass(*args_, **kwargs_)
        else:
            return loadbalancer_pool_service_appliance_set(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='loadbalancer-pool-service-appliance-set', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='loadbalancer-pool-service-appliance-set')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='loadbalancer-pool-service-appliance-set'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='loadbalancer-pool-service-appliance-set', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='loadbalancer-pool-service-appliance-set'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='loadbalancer-pool-service-appliance-set'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class loadbalancer_pool_service_appliance_set


class loadbalancer_pool_loadbalancer_member(GeneratedsSuper):
    """
    loadbalancer_pool_loadbalancer_member class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if loadbalancer_pool_loadbalancer_member.subclass:
            return loadbalancer_pool_loadbalancer_member.subclass(*args_, **kwargs_)
        else:
            return loadbalancer_pool_loadbalancer_member(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='loadbalancer-pool-loadbalancer-member', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='loadbalancer-pool-loadbalancer-member')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='loadbalancer-pool-loadbalancer-member'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='loadbalancer-pool-loadbalancer-member', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='loadbalancer-pool-loadbalancer-member'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='loadbalancer-pool-loadbalancer-member'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class loadbalancer_pool_loadbalancer_member


class LoadbalancerMemberType(GeneratedsSuper):
    """
    LoadbalancerMemberType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, admin_state=True, status=None, status_description=None, protocol_port=None, weight=None, address=None, **kwargs):
        self.admin_state = admin_state
        self.status = status
        self.status_description = status_description
        self.protocol_port = protocol_port
        self.weight = weight
        self.address = address
    def factory(*args_, **kwargs_):
        if LoadbalancerMemberType.subclass:
            return LoadbalancerMemberType.subclass(*args_, **kwargs_)
        else:
            return LoadbalancerMemberType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_admin_state(self): return self.admin_state
    def set_admin_state(self, admin_state): self.admin_state = admin_state
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_status_description(self): return self.status_description
    def set_status_description(self, status_description): self.status_description = status_description
    def get_protocol_port(self): return self.protocol_port
    def set_protocol_port(self, protocol_port): self.protocol_port = protocol_port
    def get_weight(self): return self.weight
    def set_weight(self, weight): self.weight = weight
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def validate_IpAddressType(self, value):
        # Validate type IpAddressType, a restriction on xsd:string.
        pass
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.admin_state == other.admin_state and
                self.status == other.status and
                self.status_description == other.status_description and
                self.protocol_port == other.protocol_port and
                self.weight == other.weight and
                self.address == other.address)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_admin_state (obj.populate_boolean ("admin_state"))
        obj.set_status (obj.populate_string ("status"))
        obj.set_status_description (obj.populate_string ("status_description"))
        obj.set_protocol_port (obj.populate_integer ("protocol_port"))
        obj.set_weight (obj.populate_integer ("weight"))
        obj.set_address (obj.populate_string ("address"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='LoadbalancerMemberType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LoadbalancerMemberType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LoadbalancerMemberType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='LoadbalancerMemberType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.admin_state is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadmin-state>%s</%sadmin-state>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.admin_state)), input_name='admin-state'), namespace_, eol_))
        if self.status is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespace_, self.gds_format_string(quote_xml(self.status).encode(ExternalEncoding), input_name='status'), namespace_, eol_))
        if self.status_description is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus-description>%s</%sstatus-description>%s' % (namespace_, self.gds_format_string(quote_xml(self.status_description).encode(ExternalEncoding), input_name='status-description'), namespace_, eol_))
        if self.protocol_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprotocol-port>%s</%sprotocol-port>%s' % (namespace_, self.gds_format_integer(self.protocol_port, input_name='protocol-port'), namespace_, eol_))
        if self.weight is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sweight>%s</%sweight>%s' % (namespace_, self.gds_format_integer(self.weight, input_name='weight'), namespace_, eol_))
        if self.address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress>%s</%saddress>%s' % (namespace_, self.gds_format_string(quote_xml(self.address).encode(ExternalEncoding), input_name='address'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.admin_state is not None or
            self.status is not None or
            self.status_description is not None or
            self.protocol_port is not None or
            self.weight is not None or
            self.address is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LoadbalancerMemberType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.admin_state is not None:
            showIndent(outfile, level)
            outfile.write('admin_state=%s,\n' % self.admin_state)
        if self.status is not None:
            showIndent(outfile, level)
            outfile.write('status=%s,\n' % quote_python(self.status).encode(ExternalEncoding))
        if self.status_description is not None:
            showIndent(outfile, level)
            outfile.write('status_description=%s,\n' % quote_python(self.status_description).encode(ExternalEncoding))
        if self.protocol_port is not None:
            showIndent(outfile, level)
            outfile.write('protocol_port=%d,\n' % self.protocol_port)
        if self.weight is not None:
            showIndent(outfile, level)
            outfile.write('weight=%d,\n' % self.weight)
        if self.address is not None:
            showIndent(outfile, level)
            outfile.write('address=%s,\n' % quote_python(self.address).encode(ExternalEncoding))
    def exportDict(self, name_='LoadbalancerMemberType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'admin-state':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'admin_state')
            self.admin_state = ival_
        elif nodeName_ == 'status':
            status_ = child_.text
            status_ = self.gds_validate_string(status_, node, 'status')
            self.status = status_
        elif nodeName_ == 'status-description':
            status_description_ = child_.text
            status_description_ = self.gds_validate_string(status_description_, node, 'status_description')
            self.status_description = status_description_
        elif nodeName_ == 'protocol-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'protocol_port')
            self.protocol_port = ival_
        elif nodeName_ == 'weight':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'weight')
            self.weight = ival_
        elif nodeName_ == 'address':
            address_ = child_.text
            address_ = self.gds_validate_string(address_, node, 'address')
            self.address = address_
            self.validate_IpAddressType(self.address)    # validate type IpAddressType
# end class LoadbalancerMemberType


class project_loadbalancer_healthmonitor(GeneratedsSuper):
    """
    project_loadbalancer_healthmonitor class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_loadbalancer_healthmonitor.subclass:
            return project_loadbalancer_healthmonitor.subclass(*args_, **kwargs_)
        else:
            return project_loadbalancer_healthmonitor(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-loadbalancer-healthmonitor', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-loadbalancer-healthmonitor')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-loadbalancer-healthmonitor'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-loadbalancer-healthmonitor', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-loadbalancer-healthmonitor'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-loadbalancer-healthmonitor'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_loadbalancer_healthmonitor


class loadbalancer_pool_loadbalancer_healthmonitor(GeneratedsSuper):
    """
    loadbalancer_pool_loadbalancer_healthmonitor class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if loadbalancer_pool_loadbalancer_healthmonitor.subclass:
            return loadbalancer_pool_loadbalancer_healthmonitor.subclass(*args_, **kwargs_)
        else:
            return loadbalancer_pool_loadbalancer_healthmonitor(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='loadbalancer-pool-loadbalancer-healthmonitor', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='loadbalancer-pool-loadbalancer-healthmonitor')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='loadbalancer-pool-loadbalancer-healthmonitor'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='loadbalancer-pool-loadbalancer-healthmonitor', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='loadbalancer-pool-loadbalancer-healthmonitor'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='loadbalancer-pool-loadbalancer-healthmonitor'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class loadbalancer_pool_loadbalancer_healthmonitor


class LoadbalancerHealthmonitorType(GeneratedsSuper):
    """
    LoadbalancerHealthmonitorType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, admin_state=True, monitor_type=None, delay=None, timeout=None, max_retries=None, http_method=None, url_path=None, expected_codes=None, **kwargs):
        self.admin_state = admin_state
        self.monitor_type = monitor_type
        self.delay = delay
        self.timeout = timeout
        self.max_retries = max_retries
        self.http_method = http_method
        self.url_path = url_path
        self.expected_codes = expected_codes
    def factory(*args_, **kwargs_):
        if LoadbalancerHealthmonitorType.subclass:
            return LoadbalancerHealthmonitorType.subclass(*args_, **kwargs_)
        else:
            return LoadbalancerHealthmonitorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_admin_state(self): return self.admin_state
    def set_admin_state(self, admin_state): self.admin_state = admin_state
    def get_monitor_type(self): return self.monitor_type
    def set_monitor_type(self, monitor_type): self.monitor_type = monitor_type
    def validate_HealthmonitorType(self, value):
        # Validate type HealthmonitorType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'PING', u'TCP', u'HTTP', u'HTTPS'])
        else:
            error = value not in [u'PING', u'TCP', u'HTTP', u'HTTPS']
        if error:
            raise ValueError("HealthmonitorType must be one of [u'PING', u'TCP', u'HTTP', u'HTTPS']")
    def get_delay(self): return self.delay
    def set_delay(self, delay): self.delay = delay
    def get_timeout(self): return self.timeout
    def set_timeout(self, timeout): self.timeout = timeout
    def get_max_retries(self): return self.max_retries
    def set_max_retries(self, max_retries): self.max_retries = max_retries
    def get_http_method(self): return self.http_method
    def set_http_method(self, http_method): self.http_method = http_method
    def get_url_path(self): return self.url_path
    def set_url_path(self, url_path): self.url_path = url_path
    def get_expected_codes(self): return self.expected_codes
    def set_expected_codes(self, expected_codes): self.expected_codes = expected_codes
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.admin_state == other.admin_state and
                self.monitor_type == other.monitor_type and
                self.delay == other.delay and
                self.timeout == other.timeout and
                self.max_retries == other.max_retries and
                self.http_method == other.http_method and
                self.url_path == other.url_path and
                self.expected_codes == other.expected_codes)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_admin_state (obj.populate_boolean ("admin_state"))
        obj.set_monitor_type (obj.populate_string ("monitor_type"))
        obj.set_delay (obj.populate_integer ("delay"))
        obj.set_timeout (obj.populate_integer ("timeout"))
        obj.set_max_retries (obj.populate_integer ("max_retries"))
        obj.set_http_method (obj.populate_string ("http_method"))
        obj.set_url_path (obj.populate_string ("url_path"))
        obj.set_expected_codes (obj.populate_string ("expected_codes"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='LoadbalancerHealthmonitorType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='LoadbalancerHealthmonitorType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='LoadbalancerHealthmonitorType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='LoadbalancerHealthmonitorType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.admin_state is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadmin-state>%s</%sadmin-state>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.admin_state)), input_name='admin-state'), namespace_, eol_))
        if self.monitor_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smonitor-type>%s</%smonitor-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.monitor_type).encode(ExternalEncoding), input_name='monitor-type'), namespace_, eol_))
        if self.delay is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdelay>%s</%sdelay>%s' % (namespace_, self.gds_format_integer(self.delay, input_name='delay'), namespace_, eol_))
        if self.timeout is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stimeout>%s</%stimeout>%s' % (namespace_, self.gds_format_integer(self.timeout, input_name='timeout'), namespace_, eol_))
        if self.max_retries is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smax-retries>%s</%smax-retries>%s' % (namespace_, self.gds_format_integer(self.max_retries, input_name='max-retries'), namespace_, eol_))
        if self.http_method is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shttp-method>%s</%shttp-method>%s' % (namespace_, self.gds_format_string(quote_xml(self.http_method).encode(ExternalEncoding), input_name='http-method'), namespace_, eol_))
        if self.url_path is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%surl-path>%s</%surl-path>%s' % (namespace_, self.gds_format_string(quote_xml(self.url_path).encode(ExternalEncoding), input_name='url-path'), namespace_, eol_))
        if self.expected_codes is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sexpected-codes>%s</%sexpected-codes>%s' % (namespace_, self.gds_format_string(quote_xml(self.expected_codes).encode(ExternalEncoding), input_name='expected-codes'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.admin_state is not None or
            self.monitor_type is not None or
            self.delay is not None or
            self.timeout is not None or
            self.max_retries is not None or
            self.http_method is not None or
            self.url_path is not None or
            self.expected_codes is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='LoadbalancerHealthmonitorType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.admin_state is not None:
            showIndent(outfile, level)
            outfile.write('admin_state=%s,\n' % self.admin_state)
        if self.monitor_type is not None:
            showIndent(outfile, level)
            outfile.write('monitor_type=%s,\n' % quote_python(self.monitor_type).encode(ExternalEncoding))
        if self.delay is not None:
            showIndent(outfile, level)
            outfile.write('delay=%d,\n' % self.delay)
        if self.timeout is not None:
            showIndent(outfile, level)
            outfile.write('timeout=%d,\n' % self.timeout)
        if self.max_retries is not None:
            showIndent(outfile, level)
            outfile.write('max_retries=%d,\n' % self.max_retries)
        if self.http_method is not None:
            showIndent(outfile, level)
            outfile.write('http_method=%s,\n' % quote_python(self.http_method).encode(ExternalEncoding))
        if self.url_path is not None:
            showIndent(outfile, level)
            outfile.write('url_path=%s,\n' % quote_python(self.url_path).encode(ExternalEncoding))
        if self.expected_codes is not None:
            showIndent(outfile, level)
            outfile.write('expected_codes=%s,\n' % quote_python(self.expected_codes).encode(ExternalEncoding))
    def exportDict(self, name_='LoadbalancerHealthmonitorType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'admin-state':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'admin_state')
            self.admin_state = ival_
        elif nodeName_ == 'monitor-type':
            monitor_type_ = child_.text
            monitor_type_ = self.gds_validate_string(monitor_type_, node, 'monitor_type')
            self.monitor_type = monitor_type_
            self.validate_HealthmonitorType(self.monitor_type)    # validate type HealthmonitorType
        elif nodeName_ == 'delay':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'delay')
            self.delay = ival_
        elif nodeName_ == 'timeout':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'timeout')
            self.timeout = ival_
        elif nodeName_ == 'max-retries':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'max_retries')
            self.max_retries = ival_
        elif nodeName_ == 'http-method':
            http_method_ = child_.text
            http_method_ = self.gds_validate_string(http_method_, node, 'http_method')
            self.http_method = http_method_
        elif nodeName_ == 'url-path':
            url_path_ = child_.text
            url_path_ = self.gds_validate_string(url_path_, node, 'url_path')
            self.url_path = url_path_
        elif nodeName_ == 'expected-codes':
            expected_codes_ = child_.text
            expected_codes_ = self.gds_validate_string(expected_codes_, node, 'expected_codes')
            self.expected_codes = expected_codes_
# end class LoadbalancerHealthmonitorType


class project_virtual_ip(GeneratedsSuper):
    """
    project_virtual_ip class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if project_virtual_ip.subclass:
            return project_virtual_ip.subclass(*args_, **kwargs_)
        else:
            return project_virtual_ip(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='project-virtual-ip', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='project-virtual-ip')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='project-virtual-ip'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='project-virtual-ip', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='project-virtual-ip'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='project-virtual-ip'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class project_virtual_ip


class virtual_ip_loadbalancer_pool(GeneratedsSuper):
    """
    virtual_ip_loadbalancer_pool class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_ip_loadbalancer_pool.subclass:
            return virtual_ip_loadbalancer_pool.subclass(*args_, **kwargs_)
        else:
            return virtual_ip_loadbalancer_pool(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-ip-loadbalancer-pool', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-ip-loadbalancer-pool')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-ip-loadbalancer-pool'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-ip-loadbalancer-pool', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-ip-loadbalancer-pool'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-ip-loadbalancer-pool'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_ip_loadbalancer_pool


class virtual_ip_virtual_machine_interface(GeneratedsSuper):
    """
    virtual_ip_virtual_machine_interface class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if virtual_ip_virtual_machine_interface.subclass:
            return virtual_ip_virtual_machine_interface.subclass(*args_, **kwargs_)
        else:
            return virtual_ip_virtual_machine_interface(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='virtual-ip-virtual-machine-interface', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='virtual-ip-virtual-machine-interface')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='virtual-ip-virtual-machine-interface'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='virtual-ip-virtual-machine-interface', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='virtual-ip-virtual-machine-interface'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='virtual-ip-virtual-machine-interface'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class virtual_ip_virtual_machine_interface


class VirtualIpType(GeneratedsSuper):
    """
    VirtualIpType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, address=None, status=None, status_description=None, admin_state=True, protocol=None, protocol_port=None, connection_limit=None, subnet_id=None, persistence_cookie_name=None, persistence_type=None, **kwargs):
        self.address = address
        self.status = status
        self.status_description = status_description
        self.admin_state = admin_state
        self.protocol = protocol
        self.protocol_port = protocol_port
        self.connection_limit = connection_limit
        self.subnet_id = subnet_id
        self.persistence_cookie_name = persistence_cookie_name
        self.persistence_type = persistence_type
    def factory(*args_, **kwargs_):
        if VirtualIpType.subclass:
            return VirtualIpType.subclass(*args_, **kwargs_)
        else:
            return VirtualIpType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def validate_IpAddressType(self, value):
        # Validate type IpAddressType, a restriction on xsd:string.
        pass
    def get_status(self): return self.status
    def set_status(self, status): self.status = status
    def get_status_description(self): return self.status_description
    def set_status_description(self, status_description): self.status_description = status_description
    def get_admin_state(self): return self.admin_state
    def set_admin_state(self, admin_state): self.admin_state = admin_state
    def get_protocol(self): return self.protocol
    def set_protocol(self, protocol): self.protocol = protocol
    def validate_LoadbalancerProtocolType(self, value):
        # Validate type LoadbalancerProtocolType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'HTTP', u'HTTPS', u'TCP'])
        else:
            error = value not in [u'HTTP', u'HTTPS', u'TCP']
        if error:
            raise ValueError("LoadbalancerProtocolType must be one of [u'HTTP', u'HTTPS', u'TCP']")
    def get_protocol_port(self): return self.protocol_port
    def set_protocol_port(self, protocol_port): self.protocol_port = protocol_port
    def get_connection_limit(self): return self.connection_limit
    def set_connection_limit(self, connection_limit): self.connection_limit = connection_limit
    def get_subnet_id(self): return self.subnet_id
    def set_subnet_id(self, subnet_id): self.subnet_id = subnet_id
    def validate_UuidStringType(self, value):
        # Validate type UuidStringType, a restriction on xsd:string.
        pass
    def get_persistence_cookie_name(self): return self.persistence_cookie_name
    def set_persistence_cookie_name(self, persistence_cookie_name): self.persistence_cookie_name = persistence_cookie_name
    def get_persistence_type(self): return self.persistence_type
    def set_persistence_type(self, persistence_type): self.persistence_type = persistence_type
    def validate_SessionPersistenceType(self, value):
        # Validate type SessionPersistenceType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'SOURCE_IP', u'HTTP_COOKIE', u'APP_COOKIE'])
        else:
            error = value not in [u'SOURCE_IP', u'HTTP_COOKIE', u'APP_COOKIE']
        if error:
            raise ValueError("SessionPersistenceType must be one of [u'SOURCE_IP', u'HTTP_COOKIE', u'APP_COOKIE']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.address == other.address and
                self.status == other.status and
                self.status_description == other.status_description and
                self.admin_state == other.admin_state and
                self.protocol == other.protocol and
                self.protocol_port == other.protocol_port and
                self.connection_limit == other.connection_limit and
                self.subnet_id == other.subnet_id and
                self.persistence_cookie_name == other.persistence_cookie_name and
                self.persistence_type == other.persistence_type)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_address (obj.populate_string ("address"))
        obj.set_status (obj.populate_string ("status"))
        obj.set_status_description (obj.populate_string ("status_description"))
        obj.set_admin_state (obj.populate_boolean ("admin_state"))
        obj.set_protocol (obj.populate_string ("protocol"))
        obj.set_protocol_port (obj.populate_integer ("protocol_port"))
        obj.set_connection_limit (obj.populate_integer ("connection_limit"))
        obj.set_subnet_id (obj.populate_string ("subnet_id"))
        obj.set_persistence_cookie_name (obj.populate_string ("persistence_cookie_name"))
        obj.set_persistence_type (obj.populate_string ("persistence_type"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='VirtualIpType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='VirtualIpType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='VirtualIpType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='VirtualIpType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress>%s</%saddress>%s' % (namespace_, self.gds_format_string(quote_xml(self.address).encode(ExternalEncoding), input_name='address'), namespace_, eol_))
        if self.status is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus>%s</%sstatus>%s' % (namespace_, self.gds_format_string(quote_xml(self.status).encode(ExternalEncoding), input_name='status'), namespace_, eol_))
        if self.status_description is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstatus-description>%s</%sstatus-description>%s' % (namespace_, self.gds_format_string(quote_xml(self.status_description).encode(ExternalEncoding), input_name='status-description'), namespace_, eol_))
        if self.admin_state is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sadmin-state>%s</%sadmin-state>%s' % (namespace_, self.gds_format_boolean(self.gds_str_lower(str(self.admin_state)), input_name='admin-state'), namespace_, eol_))
        if self.protocol is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprotocol>%s</%sprotocol>%s' % (namespace_, self.gds_format_string(quote_xml(self.protocol).encode(ExternalEncoding), input_name='protocol'), namespace_, eol_))
        if self.protocol_port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprotocol-port>%s</%sprotocol-port>%s' % (namespace_, self.gds_format_integer(self.protocol_port, input_name='protocol-port'), namespace_, eol_))
        if self.connection_limit is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sconnection-limit>%s</%sconnection-limit>%s' % (namespace_, self.gds_format_integer(self.connection_limit, input_name='connection-limit'), namespace_, eol_))
        if self.subnet_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssubnet-id>%s</%ssubnet-id>%s' % (namespace_, self.gds_format_string(quote_xml(self.subnet_id).encode(ExternalEncoding), input_name='subnet-id'), namespace_, eol_))
        if self.persistence_cookie_name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spersistence-cookie-name>%s</%spersistence-cookie-name>%s' % (namespace_, self.gds_format_string(quote_xml(self.persistence_cookie_name).encode(ExternalEncoding), input_name='persistence-cookie-name'), namespace_, eol_))
        if self.persistence_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spersistence-type>%s</%spersistence-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.persistence_type).encode(ExternalEncoding), input_name='persistence-type'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.address is not None or
            self.status is not None or
            self.status_description is not None or
            self.admin_state is not None or
            self.protocol is not None or
            self.protocol_port is not None or
            self.connection_limit is not None or
            self.subnet_id is not None or
            self.persistence_cookie_name is not None or
            self.persistence_type is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='VirtualIpType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.address is not None:
            showIndent(outfile, level)
            outfile.write('address=%s,\n' % quote_python(self.address).encode(ExternalEncoding))
        if self.status is not None:
            showIndent(outfile, level)
            outfile.write('status=%s,\n' % quote_python(self.status).encode(ExternalEncoding))
        if self.status_description is not None:
            showIndent(outfile, level)
            outfile.write('status_description=%s,\n' % quote_python(self.status_description).encode(ExternalEncoding))
        if self.admin_state is not None:
            showIndent(outfile, level)
            outfile.write('admin_state=%s,\n' % self.admin_state)
        if self.protocol is not None:
            showIndent(outfile, level)
            outfile.write('protocol=%s,\n' % quote_python(self.protocol).encode(ExternalEncoding))
        if self.protocol_port is not None:
            showIndent(outfile, level)
            outfile.write('protocol_port=%d,\n' % self.protocol_port)
        if self.connection_limit is not None:
            showIndent(outfile, level)
            outfile.write('connection_limit=%d,\n' % self.connection_limit)
        if self.subnet_id is not None:
            showIndent(outfile, level)
            outfile.write('subnet_id=%s,\n' % quote_python(self.subnet_id).encode(ExternalEncoding))
        if self.persistence_cookie_name is not None:
            showIndent(outfile, level)
            outfile.write('persistence_cookie_name=%s,\n' % quote_python(self.persistence_cookie_name).encode(ExternalEncoding))
        if self.persistence_type is not None:
            showIndent(outfile, level)
            outfile.write('persistence_type=%s,\n' % quote_python(self.persistence_type).encode(ExternalEncoding))
    def exportDict(self, name_='VirtualIpType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'address':
            address_ = child_.text
            address_ = self.gds_validate_string(address_, node, 'address')
            self.address = address_
            self.validate_IpAddressType(self.address)    # validate type IpAddressType
        elif nodeName_ == 'status':
            status_ = child_.text
            status_ = self.gds_validate_string(status_, node, 'status')
            self.status = status_
        elif nodeName_ == 'status-description':
            status_description_ = child_.text
            status_description_ = self.gds_validate_string(status_description_, node, 'status_description')
            self.status_description = status_description_
        elif nodeName_ == 'admin-state':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'admin_state')
            self.admin_state = ival_
        elif nodeName_ == 'protocol':
            protocol_ = child_.text
            protocol_ = self.gds_validate_string(protocol_, node, 'protocol')
            self.protocol = protocol_
            self.validate_LoadbalancerProtocolType(self.protocol)    # validate type LoadbalancerProtocolType
        elif nodeName_ == 'protocol-port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'protocol_port')
            self.protocol_port = ival_
        elif nodeName_ == 'connection-limit':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'connection_limit')
            self.connection_limit = ival_
        elif nodeName_ == 'subnet-id':
            subnet_id_ = child_.text
            subnet_id_ = self.gds_validate_string(subnet_id_, node, 'subnet_id')
            self.subnet_id = subnet_id_
            self.validate_UuidStringType(self.subnet_id)    # validate type UuidStringType
        elif nodeName_ == 'persistence-cookie-name':
            persistence_cookie_name_ = child_.text
            persistence_cookie_name_ = self.gds_validate_string(persistence_cookie_name_, node, 'persistence_cookie_name')
            self.persistence_cookie_name = persistence_cookie_name_
        elif nodeName_ == 'persistence-type':
            persistence_type_ = child_.text
            persistence_type_ = self.gds_validate_string(persistence_type_, node, 'persistence_type')
            self.persistence_type = persistence_type_
            self.validate_SessionPersistenceType(self.persistence_type)    # validate type SessionPersistenceType
# end class VirtualIpType


class BgpRouterParams(GeneratedsSuper):
    """
    BgpRouterParams class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, vendor=None, autonomous_system=None, identifier=None, address=None, port=None, hold_time=90, address_families=None, auth_data=None, local_autonomous_system=None, **kwargs):
        self.vendor = vendor
        self.autonomous_system = autonomous_system
        self.identifier = identifier
        self.address = address
        self.port = port
        self.hold_time = hold_time
        if isinstance(address_families, dict):
            obj = AddressFamilies(**address_families)
            self.address_families = obj
        else:
            self.address_families = address_families
        if isinstance(auth_data, dict):
            obj = AuthenticationData(**auth_data)
            self.auth_data = obj
        else:
            self.auth_data = auth_data
        self.local_autonomous_system = local_autonomous_system
    def factory(*args_, **kwargs_):
        if BgpRouterParams.subclass:
            return BgpRouterParams.subclass(*args_, **kwargs_)
        else:
            return BgpRouterParams(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_vendor(self): return self.vendor
    def set_vendor(self, vendor): self.vendor = vendor
    def get_autonomous_system(self): return self.autonomous_system
    def set_autonomous_system(self, autonomous_system): self.autonomous_system = autonomous_system
    def get_identifier(self): return self.identifier
    def set_identifier(self, identifier): self.identifier = identifier
    def validate_IpAddress(self, value):
        # Validate type IpAddress, a restriction on xsd:string.
        pass
    def get_address(self): return self.address
    def set_address(self, address): self.address = address
    def get_port(self): return self.port
    def set_port(self, port): self.port = port
    def get_hold_time(self): return self.hold_time
    def set_hold_time(self, hold_time): self.hold_time = hold_time
    def validate_BgpHoldTime(self, value):
        # Validate type BgpHoldTime, a restriction on xsd:integer.
        error = False
        if isinstance(value, list):
            v_int = map(int, value)
            v1, v2 = min(v_int), max(v_int)
        else:
            v1, v2 = int(value), int(value)
        error = (1 > v1)
        error |= (v2 > 65535)
        if error:
            raise ValueError("BgpHoldTime must be in the range 1-65535")
    def get_address_families(self): return self.address_families
    def set_address_families(self, address_families): self.address_families = address_families
    def get_auth_data(self): return self.auth_data
    def set_auth_data(self, auth_data): self.auth_data = auth_data
    def get_local_autonomous_system(self): return self.local_autonomous_system
    def set_local_autonomous_system(self, local_autonomous_system): self.local_autonomous_system = local_autonomous_system
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.vendor == other.vendor and
                self.autonomous_system == other.autonomous_system and
                self.identifier == other.identifier and
                self.address == other.address and
                self.port == other.port and
                self.hold_time == other.hold_time and
                self.address_families == other.address_families and
                self.auth_data == other.auth_data and
                self.local_autonomous_system == other.local_autonomous_system)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_vendor (obj.populate_string ("vendor"))
        obj.set_autonomous_system (obj.populate_integer ("autonomous_system"))
        obj.set_identifier (obj.populate_string ("identifier"))
        obj.set_address (obj.populate_string ("address"))
        obj.set_port (obj.populate_integer ("port"))
        obj.set_hold_time (obj.populate_integer ("hold_time"))
        obj.set_address_families (AddressFamilies.populate ())
        obj.set_auth_data (AuthenticationData.populate ())
        obj.set_local_autonomous_system (obj.populate_integer ("local_autonomous_system"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='BgpRouterParams', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BgpRouterParams')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BgpRouterParams'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='BgpRouterParams', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.vendor is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svendor>%s</%svendor>%s' % (namespace_, self.gds_format_string(quote_xml(self.vendor).encode(ExternalEncoding), input_name='vendor'), namespace_, eol_))
        if self.autonomous_system is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sautonomous-system>%s</%sautonomous-system>%s' % (namespace_, self.gds_format_integer(self.autonomous_system, input_name='autonomous-system'), namespace_, eol_))
        if self.identifier is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sidentifier>%s</%sidentifier>%s' % (namespace_, self.gds_format_string(quote_xml(self.identifier).encode(ExternalEncoding), input_name='identifier'), namespace_, eol_))
        if self.address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%saddress>%s</%saddress>%s' % (namespace_, self.gds_format_string(quote_xml(self.address).encode(ExternalEncoding), input_name='address'), namespace_, eol_))
        if self.port is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sport>%s</%sport>%s' % (namespace_, self.gds_format_integer(self.port, input_name='port'), namespace_, eol_))
        if self.hold_time is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%shold-time>%s</%shold-time>%s' % (namespace_, self.gds_format_integer(self.hold_time, input_name='hold-time'), namespace_, eol_))
        if self.address_families is not None:
            self.address_families.export(outfile, level, namespace_, name_='address-families', pretty_print=pretty_print)
        if self.auth_data is not None:
            self.auth_data.export(outfile, level, namespace_, name_='auth-data', pretty_print=pretty_print)
        if self.local_autonomous_system is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slocal-autonomous-system>%s</%slocal-autonomous-system>%s' % (namespace_, self.gds_format_integer(self.local_autonomous_system, input_name='local-autonomous-system'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.vendor is not None or
            self.autonomous_system is not None or
            self.identifier is not None or
            self.address is not None or
            self.port is not None or
            self.hold_time is not None or
            self.address_families is not None or
            self.auth_data is not None or
            self.local_autonomous_system is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='BgpRouterParams'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.vendor is not None:
            showIndent(outfile, level)
            outfile.write('vendor=%s,\n' % quote_python(self.vendor).encode(ExternalEncoding))
        if self.autonomous_system is not None:
            showIndent(outfile, level)
            outfile.write('autonomous_system=%d,\n' % self.autonomous_system)
        if self.identifier is not None:
            showIndent(outfile, level)
            outfile.write('identifier=%s,\n' % quote_python(self.identifier).encode(ExternalEncoding))
        if self.address is not None:
            showIndent(outfile, level)
            outfile.write('address=%s,\n' % quote_python(self.address).encode(ExternalEncoding))
        if self.port is not None:
            showIndent(outfile, level)
            outfile.write('port=%d,\n' % self.port)
        if self.hold_time is not None:
            showIndent(outfile, level)
            outfile.write('hold_time=%d,\n' % self.hold_time)
        if self.address_families is not None:
            showIndent(outfile, level)
            outfile.write('address_families=model_.AddressFamilies(\n')
            self.address_families.exportLiteral(outfile, level, name_='address_families')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.auth_data is not None:
            showIndent(outfile, level)
            outfile.write('auth_data=model_.AuthenticationData(\n')
            self.auth_data.exportLiteral(outfile, level, name_='auth_data')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.local_autonomous_system is not None:
            showIndent(outfile, level)
            outfile.write('local_autonomous_system=%d,\n' % self.local_autonomous_system)
    def exportDict(self, name_='BgpRouterParams'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'vendor':
            vendor_ = child_.text
            vendor_ = self.gds_validate_string(vendor_, node, 'vendor')
            self.vendor = vendor_
        elif nodeName_ == 'autonomous-system':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'autonomous_system')
            self.autonomous_system = ival_
        elif nodeName_ == 'identifier':
            identifier_ = child_.text
            identifier_ = self.gds_validate_string(identifier_, node, 'identifier')
            self.identifier = identifier_
            self.validate_IpAddress(self.identifier)    # validate type IpAddress
        elif nodeName_ == 'address':
            address_ = child_.text
            address_ = self.gds_validate_string(address_, node, 'address')
            self.address = address_
            self.validate_IpAddress(self.address)    # validate type IpAddress
        elif nodeName_ == 'port':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'port')
            self.port = ival_
        elif nodeName_ == 'hold-time':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'hold_time')
            self.hold_time = ival_
            self.validate_BgpHoldTime(self.hold_time)    # validate type BgpHoldTime
        elif nodeName_ == 'address-families':
            obj_ = AddressFamilies.factory()
            obj_.build(child_)
            self.set_address_families(obj_)
        elif nodeName_ == 'auth-data':
            obj_ = AuthenticationData.factory()
            obj_.build(child_)
            self.set_auth_data(obj_)
        elif nodeName_ == 'local-autonomous-system':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'local_autonomous_system')
            self.local_autonomous_system = ival_
# end class BgpRouterParams


class instance_bgp_router(GeneratedsSuper):
    """
    instance_bgp_router class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if instance_bgp_router.subclass:
            return instance_bgp_router.subclass(*args_, **kwargs_)
        else:
            return instance_bgp_router(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='instance-bgp-router', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='instance-bgp-router')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='instance-bgp-router'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='instance-bgp-router', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='instance-bgp-router'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='instance-bgp-router'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class instance_bgp_router


class BgpPeeringAttributes(GeneratedsSuper):
    """
    BgpPeeringAttributes class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, session=None, **kwargs):
        if (session is None) or (session == []):
            self.session = []
        else:
            if isinstance(session[0], dict):
                objs = [BgpSession(**elem) for elem in session]
                self.session = objs
            else:
                self.session = session
    def factory(*args_, **kwargs_):
        if BgpPeeringAttributes.subclass:
            return BgpPeeringAttributes.subclass(*args_, **kwargs_)
        else:
            return BgpPeeringAttributes(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_session(self): return self.session
    def set_session(self, session): self.session = session
    def add_session(self, value): self.session.append(value)
    def insert_session(self, index, value): self.session[index] = value
    def delete_session(self, value): self.session.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.session == other.session)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_session ([BgpSession.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='BgpPeeringAttributes', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BgpPeeringAttributes')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BgpPeeringAttributes'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='BgpPeeringAttributes', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for session_ in self.session:
            if isinstance(session_, dict):
                session_ = BgpSession(**session_)
            session_.export(outfile, level, namespace_, name_='session', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.session
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='BgpPeeringAttributes'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('session=[\n')
        level += 1
        for session_ in self.session:
            showIndent(outfile, level)
            outfile.write('model_.BgpSession(\n')
            session_.exportLiteral(outfile, level, name_='BgpSession')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='BgpPeeringAttributes'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'session':
            obj_ = BgpSession.factory()
            obj_.build(child_)
            self.session.append(obj_)
# end class BgpPeeringAttributes


class BgpSession(GeneratedsSuper):
    """
    BgpSession class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, uuid=None, attributes=None, **kwargs):
        self.uuid = uuid
        if (attributes is None) or (attributes == []):
            self.attributes = []
        else:
            if isinstance(attributes[0], dict):
                objs = [BgpSessionAttributes(**elem) for elem in attributes]
                self.attributes = objs
            else:
                self.attributes = attributes
    def factory(*args_, **kwargs_):
        if BgpSession.subclass:
            return BgpSession.subclass(*args_, **kwargs_)
        else:
            return BgpSession(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_uuid(self): return self.uuid
    def set_uuid(self, uuid): self.uuid = uuid
    def get_attributes(self): return self.attributes
    def set_attributes(self, attributes): self.attributes = attributes
    def add_attributes(self, value): self.attributes.append(value)
    def insert_attributes(self, index, value): self.attributes[index] = value
    def delete_attributes(self, value): self.attributes.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.uuid == other.uuid and
                self.attributes == other.attributes)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_uuid (obj.populate_string ("uuid"))
        obj.set_attributes ([BgpSessionAttributes.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='BgpSession', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BgpSession')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BgpSession'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='BgpSession', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.uuid is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suuid>%s</%suuid>%s' % (namespace_, self.gds_format_string(quote_xml(self.uuid).encode(ExternalEncoding), input_name='uuid'), namespace_, eol_))
        for attributes_ in self.attributes:
            if isinstance(attributes_, dict):
                attributes_ = BgpSessionAttributes(**attributes_)
            attributes_.export(outfile, level, namespace_, name_='attributes', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.uuid is not None or
            self.attributes
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='BgpSession'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.uuid is not None:
            showIndent(outfile, level)
            outfile.write('uuid=%s,\n' % quote_python(self.uuid).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('attributes=[\n')
        level += 1
        for attributes_ in self.attributes:
            showIndent(outfile, level)
            outfile.write('model_.BgpSessionAttributes(\n')
            attributes_.exportLiteral(outfile, level, name_='BgpSessionAttributes')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='BgpSession'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'uuid':
            uuid_ = child_.text
            uuid_ = self.gds_validate_string(uuid_, node, 'uuid')
            self.uuid = uuid_
        elif nodeName_ == 'attributes':
            obj_ = BgpSessionAttributes.factory()
            obj_.build(child_)
            self.attributes.append(obj_)
# end class BgpSession


class BgpSessionAttributes(GeneratedsSuper):
    """
    BgpSessionAttributes class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, bgp_router=None, address_families=None, auth_data=None, **kwargs):
        self.bgp_router = bgp_router
        if isinstance(address_families, dict):
            obj = AddressFamilies(**address_families)
            self.address_families = obj
        else:
            self.address_families = address_families
        if isinstance(auth_data, dict):
            obj = AuthenticationData(**auth_data)
            self.auth_data = obj
        else:
            self.auth_data = auth_data
    def factory(*args_, **kwargs_):
        if BgpSessionAttributes.subclass:
            return BgpSessionAttributes.subclass(*args_, **kwargs_)
        else:
            return BgpSessionAttributes(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_bgp_router(self): return self.bgp_router
    def set_bgp_router(self, bgp_router): self.bgp_router = bgp_router
    def get_address_families(self): return self.address_families
    def set_address_families(self, address_families): self.address_families = address_families
    def get_auth_data(self): return self.auth_data
    def set_auth_data(self, auth_data): self.auth_data = auth_data
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.bgp_router == other.bgp_router and
                self.address_families == other.address_families and
                self.auth_data == other.auth_data)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_bgp_router (obj.populate_string ("bgp_router"))
        obj.set_address_families (AddressFamilies.populate ())
        obj.set_auth_data (AuthenticationData.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='BgpSessionAttributes', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BgpSessionAttributes')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BgpSessionAttributes'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='BgpSessionAttributes', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.bgp_router is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbgp-router>%s</%sbgp-router>%s' % (namespace_, self.gds_format_string(quote_xml(self.bgp_router).encode(ExternalEncoding), input_name='bgp-router'), namespace_, eol_))
        if self.address_families is not None:
            self.address_families.export(outfile, level, namespace_, name_='address-families', pretty_print=pretty_print)
        if self.auth_data is not None:
            self.auth_data.export(outfile, level, namespace_, name_='auth-data', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.bgp_router is not None or
            self.address_families is not None or
            self.auth_data is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='BgpSessionAttributes'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bgp_router is not None:
            showIndent(outfile, level)
            outfile.write('bgp_router=%s,\n' % quote_python(self.bgp_router).encode(ExternalEncoding))
        if self.address_families is not None:
            showIndent(outfile, level)
            outfile.write('address_families=model_.AddressFamilies(\n')
            self.address_families.exportLiteral(outfile, level, name_='address_families')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.auth_data is not None:
            showIndent(outfile, level)
            outfile.write('auth_data=model_.AuthenticationData(\n')
            self.auth_data.exportLiteral(outfile, level, name_='auth_data')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='BgpSessionAttributes'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'bgp-router':
            bgp_router_ = child_.text
            bgp_router_ = self.gds_validate_string(bgp_router_, node, 'bgp_router')
            self.bgp_router = bgp_router_
        elif nodeName_ == 'address-families':
            obj_ = AddressFamilies.factory()
            obj_.build(child_)
            self.set_address_families(obj_)
        elif nodeName_ == 'auth-data':
            obj_ = AuthenticationData.factory()
            obj_.build(child_)
            self.set_auth_data(obj_)
# end class BgpSessionAttributes


class AddressFamilies(GeneratedsSuper):
    """
    AddressFamilies class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, family=None, **kwargs):
        if (family is None) or (family == []):
            self.family = []
        else:
            self.family = family
    def factory(*args_, **kwargs_):
        if AddressFamilies.subclass:
            return AddressFamilies.subclass(*args_, **kwargs_)
        else:
            return AddressFamilies(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_family(self): return self.family
    def set_family(self, family): self.family = family
    def add_family(self, value): self.family.append(value)
    def insert_family(self, index, value): self.family[index] = value
    def delete_family(self, value): self.family.remove(value)
    def validate_AddressFamily(self, value):
        # Validate type AddressFamily, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6-vpn'])
        else:
            error = value not in [u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6-vpn']
        if error:
            raise ValueError("AddressFamily must be one of [u'inet', u'inet-vpn', u'e-vpn', u'erm-vpn', u'route-target', u'inet6-vpn']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.family == other.family)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_family ([obj.populate_string ("family")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AddressFamilies', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AddressFamilies')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AddressFamilies'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AddressFamilies', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for family_ in self.family:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfamily>%s</%sfamily>%s' % (namespace_, self.gds_format_string(quote_xml(family_).encode(ExternalEncoding), input_name='family'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.family
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AddressFamilies'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('family=[\n')
        level += 1
        for family_ in self.family:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(family_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='AddressFamilies'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'family':
            family_ = child_.text
            family_ = self.gds_validate_string(family_, node, 'family')
            self.family.append(family_)
            self.validate_AddressFamily(self.family)    # validate type AddressFamily
# end class AddressFamilies


class AuthenticationKeyItem(GeneratedsSuper):
    """
    AuthenticationKeyItem class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, key_id=None, key=None, **kwargs):
        self.key_id = key_id
        self.key = key
    def factory(*args_, **kwargs_):
        if AuthenticationKeyItem.subclass:
            return AuthenticationKeyItem.subclass(*args_, **kwargs_)
        else:
            return AuthenticationKeyItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_key_id(self): return self.key_id
    def set_key_id(self, key_id): self.key_id = key_id
    def validate_AuthenticationKeyId(self, value):
        # Validate type AuthenticationKeyId, a restriction on xsd:integer.
        error = False
        if isinstance(value, list):
            v_int = map(int, value)
            v1, v2 = min(v_int), max(v_int)
        else:
            v1, v2 = int(value), int(value)
        error = (0 > v1)
        error |= (v2 > 63)
        if error:
            raise ValueError("AuthenticationKeyId must be in the range 0-63")
    def get_key(self): return self.key
    def set_key(self, key): self.key = key
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.key_id == other.key_id and
                self.key == other.key)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_key_id (obj.populate_integer ("key_id"))
        obj.set_key (obj.populate_string ("key"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AuthenticationKeyItem', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AuthenticationKeyItem')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AuthenticationKeyItem'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AuthenticationKeyItem', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.key_id is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%skey-id>%s</%skey-id>%s' % (namespace_, self.gds_format_integer(self.key_id, input_name='key-id'), namespace_, eol_))
        if self.key is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%skey>%s</%skey>%s' % (namespace_, self.gds_format_string(quote_xml(self.key).encode(ExternalEncoding), input_name='key'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.key_id is not None or
            self.key is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AuthenticationKeyItem'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.key_id is not None:
            showIndent(outfile, level)
            outfile.write('key_id=%d,\n' % self.key_id)
        if self.key is not None:
            showIndent(outfile, level)
            outfile.write('key=%s,\n' % quote_python(self.key).encode(ExternalEncoding))
    def exportDict(self, name_='AuthenticationKeyItem'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'key-id':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'key_id')
            self.key_id = ival_
            self.validate_AuthenticationKeyId(self.key_id)    # validate type AuthenticationKeyId
        elif nodeName_ == 'key':
            key_ = child_.text
            key_ = self.gds_validate_string(key_, node, 'key')
            self.key = key_
# end class AuthenticationKeyItem


class AuthenticationData(GeneratedsSuper):
    """
    AuthenticationData class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, key_type=None, key_items=None, **kwargs):
        self.key_type = key_type
        if (key_items is None) or (key_items == []):
            self.key_items = []
        else:
            if isinstance(key_items[0], dict):
                objs = [AuthenticationKeyItem(**elem) for elem in key_items]
                self.key_items = objs
            else:
                self.key_items = key_items
    def factory(*args_, **kwargs_):
        if AuthenticationData.subclass:
            return AuthenticationData.subclass(*args_, **kwargs_)
        else:
            return AuthenticationData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_key_type(self): return self.key_type
    def set_key_type(self, key_type): self.key_type = key_type
    def validate_AuthenticationKeyType(self, value):
        # Validate type AuthenticationKeyType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'md5'])
        else:
            error = value not in [u'md5']
        if error:
            raise ValueError("AuthenticationKeyType must be one of [u'md5']")
    def get_key_items(self): return self.key_items
    def set_key_items(self, key_items): self.key_items = key_items
    def add_key_items(self, value): self.key_items.append(value)
    def insert_key_items(self, index, value): self.key_items[index] = value
    def delete_key_items(self, value): self.key_items.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.key_type == other.key_type and
                self.key_items == other.key_items)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_key_type (obj.populate_string ("key_type"))
        obj.set_key_items ([AuthenticationKeyItem.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AuthenticationData', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AuthenticationData')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AuthenticationData'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AuthenticationData', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.key_type is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%skey-type>%s</%skey-type>%s' % (namespace_, self.gds_format_string(quote_xml(self.key_type).encode(ExternalEncoding), input_name='key-type'), namespace_, eol_))
        for key_items_ in self.key_items:
            if isinstance(key_items_, dict):
                key_items_ = AuthenticationKeyItem(**key_items_)
            key_items_.export(outfile, level, namespace_, name_='key-items', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.key_type is not None or
            self.key_items
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AuthenticationData'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.key_type is not None:
            showIndent(outfile, level)
            outfile.write('key_type=%s,\n' % quote_python(self.key_type).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('key_items=[\n')
        level += 1
        for key_items_ in self.key_items:
            showIndent(outfile, level)
            outfile.write('model_.AuthenticationKeyItem(\n')
            key_items_.exportLiteral(outfile, level, name_='AuthenticationKeyItem')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='AuthenticationData'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'key-type':
            key_type_ = child_.text
            key_type_ = self.gds_validate_string(key_type_, node, 'key_type')
            self.key_type = key_type_
            self.validate_AuthenticationKeyType(self.key_type)    # validate type AuthenticationKeyType
        elif nodeName_ == 'key-items':
            obj_ = AuthenticationKeyItem.factory()
            obj_.build(child_)
            self.key_items.append(obj_)
# end class AuthenticationData


class ServiceChainInfo(GeneratedsSuper):
    """
    ServiceChainInfo class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, routing_instance=None, prefix=None, service_chain_address=None, service_instance=None, source_routing_instance=None, **kwargs):
        self.routing_instance = routing_instance
        if (prefix is None) or (prefix == []):
            self.prefix = []
        else:
            self.prefix = prefix
        self.service_chain_address = service_chain_address
        self.service_instance = service_instance
        self.source_routing_instance = source_routing_instance
    def factory(*args_, **kwargs_):
        if ServiceChainInfo.subclass:
            return ServiceChainInfo.subclass(*args_, **kwargs_)
        else:
            return ServiceChainInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_routing_instance(self): return self.routing_instance
    def set_routing_instance(self, routing_instance): self.routing_instance = routing_instance
    def get_prefix(self): return self.prefix
    def set_prefix(self, prefix): self.prefix = prefix
    def add_prefix(self, value): self.prefix.append(value)
    def insert_prefix(self, index, value): self.prefix[index] = value
    def delete_prefix(self, value): self.prefix.remove(value)
    def get_service_chain_address(self): return self.service_chain_address
    def set_service_chain_address(self, service_chain_address): self.service_chain_address = service_chain_address
    def validate_IpAddress(self, value):
        # Validate type IpAddress, a restriction on xsd:string.
        pass
    def get_service_instance(self): return self.service_instance
    def set_service_instance(self, service_instance): self.service_instance = service_instance
    def get_source_routing_instance(self): return self.source_routing_instance
    def set_source_routing_instance(self, source_routing_instance): self.source_routing_instance = source_routing_instance
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.routing_instance == other.routing_instance and
                self.prefix == other.prefix and
                self.service_chain_address == other.service_chain_address and
                self.service_instance == other.service_instance and
                self.source_routing_instance == other.source_routing_instance)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_routing_instance (obj.populate_string ("routing_instance"))
        obj.set_prefix ([obj.populate_string ("prefix")])
        obj.set_service_chain_address (obj.populate_string ("service_chain_address"))
        obj.set_service_instance (obj.populate_string ("service_instance"))
        obj.set_source_routing_instance (obj.populate_string ("source_routing_instance"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ServiceChainInfo', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ServiceChainInfo')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ServiceChainInfo'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ServiceChainInfo', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.routing_instance is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srouting-instance>%s</%srouting-instance>%s' % (namespace_, self.gds_format_string(quote_xml(self.routing_instance).encode(ExternalEncoding), input_name='routing-instance'), namespace_, eol_))
        for prefix_ in self.prefix:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprefix>%s</%sprefix>%s' % (namespace_, self.gds_format_string(quote_xml(prefix_).encode(ExternalEncoding), input_name='prefix'), namespace_, eol_))
        if self.service_chain_address is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-chain-address>%s</%sservice-chain-address>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_chain_address).encode(ExternalEncoding), input_name='service-chain-address'), namespace_, eol_))
        if self.service_instance is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sservice-instance>%s</%sservice-instance>%s' % (namespace_, self.gds_format_string(quote_xml(self.service_instance).encode(ExternalEncoding), input_name='service-instance'), namespace_, eol_))
        if self.source_routing_instance is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssource-routing-instance>%s</%ssource-routing-instance>%s' % (namespace_, self.gds_format_string(quote_xml(self.source_routing_instance).encode(ExternalEncoding), input_name='source-routing-instance'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.routing_instance is not None or
            self.prefix or
            self.service_chain_address is not None or
            self.service_instance is not None or
            self.source_routing_instance is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ServiceChainInfo'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.routing_instance is not None:
            showIndent(outfile, level)
            outfile.write('routing_instance=%s,\n' % quote_python(self.routing_instance).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('prefix=[\n')
        level += 1
        for prefix_ in self.prefix:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(prefix_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.service_chain_address is not None:
            showIndent(outfile, level)
            outfile.write('service_chain_address=%s,\n' % quote_python(self.service_chain_address).encode(ExternalEncoding))
        if self.service_instance is not None:
            showIndent(outfile, level)
            outfile.write('service_instance=%s,\n' % quote_python(self.service_instance).encode(ExternalEncoding))
        if self.source_routing_instance is not None:
            showIndent(outfile, level)
            outfile.write('source_routing_instance=%s,\n' % quote_python(self.source_routing_instance).encode(ExternalEncoding))
    def exportDict(self, name_='ServiceChainInfo'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'routing-instance':
            routing_instance_ = child_.text
            routing_instance_ = self.gds_validate_string(routing_instance_, node, 'routing_instance')
            self.routing_instance = routing_instance_
        elif nodeName_ == 'prefix':
            prefix_ = child_.text
            prefix_ = self.gds_validate_string(prefix_, node, 'prefix')
            self.prefix.append(prefix_)
        elif nodeName_ == 'service-chain-address':
            service_chain_address_ = child_.text
            service_chain_address_ = self.gds_validate_string(service_chain_address_, node, 'service_chain_address')
            self.service_chain_address = service_chain_address_
            self.validate_IpAddress(self.service_chain_address)    # validate type IpAddress
        elif nodeName_ == 'service-instance':
            service_instance_ = child_.text
            service_instance_ = self.gds_validate_string(service_instance_, node, 'service_instance')
            self.service_instance = service_instance_
        elif nodeName_ == 'source-routing-instance':
            source_routing_instance_ = child_.text
            source_routing_instance_ = self.gds_validate_string(source_routing_instance_, node, 'source_routing_instance')
            self.source_routing_instance = source_routing_instance_
# end class ServiceChainInfo


class StaticRouteType(GeneratedsSuper):
    """
    StaticRouteType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, prefix=None, next_hop=None, route_target=None, **kwargs):
        self.prefix = prefix
        self.next_hop = next_hop
        if (route_target is None) or (route_target == []):
            self.route_target = []
        else:
            self.route_target = route_target
    def factory(*args_, **kwargs_):
        if StaticRouteType.subclass:
            return StaticRouteType.subclass(*args_, **kwargs_)
        else:
            return StaticRouteType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_prefix(self): return self.prefix
    def set_prefix(self, prefix): self.prefix = prefix
    def get_next_hop(self): return self.next_hop
    def set_next_hop(self, next_hop): self.next_hop = next_hop
    def get_route_target(self): return self.route_target
    def set_route_target(self, route_target): self.route_target = route_target
    def add_route_target(self, value): self.route_target.append(value)
    def insert_route_target(self, index, value): self.route_target[index] = value
    def delete_route_target(self, value): self.route_target.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.prefix == other.prefix and
                self.next_hop == other.next_hop and
                self.route_target == other.route_target)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_prefix (obj.populate_string ("prefix"))
        obj.set_next_hop (obj.populate_string ("next_hop"))
        obj.set_route_target ([obj.populate_string ("route_target")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='StaticRouteType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='StaticRouteType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='StaticRouteType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='StaticRouteType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.prefix is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprefix>%s</%sprefix>%s' % (namespace_, self.gds_format_string(quote_xml(self.prefix).encode(ExternalEncoding), input_name='prefix'), namespace_, eol_))
        if self.next_hop is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snext-hop>%s</%snext-hop>%s' % (namespace_, self.gds_format_string(quote_xml(self.next_hop).encode(ExternalEncoding), input_name='next-hop'), namespace_, eol_))
        for route_target_ in self.route_target:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sroute-target>%s</%sroute-target>%s' % (namespace_, self.gds_format_string(quote_xml(route_target_).encode(ExternalEncoding), input_name='route-target'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.prefix is not None or
            self.next_hop is not None or
            self.route_target
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='StaticRouteType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.prefix is not None:
            showIndent(outfile, level)
            outfile.write('prefix=%s,\n' % quote_python(self.prefix).encode(ExternalEncoding))
        if self.next_hop is not None:
            showIndent(outfile, level)
            outfile.write('next_hop=%s,\n' % quote_python(self.next_hop).encode(ExternalEncoding))
        showIndent(outfile, level)
        outfile.write('route_target=[\n')
        level += 1
        for route_target_ in self.route_target:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(route_target_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='StaticRouteType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'prefix':
            prefix_ = child_.text
            prefix_ = self.gds_validate_string(prefix_, node, 'prefix')
            self.prefix = prefix_
        elif nodeName_ == 'next-hop':
            next_hop_ = child_.text
            next_hop_ = self.gds_validate_string(next_hop_, node, 'next_hop')
            self.next_hop = next_hop_
        elif nodeName_ == 'route-target':
            route_target_ = child_.text
            route_target_ = self.gds_validate_string(route_target_, node, 'route_target')
            self.route_target.append(route_target_)
# end class StaticRouteType


class StaticRouteEntriesType(GeneratedsSuper):
    """
    StaticRouteEntriesType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, route=None, **kwargs):
        if (route is None) or (route == []):
            self.route = []
        else:
            if isinstance(route[0], dict):
                objs = [StaticRouteType(**elem) for elem in route]
                self.route = objs
            else:
                self.route = route
    def factory(*args_, **kwargs_):
        if StaticRouteEntriesType.subclass:
            return StaticRouteEntriesType.subclass(*args_, **kwargs_)
        else:
            return StaticRouteEntriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_route(self): return self.route
    def set_route(self, route): self.route = route
    def add_route(self, value): self.route.append(value)
    def insert_route(self, index, value): self.route[index] = value
    def delete_route(self, value): self.route.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.route == other.route)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_route ([StaticRouteType.populate ()])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='StaticRouteEntriesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='StaticRouteEntriesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='StaticRouteEntriesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='StaticRouteEntriesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for route_ in self.route:
            if isinstance(route_, dict):
                route_ = StaticRouteType(**route_)
            route_.export(outfile, level, namespace_, name_='route', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.route
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='StaticRouteEntriesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('route=[\n')
        level += 1
        for route_ in self.route:
            showIndent(outfile, level)
            outfile.write('model_.StaticRouteType(\n')
            route_.exportLiteral(outfile, level, name_='StaticRouteType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='StaticRouteEntriesType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'route':
            obj_ = StaticRouteType.factory()
            obj_.build(child_)
            self.route.append(obj_)
# end class StaticRouteEntriesType


class ProtocolBgpType(GeneratedsSuper):
    """
    ProtocolBgpType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if ProtocolBgpType.subclass:
            return ProtocolBgpType.subclass(*args_, **kwargs_)
        else:
            return ProtocolBgpType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ProtocolBgpType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ProtocolBgpType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ProtocolBgpType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ProtocolBgpType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ProtocolBgpType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='ProtocolBgpType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ProtocolBgpType


class ProtocolOspfType(GeneratedsSuper):
    """
    ProtocolOspfType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, area=None, **kwargs):
        self.area = area
    def factory(*args_, **kwargs_):
        if ProtocolOspfType.subclass:
            return ProtocolOspfType.subclass(*args_, **kwargs_)
        else:
            return ProtocolOspfType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_area(self): return self.area
    def set_area(self, area): self.area = area
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.area == other.area)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_area (obj.populate_integer ("area"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ProtocolOspfType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ProtocolOspfType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ProtocolOspfType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ProtocolOspfType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.area is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sarea>%s</%sarea>%s' % (namespace_, self.gds_format_integer(self.area, input_name='area'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.area is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ProtocolOspfType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.area is not None:
            showIndent(outfile, level)
            outfile.write('area=%d,\n' % self.area)
    def exportDict(self, name_='ProtocolOspfType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'area':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError), exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'area')
            self.area = ival_
# end class ProtocolOspfType


class ProtocolStaticType(GeneratedsSuper):
    """
    ProtocolStaticType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, route=None, **kwargs):
        if (route is None) or (route == []):
            self.route = []
        else:
            self.route = route
    def factory(*args_, **kwargs_):
        if ProtocolStaticType.subclass:
            return ProtocolStaticType.subclass(*args_, **kwargs_)
        else:
            return ProtocolStaticType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_route(self): return self.route
    def set_route(self, route): self.route = route
    def add_route(self, value): self.route.append(value)
    def insert_route(self, index, value): self.route[index] = value
    def delete_route(self, value): self.route.remove(value)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.route == other.route)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_route ([obj.populate_string ("route")])
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ProtocolStaticType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ProtocolStaticType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ProtocolStaticType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ProtocolStaticType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for route_ in self.route:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sroute>%s</%sroute>%s' % (namespace_, self.gds_format_string(quote_xml(route_).encode(ExternalEncoding), input_name='route'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.route
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ProtocolStaticType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('route=[\n')
        level += 1
        for route_ in self.route:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(route_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportDict(self, name_='ProtocolStaticType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'route':
            route_ = child_.text
            route_ = self.gds_validate_string(route_, node, 'route')
            self.route.append(route_)
# end class ProtocolStaticType


class ConnectionType(GeneratedsSuper):
    """
    ConnectionType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if ConnectionType.subclass:
            return ConnectionType.subclass(*args_, **kwargs_)
        else:
            return ConnectionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='ConnectionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ConnectionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='ConnectionType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='ConnectionType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ConnectionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='ConnectionType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ConnectionType


class InstanceTargetType(GeneratedsSuper):
    """
    InstanceTargetType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, import_export=None, **kwargs):
        self.import_export = import_export
    def factory(*args_, **kwargs_):
        if InstanceTargetType.subclass:
            return InstanceTargetType.subclass(*args_, **kwargs_)
        else:
            return InstanceTargetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_import_export(self): return self.import_export
    def set_import_export(self, import_export): self.import_export = import_export
    def validate_ImportExportType(self, value):
        # Validate type ImportExportType, a restriction on xsd:string.
        error = False
        if isinstance(value, list):
            error = set(value) - set([u'import', u'export'])
        else:
            error = value not in [u'import', u'export']
        if error:
            raise ValueError("ImportExportType must be one of [u'import', u'export']")
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.import_export == other.import_export)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_import_export (obj.populate_string ("import_export"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='InstanceTargetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='InstanceTargetType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='InstanceTargetType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='InstanceTargetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.import_export is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%simport-export>%s</%simport-export>%s' % (namespace_, self.gds_format_string(quote_xml(self.import_export).encode(ExternalEncoding), input_name='import-export'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.import_export is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='InstanceTargetType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.import_export is not None:
            showIndent(outfile, level)
            outfile.write('import_export=%s,\n' % quote_python(self.import_export).encode(ExternalEncoding))
    def exportDict(self, name_='InstanceTargetType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'import-export':
            import_export_ = child_.text
            import_export_ = self.gds_validate_string(import_export_, node, 'import_export')
            self.import_export = import_export_
            self.validate_ImportExportType(self.import_export)    # validate type ImportExportType
# end class InstanceTargetType


class DefaultProtocolType(GeneratedsSuper):
    """
    DefaultProtocolType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, bgp=None, ospf=None, **kwargs):
        if isinstance(bgp, dict):
            obj = ProtocolBgpType(**bgp)
            self.bgp = obj
        else:
            self.bgp = bgp
        if isinstance(ospf, dict):
            obj = ProtocolOspfType(**ospf)
            self.ospf = obj
        else:
            self.ospf = ospf
    def factory(*args_, **kwargs_):
        if DefaultProtocolType.subclass:
            return DefaultProtocolType.subclass(*args_, **kwargs_)
        else:
            return DefaultProtocolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_bgp(self): return self.bgp
    def set_bgp(self, bgp): self.bgp = bgp
    def get_ospf(self): return self.ospf
    def set_ospf(self, ospf): self.ospf = ospf
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.bgp == other.bgp and
                self.ospf == other.ospf)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_bgp (ProtocolBgpType.populate ())
        obj.set_ospf (ProtocolOspfType.populate ())
        return obj
    def export(self, outfile, level=1, namespace_='', name_='DefaultProtocolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DefaultProtocolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='DefaultProtocolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='DefaultProtocolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.bgp is not None:
            self.bgp.export(outfile, level, namespace_, name_='bgp', pretty_print=pretty_print)
        if self.ospf is not None:
            self.ospf.export(outfile, level, namespace_, name_='ospf', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.bgp is not None or
            self.ospf is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DefaultProtocolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.bgp is not None:
            showIndent(outfile, level)
            outfile.write('bgp=model_.ProtocolBgpType(\n')
            self.bgp.exportLiteral(outfile, level, name_='bgp')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ospf is not None:
            showIndent(outfile, level)
            outfile.write('ospf=model_.ProtocolOspfType(\n')
            self.ospf.exportLiteral(outfile, level, name_='ospf')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportDict(self, name_='DefaultProtocolType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'bgp':
            obj_ = ProtocolBgpType.factory()
            obj_.build(child_)
            self.set_bgp(obj_)
        elif nodeName_ == 'ospf':
            obj_ = ProtocolOspfType.factory()
            obj_.build(child_)
            self.set_ospf(obj_)
# end class DefaultProtocolType


class BindingType(GeneratedsSuper):
    """
    BindingType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if BindingType.subclass:
            return BindingType.subclass(*args_, **kwargs_)
        else:
            return BindingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='BindingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BindingType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BindingType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='BindingType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='BindingType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='BindingType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class BindingType


class AttachmentAddressType(GeneratedsSuper):
    """
    AttachmentAddressType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, **kwargs):
        pass
    def factory(*args_, **kwargs_):
        if AttachmentAddressType.subclass:
            return AttachmentAddressType.subclass(*args_, **kwargs_)
        else:
            return AttachmentAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def __eq__(self, other): return True
    def __ne__(self, other): return False
    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AttachmentAddressType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AttachmentAddressType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AttachmentAddressType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AttachmentAddressType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AttachmentAddressType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportDict(self, name_='AttachmentAddressType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AttachmentAddressType


class AttachmentInfoType(GeneratedsSuper):
    """
    AttachmentInfoType class definition from :doc:`vnc_cfg.xsd`
    """
    subclass = None
    superclass = None
    def __init__(self, static=None, bgp=None, ospf=None, state=None, **kwargs):
        if isinstance(static, dict):
            obj = ProtocolStaticType(**static)
            self.static = obj
        else:
            self.static = static
        if isinstance(bgp, dict):
            obj = ProtocolBgpType(**bgp)
            self.bgp = obj
        else:
            self.bgp = bgp
        if isinstance(ospf, dict):
            obj = ProtocolOspfType(**ospf)
            self.ospf = obj
        else:
            self.ospf = ospf
        self.state = state
    def factory(*args_, **kwargs_):
        if AttachmentInfoType.subclass:
            return AttachmentInfoType.subclass(*args_, **kwargs_)
        else:
            return AttachmentInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_static(self): return self.static
    def set_static(self, static): self.static = static
    def get_bgp(self): return self.bgp
    def set_bgp(self, bgp): self.bgp = bgp
    def get_ospf(self): return self.ospf
    def set_ospf(self, ospf): self.ospf = ospf
    def get_state(self): return self.state
    def set_state(self, state): self.state = state
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.static == other.static and
                self.bgp == other.bgp and
                self.ospf == other.ospf and
                self.state == other.state)
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    @classmethod
    def populate (cls, *a, **kwa):
        obj = cls (*a, **kwa)
        obj.set_static (ProtocolStaticType.populate ())
        obj.set_bgp (ProtocolBgpType.populate ())
        obj.set_ospf (ProtocolOspfType.populate ())
        obj.set_state (obj.populate_string ("state"))
        return obj
    def export(self, outfile, level=1, namespace_='', name_='AttachmentInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AttachmentInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='AttachmentInfoType'):
        pass
    def exportChildren(self, outfile, level, namespace_='', name_='AttachmentInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.static is not None:
            self.static.export(outfile, level, namespace_, name_='static', pretty_print=pretty_print)
        if self.bgp is not None:
            self.bgp.export(outfile, level, namespace_, name_='bgp', pretty_print=pretty_print)
        if self.ospf is not None:
            self.ospf.export(outfile, level, namespace_, name_='ospf', pretty_print=pretty_print)
        if self.state is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstate>%s</%sstate>%s' % (namespace_, self.gds_format_string(quote_xml(self.state).encode(ExternalEncoding), input_name='state'), namespace_, eol_))
    def hasContent_(self):
        if (
            self.static is not None or
            self.bgp is not None or
            self.ospf is not None or
            self.state is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AttachmentInfoType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.static is not None:
            showIndent(outfile, level)
            outfile.write('static=model_.ProtocolStaticType(\n')
            self.static.exportLiteral(outfile, level, name_='static')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.bgp is not None:
            showIndent(outfile, level)
            outfile.write('bgp=model_.ProtocolBgpType(\n')
            self.bgp.exportLiteral(outfile, level, name_='bgp')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.ospf is not None:
            showIndent(outfile, level)
            outfile.write('ospf=model_.ProtocolOspfType(\n')
            self.ospf.exportLiteral(outfile, level, name_='ospf')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.state is not None:
            showIndent(outfile, level)
            outfile.write('state=%s,\n' % quote_python(self.state).encode(ExternalEncoding))
    def exportDict(self, name_='AttachmentInfoType'):
        obj_json = json.dumps(self, default=lambda o: dict((k, v) for k, v in o.__dict__.iteritems()))
        obj_dict = json.loads(obj_json)
        return {name_: obj_dict}
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'static':
            obj_ = ProtocolStaticType.factory()
            obj_.build(child_)
            self.set_static(obj_)
        elif nodeName_ == 'bgp':
            obj_ = ProtocolBgpType.factory()
            obj_.build(child_)
            self.set_bgp(obj_)
        elif nodeName_ == 'ospf':
            obj_ = ProtocolOspfType.factory()
            obj_.build(child_)
            self.set_ospf(obj_)
        elif nodeName_ == 'state':
            state_ = child_.text
            state_ = self.gds_validate_string(state_, node, 'state')
            self.state = state_
# end class AttachmentInfoType



__all__ = [
    "AclEntriesType",
    "AclRuleType",
    "ActionListType",
    "AddressFamilies",
    "AddressType",
    "AllocationPoolType",
    "AllowedAddressPair",
    "AllowedAddressPairs",
    "ApiAccessListType",
    "ApiAccessType",
    "AttachmentAddressType",
    "AttachmentInfoType",
    "AuthenticationData",
    "AuthenticationKeyItem",
    "BgpPeeringAttributes",
    "BgpRouterParams",
    "BgpSession",
    "BgpSessionAttributes",
    "BindingType",
    "ConnectionType",
    "DefaultProtocolType",
    "DhcpOptionType",
    "DhcpOptionsListType",
    "DomainLimitsType",
    "EncapsulationPrioritiesType",
    "FloatingIpPoolType",
    "IdPermsType",
    "InstanceTargetType",
    "InterfaceMirrorType",
    "IpAddressesType",
    "IpamDnsAddressType",
    "IpamSubnetType",
    "IpamType",
    "JunosServicePorts",
    "KeyValuePair",
    "KeyValuePairs",
    "LinklocalServiceEntryType",
    "LinklocalServicesTypes",
    "LoadbalancerHealthmonitorType",
    "LoadbalancerMemberType",
    "LoadbalancerPoolType",
    "MacAddressesType",
    "MatchConditionType",
    "MirrorActionType",
    "PermType",
    "PluginProperties",
    "PluginProperty",
    "PolicyBasedForwardingRuleType",
    "PolicyEntriesType",
    "PolicyRuleType",
    "PortType",
    "ProtocolBgpType",
    "ProtocolOspfType",
    "ProtocolStaticType",
    "QuotaType",
    "RouteTableType",
    "RouteTargetList",
    "RouteType",
    "SNMPCredentials",
    "SequenceType",
    "ServiceChainInfo",
    "ServiceInstanceInterfaceType",
    "ServiceInstanceType",
    "ServiceScaleOutType",
    "ServiceTemplateInterfaceType",
    "ServiceTemplateType",
    "StaticRouteEntriesType",
    "StaticRouteType",
    "SubnetListType",
    "SubnetType",
    "TimerType",
    "UserCredentials",
    "UuidType",
    "VirtualDnsRecordType",
    "VirtualDnsType",
    "VirtualIpType",
    "VirtualMachineInterfacePropertiesType",
    "VirtualNetworkPolicyType",
    "VirtualNetworkType",
    "VnSubnetsType",
    "VrfAssignRuleType",
    "VrfAssignTableType",
    "config_root_domain",
    "config_root_global_system_config",
    "customer_attachment_floating_ip",
    "customer_attachment_virtual_machine_interface",
    "domain_namespace",
    "domain_project",
    "domain_service_template",
    "domain_virtual_DNS",
    "floating_ip_pool_floating_ip",
    "floating_ip_project",
    "floating_ip_virtual_machine_interface",
    "global_system_config_analytics_node",
    "global_system_config_bgp_router",
    "global_system_config_config_node",
    "global_system_config_database_node",
    "global_system_config_global_vrouter_config",
    "global_system_config_physical_router",
    "global_system_config_service_appliance_set",
    "global_system_config_virtual_router",
    "instance_bgp_router",
    "instance_ip_virtual_machine_interface",
    "instance_ip_virtual_network",
    "loadbalancer_pool_loadbalancer_healthmonitor",
    "loadbalancer_pool_loadbalancer_member",
    "loadbalancer_pool_service_appliance_set",
    "loadbalancer_pool_service_instance",
    "loadbalancer_pool_virtual_machine_interface",
    "logical_interface_virtual_machine_interface",
    "logical_router_gateway",
    "logical_router_interface",
    "logical_router_service_instance",
    "logical_router_target",
    "network_ipam_virtual_DNS",
    "physical_interface_logical_interface",
    "physical_router_bgp_router",
    "physical_router_logical_interface",
    "physical_router_physical_interface",
    "physical_router_virtual_network",
    "physical_router_virtual_router",
    "project_floating_ip_pool",
    "project_interface_route_table",
    "project_loadbalancer_healthmonitor",
    "project_loadbalancer_pool",
    "project_logical_router",
    "project_network_ipam",
    "project_network_policy",
    "project_qos_forwarding_class",
    "project_qos_queue",
    "project_route_table",
    "project_security_group",
    "project_service_instance",
    "project_virtual_ip",
    "project_virtual_machine_interface",
    "project_virtual_network",
    "provider_attachment_virtual_router",
    "qos_forwarding_class_qos_queue",
    "security_group_access_control_list",
    "service_appliance_set_service_appliance",
    "service_instance_service_template",
    "subnet_virtual_machine_interface",
    "virtual_DNS_virtual_DNS_record",
    "virtual_ip_loadbalancer_pool",
    "virtual_ip_virtual_machine_interface",
    "virtual_machine_interface_qos_forwarding_class",
    "virtual_machine_interface_route_table",
    "virtual_machine_interface_security_group",
    "virtual_machine_interface_sub_interface",
    "virtual_machine_interface_virtual_machine",
    "virtual_machine_interface_virtual_network",
    "virtual_machine_service_instance",
    "virtual_machine_virtual_machine_interface",
    "virtual_network_access_control_list",
    "virtual_network_floating_ip_pool",
    "virtual_network_qos_forwarding_class",
    "virtual_network_route_table",
    "virtual_network_routing_instance",
    "virtual_router_bgp_router",
    "virtual_router_virtual_machine"
    ]
