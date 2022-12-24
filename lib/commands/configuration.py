from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2
import intellireader.srv.upload_config_pb2 as config_pb2

import os
import time
import sys

from lib.dumper import suspend_dump

def upload_configuration(proto, payload):
    """ Upload configuration file ('config.zip' by default) to device """

    request = commands_pb2.Service()

    # treat payload as path to configuration file
    filepath = payload or "config.zip"
    image = open(filepath, "rb")
    filesize = os.path.getsize(filepath)

    prepare = request.prepare_for_config
    prepare.config_size = filesize
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
        sys.stdout.write("Sending config data... {:.2f}%\r".format(saved * 100.0 / filesize))
        sys.stdout.flush()

        upload_block = request.upload_block_of_config
        upload_block.data = buf
        if not proto.exchange(request, None):
            return False

    return check_configuration(proto, None)


def check_configuration(proto, payload):
    """ Check uploaded configuration """

    request = commands_pb2.Service()
    check_config = request.check_configuration
    check_config.SetInParent()

    config = config_pb2.Configuration()

    suspend_dump() # don't spam by image raw data
    if not proto.exchange(request, config):
        return False

    if not config.files:
        print("No configuration uploaded")
        return True

    format = "{: <30}{: <10}"
    header = format + "{}"
    rows = format + "0x{:08x}"
    
    print("")
    print("Configuration CRC32: 0x{:08x}".format(config.crc32))
    print("Configuration files:")

    print("")
    print(header.format("Name", "Size", "CRC32"))
    for file in config.files:
        print(rows.format(file.name.decode(), file.size, file.crc32))
    print("")

cmds = [upload_configuration, check_configuration]

from .service import responses
responses.update({
    'check_configuration': config_pb2.Configuration(),
})
