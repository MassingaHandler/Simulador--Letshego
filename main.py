import flet as ft
import pickle
from Views.Login import LoginView
from Views.Index import SimuladorView
from Views.auth import authenticate_token
import warnings


def main(page: ft.Page):
       
    # def on_route_change(route):
    #     token = load_token()
    #     if authenticate_token(token):
    #         page.go('/Index')
    #         page.update()
    #     else:
    #         page.go('/login')  
    #         page.update()  

    #     new_page = {
    #         "/": LoginView(page),
    #         "/Index": SimuladorView(page),
    #         # "/signup": Signup,
    #         # "/me": Dashboard,
    #         # "/forgotpassword": ForgotPassword
    #     },[page.route](page)
        
        
    #     page.views.clear()
    #     page.views.append(
    #         ft.View(
    #             route, 
    #             [new_page]     
    #         )
    #     )


    warnings.filterwarnings("ignore", category=DeprecationWarning)
     
        
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route='/Login',
                controls= [
                    LoginView(page),
                ],
            )
        )
        if page.route == "/Index":
            token = load_token()
            if authenticate_token(token):
                page.views.append(
                    ft.View(
                        route='/Index',
                        controls=[
                            SimuladorView(page),
                        ],
                    )
                )
                # page.go('/Index')
            else:
                page.views.append(
                    ft.View(
                        route='/Login',
                        controls=[
                            LoginView(page),
                        ],
                    )
                )
                # page.go('/Login')

        if page.route == "/":
            page.go("/Login")
        page.update()

    # def view_pop(view):
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)
    
    def load_token():
        try:
            with open('token.pickle', 'rb') as f:
                token = pickle.load(f)
            return token
        except:
            return None


    page.on_route_change = route_change
    # # page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)