
import os

import yaml

from textfsm import clitable

from netmiko import ConnectHandler





def send_and_parse_show_command(device_dict, command,

                                templates_path="templates", index="index"):

    """Отправляет команду show на устройство и разбирает вывод шаблоном TextFSM.



    device_dict — словарь с параметрами подключения к устройству

        (для netmiko ConnectHandler),

    command — команда, которую надо выполнить,

    templates_path — путь к каталогу с шаблонами TextFSM,

    index — имя файла с соответствием команд и шаблонов.



    Возвращает список словарей: ключи — имена переменных в шаблоне

    TextFSM, значения — части вывода, которые соответствуют переменным.

    """

    # файл index может лежать в каталоге задания или внутри каталога шаблонов

    if not os.path.exists(index):

        index = os.path.join(templates_path, index)



    attributes = {"Command": command, "Vendor": device_dict["device_type"]}

    cli_table = clitable.CliTable(index, templates_path)

    cli_table.ParseCmd("", attributes)



    with ConnectHandler(**device_dict) as ssh:

        ssh.enable()

        output = ssh.send_command(command)

    return [dict(zip(cli_table.header, row)) for row in cli_table.ParseText(output)]





if __name__ == "__main__":

    with open("devices.yaml") as f:

        devices = yaml.safe_load(f)

    for device in devices:

        print("-" * 60)

        print("Device:", device["host"])

        result = send_and_parse_show_command(device, "sh ip int br")

        for row in result:

            print(row)

