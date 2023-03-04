# MRO (Method Resolution Ordem)


- **MRO (Method Resolution Order)** é a ordem em que o interpretador Python procura por métodos em uma hierarquia de classes quando uma chamada de método é feita.
- A MRO é usada para determinar qual método deve ser chamado primeiro, caso uma classe tenha vários métodos com o mesmo nome, mas que foram definidos em diferentes classes pai.


````python
class A:
    def sou_a_letra():
        print('Sou a letra A')


class B(A):
    def sou_a_letra():
        print('Sou a letra B')


class C(A):
    def sou_a_letra():
        print('Sou a letra C')


class D(B, C):
    def sou_a_letra():
        print('Sou a letra D')


print(D.__mro__)
# (<class '__main__.D'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.A'>,
# <class 'object'>)

D.sou_a_letra()  # Sou a letra D
````

Isso significa que, quando uma chamada de método é feita em um objeto da classe D, o interpretador Python procurará pelo método na seguinte ordem: D, B, C, A, e finalmente, object.