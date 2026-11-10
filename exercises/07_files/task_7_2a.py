# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

import sys

if len(sys.argv) < 2:
    print("Укажите имя конфигурационного файла: python task_7_2a.py config_sw1.txt")
    sys.exit(1)

filename = sys.argv[1]
ignore = ["duplex", "alias", "configuration"]

with open(filename) as f:
    for line in f:
        if line.startswith("!") or not line.strip():
            continue
        if any(word in line for word in ignore):
            continue
        print(line, end="")