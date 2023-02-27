# Introdução à Funções


### Função SEM PARÂMETROS: 

````python
def dar_boas_vindas():
    print('Seja bem-vindo!!!')  
    # Seja bem-vindo!!!


dar_boas_vindas()
````

### Função COM PARÂMETROS:

````python
def dar_boas_vindas_personalizada(nome):
    print(f'Seja bem-vindo(a) {nome}')  
    # Seja bem-vindo(a) EMANUEL


dar_boas_vindas_personalizada('EMANUEL')
````

### Função com 2 OU MAIS PARÂMETROS:

````python
def cadastro(nome, idade):
    print(f'{nome} possui {idade} anos de idade')
    # EMANUEL possui 36 anos de idade


cadastro('EMANUEL', 36)
````

### Parâmetro com VALOR PADRÃO (opcional):

````python
def apresentar_local(local='Santa Catarina'):
    print(local)


apresentar_local()  # Santa Catarina
apresentar_local('Rio Grande do Sul')  # Rio Grande do Sul
````

### Se temos mais de um parâmetro o VALOR PADRÃO deve ser declarado ao final:

````python
def localizacao(habitantes, cidade='Porto Alegre'):
    print(f'{cidade}: {habitantes} milhões de habitantes')


localizacao(2)  # Porto Alegre: 2 milhões de habitantes
````

### Retornando Dados:

````python
def soma(a, b):
    total = a + b
    return total


resultado = soma(3, 5)
print(resultado) # 8
````