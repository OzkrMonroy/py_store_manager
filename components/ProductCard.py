import flet as ft
from components.Alert import Alert
from controllers.ProductController import ProductController
from classes.Product import Product
from utils.routes import routes


class ProductCard(ft.UserControl):
    controller = ProductController()

    def __init__(self, page: ft.Page, product: Product):
        super().__init__()
        self.product = product
        self.parent: ft.Row
        self.card: ft.Card
        self.page = page

    def build(self):
        font_family = "Roboto Bold"
        self.card = ft.Card(width=300, content=ft.Container(
            content=ft.Column(
                [
                    ft.Row([ft.Text("Nombre:", font_family=font_family),
                           ft.Text(self.product.name)]),
                    ft.Row([ft.Text("Descripción:", font_family=font_family), ft.Text(
                        self.product.description)]),
                    ft.Row([ft.Text("Precio:", font_family=font_family), ft.Text(
                        self.product.price)]),
                    ft.Row([ft.Text("Cantidad:", font_family=font_family), ft.Text(
                        self.product.quantity)]),
                    ft.Row(
                        [ft.TextButton("Editar", on_click=self.init_edit)],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ), padding=20
        ))
        return self.card

    def init_edit(self, e):
        self.controller.set_element_to_update(self.product)
        self.page.go(routes["new-product"])
