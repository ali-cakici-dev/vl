# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contactless/poll_for_token.proto

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
  name='contactless/poll_for_token.proto',
  package='contactless.poll',
  syntax='proto2',
  serialized_pb=_b('\n contactless/poll_for_token.proto\x12\x10\x63ontactless.poll\"\xaf\x02\n\x0cPollForToken\x12\x0f\n\x07timeout\x18\x01 \x01(\r\x12\x1c\n\rprefer_mifare\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fpoll_stm_sri512\x18\x03 \x01(\x08:\x05\x66\x61lse\x12H\n\x0cpolling_mode\x18\x04 \x01(\x0e\x32\x1d.contactless.poll.PollingMode:\x13POLLING_WITH_PAUSES\x12.\n\nenable_ecp\x18\x05 \x01(\x0e\x32\x1a.contactless.poll.AppleEcp\x12\x1b\n\x0clight_up_led\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\rpoll_iso15693\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0cpoll_ask_cts\x18\x08 \x01(\x08:\x05\x66\x61lse*T\n\x0bPollingMode\x12\x17\n\x13POLLING_WITH_PAUSES\x10\x01\x12\x15\n\x11\x43ONTINOUS_POLLING\x10\x02\x12\x15\n\x11LOW_POWER_POLLING\x10\x03*\x1d\n\x08\x41ppleEcp\x12\x11\n\rRUSSIA_MOSCOW\x10\x00')
)

_POLLINGMODE = _descriptor.EnumDescriptor(
  name='PollingMode',
  full_name='contactless.poll.PollingMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POLLING_WITH_PAUSES', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINOUS_POLLING', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW_POWER_POLLING', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=360,
  serialized_end=444,
)
_sym_db.RegisterEnumDescriptor(_POLLINGMODE)

PollingMode = enum_type_wrapper.EnumTypeWrapper(_POLLINGMODE)
_APPLEECP = _descriptor.EnumDescriptor(
  name='AppleEcp',
  full_name='contactless.poll.AppleEcp',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RUSSIA_MOSCOW', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=446,
  serialized_end=475,
)
_sym_db.RegisterEnumDescriptor(_APPLEECP)

AppleEcp = enum_type_wrapper.EnumTypeWrapper(_APPLEECP)
POLLING_WITH_PAUSES = 1
CONTINOUS_POLLING = 2
LOW_POWER_POLLING = 3
RUSSIA_MOSCOW = 0



_POLLFORTOKEN = _descriptor.Descriptor(
  name='PollForToken',
  full_name='contactless.poll.PollForToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='contactless.poll.PollForToken.timeout', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefer_mifare', full_name='contactless.poll.PollForToken.prefer_mifare', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poll_stm_sri512', full_name='contactless.poll.PollForToken.poll_stm_sri512', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polling_mode', full_name='contactless.poll.PollForToken.polling_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_ecp', full_name='contactless.poll.PollForToken.enable_ecp', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='light_up_led', full_name='contactless.poll.PollForToken.light_up_led', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poll_iso15693', full_name='contactless.poll.PollForToken.poll_iso15693', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poll_ask_cts', full_name='contactless.poll.PollForToken.poll_ask_cts', index=7,
      number=8, type=8, cpp_type=7, label=1,
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
  serialized_start=55,
  serialized_end=358,
)

_POLLFORTOKEN.fields_by_name['polling_mode'].enum_type = _POLLINGMODE
_POLLFORTOKEN.fields_by_name['enable_ecp'].enum_type = _APPLEECP
DESCRIPTOR.message_types_by_name['PollForToken'] = _POLLFORTOKEN
DESCRIPTOR.enum_types_by_name['PollingMode'] = _POLLINGMODE
DESCRIPTOR.enum_types_by_name['AppleEcp'] = _APPLEECP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PollForToken = _reflection.GeneratedProtocolMessageType('PollForToken', (_message.Message,), dict(
  DESCRIPTOR = _POLLFORTOKEN,
  __module__ = 'contactless.poll_for_token_pb2'
  # @@protoc_insertion_point(class_scope:contactless.poll.PollForToken)
  ))
_sym_db.RegisterMessage(PollForToken)


# @@protoc_insertion_point(module_scope)