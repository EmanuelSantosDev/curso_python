# ------------------------------------------------------------------------------------
# Ordenar Coleções Através de Propriedades
# ------------------------------------------------------------------------------------


'''
- em listas simples podemos utilizar o método sort()
- mas em um Dicionário, como fazer?
'''


# importando a biblioteca 'itemgetter'
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
'''
{'nome': 'Amanda', 'idade': 23, 'nivel_acesso': 1}, 
{'nome': 'Carol', 'idade': 18, 'nivel_acesso': 3}, 
{'nome': 'John', 'idade': 32, 'nivel_acesso': 2}, 
{'nome': 'Thomas', 'idade': 45, 'nivel_acesso': 5}
'''


# Ordenando pela key 'nivel_acesso'
pessoas.sort(key=itemgetter('nivel_acesso'))
print(pessoas)
'''
{'nome': 'Amanda', 'idade': 23, 'nivel_acesso': 1}, 
{'nome': 'John', 'idade': 32, 'nivel_acesso': 2}, 
{'nome': 'Carol', 'idade': 18, 'nivel_acesso': 3}, 
{'nome': 'Thomas', 'idade': 45, 'nivel_acesso': 5}
'''


# Ordenando Tuplas (ao invés da key utiliza-se o índice)
produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]
produtos.sort(key=itemgetter(1))
print(produtos)
'''
('Microfone', 550), 
('Celular', 750), 
('Bicicleta', 1500)
'''


# Ordenando em Ordem Decrescente
produtos.sort(key=itemgetter(1), reverse=True)
print(produtos)
'''
('Bicicleta', 1500), 
('Celular', 750), 
('Microfone', 550)
'''


# Ordenando uma Matriz de Dados
matriz = [[5, 10], [15, 21], [1, 5]]
matriz.sort(key=itemgetter(1))
print(matriz)
'''
[1, 5], 
[5, 10], 
[15, 21]
'''
