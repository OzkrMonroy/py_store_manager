import flet as ft
from components.NavigationRail import NavigationRail
from controllers.AuthController import AuthController


class Dashboard(ft.UserControl):
    user = AuthController()

    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        user = self.user.get_auth_user()
        user_name = user.name.split(" ")[0]
        return ft.Row([
            NavigationRail(self.page, None),
            ft.VerticalDivider(width=1),
            ft.Row([
                ft.Column([
                    ft.Text(""),
                    ft.Row([
                        ft.Column([
                            ft.Text(f"Bienvenido: {user_name}", font_family="PlaypenSans Black",
                                    text_align=ft.TextAlign.CENTER, style=ft.TextThemeStyle.HEADLINE_LARGE, width=350),
                            ft.Text(
                                "Selecciona una opción de la barra lateral para comenzar")
                        ], height=100, spacing=18)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Image(src="/images/welcome_dashboard.png",
                             height=300, fit=ft.ImageFit.FILL)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, height=self.page.window_height, expand=True)
            ], expand=True, alignment=ft.MainAxisAlignment.CENTER, height=self.page.window_height)
        ], expand=True, height=self.page.window_height)
