# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

idade = int(input("Indique sua idade: "))

if idade < 0:
    print("Insira um valor válido")
elif 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

peso = float(input("Insira seu peso (kg): "))
altura = float(input("Insira sua altura (m): "))

if peso <= 0 or altura <= 0:
    print("Erro: Peso e altura devem ser valores positivos.")
else:
    IMC = peso / (altura ** 2)
    print(f"IMC = {IMC:.2f}")  

    if IMC < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= IMC < 25:
        print("Peso normal")
    elif 25 <= IMC < 30:
        print("Sobrepeso")
    else: 
        print("Obeso")


# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

print("Conversor de temperatura/ C= Celsius; F= Fahrenheit e K= Kelvin")
temp = float(input("Digite a temperatura: "))
unidade_origem = input("Unidade de origem (Digite C, F ou K): ").upper()
unidade_destino = input("Unidade de destino (Digite C, F ou K): ").upper()

def c_para_f(c):
    return (c * 9/5) + 32

def f_para_c(f):
    return (f - 32) * 5/9

def c_para_k(c):
    return c + 273.15

def k_para_c(k):
    return k - 273.15

if unidade_origem == "C" and unidade_destino == "F":
    resultado = c_para_f(temp)
elif unidade_origem == "F" and unidade_destino == "C":
    resultado = f_para_c(temp)
elif unidade_origem == "C" and unidade_destino == "K":
    resultado = c_para_k(temp)
elif unidade_origem == "K" and unidade_destino == "C":
    resultado = k_para_c(temp)
elif unidade_origem == "F" and unidade_destino == "K":
    # Converte Fahrenheit → Celsius → Kelvin
    resultado = c_para_k(f_para_c(temp))
elif unidade_origem == "K" and unidade_destino == "F":
    # Converte Kelvin → Celsius → Fahrenheit
    resultado = c_para_f(k_para_c(temp))
elif unidade_origem == unidade_destino:
    resultado = temp  
else:
    print("Erro: Unidades inválidas ou conversão não suportada.")
    exit()

print(f"{temp} {unidade_origem} = {resultado:.2f} {unidade_destino}")


# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")