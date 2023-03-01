# Generator

- Generators usam expressões similares ao List Comprehension
- Contudo, ele gera 1 valor por vez (sob demanda), consumindo muito menos memória do computador

````python
generator = (i for i in range(1, 11))

print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print(next(generator))  # 4
print(next(generator))  # 5
print(next(generator))  # 6
print(next(generator))  # 7
print(next(generator))  # 8
print(next(generator))  # 9
print(next(generator))  # 10
print(next(generator)) # Erro (StopIteration)


print(type(generator))  # <class 'generator'>


# iterando com o laço FOR
for numero in generator:
    print(numero, end=' ')  # 1 2 3 4 5 6 7 8 9 10
````