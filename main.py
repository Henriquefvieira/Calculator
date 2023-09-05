# Alterar nomes das variaveis para ingles
# Não utilizar numeros nas nomeações das variaveis (pesquisar sobre operadores e operandos na calculadora)
# Tratamento para caso de inserção de letras nas variaveis num1 e num2
# PEP8

while True:
    operacao = input('Qual operação (+,-,*,/) você quer fazer? Ou \'q\' para sair ')
    if operacao == 'q':
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))

    if operacao == '+':
        total = num1 + num2
        print(total)
    elif operacao == '-':
        total = num1 - num2
        print(total)
    elif operacao == '*':
        total = num1 * num2
        print(total)
    elif operacao == '/':
        total = num1 / num2
        print(total)
    else:
        print('Operação é invalida')
