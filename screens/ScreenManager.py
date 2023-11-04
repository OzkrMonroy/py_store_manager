import flet as ft
from screens.Login import Login
from screens.Dashboard import Dashboard
from screens.Users import Users
from screens.AddUser import AddUser
from screens.Customers import Customers
from screens.AddCustomer import AddCustomer
from screens.Products import Products
from screens.AddProduct import AddProduct
from controllers.AuthController import AuthController
from utils.routes import routes


class ScreenManager:
    auth_controller = AuthController()

    def __init__(self) -> None:
        ft.app(target=self.__render_page, assets_dir="assets")
        self.page

    def __render_page(self, page: ft.Page):
        self.page = page
        page.title = "Inventario"
        page.padding = 0
        page.fonts = {
            "Roboto": "../assets/fonts/Roboto/Roboto-Regular.ttf",
            "Roboto Bold": "../assets/fonts/Roboto/Roboto-Bold.ttf",
            "Roboto Black": "../assets/fonts/Roboto/Roboto-Black.ttf",
            "PlaypenSans Black": "../assets/fonts/Playpen_Sans/PlaypenSans-ExtraBold.ttf",
        }
        page.theme = ft.Theme(font_family="Roboto")
        page.auto_scroll = True
        page.scroll = ft.ScrollMode.ADAPTIVE
        page.on_route_change = self.__route_change

        user = self.auth_controller.get_auth_user()
        if (user):
            page.go(routes["dashboard"])
        else:
            page.go(routes["login"])

    def __route_change(self, _):
        self.page.views.clear()
        if self.page.route == routes["login"]:
            self.page.views.append(
                ft.View(
                    routes["login"],
                    [Login(self.page)]
                )
            )
        if self.page.route == routes["dashboard"]:
            self.page.views.append(
                ft.View(routes["dashboard"], [Dashboard(self.page)]))

        if self.page.route == routes["users"]:
            self.page.views.append(
                ft.View(routes["users"], [Users(self.page)]))
        if self.page.route == routes["new-user"]:
            self.page.views.append(
                ft.View(routes["new-user"], [AddUser(self.page)]))

        if self.page.route == routes["customers"]:
            self.page.views.append(
                ft.View(routes["customers"], [Customers(self.page)]))
        if self.page.route == routes["new-customer"]:
            self.page.views.append(
                ft.View(routes["new-customer"], [AddCustomer(self.page)]))

        if self.page.route == routes["products"]:
            self.page.views.append(
                ft.View(routes["products"], [Products(self.page)]))
        if self.page.route == routes["new-product"]:
            self.page.views.append(
                ft.View(routes["new-product"], [AddProduct(self.page)]))

        self.page.update()
