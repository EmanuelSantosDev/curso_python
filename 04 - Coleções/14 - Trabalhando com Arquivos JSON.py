# Trabalhando com Arquivos JSON


# -----------------------------------------------------------
# Criando um Arquivo JSON
# -----------------------------------------------------------


import json
from pathlib import Path

carros = [
    {'Marca': 'Nissan', 'Preco': 45000, 'Cor': 'Azul'},
    {'Marca': 'Ford', 'Preco': 75000, 'Cor': 'Verde'},
    {'Marca': 'BMW', 'Preco': 117000, 'Cor': 'Amarelo'},
]

# converte um objeto python em um objeto JSON equivalente
carros_json = json.dumps(carros)
Path('04 - Coleções\carros.json').write_text(carros_json)


# -----------------------------------------------------------
# Lendo um Arquivo JSON
# -----------------------------------------------------------


# lendo o arquivo 'carros.json'
arquivo_carros_json = Path('04 - Coleções\carros.json').read_text()

# analisando a string JSON e convertendo em um dicionário Python
carros_dicionario = json.loads(arquivo_carros_json)

print(carros_dicionario[1]['Marca'] + ' ' + str(carros_dicionario[1]['Preco']))
# Ford 75000


# -----------------------------------------------------------
# Desafio Pikachu
# => encontrar e exibir na tela a 'ability' 'lightning-rod'
# -----------------------------------------------------------


arquivo_pikachu = Path('04 - Coleções\pikachu.json').read_text()
arquivo_pikachu_convertido = json.loads(arquivo_pikachu)
print(arquivo_pikachu_convertido['abilities'][1]['ability']['name'])
# lightning-rod
