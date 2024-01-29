# Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.

login_sistema = 'admin'
senha_sistema = 'admin123'

login = input('Digite o login: ')
senha = input('Digite a senha: ')

if login == login_sistema and senha ==senha_sistema:
    print('Acesso permitido. ')
else:
    print('Login e senha inválidos')

