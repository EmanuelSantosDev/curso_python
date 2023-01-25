# ------------------------------------------------------------------------------------
# Map
# ------------------------------------------------------------------------------------


'''
- é um método que passa como argumento uma função que será aplicada 
  sobre todos os items de um conjunto de dados retornando um novo
  conjunto de dados processados 
'''


nomes = ['Larissa', 'Rafael', 'Marcus', 'John']


def aprovar_pessoa(nome):
    return nome + ' APROVADO'


lista_aprovados = list(map(aprovar_pessoa, nomes))
print(lista_aprovados)
# ['Larissa APROVADO', 'Rafael APROVADO', 'Marcus APROVADO', 'John APROVADO']


# Extraindo as cores da lista a seguir e colocando-as em uma nova lista.


pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]


def extrair_cores(pintura):
    return pintura[1]


lista_de_cores = list(map(extrair_cores, pinturas))
print(lista_de_cores)  # ['Azul', 'Vermelha', 'Verde']
