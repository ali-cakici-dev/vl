import serial
import socket
import sys
import errno
import ssl

class tcp_transport(socket.socket):
    def write(self, buf):
        self.sendall(buf)

    def read(self, lenght):
        buf = bytes(0)
        try:
            while len(buf) < lenght:
                buf += self.recv(lenght - len(buf))
        except socket.timeout:
            pass
        except OSError as e:
            if e.errno != errno.EINTR:
                raise
        return buf

class ssl_transport():
    def __init__(self, ssock):
        self.ssock = ssock

    def write(self, buf):
        self.ssock.sendall(buf)

    def read(self, lenght):
        buf = bytes(0)
        try:
            while len(buf) < lenght:
                buf += self.ssock.recv(lenght - len(buf))
        except socket.timeout:
            pass
        except OSError as e:
            if e.errno != errno.EINTR:
                raise
        return buf

    def settimeout(self, timeout):
        self.ssock.settimeout(timeout)

    def gettimeout(self):
        return self.ssock.gettimeout()


class com_transport(serial.Serial):
    def settimeout(self, timeout):
        self.timeout = timeout

    def gettimeout(self):
        return self.timeout

    def enable_low_latency_mode(self):
        import array
        import fcntl
        import termios

        buf = array.array('i', [0] * 32)

        try:
            # get serial_struct
            fcntl.ioctl(self.fd, termios.TIOCGSERIAL, buf)

            # set ASYNC_LOW_LATENCY flag
            buf[4] |= 0x2000

            # set serial_struct
            fcntl.ioctl(self.fd, termios.TIOCSSERIAL, buf)
        except IOError as e:
            print('Warning: Failed to set ASYNC_LOW_LATENCY flag: {}'.format(e))

def default_uart_port():
    import sys
    import platform
    from serial.tools import list_ports

    for port, name, _ in list_ports.comports():
        if name == 'IntelliReader':
            return port

    if sys.platform == 'win32':
        return list_ports.comports()[0][0]
    elif platform.node() == 'msm8909':
        return '/dev/ttyUSB3'
    else:
        return '/dev/ttyUSB0'

def default_tcp_port(args):
    if not args['--ssl']:
        return [42616]
    else:
        return [42800]

def choose_transport(args):
    ip_addr = args['--ip-addr']
    port = args['--com-port'] or default_uart_port()
    baudrate = args['--baudrate'] or "115200"
    if ip_addr:
        addr, port = (ip_addr.split(':') + default_tcp_port(args))[:2]
        port = int(port)

        print('Using TCP', ip_addr)
        tcp = tcp_transport(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect((addr, port))

        if not args['--ssl']:
            return tcp

        print('Establishing TLS')
        context = ssl.create_default_context(cafile='clientid_ca.pem')

        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = False

        ssock = context.wrap_socket(tcp)

        return ssl_transport(ssock)
    else:
        print('Using UART', port)
        uart = com_transport(
            port=port,
            baudrate=int(baudrate),
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
        )
        uart.reset_input_buffer()

        plat = sys.platform.lower()
        if plat[:5] == 'linux':
            uart.enable_low_latency_mode()

        return uart
