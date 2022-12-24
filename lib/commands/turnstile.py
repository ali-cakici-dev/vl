from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import lib.proto

def allow_one_pass(proto, payload):
    """ Opens turnstile and wait for pass """

    import intellireader.turnstile.passage_pb2 as passage_pb2

    request = commands_pb2.Turnstile()
    cmd = request.allow_one_pass
    cmd.timeout_ms = 9000

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

cmds = [allow_one_pass]
