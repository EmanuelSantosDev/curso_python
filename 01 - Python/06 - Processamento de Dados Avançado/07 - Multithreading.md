# Multithreading


- **Multithreading** é a execução em massa de várias threads em um mesmo processo
- ``thread.name`` retorna o nome da thread
- neste exemplo vamos entrar em 10 sites diferentes e deixar um comentário aleatório
- ou seja, teremos 10 threads executando paralelamente


````python
import threading
import time
import random


def comentar(site, comentario):
    print(f'Comentando no site {site} => {comentario}')
    time.sleep(5)
    print(f'Dados processados no site: {site}')


def escolher_comentario(lista_comentarios):
    return random.choice(lista_comentarios)


# definindo uma lista de threads (multithreading)
threads = []
lista_comentarios = ['Incrivel', 'Amazing', 'Que maravilha', 'Muito bom']


for site in range(1, 11):
    comentario = escolher_comentario(lista_comentarios)
    nova_thread = threading.Thread(target=comentar, args=(site, comentario))
    threads.append(nova_thread)

for thread in threads:
    # Imprimindo o nome da Thread
    print(f'Iniciando {thread.name}')
    thread.start()

for thread in threads:
    thread.join()


"""
Iniciando Thread-1 (comentar)
Comentando no site 1 => Muito bom
Iniciando Thread-2 (comentar)
Comentando no site 2 => Amazing
Iniciando Thread-3 (comentar)
Comentando no site 3 => Amazing
Iniciando Thread-4 (comentar)
Comentando no site 4 => Muito bom
Iniciando Thread-5 (comentar)
Comentando no site 5 => Muito bom
Iniciando Thread-6 (comentar)
Comentando no site 6 => Muito bom
Iniciando Thread-7 (comentar)
Comentando no site 7 => Que maravilha
Iniciando Thread-8 (comentar)
Comentando no site 8 => Amazing
Iniciando Thread-9 (comentar)
Comentando no site 9 => Muito bom
Iniciando Thread-10 (comentar)
Comentando no site 10 => Incrivel
Dados processados no site: 1
Dados processados no site: 4
Dados processados no site: 3
Dados processados no site: 2
Dados processados no site: 7
Dados processados no site: 6
Dados processados no site: 5
Dados processados no site: 9
Dados processados no site: 10
Dados processados no site: 8
"""
````