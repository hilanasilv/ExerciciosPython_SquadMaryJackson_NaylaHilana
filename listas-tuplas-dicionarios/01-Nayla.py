''' Questão 1 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"". Caso contrário, ele será classificado como ""Inocente"".'''

pergunta1 = str(input('Telefonou para a vítima? Responda S para sim ou N para não: ')).lower()
pergunta2 = str(input('Esteve no local do crime? Responda S para sim ou N para não: ')).lower()
pergunta3 = str(input('Mora perto da vítima? Responda S para sim ou N para não: ')).lower()
pergunta4 = str(input('Devia para a vítima? Responda S para sim ou N para não: ')).lower()
pergunta5 = str(input('Já trabalhou com a vítima? Responda S para sim ou N para não: ')).lower()

countSim = [] #lista para respostas positivas.

#função para verificar as respostas.
def checkResp (perguntas):
   if perguntas == 's':
      countSim.append('s')

#função para verificar as sentenças.
def sentencaCrime():
   if len(countSim) == 2:
      print('Suspeita')
   elif len(countSim) == 3 or len(countSim) == 4:
      print('Cúmplice')
   elif len(countSim) == 5:
      print('Assassino')
   else:
      print('Inocente')

#impressão das respostas e da sentença.
checkResp(pergunta1)
checkResp(pergunta2)
checkResp(pergunta3)
checkResp(pergunta4)
checkResp(pergunta5)
sentencaCrime()

