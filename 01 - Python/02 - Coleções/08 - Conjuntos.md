# Conjuntos (Set)


- é um tipo mutável (pode ser alterado).
- pode receber novos elementos.
- não armazena elementos DUPLICADOS.
- não é indexado.
- é uma estrutura de dados desordenada, então ele não preserva a ordem dos elementos.


````python
# criando um "set" manualmente
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}


# podemos converter uma lista (ou uma string) para conjunto
numeros = [2, 2, 5, 8, 2, 2, 5, 2]
conj_numeros = set(numeros)
print(conj_numeros)  # {8, 2, 5}


# usando o operador de membro
print(2 in conj_numeros)  # True
print(3 in conj_numeros)  # False
print(3 not in conj_numeros)  # True


# a ordem e a quantidade não importam
print({1, 2, 3} == {3, 1, 3, 3, 2})  # True


# manipulações básicas sobre conjntos
nomes = {'João', 'Caio', 'Tiago', 'Adalberto'}
nomes.add('Bianca')
nomes.remove('Caio')
nomes.pop()  # remove um item de forma randomica
nomes.clear()


# operações sobre conjuntos
conj1 = {2, 2, 5, 8}
conj2 = {2, 2, 3, 9}
print(conj1.difference(conj2))  # {8, 5}
print(conj1.symmetric_difference(conj2))  # {3, 5, 8, 9}
print(conj1.intersection(conj2))  # {2}
conj3 = conj1.union(conj2)
print(conj3)  # {2, 3, 5, 8, 9}
conj1.update(conj2)
print(conj1)  # {2, 3, 5, 8, 9}


# verificando se um conjunto é "subconjunto" ou "superconjunto" de outro
c1 = {1, 2}
c2 = {1, 2, 3}
print(c1 <= c2)  # True
print(c1 >= c2)  # False
````