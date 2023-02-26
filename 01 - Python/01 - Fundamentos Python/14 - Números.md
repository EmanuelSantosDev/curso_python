# Números

## is_integer()

````python
numero = 2.5
print(numero.is_integer())  # False
````

## isnumeric()

````python
print('123'.isnumeric())  # True
print('12b3'.isnumeric())  # False
````

## round()

````python
print(round(5.7))  # 6
````

## abs()

````python
x = -2
print(abs(x))  # 2
````

## sum()
````python
# A função ``sum()`` devolve a soma de todos os itens de um iterável
# é possivel passar também um "start" para a realização da soma
a = (1, 2, 3, 4, 5)
print(sum(a))  # 15
print(sum(a, 7))  # 22
````