import flet as ft
from utils.routes import routes


class NavigationRail(ft.UserControl):
    dict_routes = {
        "0": "/users",
        "1": "/customers",
        "2": "/products",
        "3": "/cart"
    }

    def __init__(self, page, selected_index: None | int):
        super().__init__()
        self.page = page
        self.selected_index = selected_index

    def build(self):
        return ft.NavigationRail(
            selected_index=self.selected_index,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-1,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.ADMIN_PANEL_SETTINGS_OUTLINED, selected_icon=ft.icons.ADMIN_PANEL_SETTINGS, label="Usuarios"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.PERSON_OUTLINED),
                    selected_icon_content=ft.Icon(ft.icons.PERSON),
                    label="Clientes",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.LOCAL_GROCERY_STORE_OUTLINED,
                    selected_icon_content=ft.Icon(
                        ft.icons.LOCAL_GROCERY_STORE),
                    label_content=ft.Text("Productos"),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.PRICE_CHECK_OUTLINED,
                    selected_icon_content=ft.Icon(
                        ft.icons.PRICE_CHECK),
                    label_content=ft.Text("Facturación"),
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.LOGOUT,
                    label_content=ft.Text("Salir"),
                ),
            ],
            on_change=lambda e: self.navigate(e.control.selected_index),
        )

    def navigate(self, index: int):
        if (index != 4):
            print("Selected destination:", f"{self.dict_routes[f'{index}']}")
            self.page.go(f"{self.dict_routes[f'{index}']}")
            return
        self.page.go(routes["login"])
