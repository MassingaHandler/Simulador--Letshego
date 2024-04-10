import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#fdfdfd"
    page.padding = ft.padding.all(30)
    page.scroll = ft.ScrollMode.HIDDEN

    header = ft.Container(
        bgcolor= '#312f83',
        height=80,
        border_radius=ft.border_radius.only(top_left=15, top_right=15),
        padding=ft.padding.only(left=20, right=20),
        content=ft.Row(
            controls=[
                ft.Text(
                    value='Banco Letshego',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=15,
                ),

                ft.Row(
                    controls=[
                        ft.Text(
                            value='Patricio',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=15,
                        ),
                        ft.Icon(
                            name=ft.icons.PERSON,
                            color=ft.colors.WHITE,
                        ),
                    ]
                )

            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),

    )
    ft.Divider(height=6, color=ft.colors.BLACK),

    formulario_novo = ft.Container(
        padding=ft.padding.only(top=30),
        content=ft.ResponsiveRow(
            run_spacing=30,
            controls=[
                ft.Text(
                    value='Dados do cliente',
                    size=20,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.TextField(
                    col=6,
                    label='Nome completo ...',
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                ),
                ft.TextField(
                    col=6,
                    label='Contacto ...',
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                ),

                ft.Dropdown(
                    col=12,
                    label='Selecione a entidade',
                    options=[
                        ft.dropdown.Option(key=1, text='Marinha de Guerra'),
                        ft.dropdown.Option(text='Exercito'),
                        ft.dropdown.Option(text='MINT'),
                        ft.dropdown.Option(text='Reservistas'),
                        ft.dropdown.Option(text='Interior'),
                        ft.dropdown.Option(text='Pensionista'),
                        ft.dropdown.Option(text='Forcas areas'),
                        ft.dropdown.Option(text='ISDEF'),
                    ],
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                ),

                # ft.Text(
                #     value='Credito novo',
                #     size=20,
                #     color=ft.colors.BLACK,
                #     weight=ft.FontWeight.BOLD,
                # ),
                # salario_novo := ft.TextField(
                #     col=6,
                #     label='Salario do Bruto...',
                #     label_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                #     text_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                # ),
                # descontos_novo := ft.TextField(
                #     col=6,
                #     label='Todos os descontos...',
                #     label_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                #     text_style=ft.TextStyle(
                #         weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                # ),
            ],
        )
    )
    ft.Divider(height=6, color=ft.colors.BLACK),

    # Calcular novo credito

    # def calcular_novo(e):
    #     import math

    #     salario_liquido = salario_novo
    #     desconto_cal = descontos_novo
        
    #     salario_real = salario_liquido / 2
    #     salario_real2 = salario_real - desconto_cal





    # btn_novo = ft.Row(
    #     alignment=ft.MainAxisAlignment.START,
    #     controls=[
    #         ft.ElevatedButton(
    #             text='Calcular',
    #             bgcolor='#312f83',
    #             color=ft.colors.WHITE,
    #             on_click=calcular_novo,
    #         )
    #     ]
    # )

    formulario_reforco = ft.Container(
        padding=ft.padding.only(top=30),
        content=ft.ResponsiveRow(
            run_spacing=30,
            controls=[
                ft.Text(
                    value='Credito novo ou Reforco',
                    size=20,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                ),
                salario_bruto := ft.TextField(
                    col=6,
                    label='Salario Bruto',
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                ),
                vl_dividas_descontos := ft.TextField(
                    col=6,
                    label='Valor total de todas as dividas e descontos...',
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                ),
                vl_desejado := ft.TextField(
                    col=6,
                    label='Quanto e que o cliente gostaria de ter....',
                    label_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                ),
                tempo_pagamento := ft.TextField(
                    col=6,
                    label='Em quantos anos gostaria de pagar....',
                    label_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.colors.GREY_800),
                    input_filter=ft.NumbersOnlyInputFilter()
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
        juros = 1.033**meses

        prestacao_mensal = (float(valor_desejado) * float(juros) * float(0.033)) / (float(juros) - 1)

        
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
                            content=ft.Text(value = f'R$ {prestacao_mensal:.2f}')
                        ),
                        ft.DataCell(
                            content=ft.Text(value = valor_desejado),
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
                bgcolor='#312f83',
                color=ft.colors.WHITE,
                on_click=calcular_reforco,
            )
        ]
    )

    def toggle_select(e):
        e.control.selected = not e.control.selected
        print(f'Selecionando a linha de indice{e.control.data}')
        e.control.update()

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
                tabela_result := ft.DataTable(
                    columns=[
                        ft.DataColumn(label=ft.Text("Meses"), numeric=True),
                        ft.DataColumn(label=ft.Text(
                            "Prestacao Mensal"), numeric=True),
                        ft.DataColumn(label=ft.Text(
                            "Volor ToTal do emprestimo"), numeric=True),
                    ],
                    rows=[
                        # ft.DataRow(
                        #    cells=[
                        #       ft.DataCell(
                        #          content=ft.Text("1"),
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("2000MT")
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("50.000,00MT"),
                        #       ),
                        #    ],
                        #    selected = False,
                        #    on_select_changed= toggle_select,
                        #    data= 0,
                        # ),
                        # ft.DataRow(
                        #    cells=[
                        #       ft.DataCell(
                        #          content=ft.Text("2"),
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("2000MT")
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("50.000,00MT"),
                        #       ),
                        #    ],
                        #    selected = False,
                        #    on_select_changed= toggle_select,
                        #    data= 0,
                        # ),
                        # ft.DataRow(
                        #    cells=[
                        #       ft.DataCell(
                        #          content=ft.Text("3"),
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("2000MT")
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("50.000,00MT"),
                        #       ),
                        #    ],
                        #    selected = False,
                        #    on_select_changed= toggle_select,
                        #    data= 0,
                        # ),
                        # ft.DataRow(
                        #    cells=[
                        #       ft.DataCell(
                        #          content=ft.Text("4"),
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("2000MT")
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("50.000,00MT"),
                        #       ),
                        #    ],
                        #    selected = False,
                        #    on_select_changed= toggle_select,
                        #    data= 0,
                        # ),
                        # ft.DataRow(
                        #    cells=[
                        #       ft.DataCell(
                        #          content=ft.Text("5"),
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("2000MT")
                        #       ),
                        #       ft.DataCell(
                        #          content=ft.Text("50.000,00MT"),
                        #       ),
                        #    ],
                        #    selected = False,
                        #    on_select_changed= toggle_select,
                        #    data= 0,
                        # )
                    ],
                    show_checkbox_column=False,
                    border_radius=ft.border_radius.only(
                        bottom_left=15, bottom_right=15),
                    border=ft.border.all(color=ft.colors.BLACK),
                    bgcolor=ft.colors.GREY_300,
                    data_text_style=ft.TextStyle(
                        size=15,
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.BOLD,
                    ),
                    heading_row_color='#312f83',
                    heading_text_style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD,
                        size=15,
                    ),
                    vertical_lines=ft.BorderSide(
                        width=0.50, color=ft.colors.BLACK),
                )
            ]
        )
    )

    layout = ft.Container(
        expand=True,
        # bgcolor=ft.colors.GREY_300,
        # padding=ft.padding.all(20),
        content=ft.Column(
            controls=[
                header,
                formulario_novo,
                # btn_novo,
                formulario_reforco,
                btn_reforco,
                resultado,
            ]
        )
    )

    page.add(layout)


ft.app(target=main)
