# Questão 7 - Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura x altura).

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

calculoIMC = peso / (altura * altura)

print(f'Seu IMC é de {calculoIMC:.1f}')