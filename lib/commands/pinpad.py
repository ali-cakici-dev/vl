from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2
import intellireader.pinpad.online_pin_pb2 as online_pin_pb2
import intellireader.pinpad.key_bundle_pb2 as key_bundle_pb2

def set_encryption_params(params):
    params.key_format = key_bundle_pb2.TR31

    # AES, ISO 9564 Format 4
    params.session_key = \
        b"D0112P0AE00E0000B82679114F470F540165EDFBF7E250FCEA43F810D215F8D207E2E417C07156A27E8E31DA05F7425509593D03A457DC34"

    params.pin_block_format = online_pin_pb2.ISO_9564_FORMAT_4

def online_pin(proto, payload):
    """ Ask cardholder to enter PIN & return PIN-block """

    request = commands_pb2.PinPad()
    cmd = request.online_pin

    cmd.pan = b"432198765432109870"
    set_encryption_params(cmd.encryption_params)

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, online_pin_pb2.EntryResult())

cmds = [online_pin]
