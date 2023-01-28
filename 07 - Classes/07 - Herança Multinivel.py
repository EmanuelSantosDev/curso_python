# ------------------------------------------------------------------------------------
# Herança Multinivel
# ------------------------------------------------------------------------------------


# devemos evitá-la, pois pode tornar o código completo e dificil de interpretar


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
