# ------------------------------------------------------------------------------------
# if__name__=="__main__"
# ------------------------------------------------------------------------------------


# O conteúdo dentro da estrutura if__name__=="__main__" será executado quando...
# ...estiver sendo executado o próprio arquivo, sem importação.
# Ao rodar um arquivo em Python ele automaticamente define a variável __name__...
# ...que é uma variável reservada do Python.
# Quando fazemos uma execução direta no próprio arquivo ele atribui o valor...
# ...“__main__” para essa variável, caso contrário ela vai receber o nome do arquivo.
# É util para a checagem de escopo de execução


from app import imprimir_nome

imprimir_nome()

if __name__ == "__main__":
    print('Estou rodando a partir do arquivo principal')
    print(f'Estamos no arquivo {__name__}')  # Estamos no arquivo __main__
