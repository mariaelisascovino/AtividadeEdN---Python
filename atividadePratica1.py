
##1- Programa de Saudação
##* Crie um programa que imprima a mensagem "Olá, mundo!" na tela.

print("Olá, mundo!\n")

##2- Calculadora de Soma
##* Desenvolva um programa que soma dois números. Use as variáveis numero1 = 12 e numero2 = 14. O programa deve calcular a soma e exibir o resultado.

#Declarando variáveis
numero1= int(12)
numero2= int(16)

soma= numero1 + numero2

print(f"O resultado da soma é: {soma}\n")

##3- Calculadora de Volume
#* Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

#* Comprimento: 12 cm
#* Largura: 14 cm
#* Altura: 20 cm
#O programa deve calcular o volume e exibir o resultado em cm³.

c= int(12)
l= int(14)
a= int(20)

V= c * l * a

print(f"o Volume é {V} cm³\n")

##4- Calculadora de Preço Total
##* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

#* Nome do produto: "Cadeira Infantil"
#* Preço unitário: R$ 12.40
#* Quantidade: 3
#O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

nomeProduto = str("Cadeira Infantil")
precoProduto = float(12.40)
qtdProduto= int(3)

precoTotal= qtdProduto*precoProduto

print("----- Detalhes da Compra -----")
print(f"Produto: {nomeProduto}")
print(f"Preço unitário: R$ {precoProduto:.2f}")
print(f"Quantidade: {qtdProduto}")
print("-----------------------------")
print(f"Preço total: R$ {precoTotal:.2f}")