class AuthUser:
    def __init__(self, name) -> None:
        self.name = name


class AuthModel:
    __user = None

    @classmethod
    def set_auth_user(cls, user):
        auth_user = AuthUser(user.name)
        cls.__user = auth_user

    @classmethod
    def get_auth_user(cls):
        return cls.__user

    @classmethod
    def clear_auth_user(cls):
        cls.__user = None
