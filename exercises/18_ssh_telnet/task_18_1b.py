# -*- coding: utf-8 -*-
"""
Задание 18.1b

Скопировать функцию send_show_command из задания 18.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется при ошибке
аутентификации на устройстве, но и исключение, которое генерируется, когда IP-адрес
устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться
сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""

import yaml
from netmiko import (
    ConnectHandler,
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)

def send_show_command(device, command):
    """Подключается к устройству по SSH и выполняет команду command.
    Зарегистрирует исключения доступа из лабы."""
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            return output
    except (NetmikoAuthenticationException, NetmikoTimeoutException) as error:
        print(error)

if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    command = "sh ip int br"
    for dev in devices:
        print(send_show_command(dev, command))

import pprint

import yaml
from netmiko import ConnectHandler

ERROR_PATTERNS = ("Invalid input detected", "Incomplete command", "Ambiguous command")

def send_config_commands(device, config_commands, log=True):
    """Выполняет конфигурационные команды на устройстве.

    Возвращает кортеж из двух словарей:
    - первый: команды, которые выполнились без ошибок;
    - второй: команды с выводом об ошибках.
    Сообщения об ошибках печатаются в stdout всегда,
    независимо от значения log.
    """
    correct_commands = {}
    incorrect_commands = {}
    target = device.get("ip") or device.get("host")
    if log:
        print(f"Подключаюсь к {target}...")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        for command in config_commands:
	    output = ssh.send_config_set([command], exit_config_mode=False)
            matched = [pattern for pattern in ERROR_PATTERNS if pattern in output]
            if matched:
                error_msg = [line for line in output.splitlines() if matched[0] in line][-1]
                print(
                    f'Команда «{command}» выполнилась с ошибкой '
		    f'«{error_msg.lstrip("% ").strip()}» на устройстве {target}'
                )
                incorrect_commands[command] = output
            else:
                correct_commands[command] = output
    return correct_commands, incorrect_commands
if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    commands = [
        "logging 0255.255.1",
        "logging",
        "a",
        "logging buffered 20010",
        "ip http server",
    ]
    for dev in devices:
        result = send_config_commands(dev, commands)
        pprint.pprint(result, width=120)
