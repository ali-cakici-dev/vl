# -*- coding: utf-8 -*-

from textwrap import TextWrapper
import time
import os
import sys

import intellireader.commands_pb2 as commands_pb2

import intellireader.gui.alignment_pb2 as alignment_pb2
import intellireader.gui.background_pb2 as background_pb2
import intellireader.gui.border_pb2 as border_pb2
import intellireader.gui.font_pb2 as font_pb2
import intellireader.gui.screen_pb2 as screen_pb2
import intellireader.gui.solidfill_pb2 as solidfill_pb2
import intellireader.gui.picture_id_pb2 as picture_id_pb2
import intellireader.gui.widget_pb2 as widget_pb2

import lib.proto

from . import leds, buzz, types

last = (0, '')

def tap_card(proto):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture
    bottom = vl.widgets.add()

    text.text = 'KARTINIZI\n\nOKUTUNUZ'
    text.font = font_pb2.REGULAR_FONT

    picture.picture_id = picture_id_pb2.EMV_CONTACTLESS_SYMBOL

    ps_line(bottom)

    show_screen(proto, 'tap_card', cmd)


def tap_card_with_message(proto, message=''):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture
    bottom = vl.widgets.add()

    text.text = 'KARTINIZI\n\nOKUTUNUZ'
    text.font = font_pb2.REGULAR_FONT

    picture.picture_id = picture_id_pb2.EMV_CONTACTLESS_SYMBOL

    ps_line(bottom)

    show_screen(proto, 'tap_card', cmd)


def approve(proto, result):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = 'KART \n\n OKUTULDU'
    text.font = font_pb2.REGULAR_FONT

    picture.picture_id = picture_id_pb2.APPROVED

    border_ok(cmd)
    show_screen(proto, 'approve', cmd)


def approve_write(proto, result, message=""):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    # text.text = 'KART \n\n OKUTULDU'
    text.text = message.encode('utf-8')
    text.font = font_pb2.REGULAR_FONT

    picture.picture_id = picture_id_pb2.APPROVED

    border_ok(cmd)
    show_screen(proto, 'approve', cmd)


def decline(proto, result, message=''):
    try:
        cmd = commands_pb2.Gui().show_screen
        vl = cmd.root.vertical_layout

        text = vl.widgets.add().text
        picture = vl.widgets.add().picture

        text.text = message.encode('utf-8')
        text.font = font_pb2.REGULAR_FONT

        picture.picture_id = picture_id_pb2.REJECTED

        border_nok(cmd)
        show_screen(proto, 'decline', cmd)
    except Exception as e:
        print('ERROR - decline: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return None


def awaiting(proto, result, message=''):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = message.encode('utf-8')
    text.font = font_pb2.REGULAR_FONT

    picture.picture_id = picture_id_pb2.AWAITING

    border_nok(cmd)
    show_screen(proto, 'decline', cmd)


def write_screen(proto, result, message=''):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = message.encode('utf-8')
    text.font = font_pb2.REGULAR_FONT

    # picture.picture_id = picture_id_pb2.AWAITING

    # border_nok(cmd)
    show_screen(proto, 'write_screen', cmd)


def use_contact_iface(proto, result):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout
    
    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = 'НЕ c-\nc'
    text.font = font_pb2.LARGE_FONT

    picture.picture_id = picture_id_pb2.REJECTED

    border_nok(cmd)
    show_screen(proto, 'use_contact_iface', cmd)

def transport_card(proto, result):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout
    
    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = types.token_type_text(proto, result)
    text.font = font_pb2.LARGE_FONT
    text.vertical_alignment = alignment_pb2.OPTIMAL_VERTICALLY 
    
    picture.picture_id = picture_id_pb2.APPROVED

    border_ok(cmd)
    show_screen(proto, 'non_emv', cmd)

def expired(proto, result):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout
    
    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = 'b\nb\nb'
    text.font = font_pb2.LARGE_FONT

    picture.picture_id = picture_id_pb2.REJECTED

    border_nok(cmd)
    show_screen(proto, 'expired', cmd)

def cdcvm_required(proto, result):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout
    
    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = 'as ОТ\nsda'
    text.font = font_pb2.LARGE_FONT

    picture.picture_id = picture_id_pb2.REJECTED

    border_nok(cmd)
    show_screen(proto, 'cdcvm_required', cmd)

def non_emv(proto, result):
    leds.read_ok(proto)
    transport_card(proto, result)
    buzz.ok(proto)

def qrcode(proto, result):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    caption = vl.widgets.add().text
    text = vl.widgets.add().text

    caption.text = 'QR detected'
    caption.font = font_pb2.LARGE_FONT
    caption.vertical_alignment = alignment_pb2.OPTIMAL_VERTICALLY

    wrapper = TextWrapper()
    wrapper.width = 20
    wrapper.max_lines = 6

    text.text = wrapper.fill(result.raw_data.data.decode('utf-8', 'replace'))

    border_ok(cmd)
    show_screen(proto, 'qrcode', cmd)

def ts_coordinates(proto, result):
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    bottom = vl.widgets.add()

    coords = result.coordinates

    text.text = 'Touchscreen\ncoordinates\nX: {}\nY: {}'.format(coords.x, coords.y)
    text.font = font_pb2.LARGE_FONT

    ps_line(bottom)

    show_screen(proto, 'ts_coordinates', cmd)

def show_screen(proto, name, screen):
    global last
    last = (time.time(), name)

    request = commands_pb2.Gui()
    request.show_screen.CopyFrom(screen)

    return proto.exchange(request, None)

def ps_line(widget):
    hl = widget.horizontal_layout

    visa = hl.widgets.add()
    visa.picture.picture_id = picture_id_pb2.VISA_LOGO
    visa.picture.vertical_alignment = alignment_pb2.BOTTOM
    visa.picture.horizontal_alignment = alignment_pb2.LEFT

    mc = hl.widgets.add()
    mc.picture.picture_id = picture_id_pb2.MASTERCARD_LOGO
    mc.picture.vertical_alignment = alignment_pb2.BOTTOM

    mir = hl.widgets.add()
    mir.picture.picture_id = picture_id_pb2.MIR_LOGO
    mir.picture.vertical_alignment = alignment_pb2.BOTTOM
    mir.picture.horizontal_alignment = alignment_pb2.OPTIMAL_HORIZONTALLY

    upi = hl.widgets.add()
    upi.picture.picture_id = picture_id_pb2.UNIONPAY_LOGO
    upi.picture.vertical_alignment = alignment_pb2.BOTTOM
    upi.picture.horizontal_alignment = alignment_pb2.RIGHT

def border_ok(cmd):
    border(cmd, solidfill_pb2.SOLID_FILL_RED)

def border_nok(cmd):
    border(cmd, solidfill_pb2.SOLID_FILL_RED)

def border(cmd, color):
    border = cmd.border
    border.style = border_pb2.SOLID_BORDER
    border.color.solid_fill = color
