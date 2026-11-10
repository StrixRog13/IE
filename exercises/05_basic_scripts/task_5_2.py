# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_mask = input("Введите IP-сети в формате 10.1.1.0/24: ")

ip, mask = ip_mask.split("/")
mask = int(mask)
ip_octets = ip.split(".")

print("Network:")
for octet in ip_octets:
     print("{:10}".format(octet), end="")
print()

for octet in ip_octets:
    bin_octet = "{:08b}".format(int(octet))
    print("{:10}".format(bin_octet), end="")
print()

print("Mask:")
print("/{}".format(mask))

mask_binary = "1" * mask + "0" * (32 - mask)

mask_octets = []
for i in range(0, 32, 8):
    mask_octets.append(str(int(mask_binary[i:i + 8], 2)))
for octet in mask_octets:
     print("{:10}".format(octet), end="")
print()

for i in range(0, 32, 8):
     print("{:10}".format(mask_binary[i:i + 8]), end="")
print()