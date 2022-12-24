# encoding=utf8

import os
import time
from zipfile import ZipFile

from collections import OrderedDict

from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.gui.alignment_pb2 as alignment_pb2
import intellireader.gui.background_pb2 as background_pb2
import intellireader.gui.border_pb2 as border_pb2
import intellireader.gui.font_pb2 as font_pb2
import intellireader.gui.screen_pb2 as screen_pb2
import intellireader.gui.solidfill_pb2 as solidfill_pb2
import intellireader.gui.picture_id_pb2 as picture_id_pb2
import intellireader.gui.widget_pb2 as widget_pb2
import intellireader.gui.input_dialog_pb2 as input_dialog_pb2
import intellireader.gui.menu_dialog_pb2 as menu_dialog_pb2
import intellireader.gui.draw_bitmap_pb2 as draw_bitmap_pb2
import intellireader.gui.text_id_pb2 as text_id_pb2

def screen1():
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture
    bottom = vl.widgets.add()

    text.text = 'ПРИЛОЖИТЕ\nКАРТУ'
    text.font = font_pb2.LARGE_FONT

    picture.picture_id = picture_id_pb2.EMV_CONTACTLESS_SYMBOL

    ps_line(bottom)

    return cmd

def screen2():
    cmd = commands_pb2.Gui().show_screen

    border = cmd.border
    border.style = border_pb2.SOLID_BORDER
    border.color.solid_fill = solidfill_pb2.SOLID_FILL_GREEN

    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = 'ONAYLANDI\n'
    text.font = font_pb2.LARGE_FONT

    picture.picture_id = picture_id_pb2.APPROVED

    return cmd

def screen3():
    cmd = commands_pb2.Gui().show_screen

    border = cmd.border
    border.style = border_pb2.SOLID_BORDER
    border.color.solid_fill = solidfill_pb2.SOLID_FILL_RED

    vl = cmd.root.vertical_layout
    
    text = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text.text = 'ПРОЕЗД\nЗАПРЕЩЕН'
    text.font = font_pb2.LARGE_FONT

    picture.picture_id = picture_id_pb2.REJECTED

    return cmd

def screen4():
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    text.text = "BENİ OKU"
    text.font = font_pb2.LARGE_FONT
    text.vertical_alignment = alignment_pb2.OPTIMAL_VERTICALLY

    qr = vl.widgets.add().qr_code
    qr.text = "https://qr.t-vend.com/qpay/?qr-code=172631713&".encode()

    text = vl.widgets.add().text
    text.text = ""
    text.vertical_alignment = alignment_pb2.OPTIMAL_VERTICALLY

    return cmd


def screen5():
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    picture = vl.widgets.add().picture
    bottom = vl.widgets.add().vertical_layout

    text.text = 'ПРИЛОЖИТЕ\nКАРТУ'
    text.font = font_pb2.LARGE_FONT

    picture.picture_id = picture_id_pb2.EMV_CONTACTLESS_SYMBOL

    empty = bottom.widgets.add()
    button = bottom.widgets.add()

    button.text.text = 'OПЛАТA БАГАЖА'
    button.text.background.solid_fill_rgb = 0x99FFFF
    button.text.foreground.solid_fill_rgb = 0x000000
    button.text.button_id = 0
    button.text.border.style = border_pb2.OUTSET_BORDER

    return cmd


def screen6():
    def button(parent, text, id):
        b = parent.widgets.add().text
        b.text = text
        b.background.solid_fill_rgb = 0x99FFFF
        b.foreground.solid_fill_rgb = 0x000000
        b.button_id = id
        b.border.style = border_pb2.SOLID_BORDER

    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    caption = vl.widgets.add().text
    line1 = vl.widgets.add().horizontal_layout
    line2 = vl.widgets.add().horizontal_layout

    caption.text = 'SEÇİM YAPINIZ \n '
    caption.vertical_alignment = alignment_pb2.OPTIMAL_VERTICALLY

    button(line1, '5 TL \n 5 Dakika', 0)
    button(line1, '10 TL \n 10 Dakika', 1)

    button(line2, '15 TL \n 15 Dakika', 2)
    button(line2, '20 TL \n 20 Dakika', 3)

    return cmd


def yes_no_dialog2(proto, payload):
    """ Show Yes/No dialogue """

    request = commands_pb2.Gui()
    cmd = request.menu_dialog

    cmd.caption = 'Seçim yapınız.'

    MENU = { '5 TL 5 Dakika': 1, '10 TL 10 Dakika': 2,'15 TL 15 Dakika':3 }
    make_menu(cmd.item_list, MENU)

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, menu_dialog_pb2.SelectedItem()), request

def yes_no_dialog(proto, payload):
    """ Show Yes/No dialogue """

    request = commands_pb2.Gui()
    cmd = request.menu_dialog

    cmd.caption = 'It\'s a Yes/No\ndialog example.\nContinue?'

    MENU = { 'Going forward': 1, 'Sorry, not now': 2 }
    make_menu(cmd.item_list, MENU)

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, menu_dialog_pb2.SelectedItem())


# Lütfen Bekleyiniz Ekranı
def screen7():
    cmd = commands_pb2.Gui().show_screen
    vl = cmd.root.vertical_layout

    text = vl.widgets.add().text
    text2 = vl.widgets.add().text
    text3 = vl.widgets.add().text
    text4 = vl.widgets.add().text
    picture = vl.widgets.add().picture
    bottom = vl.widgets.add().vertical_layout

    text.text = '\n'.encode()
    text.font = font_pb2.LARGE_FONT

    text2.text = 'İŞLEMİNİZ YAPILIYOR'.encode()
    text2.font = font_pb2.REGULAR_FONT

    text3.text = '\n'.encode()
    text3.font = font_pb2.LARGE_FONT

    text4.text = '\nLÜTFEN BEKLEYİN'.encode()
    text4.font = font_pb2.REGULAR_FONT

    # picture.picture_id = picture_id_pb2.EMV_CONTACTLESS_SYMBOL

    # empty = bottom.widgets.add()
    # button = bottom.widgets.add()
    #
    # button.text.text = 'OПЛАТA БАГАЖА'
    # button.text.background.solid_fill_rgb = 0x99FFFF
    # button.text.foreground.solid_fill_rgb = 0x000000
    # button.text.button_id = 0
    # button.text.border.style = border_pb2.OUTSET_BORDER

    return cmd


def screen8(message):
    cmd = commands_pb2.Gui().show_screen

    border = cmd.border
    border.style = border_pb2.SOLID_BORDER
    border.color.solid_fill = solidfill_pb2.SOLID_FILL_RED

    vl = cmd.root.vertical_layout

    text2 = vl.widgets.add().text
    picture = vl.widgets.add().picture

    text2.text = message.encode()
    text2.font = font_pb2.REGULAR_FONT

    picture.picture_id = picture_id_pb2.REJECTED

    return cmd


def show_screen_qr(proto, payload):
    """ Show user-define screen on reader's display """

    if not payload:
        screen = globals()["screen4"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    return proto.exchange(request, None)


def show_all_screens(proto, payload):
    """ Show user-define screen on reader's display """
    print('************ SCREEN1 ************')
    if not payload:
        screen = globals()["screen1"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    proto.exchange(request, None)

    time.sleep(5)
    print('************ SCREEN2 ************')

    if not payload:
        screen = globals()["screen2"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    proto.exchange(request, None)

    time.sleep(5)

    print('************ SCREEN3 ************')
    if not payload:
        screen = globals()["screen3"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    proto.exchange(request, None)

    time.sleep(5)
    print('************ SCREEN4 ************')
    if not payload:
        screen = globals()["screen4"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    proto.exchange(request, None)

    time.sleep(5)

    print('************ SCREEN5 ************')
    if not payload:
        screen = globals()["screen5"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    proto.exchange(request, None)

    time.sleep(5)

    print('************ SCREEN6 ************')
    if not payload:
        screen = globals()["screen6"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    time.sleep(5)

    return proto.exchange(request, None)


def show_screen(proto, payload):
    """ Show user-define screen on reader's display """

    if not payload:
        screen = globals()["screen3"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    return proto.exchange(request, None)


def show_screen_wait(proto, payload):
    """ Show user-define screen on reader's display """

    if not payload:
        screen = globals()["screen7"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    return proto.exchange(request, None)


def show_screen_approved(proto, payload):
    """ Show user-define screen on reader's display """

    if not payload:
        screen = globals()["screen2"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    return proto.exchange(request, None)


def show_screen_declined(proto, payload, message):
    """ Show user-define screen on reader's display """

    if not payload:
        screen = globals()["screen8"]
        payload = MessageToString(screen(message))
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen(message))

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    return proto.exchange(request, None)


def show_screen_multi_products(proto, payload):
    """ Show user-define screen on reader's display """

    if not payload:
        screen = globals()["screen6"]
        payload = MessageToString(screen())
    else:
        screen = globals().get(payload)

        if screen:
            payload = MessageToString(screen())

    request = commands_pb2.Gui()
    cmd = request.show_screen
    Merge(payload, cmd)

    return proto.exchange(request, None)


def input_dialog(proto, payload):
    """ Show input dialogue """
    
    request = commands_pb2.Gui()
    cmd = request.input_dialog

    cmd.caption = 'INPUT NAME'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, input_dialog_pb2.EnteredText())

def make_menu(item_list, items):
    for item_text, item_content in items.items():
       menu_item = item_list.items.add()
       menu_item.text = item_text

       if isinstance(item_content, int):
           menu_item.leaf_item.id = item_content
       else:
           menu_item.submenu.SetInParent()
           make_menu(menu_item.submenu, item_content)

def menu_dialog(proto, payload):
    """ Show menu dialogue """

    request = commands_pb2.Gui()
    cmd = request.menu_dialog

    cmd.caption = 'Choose an item'

    MENU = OrderedDict([
        ('item1', 1),
        ('item2', OrderedDict([
            ('sub item1', 11),
            ('sub item2', 12),
            ('sub item3', OrderedDict([
                ('sub sub item1', 111),
                ('sub sub item2', 112),
            ])),
        ])),
        ('item3', 3),
        ('item4', 4),
        ('item5', 5),
        ('item6', 6),
        ('item7', 7),
        ('item8', 8),
        ('item9', 9),
        ('item10', 10),
        ('item11', 11),
        ('item12', 12),
        ('item13', 13),
    ])

    make_menu(cmd.item_list, MENU)

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, menu_dialog_pb2.SelectedItem())


def deflate(data):
    import zlib
    deflated = zlib.compress(data)
    return deflated[2:] # cut zlib header

def draw(proto, data, x, y, width, height):
    request = commands_pb2.Gui()
    cmd = request.draw_bitmap
    area = cmd.area

    area.x = x
    area.y = y
    area.width = width
    area.height = height

    from lib.dumper import suspend_dump
    suspend_dump() # don't spam by image raw data

    compressed = deflate(data)

    while len(compressed) != 0:
        min_len = min(len(compressed), 4096)
        cmd.data = compressed[:min_len]

        if not proto.exchange(request, None):
            return False

        cmd.ClearField('area')
        compressed = compressed[min_len:]

    return True

def draw_bitmap(proto, payload):
    """ Draw randomly generated rectangles on the LCD """

    import random

    for _ in range(0, 100):
        [x0, x1] = random.sample(range(0, 320), 2)
        [y0, y1] = random.sample(range(0, 480), 2)

        x = min(x0, x1)
        width = abs(x0 - x1)

        y = min(y0, y1)
        height = abs(y0 - y1)

        color = random.sample(range(0, 255), 3)
        data = bytearray(width * height * color)

        draw(proto, data, x, y, width, height)

def slideshow(proto, payload):
    """ Draw slideshow using customer picture """

    request = commands_pb2.Gui()
    cmd = request.slideshow

    # the picture from config.zip
    cmd.name = "visa.bmp"
    cmd.frames_count = 33
    cmd.delay_ms = 40
    cmd.background.solid_fill = solidfill_pb2.SOLID_FILL_WHITE

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def show_picture(proto, filename):
    """ Show a customer picture at the center of screen """

    request = commands_pb2.Gui()

    # the picture from config.zip
    request.show_screen.root.customer_picture.name = filename or "luggage.bmp"

    return proto.exchange(request, None)

def awaiting_connection_screen(proto, payload):
    """ Show custom 'Awaiting Connection' screen and save it to config.zip """

    request = commands_pb2.Gui()

    cmd = request.show_screen
    vl = cmd.root.vertical_layout

    info = vl.widgets.add().vertical_layout

    error = info.widgets.add().generated_text
    downtime = info.widgets.add().generated_text
    picture = vl.widgets.add().picture
    bottom = vl.widgets.add()

    error.prefix = 'Карты не принимаются\n'
    error.text_id = text_id_pb2.SERIAL_NUMBER
    error.vertical_alignment = alignment_pb2.OPTIMAL_VERTICALLY

    downtime.text_id = text_id_pb2.DOWNTIME
    downtime.vertical_alignment = alignment_pb2.OPTIMAL_VERTICALLY

    picture.picture_id = picture_id_pb2.REJECTED

    ps_line(bottom)

    if not proto.exchange(request, None):
        return False

    configname = 'config.zip'
    filename = "awaiting_connection.bin"
    pbdata = cmd.SerializeToString()

    os.remove(configname)

    with ZipFile(configname, 'a') as config:
        config.writestr(filename, pbdata)
        config.close()

    print('Configration file with custom awaiting screen has been created: {}'.format(configname))
    return True

def fonts(proto, payload):
    """ Show built-in fonts """

    request = commands_pb2.Gui()
    text = 'WWWWW\n.....'

    cmd = request.show_screen
    vl = cmd.root.vertical_layout

    large = vl.widgets.add().text
    large.text = text
    large.font = font_pb2.LARGE_FONT

    regular = vl.widgets.add().text
    regular.text = text
    regular.font = font_pb2.REGULAR_FONT

    monospace = vl.widgets.add().text
    monospace.text = text
    monospace.font = font_pb2.MONOSPACE_FONT

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

cmds = [show_screen, show_screen_approved, show_screen_declined, show_screen_wait, input_dialog, menu_dialog, yes_no_dialog, draw_bitmap, slideshow, show_picture,
        awaiting_connection_screen, fonts]
