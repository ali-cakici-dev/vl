# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mifare/ultralight/version.proto

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
  name='mifare/ultralight/version.proto',
  package='mifare.ultralight.version',
  syntax='proto2',
  serialized_pb=_b('\n\x1fmifare/ultralight/version.proto\x12\x19mifare.ultralight.version\"\x0c\n\nGetVersion\"#\n\x07Version\x12\x18\n\x10raw_version_data\x18\x01 \x02(\x0c')
)




_GETVERSION = _descriptor.Descriptor(
  name='GetVersion',
  full_name='mifare.ultralight.version.GetVersion',
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
  serialized_start=62,
  serialized_end=74,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='mifare.ultralight.version.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_version_data', full_name='mifare.ultralight.version.Version.raw_version_data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=76,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['GetVersion'] = _GETVERSION
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVersion = _reflection.GeneratedProtocolMessageType('GetVersion', (_message.Message,), dict(
  DESCRIPTOR = _GETVERSION,
  __module__ = 'mifare.ultralight.version_pb2'
  # @@protoc_insertion_point(class_scope:mifare.ultralight.version.GetVersion)
  ))
_sym_db.RegisterMessage(GetVersion)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), dict(
  DESCRIPTOR = _VERSION,
  __module__ = 'mifare.ultralight.version_pb2'
  # @@protoc_insertion_point(class_scope:mifare.ultralight.version.Version)
  ))
_sym_db.RegisterMessage(Version)


# @@protoc_insertion_point(module_scope)