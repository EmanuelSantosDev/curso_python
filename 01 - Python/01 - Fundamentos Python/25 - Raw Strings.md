# Raw Strings

- O ``r`` antes das aspas vem de **raw**, ou seja, a string será interpretada como uma string literal.
- Em uma string comum, temos a ``\`` como caracter de escape para representar quebras de linha (como ``\n``, ``\r``, ``\t``) e outros. 
- Em uma string literal, esses elementos não são processados.

````python
s = 'lang\tver\nPython\t3'
print(s)
# lang    ver
# Python  3


s = r'lang\tver\nPython\t3'
print(s)
# lang\tver\nPython\t3
````