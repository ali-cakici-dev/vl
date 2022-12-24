import intellireader.commands_pb2 as commands_pb2

import intellireader.misc.buzzer_pb2 as buzzer_pb2

import lib.proto

def ok(proto):
    request = commands_pb2.Miscellaneous()
    cmd = request.make_sound

    note1 = cmd.melody.add()
    note1.frequency_hz = 1500
    note1.duration_ms = 200

    return proto.exchange(request, None)

