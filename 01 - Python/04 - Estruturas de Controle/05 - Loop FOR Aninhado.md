# Loop FOR Aninhado


````python
# Loops Aninhados de STRINGS
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


# Loops Aninhados usando a função range()
for x in range(1, 10):
    for y in range(1, 10):
        print(f'{x} + {y} = {x + y}')
'''
1 + 1 = 2
1 + 2 = 3
1 + 3 = 4
1 + 4 = 5
1 + 5 = 6
1 + 6 = 7
1 + 7 = 8
1 + 8 = 9
1 + 9 = 10
2 + 1 = 3
2 + 2 = 4
2 + 3 = 5
2 + 4 = 6
2 + 5 = 7
2 + 6 = 8
2 + 7 = 9
2 + 8 = 10
2 + 9 = 11
3 + 1 = 4
3 + 2 = 5
3 + 3 = 6
3 + 4 = 7
3 + 5 = 8
3 + 6 = 9
3 + 7 = 10
3 + 8 = 11
3 + 9 = 12
4 + 1 = 5
4 + 2 = 6
4 + 3 = 7
4 + 4 = 8
4 + 5 = 9
4 + 6 = 10
4 + 7 = 11
4 + 8 = 12
4 + 9 = 13
5 + 1 = 6
5 + 2 = 7
5 + 3 = 8
5 + 4 = 9
5 + 5 = 10
5 + 6 = 11
5 + 7 = 12
5 + 8 = 13
5 + 9 = 14
6 + 1 = 7
6 + 2 = 8
6 + 3 = 9
6 + 4 = 10
6 + 5 = 11
6 + 6 = 12
6 + 7 = 13
6 + 8 = 14
6 + 9 = 15
7 + 1 = 8
7 + 2 = 9
7 + 3 = 10
7 + 4 = 11
7 + 5 = 12
7 + 6 = 13
7 + 7 = 14
7 + 8 = 15
7 + 9 = 16
8 + 1 = 9
8 + 2 = 10
8 + 3 = 11
8 + 4 = 12
8 + 5 = 13
8 + 6 = 14
8 + 7 = 15
8 + 8 = 16
8 + 9 = 17
9 + 1 = 10
9 + 2 = 11
9 + 3 = 12
9 + 4 = 13
9 + 5 = 14
9 + 6 = 15
9 + 7 = 16
9 + 8 = 17
9 + 9 = 18
'''
````