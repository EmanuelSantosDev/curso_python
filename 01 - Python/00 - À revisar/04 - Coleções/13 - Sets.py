# ------------------------------------------------------------------------------------
# Sets
# ------------------------------------------------------------------------------------


# é um tipo mutável (pode ser alterado)
# pode receber novos elementos
# PORÉM NÃO permite elementos DUPLICADOS
# é uma estrutura de dados desordenada, então ele não preserva a ordem dos elementos
# comparando dois conjuntos podemos estraír os items:
# >>>>> DIFERENTES, DIFERENTES SIMETRICAMENTE, IGUAIS e a UNIÃO de ambos os conjuntos


# criando um "set" manualmente
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}


# convertendo para "set" e eliminando os valores duplicados
numeros = [2, 2, 5, 8]
set_numeros = set(numeros)
print(set_numeros)  # {8, 2, 5}


# adicionando novos valores
set_numeros.add(10)
print(set_numeros)  # {8, 2, 10, 5}


# operando com CONJUNTOS
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]

a = set(numeros1)
b = set(numeros2)

print(a.difference(b))  # {8, 5}
print(a.symmetric_difference(b))  # {3, 5, 8, 9}
print(a.intersection(b))  # {2}
print(a.union(b))  # {2, 3, 5, 8, 9}
