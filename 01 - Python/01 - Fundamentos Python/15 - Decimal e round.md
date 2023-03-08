# Decimal

````python
# O cálculo abaixo gera um resultado impreciso:
print(1.1 + 2.2)  # 3.3000000000000003
````

- O problema da imprecisão está relacionado em como computadores lêem números com casas decimais e os converete para bits.
- Cálculos com grandes cadeias de bits geram eventuais imprecisões.
- O módulo ``decimal`` fornece suporte para uma aritmética rápida e corretamente arredondada de números decimais.
- Em suma, devemos utilizar ``decimal`` quando a precisão é importante.
- ``getcontext().prec`` é um método do módulo ``decimal`` que permite definir e obter a precisão atual dos números decimais em uso no contexto atual.


### Módulo decimal


````python
from decimal import Decimal, getcontext


# neste exemplo o problema está na conversão de float para decimal, pois o float já carrega essa "imprecisão":
print(Decimal(1.1) + Decimal(2.2))  # 3.300000000000000266453525910

# ao converter a partir de string este problema não existe:
print(Decimal('1.1') + Decimal('2.2'))  # 3.3

# definindo a precisão de casas decimais:
getcontext().prec = 4
print(Decimal(1) / Decimal(7))  # 0.1429


# Exemplo #2


x = Decimal('2.5')
y = Decimal('1.5')

z1 = x + y
z2 = x * y
z3 = x / y

print(z1)  # Output: 4.0
print(z2)  # Output: 3.75
print(z3)  # Output: 1.666666666666666666666666667


# Exemplo #3 (utilizando getcontext().prec) 


getcontext().prec = 5

x = Decimal('2.5')
y = Decimal('1.5')

z1 = x + y
z2 = x * y
z3 = x / y

print(z1)  # Output: 4.0
print(z2)  # Output: 3.75
print(z3)  # Output: 1.6667
````

# round()

````python
# alternativamente podemos utilizar o método round():
resultado = 1.1 + 2.2
print(resultado)  # 3.3000000000000003
print(round(resultado, 1))  # 3.3
````