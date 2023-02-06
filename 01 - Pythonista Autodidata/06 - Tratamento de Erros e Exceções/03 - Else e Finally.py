# ------------------------------------------------------------------------------------
# Else e Finally
# ------------------------------------------------------------------------------------


# o bloco "else" irá ocorrer se o código rodar sem excessões
# o bloco "finally" irá ocorrer idependente de ter ocorrido excessão ou não


# Exemplo 1


internet = 'internet'
try:
    print('Fazendo conexão com a ' + internet)
except TypeError as erro:
    print('Não há conexão com a Internet')
else:
    print('Conexão estabelecida com sucesso!')
finally:
    print('Encerrando o Programa')
# Fazendo conexão com a internet
# Conexão estabelecida com sucesso!
# Encerrando o Programa


# Exemplo 2 (tratando multiplas excessões)


try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('Não é possivel dividir por zero')
except ValueError as erro:
    print('Favor digitar apenas números')
else:
    print('Conexão estabelecida com sucesso!')
finally:
    print('Encerrando o Programa')
# Digite um valor: 2
# Não é possivel dividir por zero
# Encerrando o Programa