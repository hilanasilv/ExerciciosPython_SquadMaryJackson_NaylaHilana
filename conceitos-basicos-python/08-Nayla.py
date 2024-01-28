#Questão 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input('Quanto você ganha por hora? '))
horaTrabalho = float(input('Quantas horas você trabalha por mês? '))

totalSalario = ganhoHora * horaTrabalho

print(f'O total do seu salário por mês é de {totalSalario:.2f} reais')