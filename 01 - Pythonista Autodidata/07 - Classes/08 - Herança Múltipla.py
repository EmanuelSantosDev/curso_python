# ------------------------------------------------------------------------------------
# Herança Múltipla
# ------------------------------------------------------------------------------------


# util para criar novas classes, sem precisar reescrever funcionalidades existentes
# muito útil quando estamos usando classes altamente relacionadas...
# ...e que fazem ou usam as mesmas funcionalidades


class Pessoa:
    nome = 'Pessoa'


class Profissional:
    nome = 'Profissional'


# recebendo herança múltipla
class AtorProfissional(Pessoa, Profissional):
    pass


# a propriedade "nome" se repete nas duas classes acima
# qual vai ser a prioridade do Python quando quisermos imprimir essa propriedade?
print(AtorProfissional.nome)  # Pessoa


# ------------------------------------------------------------------------------------
# MRO (Method Resolution Ordem)
# ------------------------------------------------------------------------------------


# o Python usa algo chamado MRO (Method Resolution Ordem)
# é ele quem define a propriedade ou função que será acessada primeiro
# podemos descobrir qual será a sequência utilizando o método "mro()"


print(AtorProfissional.mro())
# [<class '__main__.AtorProfissional'>,
# <class '__main__.Pessoa'>,
# <class '__main__.Profissional'>,
# <class 'object'>]
