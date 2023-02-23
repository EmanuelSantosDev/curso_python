# Builtins

- Builtins (embutidos)
- É um módulo disponivel diretamente no escopo global, ou seja, é importado por padrão a partir da variável ``__builtins__``
- Com isso o interpretador Python tem uma série de **funções** e **tipos** incorporados que estão sempre disponíveis
- É nomeado com double-underscore com a finalidade de evitar que o mesmo seja sobrescrito

## type()

````python
print(__builtins__.type('Olá galera'))  # <class 'str'>
````

## print()

````python
__builtins__.print('Hello Wolrd')  # Hello Wolrd
````

## len()

````python
nome = 'João da Silva'
print(__builtins__.len(nome)) # 13
````

## dir()


````python
print(__builtins__.dir())

"""
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', 'nome', 'numero']
"""
````
