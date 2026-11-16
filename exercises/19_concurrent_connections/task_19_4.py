import yaml
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler


def send_show_to_device(device, command):
    """Подключается к устройству и выполняет команду show."""
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_command(command)


def send_config_to_device(device, commands):
    """Подключается к устройству и выполняет конфигурационные команды."""
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_config_set(commands)


def send_commands_to_devices(devices, filename, *, show=None, config=None, limit=3):
    """Отправляет команду show или config на устройства в параллельных
    потоках и записывает вывод команд в файл.

    Аргументы show, confi` и limit передаются только как ключевые слова.
    При передаче обоих аргументов show и config генерируется ValueError.
    Перед выводом show-команды в файл пишется имя хоста и сама команда.
    Функция ничего не возвращает.
    """
    if show and config:
        raise ValueError(
            "Можно передать только один из аргументов show или config"
        )
    with ThreadPoolExecutor(max_workers=limit) as executor:
        if show is not None:
            results = executor.map(lambda dev: send_show_to_device(dev, show), devices)
        else:
            results = executor.map(lambda dev: send_config_to_device(dev, config), devices)
    with open(filename, "w") as f:
        if show is not None:
            for device, output in zip(devices, results):
                hostname = device.get("name") or device.get("host")
                f.write(f"{hostname}#{show}\n")
                f.write(f"{output}\n")
        else:
            for output in results:
                f.write(f"{output}\n")


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    send_commands_to_devices(devices, "result_show.txt", show="sh ip int br")
    send_commands_to_devices(
        devices,
        "result_config.txt",
        config=["router ospf 55", "network 0.0.0.0 255.255.255.255 area 0"],
    )
