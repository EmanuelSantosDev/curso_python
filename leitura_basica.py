# Leitura Stream

# leitura de arquivo sobre demanda (Stream)
# podemos fazer analogia do YouTube, que faz o envio do vídeo em partes (Streaming)
# ao invés de salvar todos os dados em uma variável que ficará ocupando espaço na memória do computador

arquivo = open('pessoas.csv', encoding='utf-8')

for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')), end='')

arquivo.close()

"""
Nome: Maria Idade: 45
Nome: João Idade: 33
Nome: Pedro Idade: 63
Nome: Ana Idade: 21
Nome: Bia Idade: 40
Nome: Carlos Idade: 14
"""
