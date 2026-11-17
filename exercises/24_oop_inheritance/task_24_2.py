from netmiko.cisco.cisco_ios import CiscoIosSSH


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enable()
