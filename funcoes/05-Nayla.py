# 5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro. Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

def conta_vogais(string): 
    string = string.lower() 
    vogais = 'aeiou'
    total_vogais = 0 
    
    for i in vogais: 
        if i in string: 
            total_vogais += string.count(i) 
    return total_vogais 
 
frase_usuario = input('Digite uma frase: ')
total_vogais_frase = conta_vogais(frase_usuario)

print(f'O número total de vogais nessa frase é: {total_vogais_frase}')