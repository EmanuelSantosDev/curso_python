# ------------------------------------------------------------------------------------
# Decorators
# ------------------------------------------------------------------------------------


'''
- altera o comportamento da função sem precisar alterar o seu código internamente
- facilita o reuso de código
'''


def texto(funcao):
    def wrapper(a, b):
        print('PRIMEIRO')
        funcao(a, b)
        print('SEGUNDO')
    return wrapper


@texto
def soma(a, b):
    print(a+b)


soma(5, 10)
'''
PRIMEIRO
15
SEGUNDO
'''
