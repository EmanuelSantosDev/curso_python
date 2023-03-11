# Map


A função ``map()`` permite aplicar uma função a cada elemento de uma sequência (como uma lista, tupla ou conjunto) e retornar um iterador com os resultados.


````python
numeros = [1, 2, 3, 4, 5]
quadrados = map(lambda x: x * 2, numeros)
print(list(quadrados))  # [2, 4, 6, 8, 10]
````