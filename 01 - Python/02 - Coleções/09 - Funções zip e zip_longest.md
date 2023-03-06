# Funções zip e zip_longest


- A função ``zip()`` recebe um ou mais iteráveis (como listas, tuplas ou strings) como argumentos e retorna um iterador de tuplas.
- A função ``zip_longest()`` é uma função da biblioteca ``itertools`` que é semelhante à função ``zip()``. No entanto, em vez de parar quando o menor iterável é esgotado, ela preenche os valores ausentes com um valor de preenchimento especificado (por padrão, ``None``) para que todos os iteráveis tenham o mesmo tamanho.


### Interadores de Comprimentos Iguais com zip()


````python
a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5, 6]

for a, b in zip(a_lista, b_lista):
    print(a, end=' ')
    print(b, end=' ')

# A 1 B 2 C 3 D 4 E 5
````


### Interadores de Comprimentos Variados com zip() 


````python
# Irá 'ignorar' os dois últimos items da lista 'produtos4':

produtos4 = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos4 = [250, 150, 220]

for a, b in zip(produtos4, precos4):
    print(f'Salvando produto {a} valor R$ {b}')

# Salvando produto Produto 1 valor R$ 250
# Salvando produto Produto 2 valor R$ 150
# Salvando produto Produto 3 valor R$ 220
````


### Interadores de Comprimentos Variados com zip_longest()


````python
from itertools import zip_longest

titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
descricoes = ['Descrição 1', 'Descrição 2', 'Descrição 3']

for titulo, descricao in zip_longest(titulos, descricoes, fillvalue="Este item não existe"):
    print(f'Encontramos o {titulo} com a descrição: {descricao} ')

# Encontramos o Titulo 1 com a descrição: Descrição 1
# Encontramos o Titulo 2 com a descrição: Descrição 2
# Encontramos o Titulo 3 com a descrição: Descrição 3
# Encontramos o Titulo 4 com a descrição: Este item não existe
````