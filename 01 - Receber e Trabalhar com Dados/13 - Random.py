# Random


# gera um valor aleatório de 0.0 a 1.0
import random
print(random.random())


# gerando uma saída de VALOR MÍNIMO ao VALOR MÁXIMO com NÚMEROS DECIMAIS
print(random.uniform(4, 10))


# gerando uma saída de de VALOR MÍNIMO ao VALOR MÁXIMO com NÚMEROS INTEIROS
print(round(random.randint(4, 10)))


# selecionamento uma opção aleatória dentro de uma LISTA
times = ['Grêmio', 'Inter', 'São Paulo',
         'Palmeiras', 'Flamengo', 'Atlético PR']
print(random.choice(times))


# selecionamento uma opção aleatória dentro de uma LISTA com MULTIPLAS OPÇÕES
print(random.choices(times, k=3))


# como EMBARALHAR VALORES
cartas = ['carta1', 'carta2', 'carta3', 'carta4', 'carta5']
random.shuffle(cartas)
print(cartas)
