# ------------------------------------------------------------------------------------
# Dicionários
# ------------------------------------------------------------------------------------


# Utiliza o padrão chave:valor
# Utilizados quando precisamos de dados mais estruturados e nomes de propriedades


# utilizanso strings como chave
dicionario_pessoa = {'nome': 'Emanuel', 'idade': 36, 'altura': 1.76}


# utilizando números como chave (pouco recomendado)
dicionario_pessoa_2 = {1: 'Emanuel', 2: 36, 3: 1.76}


# criando um dicionário com o método dict()
dicionario_pessoa_3 = dict(nome='Bianca', idade=23, altura=1.52)


# acessando propriedades do dicionário
print(dicionario_pessoa_3['idade'])  # 23


# descobrindo quais são as PROPRIEDADES disponíveis em um dicionário
print(dicionario_pessoa_3.keys())  # dict_keys(['nome', 'idade', 'altura'])


# descobrindo quais são os VALORES disponíveis em um dicionário
print(dicionario_pessoa_3.values())  # dict_values(['Bianca', 23, 1.52])


# descobrindo quais são ambas as PROPRIEDADES e os VALORES de um dicionário
# nos fornece uma lista com tuplas
# dict_items([('nome', 'Bianca'), ('idade', 23), ('altura', 1.52)])
print(dicionario_pessoa_3.items())


# Iterando sobre um Dicionário
for item in dicionario_pessoa_3.items():
    print(item)
    print(item[1])
# ('nome', 'Bianca')
# Bianca
# ('idade', 23)
# 23
# ('altura', 1.52)
# 1.52
