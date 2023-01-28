# ------------------------------------------------------------------------------------
# Classe - Métodos da Classe
# ------------------------------------------------------------------------------------


# Menos utilzados, porém, são úteis em cenários específicos
# Quando precisamos modificar como uma classe é instanciada
# Exemplo: uma loja que monta computadores
# Podemos ter uma única classe que "monta" computadores básicos e de alta performance
# O parâmetro "cls" é uma convenção
# com ela informamos que estamos passando a classe inteira como parâmetro
# utiliza o decorador "@classmethod"


class Computador:

    sistema_operacional = 'Windows 10'
    versao = 'Home'

    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Ligando o computador')

    def desligar(self):
        print('Desligando o computador')

    def exibir_dados_do_computador(self):
        print(
            f'Computador => {self.marca}, {self.memoria_ram}, {self.placa_de_video}')

    # Métodos da Classe
    # o usuário tem permissão para alterar apenas a memória ram
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Sem Placa de Vídeo')

    @classmethod
    def computador_alta_performance(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'RTX Nvidia Geforce')


# Configuração para Clientes de Escritório
computador1 = Computador.computador_escritorio('8gb')


# Configuração para Gamers, Edição de Vídeo e Modelagem 3D
computador2 = Computador.computador_alta_performance('32gb')


computador1.exibir_dados_do_computador()
# Computador => Dell, 8gb, Sem Placa de Vídeo
computador2.exibir_dados_do_computador()
# Computador => Dell, 32gb, RTX Nvidia Geforce
