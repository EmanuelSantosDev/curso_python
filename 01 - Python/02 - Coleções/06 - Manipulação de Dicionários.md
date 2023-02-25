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
````