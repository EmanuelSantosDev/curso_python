# Escrita com Bloco WITH

````python
with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    with open('pessoas.txt', 'w', encoding='utf-8') as saida:
        for registro in arquivo:
            saida.write(registro)

if arquivo.closed:
    print('Arquivo Fechado')  # Arquivo Fechado
````