#1. Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'{numero1}')
else:
    print(f'{numero2}')
