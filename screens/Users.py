import flet as ft
from controllers.UserController import UserController
from components.NavigationRail import NavigationRail
from components.UserCard import UserCard
from components.Snackbar import Snackbar
from utils.routes import routes


class Users(ft.UserControl):
    user_controller = UserController()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        row = ft.Row([
            NavigationRail(self.page, 0),
            ft.VerticalDivider(width=1),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column([
                    ft.Row([
                        ft.Text("Usuarios", font_family="Roboto Bold",
                                style=ft.TextThemeStyle.HEADLINE_LARGE),
                        ft.FilledTonalButton(
                            "Agregar", on_click=self.__add_user)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    self.create_user_cards()
                ], expand=True, spacing=20, alignment=ft.MainAxisAlignment.START)
            )
        ], width=self.page.window_width, height=self.page.window_height)
        return row

    def create_user_cards(self):
        card_parent = ft.Row(controls=[], wrap=True,
                             width=self.page.window_width)
        users = self.user_controller.get_users()

        def delete(card):
            deleted = self.user_controller.delete(card.user)
            if (deleted):
                card_parent.controls.remove(card)
                self.update()
                Snackbar(self.page, "Usuario eliminado")

        if (len(users) > 0):
            for user in users:
                card = UserCard(self.page, user, delete)
                card_parent.controls.append(card)
                card.parent = card_parent
        else:
            card_parent.controls.append(ft.Column([
                ft.Image(src="/images/empty.png",
                             height=300, fit=ft.ImageFit.FILL),
                ft.Container(content=ft.Text(
                    "No hay usuarios", size=20), margin=30),
            ], height=450, width=self.page.window_width, horizontal_alignment=ft.CrossAxisAlignment.CENTER))

        return card_parent

    def __add_user(self, e):
        self.page.go(routes["new-user"])
