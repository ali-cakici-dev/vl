# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ntag/write.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ntag import file_pb2 as ntag_dot_file__pb2
from ntag import comm_pb2 as ntag_dot_comm__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ntag/write.proto',
  package='ntag.write',
  syntax='proto2',
  serialized_pb=_b('\n\x10ntag/write.proto\x12\nntag.write\x1a\x0fntag/file.proto\x1a\x0fntag/comm.proto\"w\n\tWriteFile\x12\x1d\n\x04\x66ile\x18\x01 \x02(\x0e\x32\x0f.ntag.file.File\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\x12=\n\nprotection\x18\x03 \x01(\x0e\x32\x15.ntag.comm.Protection:\x12\x45NCRYPTED_WITH_MAC')
  ,
  dependencies=[ntag_dot_file__pb2.DESCRIPTOR,ntag_dot_comm__pb2.DESCRIPTOR,])




_WRITEFILE = _descriptor.Descriptor(
  name='WriteFile',
  full_name='ntag.write.WriteFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='ntag.write.WriteFile.file', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ntag.write.WriteFile.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protection', full_name='ntag.write.WriteFile.protection', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=66,
  serialized_end=185,
)

_WRITEFILE.fields_by_name['file'].enum_type = ntag_dot_file__pb2._FILE
_WRITEFILE.fields_by_name['protection'].enum_type = ntag_dot_comm__pb2._PROTECTION
DESCRIPTOR.message_types_by_name['WriteFile'] = _WRITEFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteFile = _reflection.GeneratedProtocolMessageType('WriteFile', (_message.Message,), dict(
  DESCRIPTOR = _WRITEFILE,
  __module__ = 'ntag.write_pb2'
  # @@protoc_insertion_point(class_scope:ntag.write.WriteFile)
  ))
_sym_db.RegisterMessage(WriteFile)


# @@protoc_insertion_point(module_scope)