# Callable Object

- Um objeto pode ser chamado como se fosse uma função.
- O método ``__call__`` permite que os programadores escrevam classes onde as instâncias se comportam como funções e podem ser chamadas como uma função

````python
class Numeros:
    def __init__(self) -> None:
        pass

    def __call__(self, *numeros):
        total = 0
        for numero in numeros:
            total += numero
        return total


# instanciando um objeto e atribuindo à uma variável
calculadora_de_soma = Numeros()
resultado_soma = calculadora_de_soma(3, 3, 4)
print(resultado_soma)  # 10


# criando o objeto e chamando o método de forma imediata
print(Numeros()(5, 8, 7))  # 20
````