# Loops Aninhados


# Loops Aninhas de STRINGS
paises_america_sul = ['Brasil', 'Argentinha', 'Chile', 'Colômbia']
estacoes_do_ano = ['Verão', 'Inverno', 'Outono', 'Primavera']

for pais in paises_america_sul:
    for estacao in estacoes_do_ano:
        print(f'{pais} => {estacao}')
'''
Brasil => Verão
Brasil => Inverno
Brasil => Outono
Brasil => Primavera
Argentinha => Verão
Argentinha => Inverno
Argentinha => Outono
Argentinha => Primavera
Chile => Verão
Chile => Inverno
Chile => Outono
Chile => Primavera
Colômbia => Verão
Colômbia => Inverno
Colômbia => Outono
Colômbia => Primavera
'''


# Loops Aninhados de RANGE
for x in range(1, 6):
    for y in range(1, 11):
        print(f'x = {x} | y = {y}')
'''
x = 1 | y = 1
x = 1 | y = 2
x = 1 | y = 3
x = 1 | y = 4
x = 1 | y = 5
x = 1 | y = 6
x = 1 | y = 7
x = 1 | y = 8
x = 1 | y = 9
x = 1 | y = 10
x = 2 | y = 1
x = 2 | y = 2
x = 2 | y = 3
x = 2 | y = 4
x = 2 | y = 5
x = 2 | y = 6
x = 2 | y = 7
x = 2 | y = 8
x = 2 | y = 9
x = 2 | y = 10
x = 3 | y = 1
x = 3 | y = 2
x = 3 | y = 3
x = 3 | y = 4
x = 3 | y = 5
x = 3 | y = 6
x = 3 | y = 7
x = 3 | y = 8
x = 3 | y = 9
x = 3 | y = 10
x = 4 | y = 1
x = 4 | y = 2
x = 4 | y = 3
x = 4 | y = 4
x = 4 | y = 5
x = 4 | y = 6
x = 4 | y = 7
x = 4 | y = 8
x = 4 | y = 9
x = 4 | y = 10
x = 5 | y = 1
x = 5 | y = 2
x = 5 | y = 3
x = 5 | y = 4
x = 5 | y = 5
x = 5 | y = 6
x = 5 | y = 7
x = 5 | y = 8
x = 5 | y = 9
x = 5 | y = 10
'''
