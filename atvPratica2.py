# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

#Declarando variáveis
valor_real = float(input("Digite o valor para conversão em reais: "))
moeda = str(input("Digite dólar ou euro para conversão: "))

#Condicional:
if moeda == "dólar":
    dolar = valor_real / 5.20
    print(f"O valor em dólar é : {dolar:.2f}")
elif moeda == "euro":
    euro = valor_real / 6.15
    print(f"O valor em euro é : {euro:.2f}")
else:
    print("Digite um valor válido")


# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

# Dados do produto
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20  # 20%

# Cálculos
valor_desconto = (preco_original * percentual_desconto) / 100
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("\nCalculadora de Desconto ")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}% (R$ {valor_desconto:.2f})")
print(f"Preço final: R$ {preco_final:.2f}\n")


# 3- Calculadora de Média Escolar
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

# * Nota 1: 7.5
# * Nota 2: 8.0
# * Nota 3: 6.5
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.


# Notas do aluno (conforme enunciado)
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição dos resultados
print("\nMédia Escolar ")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}\n")
print(f"Média final: {media:.2f}\n")

# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo.

# Dados da viagem (conforme enunciado)
distancia = 300  # km
combustivel = 25  # litros

# Cálculo do consumo médio
consumo_medio = distancia / combustivel

# Exibição dos resultados
print("\nConsumo de Combustível ")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
