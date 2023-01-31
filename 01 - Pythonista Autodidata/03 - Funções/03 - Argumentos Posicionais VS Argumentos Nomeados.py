# ----------------------------------------------------------------
# Argumentos Posicionais
# ----------------------------------------------------------------


def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de R$ {preco}')


exibir_preco('iPhone', 5000)  # iPhone está no valor de R$ 5000
exibir_preco(5000, 'iPhone')  # 5000 está no valor de R$ iPhone


# ----------------------------------------------------------------
# Argumentos Nomeados
# ----------------------------------------------------------------


# invocando uma função passando argumentos nomeados
exibir_preco(preco=5000, nome_produto='iPhone')


# inserindo '*' obriga que os ARGUMENTOS À DIREITA sejam NOMEADOS
def quantidade(*, a, b):
    print(a + b)


quantidade(a=2, b=5)  # 7


# ----------------------------------------------------------------
# Mesclando Argumetos Posicionais + Argumentos Nomeados
# ----------------------------------------------------------------


def multiplicacao(x, *, y):
    print(x * y)


multiplicacao(4, y=3)  # 12
