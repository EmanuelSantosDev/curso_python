# Classe


class Computador:
    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video


computador1 = Computador('Asus', '8gb', 'Nvídia')
print(computador1.marca)
print(computador1.memoria_ram)
print(computador1.placa_de_video)
'''
Asus
8gb
Nvídia
'''


computador2 = Computador('Dell', '4gb', 'ATI')
print(computador2.marca)
print(computador2.memoria_ram)
print(computador2.placa_de_video)
'''
Dell
4gb
ATI
'''
