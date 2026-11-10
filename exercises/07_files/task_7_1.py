# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open("ospf.txt") as f:
    for line in f:
        parts = line.split()
        prefix = parts[1]
        ad_metric = parts[2].strip("[]")
        next_hop = parts[4].strip(",")
        last_update = parts[5].strip(",")
        out_interface = parts[6]
        
        print("{:<20}{}".format("Prefix", prefix))
        print("{:<20}{}".format("AD/Metric", ad_metric))
        print("{:<20}{}".format("Next-Hop", next_hop))
        print("{:<20}{}".format("Last update", last_update))
        print("{:<20}{}".format("Outbound Interface", out_interface))
        print()