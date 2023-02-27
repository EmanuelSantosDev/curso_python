# Leitura Básica de Arquivo


- ao abrir um arquivo, devemos lembrar de fechá-lo
- se não fecharmos, pode dar algum erro e o arquivo permanecer aberto no sistema


````python
arquivo = open('pessoas.csv', encoding='utf-8')
dados = arquivo.read()
arquivo.close()

# splitlines() divide uma string em uma lista onde cada linha é um item da lista
for registro in dados.splitlines():
    print('Nome: {} Idade: {}'.format(*registro.split(',')))

if arquivo.closed:
    print('Arquivo Fechado')

"""
Nome: Maria Idade: 45
Nome: João Idade: 33
Nome: Pedro Idade: 63
Nome: Ana Idade: 21
Nome: Bia Idade: 40
Nome: Carlos Idade: 14

Arquivo Fechado
"""
````