import numpy as np # importar a biblioteca numpy para manipulação de arrays
import matplotlib.pyplot as plt # importar a biblioteca matplotlib para criação de gráficos

print("Bem-vindo à análise financeira!"
"\nAqui você pode analisar seus dados financeiros de forma simples e eficiente."
"\nVocê pode analisar até 12 meses: ")

while True: # loop para garantir que o usuário insira um número válido de meses
    meses = int(input("Quantos meses de dados financeiros você deseja analisar? "))
    if meses >= 1 and meses <= 12: # verificar se o número de meses é válido
        break
    else: ValueError("Número de meses inválido. Por favor, insira um número entre 1 e 12.") # lançar um erro se o número de meses for inválido

entradas = np.array([]) # criar um array vazio para armazenar as entradas
saidas = np.array([]) # criar um array vazio para armazenar as saídas
investimentos = np.array([]) # criar um array vazio para armazenar os investimentos
reservas = np.array([]) # criar um array vazio para armazenar as reservas

print("Os dados financeiros coletados serão: entrada, saída, investimento e reserva. Caso não tenha todos os dados, insira 0 para os valores ausentes.") # informar ao usuário quais dados serão coletados

for i in range(meses): # loop para coletar os dados financeiros do usuário
    entrada = float(input(f"Digite o valor da entrada para o mês {i+1}: ")) # solicitar a entrada para o mês atual
    saida = float(input(f"Digite o valor da saída para o mês {i+1}: ")) # solicitar a saída para o mês atual
    investimento = float(input(f"Digite o valor total de investimento ao final do mês {i+1}: ")) # solicitar o investimento para o mês atual
    reserva = float(input(f"Digite o valor total de reserva ao final do mês {i+1}: ")) # solicitar a reserva para o mês atual
    entradas = np.append(entradas, entrada) # adicionar a entrada ao array de entradas
    saidas = np.append(saidas, saida) # adicionar a saída ao array de saídas
    investimentos = np.append(investimentos, investimento) # adicionar o investimento ao array de investimentos
    reservas = np.append(reservas, reserva) # adicionar a reserva ao array de reservas

fechamento = entradas - saidas # calcular o fechamento financeiro subtraindo as saídas das entradas
saldo = fechamento + investimentos + reservas # calcular o saldo financeiro somando o fechamento, os investimentos e as reservas

plt.plot(saldo, marker='o') # criar um gráfico de linha para o saldo financeiro, com marcadores nos pontos de dados
plt.title('Análise Financeira') # adicionar um título ao gráfico
plt.xlabel('Meses') # adicionar um rótulo ao eixo x
plt.ylabel('Saldo Financeiro') # adicionar um rótulo ao eixo y
plt.show() # exibir o gráfico