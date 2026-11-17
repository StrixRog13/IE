import telnetlib


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self._write_line(username)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self.telnet.expect([b">"])
        self._write_line("enable")
        self.telnet.read_until(b"Password:")
        self._write_line(secret)
        self.telnet.expect([b"#"])

    def _write_line(self, line):
        self.telnet.write(line.encode("ascii") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        output = self.telnet.read_until(b"#")
        return output.decode("utf-8")
