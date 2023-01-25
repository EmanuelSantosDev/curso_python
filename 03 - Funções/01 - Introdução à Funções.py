# ------------------------------------------------------------------------------------
# Funções
# ------------------------------------------------------------------------------------


# Função SEM PARÂMETROS
def dar_boas_vindas():
    print('Seja bem-vindo!!!')


dar_boas_vindas()


# Função COM PARÂMETROS
def dar_boas_vindas_personalizada(nome):
    print(f'Seja bem-vindo(a) {nome}')


dar_boas_vindas_personalizada('EMANUEL')


# Função COM 2 OU MAIS PARÂMETROS
def cadastro(nome, idade):
    print(f'{nome} possui {idade} anos de idade')


cadastro('EMANUEL', 36)


# Passando um Parâmetro com VALOR PADRÃO
def apresentar_local(local='Santa Catarina'):
    print(local)


apresentar_local()  # Santa Catarina
apresentar_local('Rio Grande do Sul')  # Rio Grande do Sul


# Se temos mais de um parâmetro o VALOR PADRÃO deve ser declarado ao final
def localizacao(habitantes, cidade='Porto Alegre'):
    print(f'{cidade}: {habitantes} milhões de habitantes')


localizacao(2)  # Porto Alegre: 2 milhões de habitantes
