# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: touchscreen/coordinates.proto

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
  name='touchscreen/coordinates.proto',
  package='touchscreen.coordinates',
  syntax='proto2',
  serialized_pb=_b('\n\x1dtouchscreen/coordinates.proto\x12\x17touchscreen.coordinates\"#\n\x0b\x43oordinates\x12\t\n\x01x\x18\x01 \x02(\r\x12\t\n\x01y\x18\x02 \x02(\r')
)




_COORDINATES = _descriptor.Descriptor(
  name='Coordinates',
  full_name='touchscreen.coordinates.Coordinates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='touchscreen.coordinates.Coordinates.x', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='touchscreen.coordinates.Coordinates.y', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=58,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['Coordinates'] = _COORDINATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Coordinates = _reflection.GeneratedProtocolMessageType('Coordinates', (_message.Message,), dict(
  DESCRIPTOR = _COORDINATES,
  __module__ = 'touchscreen.coordinates_pb2'
  # @@protoc_insertion_point(class_scope:touchscreen.coordinates.Coordinates)
  ))
_sym_db.RegisterMessage(Coordinates)


# @@protoc_insertion_point(module_scope)