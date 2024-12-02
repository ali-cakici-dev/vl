# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gui/alignment.proto

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
  name='gui/alignment.proto',
  package='gui.alignment',
  syntax='proto2',
  serialized_pb=_b('\n\x13gui/alignment.proto\x12\rgui.alignment*W\n\x11VerticalAlignment\x12\x15\n\x11\x43\x45NTER_VERTICALLY\x10\x00\x12\n\n\x06\x42OTTOM\x10\x01\x12\x07\n\x03TOP\x10\x02\x12\x16\n\x12OPTIMAL_VERTICALLY\x10\x03*]\n\x13HorizontalAlignment\x12\x17\n\x13\x43\x45NTER_HORIZONTALLY\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x12\x18\n\x14OPTIMAL_HORIZONTALLY\x10\x03')
)

_VERTICALALIGNMENT = _descriptor.EnumDescriptor(
  name='VerticalAlignment',
  full_name='gui.alignment.VerticalAlignment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CENTER_VERTICALLY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOTTOM', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPTIMAL_VERTICALLY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=38,
  serialized_end=125,
)
_sym_db.RegisterEnumDescriptor(_VERTICALALIGNMENT)

VerticalAlignment = enum_type_wrapper.EnumTypeWrapper(_VERTICALALIGNMENT)
_HORIZONTALALIGNMENT = _descriptor.EnumDescriptor(
  name='HorizontalAlignment',
  full_name='gui.alignment.HorizontalAlignment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CENTER_HORIZONTALLY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPTIMAL_HORIZONTALLY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=127,
  serialized_end=220,
)
_sym_db.RegisterEnumDescriptor(_HORIZONTALALIGNMENT)

HorizontalAlignment = enum_type_wrapper.EnumTypeWrapper(_HORIZONTALALIGNMENT)
CENTER_VERTICALLY = 0
BOTTOM = 1
TOP = 2
OPTIMAL_VERTICALLY = 3
CENTER_HORIZONTALLY = 0
LEFT = 1
RIGHT = 2
OPTIMAL_HORIZONTALLY = 3


DESCRIPTOR.enum_types_by_name['VerticalAlignment'] = _VERTICALALIGNMENT
DESCRIPTOR.enum_types_by_name['HorizontalAlignment'] = _HORIZONTALALIGNMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
