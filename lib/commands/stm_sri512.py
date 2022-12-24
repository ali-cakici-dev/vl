from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

def sri512_read(proto, payload):
    """ STM SRI512 Read Blocks """

    import intellireader.sri512.read_pb2 as read_pb2

    request = commands_pb2.StmCard()
    cmd = request.stm_sri512_read_blocks

    cmd.start_block = 7
    cmd.block_count = 3

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, read_pb2.Blocks())

def sri512_write(proto, payload):
    """ STM SRI512 Write Blocks """

    import intellireader.sri512.write_pb2 as write_pb2

    request = commands_pb2.StmCard()
    cmd = request.stm_sri512_write_blocks

    cmd.start_block = 7
    cmd.data = \
        b'\x00\x01\x02\x03' + b'\x04\x05\x06\x07' + b'\x08\x09\x0A\x0B' + b'\x0C\x0D\x0E\x0F'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

cmds = [sri512_read, sri512_write]
