def convert_ranges_to_ip_list(ip_addresses):
    """
    ip_addresses - список IP-адресов или диапазонов IP-адресов

    Форматы элементов списка:
    - "10.1.1.1"          один адрес
    - "10.1.1.10-11.1.10" диапазон из двух полных адресов
    - "10.1.1-10"         диапазон последнего октета

    Возвращает список IP-адресов.
    """
    result = []
    for item in ip_addresses:
        if "-" not in item:
            result.append(item)
            continue

        start, end = item.split("-")
        start_prefix, start_last = start.rsplit(".", 1)
        if "." in end:
            end_prefix, end_last = end.rsplit(".", 1)
        else:
            end_prefix, end_last = start_prefix, end

        for octet in range(int(start_last), int(end_last) + 1):
            result.append("{}.{}".format(start_prefix, octet))

    return result


if __name__ == "__main__":
    test_list = ["8.8.4.4", "1.1.1.1-2.2.2.2", "172.21.41.128-172.21.41.132"]
    print(convert_ranges_to_ip_list(test_list))
