# ============================================================================​=
# PROJETO #1
# =========​===================================================================​=

# Objetivo de projeto:
# Estamos criando um módulo de login do nosso aplicativo, e você
# deve obter as seguintes informações do funcionário:

# =============================================================================
# MÓDULO 1 - GERAR REGISTRO DO FUNCIONÁRIO
# =============================================================================

# 1. Obtenha o nome do usuário

# 2. Obtenha a idade do usuário

# 3. Registre de forma automática a data do cadastro do usuário,
#    usando a data do registro como data de registro

# 4. Para cada novo funcionário que é registrado na empresa, ele
#    recebe um dos seguintes cartões, que é sorteado de forma aleatória:
#    cartoes = ['R$50,00','R$250,00','R$120,00']

# 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)

# =============================================================================
# MÓDULO 2 - GERAR APRESENTAÇÃO DO USUÁRIO
# =============================================================================

# Usando os dados obtidos no módulo 1, exiba as seguintes informações:

# Olá (nome do usuário), seu registro foi concluído com sucesso no dia
# (data de cadastro no formato dd/mm/aaaa).
# Parabéns, houve um sorteio e você ganhou um cartão de compras no valor
# de (valor sorteado).

from datetime import datetime
import random

# data do cadastro
dia = datetime.now().day
mes = datetime.now().month
ano = datetime.now().year

# obtendo os dados do usuário
nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))
data_aniversario = datetime.strptime(
    input('Data de Aniversário: '), '%d/%m/%Y')

# sorteio do cartão
cartoes = ['R$ 50,00', 'R$ 250,00', 'R$ 120,00']
cartao = random.choice(cartoes)

# imprimindo a mensagem na tela

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {dia}/{mes}/{ano}. \nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}.')
