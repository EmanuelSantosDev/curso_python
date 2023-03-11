# Função com Múltiplos Tipos de Argumentos


Compondo uma funçao com: **Argumentos Posicionais** + **Args** + **Kwargs**.


````python
def fazer_calculo(nome, *args, **kwargs):
    print(nome)  # Jeff
    print(args)  # (4, 6, 3, 7)
    print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}


fazer_calculo('Jeff', 4, 6, 3, 7, a=1, b=2, c=3)
````
