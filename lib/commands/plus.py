from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.contact.card_slot_pb2 as card_slot_pb2
import intellireader.mifare.plus.auth_pb2 as mfr_auth_pb2
import intellireader.mifare.plus.bulk_pb2 as mfr_bulk_pb2
import intellireader.mifare.plus.counter.commit_pb2 as mfr_commit_pb2
import intellireader.mifare.plus.counter.copy_pb2 as mfr_copy_pb2
import intellireader.mifare.plus.counter.get_pb2 as mfr_get_pb2
import intellireader.mifare.plus.counter.modify_pb2 as mfr_modify_pb2
import intellireader.mifare.plus.counter.set_pb2 as mfr_set_pb2
import intellireader.mifare.plus.read_pb2 as mfr_read_pb2
import intellireader.mifare.plus.sector_pb2 as sector_key_pb2
import intellireader.mifare.plus.write_pb2 as mfr_write_pb2

from .contact import DEFAULT_SAM_SLOT

def plus_auth_clear(proto, payload):
    """ Mifare Plus Authentication on Clear key """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_auth_on_clear_key

    sector_key = cmd.key_type.sector_key
    sector_key.sector_number = 0
    sector_key.sector_key_type = sector_key_pb2.TYPE_A
    cmd.clear_key = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def plus_auth_samav2(proto, payload):
    """ Mifare Plus Authentication on key stored within NXP SAM AV2 """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_auth_on_sam_key

    sector_key = cmd.key_type.sector_key
    sector_key.sector_number = 0
    sector_key.sector_key_type = sector_key_pb2.TYPE_A

    cmd.av2_args.slot = DEFAULT_SAM_SLOT
    cmd.av2_args.key_number = 25

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def plus_read(proto, payload):
    """ Mifare Plus Read Data """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_read_blocks

    cmd.start_block = 0
    cmd.block_count = 3

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_read_pb2.Blocks())

def plus_write(proto, payload):
    """ Mifare Plus Write Data """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_write_blocks

    cmd.start_block = 1
    cmd.data = \
        b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F' + \
        b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def plus_bulk(proto, payload):
    """ Mifare Plus Bulk operations """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_bulk_operation

    auth_cmd = cmd.operations.add().auth_on_clear_key
    sector_key = auth_cmd.key_type.sector_key
    sector_key.sector_number = 0
    sector_key.sector_key_type = sector_key_pb2.TYPE_A
    auth_cmd.clear_key = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'

    write_cmd = cmd.operations.add().write_blocks
    write_cmd.start_block = 1
    write_cmd.data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'

    read_cmd = cmd.operations.add().read_blocks
    read_cmd.start_block = 1
    read_cmd.block_count = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_bulk_pb2.BulkResult())

def plus_bulk_av2(proto, payload):
    """ Mifare Plus Bulk operations use SAM AV2 """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_bulk_operation

    auth_cmd = cmd.operations.add().auth_on_sam_key
    auth_cmd.av2_args.slot = DEFAULT_SAM_SLOT
    auth_cmd.av2_args.key_number = 25
    sector_key = auth_cmd.key_type.sector_key
    sector_key.sector_number = 0
    sector_key.sector_key_type = sector_key_pb2.TYPE_A

    write_cmd = cmd.operations.add().write_blocks
    write_cmd.start_block = 1
    write_cmd.data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'

    read_cmd = cmd.operations.add().read_blocks
    read_cmd.start_block = 1
    read_cmd.block_count = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_bulk_pb2.BulkResult())

def plus_get_counter(proto, payload):
    """ Mifare Plus Get Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_get_counter

    cmd.src_block = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_get_pb2.Counter())

def plus_set_counter(proto, payload):
    """ Mifare Plus Set Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_set_counter

    cmd.dst_block = 1
    cmd.value = 0

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def plus_mod_counter(proto, payload):
    """ Mifare Plus Modify Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_modify_counter

    cmd.src_block = 1
    cmd.dst_block = 1
    cmd.operand = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def plus_copy_counter(proto, payload):
    """ Mifare Plus Copy Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_copy_counter

    cmd.src_block = 1
    cmd.dst_block = 2

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def plus_commit_counter(proto, payload):
    """ Mifare Plus Commit Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_plus_commit_counter

    cmd.dst_block = 2

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

cmds = [plus_auth_clear, plus_auth_samav2, plus_write, plus_read, plus_bulk, plus_bulk_av2,
        plus_get_counter, plus_set_counter, plus_mod_counter, plus_copy_counter, plus_commit_counter]

from .mifare import responses
responses.update({
    'mfr_plus_auth_on_clear_key': None,
    'mfr_plus_auth_on_sam_key': None,
    'mfr_plus_read_blocks': mfr_read_pb2.Blocks(),
    'mfr_plus_write_blocks': None,
    'mfr_plus_bulk_operation': mfr_bulk_pb2.BulkResult(),
    'mfr_plus_get_counter': mfr_get_pb2.Counter(),
    'mfr_plus_set_counter': None,
    'mfr_plus_modify_counter': None,
    'mfr_plus_copy_counter': None,
    'mfr_plus_commit_counter': None,
})
