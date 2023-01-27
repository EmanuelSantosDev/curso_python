# ------------------------------------------------------------------------------------
# Classe - Atributos e Métodos
# ------------------------------------------------------------------------------------


'''
-> deff'__init__()' - inicializa  a classe
-> 'self' - faz referência à um atributo que pertence ao objeto que está sendo criado
'''


class Computador:
    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Ligando o computador')

    def desligar(self):
        print('Desligando o computador')

    def exibir_dados_do_computador(self):
        print(f'Computador => {self.marca}, {self.memoria_ram}, {self.placa_de_video}')


computador = Computador('Asus', '8gb', 'Nvídia')


# Acessando Atributos
print(computador.marca)  # Asus
print(computador.memoria_ram)  # 8gb
print(computador.placa_de_video)  # Nvídia


# Acessando Métodos
computador.ligar()  # Ligando o computador
computador.desligar()  # Desligando o computador
computador.exibir_dados_do_computador()  # Computador => Asus, 8gb, Nvídia
