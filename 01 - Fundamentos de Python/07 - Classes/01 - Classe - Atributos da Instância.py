# ------------------------------------------------------------------------------------
# Classe - Atributos da Instância
# ------------------------------------------------------------------------------------


# a função "__init__" inicializa  a classe
# o parâmetro "self" faz referência ao próprio objeto que está sendo instanciado


class Computador:

    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video


computador = Computador('Asus', '8gb', 'Nvídia')


print(computador.placa_de_video)  # Nvídia
