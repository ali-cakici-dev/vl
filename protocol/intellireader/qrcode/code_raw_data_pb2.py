# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qrcode/code_raw_data.proto

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
  name='qrcode/code_raw_data.proto',
  package='qrcode.code_raw_data',
  syntax='proto2',
  serialized_pb=_b('\n\x1aqrcode/code_raw_data.proto\x12\x14qrcode.code_raw_data\"\x17\n\x07RawData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c')
)




_RAWDATA = _descriptor.Descriptor(
  name='RawData',
  full_name='qrcode.code_raw_data.RawData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='qrcode.code_raw_data.RawData.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=52,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['RawData'] = _RAWDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RawData = _reflection.GeneratedProtocolMessageType('RawData', (_message.Message,), dict(
  DESCRIPTOR = _RAWDATA,
  __module__ = 'qrcode.code_raw_data_pb2'
  # @@protoc_insertion_point(class_scope:qrcode.code_raw_data.RawData)
  ))
_sym_db.RegisterMessage(RawData)


# @@protoc_insertion_point(module_scope)