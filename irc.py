#!/usr/bin/env python3

"""IntelliReader Demo Controller, Terminal Technologies (c)

Usage:
  irc.py [options] (<cmd> [<payload>])...
  irc.py -h | --help
  irc.py -V | --version
  irc.py -l | --list
  irc.py -r | --interactive [options]

Arguments:
  <payload>  Part of Protobuf message that will be merged into request.

Options:
  -h --help                     Show this message.
  -V --version                  Show version of irc.py.
  -l --list                     List available commands.
  -r --interactive              Run irc in an interactive mode.
  -c --com-port <com-port>      COM-port to which the IntelliReader is connected.
  -i --ip-addr <host>[:port]    IP-address and optionally TCP-port of IntelliReader.
  -f --file <file name>         File name for reading response dump.
  -d --dump <short|hex|full>    Verbosity of message dump [default: short].
  -s --start-counter <number>   Start message counter from <number> [default: 0].
  -b --baudrate <bps>           Set baudrate for COM-port [default: 115200].
  -t --ssl                      Establish TLS connection over TCP-connection.
  -o --loop                     Repeat the commands in the loop.

Examples:
  Choose non-default COM-port:
    irc.py --com-port COM1 device_info

  Show full dump of the interaction:
    irc.py --dump full leds

  Run command with customized payload, enable the Blue LED:
    irc.py leds 'blue: true'

  Run multiple chained commands:
    irc.py device_info '' leds 'green: true'
"""

from docopt import docopt

import sys
sys.path.append('protocol')
sys.path.append('protocol/intellireader')

import time
import serial
import signal
import socket
import importlib

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

import lib.commander
from lib.proto import Protocol
from lib.transport import choose_transport
from lib.dumper import restore_dump, error

def version():
    try:
        import version
        return version.ver
    except:
        return 'dev'

import re
parse_cmds_pattern = re.compile("((?P<cmd>\S+)( '(?P<pld>.*?)')?)( *?\| )?")
def parse(cmds):
    return [match.groupdict() for match in parse_cmds_pattern.finditer(cmds)]

class IRC:
    def sigint_handler(self, s, f):
        if self.proto.hard_cancel():
            sys.exit(1)

    def do_list(self):
        cmd_list = list(self.cmds)
        cmd_list.sort()
        max_cmd_width = len(max(cmd_list, key=len))
        format = "{{: <{cmd_width}}}:{{}}".format(cmd_width = max_cmd_width)

        print('Available commands:')
        for cmd in cmd_list:
            print(format.format(cmd, self.cmds[cmd].__doc__ or ""))

    def do_reload(self):
        print('Reloading commands...')
        importlib.reload(lib.commander)
        lib.commander.reload_commands()
        self.load_commands()

    def load_commands(self):
        irc.cmds = {}
        for cmd in lib.commander.get_commands():
            irc.cmds[cmd.__name__] = cmd

    def do_help(self):
        help = "IntelliReader Demo Controller Interactive Shell, Terminal Technologies (c).\n" \
          "Usage:\n" \
          " Print this message:\n" \
          "  > help\n" \
          " List available commands:\n" \
          "  > list\n" \
          " Reload command list:\n" \
          "  > reload\n" \
          " Exit interactive mode:\n" \
          "  > exit\n" \
          " Run command:\n" \
          "  > command\n" \
          " Run command with payload:\n" \
          "  > command 'payload'\n" \
          " Run command chain:\n" \
          "  > command1 command2 command3\n\n" \
          "Examples:\n" \
          " Run buzz command:\n" \
          "  > buzz\n" \
          " Light up red led:\n" \
          "  > leds 'red: true'\n" \
          " Run buzz command and on success light up green led:\n" \
          "  > buzz leds 'green: true'"
        print(help)

    def do_exit(self):
        sys.exit(0)

    def batch(self, loop):
        cmd_num = len(self.arguments['<cmd>'])
        while True:
            for i in range(0, cmd_num):
                cmd = self.arguments['<cmd>'][i]
                pld = self.arguments['<payload>'][i] if i < len(self.arguments['<payload>']) else None
                if not self.do_command(cmd, pld):
                    if not loop:
                        sys.exit(1)
                    else:
                        break

            if not loop:
                break

    def interactive(self):
        signal.signal(signal.SIGINT, self.sigint_handler)
        commands = WordCompleter(self.cmds)

        session = PromptSession(
            history=FileHistory('.irc_history'),
            auto_suggest=AutoSuggestFromHistory(),
            completer=commands,
            enable_history_search=True,
        )

        while True:
            try:
                cmd_line = session.prompt('> ')
                cmds = parse(cmd_line)
                for cmd in cmds:
                    command = cmd['cmd']
                    payload = cmd['pld']
                    if command == 'help' or command == '?':
                        self.do_help()
                    elif command == 'exit' or command == 'quit' or command == 'q':
                        self.do_exit()
                    elif command == 'list':
                        self.do_list()
                    elif command == 'reload':
                        self.do_reload()
                    elif not self.do_command(command, payload):
                        break
            except KeyboardInterrupt:
                sys.exit(0)
            except (ConnectionError, serial.serialutil.SerialException) as e:
                print(e)
                self.setup_protocol()
            except Exception as e: print(e)

    def do_command(self, cmd, pld):
        if cmd not in self.cmds:
            return error("Error: Unknown command [{cmd}]".format(cmd=cmd))

        restore_dump()

        print("Running [{cmd}] ...".format(cmd = cmd))

        t0 = time.time()
        res = self.cmds[cmd](self.proto, pld)
        elapsed = time.time() - t0

        print("Command [{cmd}] took {elapsed:.2f} ms".format(cmd=cmd, elapsed=elapsed * 1000))
        return res

    def setup_protocol(self):
        dump_lvl = self.arguments['--dump']
        counter = self.arguments['--start-counter']
        self.proto = Protocol(choose_transport(self.arguments), dump_lvl, counter)

if __name__ == '__main__':
    irc = IRC()
    irc.arguments = docopt(__doc__, version=version())

    irc.load_commands()

    print("IntelliReader Demo Controller, Terminal Technologies (c), v.", version())

    if irc.arguments['--list']:
        irc.do_list()
        sys.exit(0)

    irc.setup_protocol()

    if irc.arguments['--interactive']:
        irc.interactive()
    else:
        loop = irc.arguments['--loop']
        irc.batch(loop)
