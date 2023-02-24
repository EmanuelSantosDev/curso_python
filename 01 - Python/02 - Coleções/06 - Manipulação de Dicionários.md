# Manipulação de Dicionários

````python
# manipulação de listas dentro de dicionários
professor = {'nome': 'Alberto', 'idade': 42, 'cursos': ['React', 'Python']}
professor['cursos'].append('JavaScript')
print(professor) 
# {'nome': 'Alberto', 'idade': 42, 'cursos': ['React', 'Python', 'JavaScript']}


# adicionando novos items ao dicionário
professor.update({'sexo': 'masculino', 'universidade': 'Unilasalle'})
print(professor)
# {'nome': 'Alberto', 'cursos': ['React', 'Python', 'JavaScript'],
# 'sexo': 'masculino', 'universidade': 'Unilasalle'}


# lendo um dicionário e deletando items
item_removido = professor.pop('idade')
print(item_removido)
# 42
print(professor)
# {'nome': 'Alberto', 'cursos': ['React', 'Python', 'JavaScript']}


# deletando items
del professor['cursos']
print(professor)
# {'nome': 'Alberto', 'sexo': 'masculino', 'universidade': 'Unilasalle'}


# obtendo as CHAVES disponiveis no dicionário
print(pessoa.keys())  # dict_keys(['nome', 'idade', 'altura'])


# obtendo os VALORES disponíveis no dicionário
print(pessoa.values())  # dict_values(['Bianca', 23, 1.52])


# obtendo CHAVES e VALORES disponíveis no dicionário
print(pessoa.items())
# dict_items([('nome', 'Bianca'), ('idade', 23), ('altura', 1.52)])


# Iterando sobre um Dicionário
for item in pessoa.items():
    print(item)
    print(item[1])
    
# ('nome', 'Bianca')
# Bianca
# ('idade', 23)
# 23
# ('altura', 1.52)
# 1.52
````