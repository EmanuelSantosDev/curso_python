# Acrescentando Informações com Bloco WITH

````python
cadastros = ['Roberto,45', 'Flávio,38', 'Neymar,29']

with open('pessoas.txt', 'a', encoding='utf-8') as arquivo:
    for cadastro in cadastros:
        arquivo.write(f'\n{cadastro}')

if arquivo.closed:
    print('Arquivo Fechado')  # Arquivo Fechado
````