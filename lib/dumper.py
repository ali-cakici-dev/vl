from .formatter import hex_format

from google.protobuf.text_format import *
from google.protobuf.message import *

from struct import *
from termcolor import cprint

import common.notification_pb2 as notification_pb2

from lib import proto

global tmp_dump_lvl, dump_lvl
error_color = 'red'

def set_dump_lvl(new_duml_lvl):
    global tmp_dump_lvl, dump_lvl
    dump_lvl = new_duml_lvl
    tmp_dump_lvl = None

def suspend_dump():
    global tmp_dump_lvl, dump_lvl
    if not tmp_dump_lvl:
        dump_lvl, tmp_dump_lvl = tmp_dump_lvl, dump_lvl

def restore_dump():
    global tmp_dump_lvl, dump_lvl
    if tmp_dump_lvl:
        dump_lvl, tmp_dump_lvl = tmp_dump_lvl, dump_lvl

def dump(msg_type, cnt, msg, len_buf, body_buf, crc_buf):
    global dump_lvl

    if not dump_lvl and msg_type != proto.Protocol.TYPE_FAIL:
        return

    if isinstance(msg, notification_pb2.Notification):
        if msg.HasField("log_message"):
            note = msg.log_message
            importance_decriptor = note.DESCRIPTOR.enum_types_by_name['Importance']
            level = importance_decriptor.values_by_number[note.level].name
            print("NOTE: " + level + "({})".format(note.level) + " " + str(note.msg))

        if msg.HasField("user_message"):
            user = msg.user_message
            print("USER: " + MessageToString(user, True, True))

        return

    dump = dump_short(msg_type, cnt, msg)

    if dump_lvl == 'hex':
        dump += dump_hex(len_buf, body_buf, crc_buf)
    if dump_lvl == 'full':
        dump += dump_full(len_buf, body_buf, crc_buf)

    if msg_type != proto.Protocol.TYPE_FAIL:
        print(dump.encode('utf-8'))
    else:
        error(dump)
    return dump

def dump_short(msg_type, cnt, msg):
    if msg and msg.ByteSize() > 0:
        text = MessageToString(msg, True, True, message_formatter=hex_format)
        if not text:
            raise ValueError("IRC is unable to parse payload. Maybe IRC is too old?")
    else:
        text = 'Empty'

    names = {
        proto.Protocol.TYPE_CMD: ">>>",
        proto.Protocol.TYPE_RSP: "<<<",
        proto.Protocol.TYPE_FAIL: "FAL",
        proto.Protocol.TYPE_PEND: "ACK",
        proto.Protocol.TYPE_CTRL: "CTL",
    }

    return names[msg_type] + " " + '{:03}'.format(cnt) + ": '" + text + "'"


def dump_hex(len_buf, body_buf, crc_buf=''):
    header = proto.Protocol.HEADER.hex().upper()
    length = len_buf.hex().upper()
    body = body_buf.hex().upper()
    crc = crc_buf.hex().upper()

    return '\n' + header + length + body + crc

def dump_full(len_buf, body_buf, crc_buf):
    chksum = crc_buf.hex().upper()
    chkoff = 2 + len(len_buf) + len(body_buf)

    header = proto.Protocol.HEADER.hex().upper()
    length = len_buf.hex().upper()

    counter = unpack("B", body_buf[0:1])[0]
    mod = unpack("B", body_buf[1:2])[0]
    typ = unpack("B", body_buf[2:3])[0]

    payload = body_buf[3:]

    dump = '\n'.join([
        "",
        "      HEADER LENGTH MSGID MODULE TYPE",
        "0000  {}   {}   {:0>2X}    {:0>2X}     {:0>2X}".format(header, length, counter, mod, typ),

        "",
        "      PAYLOAD",
        hexdump(payload),

        "      CHECKSUM",
        "{:04X}  {}".format(chkoff, chksum),
    ])

    return dump


def hexdump(src, offlen=7, length=16):
    FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or '.' for x in range(256)])
    lines = []
    for c in range(0, len(src), length):
        chars = src[c:c+length]
        hex = ' '.join(["%02X" % x for x in chars])
        printable = ''.join(["%s" % ((x <= 127 and FILTER[x]) or '.') for x in chars])
        lines.append("%04X  %-*s  %s\n" % (c + offlen, length*3, hex, printable))
    return ''.join(lines)


def error(text):
    cprint(text, error_color)
    return False
