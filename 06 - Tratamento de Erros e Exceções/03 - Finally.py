# ------------------------------------------------------------------------------------
# Finally
# ------------------------------------------------------------------------------------


'''
- há casos em que mesmo que uma excessão seja tratada, uma lógica
  precisa ser realizada após o erro ocorrer
'''

# Exemplo 1


internet = None
try:
    print('Fazendo conexão com a ' + internet)
except TypeError as erro:
    print('Não há conexão com a Internet')
finally:
    print('Desfazendo a compra')


# Exemplo 2 (tratando multiplas excessões)


try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('Não é possivel dividir por zero')
except ValueError as erro:
    print('Favor digitar apenas números')
finally:
    print('A operação foi cancelada')
