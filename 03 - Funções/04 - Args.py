# ------------------------------------------------------------------------------------
# *args
# ------------------------------------------------------------------------------------


'''
- em alguns casos não sabemos QUANTOS argumentos a função irá receber
- esta quantidade X de argumentos são passados no formato de TUPLAS
- os DEMAIS ARGUMETNOS devem ser NOMEADOS
'''


def somar(*valores, b):
    print(valores)  # (1, 2, 3, 4)
    for valor in valores:
        b += valor
    print(b)  # 18


somar(1, 2, 3, 4, b=8)
