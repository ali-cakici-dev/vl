# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mifare/plus/sector.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mifare/plus/sector.proto',
  package='mifare.plus.sector',
  syntax='proto2',
  serialized_pb=_b('\n\x18mifare/plus/sector.proto\x12\x12mifare.plus.sector*\'\n\rSectorKeyType\x12\n\n\x06TYPE_A\x10\x00\x12\n\n\x06TYPE_B\x10\x01')
)

_SECTORKEYTYPE = _descriptor.EnumDescriptor(
  name='SectorKeyType',
  full_name='mifare.plus.sector.SectorKeyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_A', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE_B', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=48,
  serialized_end=87,
)
_sym_db.RegisterEnumDescriptor(_SECTORKEYTYPE)

SectorKeyType = enum_type_wrapper.EnumTypeWrapper(_SECTORKEYTYPE)
TYPE_A = 0
TYPE_B = 1


DESCRIPTOR.enum_types_by_name['SectorKeyType'] = _SECTORKEYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
