#!/usr/bin/env python3

"""
Usage:
  demo.py [options]
  demo.py -h | --help

Options:
  -h --help                     Show this message.
  -c --com-port <com-port>      COM-port to which the IntelliReader is connected.
  -i --ip-addr <host>[:port]    IP-address and optionally TCP-port of IntelliReader.
  -b --baudrate <bps>           Set baudrate for COM-port [default: 115200].
  -t --ssl                      Establish TLS connection over TCP-connection.
  -q --qrcode                   Use QR-code scanner.
  -g --gui                      Use LCD display.
"""

from docopt import docopt

import sys

sys.path.append('protocol')
sys.path.append('protocol/intellireader')

from lib.proto import Protocol
from lib.transport import choose_transport
from lib.demo.controller import DemoController

if __name__ == '__main__':
    print("IntelliReader Demo Application, Terminal Technologies (c)")

    arguments = docopt(__doc__)

    transport = choose_transport(arguments)
    proto = Protocol(transport, dump_lvl='short', counter=0)

    qrcode = arguments['--qrcode']
    gui = arguments['--gui']

    dc = DemoController(proto, qrcode, gui)
    dc.run()
