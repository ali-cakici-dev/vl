# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: misc/leds.proto

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
  name='misc/leds.proto',
  package='misc.leds',
  syntax='proto2',
  serialized_pb=_b('\n\x0fmisc/leds.proto\x12\tmisc.leds\"W\n\x04Leds\x12\x0c\n\x04\x62lue\x18\x01 \x01(\x08\x12\x0e\n\x06yellow\x18\x02 \x01(\x08\x12\r\n\x05green\x18\x03 \x01(\x08\x12\x0b\n\x03red\x18\x04 \x01(\x08\x12\x15\n\rlcd_backlight\x18\x05 \x01(\x08')
)




_LEDS = _descriptor.Descriptor(
  name='Leds',
  full_name='misc.leds.Leds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blue', full_name='misc.leds.Leds.blue', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yellow', full_name='misc.leds.Leds.yellow', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='green', full_name='misc.leds.Leds.green', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='red', full_name='misc.leds.Leds.red', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lcd_backlight', full_name='misc.leds.Leds.lcd_backlight', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=30,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['Leds'] = _LEDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Leds = _reflection.GeneratedProtocolMessageType('Leds', (_message.Message,), dict(
  DESCRIPTOR = _LEDS,
  __module__ = 'misc.leds_pb2'
  # @@protoc_insertion_point(class_scope:misc.leds.Leds)
  ))
_sym_db.RegisterMessage(Leds)


# @@protoc_insertion_point(module_scope)