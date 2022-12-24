import random

from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.contact.card_slot_pb2 as card_slot_pb2
import intellireader.mifare.classic.auth_pb2 as mfr_auth_pb2
import intellireader.mifare.classic.read_pb2 as mfr_read_pb2
import intellireader.mifare.classic.write_pb2 as mfr_write_pb2
import intellireader.mifare.classic.sector.read_sector_pb2 as mfr_read_sector_pb2
import intellireader.mifare.generic.get_version_pb2 as get_version_pb2

from lib.dumper import suspend_dump, error

from .contact import DEFAULT_SAM_SLOT

USE_TEST_CARD = True

def mfr_read_sectors(proto, payload):
    """ Authenticates & reads multiple sectors from Mifare Classic card """

    request = commands_pb2.MifareExtended()
    cmd = request.mfr_classic_read_sectors

    print('Read sectors:')

    test_card_read(cmd) if USE_TEST_CARD else blank_card_read(cmd)
    # cmd.read_trailer_block = True

    suspend_dump() # don't spam by raw data

    response = mfr_read_sector_pb2.SectorsData()
    if not proto.exchange(request, response):
        return False

    print('\nSectors data:')

    for sector in response.sectors_data:
        print('{:02}: {}'.format(sector.sector_number, sector.blocks.data.hex()))

    return True

def mfr_write_sectors(proto, payload):
    """ Authenticates & writes multiple sectors on Mifare Classic card """

    request = commands_pb2.MifareExtended()
    cmd = request.mfr_classic_write_sectors

    print('Write sectors:')

    test_card_write(cmd) if USE_TEST_CARD else blank_card_write(cmd)

    rnd_byte = random.getrandbits(8)
    data = bytes(rnd_byte for _ in range(16 * 3))
    print('Write data:', data.hex())

    for sector in cmd.sectors:
        sector.blocks.start_block = 0
        sector.blocks.data = data

    suspend_dump() # don't spam by raw data

    if not proto.exchange(request, None):
        return False

    print('Write done')
    return True

def mfr_get_version(proto, payload):
    """ Get generic mifare card product version """

    request = commands_pb2.MifareExtended()
    cmd = request.mfr_get_version
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, get_version_pb2.ProductVersionInfo())

def test_card_read(cmd):
    add_clear_key(cmd.sectors.add(), 0,    'A')
    add_sam_key(  cmd.sectors.add(), 1, 3, 'A')
    add_sam_key(  cmd.sectors.add(), 2, 3, 'A')
    add_sam_key(  cmd.sectors.add(), 3, 3, 'A')
    add_sam_key(  cmd.sectors.add(), 4, 3, 'A')
    add_sam_key(  cmd.sectors.add(), 5, 3, 'A')
    add_sam_key(  cmd.sectors.add(), 6, 3, 'A')
    add_sam_key(  cmd.sectors.add(), 7, 3, 'A')
    add_sam_key(  cmd.sectors.add(), 8, 1, 'A')
    add_clear_key(cmd.sectors.add(), 9,    'A')
    add_clear_key(cmd.sectors.add(), 10,   'A')
    add_clear_key(cmd.sectors.add(), 11,   'A')
    add_clear_key(cmd.sectors.add(), 12,   'A')
    add_clear_key(cmd.sectors.add(), 13,   'A')
    add_clear_key(cmd.sectors.add(), 14,   'A')
    add_clear_key(cmd.sectors.add(), 15,   'A')

def test_card_write(cmd):
    add_sam_key(  cmd.sectors.add().sector, 1, 4, 'B')
    add_sam_key(  cmd.sectors.add().sector, 2, 4, 'B')
    add_sam_key(  cmd.sectors.add().sector, 3, 4, 'B')
    add_sam_key(  cmd.sectors.add().sector, 4, 4, 'B')
    add_sam_key(  cmd.sectors.add().sector, 5, 4, 'B')
    add_sam_key(  cmd.sectors.add().sector, 6, 4, 'B')
    add_sam_key(  cmd.sectors.add().sector, 7, 4, 'B')
    add_sam_key(  cmd.sectors.add().sector, 8, 2, 'B')
    add_clear_key(cmd.sectors.add().sector, 9,    'A')
    add_clear_key(cmd.sectors.add().sector, 10,   'A')
    add_clear_key(cmd.sectors.add().sector, 11,   'A')
    add_clear_key(cmd.sectors.add().sector, 12,   'A')
    add_clear_key(cmd.sectors.add().sector, 13,   'A')
    add_clear_key(cmd.sectors.add().sector, 14,   'A')
    add_clear_key(cmd.sectors.add().sector, 15,   'A')

def blank_card_read(cmd):
    for sector_number in range(0, 16):
        add_clear_key(cmd.sectors.add(), sector_number, 'A')

def blank_card_write(cmd):
    for sector_number in range(1, 16):
        add_clear_key(cmd.sectors.add().sector, sector_number, 'A')

def add_clear_key(sector, sector_number, key_type):
    clear_key = sector.clear_key
    
    clear_key.sector_number = sector_number
    clear_key.key_type = KEY_TYPES[key_type]
    clear_key.clear_key = b'\xFF\xFF\xFF\xFF\xFF\xFF'

    print('{:02}: CLEAR key {}: {}'.format(
        clear_key.sector_number,
        key_type,
        clear_key.clear_key.hex()))

def add_sam_key(sector, sector_number, key_number, key_type):
    sam_key = sector.sam_key

    sam_key.sector_number = sector_number
    sam_key.key_type = KEY_TYPES[key_type]

    sam_key.av2_args.slot = DEFAULT_SAM_SLOT
    sam_key.av2_args.key_number = key_number

    print('{:02}: SAM key {} number: {}'.format(
        sam_key.sector_number,
        key_type,
        sam_key.av2_args.key_number))

KEY_TYPES = {
    'A': mfr_auth_pb2.TYPE_A,
    'B': mfr_auth_pb2.TYPE_B,
    'a': mfr_auth_pb2.TYPE_A,
    'b': mfr_auth_pb2.TYPE_B,
}

cmds = [mfr_read_sectors, mfr_write_sectors, mfr_get_version]

responses = {
    'mfr_read_sectors': mfr_read_sector_pb2.SectorsData(),
    'mfr_write_sectors': None,
    'mfr_get_version': get_version_pb2.ProductVersionInfo(),
}
