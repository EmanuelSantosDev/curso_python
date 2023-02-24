# Funções de Strings


## upper() e lower()

````python
nome_do_curso = 'Edição de Vídeo'

print(nome_do_curso.upper())  # EDIÇÃO DE VÍDEO
print(nome_do_curso.lower())  # edição de vídeo
````

## strip(), lstrip() e rstrip()

````python
nome_do_curso = '   Edição de Vídeo   '

print(nome_do_curso.strip())   # Edição de Vídeo
print(nome_do_curso.lstrip())  # Edição de Vídeo
print(nome_do_curso.rstrip())  #    Edição de Vídeo
````

## find()

````python
nome_do_curso = 'Edição de Vídeo'

print(nome_do_curso.find('ção'))  # 3
````

## replace()
````python
nome_do_curso = 'Edição de Vídeo'

print(nome_do_curso.replace('Vídeo', 'Música')) # Edição de Música
print('https://sc.olx.com.br/relogio'.replace('relogio', 'carro')) # https://sc.olx.com.br/carro
````

## split()

````python
frase = "Olá, seja bem-vindo à este treinamento"

print(frase.split())  # ['Olá,', 'seja', 'bem-vindo', 'à', 'este', 'treinamento']
print(frase.split(','))  # ['Olá', ' seja bem-vindo à este treinamento']
print(frase.split('-'))  # ['Olá, seja bem', 'vindo à este treinamento']
print(frase.split(' ', 2))  # ['Olá,', 'seja', 'bem-vindo à este treinamento']
````

## join()

````python
nomes = ['Ana', 'Miguel', 'Samuel', 'Otavio']

print(' - '.join(nomes))  # Ana - Miguel - Samuel - Otavio
````