import flet as ft
from Views.auth import load_token, get_email, revoke_token
# from Login import Login

def SimuladorView(page):
    page.theme_mode = 'dark'
    page.scroll = ft.ScrollMode.HIDDEN
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK
    page.padding = 0
    


    nome_usuario = get_email(load_token())
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
        content=ft.ResponsiveRow(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            columns=12,
            expand=False,
            controls=[
                ft.Text(
                    col=6,
                    value='Banco Letshego',
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    size=15,
                ),

                ft.Row(
                    col=6,
                    controls=[
                        ft.Text(
                            value=nome_usuario,
                            color=ft.colors.BLACK,
                            weight=ft.FontWeight.BOLD,
                            size=15,
                        ),
                        ft.IconButton(
                            icon=ft.icons.LOGOUT,
                            icon_color=ft.colors.RED,
                            on_click=lambda _: (revoke_token(load_token()),page.go('/Login'))
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                )

            ],
        ),

    )
    def clear(e):
        tabela_result.rows.clear()
        
        page.update()

    def logout(e):
        (revoke_token(load_token)),
        page.go('/Login')
    

    formulario_novo = ft.Container(
        padding=ft.padding.only(top=30),
        #border=ft.border.only(top=1, bottom=1),
        content=ft.ResponsiveRow(
            run_spacing=30,
            controls=[
                ft.Text(
                    value='Bem vindo ao simulador de crédito  do banco letshego',
                    size=25,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                 ft.Container  (
                    bgcolor='#fbd400',
                    height=30,
                    border_radius=ft.border_radius.all(15),
                    padding=ft.padding.only(left=20),
                    content=ft.Text(
                        value='Capacidade Maxima',
                        size=15,
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.BOLD,
                    )     
                ),
                salario_novo := ft.TextField(
                    col={'sm':12, 'lg':4},
                    label='Salário Bruto...',
                    helper_text = 'Salário que reflete na folha de salário...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                    border_color= ft.colors.WHITE
                ),
                descontos_novo := ft.TextField(
                    col={'sm':12, 'lg':4},
                    label='Descontos...',
                    helper_text = 'Todos descontos do cliente (Ex: subsidios...)',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                    border_color= ft.colors.WHITE
                ),
                periodo_emprestimo := ft.TextField(
                    col={'sm':12, 'lg':4},
                    label='Meses a Descontar...',
                    helper_text = 'Colocar meses em que o cliente gostaria de ser descontado...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    # error_text='Colocar so numeros',
                    # error_styles=ft.TextStyle(size = 15),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                    border_color= ft.colors.WHITE
                ),
            ],
        )
    )
    ft.Divider(height=6, color=ft.colors.BLACK),

    #Calcular novo credito

    # def capacidade_maxima(e):
    #     salario_liquido = float(salario_novo.value)
    #     desconto_cal = float(descontos_novo.value)
    #     periodo_mensal = int(periodo_emprestimo.value)
    
    #     if salario_liquido < 10000:
    #         salario_real = salario_liquido * 0.33
        
    #     elif salario_liquido >= 10000 and salario_liquido <= 30000:
    #         salario_real = salario_liquido * 0.60
        
    #     elif salario_liquido > 30000:
    #         salario_real = salario_liquido * 0.70
        
    #     taxa_juro = 0.345/12
    #     salario_liquido = salario_real - desconto_cal
        
    #     capacidadeMaxima = salario_liquido * (1 - (1 + taxa_juro)**(-periodo_mensal))/taxa_juro
        
    #     if periodo_mensal <=12:
    #         seguro = salario_liquido * 0.0045
        
    #     elif periodo_mensal > 12 and periodo_mensal <= 36:
    #         seguro = salario_liquido * 0.0033
        
    #     elif periodo_mensal > 36:
    #         seguro = salario_liquido * 0.0028
        
        
    #     valor_a_receber = capacidadeMaxima - seguro


    #     tabela_result.rows.append(
    #         ft.DataRow(
    #             cells=[
    #                 ft.DataCell(
    #                     content=ft.Text(value = f'{periodo_mensal:.0f} Meses'),
    #                 ),
    #                 ft.DataCell(
    #                     content=ft.Text(value = f'{salario_liquido:,.2f} MZN')
    #                 ),
    #                 ft.DataCell(
    #                     content=ft.Text(value = f'{capacidadeMaxima:,.2f} MZN'),
    #                 ),
    #             ],
    #             selected=False,
    #             on_select_changed=toggle_select,
    #             data=0,
                
    #         ),    
    #     )
    #     tabela_result.update()


    def capacidade_maxima(e):
        salario_bruto = float(salario_novo.value)
        desconto_cal = float(descontos_novo.value)
        meses = int(periodo_emprestimo.value)

        # Calcular a capacidade de endividamento
        if salario_bruto <= 10000:
            capacidade_endividamento = salario_bruto * 0.33
        elif 10001 <= salario_bruto <= 30000:
            capacidade_endividamento = salario_bruto * 0.60
        else:
            capacidade_endividamento = salario_bruto * 0.70

        # Ajustar a capacidade de endividamento subtraindo os descontos
        capacidade_endividamento_ajustada = capacidade_endividamento - desconto_cal

        # Verificar se a capacidade de endividamento ajustada é positiva
        if capacidade_endividamento_ajustada <= 0:
            tabela_result.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            content=ft.Text(value = 'Sem Capacidade'),
                        ),
                        ft.DataCell(
                            content=ft.Text(value = 'Sem Capacidade')
                        ),
                        ft.DataCell(
                            content=ft.Text(value = 'Sem Capacidade'),
                        ),
                    ],
                    selected=False,
                    on_select_changed=toggle_select,
                    data=0,
                    
                ),    
            )
            tabela_result.update()

        # Definir a taxa de juros anual
        taxa_anual = 0.345
        juros = taxa_anual / 12

        # Calcular a taxa de seguro com base no período do empréstimo
        if meses <= 12:
            taxa_seguro = 0.0045
        elif 12 < meses <= 36:
            taxa_seguro = 0.0033
        else:
            taxa_seguro = 0.0028

        # Função para calcular a prestação mensal base
        def calcular_prestacao_mensal(valor_emprestimo, juros, meses):
            return (valor_emprestimo * juros) / (1 - (1 + juros) ** -meses)

        # Iterar para encontrar o valor máximo do empréstimo
        valor_emprestimo = 0
        incremento = 100  # Incremento para ajustar o valor do empréstimo
        prestacao_mensal_com_seguro = 0  # Inicializar a variável de prestação

        while True:
            prestacao_mensal_base = calcular_prestacao_mensal(valor_emprestimo, juros, meses)
            prestacao_mensal_com_seguro = prestacao_mensal_base + (valor_emprestimo * taxa_seguro)
            
            if prestacao_mensal_com_seguro > capacidade_endividamento_ajustada:
                break
            
            valor_emprestimo += incremento

        # Ajustar para o valor máximo que não excede a capacidade
        valor_emprestimo -= incremento
        prestacao_mensal_base = calcular_prestacao_mensal(valor_emprestimo, juros, meses)
        prestacao_mensal_com_seguro = prestacao_mensal_base + (valor_emprestimo * taxa_seguro)

        # Exibir a prestação mensal e o valor máximo do empréstimo
        # print(f"O valor máximo do empréstimo é: {valor_emprestimo:.2f}")
        # print(f"A prestação mensal será: {prestacao_mensal_com_seguro:.2f}")
        tabela_result.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        content=ft.Text(value = f'{meses} Meses'),
                    ),
                    ft.DataCell(
                        content=ft.Text(value = f'{prestacao_mensal_com_seguro:,.2f} MZN')
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
                bgcolor='#fbd400',
                color=ft.colors.BLACK,
                on_click=capacidade_maxima,
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
                # ft.Text(
                #     value='Bem vindo ao simulador de crédito  do banco letshego',
                #     size=25,
                #     color=ft.colors.WHITE,
                #     weight=ft.FontWeight.BOLD,
                #     text_align=ft.TextAlign.CENTER,
                # ),
                ft.Container  (
                    bgcolor='#fbd400',
                    height = 30,
                    border_radius=ft.border_radius.all(15),
                    padding=ft.padding.only(left=20),
                    content=ft.Text(
                        value='Valor especifico',
                        size=15,
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.BOLD,
                    )
                    
                ),
                salario_Bruto := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Salário Bruto',
                    helper_text = 'Salário que reflete na folha de salário...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                    border_color= ft.colors.WHITE
                ),
                vl_dividas_descontos := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Descontos',
                    helper_text = 'Somar todos descontos das dividas que tem em outros bancos inclusive letshego...',
                    helper_style = ft.TextStyle(italic=True, size=11, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                    border_color= ft.colors.WHITE
                ),
                vl_desejado := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Valor do Emprestimo....',
                    helper_text = 'Valor total que o cliente gostaria de ter...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    input_filter=ft.InputFilter(
                        allow=True,
                        regex_string=r"[0-9-.]"
                    ),
                    focused_border_color= '#fbd400',
                    border_color= ft.colors.WHITE

                ),
                tempo_pagamento := ft.TextField(
                    col={'sm':12, 'lg':6},
                    label='Meses a ser Descontado',
                    helper_text = 'Colocar meses em que o cliente gostaria de ser descontado...',
                    helper_style = ft.TextStyle(italic=True, size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, 
                        color=ft.colors.WHITE
                    ),
                    input_filter=ft.NumbersOnlyInputFilter(),
                    focused_border_color= '#fbd400',
                    border_color= ft.colors.WHITE
                ),
            ],
        )
    )

    # Calcular reforco

    # def prestacao_mensal(e):

    #     valor_desejado = float(vl_desejado.value)
    #     salario = float(salario_bruto.value)
    #     descontos = float(vl_dividas_descontos.value)
    #     periodo_mensal = int(tempo_pagamento.value)
    #     taxa_juro = 0.345/12

    #     if salario < 10000:
    #         salario_real = salario * 0.33
        
    #     elif salario >= 10000 and salario <= 30000:
    #         salario_real = salario * 0.60
        
    #     elif salario > 30000:
    #         salario_real = salario * 0.70
       
        
    #     salario_liquido = salario_real - descontos

    #     capacidadeMaxima = salario_liquido * (1 - (1 + taxa_juro)**(-periodo_mensal))/taxa_juro
        
        


    #     if periodo_mensal <= 12:
    #         seguro = valor_desejado * 0.0045
        
    #     elif periodo_mensal > 12 and periodo_mensal <= 36:
    #         seguro = valor_desejado * 0.0033
        
    #     elif periodo_mensal > 36:
    #         seguro = valor_desejado * 0.0028

    #     prestacao = (valor_desejado * taxa_juro)/(1 - (1 + taxa_juro) ** (-periodo_mensal)) + seguro

    #     print(seguro)
    #     print(prestacao)
        
    #     if  capacidadeMaxima < valor_desejado:
    #         tabela_result.rows.append(
    #             ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(
    #                         content=ft.Text(value = 'Sem Capacidade'),
    #                     ),
    #                     ft.DataCell(
    #                         content=ft.Text(value = 'Sem Capacidade')
    #                     ),
    #                     ft.DataCell(
    #                         content=ft.Text(value = 'Sem Capacidade'),
    #                     ),
    #                 ],
    #                 selected=False,
    #                 on_select_changed=toggle_select,
    #                 data=0,
    #             ),
    #         )

    #         tabela_result.update()
    #     else:
    #         tabela_result.rows.append(
    #             ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(
    #                         content=ft.Text(value = f'{periodo_mensal} Meses'),
    #                     ),
    #                     ft.DataCell(
    #                         content=ft.Text(value = f' {prestacao:,.2f} MZN')
    #                     ),
    #                     ft.DataCell(
    #                         content=ft.Text(value = f' {valor_desejado} MZN'),
    #                     ),
    #                 ],
    #                 selected=False,
    #                 on_select_changed=toggle_select,
    #                 data=0,
    #             ),
    #         )
    #         tabela_result.update()


    def prestacao_mensal(e):
        valor_desejado = float(vl_desejado.value)
        salario_bruto = float(salario_Bruto.value)
        desconto_cal = float(vl_dividas_descontos.value)
        meses = int(tempo_pagamento.value)

        # Calcular a capacidade de endividamento
        if salario_bruto <= 10000:
            capacidade_endividamento = salario_bruto * 0.33
        elif 10001 <= salario_bruto <= 30000:
            capacidade_endividamento = salario_bruto * 0.60
        else:
            capacidade_endividamento = salario_bruto * 0.70

        # Ajustar a capacidade de endividamento subtraindo os descontos
        capacidade_endividamento_ajustada = capacidade_endividamento - desconto_cal

        # Verificar se a capacidade de endividamento ajustada é positiva
        if capacidade_endividamento_ajustada <= 0:
            print("Os descontos são maiores ou iguais à capacidade de endividamento. Não é possível conceder o empréstimo.")
            exit()

        # Definir a taxa de juros anual
        taxa_anual = 0.345
        juros = taxa_anual / 12

        # Calcular a taxa de seguro com base no período do empréstimo
        if meses <= 12:
            taxa_seguro = 0.0045
        elif 12 < meses <= 36:
            taxa_seguro = 0.0033
        else:
            taxa_seguro = 0.0028

        # Função para calcular a prestação mensal base
        def calcular_prestacao_mensal(valor_emprestimo, juros, meses):
            return (valor_emprestimo * juros) / (1 - (1 + juros) ** -meses)

        # Calcular a prestação mensal base e com seguro
        prestacao_mensal_base = calcular_prestacao_mensal(valor_desejado, juros, meses)
        prestacao_mensal_com_seguro = prestacao_mensal_base + (valor_desejado * taxa_seguro)

        # Verificar se a prestação mensal com seguro excede a capacidade de endividamento ajustada
        if prestacao_mensal_com_seguro > capacidade_endividamento_ajustada:
            tabela_result.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            content=ft.Text(value = 'Sem Capacidade'),
                        ),
                        ft.DataCell(
                            content=ft.Text(value = 'Sem Capacidade')
                        ),
                        ft.DataCell(
                            content=ft.Text(value = 'Sem Capacidade'),
                        ),
                    ],
                    selected=False,
                    on_select_changed=toggle_select,
                    data=0,
                ),
            )
            tabela_result.update()
        
        else:
            # print(f"O valor do empréstimo é: {valor_desejado:.2f}")
            # print(f"A prestação mensal será: {prestacao_mensal_com_seguro:.2f}")
            tabela_result.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            content=ft.Text(value = f'{meses} Meses'),
                        ),
                        ft.DataCell(
                            content=ft.Text(value = f' {prestacao_mensal_com_seguro:,.2f} MZN')
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
           

            

            
           



    btn_reforco = ft.Row(
        alignment=ft.MainAxisAlignment.START,
        controls=[
            ft.ElevatedButton(
                text='Calcular',
                bgcolor='#fbd400',
                color=ft.colors.BLACK,
                on_click=prestacao_mensal,
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
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                
                ft.Row(
                    scroll = ft.ScrollMode.ALWAYS,
                    controls=[
                        tabela_result := ft.DataTable(
                            ref = datatable,
                            width = (page.width if page.width else page.window_width) - 70,
                            columns=[
                                ft.DataColumn(
                                ft.Text("Meses", max_lines=1,), 
                                numeric=False,
                                      
                                ),
                                ft.DataColumn(
                                    ft.Text("Prestacao Mensal", max_lines=1,), 
                                    numeric=False,
                                ),
                                ft.DataColumn(
                                    ft.Text("Volor Total do emprestimo", max_lines=1), 
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
                            border=ft.border.all(1, 'white'),
                            #bgcolor=ft.colors.GREY_300,
                            data_text_style=ft.TextStyle(
                                color=ft.colors.WHITE,
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
                                color=ft.colors.WHITE,
                            ),
                            horizontal_lines=ft.BorderSide(
                                width=0.50,
                                color=ft.colors.WHITE,
                            ),
                            column_spacing=10,
                        )   
                    ],
                )
            ],
        )
    )

    floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.DELETE_FOREVER,
        bgcolor=ft.colors.AMBER,
        mouse_cursor=ft.MouseCursor.CLICK,
        foreground_color= ft.colors.BLACK,
        on_click=clear
    )

    return  ft.Container(
        expand=True,
        # bgcolor=ft.colors.BLACK,
        padding=ft.padding.all(30),
        content=ft.Column(
            scroll = ft.ScrollMode.HIDDEN,
            controls=[
                header,
                formulario_novo,
                btn_novo,
                formulario_reforco,
                btn_reforco,
                resultado,
                floating_action_button,
            ]
        )
    )

    page.add(layout)


# ft.app(target=main)
