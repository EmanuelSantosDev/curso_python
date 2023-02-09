# ------------------------------------------------------------------------------------
# Polimorfismo
# ------------------------------------------------------------------------------------


# quer dizer que algo pode funcionar de formas diferentes dependendo do contexto
# um método, por exemplo, pode ter comportamentos diferentes dependendo da... 
# ...quantidade de argumentos que são passados para ele


class Carro:
    def ligar(self):
        print('Ligando o carro')


class Moto:
    def ligar(self):
        print('Ligando a moto')


# essa função terá um comportamento diferente de acordo com o objeto que ela recebe
def iniciar(veiculo):
    veiculo.ligar()


carro = Carro()
moto = Moto()


iniciar(carro)  # Ligando o carro
iniciar(moto)  # Ligando a moto


# ------------------------------------------------------------------------------------
# E quando queremos versões diferentes de uma mesma função?
# ------------------------------------------------------------------------------------


class Pessoa:
    # transformamos os argumentos extras em argumentos opcionais
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(f'{nome}')


pessoa = Pessoa()


# a mesma função, para o mesmo objeto, se comporta de maneiras diferentes:
pessoa.apresentar('John', idade=22, profissao='Programador')
# John, 22, Programador
pessoa.apresentar('John', idade=22)
# John, 22
pessoa.apresentar('John', profissao='Programador')
# John, Programador
pessoa.apresentar('John')
# John
