# Enumerate


- É usada para iterar sobre uma sequência (lista, tupla, string, etc.) e retornar um objeto enumerado. 
- O objeto ``enumerate`` contém pares de valores, onde o primeiro valor é o índice e o segundo valor é o elemento da sequência.
- Permite configurar o valor inicial para o indice.


### enumerate() sobre um range()


````python
for indice, numero in enumerate(range(32, 43), 0):
    print(indice, numero)
    if indice == 9:
        print('Estamos no penúltimo item da lista')

# 0 32
# 1 33
# 2 34
# 3 35
# 4 36
# 5 37
# 6 38
# 7 39
# 8 40
# 9 41
# Estamos no penúltimo item da lista
# 10 42
````


### enumerate() sobre uma lista


````python
frutas = ['Maçã', 'Laranja', 'Morango', 'Limão']`

for indice, fruta in enumerate(frutas, 1):
    if indice != 3:
        print(f'{indice} => {fruta}')
    else:
        print(f'{indice} => {fruta} EM PROMOÇÃO')

# 1 => Maçã
# 2 => Laranja
# 3 => Morango EM PROMOÇÃO
# 4 => Limão
````