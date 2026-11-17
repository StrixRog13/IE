
import yaml

from concurrent.futures import ThreadPoolExecutor, as_completed

from task_21_4 import send_and_parse_show_command





def send_and_parse_command_parallel(devices, command,

                                    templates_path="templates", index="index",

                                    limit=3):

    """Отправляет команду на устройства параллельно и разбирает вывод TextFSM.



    devices — список словарей с параметрами подключения к устройствам,

    command — команда, которую надо выполнить,

    templates_path — путь к каталогу с шаблонами TextFSM,

    index — имя файла с соответствием команд и шаблонов,

    limit — максимальное количество параллельных потоков.



    Возвращает словарь: ключ — IP-адрес устройства,

    значение — список словарей с результатами разбора вывода

    (как в задании 21.1a).

    """

    result = {}

    with ThreadPoolExecutor(max_workers=limit) as executor:

        futures = {}

        for device in devices:

            future = executor.submit(

                send_and_parse_show_command,

                device, command, templates_path, index,

            )

            futures[future] = device["host"]

        for future in as_completed(futures):

            result[futures[future]] = future.result()

    return result





if __name__ == "__main__":

    with open("devices.yaml") as f:

        devices = yaml.safe_load(f)

    result = send_and_parse_command_parallel(devices, "sh ip int br")

    for ip, parsed in result.items():

        print("-" * 60)

        print(ip)

        for row in parsed:

            print(row)

