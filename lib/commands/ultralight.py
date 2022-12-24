from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.contact.card_slot_pb2 as card_slot_pb2
import intellireader.mifare.ultralight.bulk_pb2 as ul_bulk_pb2
import intellireader.mifare.ultralight.counter.get_pb2 as ul_get_pb2
import intellireader.mifare.ultralight.counter.increment_pb2 as ul_increment_pb2
import intellireader.mifare.ultralight.counter.number_pb2 as ul_number_pb2
import intellireader.mifare.ultralight.password_pb2 as password_pb2
import intellireader.mifare.ultralight.read_pb2 as ul_read_pb2
import intellireader.mifare.ultralight.version_pb2 as ul_version_pb2
import intellireader.mifare.ultralight.write_pb2 as ul_write_pb2

from .contact import DEFAULT_SAM_SLOT

def ultralight_read(proto, payload):
    """ Mifare Ultralight Read pages """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_read_pages

    cmd.start_address = 4
    cmd.page_count = 4

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, ul_read_pb2.Pages())

def ultralight_write(proto, payload):
    """ Mifare Ultralight Write pages """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_write_pages

    cmd.start_address = 4
    cmd.data = \
            b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F' + \
            b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def ultralight_version(proto, payload):
    """ Mifare Ultralight EV1 Get Version """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_get_version
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, ul_version_pb2.Version())

def ultralight_get_counter(proto, payload):
    """ Mifare Ultralight EV1 Read Counter value """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_get_counter

    cmd.counter_number = ul_number_pb2.FIRST

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, ul_get_pb2.CounterValue())

def ultralight_increment_counter(proto, payload):
    """ Mifare Ultralight EV1 Increment Counter value """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_increment_counter

    cmd.counter_number = ul_number_pb2.FIRST
    cmd.operand = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def ultralight_bulk(proto, payload):
    """ Mifare Ultralight Bulk operation """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_bulk_operation

    write_cmd = cmd.operations.add()
    write_cmd.write_pages.start_address = 4
    write_cmd.write_pages.data = \
            b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F' + \
            b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F'

    read_cmd1 = cmd.operations.add()
    read_cmd1.read_pages.start_address = 4
    read_cmd1.read_pages.page_count = 4

    read_cmd2 = cmd.operations.add()
    read_cmd2.read_pages.start_address = 8
    read_cmd2.read_pages.page_count = 4

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, ul_bulk_pb2.BulkResult())

def ultralight_auth_clear(proto, payload):
    """ Mifare Ultralight 3DES Authentication on Clear Key """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_auth_on_clear_key

    cmd.clear_key = b'IEMKAERB!NACUOYF'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def ultralight_auth_samav2(proto, payload):
    """ Mifare Ultralight 3DES Authentication on SAM AV2/AV3 """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_auth_on_sam_key

    cmd.av2_args.slot = DEFAULT_SAM_SLOT
    cmd.av2_args.key_number = 27

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def ultralight_password_clear(proto, payload):
    """ Mifare Ultralight EV1 password based Authentication on Clear Key """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_auth_clear_password

    cmd.password = b'\xff\xff\xff\xff'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, password_pb2.PasswordAcknowledge())

def ultralight_password_samav2(proto, payload):
    """ Mifare Ultralight EV1 password based Authentication on SAM AV3 """

    request = commands_pb2.Mifare()
    cmd = request.mfr_ul_auth_sam_password

    cmd.av3_args.slot = DEFAULT_SAM_SLOT
    cmd.av3_args.key_number = 28

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, password_pb2.PasswordAcknowledge())

cmds = [ultralight_read, ultralight_write, ultralight_version, ultralight_get_counter, ultralight_increment_counter,
        ultralight_bulk, ultralight_auth_clear, ultralight_auth_samav2, ultralight_password_clear,
        ultralight_password_samav2]

from .mifare import responses
responses.update({
    'mfr_ul_read_pages': ul_read_pb2.Pages(),
    'mfr_ul_write_pages': None,
    'mfr_ul_get_version': ul_version_pb2.Version(),
    'mfr_ul_get_counter': ul_get_pb2.CounterValue(),
    'mfr_ul_increment_counter': None,
    'mfr_ul_bulk_operation': ul_bulk_pb2.BulkResult(),
    'mfr_ul_auth_on_clear_key': None,
    'mfr_ul_auth_on_sam_key': None,
    'mfr_ul_auth_clear_password': password_pb2.PasswordAcknowledge(),
    'mfr_ul_auth_sam_password': password_pb2.PasswordAcknowledge(),
})
