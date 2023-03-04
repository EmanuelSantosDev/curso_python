# Herança Múltipla


**Herança Múltipla** é quando uma classe filha (subclasse) herda de várias classes pai (superclasses) ao mesmo tempo.


````python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_barulho(self):
        pass


class Corredor:
    def correr(self):
        print('O corredor está correndo')


class Cachorro(Animal, Corredor):
    def fazer_barulho(self):
        print('O cachorro late')


cachorro = Cachorro('Rex')


cachorro.fazer_barulho()  # O cachorro late
cachorro.correr()  # O corredor está correndo
print(cachorro.nome)  # Rex
````