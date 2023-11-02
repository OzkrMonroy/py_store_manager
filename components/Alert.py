import flet as ft


class Alert:
    def __init__(self, page: ft.Page, title, description, ok_callback) -> None:
        self.title = title
        self.description = description
        self.ok_callback = ok_callback
        self.page = page
        self.build()

    def build(self):
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(self.title),
            content=ft.Text(self.description),
            actions_alignment=ft.MainAxisAlignment.END)

        dialog.actions = [
            ft.TextButton("No", on_click=lambda e: self.dismiss_alert(dialog)),
            ft.TextButton(
                "Sí", on_click=lambda e: self.on_ok_click(dialog)),
        ]
        self.show(dialog)

    def show(self, dialog):
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def dismiss_alert(self, dialog):
        dialog.open = False
        self.page.update()

    def on_ok_click(self, dialog):
        self.ok_callback()
        self.dismiss_alert(dialog)
