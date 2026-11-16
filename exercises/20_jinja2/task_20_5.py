
from task_20_1 import generate_config





def create_vpn_config(template1, template2, data_dict):

    """Генерирует конфигурацию GRE over IPSec VPN для двух сторон туннеля.



    template1 — файл шаблона для первой стороны туннеля,

    template2 — файл шаблона для второй стороны туннеля,

    data_dict — словарь со значениями, которые надо подставить в шаблоны.

    Возвращает кортеж из двух строк конфигурации.

    """

    config1 = generate_config(template1, data_dict)

    config2 = generate_config(template2, data_dict)

    return (config1, config2)





if __name__ == "__main__":

    data = {

        "tun_num": 10,

        "wan_ip_1": "192.168.100.1",

        "wan_ip_2": "192.168.100.2",

        "tun_ip_1": "10.0.1.1 255.255.255.252",

        "tun_ip_2": "10.0.1.2 255.255.255.252",

    }

    configs = create_vpn_config(

        "templates/gre_ipsec_vpn_1.txt",

        "templates/gre_ipsec_vpn_2.txt",

        data,

    )

    for config in configs:

        print(config)

        print("\n".join(80 * "-"))

