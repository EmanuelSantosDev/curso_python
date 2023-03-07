# Funções de Alta Ordem


**Funções de Alta Ordem** são funções que recebem outras funções como argumentos ou retornam funções como resultado.


````python
def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


processar('Dobros de 1 a 10', range(1, 11), dobro)

# Processando: Dobros de 1 a 10
# 1 => 2
# 2 => 4
# 3 => 6
# 4 => 8
# 5 => 10
# 6 => 12
# 7 => 14
# 8 => 16
# 9 => 18
# 10 => 20

processar('Quadrado de 1 a 10', range(1, 11), dobro)

# Processando: Quadrado de 1 a 10
# 1 => 2
# 2 => 4
# 3 => 6
# 4 => 8
# 5 => 10
# 6 => 12
# 7 => 14
# 8 => 16
# 9 => 18
# 10 => 20
````