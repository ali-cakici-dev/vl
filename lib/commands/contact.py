from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2
import intellireader.contact.transaction_pb2 as transaction_pb2
import intellireader.contact.card_slot_pb2 as card_slot_pb2
import intellireader.contact.power_on_pb2 as power_on_pb2
import intellireader.contact.power_off_pb2 as power_off_pb2
import intellireader.contact.iso7816_4_pb2 as iso7816_4_pb2

import lib.proto

DEFAULT_SAM_SLOT = card_slot_pb2.SAM3_SLOT

def perform_contact_txn(proto, payload):
    """ Perform EMV transaction using contact smartcard """

    request = commands_pb2.ContactLevel2()
    perform_txn = request.perform_contact_transaction

    perform_txn.amount_authorized = 100 # 1.00$
    perform_txn.transaction_date = b'\x13\x06\x20'
    perform_txn.transaction_time = b'\x12\x00\x00'
    perform_txn.transaction_type = b'\x00'
    perform_txn.terminal_country_code = b'\x06\x43'
    perform_txn.transaction_currency_code = b'\x06\x43'
    perform_txn.merchant_name_and_location = b'MosMetro. Kropotkinskaya'
    perform_txn.merchant_category_code = b'\x41\x31'
    lib.commands.pinpad.set_encryption_params(perform_txn.online_pin_params)

    if payload:
        Merge(payload, perform_txn)

    return proto.exchange(request, transaction_pb2.ContactTransactionResult())

def icc_power_on(proto, payload):
    """ Power ON contact SmartCard """

    request = commands_pb2.ContactLevel1()
    cmd = request.power_on_card
    cmd.slot = DEFAULT_SAM_SLOT

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, power_on_pb2.ContactCard())

def icc_power_off(proto, payload):
    """ Power OFF contact SmartCard """

    request = commands_pb2.ContactLevel1()
    cmd = request.power_off_card
    cmd.slot = DEFAULT_SAM_SLOT

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def icc_transmit(proto, payload):
    """ Transmit APDU (SAM AV2 Get Version by default) to SmartCard """

    request = commands_pb2.ContactLevel1()
    cmd = request.transmit_apdu
    cmd.slot = DEFAULT_SAM_SLOT
    cmd.command_apdu = b"\x80\x60\x00\x00\x00"

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, iso7816_4_pb2.ResponseApdu())

cmds = [icc_power_on, icc_power_off, icc_transmit, perform_contact_txn]

responses = {
    'power_on_card': power_on_pb2.ContactCard(),
    'power_off_card': None,
    'transmit_apdu': iso7816_4_pb2.ResponseApdu(),
    'perform_contact_txn': transaction_pb2.ContactTransactionResult(),
}
