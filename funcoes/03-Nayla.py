# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Plus: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print('Escolha o que deseja converter - 1. Celsius para Fahrenheit ou 2. Fahrenheit para Celsius: ')
    opcao = input('Digite 1 ou 2: ')
    
    try:
        temperatura = float(input('Digite a temperatura: '))
        
        if opcao == '1':
            conversao = celsius_para_fahrenheit(temperatura)
            print(f'{temperatura} graus Celsius é igual a {conversao:.2f} graus Fahrenheit.')
        elif opcao == '2':
            conversao = fahrenheit_para_celsius(temperatura)
            print(f'{temperatura} graus Fahrenheit é igual a {conversao:.2f} graus Celsius. ')
        else: 
            print('Opção inválida. Escolha 1 ou 2: ')
    except ValueError:
        print('O número digitado não é válido. Tente novamente. ')

if __name__ == '__main__':
    main()