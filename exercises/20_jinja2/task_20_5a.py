
import re

import yaml

from netmiko import ConnectHandler

from task_20_1 import generate_config

def create_vpn(src_device_params, dst_device_params, template1, template2, vpn_data_dict):

    """Настраивает GRE over IPSec VPN между двумя маршрутизаторами."""

    tunnel_numbers = []

    for device_params in (src_device_params, dst_device_params):

        with ConnectHandler(**device_params) as ssh:

            ssh.enable()

output = ssh.send_command("show run | include interface Tunnel")

            tunnel_numbers.extend(

                int(num) for num in re.findall(r"interface Tunnel(\d+)", output)

            )



    tun_num = max(tunnel_numbers) + 1 if tunnel_numbers else 1

    vpn_data_dict = dict(vpn_data_dict)

    vpn_data_dict["tun_num"] = tun_num



    config1 = generate_config(template1, vpn_data_dict)

    config2 = generate_config(template2, vpn_data_dict)



    results = []

    for device_params, config in zip(

        (src_device_params, dst_device_params), (config1, config2)

    ):

with ConnectHandler(**device_params) as ssh:

            ssh.enable()

            results.append(ssh.send_config_set(config.splitlines()))

    return tuple(results)





if __name__ == "__main__":

data = {

        "tun_num": None,

        "wan_ip_1": "192.168.100.1",

        "wan_ip_2": "192.168.100.2",

        "tun_ip_1": "10.0.1.1 255.255.255.252",

        "tun_ip_2": "10.0.1.2 255.255.255.252",

    }

    with open("devices.yaml") as f:

        devices = yaml.safe_load(f)

        output_src, output_dst = create_vpn(

        devices[0],

        devices[1],

        "templates/gre_ipsec_vpn_1.txt",

        "templates/gre_ipsec_vpn_2.txt",

        data,

    )

    print(output_src)

    print(output_dst)

