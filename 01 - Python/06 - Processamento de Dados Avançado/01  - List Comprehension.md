# List Comprehension


Oferece uma sintaxe mais curta quando se  deseja criar uma nova lista com base nos valores de uma lista existente, semelhante à função ``map()``:


````python
# -----------------------------------------------------------------------------------
# [elemento + for]
# ------------------------------------------------------------------------------------


lista = [2 * numero for numero in range(1, 11)]
print(lista)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


nomes = ['Rafael', 'Larissa', 'Mônica', 'Samantha']
aprovados = [nome + ' APROVADO' for nome in nomes]
print(aprovados)
# ['Rafael APROVADO', 'Larissa APROVADO', 'Mônica APROVADO', 'Samantha APROVADO']


# ------------------------------------------------------------------------------------
# [função(elemento) + for]
# ------------------------------------------------------------------------------------


def aprovar_aluno(nome):
    return nome + ' APROVADO'


alunos_aprovados = [aprovar_aluno(nome) for nome in nomes]
print(alunos_aprovados)
# ['Rafael APROVADO', 'Larissa APROVADO', 'Mônica APROVADO', 'Samantha APROVADO']


# ------------------------------------------------------------------------------------
# [[elemento + for] for] => Gerando uma Matriz 
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
# [elemento + for + if] 
# ------------------------------------------------------------------------------------


print([n for n in range(1, 21) if n not in (1, 5, 10, 15, 20)])
# [2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]


# ------------------------------------------------------------------------------------
# [elemento + if + else + elemento + for]
# ------------------------------------------------------------------------------------


participantes = ['Rafael', 'Larissa', 'Mônica', 'Leonardo']
ganhadores = ['Larissa', 'Leonardo']
print([nome + ' GANHADOR' if nome in ganhadores else nome +
       ' PERDEDOR' for nome in participantes])
# ['Rafael PERDEDOR', 'Larissa GANHADOR', 'Mônica PERDEDOR', 'Leonardo GANHADOR']
````