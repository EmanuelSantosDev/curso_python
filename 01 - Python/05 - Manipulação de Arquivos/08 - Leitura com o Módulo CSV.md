# Leitura com o Módulo CSV

````python
import csv

with open('pessoas.csv', encoding="utf-8") as arquivo:
    for pessoa in csv.reader(arquivo):
        print(pessoa)
        print(f'Nome: {pessoa[0]}, Idade = {pessoa[1]}')

if arquivo.close:
    print('Arquivo Fechado')

"""
Nome: Maria, Idade = 45
['João', '33']
Nome: João, Idade = 33
['Pedro', '63']
Nome: Pedro, Idade = 63
['Ana', '21']
Nome: Ana, Idade = 21
['Bia', '40']
Nome: Bia, Idade = 40
['Carlos', '14']
Nome: Carlos, Idade = 14
Arquivo Fechado
"""
````