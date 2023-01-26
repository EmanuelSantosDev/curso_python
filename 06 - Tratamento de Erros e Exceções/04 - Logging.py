# ------------------------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------------------------


'''
É uma forma de registrar o que aconteceu e o que está acontecendo na aplicação.

Níveis de Logging:

-> 'debug' - passar informações para os desenvolvedores.
-> 'info' - informar algo que está acontecendo, mas que não é um erro.
-> 'warning' - alertar sobre algo, possivelmente fora do esperado, porém,
   ainda não é um erro, mas pode gerar futuramente.
-> 'error' - um erro que aconteceu na aplicação. 
-> 'critical' - um erro com consequências graves.

Os níveis de logging são uma maneira mais organizada de guardar informações de texto 
dentro da aplicação.

Por padrão irá exibir apenas as mensagens do nível 'warning' para cima. Para
alterarmos o nível padrão, utilizamos o 'basicConfig'.

'level' é o que defini o nível mínimo de logging para que a mensagem seja
impressa no terminal
'''


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
