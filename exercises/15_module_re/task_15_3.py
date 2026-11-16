import re


def convert_ios_nat_to_asa(ios_filename, asa_filename):
    with open(ios_filename) as f:
        for line in f:
            match = re.match(
                r"ip nat inside source static \S+ (\S+) (\S+) interface \S+ (\S+)",
                line,
            )
            if match:
                with open(asa_filename, "a") as f:
                    f.write(
                        "object network LOCAL_{0}\n"
                        " host {0}\n"
                        " nat (inside,outside) static interface service tcp {1} {2}\n".format(
                            match.group(1), match.group(2), match.group(3)
                        )
                    )


if __name__ == "__main__":
    convert_ios_nat_to_asa("cisco_nat_config.txt", "cisco_nat_config_asa.txt")
