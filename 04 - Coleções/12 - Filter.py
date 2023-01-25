# ------------------------------------------------------------------------------------
# Filter
# ------------------------------------------------------------------------------------


'''
- processa uma coleção de dados e retorna APENAS os items que 
  são avaliados como TRUE
'''


nomes = ['Rafael', 'João', 'Renato', 'Emanuel', 'Ruan']


def nome_comeca_com_a_letra_r(nome):
    if nome[0] == 'R':
        return True
    else:
        return False


nomes_com_r = list(filter(nome_comeca_com_a_letra_r, nomes))
print(nomes_com_r)  # ['Rafael', 'Renato', 'Ruan']
