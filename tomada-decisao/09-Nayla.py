# 9. O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar o valor zero. Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

count_pares = 0
count_impares = 0

while True:
    try:
        numero = int(input('Digite um número e caso queira encerrar digite 0: '))
        
        if numero == 0:
            break
        if numero > 0:
            if numero %2 == 0:
                count_pares += 1
            else:
                count_impares += 1
        else:
            print('Digite apenas números inteiros positivos: ')
    except ValueError:
        print('Você deve digitar um número inteiro válido: ')
        
print(f'A quantidade de números pares inseridos é: ', count_pares)
print(f'A quantidade de números ímpares inseridos é: ', count_impares)