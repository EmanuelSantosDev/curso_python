# ------------------------------------------------------------------------------------
# Classe - Métodos Comuns
# ------------------------------------------------------------------------------------


# São os métodos mais utilizados em classes
# São métodos que acessam as propriedades da instância através do "self"


class Computador:

    sistema_operacional = 'Windows 10'
    versao = 'Home'

    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video

    # Métodos Comuns
    def ligar(self):
        print('Ligando o computador')

    def desligar(self):
        print('Desligando o computador')

    def exibir_dados_do_computador(self):
        print(
            f'Computador => {self.marca}, {self.memoria_ram}, {self.placa_de_video}')


computador = Computador('Asus', '8gb', 'Nvídia')


# Acessando Métodos Comuns
computador.ligar()  # Ligando o computador
computador.desligar()  # Desligando o computador
computador.exibir_dados_do_computador()  # Computador => Asus, 8gb, Nvídia
