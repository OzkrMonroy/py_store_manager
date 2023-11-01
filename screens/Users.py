import flet as ft
from components.NavigationRail import NavigationRail


class Users(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Row([
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
                    ft.Column([
                        ft.DataTable(
                            columns=[ft.DataColumn(ft.Text("Nombre")), ft.DataColumn(
                                ft.Text("Acción"))],
                            rows=[
                                ft.DataRow(
                                    cells=[ft.DataCell(ft.Text("Oscar")), ft.DataCell(
                                        ft.Row([
                                            ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e: self.to_edit(
                                                e, 1), tooltip="Editar"),
                                            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: self.to_edit(
                                                e, 1), tooltip="Eliminar")
                                        ])
                                    )]),
                                ft.DataRow(
                                    cells=[ft.DataCell(ft.Text("Carlos")), ft.DataCell(ft.Row([
                                        ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e: self.to_edit(
                                            e, 1), tooltip="Editar"),
                                        ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: self.to_edit(
                                            e, 1), tooltip="Eliminar")
                                    ]))])
                            ],
                            width=self.page.window_width - 200,
                        )
                    ], scroll=True, expand=True)
                ], expand=True, spacing=20)
            )
        ], width=self.page.window_width, height=self.page.window_height)

    def to_edit(self, e, element_id):
        print("To edit", element_id)

    def __add_user(self, e):
        print("Add new user")
