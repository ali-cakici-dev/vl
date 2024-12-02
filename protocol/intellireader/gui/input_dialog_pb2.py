# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gui/input_dialog.proto

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
  name='gui/input_dialog.proto',
  package='gui.input_dialog',
  syntax='proto2',
  serialized_pb=_b('\n\x16gui/input_dialog.proto\x12\x10gui.input_dialog\"\xb4\x01\n\x0bInputDialog\x12\x0f\n\x07\x63\x61ption\x18\x01 \x02(\t\x12\x13\n\x0bplaceholder\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\r\x12\x1a\n\x0fmin_text_length\x18\x04 \x01(\r:\x01\x30\x12\x1d\n\x0fmax_text_length\x18\x05 \x01(\r:\x04\x31\x30\x32\x34\x12\x33\n\x07layouts\x18\x06 \x03(\x0e\x32\x1e.gui.input_dialog.KeypadLayoutB\x02\x10\x01\"\x1b\n\x0b\x45nteredText\x12\x0c\n\x04text\x18\x01 \x02(\t*\x81\x01\n\x0cKeypadLayout\x12\x12\n\x0e\x44\x45\x43IMAL_DIGITS\x10\x00\x12\x11\n\rSPECIAL_CHARS\x10\x01\x12\x11\n\rENGLISH_LOWER\x10\x02\x12\x11\n\rENGLISH_UPPER\x10\x03\x12\x11\n\rRUSSIAN_LOWER\x10\x04\x12\x11\n\rRUSSIAN_UPPER\x10\x05')
)

_KEYPADLAYOUT = _descriptor.EnumDescriptor(
  name='KeypadLayout',
  full_name='gui.input_dialog.KeypadLayout',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DECIMAL_DIGITS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIAL_CHARS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENGLISH_LOWER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENGLISH_UPPER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUSSIAN_LOWER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUSSIAN_UPPER', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=257,
  serialized_end=386,
)
_sym_db.RegisterEnumDescriptor(_KEYPADLAYOUT)

KeypadLayout = enum_type_wrapper.EnumTypeWrapper(_KEYPADLAYOUT)
DECIMAL_DIGITS = 0
SPECIAL_CHARS = 1
ENGLISH_LOWER = 2
ENGLISH_UPPER = 3
RUSSIAN_LOWER = 4
RUSSIAN_UPPER = 5



_INPUTDIALOG = _descriptor.Descriptor(
  name='InputDialog',
  full_name='gui.input_dialog.InputDialog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='caption', full_name='gui.input_dialog.InputDialog.caption', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placeholder', full_name='gui.input_dialog.InputDialog.placeholder', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='gui.input_dialog.InputDialog.timeout', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_text_length', full_name='gui.input_dialog.InputDialog.min_text_length', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_text_length', full_name='gui.input_dialog.InputDialog.max_text_length', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1024,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layouts', full_name='gui.input_dialog.InputDialog.layouts', index=5,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),
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
  serialized_end=225,
)


_ENTEREDTEXT = _descriptor.Descriptor(
  name='EnteredText',
  full_name='gui.input_dialog.EnteredText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='gui.input_dialog.EnteredText.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=227,
  serialized_end=254,
)

_INPUTDIALOG.fields_by_name['layouts'].enum_type = _KEYPADLAYOUT
DESCRIPTOR.message_types_by_name['InputDialog'] = _INPUTDIALOG
DESCRIPTOR.message_types_by_name['EnteredText'] = _ENTEREDTEXT
DESCRIPTOR.enum_types_by_name['KeypadLayout'] = _KEYPADLAYOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputDialog = _reflection.GeneratedProtocolMessageType('InputDialog', (_message.Message,), dict(
  DESCRIPTOR = _INPUTDIALOG,
  __module__ = 'gui.input_dialog_pb2'
  # @@protoc_insertion_point(class_scope:gui.input_dialog.InputDialog)
  ))
_sym_db.RegisterMessage(InputDialog)

EnteredText = _reflection.GeneratedProtocolMessageType('EnteredText', (_message.Message,), dict(
  DESCRIPTOR = _ENTEREDTEXT,
  __module__ = 'gui.input_dialog_pb2'
  # @@protoc_insertion_point(class_scope:gui.input_dialog.EnteredText)
  ))
_sym_db.RegisterMessage(EnteredText)


_INPUTDIALOG.fields_by_name['layouts'].has_options = True
_INPUTDIALOG.fields_by_name['layouts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
