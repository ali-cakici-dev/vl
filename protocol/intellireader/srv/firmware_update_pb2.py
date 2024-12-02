# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: srv/firmware_update.proto

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
  name='srv/firmware_update.proto',
  package='srv.firmware_update',
  syntax='proto2',
  serialized_pb=_b('\n\x19srv/firmware_update.proto\x12\x13srv.firmware_update\"&\n\x07Prepare\x12\x1b\n\x13\x66irmware_image_size\x18\x01 \x01(\r\"\x1b\n\x0bUpdateBlock\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"\x1f\n\x05\x41pply\x12\x16\n\x07restart\x18\x01 \x01(\x08:\x05\x66\x61lse\"\n\n\x08Rollback')
)




_PREPARE = _descriptor.Descriptor(
  name='Prepare',
  full_name='srv.firmware_update.Prepare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firmware_image_size', full_name='srv.firmware_update.Prepare.firmware_image_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=50,
  serialized_end=88,
)


_UPDATEBLOCK = _descriptor.Descriptor(
  name='UpdateBlock',
  full_name='srv.firmware_update.UpdateBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='srv.firmware_update.UpdateBlock.data', index=0,
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
  serialized_start=90,
  serialized_end=117,
)


_APPLY = _descriptor.Descriptor(
  name='Apply',
  full_name='srv.firmware_update.Apply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='restart', full_name='srv.firmware_update.Apply.restart', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=119,
  serialized_end=150,
)


_ROLLBACK = _descriptor.Descriptor(
  name='Rollback',
  full_name='srv.firmware_update.Rollback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=152,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['Prepare'] = _PREPARE
DESCRIPTOR.message_types_by_name['UpdateBlock'] = _UPDATEBLOCK
DESCRIPTOR.message_types_by_name['Apply'] = _APPLY
DESCRIPTOR.message_types_by_name['Rollback'] = _ROLLBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Prepare = _reflection.GeneratedProtocolMessageType('Prepare', (_message.Message,), dict(
  DESCRIPTOR = _PREPARE,
  __module__ = 'srv.firmware_update_pb2'
  # @@protoc_insertion_point(class_scope:srv.firmware_update.Prepare)
  ))
_sym_db.RegisterMessage(Prepare)

UpdateBlock = _reflection.GeneratedProtocolMessageType('UpdateBlock', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEBLOCK,
  __module__ = 'srv.firmware_update_pb2'
  # @@protoc_insertion_point(class_scope:srv.firmware_update.UpdateBlock)
  ))
_sym_db.RegisterMessage(UpdateBlock)

Apply = _reflection.GeneratedProtocolMessageType('Apply', (_message.Message,), dict(
  DESCRIPTOR = _APPLY,
  __module__ = 'srv.firmware_update_pb2'
  # @@protoc_insertion_point(class_scope:srv.firmware_update.Apply)
  ))
_sym_db.RegisterMessage(Apply)

Rollback = _reflection.GeneratedProtocolMessageType('Rollback', (_message.Message,), dict(
  DESCRIPTOR = _ROLLBACK,
  __module__ = 'srv.firmware_update_pb2'
  # @@protoc_insertion_point(class_scope:srv.firmware_update.Rollback)
  ))
_sym_db.RegisterMessage(Rollback)


# @@protoc_insertion_point(module_scope)
