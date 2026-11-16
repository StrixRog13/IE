access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, port_security=None):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12': 10, 'FastEthernet0/14': 11, 'FastEthernet0/16': 17}
    access_template - список команд для порта в режиме access
    port_security - список команд port-security (опционально)

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона.
    """
    result = []

	for intf, vlan in intf_vlan_mapping.items():
        result.append(f"interface {intf}")
        for command in access_template:
            if "{{ vlan }}" in command:
                command = command.replace("{{ vlan }}", str(vlan))
            elif command.endswith("vlan"):
                command = command + f" {vlan}"
            result.append(command)
        if port_security is not None:
            result.extend(port_security)

    return result