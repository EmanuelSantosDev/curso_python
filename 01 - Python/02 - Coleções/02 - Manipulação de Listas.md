# Manipulação de Listas

````python
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2020]


# Adicionar Novo Item ao Final da Lista
valores.append(11)


# Unir Listas (criando uma nova lista)
nova_lista = valores + anos
print(nova_lista)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2020, 2030, 2040, 2020]


# Unir Listas (não cria uma nova lista, ela EXTENDE uma lista existente)
valores.extend(anos)
print(valores)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2020, 2030, 2040, 2020]


# Adicionar um Novo Item Declarando seu Índice
anos.insert(2, 2031)
print(anos)  # [2020, 2030, 2031, 2040, 2020]


# Extraír Item com Base no Índice
valor_extraido = anos.pop(0)
print(anos)  # [2030, 2031, 2040, 2020]
print(valor_extraido)  # 2020


# Remover Item da Lista pelo seu VALOR
anos.remove(2040)
print(anos)  # [2030, 2031, 2020]


# Remover Através do Índice com 'del'
decadas = [2020, 2030, 2040, 2050, 2060, 2070, 2080]
del decadas[2]
print(decadas)  # [2020, 2030, 2050, 2060, 2070, 2080]


# Removendo com 'del' utilizando uma FAIXA DE ÍNDICES
del decadas[1:5]
print(decadas)  # [2020, 2080]


# Contando a Recorrência de Valores
lista_contar = [1, 2, 3, 4, 2, 5, 6, 7, 2, 8, 9, 2]
print(lista_contar.count(2))  # 4


# Resetar uma Lista (excluír todos os seus ítems)
lista_contar.clear()
print(lista_contar)  # []


# all() retorna True se TODOS os itens em um iterável forem True
letras = ['a', 'b', 'c']
todos_iguais = all(letra == letras[0] for letra in letras)
print(todos_iguais)  # False

letras = ['a', 'a', 'a']
todos_iguais = all(letra == letras[0] for letra in letras)
print(todos_iguais)  # True
````