# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: misc/lan_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='misc/lan_settings.proto',
  package='misc.lan_settings',
  syntax='proto2',
  serialized_pb=_b('\n\x17misc/lan_settings.proto\x12\x11misc.lan_settings\"I\n\x11\x43hangeLanSettings\x12\x34\n\x0clan_settings\x18\x01 \x02(\x0b\x32\x1e.misc.lan_settings.LanSettings\"z\n\x0bLanSettings\x12\'\n\x04\x64hcp\x18\x01 \x01(\x0b\x32\x17.misc.lan_settings.DhcpH\x00\x12\x33\n\x06manual\x18\x02 \x01(\x0b\x32!.misc.lan_settings.ManualSettingsH\x00\x42\r\n\x0bipv4_method\"\x06\n\x04\x44hcp\"I\n\x0eManualSettings\x12\x15\n\rlocal_address\x18\x01 \x02(\t\x12\x0f\n\x07netmask\x18\x02 \x02(\t\x12\x0f\n\x07gateway\x18\x03 \x02(\t')
)




_CHANGELANSETTINGS = _descriptor.Descriptor(
  name='ChangeLanSettings',
  full_name='misc.lan_settings.ChangeLanSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lan_settings', full_name='misc.lan_settings.ChangeLanSettings.lan_settings', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=119,
)


_LANSETTINGS = _descriptor.Descriptor(
  name='LanSettings',
  full_name='misc.lan_settings.LanSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dhcp', full_name='misc.lan_settings.LanSettings.dhcp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manual', full_name='misc.lan_settings.LanSettings.manual', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ipv4_method', full_name='misc.lan_settings.LanSettings.ipv4_method',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=121,
  serialized_end=243,
)


_DHCP = _descriptor.Descriptor(
  name='Dhcp',
  full_name='misc.lan_settings.Dhcp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=251,
)


_MANUALSETTINGS = _descriptor.Descriptor(
  name='ManualSettings',
  full_name='misc.lan_settings.ManualSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_address', full_name='misc.lan_settings.ManualSettings.local_address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netmask', full_name='misc.lan_settings.ManualSettings.netmask', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='misc.lan_settings.ManualSettings.gateway', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=326,
)

_CHANGELANSETTINGS.fields_by_name['lan_settings'].message_type = _LANSETTINGS
_LANSETTINGS.fields_by_name['dhcp'].message_type = _DHCP
_LANSETTINGS.fields_by_name['manual'].message_type = _MANUALSETTINGS
_LANSETTINGS.oneofs_by_name['ipv4_method'].fields.append(
  _LANSETTINGS.fields_by_name['dhcp'])
_LANSETTINGS.fields_by_name['dhcp'].containing_oneof = _LANSETTINGS.oneofs_by_name['ipv4_method']
_LANSETTINGS.oneofs_by_name['ipv4_method'].fields.append(
  _LANSETTINGS.fields_by_name['manual'])
_LANSETTINGS.fields_by_name['manual'].containing_oneof = _LANSETTINGS.oneofs_by_name['ipv4_method']
DESCRIPTOR.message_types_by_name['ChangeLanSettings'] = _CHANGELANSETTINGS
DESCRIPTOR.message_types_by_name['LanSettings'] = _LANSETTINGS
DESCRIPTOR.message_types_by_name['Dhcp'] = _DHCP
DESCRIPTOR.message_types_by_name['ManualSettings'] = _MANUALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeLanSettings = _reflection.GeneratedProtocolMessageType('ChangeLanSettings', (_message.Message,), dict(
  DESCRIPTOR = _CHANGELANSETTINGS,
  __module__ = 'misc.lan_settings_pb2'
  # @@protoc_insertion_point(class_scope:misc.lan_settings.ChangeLanSettings)
  ))
_sym_db.RegisterMessage(ChangeLanSettings)

LanSettings = _reflection.GeneratedProtocolMessageType('LanSettings', (_message.Message,), dict(
  DESCRIPTOR = _LANSETTINGS,
  __module__ = 'misc.lan_settings_pb2'
  # @@protoc_insertion_point(class_scope:misc.lan_settings.LanSettings)
  ))
_sym_db.RegisterMessage(LanSettings)

Dhcp = _reflection.GeneratedProtocolMessageType('Dhcp', (_message.Message,), dict(
  DESCRIPTOR = _DHCP,
  __module__ = 'misc.lan_settings_pb2'
  # @@protoc_insertion_point(class_scope:misc.lan_settings.Dhcp)
  ))
_sym_db.RegisterMessage(Dhcp)

ManualSettings = _reflection.GeneratedProtocolMessageType('ManualSettings', (_message.Message,), dict(
  DESCRIPTOR = _MANUALSETTINGS,
  __module__ = 'misc.lan_settings_pb2'
  # @@protoc_insertion_point(class_scope:misc.lan_settings.ManualSettings)
  ))
_sym_db.RegisterMessage(ManualSettings)


# @@protoc_insertion_point(module_scope)