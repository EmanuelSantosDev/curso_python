# ------------------------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------------------------


"""
Log é uma forma de registrar o que aconteceu e o que está acontecendo na aplicação.

Os níveis de logging são uma maneira mais organizada de guardar informações de texto 
dentro da aplicação.

NÍVEIS DE LOGGING:

    "logging.debug"
    Passar informações para os desenvolvedores a fim de diagnosticar problemas.

    "logging.info"
    Informar que as coisas estão acontencendo como esperado.

    "logging.warning"
    Alertar sobre algo fora do esperado, porém, ainda não é um erro, mas pode gerar 
    um futuramente. É muito utilizado pelas bibliotecas quando se faz a sua instalação.

    "loggin.error"
    Um erro que aconteceu na aplicação onde o software não conseguiu executar alguma 
    função, como um botão que não está funcionando em um site, por exemplo. Ele impede 
    que apenas uma funcionalidade específica pare de funcionar. 

    "logging.critical"
    Um erro com consequências graves que pode impedir a execução total do programa.

Por padrão o módulo logging irá exibir no terminal apenas as mensagens do nível 
'warning' para cima. Para alterarmos o nível padrão, utilizamos a função 'basicConfig'.

'level' é o que define o nível mínimo de logging para impressão no terminal
"""


import logging


logging.basicConfig(
    level=logging.DEBUG, filename='cadastro.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8')


try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha: '))
    # simulando uma consulta ao banco de dados
    if senha == 1234:
        print('Login realizado com sucesso')
        logging.info(f'{email} entrou em sua conta bancária')
    else:
        print('Senha Inválida')
        logging.warning(f'Usuário {email} digitou uma senha inválida')
except ValueError as erro:
    print('Digite apenas números')
    logging.error(erro)
finally:
    print('<<< PROGRAMA ENCERRADO >>>')
