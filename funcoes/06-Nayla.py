# Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra da palavra. O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas. Dica: Você precisará importar uma biblioteca para resolver esse exercício'''

def jogo_da_forca():
  print('ESSE É O JOGO DA FORCA')
  print('TEMA: ARTISTA')    


  import random as rd
  lista = ['SZA', 'SEVDALIZA', 'BEYONCÉ', 'MAHALIA']

  def palavra_aleatoria(lista):    
      tamanho = len(lista)
      sorteio = rd.randint(1,tamanho)    
      palavra_aleatoria = lista[sorteio] 
      return palavra_aleatoria
  
  def localizar(texto,palavra):
      posicoes = []
      for i in range(0,len(texto)):
          if texto[i] == palavra:
              posicoes.append(i)
      return posicoes


  palavra = palavra_aleatoria(lista)
  print(f'DICA: a palavra tem {len(palavra)} letras')


  chances = 0
  palavra_secreta = list('_' * len(palavra))
  while chances <= 6:
      letra_digitada = input('Digite somente uma letra: ').upper()    
      if letra_digitada in palavra:
          print(f'A palavra secreta tem a letra {letra_digitada}')                 
          posicao = localizar(palavra,letra_digitada)
          for i in posicao:    
              palavra_secreta[i] = letra_digitada            
          print(palavra_secreta)
          
          print(palavra_secreta)  
          opcao = input('Você já sabe qual é o nome da palavra? Digite S para Sim ou N para Não: ')        
          if opcao.upper() == 'S':
              resposta = input('Digite o nome da palavra: ')
              if resposta.upper() == palavra: 
                  print('Parabéns! Você acertou a palavra secreta.')
                  break
              else:
                  print(f'Você errou! A palavra correta era {palavra}')
                  break 
      else:
          print(f'A palavra secreta não tem a letra {letra_digitada}')
          print(palavra_secreta) 
              
      chances +=1
      if chances >= 6:
          print('Você perdeu porque atingiu o número máximo de tentativas') 
          print(f'A Palavra correta era {palavra}!')
          break


jogo_da_forca()