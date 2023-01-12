# slice( )

# acessando partes de uma string
link = 'facebook.com/emanuelsantos'
print(link[0])  # f
print(link[-1])  # s
print(link[0:5])  # faceb
print(link[0:])  # facebook.com/emanuelsantos
print(link[-5:])  # antos
print(link[5:])  # ook.com/emanuelsantos
print(link[:-5])  # facebook.com/emanuels

# index()
teclado = 'Teclado'
print(teclado.index('l'))  # 3
print(teclado[teclado.index('l')])  # l

# localizando a última ocorrência de um determinado valor com rindex()
frase = 'Clean Code'
print(frase.rindex('C'))  # 6
