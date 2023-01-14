'''
INSTRUÇÕES DA TARTARUGA

forward()
backward()
right()
left()
'''

import turtle

continuar = True

while continuar == True:

    direcao = input('\n\nMovimentar para Frente (f) ou para Trás (t): ')
    pixels = int(input('Quantos pixels movimentar: '))
    rotacionar = input(
        'Rotacionar para Esquerda (e), Direita (d) ou Nenhum (n): ')
    graus = 0 if rotacionar == 'n' else int(
        input('Quantos graus rotacionar: '))

    if direcao == 'f':
        if rotacionar == 'e':
            turtle.left(graus)
        elif rotacionar == 'd':
            turtle.right(graus)
        turtle.forward(pixels)
    else:
        if rotacionar == 'e':
            turtle.left(graus)
        elif rotacionar == 'd':
            turtle.right(graus)
        turtle.backward(pixels)

    opcao = input('\nContinuar (s/n)? ')
    continuar = True if opcao == 's' else False
