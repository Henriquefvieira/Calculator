import math

def calculator(operation, primary_value, secondary_value):
    if operation =='+':
        return primary_value + secondary_value
    elif operation =='-':
        return primary_value - secondary_value
    elif operation =='*':
        return primary_value * secondary_value
    elif operation =='/':
        try:
            return primary_value / secondary_value
        except ZeroDivisionError:
            return '\033[31;1mDivisão por zero não é permitida\033[0;0m'
    elif operation == 'raiz':
        return math.sqrt(primary_value)
    else:
        return "\033[31;1mOperação inválida\033[0;0m"

while True:
    operation = input('Qual operação \033[34;1m(+,-,*,/,%,raiz)\033[0;0m você quer fazer ou \'q\' para sair: ')
    if operation == 'q':
        break
    elif operation in ('+', '-', '*', '/'):
        try:
            primary_value = float(input('Digite o primeiro número: '))
            secondary_value = float(input('Digite o segundo número: '))
        except ValueError:
            print('\033[31;1mPor favor, insira apenas números válidos.\033[0;0m')
            continue
        result = calculator(operation, primary_value, secondary_value)
        print(f'Resultado: {result}')
    elif operation == 'raiz':
        primary_value = float(input('Qual número desaja saber a raiz quadrada?'))
        result = calculator(operation, primary_value, None)
        print(f'A raiz quadrada de {primary_value} é {result}')
    elif operation =='%':
        primary_value = float(input('Qual valor deseja saber a porcentagem: '))
        secondary_value = float(input('Quantos porcento do valor deseja saber: '))/100
        value_finish = secondary_value * primary_value
        print(f'{secondary_value} de {primary_value} é: {value_finish}')
    else:
        print('\033[31;1mPor favor, insira apenas operações válidas\033[0;0m')
