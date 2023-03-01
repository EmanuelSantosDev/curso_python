# Índices de Strings

````python
link = 'facebook.com/emanuelsantos'

print(link[0])  # f
print(link[-1])  # s
print(link[0:5])  # faceb
print(link[0:])  # facebook.com/emanuelsantos
print(link[-5:])  # antos
print(link[5:])  # ook.com/emanuelsantos
print(link[:-5])  # facebook.com/emanuels
````

## Acessando Índices com Step

````python
numeros = '123456789'

print(numeros[::])  # 123456789
print(numeros[::2])  # 13579
print(numeros[3:6:2])  # 46
````

## Acessando Índices com Step REVERSO

````python
numeros = '123456789'

print(numeros[::-1])  # 987654321
print(numeros[::-2])  # 97531
````

## Método index()

````python
teclado = 'Teclado'
print(teclado.index('l'))  # 3
print(teclado[teclado.index('l')])  # l
````

## Última Ocorrência com rindex()

````python
frase = 'Clean Code'
print(frase.rindex('C'))  # 6
````