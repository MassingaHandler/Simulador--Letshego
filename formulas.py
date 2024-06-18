import os

def financiamento_maximo(e, salario: float, desconto: float, prazo: int):
    
    if salario < 10000:
        salario_real = salario * 0.33
    
    elif salario >= 10000 and salario <= 30000:
        salario_real = salario * 0.60
    
    elif salario > 30000:
        salario_real = salario * 0.70
    
    taxa_juro = 0.345/12
    salario_liquido = salario_real - desconto
    
    capacidadeMaxima = salario_liquido * (1 - (1 + taxa_juro)**(-prazo))/taxa_juro
    
    return capacidadeMaxima

def capacidade_maxima(salario: float, desconto: float, prazo: int):
    
    if salario < 10000:
        salario_real = salario * 0.33
    
    elif salario >= 10000 and salario <= 30000:
        salario_real = salario * 0.60
    
    elif salario > 30000:
        salario_real = salario * 0.70
    
    taxa_juro = 0.345/12
    salario_liquido = salario_real - desconto
    
    capacidadeMaxima = salario_liquido * (1 - (1 + taxa_juro)**(-prazo))/taxa_juro
    
    if prazo <=12:
        seguro = capacidadeMaxima * 0.0045
    
    elif prazo > 12 and prazo <= 36:
        seguro = capacidadeMaxima * 0.0033
    
    elif prazo > 36:
        seguro = capacidadeMaxima * 0.0028
    
    
    valor_a_receber = capacidadeMaxima - seguro
    
    return salario_real, seguro, capacidadeMaxima, valor_a_receber

def prestacao_mensal(salario: float, desconto: float, prazo: int, financiamento: float):
    capacidade = capacidade_maxima(salario, desconto, prazo)[0]
    taxa_juro = 0.345/12
    
    if prazo <= 12:
        financiamento_maximo = financiamento / (1 - 0.0045)
        seguro = financiamento_maximo * 0.0045
    
    elif prazo > 12 and prazo <= 36:
        financiamento_maximo = financiamento / (1 - 0.0033)
        seguro = financiamento_maximo * 0.0033
    
    elif prazo > 36:
        financiamento_maximo = financiamento / (1 - 0.0028)
        seguro = financiamento_maximo * 0.0028
    
    prestacao = (financiamento_maximo * taxa_juro)/(1 - (1 + taxa_juro) ** (-prazo))
    
    if capacidade < financiamento_maximo:
        
        return prestacao, capacidade, financiamento_maximo, 'Sem Capacidade'
    
    else:
        valor_a_receber = financiamento_maximo - seguro
        
        return prestacao, seguro, capacidade, financiamento_maximo, valor_a_receber, "Com Capacidade"