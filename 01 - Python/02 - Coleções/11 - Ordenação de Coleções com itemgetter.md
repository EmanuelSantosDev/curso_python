# Ordenação de Coleções com itemgetter


- Em listas simples podemos utilizar o método ``sort()``.
- Mas em um Dicionário, como fazer?
- ``itemgetter`` é uma função da biblioteca ``operator`` que permite obter um elemento específico de um objeto iterável (como uma lista, tupla ou dicionário) baseado em seu índice ou chave.
- É possivel ordenar de forma decrescente passando o parâmetro ``reverse=True``.`


````python
from operator import itemgetter


# Dicionário não ordenado alfabeticamente
pessoas = [
    {'nome': 'John', 'idade': 32, 'nivel_acesso': 2},
    {'nome': 'Carol', 'idade': 18, 'nivel_acesso': 3},
    {'nome': 'Thomas', 'idade': 45, 'nivel_acesso': 5},
    {'nome': 'Amanda', 'idade': 23, 'nivel_acesso': 1},
]


# Ordenando pela key 'nome'
pessoas.sort(key=itemgetter('nome'))
print(pessoas)
# {'nome': 'Amanda', 'idade': 23, 'nivel_acesso': 1},
# {'nome': 'Carol', 'idade': 18, 'nivel_acesso': 3},
# {'nome': 'John', 'idade': 32, 'nivel_acesso': 2},
# {'nome': 'Thomas', 'idade': 45, 'nivel_acesso': 5}


# ORDENAÇÃO MULTINIVEL: Ordenando pelas keys 'nome' + 'idade'
lista_cadastros = [
    {'nome': 'Luis', 'idade': 32},
    {'nome': 'César', 'idade': 24},
    {'nome': 'Beatriz', 'idade': 18},
    {'nome': 'Larissa', 'idade': 45},
    {'nome': 'Beatriz', 'idade': 22},
    {'nome': 'Beatriz', 'idade': 8}
]

lista_cadastros.sort(key=itemgetter('nome', 'idade'))

for n in lista_cadastros:
    print(n)
# {'nome': 'Beatriz', 'idade': 8}
# {'nome': 'Beatriz', 'idade': 18}
# {'nome': 'Beatriz', 'idade': 22}
# {'nome': 'César', 'idade': 24}
# {'nome': 'Larissa', 'idade': 45}
# {'nome': 'Luis', 'idade': 32}


# Ordenando Tuplas (ao invés da key utiliza-se o índice)
produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]
produtos.sort(key=itemgetter(1))
print(produtos)
# ('Microfone', 550),
# ('Celular', 750),
# ('Bicicleta', 1500)


# Ordenando em Ordem Decrescente
produtos.sort(key=itemgetter(1), reverse=True)
print(produtos)
# ('Bicicleta', 1500),
# ('Celular', 750),
# ('Microfone', 550)


# Ordenando uma Matriz de Dados
matriz = [[5, 10], [15, 21], [1, 5]]
matriz.sort(key=itemgetter(1))
print(matriz)
# [1, 5],
# [5, 10],
# [15, 21]
````