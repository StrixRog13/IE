
import textfsm





def parse_command_output(template, command_output):

    """Разбирает вывод команды с помощью шаблона TextFSM.



    template — путь к файлу с шаблоном TextFSM

        (например, "templates/sh_ip_int_br.template"),

    command_output — вывод соответствующей команды show (строка).



    Возвращает список: первый элемент — список с названиями столбцов,

    остальные элементы — списки с результатами разбора вывода.

    """

    with open(template) as f:

        re_table = textfsm.TextFSM(f)

    result = re_table.ParseText(command_output)

    return [re_table.header] + result





if __name__ == "__main__":

    with open("output/sh_ip_int_br.txt") as f:

        output = f.read()

    result = parse_command_output("templates/sh_ip_int_br.template", output)

    for row in result:

        print(row)

