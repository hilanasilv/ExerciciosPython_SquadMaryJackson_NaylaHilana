#Questão 1 - Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão.

numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2

print(f'A soma dos números digitados é {soma}. A subtração dos números digitados é {subtracao}. A multiplicação dos números digitados é {multiplicacao}. A divisão dos números digitados é {divisao}. E a divisão inteira dos números digitados é {divisao_inteira}')
