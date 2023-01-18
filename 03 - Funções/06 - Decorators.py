# Decorators


'''
- altera o comportamento da função sem precisar alterar o seu código internamente
- facilita o reuso de código
'''


def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper


@meu_decorator
def parabenizar():
    print('Parabéns')


parabenizar()
