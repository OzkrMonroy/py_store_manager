import flet as ft
from components.NavigationRail import NavigationRail
from components.Alert import Alert
from components.Snackbar import Snackbar
from controllers.CustomerController import CustomerController
from classes.Customer import Customer
from utils.routes import routes


class AddCustomer(ft.UserControl):
    user_controller = CustomerController()
    _name_field = ft.TextField(label="Nombre", autofocus=True)
    _address_field = ft.TextField(label="Dirección")
    _phone_field = ft.TextField(label="Teléfono")
    _nit_field = ft.TextField(label="Nit")
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
                    ft.Text(f"{self._page_title} cliente", font_family="Roboto Bold",
                            style=ft.TextThemeStyle.HEADLINE_LARGE),
                    self._name_field,
                    self._address_field,
                    self._phone_field,
                    self._nit_field,
                    ft.Row([
                        ft.ElevatedButton(
                            text="Cancelar", on_click=lambda e:  self.page.go(routes["customers"]), height=50, width=200),
                        ft.ElevatedButton(
                            text=self._page_title, on_click=self.__on_add, height=50, width=200),
                    ], alignment=ft.MainAxisAlignment.END)
                ], expand=True, spacing=24)
            )
        ], width=self.page.window_width, height=self.page.window_height)

    def __on_add(self, e):
        name = self._name_field.value.strip()
        address = self._address_field.value.strip()
        phone = self._phone_field.value.strip()
        nit = self._nit_field.value.strip()

        pass_validation = self.__validations(
            name, address, phone, nit)

        if (pass_validation):
            customer = Customer(0, name, address, phone, nit)
            created = None
            if (self._is_to_update):
                customer.id = self._element_to_update.id
                created = self.user_controller.update(customer)
            else:
                created = self.user_controller.save(customer)
            self.__notify_add_user(created)

    def __fill_fields(self):
        options = self.user_controller.get_element_to_update()
        if (options[0]):
            customer = options[1]
            self._is_to_update = options[0]
            self._element_to_update = customer
            self._page_title = "Actualizar "
            self._name_field.value = customer.name
            self._address_field.value = customer.address
            self._phone_field.value = customer.phone
            self._nit_field.value = customer.nit

    def __validations(self, name: str, address: str, phone: str, nit: str) -> bool:
        if (name == "" and address == "" and phone == "" and nit == ""):
            Alert(self.page, "Información",
                  "Todos los campos son obligatorios", None, "info")
            return False
        return True

    def __notify_add_user(self, created: bool):
        success_message = "Cliente actualizado" if self._is_to_update else "Cliente agregado"
        error_message = "Ha ocurrido un error al actualizar el cliente" if self._is_to_update else "Ha ocurrido un error al crear el cliente"
        if (created):
            Snackbar(self.page, success_message)
            self._name_field.value = ""
            self._address_field.value = ""
            self._phone_field.value = ""
            self._nit_field.value = ""
            self.page.go(routes["customers"])
            return
        Snackbar(self.page, error_message)
