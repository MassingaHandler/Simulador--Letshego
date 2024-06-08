import flet as ft
import os
from validacao.validacao import is_valid_email, is_valid_password
from flet.auth.providers import GoogleOAuthProvider
#from flet.auth.providers import GitHubOAuthProvider
#pip install cryptography
from flet.security import encrypt, decrypt
from Views.auth import login_user, store_session




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




def LoginView(page):
    
    
    page.fonts = {
        "LatoLight": "/fontes/Lato-Light.ttf"
    }
    
    
    
    # provider = GoogleOAuthProvider(
    #     client_id = GOOGLE_CLIENT_ID,
    #     client_secret = GOOGLE_CLIENT_SECRET,
    #     redirect_url = "http://127.0.0.1:54500/api/oauth/redirect"
    # )

    # encrypted_token = page.client_storage.get('google_token')
    # if encrypted_token:
    #     saved_token = decrypt(encrypted_token, SECRET)
    #     page.login(provider=provider, saved_token=saved_token)

    # def on_login(e: ft.LoginEvent):
    #     if not e.error:
    #         # import pprint
    #         # pprint.pprint(page.auth.user)
    #         token = page.auth.token.to_json()
    #         encrypted_token = encrypt(token, SECRET)
    #         page.client_storage.set("google_token", encrypted_token)
    #         page.go('/Index')
    #         page.update()
            
            
    #     else:
    #         print('Error:', e.error)
    #         print('Error', e.error_description)
    # page.update()
    # page.on_login = on_login

    # if page.auth:
    #     # page.client_storage.set("key", "value")
    #     page.go("/Index")
    # else:
    #     ft.Text(value='Login Falfou')
    
    def login(e):
            if not is_valid_email(email_box.content.value):
                email_box.border = ft.Text('ivalido')
                email_box.update()

            if not is_valid_password(password_box.content.value):
                password_box.border = ft.Text('ivalido')
                password_box.update()

            else:
                email = email_box.content.value
                password = password_box.content.value

                page.splash = ft.ProgressBar()
                page.update()

                token = login_user(email, password)
                page.splash = None
                page.update()
                if token:
                    store_session(token)
                    page.go('/Index')
                    page.update()
                else:
                    page.snack_bar = ft.SnackBar(
                        ft.Text('Invalid credentials')
                    )
                    page.snack_bar.open = True
                    page.update()
          

   
        
    login = ft.ResponsiveRow(
        expand= False,
        alignment= ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                col = {"md":3},
                width=500,
                height=600,
                bgcolor=ft.colors.WHITE,
                alignment=ft.alignment.center,
                border_radius =ft.border_radius.all(25),
                padding=ft.padding.all(50),
                content=ft.Column(
                    
                    # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    # alignment= ft.MainAxisAlignment.CENTER,
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

                        email_box := ft.Container(
                            content=ft.TextField(
                                border=ft.InputBorder.NONE,
                                content_padding=ft.padding.only(
                                    top=0, bottom=0, right=20, left=20),
                                hint_style=ft.TextStyle(
                                    size=12, color=ft.colors.BLACK,
                                ),
                                hint_text='Enter email address...',
                                cursor_color='#858796',
                                text_style=ft.TextStyle(
                                    size=14,
                                    color='black',
                                ),
                                focused_border_color= '#fbd400',
                            ),
                            border=ft.border.all(width=1, color='#fbd400'),
                            border_radius=30
                        ),


                        password_box := ft.Container(
                            content=ft.TextField(
                                border=ft.InputBorder.NONE,
                                content_padding=ft.padding.only(
                                    top=0, bottom=0, right=20, left=20),
                                hint_style=ft.TextStyle(
                                    size=12, color=ft.colors.BLACK,
                                ),
                                text_style=ft.TextStyle(
                                    size=14,
                                    color='black',
                                ),
                                hint_text='Password',
                                cursor_color='#858796',
                                password=True,
                                focused_border_color= '#fbd400',
                            ),
                            border=ft.border.all(width=1, color='#fbd400'),
                            border_radius=30
                        ),
                        
                        ft.Container(
                            padding=ft.padding.only(top=30),
                            content=ft.ElevatedButton(
                                height=50,
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        # ft.Image(
                                        #     src='/imagem/icon.png',
                                        #     width=30,
                                        #     height=30,
                                        #     border_radius=ft.border_radius.all(50),
                                        # ),
                                        ft.Text(
                                            value='Entrar',
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
                                # on_click=lambda _: page.go('/index')
                                on_click=login
                            )
                        ),

                        ft.Column(
                            controls=[
                                ft.Text(
                                    value='Para ter acesso ao simulador entre em contacto com os ITs',
                                    color='#4a4f4c',
                                    size=15,
                                    text_align=ft.TextAlign.JUSTIFY,
                                ), 
                            ],
                            
                        )       
                    ],
                )
            )
        ]
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

    return  ft.Container(
        expand=True,
        image_src='imagem/bg-2x.png',
        image_fit=ft.ImageFit.COVER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                login,
            ]  
        )
    )


    page.add(layout)



# ft.app(target= main, assets_dir='assets')