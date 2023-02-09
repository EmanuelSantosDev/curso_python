# ------------------------------------------------------------------------------------
# Recebendo Dados do Usuário
# ------------------------------------------------------------------------------------


senha = input('Digite a sua senha: ')
print(f'Você digitou {senha}')


# a senha será sempre do tipo STRING
print(type(senha))  # <class 'str'>


# convertendo de STRING para INTEIRO
quantidade = int(input('Quantos filmes você já viu este mês? '))
print(type(quantidade))  # <class 'int'>
