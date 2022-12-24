from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

def ntag_select(proto, payload):
    """ NXP NTAG Select Application """

    import intellireader.ntag.select_pb2 as select_pb2

    request = commands_pb2.NtagCard()
    cmd = request.ntag_select_file
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def ntag_auth(proto, payload):
    """ NXP NTAG Authenticate on Clear Key """

    import intellireader.ntag.auth_pb2 as auth_pb2

    request = commands_pb2.NtagCard()
    cmd = request.ntag_auth_on_clear_key

    cmd.clear_key = bytes(16)
    cmd.key_on_card = 2

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def ntag_read(proto, payload):
    """ NXP NTAG Read File """

    import intellireader.ntag.read_pb2 as read_pb2
    import intellireader.ntag.file_pb2 as file_pb2
    import intellireader.ntag.comm_pb2 as comm_pb2

    request = commands_pb2.NtagCard()
    cmd = request.ntag_read_file

    cmd.file = file_pb2.NDEF_MESSAGE
    cmd.protection = comm_pb2.PLAINTEXT

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, read_pb2.FileContent())

def ntag_write(proto, payload):
    """ NXP NTAG Write File """

    import intellireader.ntag.write_pb2 as write_pb2
    import intellireader.ntag.file_pb2 as file_pb2
    import intellireader.ntag.comm_pb2 as comm_pb2
    import datetime
    from irc import version

    now = datetime.datetime.now()
    text = "This string was written using IntelliReader v. {} at {}. Find more info at [https://valitek.ru]. "
    text = text.format(version(), now) * 2

    request = commands_pb2.NtagCard()
    cmd = request.ntag_write_file

    cmd.file = file_pb2.NDEF_MESSAGE
    cmd.protection = comm_pb2.ENCRYPTED_WITH_MAC
    cmd.data = text.encode('utf-8').ljust(256)

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

cmds = [ntag_select, ntag_auth, ntag_read, ntag_write]
