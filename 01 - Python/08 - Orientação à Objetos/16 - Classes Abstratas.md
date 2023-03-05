# Classes Abstratas


- Uma classe abstrata é uma classe que não pode ser instanciada diretamente.
- Em vez disso, ela é projetada para ser usada como uma classe base para outras classes que implementam seus métodos abstratos.
- A classe abstrata define um contrato para as classes filhas, especificando quais métodos elas devem implementar.
- Esse contrato garante que todas as classes filhas da classe abstrata tenham uma funcionalidade básica em comum.
- Uma classe abstrata é definida usando o módulo ``abc`` (Abstract Base Class) da biblioteca padrão do Python. Você pode criar uma classe abstrata definindo pelo menos um método abstrato, usando o decorador ``@abstractmethod``.


````python
from abc import ABC, abstractmethod


class Forma(ABC):

    @abstractmethod
    def calcular_area(self):
        pass


class Retangulo(Forma):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


retangulo = Retangulo(10, 20)
area = retangulo.calcular_area()
print(area)  # 200
````