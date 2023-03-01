# Callable

- Uma função pode ser passada como parâmetro para outra função
- A função ``callable()`` testa se o objeto recebido é uma função que pode ser chamada

````python
def acionar_funcao(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom Dia!')


def boa_noite():
    print('Boa Noite!')


acionar_funcao(bom_dia())
acionar_funcao('Olá Mundo')
acionar_funcao(boa_noite())

# Bom Dia!
# Boa Noite!
````