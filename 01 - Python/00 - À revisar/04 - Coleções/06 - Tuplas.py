# ------------------------------------------------------------------------------------
# Tuplas
# ------------------------------------------------------------------------------------


# É uma maneira de armazenar valores que não devem ser alterados
# Não é possivel alterar os valores depois de terem sido criadas
# É um tipo dinâmico, assim como a lista, e aceita qualquer tipo de dado


# criando uma Tupla
sites = ('youtube.com', 'facebook.com', 'instagram.com')
valores = (23, 43, 65)


# acessando os valores de uma Tupla
print(sites[1])  # facebook.com
print(valores[2])  # 65


# não é possivel alterar os valores
# TypeError: 'tuple' object does not support item assignment
sites[1] = 'google.com'


# União de Tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)
# ('youtube.com', 'facebook.com', 'instagram.com', 23, 43, 65)
