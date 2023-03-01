# Funções Recursivas

- Há um limite onde as funções podem ser chamadas de forma recursiva até mais ou menos 997 vezes
- Se forçar além disso lançará o erro ``maximum recursion depth exceeded while calling a Python object``
- No exemplo abaixo o ``return`` é vazio com a finalidade apenas de encerrar a função
- Um ``return`` vazio, por baixo retorna ``None``

````python
def imprimir(maximo, atual):
    if atual > maximo:
        return
    print(atual, end=' ')
    imprimir(maximo, atual + 1)
    
imprimir(1000, 1)
# 1 2 3 4 5 6 7 8 9 10
````