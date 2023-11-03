import flet as ft
from controllers.UserController import UserController
from classes.User import NewUser


class Login(ft.UserControl):
    _user_field = ft.TextField(label="Usuario")
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
                    self._user_field,
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
        name = self._user_field.value
        password = self._password_field.value
        print(name, password)
        self.page.go("/dashboard")

    def __create_admin_user(self):
        controller = UserController()
        users = controller.get_users()
        if (len(users) == 0):
            user = NewUser(0, "Administrador",
                           "Admin", "Algoritmos123")
            controller.save(user)
