import yaml
from netmiko import ConnectHandler, NetmikoAuthenticationException


def send_show_command(device, command):
    """Подключается к устройству по SSH и выполняет команду command."""
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
        return output
    except NetmikoAuthenticationException as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_show_command(dev, "sh ip int br"))
