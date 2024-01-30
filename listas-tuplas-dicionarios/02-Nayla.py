# Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias_alunos = []

for i in range(5):
    print(f'Aluno {i + 1}: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))

    media= (nota1 + nota2 + nota3 + nota4) /4


    medias_alunos.append(media)
    
    alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)
    
    print(f'Quantidade de alunos que tiveram média maior ou igual a 7.0: {alunos_aprovados} ')