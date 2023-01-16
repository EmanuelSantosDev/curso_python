# **kwargs (Keyword Arguments)
# São funções com nº ilimitado de argumentos nomeados

def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)


# O Grêmio vai sair campeão
concatenar(a='O', b='Grêmio', c='vai', d='sair', e='campeão')


'''
Função com:

- número ilimitado de argumentos POSICIONAIS
- número ilimitado de argumentos NOMEADOS
'''


def fazer_calculo(nome, *args, **kwargs):
    print(nome)  # Jeff
    print(args)  # (4, 6, 3, 7)
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3} => dicionário
    for arg in args:
        print(arg, end=" ")  # 4 6 3 7
    for kwarg in kwargs.values():
        print(kwarg, end=" ")  # 1 2 3


fazer_calculo('Jeff', 4, 6, 3, 7, a=1, b=2, c=3)
