# Filter


A função ``filter()`` permite filtrar os elementos de uma sequência (como uma lista, tupla ou conjunto) com base em uma condição especificada por uma função. A função ``filter()`` retorna um iterador com os elementos da sequência que atendem à condição.


````python
# Filtrando apenas os números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # [2, 4, 6, 8, 10]
````