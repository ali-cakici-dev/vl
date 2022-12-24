import intellireader.commands_pb2 as commands_pb2

import intellireader.misc.leds_pb2 as leds_pb2

import lib.proto

def polling(proto):
    request = commands_pb2.Miscellaneous()
    request.set_leds_state.blue = True
    request.set_leds_state.yellow = False
    request.set_leds_state.green = False
    request.set_leds_state.red = False

    return proto.exchange(request, None)

def read_ok(proto):
    request = commands_pb2.Miscellaneous()
    request.set_leds_state.blue = True
    request.set_leds_state.yellow = True
    request.set_leds_state.green = True
    request.set_leds_state.red = False

    return proto.exchange(request, None)
