# ------------------------------------------------------------------------------------
# Arquivos JSON
# ------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------
# Lendo um Arquivo JSON
# ------------------------------------------------------------------------------------


import json


with open('05 - Trabalhando com Arquivos/usuarios.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

    # nome do 2º usuário?
    print(data['usuários'][1]['nome'])  # Douglas

    # permissão na 2ª posição da lista?
    print(data['usuários'][1]['permissões'][1])  # intermediário

    # preço do plano?
    print(data['usuários'][1]['plano']['preco'])  # R$50,00


# ------------------------------------------------------------------------------------
# Criando um Arquivo JSON
# ------------------------------------------------------------------------------------


computador = {
    'marca': 'Dell',
    'preço': 15000,
    'tamanhos': ['pequeno', 'médio', 'grande']
}


# criando o arquivo .json
with open('05 - Trabalhando com Arquivos/computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador, arquivo_json)


# lendo o arquivo .json que foi criado
with open('05 - Trabalhando com Arquivos/computador.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['marca'])  # Dell
    print(data['tamanhos'][1])  # médio
