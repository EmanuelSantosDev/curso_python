# *args


- em alguns casos não sabemos QUANTOS argumentos a função irá receber
- esta quantidade X de argumentos são passados no formato de TUPLAS
- os DEMAIS ARGUMENTOS devem ser NOMEADOS
- **Args** são parâmetros considerados **Packing**, pois empacotam os argumentos recebidos em uma Tupla

````python
def somar(*valores, b):
    print(valores)  # (1, 2, 3, 4)
    for valor in valores:
        b += valor
    print(b)  # 18


somar(1, 2, 3, 4, b=8)
````