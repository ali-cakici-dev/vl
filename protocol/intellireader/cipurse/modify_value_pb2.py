# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cipurse/modify_value.proto

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
  name='cipurse/modify_value.proto',
  package='cipurse.modify_value',
  syntax='proto2',
  serialized_pb=_b('\n\x1a\x63ipurse/modify_value.proto\x12\x14\x63ipurse.modify_value\"H\n\x0bModifyValue\x12\x15\n\rshort_file_id\x18\x01 \x02(\r\x12\x0f\n\x07operand\x18\x02 \x02(\x11\x12\x11\n\x06record\x18\x03 \x01(\r:\x01\x31\"\x19\n\x08NewValue\x12\r\n\x05value\x18\x01 \x02(\x11')
)




_MODIFYVALUE = _descriptor.Descriptor(
  name='ModifyValue',
  full_name='cipurse.modify_value.ModifyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='short_file_id', full_name='cipurse.modify_value.ModifyValue.short_file_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operand', full_name='cipurse.modify_value.ModifyValue.operand', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='cipurse.modify_value.ModifyValue.record', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
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
  serialized_end=124,
)


_NEWVALUE = _descriptor.Descriptor(
  name='NewValue',
  full_name='cipurse.modify_value.NewValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='cipurse.modify_value.NewValue.value', index=0,
      number=1, type=17, cpp_type=1, label=2,
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
  serialized_start=126,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['ModifyValue'] = _MODIFYVALUE
DESCRIPTOR.message_types_by_name['NewValue'] = _NEWVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModifyValue = _reflection.GeneratedProtocolMessageType('ModifyValue', (_message.Message,), dict(
  DESCRIPTOR = _MODIFYVALUE,
  __module__ = 'cipurse.modify_value_pb2'
  # @@protoc_insertion_point(class_scope:cipurse.modify_value.ModifyValue)
  ))
_sym_db.RegisterMessage(ModifyValue)

NewValue = _reflection.GeneratedProtocolMessageType('NewValue', (_message.Message,), dict(
  DESCRIPTOR = _NEWVALUE,
  __module__ = 'cipurse.modify_value_pb2'
  # @@protoc_insertion_point(class_scope:cipurse.modify_value.NewValue)
  ))
_sym_db.RegisterMessage(NewValue)


# @@protoc_insertion_point(module_scope)
