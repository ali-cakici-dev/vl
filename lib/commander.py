from .proto import Protocol
import intellireader.commands_pb2 as commands_pb2
from . import commands
from .commands import cipurse
from .commands import complex
from .commands import configuration
from .commands import contact
from .commands import contactless
from .commands import control
from .commands import gui
from .commands import mario
from .commands import mifare
from .commands import mifare_ext
from .commands import mifare_ext_samav2
from .commands import misc
from .commands import ntag
from .commands import pinpad
from .commands import plus
from .commands import qrcode
from .commands import service
from .commands import stm_sri512
from .commands import touchscreen
from .commands import troika
from .commands import turnstile
from .commands import ultralight
from .commands import update

def gui_tests_cmds():
    try:
        from .tests.gui_tests import cmds as gui_cmds
        return gui_cmds
    except ImportError:
        return []

def mifare_tests_cmds():
    try:
        from .tests.mifare_tests import cmds as mifare_cmds
        return mifare_cmds
    except ImportError:
        return []

def puzzle_cmds():
    try:
        from .tests.puzzle import cmds as puzzle_cmds
        return puzzle_cmds
    except ImportError:
        return []

def get_commands():
    return cipurse.cmds + complex.cmds + configuration.cmds + \
        contact.cmds + contactless.cmds + control.cmds + \
        gui.cmds + mario.cmds + mifare.cmds + mifare_ext.cmds + mifare_ext_samav2.cmds + \
        misc.cmds + ntag.cmds + pinpad.cmds + \
        plus.cmds + qrcode.cmds + service.cmds + stm_sri512.cmds + \
        update.cmds + touchscreen.cmds + troika.cmds + turnstile.cmds + ultralight.cmds + \
        gui_tests_cmds() + mifare_tests_cmds() + puzzle_cmds()

def get_module(req):
    for module, msg in MODULES.items():
        if type(req) == type(msg[0]):
            return module

    return None

def reload_commands():
    from importlib import reload

    reload(cipurse)
    reload(complex)
    reload(configuration)
    reload(contact)
    reload(contactless)
    reload(control)
    reload(gui)
    reload(mario)
    reload(mifare)
    reload(mifare_ext)
    reload(mifare_ext_samav2)
    reload(misc)
    reload(ntag)
    reload(pinpad)
    reload(plus)
    reload(qrcode)
    reload(service)
    reload(stm_sri512)
    reload(touchscreen)
    reload(troika)
    reload(turnstile)
    reload(ultralight)
    reload(update)

MODULES = {
    Protocol.MOD_MISC        : (commands_pb2.Miscellaneous(), 'misc_cmd', misc.responses),
    Protocol.MOD_CONTACT_L1  : (commands_pb2.ContactLevel1(), 'contact_level1_cmd', contact.responses),
    Protocol.MOD_CONTACT_L2  : (commands_pb2.ContactLevel2(), 'contact_level2_cmd', contact.responses),
    Protocol.MOD_CLESS_L1    : (commands_pb2.ContactlessLevel1(), 'contactless_level1_cmd', contactless.responses),
    Protocol.MOD_CLESS_L2    : (commands_pb2.ContactlessLevel2(), 'contactless_level2_cmd', contactless.responses),
    Protocol.MOD_MIFARE      : (commands_pb2.Mifare(), 'mifare_cmd', mifare.responses),
    Protocol.MOD_PINPAD      : (commands_pb2.PinPad(), 'pinpad_cmd', None),
    Protocol.MOD_SRV         : (commands_pb2.Service(), 'srv_cmd', service.responses),
    Protocol.MOD_STMCARD     : (commands_pb2.StmCard(), 'stmcard_cmd', None),
    Protocol.MOD_NTAGCARD    : (commands_pb2.NtagCard(), 'ntagcard_cmd', None),
    Protocol.MOD_GUI         : (commands_pb2.Gui(), 'gui_cmd', None),
    Protocol.MOD_TOUCHSCREEN : (commands_pb2.Touchscreen(), 'touchscreen_cmd', None),
    Protocol.MOD_COMPLEX     : (commands_pb2.Complex(), 'complex_cmd', complex.responses),
    Protocol.MOD_QRCODE      : (commands_pb2.QrCode(), 'qrcode_cmd', qrcode.responses),
    Protocol.MOD_CIPURSE     : (commands_pb2.Cipurse(), 'cipurse_cmd', cipurse.responses),
    Protocol.MOD_TURNSTILE   : (commands_pb2.Turnstile(), 'turnstile_cmd', None),
    Protocol.MOD_MIFAREEXT   : (commands_pb2.MifareExtended(), 'mifare_cmd', mifare_ext.responses),
    Protocol.MOD_TROIKA      : (commands_pb2.TroikaCard(), 'troika_cmd', troika.responses),
}
