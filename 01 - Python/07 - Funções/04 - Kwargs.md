# **kwargs (Keyword Arguments)


- são funções com nº ilimitado de argumentos nomeados
- enquanto os "args" são passados como tuplas, os "kwargs" são passados como DICIONÁRIO


````python
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)


concatenar(a='O', b='Grêmio', c='vai', d='sair',
           e='campeão')  # O Grêmio vai sair campeão


# Mesclando uma Função com:
# => argumento posicional de QUANTIDADE DEFINIDA
# => argumentos POSICIONAIS de quantidade X
# => argumentos NOMEADOS de quantidade X


def fazer_calculo(nome, *args, **kwargs):
    print(nome)  # Jeff
    print(args)  # (4, 6, 3, 7)
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3} => dicionário
    for arg in args:
        print(arg, end=" ")  # 4 6 3 7
    for kwarg in kwargs.values():
        print(kwarg, end=" ")  # 1 2 3


fazer_calculo('Jeff', 4, 6, 3, 7, a=1, b=2, c=3)
````
