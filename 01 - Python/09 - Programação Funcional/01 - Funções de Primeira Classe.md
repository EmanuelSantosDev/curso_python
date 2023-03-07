# Funções de Primeira Classe


- A partir do momento que eu tenho duas funções, o Python permite que eu trate estas funções como se fossem dados.
- Podemos, por exemplo, armazenar funções dentro de uma lista.


````python
def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


# Armazenando Funções em Variáveis


d = dobro
print(d(5))  # 10


q = quadrado
print(q(5))  # 25


# Armazenando Funções em uma Lista


funcoes = [dobro, quadrado] * 5
for funcao, numero in zip(funcoes, range(1, 11)):
    print(f'O {funcao.__name__} de {numero} é {funcao(numero)}')

# O dobro de 1 é 2
# O quadrado de 2 é 4
# O dobro de 3 é 6
# O quadrado de 4 é 16
# O dobro de 5 é 10
# O quadrado de 6 é 36
# O dobro de 7 é 14
# O quadrado de 8 é 64
# O dobro de 9 é 18
# O quadrado de 10 é 100
````