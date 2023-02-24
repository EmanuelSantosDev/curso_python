# Decimal

````python
# esse cálculo gera um resultado impreciso:
print(1.1 + 2.2)  # 3.3000000000000003
````

- O problema da imprecisão está relacionado em como computadores lêem números com casas decimais e os converete para bits.
- Cálculos com grandes cadeias de bits geram eventuais imprecisões.
- O módulo ``decimal`` fornece suporte para uma aritmética rápida e corretamente arredondada de números decimais.
- Em suma, devemos utilizar ``decimal`` quando a precisão é importante.

## Módulo decimal


````python
from decimal import Decimal, getcontext

# o problema real é a conversão de float para decimal, pois o float já possui uma "imprecisão":
print(Decimal(1.1) + Decimal(2.2))  # 3.300000000000000266453525910

# ao converter a partir de string este problema não existe:
print(Decimal('1.1') + Decimal('2.2'))  # 3.3

# definindo a precisão de casas decimais:
getcontext().prec = 4
print(Decimal(1) / Decimal(7))  # 0.1429
````

# round()

````python
# alternativamente podemos utilizar o método round():
resultado = 1.1 + 2.2
print(round(resultado, 2))  # 3.3
````