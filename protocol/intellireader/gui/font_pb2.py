# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gui/font.proto

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
  name='gui/font.proto',
  package='gui.font',
  syntax='proto2',
  serialized_pb=_b('\n\x0egui/font.proto\x12\x08gui.font*<\n\x04\x46ont\x12\x10\n\x0cREGULAR_FONT\x10\x00\x12\x0e\n\nLARGE_FONT\x10\x01\x12\x12\n\x0eMONOSPACE_FONT\x10\x02')
)

_FONT = _descriptor.EnumDescriptor(
  name='Font',
  full_name='gui.font.Font',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGULAR_FONT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LARGE_FONT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONOSPACE_FONT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=28,
  serialized_end=88,
)
_sym_db.RegisterEnumDescriptor(_FONT)

Font = enum_type_wrapper.EnumTypeWrapper(_FONT)
REGULAR_FONT = 0
LARGE_FONT = 1
MONOSPACE_FONT = 2


DESCRIPTOR.enum_types_by_name['Font'] = _FONT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
