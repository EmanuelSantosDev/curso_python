# Extrair o nono e o quarto campos do arquivo
# Ignorando a primeira linha que é o cabeçalho

import csv

with open('desafio_ibge.csv') as arquivo:
    for indice, local in enumerate(arquivo):
        if indice == 0:
            continue
        locais = local.strip().split(',')
        print(f'Local de Origem: {locais[3]} => Local de Destino: {locais[8]}')

if arquivo.closed:
    print('\nArquivo Fechado')
