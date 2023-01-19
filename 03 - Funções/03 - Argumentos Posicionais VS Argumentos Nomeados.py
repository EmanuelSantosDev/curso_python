# Argumentos Posicionais


def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de R$ {preco}')


exibir_preco('iPhone', 5000)
exibir_preco(5000, 'iPhone')
'''
iPhone está no valor de R$ 5000
5000 está no valor de R$ iPhone
'''


# Argumentos Nomeados


exibir_preco(preco=5000, nome_produto='iPhone')


# inserindo '*' obriga que todos os próximos argumentos sejam NOMEADOS
# TypeError: quantidade() takes 0 positional arguments but 2 were given
def quantidade(*, a, b):
    print(a + b)
quantidade(2, 5)


# / TypeError: multiplicacao() takes 1 positional argument but 2 were given
def multiplicacao(x, *, y):
    print(x * y)
multiplicacao(4, 3)
