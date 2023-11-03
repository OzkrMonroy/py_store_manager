from models.UserModel import UserModel
from classes.User import User


class UserController:
    user = UserModel()
    is_to_update = None
    element_to_update = None

    def __init__(self) -> None:
        self.load_users()

    def load_users(self):
        self.user.load_users()

    def get_users(self):
        return self.user.get_users()

    def save(self, user: User) -> bool:
        return self.user.save(user)

    def update(self, user: User) -> bool:
        return self.user.update(user)

    def delete(self, user: User) -> bool:
        return self.user.delete(user)

    @classmethod
    def set_element_to_update(cls, user: User):
        cls.element_to_update = user
        cls.is_to_update = True

    @classmethod
    def get_element_to_update(cls):
        return [cls.is_to_update, cls.element_to_update]
