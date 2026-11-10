# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip = input("Введите IP-адрес в формате 10.0.1.1: ")
    parts = ip.split(".")
    valid = True
    if len(parts) != 4:
        valid = False
    else:
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                valid = False
                break
    if len(parts) != 4:
        valid = False
    else:
        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                valid = False
                break
    if valid:
        break
    else:
        print("Неправильный IP-адрес")
first_octet = int(parts[0])
if ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
elif 1 <= first_octet <= 223:
    print("unicast")
elif 224 <= first_octet <= 239:
    print("multicast")
else:
    print("unassigned")