import flet as ft
from controllers.CustomerController import CustomerController
from classes.Customer import Customer
from components.NavigationRail import NavigationRail
from components.CustomerCard import CustomerCard
from components.Snackbar import Snackbar
from utils.routes import routes


class Customers(ft.UserControl):
    user_controller = CustomerController()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        row = ft.Row([
            NavigationRail(self.page, 1),
            ft.VerticalDivider(width=1),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column([
                    ft.Row([
                        ft.Text("Clientes", font_family="Roboto Bold",
                                style=ft.TextThemeStyle.HEADLINE_LARGE),
                        ft.FilledTonalButton(
                            "Agregar", on_click=self.__add_customer)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    self.create_user_cards()
                ], expand=True, spacing=20, alignment=ft.MainAxisAlignment.START)
            )
        ], width=self.page.window_width, height=self.page.window_height)
        return row

    def create_user_cards(self):
        card_parent = ft.Row(controls=[], wrap=True,
                             width=self.page.window_width)
        customers = self.user_controller.get_customers()

        def delete(card, customer: Customer):
            deleted = self.user_controller.delete(customer)
            if (deleted):
                card_parent.controls.remove(card)
                self.update()
                Snackbar(self.page, "Cliente eliminado")

        if (len(customers) > 0):
            for customer in customers:
                card = CustomerCard(self.page, customer, delete)
                card_parent.controls.append(card)
                card.parent = card_parent
        else:
            self.__add_empty_element(card_parent)

        return card_parent

    def __add_empty_element(self, card_parent: ft.Row):
        card_parent.controls.append(ft.Column([
            ft.Image(src="/images/empty.png",
                     height=300, fit=ft.ImageFit.FILL),
            ft.Container(content=ft.Text(
                "No hay clientes", size=20), margin=30),
        ], height=450, width=self.page.window_width, horizontal_alignment=ft.CrossAxisAlignment.CENTER))

    def __add_customer(self, e):
        self.page.go(routes["new-customer"])
