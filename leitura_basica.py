# Leitura com Bloco WITH


with open('pessoas.csv', encoding='utf-8') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo Fechado')

"""
Nome: Maria Idade: 45
Nome: João Idade: 33
Nome: Pedro Idade: 63
Nome: Ana Idade: 21
Nome: Bia Idade: 40
Nome: Carlos Idade: 14

Arquivo Fechado
"""