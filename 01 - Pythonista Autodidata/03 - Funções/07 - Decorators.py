# ------------------------------------------------------------------------------------
# Decorators
# ------------------------------------------------------------------------------------


# altera o comportamento da função sem precisar alterar o seu código internamente
# facilita o reuso de código
# as funções são passadas como argumento em outra função e então chamadas dentro...
# ...da função wrapper


from datetime import datetime


def calcular_tempo_de_duracao(funcao):
    def wrapper(a, b):
        inicio = datetime.now()
        funcao(a, b)
        fim = datetime.now()
        duracao = fim - inicio
        print(f'Tempo de Duração => {duracao}')
    return wrapper


@calcular_tempo_de_duracao
def somar_e_calcular_tempo(a, b):
    print(a + b)


somar_e_calcular_tempo(5, 10)
# 15
# Tempo de Duração => 0:00:00.000997
