# 8. Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 and numero3:
    print(f'O maior número é {numero1}')
elif numero2 > numero3 and numero1:
    print(f'O maior número é {numero2}')
elif numero3 > numero1 and numero2:
    print(f'O maior número é {numero3}')