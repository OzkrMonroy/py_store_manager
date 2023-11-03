import flet as ft
from components.Alert import Alert


class UserCard(ft.UserControl):
    def __init__(self, page: ft.Page, user, delete_callback):
        super().__init__()
        self.user = user
        self.parent: ft.Row
        self.card: ft.Card
        self.delete_callback = delete_callback
        self.page = page

    def build(self):
        self.card = ft.Card(width=300, content=ft.Container(
            content=ft.Column(
                [
                    ft.Row([ft.Text("Nombre:"), ft.Text(self.user.name)]),
                    ft.Row([ft.Text("Usuario:"), ft.Text(self.user.user_name)]),
                    ft.Row(
                        [ft.TextButton("Editar"), ft.TextButton(
                            "Borrar", on_click=self.show_alert)],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ), padding=20
        ))
        return self.card

    def show_alert(self, e):
        if (self.user.id != "0"):
            Alert(self.page, "Eliminar usuario",
                  f"¿Desea eliminar a {self.user.name}?", self.delete_card, "")
        else:
            Alert(self.page, "Información",
                  f"No puedes eliminar a {self.user.name}", self.delete_card, "info")

    def delete_card(self):
        self.delete_callback(self)
