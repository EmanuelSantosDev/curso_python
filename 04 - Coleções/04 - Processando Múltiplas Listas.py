# Processando Múltiplas Listas - zip()


# Iterando sobre duas listas simultaneamente com zip()
a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5, 6]
for a, b in zip(a_lista, b_lista):
    print(a, end=' ')
    print(b, end=' ')
    # A 1 B 2 C 3 D 4 E 5


# Lista com Quantidade de Itens Diferentes 
produtos4 = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos4 = [250, 150, 220]
for a, b in zip(produtos4, precos4):
    print(f'Salvando produto {a} valor R$ {b}')
'''
Irá 'ignorar' os dois últimos items da lista 'produtos4':

Salvando produto Produto 1 valor R$ 250
Salvando produto Produto 2 valor R$ 150
Salvando produto Produto 3 valor R$ 220
'''


# Lista com Quantidade de Itens Diferentes (utilizando zip_longest)
from itertools import zip_longest
titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descrição 1', 'Descrição 2', 'Descrição 3']
for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo} com a descrição: {descricao} ')
'''
Encontramos o Titulo 1 com a descrição: Descrição 1
Encontramos o Titulo 2 com a descrição: Descrição 2
Encontramos o Titulo 3 com a descrição: Descrição 3
Encontramos o Titulo 4 com a descrição: None
'''