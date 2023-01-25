# ------------------------------------------------------------------------------------
# Loop While
# ------------------------------------------------------------------------------------


# utilizando um contador
tentativas = 0
while tentativas < 3:
    print('Tente Novamente')
    tentativas += 1
'''
Tente Novamente
Tente Novamente
Tente Novamente
'''


# repetir enquanto uma condição não for satisfeita
senha = ''
while senha != 1234:
    senha = int(input('Digite sua senha: '))
print('LOGIN EFETUADO COM SUCESSO')


# repetir enquanto o usuário não preencher o dado solicitado
nome = ''
while nome == '':
    nome = input('Digite seu nome: ')
    if nome == '':
        print('DADO NÃO DIGITAVO. Tente novamente...')
print(f'{nome.upper()} seu cadastro foi REALIZADO COM SUCESSO!!!')


# loop DECRESCENTE
contador = 10
while contador >= 0:
    print(f'Contagem Regressiva: {contador}')
    contador -= 1
'''
Contagem Regressiva: 10
Contagem Regressiva: 9
Contagem Regressiva: 8
Contagem Regressiva: 7
Contagem Regressiva: 6
Contagem Regressiva: 5
Contagem Regressiva: 4
Contagem Regressiva: 3
Contagem Regressiva: 2
Contagem Regressiva: 1
Contagem Regressiva: 0
'''
