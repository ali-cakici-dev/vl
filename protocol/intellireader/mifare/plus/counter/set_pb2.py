# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mifare/plus/counter/set.proto

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
  name='mifare/plus/counter/set.proto',
  package='mifare.plus.counter.set',
  syntax='proto2',
  serialized_pb=_b('\n\x1dmifare/plus/counter/set.proto\x12\x17mifare.plus.counter.set\".\n\nSetCounter\x12\x11\n\tdst_block\x18\x01 \x02(\r\x12\r\n\x05value\x18\x02 \x02(\x05')
)




_SETCOUNTER = _descriptor.Descriptor(
  name='SetCounter',
  full_name='mifare.plus.counter.set.SetCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dst_block', full_name='mifare.plus.counter.set.SetCounter.dst_block', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='mifare.plus.counter.set.SetCounter.value', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['SetCounter'] = _SETCOUNTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetCounter = _reflection.GeneratedProtocolMessageType('SetCounter', (_message.Message,), dict(
  DESCRIPTOR = _SETCOUNTER,
  __module__ = 'mifare.plus.counter.set_pb2'
  # @@protoc_insertion_point(class_scope:mifare.plus.counter.set.SetCounter)
  ))
_sym_db.RegisterMessage(SetCounter)


# @@protoc_insertion_point(module_scope)