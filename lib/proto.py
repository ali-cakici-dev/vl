import time

import common.notification_pb2 as notification_pb2
import common.failure_pb2 as failure_pb2

from termcolor import cprint

import crcmod
import socket

from struct import *
from .dumper import *
from .spinner import Spinner

crc_func = crcmod.predefined.mkCrcFun('xmodem')

class Protocol:
    """Implements IntelliReader protocol handling"""

    MOD_ALL         = 0x00
    MOD_MISC        = 0x01
    MOD_CONTACT_L1  = 0x02
    MOD_CLESS_L1    = 0x03
    MOD_CLESS_L2    = 0x04
    MOD_MIFARE      = 0x05
    MOD_PINPAD      = 0x06
    MOD_SRV         = 0x07
    MOD_STMCARD     = 0x08
    MOD_NTAGCARD    = 0x09
    MOD_GUI         = 0x0A
    MOD_TOUCHSCREEN = 0x0B
    MOD_COMPLEX     = 0x0C
    MOD_QRCODE      = 0x0D
    MOD_CIPURSE     = 0x0E
    MOD_CONTACT_L2  = 0x0F
    MOD_TURNSTILE   = 0x10
    MOD_MIFAREEXT   = 0x11
    MOD_TROIKA      = 0x12

    TYPE_CMD = 0x01
    TYPE_RSP = 0x02
    TYPE_FAIL = 0x03
    TYPE_PEND = 0x04
    TYPE_NOTE = 0x05
    TYPE_CTRL = 0x06

    HEADER = b'IR'

    def __init__(self, transport, dump_lvl, counter):

        self.timeout = 10
        self.counter = int(counter)
        self.transport = transport
        self.transport.settimeout(self.timeout)
        self.is_hard_cancel_required = False
        self.last_error = None

        set_dump_lvl(dump_lvl)

    def flush_rx(self):
        try:
            self.transport.settimeout(0)
            while True:
                data = self.transport.read(1)
                if len(data) == 0:
                    break
        except:
            pass
        finally:
            self.transport.settimeout(self.timeout)

    def exchange(self, req, rsp):
        t0 = time.time()
        self.is_hard_cancel_required = False
        self.last_error = None
        self.flush_rx()

        from .commander import get_module
        module = get_module(req)
        if not module:
            return error('ERR: Attempt to send message for unknown module')
        self.send(module, req, self.TYPE_CMD)
        res = self.recv(module, rsp)
        return res

    def send(self, mod, request, msg_type):
        hdr_buf = self.HEADER

        if msg_type != self.TYPE_CTRL:
            self.counter += 1
            self.counter %= 256
            req_buf = pack("B", self.counter)
        else:
            req_buf = pack("B", 0)

        req_buf += pack("B", mod)
        req_buf += pack("B", msg_type)

        if request:
            req_buf += request.SerializeToString()

        req_len = len(req_buf)
        len_buf = pack(">H", req_len)

        crc = crc_func(hdr_buf + len_buf + req_buf)
        crc_buf = pack(">H", crc)

        dump(self.TYPE_CMD, self.counter, request, len_buf, req_buf, crc_buf)

        msg = hdr_buf + len_buf + req_buf + crc_buf
        self.transport.write(msg)

    def recv(self, mod, response):
        local_counter = self.counter
        pending = False
        spinner = Spinner()

        while True:
            hdr_buf = self.transport.read(2)

            if len(hdr_buf) == 0:
                if pending is True:
                    next(spinner)
                    continue

                return error('ERR: NO RESPONSE RECEIVED DURING {} SECONDS'.format(self.transport.gettimeout()))

            if hdr_buf != self.HEADER:
                return error('ERR: UNKNOWN MESSAGE HEADER: {}'.format(hdr_buf.hex()))

            len_buf = self.transport.read(2)
            rsp_len = unpack(">H", len_buf)[0]

            rsp_buf = self.transport.read(rsp_len)
            rsp_cnt = unpack("B", rsp_buf[0:1])[0]
            rsp_mod = unpack("B", rsp_buf[1:2])[0]
            msg_type = unpack("B", rsp_buf[2:3])[0]

            crc_buf = self.transport.read(2)
            if not len(crc_buf):
                return error('ERR: NO CHECKSUM FOUND IN THE MESSAGE')

            got_crc = unpack(">H", crc_buf)[0]
            exp_crc = crc_func(hdr_buf + len_buf + rsp_buf)
            if exp_crc != got_crc:
                return error('ERR: WRONG CHECKSUM: expected {:#x} got {:#x}'.format(exp_crc, got_crc))

            if msg_type == self.TYPE_NOTE:
                payload = notification_pb2.Notification()
                payload.ParseFromString(rsp_buf[3:])

                dump(msg_type, rsp_cnt, payload, len_buf, rsp_buf, crc_buf)
                continue

            if msg_type == self.TYPE_PEND:
                dump(msg_type, rsp_cnt, None, len_buf, rsp_buf, crc_buf)
                pending = True
                continue

            if msg_type == self.TYPE_FAIL:
                fail_rsp = failure_pb2.FailureResponse()
                fail_rsp.ParseFromString(rsp_buf[3:])

                dump(msg_type, rsp_cnt, fail_rsp, len_buf, rsp_buf, crc_buf)

                self.last_error = fail_rsp.error
                return False

            if rsp_cnt != local_counter:
                return error('ERR: MISMATCHED COUNTER: expected {:03} got {:03}'.format(local_counter, rsp_cnt))

            if rsp_mod != mod:
                return error('ERR: MISMATCHED MODULE: expected {:03} got {:03}'.format(mod, rsp_mod))

            if msg_type == self.TYPE_RSP:
                if response:
                    response.ParseFromString(rsp_buf[3:])
                self.dump = dump(msg_type, rsp_cnt, response, len_buf, rsp_buf, crc_buf)
                return True

            return error('ERR: UNKNOWN MESSAGE TYPE: {:02X}'.format(msg_type))

    def hard_cancel(self):
        if self.is_hard_cancel_required:
            return True

        cprint('\nCancelling command...')
        self.send(self.MOD_ALL, None, self.TYPE_CTRL)
        self.is_hard_cancel_required = True
        return False
