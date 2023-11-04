import flet as ft
from components.NavigationRail import NavigationRail
from components.Alert import Alert
from components.Snackbar import Snackbar
from controllers.UserController import UserController
from classes.User import User
from utils.routes import routes


class AddUser(ft.UserControl):
    user_controller = UserController()
    _name_field = ft.TextField(label="Nombre", autofocus=True)
    _user_name_field = ft.TextField(label="Nombre de usuario")
    _password_field = ft.TextField(label="Contraseña",
                                   password=True, can_reveal_password=True)
    _confirm_password_field = ft.TextField(label="Confirma la contraseña",
                                           password=True, can_reveal_password=True)
    _page_title = "Agregar "
    _is_to_update = False
    _element_to_update = None

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        self.__fill_fields()
        return ft.Row([
            NavigationRail(self.page, 0),
            ft.VerticalDivider(width=1),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column([
                    ft.Text(f"{self._page_title} usuario", font_family="Roboto Bold",
                            style=ft.TextThemeStyle.HEADLINE_LARGE),
                    self._name_field,
                    self._user_name_field,
                    self._password_field,
                    self._confirm_password_field,
                    ft.Row([
                        ft.ElevatedButton(
                            text="Cancelar", on_click=lambda e:  self.page.go(routes["users"]), height=50, width=200),
                        ft.ElevatedButton(
                            text=self._page_title, on_click=self.__on_add, height=50, width=200),
                    ], alignment=ft.MainAxisAlignment.END)
                ], expand=True, spacing=24)
            )
        ], width=self.page.window_width, height=self.page.window_height)

    def __on_add(self, e):
        name = self._name_field.value.strip()
        user_name = self._user_name_field.value.strip()
        password = self._password_field.value.strip()
        confirm_password = self._confirm_password_field.value.strip()

        pass_validation = self.__validations(
            name, user_name, password, confirm_password)

        if (pass_validation):
            user = User(0, name, user_name, password)
            created = None
            if (self._is_to_update):
                user.id = self._element_to_update.id
                created = self.user_controller.update(user)
            else:
                created = self.user_controller.save(user)
            self.__notify_add_user(created)

    def __fill_fields(self):
        options = self.user_controller.get_element_to_update()
        if (options[0]):
            user = options[1]
            self._is_to_update = options[0]
            self._element_to_update = user
            self._page_title = "Actualizar "
            self._name_field.value = user.name
            self._user_name_field.value = user.user_name
            self._password_field.value = user.password
            self._confirm_password_field.value = user.password

    def __validations(self, name: str, user_name: str, password: str, confirm_password: str) -> bool:
        if (name == "" and user_name == "" and password == "" and confirm_password == ""):
            Alert(self.page, "Información",
                  "Todos los campos son obligatorios", None, "info")
            return False
        if (password != confirm_password):
            Alert(self.page, "Información",
                  "Las contraseñas no coinciden", None, "info")
            return False
        return True

    def __notify_add_user(self, created: bool):
        success_message = "Usuario actualizado" if self._is_to_update else "Usuario agregado"
        error_message = "Ha ocurrido un error al actualizar el usuario" if self._is_to_update else "Ha ocurrido un error al crear el usuario"
        if (created):
            Snackbar(self.page, success_message)
            self._name_field.value = ""
            self._user_name_field.value = ""
            self._password_field.value = ""
            self._confirm_password_field.value = ""
            self.page.go(routes["users"])
            return
        Snackbar(self.page, error_message)
