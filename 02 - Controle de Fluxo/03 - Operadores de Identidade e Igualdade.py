# ------------------------------------------------------------------------------------
# Operador 'is'
# comparar a IDENTIDADE DE UM OBJETO, isto é, seu endereço na memória:
# ------------------------------------------------------------------------------------


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
print(b is c)  # False
print(b == c)  # True (estamos comparando a igualdade dos valores)


# ------------------------------------------------------------------------------------
# Operador '=='
# verifica se os VALORES são IGUAIS:
# ------------------------------------------------------------------------------------


x = 'Emanuel'
y = 'Emanuel'
z = 'emanuel'

print(x == y)  # True
print(x is y)  # True (otimização interna do interpretador Python)
print(x == z)  # False
print(x is z)  # False
