# 16 - Trabalhando com Arquivos


'''
COMO CRIAR E MODIFICAR ARQUIVOS

'r' -> usado para LER algo
'w' -> usado para ESCREVER algo (iniciar um novo arquivo)
'r+' -> para LER e ESCREVER algo
'a' -> usado para acrescentar algo
'''


import os


with open('celulares.txt', 'w') as meu_arquivo:
    meu_arquivo.write('Celular 1')
