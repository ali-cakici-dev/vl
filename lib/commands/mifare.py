from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.contact.card_slot_pb2 as card_slot_pb2
import intellireader.mifare.classic.auth_pb2 as mfr_auth_pb2
import intellireader.mifare.classic.read_pb2 as mfr_read_pb2
import intellireader.mifare.classic.write_pb2 as mfr_write_pb2
import intellireader.mifare.classic.counter.get_pb2 as mfr_get_pb2
import intellireader.mifare.classic.counter.set_pb2 as mfr_set_pb2
import intellireader.mifare.classic.counter.modify_pb2 as mfr_modify_pb2
import intellireader.mifare.classic.counter.copy_pb2 as mfr_copy_pb2
import intellireader.mifare.classic.counter.commit_pb2 as mfr_commit_pb2
import intellireader.mifare.classic.bulk_pb2 as mfr_bulk_pb2
import intellireader.mifare.av2.host_auth_pb2 as host_auth_pb2
import intellireader.mifare.av2.change_keyentry_pb2 as change_keyentry_pb2
import intellireader.mifare.av2.unlock_pb2 as unlock_pb2

from .contact import DEFAULT_SAM_SLOT

def mfr_auth_clear(proto, payload):
    """ Mifare Classic Authentication on Clear key """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_auth_on_clear_key

    cmd.sector_number = 0
    cmd.key_type = mfr_auth_pb2.TYPE_A
    cmd.clear_key = b'\xFF\xFF\xFF\xFF\xFF\xFF'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def mfr_auth_samav2(proto, payload):
    """ Mifare Classic Authentication on key stored within NXP SAM AV2 """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_auth_on_sam_key

    cmd.sector_number = 1
    cmd.key_type = mfr_auth_pb2.TYPE_A

    cmd.av2_args.slot = DEFAULT_SAM_SLOT
    cmd.av2_args.key_number = 3

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def mfr_read(proto, payload):
    """ Mifare Classic Read Data """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_read_blocks

    cmd.start_block = 0
    cmd.block_count = 3

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_read_pb2.Blocks())

def mfr_write(proto, payload):
    """ Mifare Classic Write Data """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_write_blocks

    cmd.start_block = 1
    cmd.data = \
        b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F' + \
        b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def mfr_get_counter(proto, payload):
    """ Mifare Classic Get Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_get_counter

    cmd.src_block = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_get_pb2.Counter())

def mfr_set_counter(proto, payload):
    """ Mifare Classic Set Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_set_counter

    cmd.dst_block = 1
    cmd.value = 0

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def mfr_mod_counter(proto, payload):
    """ Mifare Classic Modify Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_modify_counter

    cmd.src_block = 1
    cmd.dst_block = 1
    cmd.operand = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def mfr_copy_counter(proto, payload):
    """ Mifare Classic Copy Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_copy_counter

    cmd.src_block = 1
    cmd.dst_block = 2

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def mfr_commit_counter(proto, payload):
    """ Mifare Classic Commit Counter """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_commit_counter

    cmd.dst_block = 2

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def mfr_bulk(proto, payload):
    """ Mifare Classic Bulk operations """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_bulk_operation

    auth_cmd = cmd.operations.add().auth_on_clear_key
    auth_cmd.sector_number = 0
    auth_cmd.key_type = mfr_auth_pb2.TYPE_A
    auth_cmd.clear_key = b'\xFF\xFF\xFF\xFF\xFF\xFF'

    write_cmd = cmd.operations.add().write_blocks
    write_cmd.start_block = 1
    write_cmd.data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'

    read_cmd = cmd.operations.add().read_blocks
    read_cmd.start_block = 1
    read_cmd.block_count = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_bulk_pb2.BulkResult())


def mfr_bulk_av2(proto, payload):
    """ Mifare Classic Bulk operations using SAM AV2 """

    request = commands_pb2.Mifare()
    cmd = request.mfr_classic_bulk_operation

    auth_cmd = cmd.operations.add().auth_on_sam_key
    auth_cmd.sector_number = 8
    auth_cmd.key_type = mfr_auth_pb2.TYPE_B
    auth_cmd.av2_args.slot = DEFAULT_SAM_SLOT
    auth_cmd.av2_args.key_number = 2

    write_cmd = cmd.operations.add().write_blocks
    write_cmd.start_block = 1
    write_cmd.data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'

    read_cmd = cmd.operations.add().read_blocks
    read_cmd.start_block = 1
    read_cmd.block_count = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, mfr_bulk_pb2.BulkResult())

def av2_authenticate_host(proto, payload):
    """ Mifare SAM AV2 authenticate host """

    request = commands_pb2.Mifare()
    cmd = request.av2_authenticate_host

    cmd.args.slot = DEFAULT_SAM_SLOT
    cmd.args.key_number = 0

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def av2_create_mifare_keys(proto, payload):
    """ Creates/changes MIFARE keys in the SAM AV2 """

    request = commands_pb2.Mifare()
    cmd = request.av2_change_keyentry

    cmd.slot = DEFAULT_SAM_SLOT
    cmd.keyentry_number = 10
    cmd.key_version = 0
    cmd.mifare.key_a.key = b'\xFF\xFF\xFF\xFF\xFF\xFF'
    cmd.mifare.key_b.key = b'\xFF\xFF\xFF\xFF\xFF\xFF'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def av2_unlock(proto, payload):
    """ Unlock Mifare SAM AV2 """

    request = commands_pb2.Mifare()
    cmd = request.av2_unlock

    cmd.key = bytes.fromhex("E571800C723099603504239A26C4B641")
    cmd.args.slot = DEFAULT_SAM_SLOT
    cmd.args.key_number = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

cmds = [mfr_auth_clear, mfr_auth_samav2, mfr_write, mfr_read, mfr_bulk, mfr_bulk_av2,
        mfr_get_counter, mfr_set_counter, mfr_mod_counter, mfr_copy_counter, mfr_commit_counter,
        av2_authenticate_host, av2_create_mifare_keys, av2_unlock]

responses = {
    'mfr_classic_auth_on_clear_key': None,
    'mfr_classic_auth_on_sam_key': None,
    'mfr_classic_read_blocks': mfr_read_pb2.Blocks(),
    'mfr_classic_write_blocks': None,
    'mfr_classic_bulk_operation': mfr_bulk_pb2.BulkResult(),
    'mfr_classic_get_counter': mfr_get_pb2.Counter(),
    'mfr_classic_set_counter': None,
    'mfr_classic_modify_counter': None,
    'mfr_classic_copy_counter': None,
    'mfr_classic_commit_counter': None,

    'av2_authenticate_host': None,
    'av2_change_keyentry': None,
    'av2_unlock': None,
}
