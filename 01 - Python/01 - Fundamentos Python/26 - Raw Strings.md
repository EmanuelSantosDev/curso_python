# Raw Strings

````python
# Python usa a barra invertida (\) para indicar o início de uma sequência de escape:
s = 'lang\tver\nPython\t3'
print(s)
# lang    ver
# Python  3


# No entanto, raw strings tratam a barra invertida (\) como um caractere literal:
s = r'lang\tver\nPython\t3'
print(s)
# lang\tver\nPython\t3


# Uma raw string é como sua string regular com a barra invertida (\) representada como barras invertidas duplas (\\):
s = 'lang\\tver\\nPython\\t3'
print(s)
# lang\tver\nPython\t3
````