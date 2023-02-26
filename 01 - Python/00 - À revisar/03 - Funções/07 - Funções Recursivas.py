# Funções Recursivas

# o "return" é vazio
# há um limite nas funções recursivas que podem ser chamadas até 996 vezes
def imprimir(maximo, atual):
    if atual > maximo:
        return
    print(atual, end=' ')
    imprimir(maximo, atual + 1)
    
imprimir(10, 1)
# 1 2 3 4 5 6 7 8 9 10