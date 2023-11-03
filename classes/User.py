from classes.GeneralClass import GeneralClass


class User(GeneralClass):
    def __init__(self, id, name, user_name) -> None:
        super().__init__(id, name)
        self.user_name = user_name


class NewUser(User):
    def __init__(self, id, name, user_name, password) -> None:
        super().__init__(id, name, user_name)
        self.password = password
