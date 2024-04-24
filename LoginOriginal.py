import flet as ft
import os
from flet.auth.providers import GoogleOAuthProvider
#from flet.auth.providers import GitHubOAuthProvider
#pip install cryptography
from flet.security import encrypt, decrypt



# Autenticar via GITHUB
# GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
# GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
# SECRET = os.getenv("SECRET")

# GITHUB_CLIENT_ID = "1089941649587-srop8s83hr5pgacsvsn8klple0t14imf.apps.googleusercontent.com"
# GITHUB_CLIENT_ID_SECRET = ""
# SECRET = "FSDFSDFSFSDFSFSDFSFSDFSDFLKDFFNFDFDKFSKLDKNF"

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
SECRET = os.getenv("SECRET")

GOOGLE_CLIENT_ID = "1089941649587-srop8s83hr5pgacsvsn8klple0t14imf.apps.googleusercontent.com"
GOOGLE_CLIENT_ID_SECRET = "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"
SECRET = "FSDFSDFSFSDFSFSDFSFSDFSDFLKDFFNFDFDKFSKLDKNF"



def main(page: ft.Page):

    #Definicao de routas
    
    provider = GoogleOAuthProvider(
        client_id = GOOGLE_CLIENT_ID,
        client_secret = GOOGLE_CLIENT_SECRET,
        redirect_url = "http://127.0.0.1:54500/api/oauth/redirect"
    )

    encrypted_token = page.client_storage.get('google_token')
    if encrypted_token:
        saved_token = decrypt(encrypted_token, SECRET)
        page.login(provider=provider, saved_token=saved_token)

    def on_login(e: ft.LoginEvent):
        if not e.error:
            # import pprint
            # pprint.pprint(page.auth.user)
            token = page.auth.token.to_json()
            encrypted_token = encrypt(token, SECRET)
            page.client_storage.set("google_token", encrypted_token)
            #page.go('Index')

            
            
        else:
            print('Error:', e.error)
            print('Error', e.error_description)

    page.on_login = on_login

    page.fonts = {
        "LatoLight": "/fontes/Lato-Light.ttf"
    }


    #if page.auth:
    
        

    login = ft.Container(
        width=500,
        height=600,
        bgcolor=ft.colors.WHITE,
        #alignment=ft.alignment.center,
        border_radius =ft.border_radius.all(25),
        padding=ft.padding.all(50),
        content=ft.Column(
            #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value='Bem vindo ao',
                    size= 26,
                    color=ft.colors.BLACK,
                    font_family= 'LatoLight',
                    #weight=ft.FontWeight.W_100,
                ),
                ft.Text(
                    value='Banco Letshego',
                    size=26,
                    weight=ft.FontWeight.W_600,
                    color=ft.colors.BLACK,
                ),
                ft.Text(
                    value='Faca login com o email da google para ter acesso ao simulador',
                    color='#4a4f4c',
                    size=16,
                ),
                
                ft.Container(
                    padding=ft.padding.only(top=80),
                    content=ft.ElevatedButton(
                        height=50,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Image(
                                    src='assets/imagem/google.png',
                                    width=30,
                                    height=30,
                                ),
                                ft.Text(
                                    value='Iniciar a sessao com google',
                                    color=ft.colors.WHITE,
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                )
                            ],
                            # run_spacing=50,
                            # vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            # expand=True,
                        ),
                        
                        style=ft.ButtonStyle(
                            color={
                                ft.MaterialState.HOVERED: ft.colors.BLACK,
                                ft.MaterialState.DEFAULT: ft.colors.WHITE

                            },
                            bgcolor= {
                                ft.MaterialState.HOVERED: '#f7c70b',
                                '': '#312f83',
                            },
                        ),
                        on_click=lambda _: page.login(provider=provider)
                    )
                ) ,

                ft.Text(
                    value=''
                )         
            ],
        )
          
    )

    # btn = ft.Container(
    #         content=ft.ElevatedButton(
    #         content=ft.Row(
    #             alignment=ft.MainAxisAlignment.CENTER,
    #             spacing=4,
    #             controls=[
    #                 ft.Image(
    #                     src='assets/imagem/google.png',
    #                     width=30,
    #                     height=30,
    #                 )
    #             ]
    #         )
    #     )
    # )




    layout = ft.Container(
        expand=True,
        image_src='imagem/bg-2x.png',
        image_fit=ft.ImageFit.COVER,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                login,
            ]  
        )
    )


    page.add(layout)



ft.app(target= main, assets_dir='assets')