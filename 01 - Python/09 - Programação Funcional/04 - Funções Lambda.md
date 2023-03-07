# Funções Lambda


**Funções Lambda**, também conhecidas como _funções anônimas_, são funções de uma única expressão que podem ser definidas e usadas em uma única linha de código, sem precisar de um nome para a função. 


### Exemplo #1


````python
soma = lambda x, y: x + y
print(soma(3, 4))  # 7
````


### Exemplo #2


````python
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)


totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)


print('Preços Totais:', totais)  # Preços Totais: (20, 60, 70)
````