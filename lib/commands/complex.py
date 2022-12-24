import time

from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.complex.poll_for_event_pb2 as poll_for_event_pb2
import intellireader.touchscreen.poll_touchscreen_pb2 as poll_touchscreen_pb2
import intellireader.gui.border_pb2 as border_pb2

import lib.proto
from lib.commands import troika

def poll_for_event(proto, payload):
    """ Poll for an event from multiple reader interfaces """

    request = commands_pb2.Complex()
    cmd = request.poll_for_event

    cmd.perform_txn.poll_for_token.timeout = 10 * 1000
    cmd.perform_txn.poll_for_token.poll_stm_sri512 = True
    cmd.perform_txn.poll_for_token.prefer_mifare = False

    cmd.perform_txn.amount_authorized = 100 # 1.00$
    cmd.perform_txn.transaction_date = b'\x13\x06\x13'
    cmd.perform_txn.transaction_time = b'\x12\x00\x00'
    cmd.perform_txn.transaction_type = b'\x00'
    cmd.perform_txn.terminal_country_code = b'\x06\x43'
    cmd.perform_txn.transaction_currency_code = b'\x06\x43'

    cmd.poll_touchscreen.event_type = poll_touchscreen_pb2.WIDGET_ID

    # uncomment to enable QR-code polling
    # cmd.poll_for_qrcode.SetInParent()

    on_start(cmd.on_start_ui_action)
    on_event(cmd.on_event_ui_action)
    on_mifare(cmd.on_mifare_card_present)

    return proto.exchange(request, poll_for_event_pb2.Event())

def on_start(gui):
    leds = gui.set_leds_state
    leds.blue = True
    leds.yellow = False
    leds.green = False
    leds.red = False

    screen = gui.show_screen
    vl = screen.root.vertical_layout
    vl.widgets.add().text.text = 'Pool for an\nevent example...'

    empty = vl.widgets.add()
    empty = vl.widgets.add()
    empty = vl.widgets.add()

    b = vl.widgets.add().text
    b.text = 'Cancel'
    b.button_id = 0
    b.background.solid_fill_rgb = 0x99FFFF
    b.foreground.solid_fill_rgb = 0x000000
    b.border.style = border_pb2.INSET_BORDER

def on_event(gui):
    leds = gui.set_leds_state
    leds.blue = True
    leds.yellow = True
    leds.green = True
    leds.red = True

    screen = gui.show_screen
    screen.root.text.text = 'Some event\nhas been occured.'

def on_mifare(action):
    troika.read_ticket_init(action.troika_av3_read_ticket)

cmds = [poll_for_event]

responses = {
    'poll_for_event': poll_for_event_pb2.Event(),
}
