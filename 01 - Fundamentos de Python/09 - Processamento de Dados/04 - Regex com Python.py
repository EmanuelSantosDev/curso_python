# ------------------------------------------------------------------------------------
# Regex ou Regular Expression
# ------------------------------------------------------------------------------------


import re


# ------------------------------------------------------------------------------------
# Findall
# ------------------------------------------------------------------------------------


# retorna todas as ocorrências que inicial com "bl"
texto = "black, blue and brown"
expressao = r'bl\w+'
localizados = re.findall(expressao, texto)
print(localizados)  # ['black', 'blue']


# ------------------------------------------------------------------------------------
# Search
# ------------------------------------------------------------------------------------


# Retorna um objeto "Match" se houver uma correspondência em qualquer lugar da string
# Procurando o primeiro caractere de espaço em branco na string:
texto = "The rain in Spain"
expressao = r"\s"
x = re.search(expressao, texto)
print(x)  # <re.Match object; span=(3, 4), match=' '>
print(f'Posição Inicial = {x.start()}')  # Posição Inicial = 3


# ------------------------------------------------------------------------------------
# Split
# ------------------------------------------------------------------------------------


email = 'carol@gmail.com.br'
expressao = r"(@.{1,8}\.)"
resultado = re.split(expressao, email)
print(resultado)  # ['carol', '@gmail.', 'com.br']


# ------------------------------------------------------------------------------------
# Sub
# ------------------------------------------------------------------------------------


email = 'carol@gmail.com.br'
expressao = r"(@.{1,8}\.)"
resultado = re.sub(expressao, '@yahoo.', email)
print(resultado)  # carol@yahoo.com.br
