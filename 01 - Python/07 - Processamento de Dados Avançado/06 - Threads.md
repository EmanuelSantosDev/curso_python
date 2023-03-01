# Threads


- uma **thread** é um fluxo separado de execução
- isso significa que seu programa terá duas ou mais coisas acontecendo ao mesmo tempo
- os fluxos podem ser executados de forma concorrente
- cada Thread roda dentro de seu próprio espaço
- se uma das Threads der erro, não impedirá a execução das demais


````python
import threading
import webbrowser
import time


def extrar_dados_site(site):
    print(f'Estamos navegando até o site {site}')
    webbrowser.open_new(site)
    for i in range(1, 21):
        print(f'Processando dados - {i}/20')
        time.sleep(1)
    print('Finalizando extração de dados do site')


def baixar_arquivos():
    for i in range(1, 11):
        print(f'Baixando arquivos - {i}/10')
        time.sleep(1)
    print('Arquivos baixados')


def tabulacao_de_dados():
    print('TABULAÇÃO DE DADOS: Vou ser executado somente após finalizar a nova_thread')


# ------------------------------------------------------------------------------------
# criando a Thread
# ------------------------------------------------------------------------------------


# o parâmetro "args" recebe uma "," ao final para identificá-lo como uma tupla
# o parâmetro "daemon" define que a thread rodará em segundo plano
# o método join() pausa a thread atual até que a thread alvo termine
# todo o código definido após join() rodará somente após o termino da thread alvo
# deve-se chamar join() para todas as threads, mesmo que já tenham parado
# o fato de chamar join() libera recursos de sistema


nova_thread = threading.Thread(target=extrar_dados_site, args=(
    'https://www.globo.com/',), daemon=True)
nova_thread.start()
baixar_arquivos()
nova_thread.join()
tabulacao_de_dados()


"""
Estamos navegando até o site https://www.globo.com/
Baixando arquivos - 1/10
Processando dados - 1/20
Baixando arquivos - 2/10
Processando dados - 2/20
Baixando arquivos - 3/10
Processando dados - 3/20
Baixando arquivos - 4/10
Processando dados - 4/20
Baixando arquivos - 5/10
Processando dados - 5/20
Baixando arquivos - 6/10
Processando dados - 6/20
Baixando arquivos - 7/10
Processando dados - 7/20
Baixando arquivos - 8/10
Processando dados - 8/20
Baixando arquivos - 9/10
Processando dados - 9/20
Baixando arquivos - 10/10
Processando dados - 10/20
Arquivos baixados
Processando dados - 11/20
Processando dados - 12/20
Processando dados - 13/20
Processando dados - 14/20
Processando dados - 15/20
Processando dados - 16/20
Processando dados - 17/20
Processando dados - 18/20
Processando dados - 19/20
Processando dados - 20/20
Finalizando extração de dados do site
TABULAÇÃO DE DADOS: Vou ser executado somente após finalizar a nova_thread
"""
````