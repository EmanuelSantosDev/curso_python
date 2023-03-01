# Dictionary Comprehension

````python
from pprint import pprint
import random


# ------------------------------------------------------------------------------------
# {chave:valor + for}
# ------------------------------------------------------------------------------------


produtos = ['Computador', 'Impressora', 'Mesa', 'Cadeira', 'Armário']
dicionario_produtos = {chave: produto for chave, produto in enumerate(produtos, 1)}
pprint(dicionario_produtos)
# {1: 'Computador', 2: 'Impressora', 3: 'Mesa', 4: 'Cadeira', 5: 'Armário'}


# ------------------------------------------------------------------------------------
# {chave: [valor_tipo_lista + for] + for}
# ------------------------------------------------------------------------------------


pprint({produto: [random.randint(1, 100) for i in range(5)] for produto in imobilizado})
"""
{'Armário': [84, 36, 28, 66, 49],
 'Cadeira': [87, 20, 100, 10, 20],
 'Computador': [15, 20, 39, 17, 81],
 'Impressora': [61, 63, 33, 68, 81],
 'Mesa': [90, 3, 71, 53, 2]}
"""
````