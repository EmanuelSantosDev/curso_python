# Operador de Identidade


Compara a **IDENTIDADE DE UM OBJETO**, isto é, seu endereço na memória:


````python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
print(b is c)  # False
print(b == c)  # True (estamos comparando a igualdade dos valores)
````


## Comparando com o Operador de Igualdade

Verifica se dois **VALORES** são **IGUAIS**:

````python
x = 'Emanuel'
y = 'Emanuel'
z = 'emanuel'

print(x == y)  # True
print(x is y)  # True (para variáveis comuns, o interpretador compara o valor)
print(x == z)  # False
print(x is z)  # False
````