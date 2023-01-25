# ------------------------------------------------------------------------------------
# Mantendo um Log de Exceções
# ------------------------------------------------------------------------------------


import logging


logging.basicConfig(level=logging.DEBUG, filename='06 - Tratamento de Erros e Exceções/cadastro.log',
                    filemode='a', format='%(levelname)s - %(message)s - %(asctime)s', encoding='utf-8')


try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha: '))
    # simulando uma consulta ao banco de dados
    if senha == 1234:
        print('Login realizado com sucesso')
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('Digite apenas números')
    logging.info(erro)
