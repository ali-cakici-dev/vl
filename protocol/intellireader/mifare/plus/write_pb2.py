# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mifare/plus/write.proto

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
  name='mifare/plus/write.proto',
  package='mifare.plus.write',
  syntax='proto2',
  serialized_pb=_b('\n\x17mifare/plus/write.proto\x12\x11mifare.plus.write\"0\n\x0bWriteBlocks\x12\x13\n\x0bstart_block\x18\x01 \x02(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c')
)




_WRITEBLOCKS = _descriptor.Descriptor(
  name='WriteBlocks',
  full_name='mifare.plus.write.WriteBlocks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_block', full_name='mifare.plus.write.WriteBlocks.start_block', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mifare.plus.write.WriteBlocks.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
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
  serialized_start=46,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['WriteBlocks'] = _WRITEBLOCKS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteBlocks = _reflection.GeneratedProtocolMessageType('WriteBlocks', (_message.Message,), dict(
  DESCRIPTOR = _WRITEBLOCKS,
  __module__ = 'mifare.plus.write_pb2'
  # @@protoc_insertion_point(class_scope:mifare.plus.write.WriteBlocks)
  ))
_sym_db.RegisterMessage(WriteBlocks)


# @@protoc_insertion_point(module_scope)
