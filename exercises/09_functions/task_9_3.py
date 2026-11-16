# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    """
    config_filename - имя файла конфигурации

    Возвращает кортеж из двух словарей:
    - словарь портов в режиме access: {'FastEthernet0/12': 10, ...}
    - словарь портов в режиме trunk: {'FastEthernet0/17': [10, 20, 30], ...}
    """
    access = {}
    trunk = {}
    intf = None
    
    with open(config_filename) as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            if parts[0] == "interface":
                intf = parts[1]
            elif parts[0] == "switchport" and intf is not None:
                if parts[1] == "access" and parts[2] == "vlan":
                    access[intf] = int(parts[-1])
                elif parts[1] == "trunk" and parts[2] == "allowed":
                    vlan_list = []
                    for v in parts[-1].split(","):
                        vlan_list.append(int(v))
                    trunk[intf] = vlan_list

    return (access, trunk)


print(get_int_vlan_map("config_sw1.txt"))
