# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qrcode/poll_for_qrcode.proto

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
  name='qrcode/poll_for_qrcode.proto',
  package='qrcode.poll',
  syntax='proto2',
  serialized_pb=_b('\n\x1cqrcode/poll_for_qrcode.proto\x12\x0bqrcode.poll\"V\n\rPollForQrCode\x12\x34\n\nevent_type\x18\x01 \x01(\x0e\x32\x16.qrcode.poll.EventType:\x08RAW_DATA\x12\x0f\n\x07timeout\x18\x02 \x01(\r*\x19\n\tEventType\x12\x0c\n\x08RAW_DATA\x10\x00')
)

_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='qrcode.poll.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW_DATA', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=133,
  serialized_end=158,
)
_sym_db.RegisterEnumDescriptor(_EVENTTYPE)

EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
RAW_DATA = 0



_POLLFORQRCODE = _descriptor.Descriptor(
  name='PollForQrCode',
  full_name='qrcode.poll.PollForQrCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_type', full_name='qrcode.poll.PollForQrCode.event_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='qrcode.poll.PollForQrCode.timeout', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=45,
  serialized_end=131,
)

_POLLFORQRCODE.fields_by_name['event_type'].enum_type = _EVENTTYPE
DESCRIPTOR.message_types_by_name['PollForQrCode'] = _POLLFORQRCODE
DESCRIPTOR.enum_types_by_name['EventType'] = _EVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PollForQrCode = _reflection.GeneratedProtocolMessageType('PollForQrCode', (_message.Message,), dict(
  DESCRIPTOR = _POLLFORQRCODE,
  __module__ = 'qrcode.poll_for_qrcode_pb2'
  # @@protoc_insertion_point(class_scope:qrcode.poll.PollForQrCode)
  ))
_sym_db.RegisterMessage(PollForQrCode)


# @@protoc_insertion_point(module_scope)
