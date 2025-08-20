# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
#define a função calcular_gorjeta, que tem o parâmetro valor_conta e porcentagem_gorjeta em float e resultado também em float
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100) # calculando valor da gorjeta através da indicação da porcentagem da gorjeta e valor da conta
    return gorjeta


# Exemplo:
conta = 200.0
porcentagem = 10
print("Questão 1")
print(f"Gorjeta: R$ {calcular_gorjeta(conta, porcentagem):.2f}\n")

# Interação com usuário:
valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (%): "))

resultado = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f"Gorjeta calculada: R$ {resultado:.2f}\n")


# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, ignorando espaços e pontuação). 
# Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.


import string

def verificar_palindromo(texto: str) -> str:
    #define uma função verificar_palindromo com parametro texto no formato string e resultado também string

    # Coloca tudo em minúsculas para padronizar
    texto = texto.lower()

    # Remove espaços e pontuações
    texto = ''.join(char for char in texto if char.isalnum())

    # Verifica se é igual de frente pra trás e de trás pra frente
    if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"


# Exemplo:
print("Questão 2")
print(verificar_palindromo("arara"))          # Sim
print(verificar_palindromo("Python\n"))         # Não

# Interação com o usuário:
frase = input("Digite uma palavra ou frase para verificar se é palíndromo: ")
resultado = verificar_palindromo(frase)
print(f"É palíndromo? {resultado}\n")


# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

def calcular_preco_com_desconto(preco: float, desconto: float) -> float:
  #define uma função calcular_preco_com_desconto com parâmetros preco e desconto em float e resposta em float

    # Calcula o valor do desconto
    valor_desconto = preco * (desconto / 100)

    # Calcula o preço final
    preco_final = preco - valor_desconto

    # Arredonda para 2 casas decimais
    return round(preco_final, 2)


#Interação com o usuário:
print("Questão 3")
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

preco_final = calcular_preco_com_desconto(preco, desconto)

print(f"Preço final com desconto: R$ {preco_final:.2f}\n")


# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime

def calcular_dias_vivo(data_nascimento: str) -> int:
 
    # Converte a string para objeto datetime
    nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    # Pega a data de hoje
    hoje = datetime.today()

    # Calcula a diferença em dias
    dias_vivo = (hoje - nascimento).days
    return dias_vivo


# Iteração com usuário:
print("Questão 4")
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias = calcular_dias_vivo(data)
print(f"Você está vivo há {dias} dias.\n")
