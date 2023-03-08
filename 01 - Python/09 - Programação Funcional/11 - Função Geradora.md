# Função Geradora


- Uma **Função Geradora** é útil quando você precisa gerar um grande número de valores ou quando os valores precisam ser gerados sob demanda em vez de armazenados em uma lista.
- ``yield``  é uma palavra-chave do Python usada em funções geradoras para produzir um valor e pausar a execução da função.
- ``next()`` é uma função interna do Python que permite obter o próximo elemento de um iterador ou de um objeto gerador.


````python
# Observe que a função "rainbow_colors()" não retorna uma lista de cores,
# mas sim um gerador que produz uma sequência de valores quando é iterado.


def rainbow_colors():
    yield "vermelho"
    yield "laranja"
    yield "amarelo"
    yield "verde"
    yield "azul"
    yield "anil"
    yield "violeta"


for color in rainbow_colors():
    print(color)

# vermelho
# laranja
# amarelo
# verde
# azul
# anil
# violeta


# Função Geradora que produz uma sequência de números pares infinita.
# Usamos a função "next()" para obter cada número sucessivo na sequência


def even_numbers():
    n = 0
    while True:
        yield n
        n += 2


evens = even_numbers()
for i in range(10):
    print(next(evens))

# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
````