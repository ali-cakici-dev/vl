import crcmod
from struct import *

from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.qrcode.qrcode_event_pb2 as qrcode_event_pb2
import intellireader.qrcode.exchange_pb2 as exchange_pb2

import lib.proto
from lib.dumper import suspend_dump, error

e4000_crc_func = crcmod.predefined.mkCrcFun('crc-16')

V1 = 1
V2 = 2

def poll_for_qrcode(proto, payload):
    """ Poll for QR-code event """

    request = commands_pb2.QrCode()
    cmd = request.poll_for_qrcode
    cmd.timeout = 15000

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, qrcode_event_pb2.QrCodeEvent())

def e4000_read_settings(proto, payload):
    """ Read E4000 QR-scanner settings """

    protocols = {
        V1: (e4000_v1_exchange, [
            (0x0027, 'Firmware version', ''),
            (0x0028, 'Scan mode', '0: manual, 1: auto'),
            (0x001E, 'Custom prefix', 'off: 0, on: 1'),
            (0x001F, 'Custom prefix value', ''),
        ]),
        V2: (e4000_v2_exchange, [
            (0x020300, 'Firmware version', ''),
            (0x030101, 'Scan mode', '1: auto, 2: manual, 3: continuous, 4: host'),
            (0x050101, 'Custom prefix', 'off: 0, on: 1'),
            (0x050103, 'Custom prefix value', ''),
        ]),
    }

    suspend_dump() # don't spam by raw data

    version = e4000_wakeup(proto)
    if not version:
        return False

    e4000_exchange = protocols[version][0]
    e4000_settings = protocols[version][1]

    for setting in e4000_settings:
        cmd = setting[0]
        name = setting[1]
        desc = setting[2]

        if desc:
            desc = '(' + desc + ')'

        value = e4000_exchange(proto, cmd, '')
        if value is None:
            return False

        if len(value) == 0:
            value = '<empty>'
        elif cmd == 0x0027 or cmd == 0x020300:
            pass
        else:
            value = value.hex()

        print('{:X} {: <20}: {} {}'.format(cmd, name, value, desc))

    return True

def e4000_wakeup(proto):
    """ Wake scanner up from power-down mode """

    for attempt in range(3):
        print('Checking E4000 v1 is alive...')
        if e4000_v1_exchange(proto, 0x0027, ''):
            return V1
        print('Checking E4000 v2 is alive...')
        if e4000_v2_exchange(proto, 0x020300, ''):
            return V2

    return error('E4000 does not answer')

def e4000_v1_exchange(proto, cmd, data):
    """ E4000 exchange protocol v.1 """

    data_length = len(data)
    cmd |= 0x0000 if data_length else 0x2000 # set 'read value' bit if data is empty

    request = b'\x57\x00'
    request += pack("<H", cmd)
    request += pack("<H", data_length)
    request += bytes.fromhex(data)
    request += pack("<H", e4000_crc_func(request))
    request += b'\x50\x00'

    qr_code_module = commands_pb2.QrCode()
    send_command = qr_code_module.send_command

    send_command.timeout = 1000
    send_command.command = bytes(request)

    response = exchange_pb2.ScannerReply()
    if not proto.exchange(qr_code_module, response):
        return None

    ack_data = response.reply[6:-4]
    return ack_data

def e4000_v2_exchange(proto, cmd, data):
    """ E4000 exchange protocol v.2 """

    cmd = unpack("<I", pack(">I", cmd))[0] >> 8

    data_length = len(data)
    if not data_length:
        cmd |= 0x10000000 # set 'read value' bit if data is empty

    device_number = 0
    packet_label = 0

    request = b'\x57\x00'
    request += pack("B", device_number)
    request += pack("<I", cmd)
    request += pack("<H", packet_label)
    request += pack("<H", data_length)
    request += bytes.fromhex(data)
    request += pack("<H", e4000_crc_func(request))
    request += b'\x50\x41'

    qr_code_module = commands_pb2.QrCode()
    send_command = qr_code_module.send_command

    send_command.timeout = 1000
    send_command.command = bytes(request)

    response = exchange_pb2.ScannerReply()
    if not proto.exchange(qr_code_module, response):
        return None

    ack_data = response.reply[11:-4]
    return ack_data

cmds = [poll_for_qrcode, e4000_read_settings]

responses = {
    'poll_for_qrcode': qrcode_event_pb2.QrCodeEvent(),
    'send_command': exchange_pb2.ScannerReply(),
}
