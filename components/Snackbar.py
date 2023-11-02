import flet as ft


class Snackbar:
    def __init__(self, page: ft.Page, description) -> None:
        self.description = description
        self.page = page
        self.build()

    def build(self):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(self.description), duration=2000)
        self.page.snack_bar.open = True
        self.page.update()
