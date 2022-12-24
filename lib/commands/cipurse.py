from google.protobuf.text_format import *
from google.protobuf.message import *

import lib.proto

import intellireader.contact.card_slot_pb2 as card_slot_pb2
import intellireader.commands_pb2 as commands_pb2
import intellireader.cipurse.read_binary_pb2 as read_binary_pb2
import intellireader.cipurse.read_record_pb2 as read_record_pb2
import intellireader.cipurse.read_value_pb2 as read_value_pb2
import intellireader.cipurse.modify_value_pb2 as modify_value_pb2

from .contact import DEFAULT_SAM_SLOT

def cipurse_authorize_sam(proto, payload):
    """ Authorize (unlock) CIPURSE Hardware SAM for processing """

    request = commands_pb2.Cipurse()
    cmd = request.authorize_sam

    cmd.slot = DEFAULT_SAM_SLOT
    cmd.aid = bytes.fromhex('D276000004FF00000000000000000001')

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def cipurse_select_file(proto, payload):
    """ Select file on the CIPURSE card """

    request = commands_pb2.Cipurse()
    cmd = request.select_file

    cmd.aid = bytes.fromhex('A0000005070101')

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def cipurse_establish_secure_channel(proto, payload):
    """ Establish secure channel between CIPURSE card and the reader """

    request = commands_pb2.Cipurse()
    cmd = request.establish_secure_channel

    cmd.key_number = 1
    cmd.sam_key_id = 3
    cmd.diversification_data = bytes.fromhex('0502058555B25C0000FF5F7C69000000')

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def cipurse_read_binary(proto, payload):
    """ Read binary file content """

    request = commands_pb2.Cipurse()
    cmd = request.read_binary

    cmd.short_file_id = 1
    cmd.length = 512

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, read_binary_pb2.Binary())

def cipurse_update_binary(proto, payload):
    """ Update binary file content """

    request = commands_pb2.Cipurse()
    cmd = request.update_binary

    cmd.short_file_id = 1
    cmd.data = b'\xde\xad\xbe\xef\x00\x00\x00\x00\xca\xfe\xfa\xde\x00\x00\x00\x00' * 32

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def cipurse_read_record(proto, payload):
    """ Read the content of the record(s) """

    request = commands_pb2.Cipurse()
    cmd = request.read_record

    cmd.short_file_id = 2
    cmd.first_record = 1
    cmd.length = 16 * 4
    cmd.read_multiple_records = True

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, read_record_pb2.Record())

def cipurse_update_record(proto, payload):
    """ Update the content of the record(s) """

    request = commands_pb2.Cipurse()
    cmd = request.update_record

    cmd.short_file_id = 2
    cmd.first_record = 1
    cmd.update_multiple_records = True
    cmd.data = b'\xde\xad\xbe\xef\x00\x00\x00\x00\xca\xfe\xfa\xde\x00\x00\x00\x00' * 4

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def cipurse_append_record(proto, payload):
    """ Append new record to the Cyclic Record File """

    request = commands_pb2.Cipurse()
    cmd = request.append_record

    cmd.short_file_id = 4
    cmd.data = b'\xde\xad\xbe\xef\x00\x00\x00\x00\xca\xfe\xfa\xde\x00\x00\x00\x00' * 3

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def cipurse_read_value(proto, payload):
    """ Read the value of the value-record(s) """

    request = commands_pb2.Cipurse()
    cmd = request.read_value

    cmd.short_file_id = 3
    cmd.first_record = 1
    cmd.count = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, read_value_pb2.Values())

def cipurse_modify_value(proto, payload):
    """ Increment or decrement the value of the record-value """

    request = commands_pb2.Cipurse()
    cmd = request.modify_value

    cmd.short_file_id = 3
    cmd.record = 1
    cmd.operand = 1

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, modify_value_pb2.NewValue())

cmds = [
    cipurse_authorize_sam, cipurse_select_file, cipurse_establish_secure_channel,
    cipurse_read_binary, cipurse_update_binary,
    cipurse_read_record, cipurse_update_record, cipurse_append_record,
    cipurse_read_value, cipurse_modify_value,
]

responses = {
    'authorize_sam': None,
    'select_file': None,
    'establish_secure_channel': None,
    'read_binary': read_binary_pb2.Binary(),
    'update_binary': None,
    'read_record': read_record_pb2.Record(),
    'update_record': None,
    'append_record': None,
    'read_value': read_value_pb2.Values(),
    'modify_value': modify_value_pb2.NewValue(),
}
