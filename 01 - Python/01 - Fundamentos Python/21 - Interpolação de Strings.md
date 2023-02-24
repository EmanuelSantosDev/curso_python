# Interpolação de Strings

````python
from string import Template

nome, idade, altura = 'Ana', 32, 1.76

print('Nome: %s Idade: %d Altura: %.2f' % (nome, idade, altura))
# Nome: Ana Idade: 32 Altura: 1.76

print('Nome: {0} Idade: {1} Altura: {2}'.format(nome, idade, altura))
# Nome: Ana Idade: 32 Altura: 1.76

print(f'Nome: {nome} Idade: {idade} Altura: {altura}')
# Nome: Ana Idade: 32 Altura: 1.76

meu_template = Template('Nome: $nome Idade: $idade Altura: $altura')
print(meu_template.substitute(nome=nome, idade=idade, altura=altura))
# Nome: Ana Idade: 32 Altura: 1.76
````