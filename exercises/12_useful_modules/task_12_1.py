# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def ping_ip_addresses(ip_addresses):
    """
    ip_addresses - список IP-адресов

    Возвращает кортеж из двух списков:
    * список доступных IP-адресов
    * список недоступных IP-адресов
    """
    reachable = []
    unreachable = []
    for ip in ip_addresses:
        reply = subprocess.run(
            ["ping", ip, "-c", "2"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if reply.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return (reachable, unreachable)

if __name__ == "__main__":
    print(ping_ip_addresses(["8.8.8.8", "255.255.255.255"]))