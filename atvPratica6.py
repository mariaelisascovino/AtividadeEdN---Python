# 1 - Crie um programa que gera uma senha aleatória com o módulo
# random, utilizando caracteres especiais, possibilitando o
# usuário a informar a quantidade de caracteres dessa senha
# aleatória.

import random
import string

def gerar_senha(tamanho: int) -> str:
    # Conjunto de caracteres: letras maiúsculas, minúsculas, dígitos e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


# Interação com o usuário:
print("Questão 1 - Gerador de Senha Aleatória")
qtd = int(input("Digite a quantidade de caracteres da senha: "))
print(f"Sua senha gerada é: {gerar_senha(qtd)}\n")


# 2 - Crie um programa que gera um perfil de usuário aleatório usando a
# API 'Random User Generator'. O programa deve exibir o nome, email e
# país do usuário gerado.

import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]
        return nome, email, pais
    else:
        return None


# Interação com o usuário:
print("Questão 2 - Gerador de Perfil Aleatório")
input("Pressione ENTER para gerar um usuário aleatório...")
resultado = gerar_usuario()

if resultado:
    nome, email, pais = resultado
    print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}\n")
else:
    print("Erro ao consultar a API.\n")


# 3 - Desenvolva um programa que consulte informações de
# endereço a partir de um CEP fornecido pelo usuário, utilizando
# a API ViaCEP. O programa deve exibir o logradouro, bairro,
# cidade e estado correspondentes ao CEP consultado.

import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            logradouro = dados.get("logradouro", "Não informado")
            bairro = dados.get("bairro", "Não informado")
            cidade = dados.get("localidade", "Não informado")
            estado = dados.get("uf", "Não informado")
            return logradouro, bairro, cidade, estado
    return None


# Interação com o usuário:
print("Questão 3 - Consulta de Endereço por CEP")
cep = input("Digite o CEP (somente números): ")
resultado = consultar_cep(cep)

if resultado:
    logradouro, bairro, cidade, estado = resultado
    print(f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}\n")
else:
    print("CEP inválido ou não encontrado.\n")


# 4 - Crie um programa que consulte a cotação atual de uma moeda
# estrangeira em relação ao Real Brasileiro (BRL). O usuário
# deve informar o código da moeda desejada (ex: USD, EUR, GBP), 
# e o programa deve exibir o valor atual, máximo e mínimo
# da cotação, além da data e hora da última atualização. Utilize
# a API da AwesomeAPI para obter os dados de cotação.

import requests

def consultar_cotacao(moeda: str):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            return {
                "moeda": info["code"],
                "valor_atual": float(info["bid"]),
                "maximo": float(info["high"]),
                "minimo": float(info["low"]),
                "data_hora": info["create_date"]
            }
    return None


# Interação com o usuário:
print("Questão 4 - Cotação de Moeda")
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
resultado = consultar_cotacao(moeda)

if resultado:
    print(f"Moeda: {resultado['moeda']}")
    print(f"Valor Atual: R$ {resultado['valor_atual']:.2f}")
    print(f"Máximo: R$ {resultado['maximo']:.2f}")
    print(f"Mínimo: R$ {resultado['minimo']:.2f}")
    print(f"Última atualização: {resultado['data_hora']}\n")
else:
    print("Erro ao consultar a cotação.\n")
