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
