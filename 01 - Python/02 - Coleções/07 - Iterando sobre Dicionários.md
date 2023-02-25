# Iterando sobre Dicionários

````python
pessoa = {'nome': 'Júlio', 'idade': 32,
          'profissao': 'Programador', 'sexo': 'masculino'}


# Obtendo as CHAVES
print(pessoa.keys())
# dict_keys(['nome', 'idade', 'profissao', 'sexo'])


# Obtendo os VALORES
print(pessoa.values())
# dict_values(['Júlio', 32, 'Programador', 'masculino'])


# Obtendo CHAVES e VALORES
print(pessoa.items())
# dict_items([('nome', 'Júlio'), ('idade', 32), ('profissao', 'Programador'), ('sexo', 'masculino')]


# Iterando sobre um Dicionário (Forma #1)
for item in pessoa.items():
    print(item)
    print(item[1])

# ('nome', 'Júlio')
# Júlio
# ('idade', 32)
# 32
# ('profissao', 'Programador')
# Programador
# ('sexo', 'masculino')
# masculino


# Iterando sobre um Dicionário (Forma #2)
for chave, valor in pessoa.items():
    print(f'Chave = {chave} | Valor = {valor}')

# Chave = nome | Valor = Júlio
# Chave = idade | Valor = 32
# Chave = profissao | Valor = Programador
# Chave = sexo | Valor = masculino
````