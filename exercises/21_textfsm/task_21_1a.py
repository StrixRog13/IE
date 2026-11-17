
import textfsm





def parse_output_to_dict(template, command_output):

    """Разбирает вывод команды с помощью шаблона TextFSM.



    template — путь к файлу с шаблоном TextFSM

        (например, "templates/sh_ip_int_br.template"),

    command_output — вывод соответствующей команды show (строка).



    Возвращает список словарей: ключи — имена переменных из шаблона

    TextFSM, значения — соответствующие данные из вывода.

    """

    with open(template) as f:

        re_table = textfsm.TextFSM(f)

    result = re_table.ParseTextToDicts(command_output)

    return result





if __name__ == "__main__":

    with open("output/sh_ip_int_br.txt") as f:

        output = f.read()

    result = parse_output_to_dict("templates/sh_ip_int_br.template", output)

    for row in result:

        print(row)

