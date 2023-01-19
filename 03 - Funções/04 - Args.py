# *args


'''
- Número de Argumentos Dinâmicos
- em alguns casos não sabemos quantos argumentos a função irá receber
- os argumentos INDEFINIDOS são passados no formato de tuplas(tipo de lista)
- os argumentos que SIM, já estão definidos, precisam ser nomeados
'''


def somar(*valores, b):
    print(valores)  # (1, 2, 3, 4)
    for valor in valores:
        b += valor
    print(b)  # 18


somar(1, 2, 3, 4, b=8)
