# AtividadeEdN - Exercícios de Introdução a Programação em Python

**Objetivo didático:** Desenvolver habilidades básicas em Python, incluindo manipulação de dados numéricos, formatação de saída e implementação de cálculos matemáticos simples, ideais para iniciantes na linguagem. 

**📋 Exercícios Propostos**
-----------------------------------------------------------
### 📋 Atividade Prática 1  

#### 1️⃣ **Programa de Saudação**  
Imprime a mensagem "Olá, mundo!" na tela.  

**Conceitos trabalhados:** Função básica de saída (`print()`), sintaxe fundamental do Python.  

#### 2️⃣ **Calculadora de Soma**  
Realiza a soma de dois números pré-definidos (12 e 14).  

**Conceitos trabalhados:** Declaração de variáveis, operador aritmético de adição (`+`).  

#### 3️⃣ **Calculadora de Volume**  
Calcula o volume de uma caixa retangular com dimensões 12cm × 14cm × 20cm.  

**Conceitos trabalhados:** Variáveis numéricas, operação de multiplicação, formatação de valores decimais.  

#### 4️⃣ **Calculadora de Preço Total**  
Calcula o valor total da compra de 3 unidades de "Cadeira Infantil" a R$ 12.40 cada.  

**Conceitos trabalhados:** Tipos de variáveis (string, float, int), formatação monetária (`:.2f`), operações com valores decimais.  

--------------------------------------------------------------

**Atividade Prática 2**

#### 1️⃣ **Conversor de Moeda**  
Programa que converte um valor em reais para dólar ou euro, utilizando taxas de câmbio pré-definidas (R$ 5,20 para dólar e R$ 6,15 para euro). O resultado é exibido com duas casas decimais.

**Conceitos trabalhados:** Entrada de dados com `input()`, formatação de números decimais, estruturas condicionais simples (`if-elif-else`) e operações matemáticas básicas.  

#### 2️⃣ **Calculadora de Desconto**  
Calcula o desconto e o preço final de um produto ("Camiseta" a R$ 50,00 com 20% de desconto), mostrando detalhes como valor do desconto e preço final.  

**Conceitos trabalhados:** Cálculos percentuais, formatação de saída com `f-strings`, variáveis constantes e exibição organizada de múltiplos valores.  

#### 3️⃣ **Calculadora de Média Escolar**  
Calcula a média aritmética de três notas (7,5, 8,0 e 6,5) e exibe as notas individuais junto com a média final, arredondada para duas casas decimais.  

**Conceitos trabalhados:** Operações com listas implícitas (soma de valores), cálculo de média aritmética, formatação de números decimais e organização de saída de dados.  

#### 4️⃣ **Calculadora de Consumo de Combustível**  
Determina o consumo médio de um veículo (km/l) com base na distância percorrida (300 km) e no combustível gasto (25 litros), apresentando os dados da viagem e o resultado formatado. 

**Conceitos trabalhados:** Cálculo de razão (divisão simples), formatação de saída, variáveis descritivas e exibição de métricas de desempenho.  

---  
**Atividade Prática 3**

#### 1️⃣ **Classificador de Idade**  
Classifica a idade em categorias (Criança, Adolescente, Adulto ou Idoso) com validação de entrada. 

**Conceitos trabalhados:** Estruturas condicionais (`if-elif-else`), operadores de comparação e validação de input.  

#### 2️⃣ **Calculadora de IMC**  
Calcula o Índice de Massa Corporal e classifica o resultado, com tratamento para valores inválidos.  

**Conceitos trabalhados:** Operações matemáticas, formatação de saída (`f-strings`), condições aninhadas e checagem de inputs positivos.  

#### 3️⃣ **Conversor de Temperatura**  
Converte entre escalas termométricas (Celsius, Fahrenheit e Kelvin) com base na unidade de origem e destino.  

**Conceitos trabalhados:** Funções personalizadas, conversão de unidades, estruturas condicionais complexas e formatação de números decimais.


#### 4️⃣ **Verificador de Ano Bissexto**  
Determina se um ano é bissexto seguindo as regras do calendário gregoriano.  

**Conceitos trabalhados:** Operadores lógicos (`and`, `or`), resto de divisão (`%`) e condições compostas.  


---------------------------------------------------------------

**Atividade Prática 4**

#### 1️⃣ **Calculadora Simples**

Executa operações matemáticas básicas entre dois números informados pelo usuário: soma, subtração, multiplicação e divisão.
**Conceitos trabalhados:** Entrada de dados com `input()`, conversão de tipos (`float`), operadores aritméticos (`+`, `-`, `*`, `/`), condicionais `if/elif/else`, tratamento de erro de divisão por zero.


#### 2️⃣ **Registro de Notas e Cálculo da Média da Turma**

Solicita a quantidade de alunos, registra suas notas individualmente e calcula a média da turma.
**Conceitos trabalhados:** Estrutura de repetição `for`, declaração e soma de variáveis, média aritmética, formatação de saída com `:.2f`.


#### 3️⃣ **Verificador de Senha Segura**

Valida se uma senha atende aos critérios básicos de segurança: no mínimo 8 caracteres e pelo menos um número.
**Conceitos trabalhados:** Manipulação de strings, função `len()`, verificação de dígitos com `isdigit()`, função `any()`, estruturas condicionais compostas.


#### 4️⃣ **Analisador de Números Pares e Ímpares**

Recebe números do usuário até que digite `"sair"`. Cada número é classificado como **par** ou **ímpar**, e ao final exibe a contagem de cada tipo.
**Conceitos trabalhados:** Estrutura de repetição `while`, controle de fluxo com `break` e `continue`, verificação de paridade (`%`), uso de métodos de string (`lower()`, `isdigit()`).

---------------------------------------------------------------

# 📋 Atividade Prática 5

1️⃣ **Cálculo de Gorjeta em Restaurante**
Cria uma função que calcula a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta informada pelo usuário.
**Conceitos trabalhados:** Definição de funções (`def`), parâmetros com tipo (`float`), operadores aritméticos, retorno de valores, formatação de saída com `:.2f`, e interação com o usuário via `input()`.


2️⃣ **Verificador de Palíndromo**
Implementa uma função que verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente), desconsiderando espaços e pontuações. Retorna **“Sim”** se for palíndromo e **“Não”** caso contrário.
**Conceitos trabalhados:** Definição de funções (`def`), manipulação de strings (`lower()`, `isalnum()`), compreensão de listas para filtragem de caracteres, fatiamento de strings (`[::-1]`), condicionais `if/else`, e interação com o usuário via `input()`.


3️⃣ **Cálculo de Preço com Desconto**
Programa que calcula o preço final de um produto após aplicar um desconto percentual. Solicita o preço original e a porcentagem de desconto ao usuário e mostra o valor final já arredondado.
**Conceitos trabalhados:** Definição de funções (`def`), operadores aritméticos, arredondamento de valores (`round()`), formatação de saída com `:.2f`, e entrada de dados com `input()`.


4️⃣ **Cálculo de Dias de Vida**
Determina há quantos dias um indivíduo está vivo com base em sua data de nascimento e a data atual. O usuário informa a data no formato `dd/mm/aaaa`, e o programa retorna a quantidade de dias.
**Conceitos trabalhados:** Biblioteca `datetime`, manipulação e conversão de datas (`strptime`, `today`), cálculo de diferença entre datas, propriedades (`.days`), entrada de dados com `input()`, e formatação de saída.

---------------------------------------------------------------

# Readme Atividade Prática 6

1️⃣ **Gerador de Senha Aleatória**
Gera uma senha aleatória contendo letras maiúsculas, minúsculas, números e caracteres especiais. O usuário informa a quantidade de caracteres desejada.
**Conceitos trabalhados:**

* Módulo `random` para escolha aleatória de caracteres
* Módulo `string` para conjuntos de caracteres (letras, dígitos e símbolos)
* Estrutura de repetição com compreensão de listas
* Interação com o usuário via `input()`
* Funções em Python (`def`) e retorno de valores (`return`)


2️⃣ **Gerador de Perfil de Usuário Aleatório**
Consulta a API [Random User Generator](https://randomuser.me/) para gerar informações de um usuário fictício, exibindo nome completo, email e país.
**Conceitos trabalhados:**

* Requisições HTTP com o módulo `requests`
* Manipulação de respostas JSON (`resposta.json()`)
* Acesso a dados aninhados em dicionários
* Condicional para tratar erros de requisição (`status_code`)
* Funções em Python para encapsular lógica


3️⃣ **Consulta de Endereço por CEP**
Recebe um CEP do usuário e retorna o logradouro, bairro, cidade e estado correspondentes, usando a API [ViaCEP](https://viacep.com.br/).
**Conceitos trabalhados:**

* Requisições HTTP e manipulação de JSON
* Acesso seguro a chaves de dicionários com `get()`
* Validação de dados e tratamento de erros (CEP inválido ou não encontrado)
* Funções em Python para organizar código
* Interação com o usuário e exibição formatada de resultados


4️⃣ **Consulta de Cotação de Moeda**
Permite ao usuário informar o código de uma moeda estrangeira (ex: USD, EUR, GBP) e retorna o valor atual em reais, valor máximo, mínimo e a data/hora da última atualização, utilizando a API [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas).
**Conceitos trabalhados:**

* Requisições HTTP e parsing de JSON
* Conversão de strings para números (`float`)
* Manipulação de dicionários para acessar informações específicas
* Formatação de saída com casas decimais (`:.2f`)
* Funções em Python para encapsular lógica



