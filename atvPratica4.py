# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def calculadora():
    print(" Calculadora Simples ")
    print("Operações: +  -  *  /")

    # Entrada dos valores
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    # Lógica das operações
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero.")
            return
    else:
        print("Operador inválido.")
        return

    print(f"Resultado: {num1} {operador} {num2} = {resultado}")

calculadora()

# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def calcular_media_turma():
    print(" Registro de Notas ")

    total_alunos = int(input("Quantos alunos na turma? "))
    soma_notas = 0

    for i in range(1, total_alunos + 1):
        nota = float(input(f"Digite a nota do aluno {i}: "))
        soma_notas += nota

    media = soma_notas / total_alunos
    print(f"\nMédia da turma: {media:.2f}")

calcular_media_turma()

# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.

def verificar_senha():
    senha = input("Digite a senha: ")

    # mínimo de 8 caracteres
    tem_tamanho_minimo = len(senha) >= 8

    # contém pelo menos um número
    tem_numero = any(char.isdigit() for char in senha)

    if tem_tamanho_minimo and tem_numero:
        print("✅ Senha válida.")
    else:
        print("Senha inválida. Requisitos:")
        if not tem_tamanho_minimo:
            print("- Deve ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("- Deve conter pelo menos um número.")

verificar_senha()

# 4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares 
# e contabilizando quantos de cada tipo foram inseridos.

def analisar_numeros():
    qtd_pares = 0
    qtd_impares = 0

    print("Digite os números. Digite 'sair' para encerrar.\n")

    while True:
        entrada = input("Número: ")

        if entrada.lower() == "sair":
            break

        if not entrada.isdigit():
            print("Entrada inválida. Digite apenas números ou 'sair'.")
            continue

        numero = int(entrada)

        if numero % 2 == 0:
            qtd_pares += 1
            print(f"{numero} é PAR.")
        else:
            qtd_impares += 1
            print(f"{numero} é ÍMPAR.")

    print("\n📊 Resultado:")
    print(f"🔵 Pares: {qtd_pares}")
    print(f"🟣 Ímpares: {qtd_impares}")

analisar_numeros()
