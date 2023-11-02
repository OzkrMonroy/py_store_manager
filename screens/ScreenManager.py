import flet as ft
from screens.Login import Login
from screens.Dashboard import Dashboard
from screens.Users import Users


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
        page.go("/users")

    def __route_change(self, route):
        self.page.views.clear()
        if self.page.route == '/login':
            self.page.views.append(
                ft.View(
                    "/login",
                    [Login(self.page)]
                )
            )
        if self.page.route == "/dashboard":
            self.page.views.append(
                ft.View("/dashboard", [Dashboard(self.page)]))
        if self.page.route == "/users":
            users_view = Users(self.page)
            self.page.views.append(ft.View("/users", [users_view]))
            users_view.update()

        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
