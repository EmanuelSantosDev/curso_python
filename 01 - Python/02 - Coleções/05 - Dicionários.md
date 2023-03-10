# Dicionários


- Utiliza o padrão ``chave:valor``
- É indexada através de strings e números (este último pouco recomendado)
- Utilizados quando precisamos de dados mais estruturados e nomes de propriedades

````python
# utilizando strings como chave
cadastro = {'nome': 'Emanuel', 'idade': 36, 'altura': 1.76}
 

# criando um dicionário com o método dict()
pessoa = dict(nome='Bianca', idade=23, altura=1.52)


# acessando propriedades do dicionário
print(pessoa['idade'])  # 23
print(pessoa.get('idade'))  # 23


# retornando um valor default em caso de erro
print(pessoa.get('tags', 'chave indisponível'))  # chave indisponível
````