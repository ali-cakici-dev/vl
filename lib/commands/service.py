import os
from pyaes import AESModeOfOperationECB
from getpass import getpass
from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.srv.diagnostic_pb2 as diagnostic_pb2

# "Challenge protection key"
PROT_KEY = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF\xFE\xDC\xBA\x98\x76\x54\x32\x10'
# passwords values
PASS1 = '12345678'
PASS2 = '12345678'

def generate_challenge(proto, payload):
    """ Get Challenge """

    import intellireader.srv.challenge_pb2 as challenge_pb2

    # generate "Request Random Data"
    rand = os.urandom(16)

    # encrypt on "Challenge protection key" Request Random Data
    cipher = AESModeOfOperationECB(PROT_KEY)
    encrypted = cipher.encrypt(rand)

    request = commands_pb2.Service()
    challenge = request.get_challenge

    challenge.data = encrypted

    if payload:
        Merge(payload, challenge)

    response = challenge_pb2.Challenge()

    if not proto.exchange(request, response):
        return None

    # get encrypted on "Challenge protection key" Response Random Data
    encrypted = response.data

    # decrypt on "Challenge protection key" encrypted Response Random Data
    decrypted = cipher.decrypt(encrypted)

    # calculate "Challenge Data" = "Response Random Data" XOR "Request Random Data"
    challenge = [a ^ b for a, b in zip(decrypted, rand)]
    challenge = bytes(challenge)

    return challenge

def activate_prot(proto, payload):
    """ Activate anti-removal protection """

    import intellireader.srv.protection_pb2 as protection_pb2

    pswd = getpass('Enter password 1: ')
    if pswd != PASS1:
        print("Invalid password 1 value entered!")
        return False

    pswd = getpass('Enter password 2: ')
    if pswd != PASS2:
        print("Invalid password 2 value entered!")
        return False

    # get Challenge Data from terminal
    challenge = generate_challenge(proto, payload)
    if challenge is None:
        return False

    # encrypt on "Challenge protection key" Challenge Data
    cipher = AESModeOfOperationECB(PROT_KEY)
    encrypted = cipher.encrypt(challenge)

    request = commands_pb2.Service()
    cmd = request.activate_protection

    cmd.encrypted_challenge = encrypted

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def deactivate_prot(proto, payload):
    """ Deactivate anti-removal protection """

    import intellireader.srv.protection_pb2 as protection_pb2

    request = commands_pb2.Service()
    cmd = request.deactivate_protection
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def get_diagnostic(proto, payload):
    """ Get diagnostic info from the reader """

    request = commands_pb2.Service()
    cmd = request.get_diagnostic
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, diagnostic_pb2.DiagnosticInfo())

cmds = [activate_prot, deactivate_prot, get_diagnostic]

responses = {
    'get_diagnostic': diagnostic_pb2.DiagnosticInfo(),
}
