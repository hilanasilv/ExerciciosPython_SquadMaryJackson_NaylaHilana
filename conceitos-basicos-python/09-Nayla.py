#Questão 9 - Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

horas = int(input('Quantas horas de exercício físico você faz por semana? '))
totalCalorias = (horas * 60) * 5

print(f'O total de calorias queimadas por minuto é {totalCalorias}')