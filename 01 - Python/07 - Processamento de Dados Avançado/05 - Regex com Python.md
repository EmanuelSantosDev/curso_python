# Regex ou Regular Expression


````python
import re


# ------------------------------------------------------------------------------------
# compile (cria um padrão)
# ------------------------------------------------------------------------------------


padrao = re.compile('python')
string1 = 'python'
string2 = 'python python'


# ------------------------------------------------------------------------------------
# fullmatch (devolve um objecto se e só se a string inteira corresponder ao padrão)
# ------------------------------------------------------------------------------------


x = re.fullmatch(padrao, string1)  #
y = re.fullmatch(padrao, string2)  #
print(x)  # <re.Match object; span=(0, 6), match='python'>
print(y)  # None


# ------------------------------------------------------------------------------------
# search (devolve um objeto se houver uma correspondência em qualquer parte da string)
# ------------------------------------------------------------------------------------


x = re.search(padrao, string1)
y = re.search(padrao, string2)
print(x)  # <re.Match object; span=(0, 6), match='python'>
print(y)  # <re.Match object; span=(0, 6), match='python'>


# ------------------------------------------------------------------------------------
# findall (devolve uma lista com todas as ocorrências encontradas)
# ------------------------------------------------------------------------------------


x = re.findall(padrao, string1)
y = re.findall(padrao, string2)
print(x)  # ['python']
print(y)  # ['python', 'python']


# ------------------------------------------------------------------------------------
# split (divide a string a partir de um padrão específico)
# ------------------------------------------------------------------------------------


string = 'carol@gmail.com.br'
padrao = re.compile('([@].{1,8}\.)')
resultado = re.split(padrao, string)
print(resultado)  # ['carol', '@gmail.', 'com.br']


# ------------------------------------------------------------------------------------
# sub (substitui o padrão encontrado, por outro)
# ------------------------------------------------------------------------------------


string = 'carol@gmail.com.br'
padrao = re.compile('(@.{1,8}\.)')
resultado = re.sub(padrao, '@yahoo.', string)
print(resultado)  # carol@yahoo.com.br
````