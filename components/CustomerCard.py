import flet as ft
from components.Alert import Alert
from controllers.CustomerController import CustomerController
from utils.routes import routes


class CustomerCard(ft.UserControl):
    controller = CustomerController()

    def __init__(self, page: ft.Page, customer, delete_callback):
        super().__init__()
        self.customer = customer
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
                           ft.Text(self.customer.name)]),
                    ft.Row([ft.Text("Dirección:", font_family=font_family), ft.Text(
                        self.customer.address)]),
                    ft.Row([ft.Text("Teléfono:", font_family=font_family), ft.Text(
                        self.customer.phone)]),
                    ft.Row([ft.Text("Nit:", font_family=font_family), ft.Text(
                        self.customer.nit)]),
                    ft.Row(
                        [ft.TextButton("Editar", on_click=self.init_edit), ft.TextButton(
                            "Borrar", on_click=self.show_alert)],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ), padding=20
        ))
        return self.card

    def show_alert(self, e):
        Alert(self.page, "Eliminar cliente",
              f"¿Desea eliminar a {self.customer.name}?", self.delete_card, "")

    def delete_card(self):
        self.delete_callback(self)

    def init_edit(self, e):
        self.controller.set_element_to_update(self.customer)
        self.page.go(routes["new-customer"])
