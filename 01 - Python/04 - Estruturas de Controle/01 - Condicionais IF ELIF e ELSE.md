# Condicionais IF, ELIF e ELSE

### Condicional IF

````python
trabalho_terminado = True

if trabalho_terminado == True:
    print('Bora dar uma saída')
````

### Condicional ELSE

````python
trabalho_terminado = False

if trabalho_terminado == True:
    print('Bora dar uma saída')
else:
    print('Não vai rolar a saída')
````

### Condicional ELIF

````python
numero_atrasos = 2

if numero_atrasos >= 3:
    print('Vá para a diretoria')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta')
elif numero_atrasos == 1:
    print('Essa é sua primeira falta')
else:
    print('Pode entrar na sala')
````

### Operando com um RANGE DE VALORES


````python
velocidade = 51

if velocidade <= 50:
    print('Está no limite permitido')
elif velocidade >= 51 and velocidade <= 60:
    print('Tomou 2 pontos na carteira')
elif velocidade >= 61 and velocidade <= 75:
    print('Tomou 3 pontos na carteira')
else:
    print('Tomou 7 pontos na carteira')
````