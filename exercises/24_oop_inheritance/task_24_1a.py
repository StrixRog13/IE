from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **kwargs):
        self.ip = kwargs.get("host") or kwargs.get("ip") or input(
            "Введите IP адрес: "
        )
        self.username = kwargs.get("username") or input(
            "Введите имя пользователя: "
        )
        self.password = kwargs.get("password") or input(
            "Введите пароль: "
        )
        self.enable_password = kwargs.get("secret") or kwargs.get(
            "enable_password"
        ) or input("Введите пароль для режима enable: ")
        super().__init__(
            self.ip, self.username, self.password, self.enable_password
        )
        self.enable()
