import numpy as np # importar a biblioteca numpy para manipulação de arrays
import matplotlib.pyplot as plt # importar a biblioteca matplotlib para criação de gráficos
import funçôes as f # importar o módulo funcoes para utilizar a função de entrada de dados

print("Bem-vindo à análise financeira!"
"\nAqui você pode analisar seus dados financeiros de forma simples e eficiente."
"\nVocê pode analisar até 12 meses: ")

while True: # loop para garantir que o usuário insira um número válido de meses
    meses = int(input("Quantos meses de dados financeiros você deseja analisar? ")) # solicitar ao usuário o número de meses que deseja analisar
    if meses >= 1 and meses <= 12: # verificar se o número de meses é válido
        break
    else: ValueError("Número de meses inválido. Por favor, insira um número entre 1 e 12.") # lançar um erro se o número de meses for inválido

entradas = np.array([]) # criar um array vazio para armazenar as entradas
saidas = np.array([]) # criar um array vazio para armazenar as saídas
investimentos = np.array([]) # criar um array vazio para armazenar os investimentos
reservas = np.array([]) # criar um array vazio para armazenar as reservas

print("Os dados financeiros coletados serão: entrada, saída, investimento e reserva. Caso não tenha todos os dados, insira 0 para os valores ausentes.") # informar ao usuário quais dados serão coletados

entradas, saidas, investimentos, reservas = f.entrada(meses, entradas, saidas, investimentos, reservas) # chamar a função de entrada para coletar os dados financeiros do usuário

fechamento = entradas - saidas # calcular o fechamento financeiro subtraindo as saídas das entradas
saldo = fechamento + investimentos + reservas # calcular o saldo financeiro somando o fechamento, os investimentos e as reservas

plt.plot(saldo, marker='o') # criar um gráfico de linha para o saldo financeiro, com marcadores nos pontos de dados
plt.title('Análise Financeira') # adicionar um título ao gráfico
plt.xlabel('Meses') # adicionar um rótulo ao eixo x
plt.ylabel('Saldo Financeiro') # adicionar um rótulo ao eixo y
plt.show() # exibir o gráfico