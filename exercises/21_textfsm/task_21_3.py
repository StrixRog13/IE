
import os

from textfsm import clitable





def parse_command_dynamic(command_output, attributes_dict=None,

                          index_file="index", templ_path="templates"):

    """Разбирает вывод команды с динамическим выбором шаблона TextFSM.



    command_output — вывод команды show (строка),

    attributes_dict — словарь атрибутов для выбора шаблона,

        по заданию содержит ключи 'Command' и 'Vendor',

    index_file — имя файла, где хранится соответствие между командами

        и шаблонами (по умолчанию "index"),

    templ_path — каталог, где хранятся шаблоны (по умолчанию "templates").



    Возвращает список словарей: ключи — имена переменных в шаблоне

    TextFSM, значения — части вывода, которые соответствуют переменным.

    """

    if attributes_dict is None:

        attributes_dict = {"Command": "sh ip int br", "Vendor": "cisco_ios"}

    # файл index может лежать в каталоге задания или внутри каталога шаблонов

    if not os.path.exists(index_file):

        index_file = os.path.join(templ_path, index_file)

    cli_table = clitable.CliTable(index_file, templ_path)

    cli_table.ParseCmd(command_output, attributes_dict)

    return [dict(zip(cli_table.header, row)) for row in cli_table]





if __name__ == "__main__":

    with open("output/sh_ip_int_br.txt") as f:

        output = f.read()

    result = parse_command_dynamic(

        output, {"Command": "sh ip int br", "Vendor": "Cisco"}

    )

    for row in result:

        print(row)

