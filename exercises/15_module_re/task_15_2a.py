def convert_to_dict(headers, data):
    """
        headers - список назаний поля
        data - слисок кортеейеы
    """
    result = []
    for tuple in data:
        header_dict = {}
        for i, value in enumerate(tuple):
            key = headers[i]
            header_dict[key] = value
        result.append(header_dict)
    return result

if __name__ == "__main__":
    headers = ["hostname", "ios", "platform"]
    data = [
        ("R1", "12.4(24)T", "Cisco 3825"),
        ("R2", "15.2(2)T", "Cisco 2911"),
        ("SW1", "12.2(55)SE9", "Cisco WS-C2960-BTC-L"),
    ]
    print(convert_to_dict(headers, data))
