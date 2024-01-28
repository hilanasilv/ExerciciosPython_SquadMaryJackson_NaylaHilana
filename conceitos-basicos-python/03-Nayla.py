# Questão 3 - Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

quilometro = int(input('Digite uma quantidade em quilômetros: '))

metro = quilometro * 1000
centimetro = quilometro * 100000
milimetro = quilometro * 1000000

print(f'A quantidade em metros é {metro}, em centímetros é {centimetro} e em milímetros é {milimetro}.')