import flet as ft
from components.Alert import Alert
from controllers.UserController import UserController
from controllers.AuthController import AuthController
from classes.User import User
from utils.routes import routes


class Login(ft.UserControl):
    _user_name_field = ft.TextField(label="Usuario", autofocus=True)
    _password_field = ft.TextField(label="Contraseña",
                                   password=True, can_reveal_password=True)

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.__create_admin_user()

    def build(self):
        return ft.ResponsiveRow([
            ft.Container(
                col={"sm": 10, "md": 8, "lg": 6},
                content=ft.Column([
                    ft.Row([
                        ft.Text("Bienvenido", font_family="PlaypenSans Black",
                                text_align=ft.TextAlign.CENTER, style=ft.TextThemeStyle.HEADLINE_LARGE, expand=True)
                    ]),
                    self._user_name_field,
                    self._password_field,
                    ft.Row([
                        ft.ElevatedButton(
                            text="Ingresar", on_click=self.__on_signin, expand=True, height=50)
                    ])
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=24, height=self.page.window_height),
                height=self.page.window_height,
                expand=True,
            )
        ], alignment=ft.MainAxisAlignment.CENTER, height=self.page.window_height)

    def __on_signin(self, e):
        name = self._user_name_field.value
        password = self._password_field.value

        if (name == "" or password == ""):
            Alert(self.page, "Error",
                  "Por favor ingrese sus credenciales", None, "info")
            return
        auth_controller = AuthController()

        result = auth_controller.sign_in(name, password)
        success_status = result[0]
        if (success_status):
            self._user_name_field.value = ""
            self._password_field.value = ""
            self.page.go(routes["dashboard"])
            return
        error = result[1]
        if (error == "user_name"):
            Alert(self.page, "Error", "Usuario incorrecto", None, "info")
        if (error == "password"):
            Alert(self.page, "Error", "Contraseña incorrecta", None, "info")

    def __create_admin_user(self):
        controller = UserController()
        users = controller.get_users()
        if (len(users) == 0):
            user = User(0, "Administrador",
                           "Admin", "Algoritmos123")
            controller.save(user)
