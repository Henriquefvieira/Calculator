def calculator(operation, primary_value, secondary_value):
    if operation =='+':
        return primary_value + secondary_value
    elif operation =='-':
        return primary_value - secondary_value
    elif operation =='*':
        return primary_value * secondary_value
    elif operation =='/':
        if secondary_value != 0:
            return primary_value / secondary_value
        else:
            return "Divisão por zero não é permitida"

    else:
        return "Operação inválida"

while True:
    operation = input('Qual operação (+,-,*,/,%,raiz) você quer fazer ou \'q\' para sair ')
    if operation == 'q':
        break
    elif operation in ('+', '-', '*', '/'):
        try:
            primary_value = float(input('Digite o primeiro número: '))
            secondary_value = float(input('Digite o segundo número: '))
        except ValueError:
            print('Por favor, insira apenas números válidos.')
            continue
        result = calculator(operation, primary_value, secondary_value)
        print (f'Resultado: {result}')
    elif operation == 'raiz':
        import math
        num = float(input('Qual número desaja saber a raiz quadrada?'))
        raiz = math.sqrt(num)
        print(f'A raiz quadrada de {num} é {raiz}')
    elif operation =='%':
        value = float(input('Qual valor deseja saber a porcentagem:'))
        porcent = float(input('Quantos porcento do valor deseja saber: '))/100
        value_finish = porcent * value
        print(f'{porcent} de {value} é: {value_finish}')
    else:
        print('Por favor, insira apenas operações válidas')
