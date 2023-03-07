# Reduce


A função ``reduce()`` foi incluída no módulo ``functools`` a partir do Python 3. A função ``reduce()`` recebe uma função e uma sequência e retorna um único valor que é o resultado de aplicar a função acumuladora aos itens da sequência, de forma que os itens da sequência sejam reduzidos a um único valor.


````python
from functools import reduce


numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # 15


palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
frase = reduce(lambda x, y: x + ' ' + y, palavras)
print(frase)  # Python é uma linguagem de programação
````