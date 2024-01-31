# 3. Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.

carrinho_de_compras = {}
carrinho_de_compras ['produto1'] = 2
carrinho_de_compras ['produto2'] = 4
carrinho_de_compras ['produto3'] = 3
carrinho_de_compras ['produto4'] = 1
carrinho_de_compras ['produto5'] = 3

precos = {
    'produto1' : 4.70,
    'produto2' : 2.50,
    'produto3' : 8.0,
    'produto4' : 3.70,
    'produto5' : 2.25
}

total_carrinho = sum(qnt * precos[produto] for produto, qnt in carrinho_de_compras.items())

print('Quantidade de itens do carrinho de compras:')

for produto, qnt in carrinho_de_compras.items():
    print(f'{produto}: {qnt} unidades ')
    
print(f'Total das compras: R$ {total_carrinho:.2f}')