# ------------------------------------------------------------------------------------
# Verbos HTTP na Prática
# ------------------------------------------------------------------------------------


# Free fake API:
# https://jsonplaceholder.typicode.com/

# precisaremos da biblioteca "requests":
# pip install requests

# "pprint" é um módulo utilitário para imprimir estruturas de dados de forma legível


import requests
from pprint import pprint


# ------------------------------------------------------------------------------------
# Método GET
# ------------------------------------------------------------------------------------


resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
pprint(resultado_get.json())


# ------------------------------------------------------------------------------------
# Método GET com ID
# ------------------------------------------------------------------------------------


resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_get.json())


# ------------------------------------------------------------------------------------
# Método POST
# ------------------------------------------------------------------------------------


# não precisamos inserir o "id", pois ele será gerado dinamicamente
nova_tarefa = {'completed': False,
               'title': 'Consultando APIs em Python',
               'userId': 1}

resultado_post = requests.post(
    'https://jsonplaceholder.typicode.com/todos', nova_tarefa)

pprint(resultado_post.json())


# ------------------------------------------------------------------------------------
# Método PUT
# ------------------------------------------------------------------------------------


atualizar_tarefa = {'completed': False,
                    'title': 'Construindo um Back-End com Python',
                    'userId': 1}

resultado_put = requests.put(
    'https://jsonplaceholder.typicode.com/todos/2', atualizar_tarefa)

pprint(resultado_put.json())


# ------------------------------------------------------------------------------------
# Método DELETE
# ------------------------------------------------------------------------------------


resultado_delete = requests.delete(
    'https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())
