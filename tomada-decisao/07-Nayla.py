# 7. Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.

idade = int(input('Digite sua idade: '))

if idade < 12:
    print('O usuário é uma criança. ')
elif idade >= 12 and idade <= 18:
    print('O usuário é um adolescente. ')
elif idade > 18 and idade < 65:
    print('O usuário é um adulto. ')
elif idade >= 65:
    print('O usuário é um idoso. ')