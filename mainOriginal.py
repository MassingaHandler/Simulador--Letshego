import flet as ft
from Views.Login import LoginView
from Views.Index import SimuladorView

def main(page: ft.Page):
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/Login",
                [
                    LoginView(page),
                ],
            )
        )
        if page.route == "/Index":

            if not page.client_storage.get("/Login"):
                page.go("/Login")
                print(page.client_storage.get("/Login"))
                print(page.route)
                page.update()
            else:
                page.views.append(
                    ft.View(
                        "/Index",
                        [
                            SimuladorView(page),
                        ],
                    )
                )
        page.update()
        if page.route == "/":
            page.go("/Login")
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)