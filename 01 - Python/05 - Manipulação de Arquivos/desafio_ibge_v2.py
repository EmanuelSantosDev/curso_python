# Extrair o nono e o quarto campos do arquivo
# Ignorando a primeira linha que é o cabeçalho

import csv

with open('desafio_ibge.csv') as arquivo:
    for indice, local in enumerate(csv.reader(arquivo)):
        if indice == 0:
            continue
        print(f'Local de Origem: {local[3]} => Local de Destino: {local[8]}')

if arquivo.closed:
    print('\nArquivo Fechado')
