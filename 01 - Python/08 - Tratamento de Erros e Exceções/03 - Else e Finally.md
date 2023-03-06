# Else e Finally


- o bloco ``else`` irá ocorrer se o código rodar sem excessões
- o bloco ``finally`` irá ocorrer idependente de ter ocorrido excessão ou não


````python
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
````