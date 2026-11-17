from netmiko.cisco.cisco_ios import CiscoIosSSH


class ErrorInCommand(Exception):
    """Исключение генерируется, если при выполнении команды на оборудовании возникла ошибка"""


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enable()

    def check_error_in_command(self, command, output):
        error_markers = {
            "Invalid input detected": r'Invalid input detected at "^" marker',
            "Incomplete command": "Incomplete command",
            "Ambiguous command": "Ambiguous command",
        }
        for marker, text in error_markers.items():
            if marker in output:
                raise ErrorInCommand(
                    "При выполнении команды " + repr(command) + " на устройстве "
                    + str(self.host) + " возникла ошибка -> " + text
                )

    def send_command(self, command):
        output = super().send_command(command)
        self.check_error_in_command(command, output)
        return output

    def send_config_set(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        output = self.config_mode()
        for command in commands:
            output += self.send_command(command)
        output += self.exit_config_mode()
        return output
