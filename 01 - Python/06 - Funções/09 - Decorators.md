# Decorators


- **Decorator** é que um método que envolve uma função, modificando o seu comportamento sem precisar alterar o seu código internamente
- Facilita o reuso de código


````python
def banco_dados(function):
    def decorator(a, b):
        print('Abrindo o banco de dados')
        resultado = function(a, b)
        print(f'Resultado da Soma = {resultado}')
        print('Fechando o banco de dados')
        return resultado
    return decorator


@banco_dados
def soma(a, b):
    return a + b


resultado = soma(5, 2)
print(resultado)
# Abrindo o banco de dados
# Resultado da Soma = 7
# Fechando o banco de dados
# 7


# SEM DECORATOR


def soma2(a, b):
    return a + b


resultado = soma2(5, 2)
print(resultado)
# 7
````