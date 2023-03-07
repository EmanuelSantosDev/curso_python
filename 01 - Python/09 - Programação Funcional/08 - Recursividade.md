# Recursividade

- **Recursividade** é um conceito de programação que se refere à capacidade de uma função chamar a si mesma.
- Essa técnica pode ser usada para resolver problemas complexos, dividindo-os em problemas menores e resolvendo cada um deles recursivamente.
- A chamada recursiva só para quando uma condição de parada é alcançada, chamada de **caso base**.


````python
def imprimir(maximo, atual):
    if atual > maximo:
        return
    print(atual, end=' ')
    imprimir(maximo, atual + 1)
    
imprimir(10, 1)

# 1 2 3 4 5 6 7 8 9 10
````