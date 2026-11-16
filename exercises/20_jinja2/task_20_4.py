
import yaml

from task_20_1 import generate_config





if __name__ == "__main__":

    with open("data_files/add_vlan_to_switch.yml") as f:

        data = yaml.safe_load(f)

    print(generate_config("templates/add_vlan_to_switch.txt", data))

