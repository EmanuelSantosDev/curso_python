# ------------------------------------------------------------------------------------
# condicional IF
# ------------------------------------------------------------------------------------


trabalho_terminado = True
if trabalho_terminado == True:
    print('Bora dar uma saída')


# ------------------------------------------------------------------------------------
# condicional ELSE
# ------------------------------------------------------------------------------------


trabalho_terminado = False
if trabalho_terminado == True:
    print('Bora dar uma saída')
else:
    print('Não vai rolar a saída')


# ------------------------------------------------------------------------------------
# condicional ELIF
# ------------------------------------------------------------------------------------


numero_atrasos = 2
if numero_atrasos >= 3:
    print('Vá para a diretoria')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta')
else:
    print('Pode entrar na sala')


# Operando com um RANGE DE VALORES


'''
A velocidade máxima para essa rua é de 50km/h
* Cruzou entre 51 e 60, levou multa de 2 pontos
* Cruzou entre 61 e 75, levou multa de 3 pontos
* Cruzou acima de 75, levou multa de 7 pontos
'''
velocidade = 51
if velocidade <= 50:
    print('Está no limite permitido')
elif velocidade >= 51 and velocidade <= 60:
    print('Tomou 2 pontos na carteira')
elif velocidade >= 61 and velocidade <= 75:
    print('Tomou 3 pontos na carteira')
else:
    print('Tomou 7 pontos na carteira')


# Chaining (encadeamento)


velocidade = 76
if velocidade <= 50:
    print('Está no limite permitido')
elif 51 <= velocidade <= 60:
    print('Tomou 2 pontos na carteira')
elif 61 <= velocidade <= 75:
    print('Tomou 3 pontos na carteira')
else:
    print('Tomou 7 pontos na carteira')
