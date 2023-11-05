import flet as ft
from components.NavigationRail import NavigationRail
from components.Alert import Alert
from components.Snackbar import Snackbar
from controllers.ProductCategoryController import ProductCategoryController
from classes.ProductCategory import ProductCategory
from utils.routes import routes


class AddProductCategory(ft.UserControl):
    category_controller = ProductCategoryController()
    _name_field = ft.TextField(label="Nombre", autofocus=True)
    _description_field = ft.TextField(label="Descripción")
    _page_title = "Agregar "
    _is_to_update = False
    _element_to_update = None

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        self.__fill_fields()
        return ft.Row([
            NavigationRail(self.page, 3),
            ft.VerticalDivider(width=1),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column([
                    ft.Text(f"{self._page_title} categoría", font_family="Roboto Bold",
                            style=ft.TextThemeStyle.HEADLINE_LARGE),
                    self._name_field,
                    self._description_field,
                    ft.Row([
                        ft.ElevatedButton(
                            text="Cancelar", on_click=lambda e:  self.page.go(routes["products-category"]), height=50, width=200),
                        ft.ElevatedButton(
                            text=self._page_title, on_click=self.__on_add, height=50, width=200),
                    ], alignment=ft.MainAxisAlignment.END)
                ], expand=True, spacing=24)
            )
        ], width=self.page.window_width, height=self.page.window_height)

    def __on_add(self, e):
        name = self._name_field.value.strip()
        description = self._description_field.value.strip()

        pass_validation = self.__validations(
            name, description)

        if (pass_validation):
            category = ProductCategory(0, name, description)
            created = None
            if (self._is_to_update):
                category.id = self._element_to_update.id
                created = self.category_controller.update(category)
            else:
                created = self.category_controller.save(category)
            self.__notify_add_product(created)

    def __fill_fields(self):
        options = self.category_controller.get_element_to_update()
        if (options[0]):
            category = options[1]
            self._is_to_update = options[0]
            self._element_to_update = category
            self._page_title = "Actualizar "
            self._name_field.value = category.name
            self._description_field.value = category.description

    def __validations(self, name: str, description: str) -> bool:
        if (name == "" and description == ""):
            Alert(self.page, "Información",
                  "Todos los campos son obligatorios", None, "info")
            return False
        return True

    def __notify_add_product(self, created: bool):
        success_message = "Categoría actualizada" if self._is_to_update else "Categoría agregada"
        error_message = "Ha ocurrido un error al actualizar la categoría" if self._is_to_update else "Ha ocurrido un error al crear la categoría"
        if (created):
            Snackbar(self.page, success_message)
            self._name_field.value = ""
            self._description_field.value = ""
            self.page.go(routes["products-category"])
            return
        Snackbar(self.page, error_message)
