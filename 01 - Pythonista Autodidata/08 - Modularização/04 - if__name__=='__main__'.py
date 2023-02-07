# ------------------------------------------------------------------------------------
# if__name__=="__main__"
# ------------------------------------------------------------------------------------


# O conteúdo da estrutura if __name__=="__main__" será ativado somente quando...
# ...estiver sendo executado o próprio módulo que o contém, sem importação.
# Ao rodar um arquivo em Python ele automaticamente define a variável __name__...
# ...que é uma variável reservada do Python.
# Quando fazemos uma execução direta no próprio módulo ele atribui o valor...
# ...“__main__” para essa variável, caso contrário ela vai receber o nome do módulo.
# É util para a checagem de escopo de execução.
# Uma aplicação útil pra esse conceito é quando há um módulo Python que é tanto...
# ...executado de forma independente quanto importado por outro módulo.
# Também útil para testes unitários de módulos, impedindo que certas ações sejam...
# ...executadas quando este mesmo módulo é importado por outro módulo.


from app import imprimir_nome

imprimir_nome()

if __name__ == "__main__":
    print('Estou rodando a partir do arquivo principal')
    print(f'Estamos no arquivo {__name__}')  # Estamos no arquivo __main__
