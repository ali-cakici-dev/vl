import time

from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.contactless.transaction_pb2 as transaction_pb2
import intellireader.contactless.poll_for_token_pb2 as poll_for_token_pb2
import intellireader.contactless.token_pb2 as token_pb2
import intellireader.contactless.transceive_pb2 as transceive_pb2
import intellireader.contactless.iso14443_4_pb2 as iso14443_4_pb2
import intellireader.contactless.rf_field_pb2 as rf_field_pb2
import intellireader.contactless.emv_removal_pb2 as emv_removal_pb2
import intellireader.contactless.iso14443_4a_pb2 as iso14443_4a_pb2

import lib.proto
from . import misc

def contactless_txn(proto, payload):
    """ Example of real life contactless transaction behaviour """

    res = perform_txn(proto, payload)
    if res:
        time.sleep(0.75)
        emv_removal(proto, None)

    if not misc.leds(proto, 'blue: false yellow: false green: false red: false'):
        return False

    return res

def perform_txn(proto, payload):
    """ Perform EMV transaction using contactless smartcard """

    request = commands_pb2.ContactlessLevel2()
    perform_txn = request.perform_transaction

    perform_txn.poll_for_token.timeout = 15000
    perform_txn.poll_for_token.light_up_led = True
    #perform_txn.poll_for_token.enable_ecp = poll_for_token_pb2.RUSSIA_MOSCOW

    perform_txn.amount_authorized = 100 # 1.00$
    perform_txn.transaction_date = b'\x13\x06\x13'
    perform_txn.transaction_time = b'\x12\x00\x00'
    perform_txn.transaction_type = b'\x00'
    perform_txn.terminal_country_code = b'\x06\x43'
    perform_txn.transaction_currency_code = b'\x06\x43'
    perform_txn.merchant_name_and_location = b'MosMetro. Kropotkinskaya'
    perform_txn.merchant_category_code = b'\x41\x31'

    if payload:
        Merge(payload, perform_txn)

    result = transaction_pb2.TransactionResult()
    if not proto.exchange(request, result):
        return False

    if result.HasField('encrypted_sensitive_data'):
        print("Decrypting sensitive data...")

        import rsa
        from lib.formatter import hex_format

        private_key = "emv_priv.pem"
        f = open(private_key, "r")

        key = rsa.PrivateKey.load_pkcs1(f.read())
        clear_data = rsa.decrypt(result.encrypted_sensitive_data, key)

        sensitive_data = transaction_pb2.SensitiveData()
        sensitive_data.ParseFromString(clear_data)

        print(MessageToString(sensitive_data, True, True, message_formatter=hex_format))

    return True

def poll_for_token(proto, payload):
    """ Poll for contactless token """

    request = commands_pb2.ContactlessLevel1()
    cmd = request.poll_for_token

    #cmd.poll_stm_sri512 = True
    #cmd.poll_iso15693 = True
    #cmd.poll_ask_cts = True
    cmd.timeout = 5000

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, token_pb2.Token())

def emv_removal(proto, payload):
    """ Execute EMVCo removal procedure """

    request = commands_pb2.ContactlessLevel1()
    cmd = request.emv_removal

    cmd.timeout = 5000

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def tsv_bit_array(proto, payload):
    """ Transceive BitArray to contactless token """

    request = commands_pb2.ContactlessLevel1()
    cmd = request.tsv_bit_array

    cmd.bit_array.data = b"\x02\x00\xA4\x04\x00\x0E2PAY.SYS.DDF01\x00"
    cmd.bit_array.count = len(cmd.bit_array.data) * 8
    cmd.response_timeout_us = 50000
    cmd.tx_crc = True
    cmd.rx_crc = True
    cmd.parity = True

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, transceive_pb2.BitArray())

def iso14443_4_command(proto, payload):
    """ Send command by ISO14443-4 half-duplex protocol to token """

    request = commands_pb2.ContactlessLevel1()
    cmd = request.iso14443_4_command

    cmd.data = b"\x00\xA4\x04\x00\x0E2PAY.SYS.DDF01\x00"

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, iso14443_4_pb2.Response())

def power_off_field(proto, payload):
    """ Power OFF reader's RF Field """

    request = commands_pb2.ContactlessLevel1()
    cmd = request.power_off_field
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def request_for_ats(proto, payload):
    """ Send the RATS command to the card """

    request = commands_pb2.ContactlessLevel1()
    cmd = request.request_for_ats
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, iso14443_4a_pb2.AnswerToSelect())

cmds = [contactless_txn, poll_for_token, emv_removal, perform_txn, tsv_bit_array, iso14443_4_command,
        power_off_field, request_for_ats]

responses = {
    'perform_transaction': transaction_pb2.TransactionResult(),
    'poll_for_token': token_pb2.Token(),
    'tsv_bit_array': transceive_pb2.BitArray(),
    'iso14443_4_command': iso14443_4_pb2.Response(),
    'emv_removal': None,
    'power_off_field': None,
    'request_for_ats': iso14443_4a_pb2.AnswerToSelect(),
}
