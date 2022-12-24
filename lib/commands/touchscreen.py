from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import lib.proto

def poll_touchscreen_widget(proto, payload):
    """ Poll touchscreen for widget pressed event """

    import intellireader.touchscreen.poll_touchscreen_pb2 as poll_touchscreen_pb2
    import intellireader.touchscreen.touchscreen_event_pb2 as touchscreen_event_pb2

    request = commands_pb2.Touchscreen()
    cmd = request.poll_touchscreen
    cmd.timeout = 5000
    cmd.event_type = poll_touchscreen_pb2.WIDGET_ID

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, touchscreen_event_pb2.TouchscreenEvent())

def poll_touchscreen_coords(proto, payload):
    """ Poll touchscreen for press in any point """

    import intellireader.touchscreen.poll_touchscreen_pb2 as poll_touchscreen_pb2
    import intellireader.touchscreen.touchscreen_event_pb2 as touchscreen_event_pb2

    request = commands_pb2.Touchscreen()
    cmd = request.poll_touchscreen
    cmd.timeout = 5000
    cmd.event_type = poll_touchscreen_pb2.COORDINATES

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, touchscreen_event_pb2.TouchscreenEvent())

cmds = [poll_touchscreen_widget, poll_touchscreen_coords]
