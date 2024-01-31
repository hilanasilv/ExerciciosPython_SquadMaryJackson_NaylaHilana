# 4. Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.

contatos = {'Aline': '98845-9735', 'Débora': '99976-3422', 'Eliane': '99166-7371'}
busca_contato = input('Digite o nome do contato que deseja buscar: ')
telefone = contatos.get(busca_contato, 'Contato não existe')

print(f'{busca_contato} \n{telefone}')