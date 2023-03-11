# **kwargs (Keyword Arguments)


- são funções com nº ilimitado de argumentos nomeados
- enquanto os "args" são passados como tuplas, os "kwargs" são passados como DICIONÁRIO
- **Kwargs** são parâmetros considerados **Packing**, pois empacotam os argumentos recebidos em um Dicionário

````python
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)


concatenar(a='O', b='Grêmio', c='vai', d='sair',
           e='campeão')  # O Grêmio vai sair campeão
````
