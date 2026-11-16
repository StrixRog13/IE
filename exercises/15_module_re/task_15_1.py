import re


def get_ip_from_cfg(config_filename):
    with open(config_filename) as f:
        config = f.read()
    regex = re.compile(r"ip address (\S+) (\S+)")
    return regex.findall(config)


if __name__ == "__main__":
    print(get_ip_from_cfg("config_r1.txt"))
