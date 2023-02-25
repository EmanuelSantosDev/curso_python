# Loop While


````python
# loop CRESCENTE
repeticoes = 0
while repeticoes < 5:
    print(f'Repetiçao => {repeticoes + 1}')
    repeticoes += 1
'''
Repetiçao => 1
Repetiçao => 2
Repetiçao => 3
Repetiçao => 4
Repetiçao => 5
'''


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


# repetir enquanto uma condição não for satisfeita
senha = ''
while senha != 1234:
    senha = int(input('Digite sua senha: '))
print('LOGIN EFETUADO COM SUCESSO')
````