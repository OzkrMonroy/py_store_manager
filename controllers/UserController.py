from models.UserModel import UserModel
from classes.User import NewUser


class UserController:
    user = UserModel()

    def __init__(self) -> None:
        self.load_users()

    def load_users(self):
        self.user.load_users()

    def get_users(self):
        return self.user.get_users()

    def save(self, user: NewUser) -> bool:
        return self.user.save(user)
