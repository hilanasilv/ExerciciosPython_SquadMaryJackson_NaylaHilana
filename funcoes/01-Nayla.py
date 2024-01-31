# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma (a, b, c):
    return a + b + c

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o primeiro número: '))
num3 = int(input('Digite o primeiro número: '))

calculo = soma(num1, num2, num3)
print(f'O resultado da soma é {calculo} ')