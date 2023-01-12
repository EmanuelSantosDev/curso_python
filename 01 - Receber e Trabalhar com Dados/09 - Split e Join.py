# split()

frase = "Olá, seja bem-vindo à este treinamento"

print(frase.split())
# ['Olá,', 'seja', 'bem-vindo', 'à', 'este', 'treinamento']
print(frase.split(','))
# ['Olá', ' seja bem-vindo à este treinamento']
print(frase.split('-'))
# ['Olá, seja bem', 'vindo à este treinamento']

# 'Bruna' e 'Carol' não tem espaço

nomes = 'Emanuel, Cecília, Joaquina, Ana, Bruna,Carol'

print(nomes.split())
# ['Emanuel,', 'Cecília,', 'Joaquina,', 'Ana,', 'Bruna,Carol']
print(nomes.split(','))
# ['Emanuel', ' Cecília', ' Joaquina', ' Ana', ' Bruna', 'Carol']

# especificando um número máximo de ocorrências

print(nomes.split(',', 3))
# ['Emanuel', ' Cecília', ' Joaquina', ' Ana, Bruna,Carol']

# join() para concatenar strings

hashtags = '#python #javascript #java #programação #sql #html'
hashtags_separadas = hashtags.split()

print(', '.join(hashtags_separadas))
# #python, #javascript, #java, #programação, #sql, #html
print('. '.join(hashtags_separadas))
# #python. #javascript. #java. #programação. #sql. #html
print(' '.join(hashtags_separadas))
# #python #javascript #java #programação #sql #html
