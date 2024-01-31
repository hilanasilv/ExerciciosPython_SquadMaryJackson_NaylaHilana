'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''

tabela_conversao = {
    'Dólar Americano': 4.91,
    'Peso Argentino':  0.02,
    'Dólar Australiano':  3.18,
    'Dólar Canadense':  3.64,
    'Franco Suiço':  0.42,
    'Euro':  5.36,
    'Libra esterlina':  6.21
}

dinheiro_na_carteira = float(input('Digite quanto dinheiro em R$ você tem na carteira: '))

print('Com R$ {:.2f} na carteira, essa é a quantidade que você poderia comprar de cada moeda estrangeira: '.format(dinheiro_na_carteira))
for moeda, taxa in tabela_conversao.items():
    quantidade = dinheiro_na_carteira / taxa
    print(f'{moeda}: {quantidade:.2f}')