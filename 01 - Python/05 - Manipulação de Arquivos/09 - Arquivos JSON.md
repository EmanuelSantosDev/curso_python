# Arquivos JSON


- ``json.load()`` é uma função que lê e decodifica um arquivo JSON e retorna um objeto Python.
- ``json.dump()`` grava os dados JSON em um arquivo ou stream.
- ``json.dumps()`` retorna uma string contendo a representação JSON do objeto Python.


### Lendo um Arquivo JSON


````python
import json


with open('usuarios.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

    # nome do 2º usuário?
    print(data['usuários'][1]['nome'])  # Douglas
````


### Criando um Arquivo JSON com json.dump()


````python
import json


computador = {
    'marca': 'Dell',
    'preço': 15000,
    'tamanhos': ['pequeno', 'médio', 'grande']
}


# criando o arquivo .json
with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador, arquivo_json)
````


### Transformando um Objeto Pythom em uma String JSON com json.dumps()


````python
import json


cadastro = {
    'nome': 'Lucas Silva',
    'idade': 23,
    'habilidades': [
        'Programação',
        'Planilhas Excel',
        'Digitação'
    ],
    'carteira_de_habilitacao': True
}

formato_json = json.dumps(cadastro, indent=4)
print(formato_json)

"""
{
    "nome": "Lucas Silva",
    "idade": 23,
    "habilidades": [
        "Programa\u00e7\u00e3o",
        "Planilhas Excel",
        "Digita\u00e7\u00e3o"
    ],
    "carteira_de_habilitacao": true
}
"""
````