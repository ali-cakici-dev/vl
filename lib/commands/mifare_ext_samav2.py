from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2
import intellireader.contact.card_slot_pb2 as card_slot_pb2

UID = [0xbc, 0x07, 0xba, 0x0f]
SAM_SLOT = card_slot_pb2.SAM3_SLOT
KEY_NUMBER = 0x03
BLOCK_NUMBER = 0x04

def mfr_transmit(proto, tx_data, options):
    import intellireader.contactless.transceive_pb2 as transceive_pb2

    request = commands_pb2.ContactlessLevel1()
    cmd = request.tsv_bit_array

    cmd.bit_array.data = tx_data
    cmd.bit_array.count = len(tx_data) * 8
    cmd.response_timeout_us = 1000

    Merge(options, cmd)

    response = transceive_pb2.BitArray()
    if not proto.exchange(request, response):
        return None

    return response.data

def sam_transmit(proto, cmd):
    import intellireader.contact.iso7816_4_pb2 as iso7816_4_pb2

    request = commands_pb2.ContactLevel1()
    request.transmit_apdu.command_apdu = bytes(cmd)
    request.transmit_apdu.slot = SAM_SLOT

    rsp = iso7816_4_pb2.ResponseApdu()

    if not proto.exchange(request, rsp):
        raise ValueError("Transmit APDU failed")

    return rsp.body, rsp.trailer

def mfr_auth_via_external_sam(proto, payload):
    """ Mifare Classic Authentication using "external" NXP SAM """

    kill_auth = [0x80, 0xCA, 0x00, 0x00]
    sam_transmit(proto, kill_auth)

    mifare_auth = bytes([0x60, BLOCK_NUMBER])
    number_rb = mfr_transmit(proto, mifare_auth, 'tx_crc: true rx_crc: false parity: true')
    if not number_rb:
        return False
    number_rb = list(number_rb)

    # Key Entry number, version 0x00, Key Type 0x0A
    samav2_key_entry = [KEY_NUMBER, 0x00, 0x0A]
    # Block Number, "number RB"
    mifare_info = [BLOCK_NUMBER] + number_rb

    first_part = \
        [0x80, 0x1C, 0x00, 0x00] + [0x0D] + \
        UID + samav2_key_entry + mifare_info + [0x00] + \
        [0x00]

    token_ab, sw12 = sam_transmit(proto, first_part)
    if sw12 != 0x90AF:
        return False

    token_ab = bytes(token_ab)
    token_ba = mfr_transmit(proto, token_ab, '')
    if not token_ba:
        return False
    token_ba = list(token_ba)

    second_part = [0x80, 0x1C, 0x00, 0x00] + [0x05] + token_ba
    _, sw12 = sam_transmit(proto, second_part)
    if sw12 != 0x9000:
        return False

    return True

cmds = [mfr_auth_via_external_sam]
