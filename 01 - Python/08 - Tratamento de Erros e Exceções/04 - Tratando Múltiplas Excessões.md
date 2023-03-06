# Tratando Múltiplas Excessões


````python
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
````