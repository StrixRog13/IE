import re

def parse_sh_ip_int_br(output):
    with open(output) as f:
        output_lines = f.readlines()
    result = []
    for line in output_lines:
        match = re.match(
            r"(^\S+)\s+(\S+)\s+\S+\s+\S+\s+(.+?)\s+(\S+)$", line
        )
        if match and match.group(1) != "Interface":
            result.append(match.groups())
    return result

if __name__ == "__main__":
    print(parse_sh_ip_int_br("sh_ip_int_br.txt"))
