class IPAddress:
    def __init__(self, address):
        ip, mask = address.split("/")
        ip_octets = ip.split(".")
        if len(ip_octets) != 4 or not all(
            octet.isdigit() and 0 <= int(octet) <= 255 for octet in ip_octets
        ):
            raise ValueError("Incorrect IPv4 address")
        if not (mask.isdigit() and 0 <=int(mask) <= 32):
            raise ValueError("Incorrect mask")
        self.ip = ip
        self.mask = int(mask)
