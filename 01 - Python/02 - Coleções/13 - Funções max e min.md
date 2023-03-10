# Funções max() e min()


As funções ``max()`` e ``min()`` permitem encontrar o maior e o menor valor em um iterável (uma sequência de elementos como uma lista, tupla, conjunto, etc.).


### Sintaxe Basica:


    # max(iterable, *iterables, key=None, default=None)


- ``iterable``: o iterável a ser analisado.
- ``iterables``: outros iteráveis opcionais que serão combinados com o iterable para encontrar o maior valor.
- ``key``: uma função opcional que especifica uma chave de ordenação para cada elemento antes de serem comparados.
- ``default``: um valor opcional que será retornado caso o iterável esteja vazio.


### Exemplo Básico


````python
numeros = [1, 5, 2, 8, 3, 9]
menor = min(numeros)
maior = max(numeros)
print(menor, 'e', maior)  # 1 e 9
````


### Utilizando o Parâmetro key


````python
# encontrando o animal cuja palavra tem mais caracteres
palavras = ['gato', 'elefante', 'cachorro', 'rato', 'leão']
palavra_mais_longa = max(palavras, key=len)
print(palavra_mais_longa)  # elefante


# encontrando a pessoa mais velha em uma lista de pessoas
pessoas = [
    {'nome': 'Alice', 'idade': 25},
    {'nome': 'Bob', 'idade': 30},
    {'nome': 'Charlie', 'idade': 20},
    {'nome': 'David', 'idade': 35},
]

pessoa_mais_velha = max(pessoas, key=lambda pessoa: pessoa['idade'])
print(pessoa_mais_velha)  # {'nome': 'David', 'idade': 35}
````


### Comparando Duas ou Mais Coleções (iterables)


````python
# Em ambos os casos utilizamos o operador '+' para unir as coleções:


# Exemplo 1 (numero mais alto)
lista1 = [1, 2, 3, 20, 4, 5]
lista2 = [6, 7, 8, 21, 9, 10]
maior_valor = max(lista1 + lista2)
print(maior_valor)  # 21


# Exemplo 2 (produto mais vendido)
dados_loja1 = [
    {'produto': 'camiseta', 'preco': 20, 'vendas': 100},
    {'produto': 'calca', 'preco': 40, 'vendas': 50},
    {'produto': 'meia', 'preco': 5, 'vendas': 200}
]
dados_loja2 = [
    {'produto': 'camiseta', 'preco': 15, 'vendas': 150},
    {'produto': 'calca', 'preco': 50, 'vendas': 30},
    {'produto': 'meia', 'preco': 3, 'vendas': 300}
]

produto_mais_vendido = max(dados_loja1 + dados_loja2,
                           key=lambda produto: produto['vendas'])
print(produto_mais_vendido)  # {'produto': 'meia', 'preco': 5, 'vendas': 300}
````