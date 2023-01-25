# ------------------------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------------------------


'''
É uma forma de registrar o que aconteceu e o que está acontecendo na aplicação

Níveis de Logging:

-> 'debug' - passar informações para os desenvolvedores.
-> 'info' - informar algo que está acontecendo, mas que não é um erro.
-> 'warning' - alertar sobre algo, possivelmente fora do esperado, porém,
   ainda não é um erro, mas pode gerar futuramente.
-> 'error' - um erro que aconteceu na aplicação. 
-> 'critical' - um erro com consequências graves.

Os níveis de logging não irão gerar excessões ou tratamento de excessões. Elas 
são apenas uma maneira mais organizada de guardar informações de texto dentro
da aplicação.

Mensagem que irá aparecer no terminal:

-> "nivel do logging + quem chamou este logging + mensagem"

Por padrão irá exibir apenas as mensagens do nível 'warning' para cima. Para
alterarmos o nível padrão, utilizamos o 'basicConfig'.
'''


import logging


# configurando o nível padrão e o registro em arquivo
logging.basicConfig(level=logging.DEBUG, filename='06 - Tratamento de Erros e Exceções/app.log',
                    filemode='a', format='%(levelname)s - %(message)s - %(asctime)s', encoding='utf-8')


logging.debug('Logging nível debug')
# não iria aparece a mensagem se não tivéssemos utilizado o 'basicConfig'
# DEBUG:root:Logging nível debug

logging.info('Logging nível info')
# não iria aparece a mensagem se não tivéssemos utilizado o 'basicConfig'
# INFO:root:Logging nível info

logging.warning('Logging nível warning')
# WARNING:root:Logging nível warning

logging.error('Logging nível error')
# ERROR:root:Logging nível error

logging.critical('Logging nível critical')
# CRITICAL:root:Logging nível critico
