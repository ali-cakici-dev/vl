# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qrcode/qrcode_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from qrcode import code_raw_data_pb2 as qrcode_dot_code__raw__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qrcode/qrcode_event.proto',
  package='qrcode.event',
  syntax='proto2',
  serialized_pb=_b('\n\x19qrcode/qrcode_event.proto\x12\x0cqrcode.event\x1a\x1aqrcode/code_raw_data.proto\"I\n\x0bQrCodeEvent\x12\x31\n\x08raw_data\x18\x01 \x01(\x0b\x32\x1d.qrcode.code_raw_data.RawDataH\x00\x42\x07\n\x05\x65vent')
  ,
  dependencies=[qrcode_dot_code__raw__data__pb2.DESCRIPTOR,])




_QRCODEEVENT = _descriptor.Descriptor(
  name='QrCodeEvent',
  full_name='qrcode.event.QrCodeEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw_data', full_name='qrcode.event.QrCodeEvent.raw_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='event', full_name='qrcode.event.QrCodeEvent.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=71,
  serialized_end=144,
)

_QRCODEEVENT.fields_by_name['raw_data'].message_type = qrcode_dot_code__raw__data__pb2._RAWDATA
_QRCODEEVENT.oneofs_by_name['event'].fields.append(
  _QRCODEEVENT.fields_by_name['raw_data'])
_QRCODEEVENT.fields_by_name['raw_data'].containing_oneof = _QRCODEEVENT.oneofs_by_name['event']
DESCRIPTOR.message_types_by_name['QrCodeEvent'] = _QRCODEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QrCodeEvent = _reflection.GeneratedProtocolMessageType('QrCodeEvent', (_message.Message,), dict(
  DESCRIPTOR = _QRCODEEVENT,
  __module__ = 'qrcode.qrcode_event_pb2'
  # @@protoc_insertion_point(class_scope:qrcode.event.QrCodeEvent)
  ))
_sym_db.RegisterMessage(QrCodeEvent)


# @@protoc_insertion_point(module_scope)