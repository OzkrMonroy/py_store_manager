from controllers.UserController import UserController
from models.AuthModel import AuthModel


class AuthController:
    auth_model = AuthModel()

    def sign_in(self, user_name: str, password: str):
        user_controller = UserController()
        users = user_controller.get_users()
        index = self.__find_user_index(user_name, users)
        if (index == None):
            return [False, "user_name"]
        user = users[index]
        if (user.password == password):
            self.auth_model.set_auth_user(user)
            return [True]
        return [False, "password"]

    def logout(self):
        self.auth_model.clear_auth_user()

    def get_auth_user(self):
        return self.auth_model.get_auth_user()

    def __find_user_index(self, user_name: str, users: list):
        index = None
        for i, element in enumerate(users):
            if element.user_name == user_name:
                index = i
        return index
