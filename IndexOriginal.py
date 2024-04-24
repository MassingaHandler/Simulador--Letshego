import flet as ft
# from Login import Login

def main(page: ft.Page):
    page.bgcolor = "#fdfdf9"
    page.padding = 0
    page.scroll = ft.ScrollMode.HIDDEN



    # #Definicao de routas
    # def route_change(route):
    #     page.views.clear()
    #     page.views.append(
    #         ft.View(
    #             route="Login",
    #             controls=[
    #                 Login,
    #             ]
    #         )
    #     )

    # page.on_route_change = route_change
    # page.update()
    
    

    header = ft.Container(
        bgcolor= '#fbd400',
        height=80,
        border_radius=ft.border_radius.only(top_left=15, top_right=15),
        padding=ft.padding.only(left=20, right=20),
        content=ft.Row(
            controls=[
                ft.Text(
                    value='Banco Letshego',
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    size=15,
                ),

                ft.Row(
                    controls=[
                        ft.Text(
                            value='Patricio',
                            color=ft.colors.BLACK,
                            weight=ft.FontWeight.BOLD,
                            size=15,
                        ),
                        ft.Icon(
                            name=ft.icons.PERSON,
                            color=ft.colors.BLACK,
                        ),
                    ]
                )

            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),

    )
    

    formulario_novo = ft.Container(
        padding=ft.padding.only(top=30),
        #border=ft.border.only(top=1, bottom=1),
        content=ft.ResponsiveRow(
            run_spacing=30,
            controls=[
                ft.Text(
                    value='Bem vindo ao simulador de crédito  do banco letshego',
                    size=25,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                # ft.TextField(
                #     col={'sm':12, 'lg':6},
                #     label='Nome completo...',
                #     label_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD,
                #         color=ft.colors.GREY_800
                #     ),
                #     text_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD,
                #         color=ft.colors.GREY_800
                #     ),
                #     focused_border_color= '#fbd400',
                # ),
                # ft.TextField(
                #     col={'sm':12, 'lg':6},
                #     label='Contacto...',
                #     label_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, 
                #         color=ft.colors.GREY_800
                #     ),
                #     text_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, 
                #         color=ft.colors.GREY_800
                #     ),
                #     focused_border_color= '#fbd400',
                # ),

                # ft.Dropdown(
                #     col=12,
                #     label='Selecione a entidade',
                #     options=[
                #         ft.dropdown.Option(key=1, text='Marinha de Guerra'),
                #         ft.dropdown.Option(text='Exercito'),
                #         ft.dropdown.Option(text='MINT'),
                #         ft.dropdown.Option(text='Reservistas'),
                #         ft.dropdown.Option(text='Interior'),
                #         ft.dropdown.Option(text='Pensionista'),
                #         ft.dropdown.Option(text='Forcas areas'),
                #         ft.dropdown.Option(text='ISDEF'),
                #     ],
                #     label_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, ),
                #     text_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, color=ft.colors.BLACK, bgcolor=ft.colors.WHITE),
                #         bgcolor=ft.colors.WHITE,
                # ),

                ft.Text(
                    value='Novo crédito ',
                    size=20,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                ),
                salario_novo := ft.TextField(
                    col={'sm':12, 'lg':4},
                    label='Salário Bruto...',
                    helper_text = 'Salário que reflete na folha de salário...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                ),
                descontos_novo := ft.TextField(
                    col={'sm':12, 'lg':4},
                    label='Descontos...',
                    helper_text = 'Todos descontos do cliente (Ex: subsidios...)',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.GREY_800
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                ),
                periodo_emprestimo := ft.TextField(
                    col={'sm':12, 'lg':4},
                    label='Anos a Descontar...',
                    helper_text = 'Colocar anos em que o cliente gostaria de ser descontado...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    # error_text='Colocar so numeros',
                    # error_style=ft.TextStyle(size = 15),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                ),
            ],
        )
    )
    ft.Divider(height=6, color=ft.colors.BLACK),

    #Calcular novo credito

    def calcular_novo(e):
        import math

        salario_liquido = salario_novo.value
        desconto_cal = descontos_novo.value
        periodo_emprestimo_real = periodo_emprestimo.value
        
        salario_real = float(salario_liquido) / 2
        capacidade_desconto = float(salario_real) - float(desconto_cal)
        taxa_anual = 0.32
        taxa_mensal = taxa_anual / 12
        
        #periodo_emprestimo_real = periodo_emprestimo  # em anos

        numero_pagamentos = float(periodo_emprestimo_real) * 12
        valor_emprestimo = (float(capacidade_desconto) * (1 - (1 + taxa_mensal)** - float(numero_pagamentos))) / (taxa_mensal)
        #emprestimo_maximo_formatado = '{:,.2f}'.format(emprestimo_maximo)

        tabela_result.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            content=ft.Text(value = f'{numero_pagamentos:.0f} Meses'),
                        ),
                        ft.DataCell(
                            content=ft.Text(value = f'{capacidade_desconto:,.2f} MZN')
                        ),
                        ft.DataCell(
                            content=ft.Text(value = f'{valor_emprestimo:,.2f} MZN'),
                        ),
                    ],
                    selected=False,
                    on_select_changed=toggle_select,
                    data=0,
                    
                ),    
            )
        
        tabela_result.update()
            

    btn_novo = ft.Row(
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.ElevatedButton(
                text='Calcular',
                bgcolor=ft.colors.BLACK,
                color=ft.colors.WHITE,
                on_click=calcular_novo,
            )
        ]
    )

    def toggle_select(e):
        e.control.selected = not e.control.selected
        print(f'Selecionando a linha de indice{e.control.data}')
        e.control.update()

    formulario_reforco = ft.Container(
        padding=ft.padding.only(top=30),
        content=ft.ResponsiveRow(
            run_spacing=30,
            controls=[
                ft.Text(
                    value='Reforço ',
                    size=20,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                ),
                salario_bruto := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Salário Bruto',
                    helper_text = 'Salário que reflete na folha de salário...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                ),
                vl_dividas_descontos := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Descontos',
                    helper_text = 'Somar todos descontos das dividas que tem em outros bancos inclusive letshego...',
                    helper_style = ft.TextStyle(italic=True, size=11, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                ),
                vl_desejado := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Valor do Emprestimo....',
                    helper_text = 'Valor total que o cliente gostaria de ter...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                ),
                tempo_pagamento := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Anos a ser Descontado',
                    helper_text = 'Colocar anos em que o cliente gostaria de ser descontado...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.GREY_800
                    ),
                    input_filter=ft.NumbersOnlyInputFilter(),
                    focused_border_color= '#fbd400',
                )
            ],
        )
    )

    # Calcular reforco

    def calcular_reforco(e):
        import math

        salario = salario_bruto.value
        valor_total = vl_dividas_descontos.value
        valor_desejado = vl_desejado.value
        anos_a_pagar = tempo_pagamento.value
        #calcular o valor total depois das dividas
        valor_sem_divida = float(salario) / 2

        valor_real = float(valor_sem_divida) - float(valor_total)
        meses = math.ceil(int(anos_a_pagar) * 12)
        juros = 1.032**meses

        prestacao_mensal = (float(valor_desejado) * float(juros) * float(0.032)) / (float(juros) - 1)

        
        # juros_mensal = math.ceil(int(valor_desejado) * 0.02836)
        # juros_total = math.ceil(int(anos_a_pagar) * juros)
        # prestacao_mensal_1 = float(valor_real) / meses
        # prestacao_mensal = float(prestacao_mensal_1) + juros_mensal
        #valor_total_emprestimo = float(juros) + float(prestacao_mensal)

        if valor_real >= prestacao_mensal:
            tabela_result.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            content=ft.Text(value = meses),
                        ),
                        ft.DataCell(
                            content=ft.Text(value = f' {prestacao_mensal:,.2f} MZN')
                        ),
                        ft.DataCell(
                            content=ft.Text(value = f' {valor_desejado} MZN'),
                        ),
                    ],
                    selected=False,
                    on_select_changed=toggle_select,
                    data=0,
                ),
            )

            tabela_result.update()
        else:
            tabela_result.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            content=ft.Text(value = 'Sem capacidade'),
                        ),
                        ft.DataCell(
                            content=ft.Text(value = 'Sem capacidade')
                        ),
                        ft.DataCell(
                            content=ft.Text(value = 'Sem capacidade'),
                        ),
                    ],
                    selected=False,
                    on_select_changed=toggle_select,
                    data=0,
                ),
            )

            tabela_result.update()



    btn_reforco = ft.Row(
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.ElevatedButton(
                text='Calcular',
                bgcolor=ft.colors.BLACK,
                color=ft.colors.WHITE,
                on_click=calcular_reforco,
            )
        ]
    )

    def toggle_select(e):
        e.control.selected = not e.control.selected
        print(f'Selecionando a linha de indice{e.control.data}')
        e.control.update()


    

    def resized(e):
        if page.web:
            datatable.current.width = page.width - 70
        else:
            datatable.current.width = page.window_width - 70
        
        datatable.current.update()

    page.on_resize = resized

    datatable = ft.Ref[ft.DataTable]()

    resultado = ft.Container(
        padding=ft.padding.only(top=20),
        
        content=ft.ResponsiveRow(
            controls=[
                ft.Text(
                    value='Resultado',
                    size=20,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                ),
                
                ft.Row(
                    scroll = ft.ScrollMode.AUTO,
                    
                    controls=[
                        tabela_result := ft.DataTable(
                            ref = datatable,
                            width = (page.width if page.width else page.window_width) - 70,
                            
                            columns=[
                                ft.DataColumn(
                                ft.Text("Meses"), 
                                numeric=False,
                                      
                                ),
                                ft.DataColumn(
                                    ft.Text("Prestacao Mensal"), 
                                    numeric=False,
                                ),
                                ft.DataColumn(
                                    ft.Text("Volor Total do emprestimo"), 
                                    numeric=False,
                                   
                                ),
                            ],
                            rows=[
                                
                            ],
                            show_checkbox_column=False,
                            # border_radius=ft.border_radius.only(
                            #     bottom_left=15, 
                            #     bottom_right=15,
                            # ),
                            border=ft.border.all(1),
                            #bgcolor=ft.colors.GREY_300,
                            data_text_style=ft.TextStyle(
                                color=ft.colors.BLACK,
                                weight=ft.FontWeight.BOLD,
                            ),
                            heading_row_color='#fbd400',
                            heading_text_style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                size=14,
                                color=ft.colors.BLACK,
                                
                            ),
                            vertical_lines=ft.BorderSide(
                                width=0.50,
                                color=ft.colors.BLACK,
                            ),
                        )
                    ],
                    
                )
            ],
        )
    )

    layout = ft.Container(
        expand=True,
        # bgcolor=ft.colors.GREY_300,
        padding=ft.padding.all(30),
        content=ft.Column(
            controls=[
                header,
                formulario_novo,
                btn_novo,
                formulario_reforco,
                btn_reforco,
                resultado,
            ]
        )
    )

    page.add(layout)


ft.app(target=main)
