# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
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
if not valid:
    print("Неправильный IP-адрес")
else:
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