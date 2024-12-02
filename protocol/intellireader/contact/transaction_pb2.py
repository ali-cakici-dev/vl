# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contact/transaction.proto

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


from contact import emv_tag_pb2 as contact_dot_emv__tag__pb2
from pinpad import online_pin_pb2 as pinpad_dot_online__pin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contact/transaction.proto',
  package='contact.transaction',
  syntax='proto2',
  serialized_pb=_b('\n\x19\x63ontact/transaction.proto\x12\x13\x63ontact.transaction\x1a\x15\x63ontact/emv_tag.proto\x1a\x17pinpad/online_pin.proto\"\xe7\x02\n\x12PerformTransaction\x12\x19\n\x11\x61mount_authorized\x18\x01 \x02(\x04\x12\x18\n\x10transaction_date\x18\x02 \x02(\x0c\x12\x18\n\x10transaction_type\x18\x03 \x02(\x0c\x12\x1d\n\x15terminal_country_code\x18\x04 \x02(\x0c\x12\x18\n\x10transaction_time\x18\x05 \x02(\x0c\x12!\n\x19transaction_currency_code\x18\x06 \x02(\x0c\x12\"\n\x1amerchant_name_and_location\x18\x07 \x01(\x0c\x12\x1e\n\x16merchant_category_code\x18\x08 \x01(\x0c\x12\x1f\n\x17terminal_identification\x18\t \x01(\x0c\x12\x41\n\x11online_pin_params\x18\n \x01(\x0b\x32&.pinpad.online_pin.PinEncryptionParams\"\xad\x01\n\x18\x43ontactTransactionResult\x12\x36\n\x06status\x18\x01 \x02(\x0e\x32&.contact.transaction.TransactionStatus\x12)\n\x08\x65mv_tags\x18\x02 \x03(\x0b\x32\x17.contact.emv_tag.EmvTag\x12\x14\n\x0c\x65rror_reason\x18\x03 \x01(\t\x12\x18\n\x10online_pin_block\x18\x04 \x01(\x0c*a\n\x11TransactionStatus\x12\x0c\n\x08\x41PPROVED\x10\x00\x12\x0c\n\x08\x44\x45\x43LINED\x10\x01\x12\x1e\n\x1aUNABLE_PERFORM_TRANSACTION\x10\x02\x12\x10\n\x0c\x43\x41RD_EXPIRED\x10\x03')
  ,
  dependencies=[contact_dot_emv__tag__pb2.DESCRIPTOR,pinpad_dot_online__pin__pb2.DESCRIPTOR,])

_TRANSACTIONSTATUS = _descriptor.EnumDescriptor(
  name='TransactionStatus',
  full_name='contact.transaction.TransactionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APPROVED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DECLINED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNABLE_PERFORM_TRANSACTION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARD_EXPIRED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=636,
  serialized_end=733,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONSTATUS)

TransactionStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONSTATUS)
APPROVED = 0
DECLINED = 1
UNABLE_PERFORM_TRANSACTION = 2
CARD_EXPIRED = 3



_PERFORMTRANSACTION = _descriptor.Descriptor(
  name='PerformTransaction',
  full_name='contact.transaction.PerformTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount_authorized', full_name='contact.transaction.PerformTransaction.amount_authorized', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_date', full_name='contact.transaction.PerformTransaction.transaction_date', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_type', full_name='contact.transaction.PerformTransaction.transaction_type', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terminal_country_code', full_name='contact.transaction.PerformTransaction.terminal_country_code', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_time', full_name='contact.transaction.PerformTransaction.transaction_time', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_currency_code', full_name='contact.transaction.PerformTransaction.transaction_currency_code', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merchant_name_and_location', full_name='contact.transaction.PerformTransaction.merchant_name_and_location', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merchant_category_code', full_name='contact.transaction.PerformTransaction.merchant_category_code', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terminal_identification', full_name='contact.transaction.PerformTransaction.terminal_identification', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='online_pin_params', full_name='contact.transaction.PerformTransaction.online_pin_params', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=99,
  serialized_end=458,
)


_CONTACTTRANSACTIONRESULT = _descriptor.Descriptor(
  name='ContactTransactionResult',
  full_name='contact.transaction.ContactTransactionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='contact.transaction.ContactTransactionResult.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emv_tags', full_name='contact.transaction.ContactTransactionResult.emv_tags', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_reason', full_name='contact.transaction.ContactTransactionResult.error_reason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='online_pin_block', full_name='contact.transaction.ContactTransactionResult.online_pin_block', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=461,
  serialized_end=634,
)

_PERFORMTRANSACTION.fields_by_name['online_pin_params'].message_type = pinpad_dot_online__pin__pb2._PINENCRYPTIONPARAMS
_CONTACTTRANSACTIONRESULT.fields_by_name['status'].enum_type = _TRANSACTIONSTATUS
_CONTACTTRANSACTIONRESULT.fields_by_name['emv_tags'].message_type = contact_dot_emv__tag__pb2._EMVTAG
DESCRIPTOR.message_types_by_name['PerformTransaction'] = _PERFORMTRANSACTION
DESCRIPTOR.message_types_by_name['ContactTransactionResult'] = _CONTACTTRANSACTIONRESULT
DESCRIPTOR.enum_types_by_name['TransactionStatus'] = _TRANSACTIONSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PerformTransaction = _reflection.GeneratedProtocolMessageType('PerformTransaction', (_message.Message,), dict(
  DESCRIPTOR = _PERFORMTRANSACTION,
  __module__ = 'contact.transaction_pb2'
  # @@protoc_insertion_point(class_scope:contact.transaction.PerformTransaction)
  ))
_sym_db.RegisterMessage(PerformTransaction)

ContactTransactionResult = _reflection.GeneratedProtocolMessageType('ContactTransactionResult', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTTRANSACTIONRESULT,
  __module__ = 'contact.transaction_pb2'
  # @@protoc_insertion_point(class_scope:contact.transaction.ContactTransactionResult)
  ))
_sym_db.RegisterMessage(ContactTransactionResult)


# @@protoc_insertion_point(module_scope)
