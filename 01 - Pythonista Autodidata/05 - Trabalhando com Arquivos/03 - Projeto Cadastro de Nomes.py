# ------------------------------------------------------------------------------------
# Projeto Cadastro de Nomes
# ------------------------------------------------------------------------------------


import os

with open('nomes.txt', 'a', newline='', encoding='utf-8') as arquivo:
    arquivo.write('')

continuar = True

while continuar == True:
    print('')
    nome_digitado = input('Digite o Nome: ')
    encontrou = False
    with open('nomes.txt', 'r+', newline='', encoding='utf-8') as arquivo:
        for nome in arquivo:
            nome_editado = nome.strip()
            if nome_editado == nome_digitado:
                print(f'Encontrei o nome digitado => {nome_digitado}')
                encontrou = True
                break

        if encontrou == False:
            print(
                f'O nome {nome_digitado} não foi encontrado. Incluido no arquivo')
            arquivo.write(nome_digitado + os.linesep)

    continuar = True if input(
        'Deseja Continuar ("N" para sair)? ') != 'N' else False
