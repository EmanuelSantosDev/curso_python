# ------------------------------------------------------------------------------------
# Métodos Mágicos - Double Underscore
# ------------------------------------------------------------------------------------


"""

-> são métodos que executam automaticamente quando efetuamos alguma rotina específica

-> "__init__" é um método mágico que inicializa uma classe

-> "__len__" determina o que deve ser mensurado para se obter a quantidade(comprimento) 
   de uma determinada classe 

-> "__repr__" cria uma representação do objeto para o programador no console do Python. 

-> "__str__" cria uma representação legível no formato de string e serve para exibir 
    o objeto para usuário final, usada pelo comando print() e pela função str

-> "dir(nome_da_instância)" fornece todos os métodos mágicos disponíveis em uma classe

"""


class Pessoa:
    def __init__(self):
        self.nome = 'Pessoa'
        self.habilidades = ['Pular', 'Correr', 'Salvar', 'Falar']

    def __repr__(self):
        return 'Classe Pessoa com propriedades "nome" e "habilidades"'

    def __len__(self):
        return len(self.habilidades)

    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidades}'


pessoa = Pessoa()

print(len(pessoa))
# 4

print(repr(pessoa))
# Classe Pessoa com propriedades "nome" e "habilidades"
# esta é a frase que irá aparecer no console de debug se digitarmos "pessoa"

print(pessoa)
# Pessoa com as habilidades ['Pular', 'Correr', 'Salvar', 'Falar']

print(dir(pessoa))
# fornece todos os métodos mágicos disponíveis em uma classe
