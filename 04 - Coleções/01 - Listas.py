# ------------------------------------------------------------------------------------
# Listas
# ------------------------------------------------------------------------------------


# como descobrir índice de determinado valor? Função index()
precos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
print(precos.index(30))  # 2


# as listas no Python são dinâmicas (aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Bolacha', 'Café', True, 10.6]
print(itens[4])  # Café


# Maneiras diferentes de se gerar uma lista


# Multiplicação de Valores
lista_de_noves = [9] * 10
lista_de_testes = ['Teste'] * 5
print(lista_de_noves)  # [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
print(lista_de_testes)  # ['Teste', 'Teste', 'Teste', 'Teste', 'Teste']


# Usando o Gerador range(sequência) e a função list()
lista_sequencial = list(range(1, 30, 3))
print(lista_sequencial)  # [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]


# Gerando a partir de Strings
lista_de_caracteres = list('Canoas')
print(lista_de_caracteres)  # ['C', 'a', 'n', 'o', 'a', 's']


# Lista de Lista (MATRIZ)
cadastros = [['Carol', 30], ['Emanuel', 36], ['Paula', 44]]
print(cadastros[1])  # ['Emanuel', 36]
print(cadastros[2][0])  # Paula