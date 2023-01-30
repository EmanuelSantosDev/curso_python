# ------------------------------------------------------------------------------------
# Sets
# ------------------------------------------------------------------------------------


# é um tipo mutável (pode ser alterado)
# pode receber novos elementos
# PORÉM NÃO permite elementos DUPLICADOS
# é uma estrutura de dados desordenada, então ele não preserva a ordem dos elementos


# convertendo para set e eliminando os valores duplicados
numeros = [2, 2, 5, 8]
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}  # criando um set
set_numeros = set(numeros)
set_frutas = set(frutas)
print(set_numeros)
print(set_frutas)
# {8, 2, 5}
# {'morango', 'maça', 'uva', 'banana'}


# adicionando novos valores
set_numeros.add(10)
print(set_numeros)  # {8, 2, 10, 5}


# Conjuntos
numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)
print(a.symmetric_difference(b))  # {3, 5, 8, 9}
print(a.intersection(b))  # {2}
print(a.union(b))  # {2, 3, 5, 8, 9}
