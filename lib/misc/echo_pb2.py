# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: misc/echo.proto

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
  name='misc/echo.proto',
  package='misc.echo',
  syntax='proto2',
  serialized_pb=_b('\n\x0fmisc/echo.proto\x12\tmisc.echo\"G\n\x07GetEcho\x12\x1a\n\x0csend_pending\x18\x01 \x01(\x08:\x04true\x12\x12\n\nreply_size\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\x14\n\x04\x45\x63ho\x12\x0c\n\x04\x65\x63ho\x18\x01 \x01(\x0c')
)




_GETECHO = _descriptor.Descriptor(
  name='GetEcho',
  full_name='misc.echo.GetEcho',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='send_pending', full_name='misc.echo.GetEcho.send_pending', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reply_size', full_name='misc.echo.GetEcho.reply_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='misc.echo.GetEcho.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=30,
  serialized_end=101,
)


_ECHO = _descriptor.Descriptor(
  name='Echo',
  full_name='misc.echo.Echo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='echo', full_name='misc.echo.Echo.echo', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=103,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['GetEcho'] = _GETECHO
DESCRIPTOR.message_types_by_name['Echo'] = _ECHO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetEcho = _reflection.GeneratedProtocolMessageType('GetEcho', (_message.Message,), dict(
  DESCRIPTOR = _GETECHO,
  __module__ = 'misc.echo_pb2'
  # @@protoc_insertion_point(class_scope:misc.echo.GetEcho)
  ))
_sym_db.RegisterMessage(GetEcho)

Echo = _reflection.GeneratedProtocolMessageType('Echo', (_message.Message,), dict(
  DESCRIPTOR = _ECHO,
  __module__ = 'misc.echo_pb2'
  # @@protoc_insertion_point(class_scope:misc.echo.Echo)
  ))
_sym_db.RegisterMessage(Echo)


# @@protoc_insertion_point(module_scope)