# Classe Exception


Útil para capturar uma excessão ainda não tratada em nosso programa.


````python
try:
    a = 5
    b = 0
    media = a / b
except Exception as erro:
    print(erro.__class__)  # <class 'ZeroDivisionError'>
````