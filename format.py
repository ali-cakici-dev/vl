#!/usr/bin/env python3

import sys

sys.path.append('protocol')
sys.path.append('protocol/intellireader')

from lib.commander import MODULES
from lib.proto import Protocol
from lib import dumper

from google.protobuf.text_format import *
from google.protobuf.message import *

import common.notification_pb2 as notification_pb2
import common.failure_pb2 as failure_pb2

def choose_type():
    types = [
        (Protocol.TYPE_CMD,  '01h: Command'),
        (Protocol.TYPE_RSP,  '02h: Response'),
        (Protocol.TYPE_FAIL, '03h: Failure'),
        (Protocol.TYPE_NOTE, '05h: Notification'),
    ]

    print()
    for n, type in enumerate(types):
        print('{}: {}'.format(n, type[1]))

    item = input('Choose message type: ')
    return types[int(item)][0]

def choose_module():
    modules = [
        (Protocol.MOD_MISC,        '01h: Miscellaneous'),
        (Protocol.MOD_CONTACT_L1,  '02h: Contact Level1'),
        (Protocol.MOD_CLESS_L1,    '03h: Contactless Level1'),
        (Protocol.MOD_CLESS_L2,    '04h: Contactless Level2'),
        (Protocol.MOD_MIFARE,      '05h: Mifare'),
        (Protocol.MOD_PINPAD,      '06h: PinPad'),
        (Protocol.MOD_SRV,         '07h: Service'),
        (Protocol.MOD_STMCARD,     '08h: STM card'),
        (Protocol.MOD_NTAGCARD,    '09h: NTAG card'),
        (Protocol.MOD_GUI,         '0Ah: GUI'),
        (Protocol.MOD_TOUCHSCREEN, '0Bh: Touchscreen'),
        (Protocol.MOD_COMPLEX,     '0Ch: Complex'),
        (Protocol.MOD_QRCODE,      '0Dh: QR Code'),
        (Protocol.MOD_CIPURSE,     '0Eh: Cipurse'),
        (Protocol.MOD_CONTACT_L2,  '0Fh: Contact Level2'),
        (Protocol.MOD_TURNSTILE,   '10h: Turnstile'),
        (Protocol.MOD_MIFAREEXT,   '11h: Mifare Extended'),
        (Protocol.MOD_TROIKA,      '12h: Troika card'),
    ]

    print()
    for n, module in enumerate(modules):
        print('{}: {}'.format(n, module[1]))

    item = input('Choose message module: ')
    return modules[int(item)][0]

def choose_command(commands):
    print()
    for n, command in enumerate(commands):
        print('{}: {}'.format(n, command))

    item = input('Choose command: ')
    return list(commands.values())[int(item)]

if __name__ == '__main__':
    dumper.set_dump_lvl('short')

    msgtype = choose_type()

    pbuf = None

    if msgtype == Protocol.TYPE_CMD:
        module = choose_module()
        pbuf = MODULES[module][0]

    elif msgtype == Protocol.TYPE_RSP:
        module = choose_module()
        module = MODULES[module]
        pbuf = choose_command(module[2])

    elif msgtype == Protocol.TYPE_FAIL:
        pbuf = failure_pb2.FailureResponse()

    elif msgtype == Protocol.TYPE_NOTE:
        pbuf = notification_pb2.Notification()

    payload = input('\nInput payload in HEX: ')
    payload = bytes.fromhex(payload)

    pbuf.ParseFromString(payload)
   
    dumper.dump(msgtype, cnt = 0, msg = pbuf, len_buf = '', body_buf = '', crc_buf = '')
