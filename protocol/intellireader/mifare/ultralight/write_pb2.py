# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mifare/ultralight/write.proto

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
  name='mifare/ultralight/write.proto',
  package='mifare.ultralight.write',
  syntax='proto2',
  serialized_pb=_b('\n\x1dmifare/ultralight/write.proto\x12\x17mifare.ultralight.write\"1\n\nWritePages\x12\x15\n\rstart_address\x18\x01 \x02(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c')
)




_WRITEPAGES = _descriptor.Descriptor(
  name='WritePages',
  full_name='mifare.ultralight.write.WritePages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_address', full_name='mifare.ultralight.write.WritePages.start_address', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mifare.ultralight.write.WritePages.data', index=1,
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
  serialized_start=58,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['WritePages'] = _WRITEPAGES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WritePages = _reflection.GeneratedProtocolMessageType('WritePages', (_message.Message,), dict(
  DESCRIPTOR = _WRITEPAGES,
  __module__ = 'mifare.ultralight.write_pb2'
  # @@protoc_insertion_point(class_scope:mifare.ultralight.write.WritePages)
  ))
_sym_db.RegisterMessage(WritePages)


# @@protoc_insertion_point(module_scope)
