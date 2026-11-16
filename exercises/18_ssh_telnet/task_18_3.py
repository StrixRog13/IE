# -*- coding: utf-8 -*-
"""
Задание 18.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к одному устройству
* show - одна команда show (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

Аргументы show и config должны передаваться только как ключевые. При передачи
этих аргументов как позиционных, должно генерироваться исключение TypeError.

In [4]: send_commands(r1, 'sh clock')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-75adcfb4a005> in <module>
----> 1 send_commands(r1, 'sh clock')

TypeError: send_commands() takes 1 positional argument but 2 were given


В зависимости от того, какой аргумент был передан, функция вызывает разные функции
внутри. При вызове функции send_commands, всегда должен передаваться
только один из аргументов show, config. Если передаются оба аргумента, должно
генерироваться исключение ValueError.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 18.1
* config - функция send_config_commands из задания 18.2

Функция возвращает строку с результатами выполнения команд или команды.

Проверить работу функции:
* со списком команд commands
* командой command

Пример работы функции:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: commands = ['username user5 password pass5', 'username user6 password pass6']

In [16]: send_commands(r1, config=commands)
Out[16]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#username user5 password pass5\nR1(config)#username user6 password pass6\nR1(config)#end\nR1#'

"""

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"

import yaml
from netmiko import ConnectHandler


def send_show_command(device, command):
    """Подключается к устройству по SSH и выполняет команду command."""
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_command(command)


def send_config_commands(device, config_commands, log=True):
    """Выполняет конфигурационные команды на устройстве."""
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        return ssh.send_config_set(config_commands)


def send_commands(device, *, show="", config=""):
    """Вызывает send_show_command или send_config_commands
    в зависимости от переданного аргумента.

    Аргументы show/config передаются только по имени (keyword-only):
    при позиционной передаче Python сам бросит TypeError.
    Если переданы оба аргумента — ValueError.
    """
    if show and config:
        raise ValueError(
            "Можно передать только один из аргументов show или config"
        )
    if show:
        return send_show_command(device, show)
    if config:
        return send_config_commands(device, config)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    commands = [
        "logging 0255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    command = "sh ip int br"

    for dev in devices:
        print(send_commands(dev, show=command))
        print(send_commands(dev, config=commands))

