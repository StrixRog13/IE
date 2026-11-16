import re

def generate_description_from_cdp(filename):
    result = {}
    regex = r"^(\S+) +(\S+ \S+) +\d+ +\S+ +(.+) +(\S+ \S+)$"
    with open(filename) as f:
        for line in f:
            match = re.match(regex, line.rstrip())
            if match:
                result[match.group(2)] = "description Connected to {} port {}".format(
                    match.group(1), match.group(4)
                )
    return result

if __name__ == "__main__":
    print(generate_description_from_cdp("sh_cdp_n_sw1.txt"))
