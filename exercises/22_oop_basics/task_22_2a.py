import re
import textfsm
from task_22_2 import CiscoTelnet as BaseCiscoTelnet


class CiscoTelnet(BaseCiscoTelnet):
    def __init__(self, ip, username, password, secret):
        super().__init__(ip, username, password, secret)

    def send_show_command(self, command, parse=True, templates="templates", index="index"):
        self._write_line(command)
        command_output = self.telnet.read_until(b"#").decode("utf-8")
        if not parse:
            return command_output
        with open(index) as f:
            index_content = f.read()
        template = None
        for line in index_content.splitlines():
            template_name, regex, description = line.split(",")
            if re.search(regex, command):
                template = templates + "/" + template_name
                break
        if template is None:
            print("Шаблон не найден")
            return command_output
        with open(template) as f:
            fsm = textfsm.TextFSM(f)
        result = fsm.ParseText(command_output)
        return [dict(zip(fsm.header, row)) for row in result]
