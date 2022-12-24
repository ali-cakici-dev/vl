#!/usr/bin/env python3

"""
Usage:
  annotate.py [options] <file>

Arguments:
  <file>  File contained IntelliReader messages in HEX format.

Options:
  -h --help                     Show this message.
  -i --inline                   Inline decoded messages.
"""

from docopt import docopt

import re
import sys
from struct import *
import crcmod

sys.path.append('protocol')
sys.path.append('protocol/intellireader')

from lib.commander import MODULES
from lib.proto import Protocol
from lib import dumper

from google.protobuf.text_format import *
from google.protobuf.message import *

import common.notification_pb2 as notification_pb2
import common.failure_pb2 as failure_pb2

COMMANDS = {}

def annotate(msg):
    try:
        msg = bytes.fromhex(msg)

        header  = msg[0:2]
        lenbuf  = msg[2:4]
        length  = unpack(">H", lenbuf)[0]
        body    = msg[4:][:length]
        msgid   = body[0]
        msgid   = int(msgid)
        module  = body[1]
        msgtype = body[2]
        payload = body[3:][:length-3]
        crcbuf  = msg[-2:]
        crc     = unpack(">H", crcbuf)[0]

        if length > len(body): raise IndexError('Truncated message')

        crc_func = crcmod.predefined.mkCrcFun('xmodem')
        if crc != crc_func(msg[0:-2]): raise IndexError('Checksum mismatch')

        pbuf = None

        if   msgtype == Protocol.TYPE_CMD:  pbuf = MODULES[module][0]
        elif msgtype == Protocol.TYPE_RSP:  pbuf = COMMANDS.pop(msgid, None)
        elif msgtype == Protocol.TYPE_FAIL: pbuf = failure_pb2.FailureResponse()
        elif msgtype == Protocol.TYPE_NOTE: pbuf = notification_pb2.Notification()

        if pbuf: pbuf.ParseFromString(payload)

        if msgtype == Protocol.TYPE_CMD:
            module = MODULES[module]
            oneof_name = module[1]
            oneof = pbuf.WhichOneof(oneof_name)

            if oneof:
                if module[2]:
                    rsp = module[2].get(oneof)
                    if rsp:
                        COMMANDS[msgid] = rsp

        dumper.dump(msgtype, msgid, pbuf, lenbuf, body, crc)

    except Exception as e: dumper.error(e)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    dumper.set_dump_lvl('short')

    for line in open(arguments['<file>']):
        if arguments['--inline']:
            print(line)

        messages = re.findall(r'4952[0-9a-fA-F]*', line)
        for m in messages:
            annotate(m)

