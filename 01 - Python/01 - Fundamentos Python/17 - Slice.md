# Slice

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

### Adicionando um Step

````python
numeros = '123456789'

print(numeros[::])  # 123456789
print(numeros[::2])  # 13579
print(numeros[3:6:2])  # 46
````

### Slice Reverso

````python
numeros = '123456789'

print(numeros[::-1])  # 987654321
print(numeros[::-2])  # 97531
````

