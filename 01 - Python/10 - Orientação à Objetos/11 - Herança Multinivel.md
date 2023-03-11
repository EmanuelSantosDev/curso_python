# Herança Multinivel


- *Herança Multinível* é quando uma classe filha (subclasse) herda de uma classe pai (superclasse), que por sua vez herda de outra classe pai, e assim por diante. 
- Devemos evitá-la, pois pode tornar o código complexo e dificil de interpretar.


````python
class Veiculo:
    pass


class VeiculoDeRodas(Veiculo):
    pass


class Carro(VeiculoDeRodas):
    pass


class CarroEletrico(Carro):
    pass


class CarroEletricoDuasPortas(CarroEletrico):
    pass
````