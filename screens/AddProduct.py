import flet as ft
from components.NavigationRail import NavigationRail
from components.Alert import Alert
from components.Snackbar import Snackbar
from controllers.ProductController import ProductController
from classes.Product import Product
from utils.routes import routes


class AddProduct(ft.UserControl):
    product_controller = ProductController()
    _name_field = ft.TextField(label="Nombre", autofocus=True)
    _description_field = ft.TextField(label="Descripción")
    _price_field = ft.TextField(label="Precio")
    _quantity_field = ft.TextField(label="Cantidad")
    _page_title = "Agregar "
    _is_to_update = False
    _element_to_update = None

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        self.__fill_fields()
        return ft.Row([
            NavigationRail(self.page, 1),
            ft.VerticalDivider(width=1),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column([
                    ft.Text(f"{self._page_title} producto", font_family="Roboto Bold",
                            style=ft.TextThemeStyle.HEADLINE_LARGE),
                    self._name_field,
                    self._description_field,
                    self._price_field,
                    self._quantity_field,
                    ft.Row([
                        ft.ElevatedButton(
                            text="Cancelar", on_click=lambda e:  self.page.go(routes["products"]), height=50, width=200),
                        ft.ElevatedButton(
                            text=self._page_title, on_click=self.__on_add, height=50, width=200),
                    ], alignment=ft.MainAxisAlignment.END)
                ], expand=True, spacing=24)
            )
        ], width=self.page.window_width, height=self.page.window_height)

    def __on_add(self, e):
        name = self._name_field.value.strip()
        description = self._description_field.value.strip()
        price = self._price_field.value.strip()
        quantity = self._quantity_field.value.strip()

        pass_validation = self.__validations(
            name, description, price, quantity)

        if (pass_validation):
            product = Product(0, name, description, price, quantity)
            created = None
            if (self._is_to_update):
                product.id = self._element_to_update.id
                created = self.product_controller.update(product)
            else:
                created = self.product_controller.save(product)
            self.__notify_add_product(created)

    def __fill_fields(self):
        options = self.product_controller.get_element_to_update()
        if (options[0]):
            product = options[1]
            self._is_to_update = options[0]
            self._element_to_update = product
            self._page_title = "Actualizar "
            self._name_field.value = product.name
            self._description_field.value = product.description
            self._price_field.value = product.price
            self._quantity_field.value = product.quantity

    def __validations(self, name: str, description: str, price: str, quantity: str) -> bool:
        if (name == "" and description == "" and price == "" and quantity == ""):
            Alert(self.page, "Información",
                  "Todos los campos son obligatorios", None, "info")
            return False
        return True

    def __notify_add_product(self, created: bool):
        success_message = "Producto actualizado" if self._is_to_update else "Producto agregado"
        error_message = "Ha ocurrido un error al actualizar el producto" if self._is_to_update else "Ha ocurrido un error al crear el producto"
        if (created):
            Snackbar(self.page, success_message)
            self._name_field.value = ""
            self._description_field.value = ""
            self._price_field.value = ""
            self._quantity_field.value = ""
            self.page.go(routes["products"])
            return
        Snackbar(self.page, error_message)
