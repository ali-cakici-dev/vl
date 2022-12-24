import intellireader.commands_pb2 as commands_pb2

import intellireader.contact.card_slot_pb2 as card_slot_pb2
import intellireader.mifare.classic.auth_pb2 as mfr_auth_pb2

import intellireader.troika.av3.read_ticket_pb2 as read_ticket_pb2
import intellireader.troika.av3.write_ticket_pb2 as write_ticket_pb2

from .contact import DEFAULT_SAM_SLOT

def troika_av3_read_ticket(proto, payload):
    """ Reads logical ticket out of the Troika card """

    request = commands_pb2.TroikaCard()
    cmd = request.troika_av3_read_ticket
    read_ticket_init(cmd)

    response = read_ticket_pb2.Ticket()
    return proto.exchange(request, response)

def troika_av3_write_ticket(proto, payload):
    """ Prepares bitmap from parameters and writes bitmap on the card """

    request = commands_pb2.TroikaCard()
    cmd = request.troika_av3_write_ticket

    add_sam_key(cmd.sector, 8, 12, 'B')

    cmd.ticket_params = bytes.fromhex('011701B10300010000000000000000')
    cmd.validate_params = bytes.fromhex('0000000000030049520666');

    response = write_ticket_pb2.WriteResult()
    return proto.exchange(request, response)

def read_ticket_init(cmd):
    cmd.date.year = 21
    cmd.date.month = 11
    cmd.date.day = 13
    cmd.time.hour = 12
    cmd.time.minute = 0
    cmd.time.second = 0

    add_sam_key(cmd.sectors.add(), 1, 5,  'A')
    add_sam_key(cmd.sectors.add(), 7, 10, 'A')
    add_sam_key(cmd.sectors.add(), 8, 12, 'A')

def add_sam_key(sam_key, sector_number, key_number, key_type):
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

cmds = [troika_av3_read_ticket, troika_av3_write_ticket]

responses = {
    'troika_av3_read_ticket': read_ticket_pb2.Ticket(),
    'troika_av3_write_ticket': write_ticket_pb2.WriteResult(),
}
