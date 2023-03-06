# Conversão de Tipo entre Coleções


### Convertendo uma String para Coleções


````python
saudacao = 'Hello'

print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))

# ['H', 'e', 'l', 'l', 'o']
# {'l', 'H', 'o', 'e'}
# ('H', 'e', 'l', 'l', 'o')
````


### Convertendo uma Range para Coleções


````python
print(list(range(30)))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
#  16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
````


### Convertendo uma Lista para Outros Tipos de Coleções


````python
numeros = [10, 20, 20, 50]

print(set(numeros))
print(tuple(numeros))

# {10, 20, 50}
# (10, 20, 20, 50)
````