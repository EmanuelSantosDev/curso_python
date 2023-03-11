# Logging


- Log é uma forma de registrar o que aconteceu e o que está acontecendo na aplicação.
- Os **níveis de logging** são uma maneira organizada de guardar informações da aplicação em formato de texto.
- ``logging.basicConfig()`` é uma função da biblioteca de registro ``logging`` que é usada para configurar o registro básico de logs em aplicativos simples.
- ``level`` é um parâmetro que define o nível mínimo de gravidade para registrar as mensagens de log (por exemplo, ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR`` ou ``CRITICAL``).
- Se um nível de gravidade for definido em uma configuração, todos os registros de gravidade naquele nível e acima serão registrados.


### Níveis de Logging::


Depois de chamar ``basicConfig()``, você pode usar as funções de registro de log:


- ``logging.debug()`` - Mensagens de depuração que são destinadas apenas para desenvolvedores.
- ``logging.info()`` - Mensagens de informação para fornecer informações úteis sobre o status do programa.
- ``logging.warning()`` - Mensagens de advertência que indicam que algo inesperado aconteceu ou pode acontecer em breve.
- ``loggin.error()`` - Mensagens de erro que indicam um problema sério que impediu a execução normal do programa. 
- ``logging.critical()`` - Mensagens críticas que indicam um erro fatal que impede a continuação do programa.


````python
import logging


logging.basicConfig(
    level=logging.DEBUG, 
    filename='cadastro.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8')


try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha: '))
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
````


### Arquivo de Log


````
2023-02-04 16:52:06,287 - INFO - emanuel.santos@gmail.com entrou em sua conta bancária
2023-02-04 16:52:31,575 - WARNING - Usuário joana.maria@yahoo.com digitou uma senha inválida
2023-02-04 16:52:57,715 - ERROR - invalid literal for int() with base 10: 'abc123'
2023-02-04 16:53:23,711 - INFO - joana.maria@yahoo.com entrou em sua conta bancária
2023-02-04 16:53:37,563 - INFO - joao.santos@outlook.com entrou em sua conta bancária
````