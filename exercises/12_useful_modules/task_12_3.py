def print_ip_table(reachable, unreachable):
    """
    reachable - список доступных IP-адресов
    unreachable - список недоступных IP-адресов

    Выводит на стандартный поток вывода таблицу:
    доступные адреса в первой колонке, недоступные во второй.
    """
    width = 12
    print("{:{width}}{:{width}}".format("Reachable", "Unreachable", width=width))
    print("{} {}".format("-" * width, "-" * width))
    for num in range(max(len(reachable), len(unreachable))):
        reachable_ip = reachable[num] if num < len(reachable) else ""
        unreachable_ip = unreachable[num] if num < len(unreachable) else ""
        print("{:{width}}{:{width}}".format(reachable_ip, unreachable_ip, width=width))


if __name__ == "__main__":
    print_ip_table(
        ["10.1.1.1", "10.1.1.2"],
        ["10.1.1.7", "10.1.1.8", "10.1.1.9"],
    )
