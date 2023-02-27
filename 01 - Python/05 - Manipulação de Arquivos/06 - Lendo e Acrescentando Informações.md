# Lendo e Acrescentando Novas Informações com Bloco WITH

````python
cadastros = ['Pikachu,12', 'Charmander,9', 'Squirtle,8']

with open('pessoas.txt', 'r+', encoding='utf-8') as arquivo:
    # leitura dos cadastros
    for cadastro in arquivo:
        print(cadastro.strip())
    # incluindo novos cadastros
    for novo_cadastro in cadastros:
        arquivo.write(f'\n{novo_cadastro}')

if arquivo.closed:
    print('Arquivo Fechado')  # Arquivo Fechado
````