import re

def get_ip_from_cfg(config_filename):
    with open(config_filename) as f:
        config = f.read()
    current_int = None
    result = {}
    for line in config.splitlines():
        int_match = re.match(r"interface (\S+)", line)
        if int_match:
            current_int = int_match.group(1)
            continue
        ip_match = re.match(r"\s+ip address (\S+) (\S+)", line)
        if ip_match:
            result.setdefault(current_int, []).append(ip_match.groups())
    return result

if __name__ == "__main__":
    print(get_ip_from_cfg("config_r2.txt"))
