# ------------------------------------------------------------------------------------
# Funções são Objetos de Primeira Classe
# ------------------------------------------------------------------------------------


# Significa que uma função é um objeto e pode ser tratada como os demais objetos:
# >>>>> armazenar a função em uma variável.
# >>>>> passar a função como um parâmetro para outra função.
# >>>>> retornar a função de uma função.
# >>>>> armazená-los em estruturas de dados, como tabelas de hash, listas…


# ------------------------------------------------------------------------------------
# EXEMPLO 1: Armazenando uma Função em uma Variável
# ------------------------------------------------------------------------------------


def shout(text):
    return text.upper()


print(shout('Hello'))  # HELLO
yell = shout
print(yell('Hello'))  # HELLO


# ------------------------------------------------------------------------------------
# EXEMPLO 2: Passando a Função como um Argumento
# ------------------------------------------------------------------------------------


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    greeting = func('Hi, I am created by a function passed as an argument.')
    print(greeting)


greet(shout)
# HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.

greet(whisper)
# hi, i am created by a function passed as an argument.


# ------------------------------------------------------------------------------------
# EXEMPLO 3: Retornando Funções de Outra Função
# ------------------------------------------------------------------------------------


def create_adder(x):
    def adder(y):
        return x+y
    return adder


add_15 = create_adder(15)
print(add_15(10))  # 25
