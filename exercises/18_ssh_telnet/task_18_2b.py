import pprint

import yaml
from netmiko import ConnectHandler

ERROR_PATTERNS = ("Invalid input detected", "Incomplete command", "Ambiguous command")


def send_config_commands(device, config_commands, log=True):
    """Выполняет команды на устройстве.

    Возвращает кортеж из двух словарей:
    - первый: команды, которые выполнились без ошибок;
    - второй: команды с выводом об ошибках.
    Сообщения об ошибках печатаются в stdout всегда,
    независимо от значения параметра log.
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
            matched = [p for p in ERROR_PATTERNS if p in output]
            if matched:
                error_msg = [l for l in output.splitlines() if matched[0] in l][-1]
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
