# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: srv/diagnostic.proto

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
  name='srv/diagnostic.proto',
  package='srv.diagnostic',
  syntax='proto2',
  serialized_pb=_b('\n\x14srv/diagnostic.proto\x12\x0esrv.diagnostic\"\x0f\n\rGetDiagnostic\"\x84\x01\n\x0e\x44iagnosticInfo\x12\x11\n\tnfc_error\x18\x01 \x01(\t\x12\x11\n\tmcu_error\x18\x02 \x01(\t\x12\x19\n\x11touchscreen_error\x18\x03 \x01(\t\x12\x15\n\rstorage_error\x18\x04 \x01(\t\x12\x1a\n\x12last_reboot_reason\x18\x05 \x01(\t')
)




_GETDIAGNOSTIC = _descriptor.Descriptor(
  name='GetDiagnostic',
  full_name='srv.diagnostic.GetDiagnostic',
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
  serialized_start=40,
  serialized_end=55,
)


_DIAGNOSTICINFO = _descriptor.Descriptor(
  name='DiagnosticInfo',
  full_name='srv.diagnostic.DiagnosticInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nfc_error', full_name='srv.diagnostic.DiagnosticInfo.nfc_error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mcu_error', full_name='srv.diagnostic.DiagnosticInfo.mcu_error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='touchscreen_error', full_name='srv.diagnostic.DiagnosticInfo.touchscreen_error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_error', full_name='srv.diagnostic.DiagnosticInfo.storage_error', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_reboot_reason', full_name='srv.diagnostic.DiagnosticInfo.last_reboot_reason', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['GetDiagnostic'] = _GETDIAGNOSTIC
DESCRIPTOR.message_types_by_name['DiagnosticInfo'] = _DIAGNOSTICINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDiagnostic = _reflection.GeneratedProtocolMessageType('GetDiagnostic', (_message.Message,), dict(
  DESCRIPTOR = _GETDIAGNOSTIC,
  __module__ = 'srv.diagnostic_pb2'
  # @@protoc_insertion_point(class_scope:srv.diagnostic.GetDiagnostic)
  ))
_sym_db.RegisterMessage(GetDiagnostic)

DiagnosticInfo = _reflection.GeneratedProtocolMessageType('DiagnosticInfo', (_message.Message,), dict(
  DESCRIPTOR = _DIAGNOSTICINFO,
  __module__ = 'srv.diagnostic_pb2'
  # @@protoc_insertion_point(class_scope:srv.diagnostic.DiagnosticInfo)
  ))
_sym_db.RegisterMessage(DiagnosticInfo)


# @@protoc_insertion_point(module_scope)
