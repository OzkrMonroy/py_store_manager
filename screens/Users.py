import flet as ft
from components.NavigationRail import NavigationRail
from components.Card import Card
from components.Snackbar import Snackbar


class Users(ft.UserControl):
    card_row: ft.Row | None

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
        users = ["Oscar", "Carlos", "William", "Jefferson"]

        def delete(card):
            card_parent.controls.remove(card)
            self.update()
            Snackbar(self.page, "Se ha eliminado al usuario")

        for user in users:
            card = Card(self.page, user, delete)
            card_parent.controls.append(card)
            card.parent = card_parent

        return card_parent

    def __add_user(self, e):
        print("Add new user")
