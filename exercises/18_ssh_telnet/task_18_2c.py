import yaml
from netmiko import ConnectHandler

ERROR_PATTERNS = ("Invalid input detected", "Incomplete command", "Ambiguous command")


def send_config_commands(device, config_commands, log=True):
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
                print(f'Команда «{command}» выполнилась с ошибкой «{error_msg.lstrip("% ").strip()}» на устройстве {target}')
                incorrect_commands[command] = output
                answer = input("Продолжать выполнять команды? [y]/n: ")
                if answer.strip().lower() in ("n", "no"):
                    break
            else:
                correct_commands[command] = output
    return correct_commands, incorrect_commands
