import flet as ft
from screens.Login import Login
from screens.Dashboard import Dashboard
from screens.Users import Users
from screens.AddUser import AddUser
from utils.routes import routes


class ScreenManager:
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
        page.on_view_pop = self.view_pop
        page.go(routes["login"])

    def __route_change(self, route):
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

        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
