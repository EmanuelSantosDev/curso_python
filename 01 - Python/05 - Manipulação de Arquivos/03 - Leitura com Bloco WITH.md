# Leitura com Bloco WITH

Facilita o trabalho com arquivos, pois fecha o mesmo automaticamente.


### OBJETIVOS AO ABRIR O ARQUIVO


|Objetivo|Ação|
|:---:|---|
|``w``|usado para ESCREVER um novo arquivo ou SOBRESCREVER caso já exista |
|``a``|usado para ACRESCENTAR informação à um arquivo|
|``r``|usado para LER um arquivo|
|``r+``|usado para LER e ESCREVER no arquivo|


````python
with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo Fechado')

# Nome: Maria Idade: 45
# Nome: João Idade: 33
# Nome: Pedro Idade: 63
# Nome: Ana Idade: 21
# Nome: Bia Idade: 40
# Nome: Carlos Idade: 14
# Arquivo Fechado
````
