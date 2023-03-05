# Mixin


- **Mixin** é um conceito de programação orientada a objetos que se refere a uma classe que fornece um conjunto de funcionalidades que podem ser adicionadas a outras classes, sem precisar ser uma classe base para elas.
- Ou seja, um mixin é uma classe que não é destinada a ser usada sozinha, mas sim para fornecer um conjunto de comportamentos adicionais para outras classes.
- A implementação de mixins em Python é feita por meio de herança múltipla.


Neste exemplo, a classe ``AndarMixin`` define o método ``andar()``. A classe ``Cachorro`` herda de ``Animal`` e de ``AndarMixin``, enquanto a classe ``Gato`` herda apenas de ``Animal``:


````python
class AndarMixin:
    def andar(self):
        print("O animal está andando...")


class Animal:
    pass


class Cachorro(Animal, AndarMixin):
    pass


class Gato(Animal):
    pass


cachorro = Cachorro()
cachorro.andar()  # O animal está andando...
````


Neste exemplo temos uma classe que implementa métodos de comparação para objetos com base em um único atributo. Essa classe pode ser usada como mixin para outras classes que precisam ser comparáveis com base nesse atributo específico:


````python
class ComparableMixin:
    def __eq__(self, other):
        return self.idade == other.idade

    def __lt__(self, other):
        return self.idade < other.idade

    def __le__(self, other):
        return self.idade <= other.idade

    def __gt__(self, other):
        return self.idade > other.idade

    def __ge__(self, other):
        return self.idade >= other.idade


class Pessoa(ComparableMixin):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

print(pessoa1 == pessoa2)  # False
print(pessoa1 > pessoa2)  # True
print(pessoa1 < pessoa2)  # False
````