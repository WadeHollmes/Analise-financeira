import numpy as np # importar a biblioteca numpy para manipulação de arrays
import matplotlib.pyplot as plt # importar a biblioteca matplotlib para criação de gráficos


def entrada(meses, entradas, saidas, investimentos, reservas):  
    for i in range(meses): # loop para coletar os dados financeiros do usuário
        entrada = float(input(f"Digite o valor da entrada para o mês {i+1}: ")) # solicitar a entrada para o mês atual
        saida = float(input(f"Digite o valor da saída para o mês {i+1}: ")) # solicitar a saída para o mês atual
        investimento = float(input(f"Digite o valor total de investimento ao final do mês {i+1}: ")) # solicitar o investimento para o mês atual
        reserva = float(input(f"Digite o valor total de reserva ao final do mês {i+1}: ")) # solicitar a reserva para o mês atual
        entradas = np.append(entradas, entrada) # adicionar a entrada ao array de entradas
        saidas = np.append(saidas, saida) # adicionar a saída ao array de saídas
        investimentos = np.append(investimentos, investimento) # adicionar o investimento ao array de investimentos
        reservas = np.append(reservas, reserva) # adicionar a reserva ao array de reservas
        print(f"{i+1}º mês registrado com sucesso!") # informar ao usuário que o mês foi registrado com sucesso
    return entradas, saidas, investimentos, reservas # retornar os arrays atualizados com os dados financeiros coletados do usuário