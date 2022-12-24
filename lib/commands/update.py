from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2
import intellireader.srv.firmware_update_pb2 as update_pb2
import os
import sys
import time

from lib.dumper import suspend_dump

def update_firmware(proto, payload):
    """ Update device's firmware ('reader.bin') """

    request = commands_pb2.Service()

    # treat payload as path to firmware image file
    filepath = payload
    if not filepath:
        print('Please, provide firmware image file (reader-*.bin.signed) as an argument')
        return False

    image = open(filepath, "rb")
    filesize = os.path.getsize(filepath)

    prepare = request.prepare_update
    prepare.firmware_image_size = filesize

    if not proto.exchange(request, None):
        return False

    suspend_dump() # don't spam by image raw data

    saved = 0
    t0 = time.time()

    while True:
        buf = image.read(4096)
        if len(buf) == 0:
            elapsed = time.time() - t0
            print("\nDone in {:.2f} s".format(elapsed))
            break

        saved += len(buf)
        sys.stdout.write("Sending firmware data... {:.2f}%\r".format(saved * 100.0 / filesize))
        sys.stdout.flush()

        update_block = request.update_block
        update_block.data = buf
        if not proto.exchange(request, None):
            return False

    apply_cmd = request.apply_update
    apply_cmd.restart = True
    return proto.exchange(request, None)

def rollback_update(proto, payload):
    """ Rollback device's firmware update """

    request = commands_pb2.Service()
    cmd = request.rollback_update
    cmd.SetInParent()

    return proto.exchange(request, None)

cmds = [update_firmware, rollback_update]
