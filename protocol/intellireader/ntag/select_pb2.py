# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ntag/select.proto

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
  name='ntag/select.proto',
  package='ntag.select',
  syntax='proto2',
  serialized_pb=_b('\n\x11ntag/select.proto\x12\x0bntag.select\"=\n\nSelectFile\x12/\n\x04\x66ile\x18\x01 \x01(\x0e\x32\x14.ntag.select.IsoFile:\x0b\x41PPLICATION*$\n\x07IsoFile\x12\x0f\n\x0b\x41PPLICATION\x10\x00\x12\x08\n\x04PICC\x10\x01')
)

_ISOFILE = _descriptor.EnumDescriptor(
  name='IsoFile',
  full_name='ntag.select.IsoFile',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APPLICATION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICC', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=97,
  serialized_end=133,
)
_sym_db.RegisterEnumDescriptor(_ISOFILE)

IsoFile = enum_type_wrapper.EnumTypeWrapper(_ISOFILE)
APPLICATION = 0
PICC = 1



_SELECTFILE = _descriptor.Descriptor(
  name='SelectFile',
  full_name='ntag.select.SelectFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='ntag.select.SelectFile.file', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=34,
  serialized_end=95,
)

_SELECTFILE.fields_by_name['file'].enum_type = _ISOFILE
DESCRIPTOR.message_types_by_name['SelectFile'] = _SELECTFILE
DESCRIPTOR.enum_types_by_name['IsoFile'] = _ISOFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SelectFile = _reflection.GeneratedProtocolMessageType('SelectFile', (_message.Message,), dict(
  DESCRIPTOR = _SELECTFILE,
  __module__ = 'ntag.select_pb2'
  # @@protoc_insertion_point(class_scope:ntag.select.SelectFile)
  ))
_sym_db.RegisterMessage(SelectFile)


# @@protoc_insertion_point(module_scope)