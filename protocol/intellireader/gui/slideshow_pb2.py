# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gui/slideshow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gui import alignment_pb2 as gui_dot_alignment__pb2
from gui import background_pb2 as gui_dot_background__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gui/slideshow.proto',
  package='gui.slideshow',
  syntax='proto2',
  serialized_pb=_b('\n\x13gui/slideshow.proto\x12\rgui.slideshow\x1a\x13gui/alignment.proto\x1a\x14gui/background.proto\"\x9c\x02\n\tSlideshow\x12\x0c\n\x04name\x18\x01 \x02(\t\x12.\n\nbackground\x18\x02 \x02(\x0b\x32\x1a.gui.background.Background\x12\x14\n\x0c\x66rames_count\x18\x03 \x02(\r\x12\x13\n\x08\x64\x65lay_ms\x18\x04 \x01(\r:\x01\x30\x12O\n\x12vertical_alignment\x18\x05 \x01(\x0e\x32 .gui.alignment.VerticalAlignment:\x11\x43\x45NTER_VERTICALLY\x12U\n\x14horizontal_alignment\x18\x06 \x01(\x0e\x32\".gui.alignment.HorizontalAlignment:\x13\x43\x45NTER_HORIZONTALLY')
  ,
  dependencies=[gui_dot_alignment__pb2.DESCRIPTOR,gui_dot_background__pb2.DESCRIPTOR,])




_SLIDESHOW = _descriptor.Descriptor(
  name='Slideshow',
  full_name='gui.slideshow.Slideshow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gui.slideshow.Slideshow.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background', full_name='gui.slideshow.Slideshow.background', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frames_count', full_name='gui.slideshow.Slideshow.frames_count', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delay_ms', full_name='gui.slideshow.Slideshow.delay_ms', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_alignment', full_name='gui.slideshow.Slideshow.vertical_alignment', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_alignment', full_name='gui.slideshow.Slideshow.horizontal_alignment', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=82,
  serialized_end=366,
)

_SLIDESHOW.fields_by_name['background'].message_type = gui_dot_background__pb2._BACKGROUND
_SLIDESHOW.fields_by_name['vertical_alignment'].enum_type = gui_dot_alignment__pb2._VERTICALALIGNMENT
_SLIDESHOW.fields_by_name['horizontal_alignment'].enum_type = gui_dot_alignment__pb2._HORIZONTALALIGNMENT
DESCRIPTOR.message_types_by_name['Slideshow'] = _SLIDESHOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Slideshow = _reflection.GeneratedProtocolMessageType('Slideshow', (_message.Message,), dict(
  DESCRIPTOR = _SLIDESHOW,
  __module__ = 'gui.slideshow_pb2'
  # @@protoc_insertion_point(class_scope:gui.slideshow.Slideshow)
  ))
_sym_db.RegisterMessage(Slideshow)


# @@protoc_insertion_point(module_scope)