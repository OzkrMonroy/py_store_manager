import flet as ft
from components.Alert import Alert
from controllers.ProductCategoryController import ProductCategoryController
from classes.ProductCategory import ProductCategory
from utils.routes import routes


class ProductCategoryCard(ft.UserControl):
    controller = ProductCategoryController()

    def __init__(self, page: ft.Page, category: ProductCategory, delete_callback):
        super().__init__()
        self.category = category
        self.parent: ft.Row
        self.card: ft.Card
        self.delete_callback = delete_callback
        self.page = page

    def build(self):
        font_family = "Roboto Bold"
        self.card = ft.Card(width=300, content=ft.Container(
            content=ft.Column(
                [
                    ft.Row([ft.Text("Nombre:", font_family=font_family),
                           ft.Text(self.category.name)]),
                    ft.Row([ft.Text("Descripción:", font_family=font_family), ft.Text(
                        self.category.description, overflow=ft.TextOverflow.ELLIPSIS, width=250)]),
                    ft.Row(
                        [ft.TextButton("Editar", on_click=self.init_edit), ft.TextButton(
                            "Borrar", on_click=self.show_alert)],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ), padding=20
        ))
        return self.card

    def init_edit(self, e):
        self.controller.set_element_to_update(self.category)
        self.page.go(routes["new-category"])

    def show_alert(self, e):
        Alert(self.page, "Eliminar categoría",
              f"¿Desea eliminar la categoría: {self.category.name}?", self.delete_card, "")

    def delete_card(self):
        self.delete_callback(self, self.category)
