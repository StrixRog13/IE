import re


def get_ints_without_description(config_filename):
    result = []
    current_int = None
    described = False
    with open(config_filename) as f:
        for line in f:
            if not line.strip():
                continue
            if not line.startswith((" ", "\t")):
                if current_int is not None and not described:
                    result.append(current_int)
                match = re.match(r"interface (\S+)", line)
                if match:
                    current_int = match.group(1)
                    described = False
                else:
                    current_int = None
            elif current_int is not None and re.match(r"\s+description\s", line):
                described = True
    if current_int is not None and not described:
        result.append(current_int)
    return result


if __name__ == "__main__":
    print(get_ints_without_description("config_r1.txt"))
