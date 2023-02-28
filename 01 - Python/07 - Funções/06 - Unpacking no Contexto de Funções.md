# Unpacking no Contexto de Funções


### No contexto de Lista e Tuplas

````python
def soma(a, b, c):
    print(a + b + c)


numeros = [3, 5, 8]
soma(*numeros)  # 16

numeros2 = (10, 20, 30)
soma(*numeros2)  # 60
````

### No contexto de Dicionários

````python
def imprimir_cadastro(nome, idade, profissao):
    print('{}, {}, {}'.format(nome, idade, profissao))


pessoa = {
    'nome': 'João',
    'idade': 34,
    'profissao': 'programador'
}

imprimir_cadastro(**pessoa)  # João, 34, programador
````