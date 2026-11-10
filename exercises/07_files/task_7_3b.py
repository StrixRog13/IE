# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan_input = input("Enter VLAN number: ")

if not vlan_input.isdigit():
    print("VLAN должен быть числом")
    sys.exit(1)

vlan_needed = int(vlan_input)

rows = []

with open("CAM_table.txt") as f:
    for line in f:
        parts = line.split()
        if len(parts) < 4 or not parts[0].isdigit():
            continue
        vlan, mac, typ, port = parts
        if int(vlan) == vlan_needed:
            rows.append((vlan, mac, port))

for vlan, mac, port in rows:
    print(f"{vlan}      {mac}      {port}")