# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: misc/ethernet.proto

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
  name='misc/ethernet.proto',
  package='misc.ethernet',
  syntax='proto2',
  serialized_pb=_b('\n\x13misc/ethernet.proto\x12\rmisc.ethernet\"\x86\x01\n\tStatistic\x12\'\n\x05port1\x18\x01 \x01(\x0b\x32\x18.misc.ethernet.PortStats\x12\'\n\x05port2\x18\x02 \x01(\x0b\x32\x18.misc.ethernet.PortStats\x12\'\n\x05port3\x18\x03 \x01(\x0b\x32\x18.misc.ethernet.PortStats\"\\\n\tPortStats\x12\x12\n\ntx_packets\x18\x01 \x02(\r\x12\x12\n\nrx_packets\x18\x02 \x02(\r\x12\x11\n\trx_errors\x18\x03 \x02(\r\x12\x14\n\x0ctxrx_dropped\x18\x04 \x02(\r')
)




_STATISTIC = _descriptor.Descriptor(
  name='Statistic',
  full_name='misc.ethernet.Statistic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port1', full_name='misc.ethernet.Statistic.port1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port2', full_name='misc.ethernet.Statistic.port2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port3', full_name='misc.ethernet.Statistic.port3', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=39,
  serialized_end=173,
)


_PORTSTATS = _descriptor.Descriptor(
  name='PortStats',
  full_name='misc.ethernet.PortStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_packets', full_name='misc.ethernet.PortStats.tx_packets', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx_packets', full_name='misc.ethernet.PortStats.rx_packets', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rx_errors', full_name='misc.ethernet.PortStats.rx_errors', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txrx_dropped', full_name='misc.ethernet.PortStats.txrx_dropped', index=3,
      number=4, type=13, cpp_type=3, label=2,
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
  serialized_start=175,
  serialized_end=267,
)

_STATISTIC.fields_by_name['port1'].message_type = _PORTSTATS
_STATISTIC.fields_by_name['port2'].message_type = _PORTSTATS
_STATISTIC.fields_by_name['port3'].message_type = _PORTSTATS
DESCRIPTOR.message_types_by_name['Statistic'] = _STATISTIC
DESCRIPTOR.message_types_by_name['PortStats'] = _PORTSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Statistic = _reflection.GeneratedProtocolMessageType('Statistic', (_message.Message,), dict(
  DESCRIPTOR = _STATISTIC,
  __module__ = 'misc.ethernet_pb2'
  # @@protoc_insertion_point(class_scope:misc.ethernet.Statistic)
  ))
_sym_db.RegisterMessage(Statistic)

PortStats = _reflection.GeneratedProtocolMessageType('PortStats', (_message.Message,), dict(
  DESCRIPTOR = _PORTSTATS,
  __module__ = 'misc.ethernet_pb2'
  # @@protoc_insertion_point(class_scope:misc.ethernet.PortStats)
  ))
_sym_db.RegisterMessage(PortStats)


# @@protoc_insertion_point(module_scope)
