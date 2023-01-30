# ------------------------------------------------------------------------------------
# Laço FOR
# ------------------------------------------------------------------------------------


# O laço for não inclui o último valor:
for numero in range(5):
    print(f'carregando {numero}')
'''
carregando 0
carregando 1
carregando 2
carregando 3
carregando 4
'''


# passando um valor inicial para o range()
for numero in range(10, 16):
    print(f'carregando {numero}')
'''
carregando 10
carregando 11
carregando 12
carregando 13
carregando 14
carregando 15
'''


# passando o STEP como 3º parâmetro
for numero in range(10, 30, 3):
    print(f'Número {numero}')
'''
Número 10
Número 13
Número 16
Número 19
Número 22
Número 25
Número 28 
'''


# iterando sobre uma LISTA DE STRINGS
nomes = ['Emanuel', 'Lucas', 'Sabrina', 'Ariel', 'Jonny']
for nome in nomes:
    print(f'NOME: {nome}')
'''
NOME: Emanuel
NOME: Lucas
NOME: Sabrina
NOME: Ariel
NOME: Jonny
'''
