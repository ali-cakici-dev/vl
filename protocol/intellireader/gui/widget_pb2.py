# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gui/widget.proto

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
from gui import border_pb2 as gui_dot_border__pb2
from gui import font_pb2 as gui_dot_font__pb2
from gui import foreground_pb2 as gui_dot_foreground__pb2
from gui import picture_id_pb2 as gui_dot_picture__id__pb2
from gui import text_id_pb2 as gui_dot_text__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gui/widget.proto',
  package='gui.widget',
  syntax='proto2',
  serialized_pb=_b('\n\x10gui/widget.proto\x12\ngui.widget\x1a\x13gui/alignment.proto\x1a\x14gui/background.proto\x1a\x10gui/border.proto\x1a\x0egui/font.proto\x1a\x14gui/foreground.proto\x1a\x14gui/picture_id.proto\x1a\x11gui/text_id.proto\"\xe3\x02\n\x06Widget\x12\x35\n\x0fvertical_layout\x18\x01 \x01(\x0b\x32\x1a.gui.widget.VerticalLayoutH\x00\x12\x39\n\x11horizontal_layout\x18\x02 \x01(\x0b\x32\x1c.gui.widget.HorizontalLayoutH\x00\x12 \n\x04text\x18\x03 \x01(\x0b\x32\x10.gui.widget.TextH\x00\x12&\n\x07picture\x18\x04 \x01(\x0b\x32\x13.gui.widget.PictureH\x00\x12%\n\x07qr_code\x18\x05 \x01(\x0b\x32\x12.gui.widget.QrCodeH\x00\x12\x37\n\x10\x63ustomer_picture\x18\x06 \x01(\x0b\x32\x1b.gui.widget.CustomerPictureH\x00\x12\x33\n\x0egenerated_text\x18\x07 \x01(\x0b\x32\x19.gui.widget.GeneratedTextH\x00\x42\x08\n\x06widget\"5\n\x0eVerticalLayout\x12#\n\x07widgets\x18\x01 \x03(\x0b\x32\x12.gui.widget.Widget\"7\n\x10HorizontalLayout\x12#\n\x07widgets\x18\x01 \x03(\x0b\x32\x12.gui.widget.Widget\"\xff\x02\n\x04Text\x12\x0c\n\x04text\x18\x01 \x02(\t\x12O\n\x12vertical_alignment\x18\x02 \x01(\x0e\x32 .gui.alignment.VerticalAlignment:\x11\x43\x45NTER_VERTICALLY\x12U\n\x14horizontal_alignment\x18\x03 \x01(\x0e\x32\".gui.alignment.HorizontalAlignment:\x13\x43\x45NTER_HORIZONTALLY\x12.\n\nbackground\x18\x04 \x01(\x0b\x32\x1a.gui.background.Background\x12.\n\nforeground\x18\x05 \x01(\x0b\x32\x1a.gui.foreground.Foreground\x12*\n\x04\x66ont\x18\x06 \x01(\x0e\x32\x0e.gui.font.Font:\x0cREGULAR_FONT\x12\x11\n\tbutton_id\x18\x07 \x01(\r\x12\"\n\x06\x62order\x18\x08 \x01(\x0b\x32\x12.gui.border.Border\"\xa3\x02\n\x07Picture\x12-\n\npicture_id\x18\x01 \x02(\x0e\x32\x19.gui.picture_id.PictureId\x12O\n\x12vertical_alignment\x18\x02 \x01(\x0e\x32 .gui.alignment.VerticalAlignment:\x11\x43\x45NTER_VERTICALLY\x12U\n\x14horizontal_alignment\x18\x03 \x01(\x0e\x32\".gui.alignment.HorizontalAlignment:\x13\x43\x45NTER_HORIZONTALLY\x12.\n\nbackground\x18\x04 \x01(\x0b\x32\x1a.gui.background.Background\x12\x11\n\tbutton_id\x18\x05 \x01(\r\"\xb8\x02\n\x06QrCode\x12\x0c\n\x04text\x18\x01 \x02(\x0c\x12\x18\n\x10module_dimension\x18\x02 \x01(\r\x12O\n\x12vertical_alignment\x18\x03 \x01(\x0e\x32 .gui.alignment.VerticalAlignment:\x11\x43\x45NTER_VERTICALLY\x12U\n\x14horizontal_alignment\x18\x04 \x01(\x0e\x32\".gui.alignment.HorizontalAlignment:\x13\x43\x45NTER_HORIZONTALLY\x12.\n\nbackground\x18\x05 \x01(\x0b\x32\x1a.gui.background.Background\x12.\n\nforeground\x18\x06 \x01(\x0b\x32\x1a.gui.foreground.Foreground\"\x8a\x02\n\x0f\x43ustomerPicture\x12\x0c\n\x04name\x18\x01 \x02(\t\x12O\n\x12vertical_alignment\x18\x02 \x01(\x0e\x32 .gui.alignment.VerticalAlignment:\x11\x43\x45NTER_VERTICALLY\x12U\n\x14horizontal_alignment\x18\x03 \x01(\x0e\x32\".gui.alignment.HorizontalAlignment:\x13\x43\x45NTER_HORIZONTALLY\x12.\n\nbackground\x18\x04 \x01(\x0b\x32\x1a.gui.background.Background\x12\x11\n\tbutton_id\x18\x05 \x01(\r\"\x8e\x03\n\rGeneratedText\x12$\n\x07text_id\x18\x01 \x02(\x0e\x32\x13.gui.text_id.TextId\x12\x10\n\x06prefix\x18\x02 \x01(\t:\x00\x12O\n\x12vertical_alignment\x18\x03 \x01(\x0e\x32 .gui.alignment.VerticalAlignment:\x11\x43\x45NTER_VERTICALLY\x12U\n\x14horizontal_alignment\x18\x04 \x01(\x0e\x32\".gui.alignment.HorizontalAlignment:\x13\x43\x45NTER_HORIZONTALLY\x12.\n\nbackground\x18\x05 \x01(\x0b\x32\x1a.gui.background.Background\x12.\n\nforeground\x18\x06 \x01(\x0b\x32\x1a.gui.foreground.Foreground\x12*\n\x04\x66ont\x18\x07 \x01(\x0e\x32\x0e.gui.font.Font:\x0cREGULAR_FONT\x12\x11\n\tbutton_id\x18\x08 \x01(\r')
  ,
  dependencies=[gui_dot_alignment__pb2.DESCRIPTOR,gui_dot_background__pb2.DESCRIPTOR,gui_dot_border__pb2.DESCRIPTOR,gui_dot_font__pb2.DESCRIPTOR,gui_dot_foreground__pb2.DESCRIPTOR,gui_dot_picture__id__pb2.DESCRIPTOR,gui_dot_text__id__pb2.DESCRIPTOR,])




_WIDGET = _descriptor.Descriptor(
  name='Widget',
  full_name='gui.widget.Widget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertical_layout', full_name='gui.widget.Widget.vertical_layout', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_layout', full_name='gui.widget.Widget.horizontal_layout', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='gui.widget.Widget.text', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='picture', full_name='gui.widget.Widget.picture', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qr_code', full_name='gui.widget.Widget.qr_code', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer_picture', full_name='gui.widget.Widget.customer_picture', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generated_text', full_name='gui.widget.Widget.generated_text', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
      name='widget', full_name='gui.widget.Widget.widget',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=173,
  serialized_end=528,
)


_VERTICALLAYOUT = _descriptor.Descriptor(
  name='VerticalLayout',
  full_name='gui.widget.VerticalLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='widgets', full_name='gui.widget.VerticalLayout.widgets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=530,
  serialized_end=583,
)


_HORIZONTALLAYOUT = _descriptor.Descriptor(
  name='HorizontalLayout',
  full_name='gui.widget.HorizontalLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='widgets', full_name='gui.widget.HorizontalLayout.widgets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=585,
  serialized_end=640,
)


_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='gui.widget.Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='gui.widget.Text.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_alignment', full_name='gui.widget.Text.vertical_alignment', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_alignment', full_name='gui.widget.Text.horizontal_alignment', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background', full_name='gui.widget.Text.background', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='foreground', full_name='gui.widget.Text.foreground', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='font', full_name='gui.widget.Text.font', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_id', full_name='gui.widget.Text.button_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='border', full_name='gui.widget.Text.border', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=643,
  serialized_end=1026,
)


_PICTURE = _descriptor.Descriptor(
  name='Picture',
  full_name='gui.widget.Picture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='picture_id', full_name='gui.widget.Picture.picture_id', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_alignment', full_name='gui.widget.Picture.vertical_alignment', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_alignment', full_name='gui.widget.Picture.horizontal_alignment', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background', full_name='gui.widget.Picture.background', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_id', full_name='gui.widget.Picture.button_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=1029,
  serialized_end=1320,
)


_QRCODE = _descriptor.Descriptor(
  name='QrCode',
  full_name='gui.widget.QrCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='gui.widget.QrCode.text', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_dimension', full_name='gui.widget.QrCode.module_dimension', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_alignment', full_name='gui.widget.QrCode.vertical_alignment', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_alignment', full_name='gui.widget.QrCode.horizontal_alignment', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background', full_name='gui.widget.QrCode.background', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='foreground', full_name='gui.widget.QrCode.foreground', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=1323,
  serialized_end=1635,
)


_CUSTOMERPICTURE = _descriptor.Descriptor(
  name='CustomerPicture',
  full_name='gui.widget.CustomerPicture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gui.widget.CustomerPicture.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_alignment', full_name='gui.widget.CustomerPicture.vertical_alignment', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_alignment', full_name='gui.widget.CustomerPicture.horizontal_alignment', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background', full_name='gui.widget.CustomerPicture.background', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_id', full_name='gui.widget.CustomerPicture.button_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=1638,
  serialized_end=1904,
)


_GENERATEDTEXT = _descriptor.Descriptor(
  name='GeneratedText',
  full_name='gui.widget.GeneratedText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_id', full_name='gui.widget.GeneratedText.text_id', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='gui.widget.GeneratedText.prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vertical_alignment', full_name='gui.widget.GeneratedText.vertical_alignment', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='horizontal_alignment', full_name='gui.widget.GeneratedText.horizontal_alignment', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background', full_name='gui.widget.GeneratedText.background', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='foreground', full_name='gui.widget.GeneratedText.foreground', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='font', full_name='gui.widget.GeneratedText.font', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_id', full_name='gui.widget.GeneratedText.button_id', index=7,
      number=8, type=13, cpp_type=3, label=1,
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
  serialized_start=1907,
  serialized_end=2305,
)

_WIDGET.fields_by_name['vertical_layout'].message_type = _VERTICALLAYOUT
_WIDGET.fields_by_name['horizontal_layout'].message_type = _HORIZONTALLAYOUT
_WIDGET.fields_by_name['text'].message_type = _TEXT
_WIDGET.fields_by_name['picture'].message_type = _PICTURE
_WIDGET.fields_by_name['qr_code'].message_type = _QRCODE
_WIDGET.fields_by_name['customer_picture'].message_type = _CUSTOMERPICTURE
_WIDGET.fields_by_name['generated_text'].message_type = _GENERATEDTEXT
_WIDGET.oneofs_by_name['widget'].fields.append(
  _WIDGET.fields_by_name['vertical_layout'])
_WIDGET.fields_by_name['vertical_layout'].containing_oneof = _WIDGET.oneofs_by_name['widget']
_WIDGET.oneofs_by_name['widget'].fields.append(
  _WIDGET.fields_by_name['horizontal_layout'])
_WIDGET.fields_by_name['horizontal_layout'].containing_oneof = _WIDGET.oneofs_by_name['widget']
_WIDGET.oneofs_by_name['widget'].fields.append(
  _WIDGET.fields_by_name['text'])
_WIDGET.fields_by_name['text'].containing_oneof = _WIDGET.oneofs_by_name['widget']
_WIDGET.oneofs_by_name['widget'].fields.append(
  _WIDGET.fields_by_name['picture'])
_WIDGET.fields_by_name['picture'].containing_oneof = _WIDGET.oneofs_by_name['widget']
_WIDGET.oneofs_by_name['widget'].fields.append(
  _WIDGET.fields_by_name['qr_code'])
_WIDGET.fields_by_name['qr_code'].containing_oneof = _WIDGET.oneofs_by_name['widget']
_WIDGET.oneofs_by_name['widget'].fields.append(
  _WIDGET.fields_by_name['customer_picture'])
_WIDGET.fields_by_name['customer_picture'].containing_oneof = _WIDGET.oneofs_by_name['widget']
_WIDGET.oneofs_by_name['widget'].fields.append(
  _WIDGET.fields_by_name['generated_text'])
_WIDGET.fields_by_name['generated_text'].containing_oneof = _WIDGET.oneofs_by_name['widget']
_VERTICALLAYOUT.fields_by_name['widgets'].message_type = _WIDGET
_HORIZONTALLAYOUT.fields_by_name['widgets'].message_type = _WIDGET
_TEXT.fields_by_name['vertical_alignment'].enum_type = gui_dot_alignment__pb2._VERTICALALIGNMENT
_TEXT.fields_by_name['horizontal_alignment'].enum_type = gui_dot_alignment__pb2._HORIZONTALALIGNMENT
_TEXT.fields_by_name['background'].message_type = gui_dot_background__pb2._BACKGROUND
_TEXT.fields_by_name['foreground'].message_type = gui_dot_foreground__pb2._FOREGROUND
_TEXT.fields_by_name['font'].enum_type = gui_dot_font__pb2._FONT
_TEXT.fields_by_name['border'].message_type = gui_dot_border__pb2._BORDER
_PICTURE.fields_by_name['picture_id'].enum_type = gui_dot_picture__id__pb2._PICTUREID
_PICTURE.fields_by_name['vertical_alignment'].enum_type = gui_dot_alignment__pb2._VERTICALALIGNMENT
_PICTURE.fields_by_name['horizontal_alignment'].enum_type = gui_dot_alignment__pb2._HORIZONTALALIGNMENT
_PICTURE.fields_by_name['background'].message_type = gui_dot_background__pb2._BACKGROUND
_QRCODE.fields_by_name['vertical_alignment'].enum_type = gui_dot_alignment__pb2._VERTICALALIGNMENT
_QRCODE.fields_by_name['horizontal_alignment'].enum_type = gui_dot_alignment__pb2._HORIZONTALALIGNMENT
_QRCODE.fields_by_name['background'].message_type = gui_dot_background__pb2._BACKGROUND
_QRCODE.fields_by_name['foreground'].message_type = gui_dot_foreground__pb2._FOREGROUND
_CUSTOMERPICTURE.fields_by_name['vertical_alignment'].enum_type = gui_dot_alignment__pb2._VERTICALALIGNMENT
_CUSTOMERPICTURE.fields_by_name['horizontal_alignment'].enum_type = gui_dot_alignment__pb2._HORIZONTALALIGNMENT
_CUSTOMERPICTURE.fields_by_name['background'].message_type = gui_dot_background__pb2._BACKGROUND
_GENERATEDTEXT.fields_by_name['text_id'].enum_type = gui_dot_text__id__pb2._TEXTID
_GENERATEDTEXT.fields_by_name['vertical_alignment'].enum_type = gui_dot_alignment__pb2._VERTICALALIGNMENT
_GENERATEDTEXT.fields_by_name['horizontal_alignment'].enum_type = gui_dot_alignment__pb2._HORIZONTALALIGNMENT
_GENERATEDTEXT.fields_by_name['background'].message_type = gui_dot_background__pb2._BACKGROUND
_GENERATEDTEXT.fields_by_name['foreground'].message_type = gui_dot_foreground__pb2._FOREGROUND
_GENERATEDTEXT.fields_by_name['font'].enum_type = gui_dot_font__pb2._FONT
DESCRIPTOR.message_types_by_name['Widget'] = _WIDGET
DESCRIPTOR.message_types_by_name['VerticalLayout'] = _VERTICALLAYOUT
DESCRIPTOR.message_types_by_name['HorizontalLayout'] = _HORIZONTALLAYOUT
DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['Picture'] = _PICTURE
DESCRIPTOR.message_types_by_name['QrCode'] = _QRCODE
DESCRIPTOR.message_types_by_name['CustomerPicture'] = _CUSTOMERPICTURE
DESCRIPTOR.message_types_by_name['GeneratedText'] = _GENERATEDTEXT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Widget = _reflection.GeneratedProtocolMessageType('Widget', (_message.Message,), dict(
  DESCRIPTOR = _WIDGET,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.Widget)
  ))
_sym_db.RegisterMessage(Widget)

VerticalLayout = _reflection.GeneratedProtocolMessageType('VerticalLayout', (_message.Message,), dict(
  DESCRIPTOR = _VERTICALLAYOUT,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.VerticalLayout)
  ))
_sym_db.RegisterMessage(VerticalLayout)

HorizontalLayout = _reflection.GeneratedProtocolMessageType('HorizontalLayout', (_message.Message,), dict(
  DESCRIPTOR = _HORIZONTALLAYOUT,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.HorizontalLayout)
  ))
_sym_db.RegisterMessage(HorizontalLayout)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), dict(
  DESCRIPTOR = _TEXT,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.Text)
  ))
_sym_db.RegisterMessage(Text)

Picture = _reflection.GeneratedProtocolMessageType('Picture', (_message.Message,), dict(
  DESCRIPTOR = _PICTURE,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.Picture)
  ))
_sym_db.RegisterMessage(Picture)

QrCode = _reflection.GeneratedProtocolMessageType('QrCode', (_message.Message,), dict(
  DESCRIPTOR = _QRCODE,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.QrCode)
  ))
_sym_db.RegisterMessage(QrCode)

CustomerPicture = _reflection.GeneratedProtocolMessageType('CustomerPicture', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERPICTURE,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.CustomerPicture)
  ))
_sym_db.RegisterMessage(CustomerPicture)

GeneratedText = _reflection.GeneratedProtocolMessageType('GeneratedText', (_message.Message,), dict(
  DESCRIPTOR = _GENERATEDTEXT,
  __module__ = 'gui.widget_pb2'
  # @@protoc_insertion_point(class_scope:gui.widget.GeneratedText)
  ))
_sym_db.RegisterMessage(GeneratedText)


# @@protoc_insertion_point(module_scope)