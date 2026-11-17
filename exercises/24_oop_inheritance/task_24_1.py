from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, ip=None, username=None, password=None,
                 enable_password=None, **kwargs):
        ip = ip or kwargs.get("host")
        enable_password = enable_password or kwargs.get("secret")
        super().__init__(ip, username, password, enable_password, **kwargs)
        self.enable()
