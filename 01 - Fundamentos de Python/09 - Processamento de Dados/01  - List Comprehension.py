# ------------------------------------------------------------------------------------
# List Comprehension
# ------------------------------------------------------------------------------------


# Oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base...
# ...nos valores de uma lista existente, semelhante à função map()
from pprint import pprint


# ------------------------------------------------------------------------------------
# [expressão for membro in iterável] => NÚMEROS
# ------------------------------------------------------------------------------------


lista = [2 * numero for numero in range(1, 11)]
print(lista)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


nomes = ['Rafael', 'Larissa', 'Mônica', 'Samantha']
aprovados = [nome + ' APROVADO' for nome in nomes]
print(aprovados)
# ['Rafael APROVADO', 'Larissa APROVADO', 'Mônica APROVADO', 'Samantha APROVADO']


# ------------------------------------------------------------------------------------
# [função for membro in iterável] => STRING
# ------------------------------------------------------------------------------------


def aprovar_aluno(nome):
    return nome + ' APROVADO'


alunos_aprovados = [aprovar_aluno(nome) for nome in nomes]
print(alunos_aprovados)
# ['Rafael APROVADO', 'Larissa APROVADO', 'Mônica APROVADO', 'Samantha APROVADO']


# ------------------------------------------------------------------------------------
# Gerando uma Matriz de Dados
# ------------------------------------------------------------------------------------


matriz = [[numero for numero in range(1, 16)] for x in range(5)]
pprint(matriz)
"""
[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
"""


# ------------------------------------------------------------------------------------
# [expressão for membro in iterável (condicional if)] => STRING
# ------------------------------------------------------------------------------------


alunos = ['Rafael', 'Larissa', 'Mônica', 'Leonardo']
print([nome for nome in alunos if 'L' in nome])  # ['Larissa', 'Leonardo']


# ------------------------------------------------------------------------------------
# [expressão for membro in iterável (condicional if)] => NÚMEROS
# ------------------------------------------------------------------------------------


print([n for n in range(1, 21) if n not in (1, 5, 10, 15, 20)])
# [2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]


# ------------------------------------------------------------------------------------
# [expressão for membro in iterável (condicional if)] => NÚMEROS PARES
# ------------------------------------------------------------------------------------


def numero_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


print([numero for numero in range(1, 21) if numero_par(numero)])
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# ------------------------------------------------------------------------------------
# A condicional é flexível... [expressão (condicional if) for membro in iterável]
# ------------------------------------------------------------------------------------


participantes = ['Rafael', 'Larissa', 'Mônica', 'Leonardo']
ganhadores = ['Larissa', 'Leonardo']
print([nome + ' GANHADOR' if nome in ganhadores else nome +
       ' PERDEDOR' for nome in participantes])
# ['Rafael PERDEDOR', 'Larissa GANHADOR', 'Mônica PERDEDOR', 'Leonardo GANHADOR']
