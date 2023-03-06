# String

Uma string é uma cadeia de caracteres **imutável** onde podemos:
- acessar seus valores individualmente através dos índices.
- atribuir um novo valor para o conteúdo da variável.
- mas não podemos alterar o valor da string propriamente dita.

````python
nome = 'Saulo Pedro'

print(nome[0])  # S
nome[0] = 'P'  # (TypeError: 'str' object does not support item assignment)
````

### Caracteres de Escape

````python
# não interpreta as aspas internas
print('Dias D\'ávila')  # Dias D'ávila

# mesclando aspas (') com aspas ("") - exemplo #1
print("Dias D'ávila")  # Dias D'ávila

# Escape mesclando aspas (') com aspas ("") - exemplo #2
print('Texto entre apóstrofos pode ter "aspas"')  
# Texto entre apóstrofos pode ter "aspas"
````

### Texto com Múltiplas Linhas

````python
# Forma #1 (aspas triplas)
print('''Sou um texto
com múltiplas linhas''')

# Forma #2 (\n)
print('''Sou um texto \ncom múltiplas linhas''')
````