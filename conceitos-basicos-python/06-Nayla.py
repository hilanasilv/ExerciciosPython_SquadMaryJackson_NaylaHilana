'''Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

distancia = float(input('Digite a distância em km: '))
velocidadeAviao = 600
velocidadeCarro = 100
velocidadeOnibus = 80

tempoAviao = distancia / velocidadeAviao
tempoCarro = distancia / velocidadeCarro
tempoOnibus = distancia / velocidadeOnibus

print(f'O tempo da viagem de avião é {tempoAviao:.1f} horas, de carro é {tempoCarro:.1f} horas e de ônibus é {tempoOnibus:.1f} horas')