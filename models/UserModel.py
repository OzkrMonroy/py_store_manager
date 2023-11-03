import os
from classes.User import User
from classes.ParentModel import ParentModel
from utils.consts import ROOT_PATH, USERS_FILE


class UserModel(ParentModel):
    users = []

    def load_users(self):
        file = self.__open_file("r")
        self.users = []
        if (file):
            for user in file:
                user = user.rstrip("\n").split(",")
                user_to_save = User(user[0], user[1], user[2], user[3])
                self.__save_user_to_list(user_to_save)
            file.close()

    def get_users(self):
        return self.users

    def save(self, user: User) -> bool:
        file = self.__open_file("a")
        user.id = len(self.users)
        if (file):
            file.write(
                f"{user.id},{user.name},{user.user_name},{user.password}\n")
            file.close()
            self.__save_user_to_list(user)
            return True

        return False

    def update(self, user: User) -> bool:
        is_updated = self.__update_in_file(user)
        if (is_updated):
            index = self.get_element_index(user, self.users)
            if (index != None):
                self.users[index].name = user.name
                self.users[index].user_name = user.user_name
                self.users[index].password = user.password
        return is_updated

    def delete(self, user: User):
        is_deleted = self.__delete_in_file(user)
        if (is_deleted):
            self.users.remove(user)

        return is_deleted

    def __save_user_to_list(self, user: User):
        self.users.append(user)

    def __open_file(self, open_mode: str):
        try:
            file = open(os.path.abspath(
                f"{ROOT_PATH}\{USERS_FILE}"), mode=open_mode, encoding="utf-8")
            return file
        except FileNotFoundError:
            print(f"Sorry, the file {USERS_FILE} does not exist.")
            return None

    def __delete_in_file(self, user: User):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            updated_lines = [
                line for line in lines if not line.startswith(user.id)]
            write_file = self.__open_file("w")
            write_file.writelines(updated_lines)
            write_file.close()
            return True
        return False

    def __update_in_file(self, user: User):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            index = self.get_element_index_in_file(user, lines)
            lines[index] = f"{user.id},{user.name},{user.user_name},{user.password}\n"
            write_file = self.__open_file("w")
            write_file.writelines(lines)
            write_file.close()
            return True
        return False
