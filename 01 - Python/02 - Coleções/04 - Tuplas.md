# Tuplas


- É uma maneira de armazenar valores que não devem ser alterados
- Não é possivel alterar os valores depois de terem sido criadas
- É um tipo dinâmico, assim como a lista, e aceita qualquer tipo de dado

````python
# criando uma Tupla
sites = ('youtube.com', 'facebook.com', 'instagram.com')
valores = (23, 43, 65)


# criando uma Tupla com um único elemento
instrumentos = ('guitarra',)
print(instrumentos)  # ('guitarra',)
print(type(instrumentos))  # <class 'tuple'>


# criando uma tupla com tuple(iterável)
lista = ['João', 'Marcelo', 'Caio']
tupla = tuple(lista)
print(tupla)  # ('João', 'Marcelo', 'Caio')


# acessando os valores de uma Tupla
print(valores[2])  # 65


# não é possivel alterar os valores
sites[1] = 'google.com'
# TypeError: 'tuple' object does not support item assignment


# União de Tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)
# ('youtube.com', 'facebook.com', 'instagram.com', 23, 43, 65)


# index(), count() e len()
cores = ('azul', 'amarelo', 'verde', 'azul', 'vermelho')
print(cores.count('azul'))  # 2
print(cores.index('amarelo'))  # 1
print(len(cores))  # 5
````