# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

import sys

if len(sys.argv) < 3:
    print("Укажите два файла: python task_7_2b.py config_sw1.txt result.txt")
    sys.exit(1)

src_filename = sys.argv[1]
dst_filename = sys.argv[2]
ignore = ["duplex", "alias", "configuration"]

with open(src_filename) as f, open(dst_filename, "w") as out:
    for line in f:
        if line.startswith("!") or not line.strip():
            continue
        if any(word in line for word in ignore):
            continue
        out.write(line)