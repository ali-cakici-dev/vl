# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mifare/av2/channel.proto

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
  name='mifare/av2/channel.proto',
  package='mifare.av2.channel',
  syntax='proto2',
  serialized_pb=_b('\n\x18mifare/av2/channel.proto\x12\x12mifare.av2.channel*U\n\x07\x43hannel\x12\x11\n\rAV2_CHANNEL_0\x10\x00\x12\x11\n\rAV2_CHANNEL_1\x10\x01\x12\x11\n\rAV2_CHANNEL_2\x10\x02\x12\x11\n\rAV2_CHANNEL_3\x10\x03')
)

_CHANNEL = _descriptor.EnumDescriptor(
  name='Channel',
  full_name='mifare.av2.channel.Channel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AV2_CHANNEL_0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AV2_CHANNEL_1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AV2_CHANNEL_2', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AV2_CHANNEL_3', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=48,
  serialized_end=133,
)
_sym_db.RegisterEnumDescriptor(_CHANNEL)

Channel = enum_type_wrapper.EnumTypeWrapper(_CHANNEL)
AV2_CHANNEL_0 = 0
AV2_CHANNEL_1 = 1
AV2_CHANNEL_2 = 2
AV2_CHANNEL_3 = 3


DESCRIPTOR.enum_types_by_name['Channel'] = _CHANNEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
