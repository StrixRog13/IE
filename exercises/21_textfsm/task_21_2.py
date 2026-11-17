
from task_21_1 import parse_command_output





if __name__ == "__main__":

    with open("output/sh_ip_dhcp_snooping.txt") as f:

        output = f.read()

    result = parse_command_output("templates/sh_ip_dhcp_snooping.template", output)

    for row in result:

        print(row)

