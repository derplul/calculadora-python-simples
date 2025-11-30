# Função que realiza a adição de dois números
def adicao(x, y):
    return x + y

# Função que realiza a subtração de dois números
def subtracao(x, y):
    return x - y

# Função que realiza a multiplicação de dois números
def multiplicacao(x, y):
    return x * y

# Função que realiza a divisão de dois números
def divisao(x, y):
    if y == 0:  # Verifica se o denominador é zero para evitar erro
        return "Erro: Divisão por zero"
    return x / y

# Exibição do menu de opções
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Entrada da escolha do usuário
escolha = input("Digite o número da operação desejada (1/2/3/4): ")

# Entrada dos números para a operação
try:
    num1 = float(input("Digite o primeiro número: "))  # Converte a entrada para float
    num2 = float(input("Digite o segundo número: "))  # Converte a entrada para float
except ValueError:
    print("Erro: Por favor, insira um número válido.")
    exit()

# Verifica qual operação foi escolhida e executa a função correspondente
if escolha == '1':
    print(f"Resultado: {adicao(num1, num2)}")
elif escolha == '2':
    print(f"Resultado: {subtracao(num1, num2)}")
elif escolha == '3':
    print(f"Resultado: {multiplicacao(num1, num2)}")
elif escolha == '4':
    print(f"Resultado: {divisao(num1, num2)}")
else:
    print("Opção inválida. Por favor, escolha entre 1 e 4.")