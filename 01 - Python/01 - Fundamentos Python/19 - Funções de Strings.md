# Funções de Strings


### upper() e lower()


````python
nome_do_curso = 'Edição de Vídeo'

print(nome_do_curso.upper())  # EDIÇÃO DE VÍDEO
print(nome_do_curso.lower())  # edição de vídeo
````


### strip(), lstrip() e rstrip() 
     

- A função ``strip()`` retorna uma cópia da string original com todos os caracteres de espaço em branco (espaço, tabulação, nova linha) removidos do início e do final da string.
- Além disso, a função também aceita um argumento opcional que especifica os caracteres que devem ser removidos da string, em vez de apenas espaços em branco.


````python
nome_do_curso = '   Edição de Vídeo   '

print(nome_do_curso.strip())   # Edição de Vídeo
print(nome_do_curso.lstrip())  # Edição de Vídeo
print(nome_do_curso.rstrip())  #    Edição de Vídeo

# retirando os "0" e os "espaços em branco"
palavra = '000 123 abc 000'
print(palavra.strip('0').strip())  # 123 abc
````


### replace()


````python
nome_do_curso = 'Edição de Vídeo'

print(nome_do_curso.replace('Vídeo', 'Música')) # Edição de Música
print('https://sc.olx.com.br/relogio'.replace('relogio', 'carro')) # https://sc.olx.com.br/carro
````


### split()


````python
frase = "Olá, seja bem-vindo à este treinamento"

print(frase.split())  # ['Olá,', 'seja', 'bem-vindo', 'à', 'este', 'treinamento']
print(frase.split(','))  # ['Olá', ' seja bem-vindo à este treinamento']
print(frase.split('-'))  # ['Olá, seja bem', 'vindo à este treinamento']
print(frase.split(' ', 2))  # ['Olá,', 'seja', 'bem-vindo à este treinamento']
````

### join()


````python
nomes = ['Ana', 'Miguel', 'Samuel', 'Otavio']
print(' - '.join(nomes))  # Ana - Miguel - Samuel - Otavio
````


### find()


Sintaxe básica:

    string.find(value, start, end)

````python
nome_do_curso = 'Edição de Vídeo'
print(nome_do_curso.find('ção'))  # 3
print(nome_do_curso.find('z'))  # -1
````


### index()


Sintaxe básica:

    lista.index(elemento, start, end)


A função ``index()`` é semelhante à função ``find()``, mas se a substring não for encontrada na string, a função ``index()`` gera uma exceção ``ValueError``, enquanto a função ``find()`` retorna ``-1``.


````python
teclado = 'Teclado'
print(teclado.index('l'))  # 3
print(teclado[teclado.index('l')])  # l
print(teclado[teclado.index('x')])  # ValueError: substring not found
````


### Última Ocorrência com rindex() e rfind()


Sintaxe básica:

    string.rindex(value, start, end)
    string.rfind(value, start, end)

Se o valor não for encontrado, o método ``rfind()`` retornará ``-1``, mas o método ``rindex()`` gerará uma exceção.

````python
txt = "Hello, welcome to my world."
print(txt.rfind("y"))  # 19
print(txt.rindex("y"))  # 19
print(txt.rfind("q"))  # -1 
print(txt.rindex("q"))  # ValueError: substring not found
````