# Ordenação de Lista

````python
# Ordem Crescente
valores = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]
valores.sort()
print(valores)  # [6, 7, 20, 21, 23, 23, 31, 33, 36, 37]

# Ordem Decrescente
valores2 = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]
valores2.sort(reverse=True)
print(valores2)  # [37, 36, 33, 31, 23, 23, 21, 20, 7, 6]

# Invertendo os Valores
valores3 = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]
valores3.reverse()
print(valores3)  # [23, 20, 7, 37, 33, 21, 36, 6, 23, 31]
````