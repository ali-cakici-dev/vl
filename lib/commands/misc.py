import math
import time

from google.protobuf.text_format import *
from google.protobuf.message import *

import intellireader.commands_pb2 as commands_pb2

import intellireader.misc.device_pb2 as device_pb2
import intellireader.misc.leds_pb2 as leds_pb2
import intellireader.misc.reboot_pb2 as reboot_pb2
import intellireader.misc.buzzer_pb2 as buzzer_pb2
import intellireader.misc.stats_pb2 as stats_pb2
import intellireader.misc.echo_pb2 as echo_pb2
import intellireader.misc.baudrate_pb2 as baudrate_pb2
import intellireader.misc.event_pb2 as event_pb2
import intellireader.misc.lan_settings_pb2 as lan_settings_pb2

from lib.dumper import suspend_dump

def device_info(proto, payload):
    """ Get information about device """

    request = commands_pb2.Miscellaneous()
    cmd = request.read_device_info
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, device_pb2.DeviceInfo())

def device_status(proto, payload):
    """ Get runtime status of device """

    request = commands_pb2.Miscellaneous()
    cmd = request.get_device_status
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, device_pb2.DeviceStatus())

def leds(proto, payload):
    """ Manage state of the LEDS, switch off all LEDS by default """

    request = commands_pb2.Miscellaneous()
    leds = request.set_leds_state

    leds.blue = False
    leds.yellow = False
    leds.green = False
    leds.red = False

    if payload:
        Merge(payload, leds)

    return proto.exchange(request, None)

def reboot_device(proto, payload):
    """ Reboots device """

    request = commands_pb2.Miscellaneous()
    cmd = request.reboot_device

    cmd.mode = reboot_pb2.Reboot().NORMAL_MODE

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def management_mode(proto, payload):
    """ Switches (reboots) device into Management Mode """

    request = commands_pb2.Miscellaneous()
    cmd = request.reboot_device

    cmd.mode = reboot_pb2.Reboot().MANAGEMENT_MODE

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def buzz(proto, payload):
    """ Make some sound by the buzzer """

    request = commands_pb2.Miscellaneous()
    cmd = request.make_sound

    note1 = cmd.melody.add()
    note1.frequency_hz = 1500
    note1.duration_ms = 100
    note1.silence_duration_ms = 150

    note2 = cmd.melody.add()
    note2.frequency_hz = 1000
    note2.duration_ms = 100

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def device_stats(proto, payload):
    """ Get various statistic data from the device """

    from termcolor import cprint

    request = commands_pb2.Miscellaneous()
    cmd = request.get_device_statistic
    cmd.SetInParent()

    if payload:
        Merge(payload, cmd)

    response = stats_pb2.DeviceStatistic()

    if not proto.exchange(request, response):
        return False

    def format_lwip_stat(level, stats):
        tx = stats.xmit
        rx = stats.recv
        err = stats.chkerr + stats.lenerr + stats.memerr + stats.rterr + stats.proterr + stats.opterr + stats.err
        str = "{:4}: {}/{}/{}".format(level, tx, rx, err)

        if err != 0:
            cprint(str, 'red')
        else:
            print(str)

    print("\nlwIP statistic (tx/rx/err):")
    format_lwip_stat("Link", response.lwip.link)
    format_lwip_stat("ARP", response.lwip.arp)
    format_lwip_stat("IP", response.lwip.ip)
    format_lwip_stat("TCP", response.lwip.tcp)

    def format_ethernet_stat(num, port):
        str = "Port{}: Tx packets {:6} Rx packets {:6} Rx errors {:6} Dropped packets {:6}" \
            .format(num, port.tx_packets, port.rx_packets, port.rx_errors, port.txrx_dropped)
        if port.rx_errors != 0:
            cprint(str, 'red')
        else:
            print(str)

    if response.HasField('ethernet'):
        print("\nEthernet statistic:")
        format_ethernet_stat(1, response.ethernet.port1)
        format_ethernet_stat(2, response.ethernet.port2)
        format_ethernet_stat(3, response.ethernet.port3)

    print("\nEvent log:")
    now = time.time()
    for event in response.events:
        event_time = now - event.event_time_offset / 1000
        localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(event_time))
        fractional = int(math.modf(event_time)[0] * 1000)

        event_type = event.event_type
        decriptor = event_pb2.DESCRIPTOR.enum_types_by_name['EventType']
        event_name = decriptor.values_by_number[event_type].name

        event_line = '{localtime}.{fractional:0>3} {event_name:3}'.format(
                localtime = localtime,
                fractional = fractional,
                event_name = event_name)

        if event.HasField('event_info'):
            event_line += ': ' + event.event_info
        print(event_line)

    print("")

    return True

def echo(proto, payload):
    """ Get echo from device """
    
    request = commands_pb2.Miscellaneous()
    cmd = request.get_echo
    cmd.data = b'anything'

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, echo_pb2.Echo())

def check_connection(proto, payload):
    """ Check physical connection to the reader """

    import random
    from struct import pack
    import sys
    import time

    ITERATIONS = 256
    DATA_SIZE = 4096

    request = commands_pb2.Miscellaneous()
    cmd = request.get_echo
    rsp = echo_pb2.Echo()

    suspend_dump() # don't spam by raw data

    times = []
    start = time.time()
    tx_size = 0
    rx_size = 0

    for i in range(0, ITERATIONS):
        cmd.data = bytes(random.getrandbits(8) for _ in range(DATA_SIZE))

        sys.stdout.write("Proceeding... {:.2f}%\r".format(i * 100.0 / ITERATIONS))
        sys.stdout.flush()

        t0 = time.time()
        if not proto.exchange(request, rsp):
            return False
        t1 = time.time()

        times.append(t1 - t0)
        tx_size += len(cmd.data or '')
        rx_size += len(rsp.echo or '')

    finish = time.time()
    tsf_time = finish - start
    tx_size /= 1024
    rx_size /= 1024
    tsf_speed = (tx_size + rx_size) / tsf_time

    print("Transferred TX/RX {:.2f}/{:.2f}KiB totally at {:.2f} KiB/sec"
            .format(tx_size, rx_size, tsf_speed))

    max_time = max(times) * 1000
    min_time = min(times) * 1000
    avg_time = sum(times)/len(times) * 1000
    mdev = max_time - avg_time

    print("RTT min/avg/max/mdev = {:.2f}/{:.2f}/{:.2f}/{:.2f} ms".format(min_time, avg_time, max_time, mdev))

    result = device_stats(proto, payload)
    return result

def change_baudrate(proto, payload):
    """ Change reader's COM-port baudrate """

    request = commands_pb2.Miscellaneous()
    cmd = request.change_baudrate

    cmd.baudrate = baudrate_pb2.BPS_115200

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

def change_lan_settings(proto, payload):
    """ Change reader's LAN settings """

    request = commands_pb2.Miscellaneous()
    cmd = request.change_lan_settings

    cmd.lan_settings.dhcp.SetInParent()

    if payload:
        Merge(payload, cmd)

    return proto.exchange(request, None)

cmds = [device_info, device_status, leds, reboot_device, management_mode, buzz, device_stats, echo,
        check_connection, change_baudrate, change_lan_settings]

responses = {
    'set_leds_state': None,
    'read_device_info': device_pb2.DeviceInfo(),
    'reboot_device': None,
    'get_device_status': device_pb2.DeviceStatus(),
    'make_sound': None,
    'get_device_statistic': stats_pb2.DeviceStatistic(),
    'get_echo': echo_pb2.Echo(),
    'change_baudrate': None,
    'change_lan_settings': None,
}
