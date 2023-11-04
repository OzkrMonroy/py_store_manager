import flet as ft


class Alert:
    def __init__(self, page: ft.Page, title, description, ok_callback, type) -> None:
        self.ok_callback = ok_callback
        self.page = page
        self.type = type
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title),
            content=ft.Text(description),
            actions_alignment=ft.MainAxisAlignment.END)
        self.build()

    def build(self):

        if (self.type == "info"):
            self.dialog.actions = [ft.TextButton(
                "Aceptar", on_click=self.dismiss_alert)]
        else:
            self.dialog.actions = [
                ft.TextButton(
                    "No", on_click=self.dismiss_alert),
                ft.TextButton(
                    "Sí", on_click=self.on_ok_click),
            ]
        self.show()

    def show(self):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def dismiss_alert(self, e):
        self.dialog.open = False
        self.page.update()

    def on_ok_click(self, e):
        self.ok_callback()
        self.dismiss_alert(self.dialog)
