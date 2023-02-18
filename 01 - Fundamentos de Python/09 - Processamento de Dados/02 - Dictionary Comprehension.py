# ------------------------------------------------------------------------------------
# Dictionary Comprehension
# ------------------------------------------------------------------------------------


from pprint import pprint
import random


# ------------------------------------------------------------------------------------
# {chave: expressão for membro in iterável}
# ------------------------------------------------------------------------------------


pprint({i: i for i in range(1, 6)})
"""
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
"""


# ------------------------------------------------------------------------------------
# Popular um Dicionário com Valores Utilizando outra Lista como Base
# ------------------------------------------------------------------------------------


produtos = ['Computador', 'Impressora', 'Mesa', 'Cadeira', 'Armário']
dicionario_produtos = {chave: produto for chave,
                       produto in enumerate(produtos, 1)}
pprint(dicionario_produtos)
# {1: 'Computador', 2: 'Impressora', 3: 'Mesa', 4: 'Cadeira', 5: 'Armário'}


# ------------------------------------------------------------------------------------
# Gerando uma Matriz de Valores
# ------------------------------------------------------------------------------------


imobilizado = ['Computador', 'Impressora', 'Mesa', 'Cadeira', 'Armário']
pprint({produto: [i for i in range(1, 6)] for produto in imobilizado})
"""
{'Armário': [1, 2, 3, 4, 5],
 'Cadeira': [1, 2, 3, 4, 5],
 'Computador': [1, 2, 3, 4, 5],
 'Impressora': [1, 2, 3, 4, 5],
 'Mesa': [1, 2, 3, 4, 5]}
"""

# ------------------------------------------------------------------------------------
# Variação do Exemplo Anterior
# ------------------------------------------------------------------------------------


pprint({produto: [2 * i for i in range(1, 6)] for produto in imobilizado})
"""
{'Armário': [2, 4, 6, 8, 10],
 'Cadeira': [2, 4, 6, 8, 10],
 'Computador': [2, 4, 6, 8, 10],
 'Impressora': [2, 4, 6, 8, 10],
 'Mesa': [2, 4, 6, 8, 10]}
"""


# ------------------------------------------------------------------------------------
# Variação do Exemplo Anterior Gerando Valores Aleatórios
# ------------------------------------------------------------------------------------


pprint({produto: [random.randint(1, 100) for i in range(5)]
       for produto in imobilizado})
"""
{'Armário': [84, 36, 28, 66, 49],
 'Cadeira': [87, 20, 100, 10, 20],
 'Computador': [15, 20, 39, 17, 81],
 'Impressora': [61, 63, 33, 68, 81],
 'Mesa': [90, 3, 71, 53, 2]}
"""
