import flet as ft
from controllers.ProductCategoryController import ProductCategoryController
from components.NavigationRail import NavigationRail
from components.ProductCategoryCard import ProductCategoryCard
from components.Snackbar import Snackbar
from classes.ProductCategory import ProductCategory
from utils.routes import routes


class ProductsCategory(ft.UserControl):
    product_category_controller = ProductCategoryController()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        row = ft.Row([
            NavigationRail(self.page, 3),
            ft.VerticalDivider(width=1),
            ft.Container(
                expand=True,
                padding=30,
                content=ft.Column([
                    ft.Row([
                        ft.Text("Categoría de productos", font_family="Roboto Bold",
                                style=ft.TextThemeStyle.HEADLINE_LARGE),
                        ft.FilledTonalButton(
                            "Agregar", on_click=self.__add_product)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    self.create_category_cards()
                ], expand=True, spacing=20, alignment=ft.MainAxisAlignment.START)
            )
        ], width=self.page.window_width, height=self.page.window_height)
        return row

    def create_category_cards(self):
        card_parent = ft.Row(controls=[], wrap=True,
                             width=self.page.window_width)
        categories = self.product_category_controller.get_categories()

        def delete(card, category: ProductCategory):
            deleted = self.product_category_controller.delete(category)
            if (deleted):
                card_parent.controls.remove(card)
                self.update()
                Snackbar(self.page, "Categoría eliminada")

        if (len(categories) > 0):
            for category in categories:
                card = ProductCategoryCard(self.page, category, delete)
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
                "No hay categorías", size=20), margin=30),
        ], height=450, width=self.page.window_width, horizontal_alignment=ft.CrossAxisAlignment.CENTER))

    def __add_product(self, e):
        self.page.go(routes["new-product-category"])
