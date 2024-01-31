# 5. Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno. equilátero: todos os lados com o mesmo valor isósceles: dois lados com o mesmo valor escaleno: todos os lados com medidas distintas.

lado1 = float(input('Informe o comprimento do lado 1 do triângulo: '))
lado2 = float(input('Informe o comprimento do lado 2 do triângulo: '))
lado3 = float(input('Informe o comprimento do lado 3 do triângulo: '))

if lado1 == lado2 == lado3:
    print('O triângulo é equilatero. ')
elif lado1 == lado2 != lado3 or lado1!= lado2 == lado3 or lado1 == lado3 !=lado2:
    print('O triângulo é isósceles. ')
elif lado1 != lado2 != lado3:
    print('O triângulo é escaleno. ')