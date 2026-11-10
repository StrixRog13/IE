with open("CAM_table.txt") as f:
    for line in f:
        parts = line.split()
        if len(parts) < 4 or not parts[0].isdigit():
            continue
        vlan, mac, typ, port = parts
        print(f"{vlan:<4} {mac:<18} {port}")