# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ntag/comm.proto

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
  name='ntag/comm.proto',
  package='ntag.comm',
  syntax='proto2',
  serialized_pb=_b('\n\x0fntag/comm.proto\x12\tntag.comm*K\n\nProtection\x12\x16\n\x12\x45NCRYPTED_WITH_MAC\x10\x00\x12\x16\n\x12PLAINTEXT_WITH_MAC\x10\x01\x12\r\n\tPLAINTEXT\x10\x02')
)

_PROTECTION = _descriptor.EnumDescriptor(
  name='Protection',
  full_name='ntag.comm.Protection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENCRYPTED_WITH_MAC', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAINTEXT_WITH_MAC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAINTEXT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=30,
  serialized_end=105,
)
_sym_db.RegisterEnumDescriptor(_PROTECTION)

Protection = enum_type_wrapper.EnumTypeWrapper(_PROTECTION)
ENCRYPTED_WITH_MAC = 0
PLAINTEXT_WITH_MAC = 1
PLAINTEXT = 2


DESCRIPTOR.enum_types_by_name['Protection'] = _PROTECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
