# ------------------------------------------------------------------------------------
# Arrays
# ------------------------------------------------------------------------------------


# podemos armazenar apenas ITEMS DO MESMO TIPO
# essa é a grande diferença se comparado a listas
# as operações são basicamente iguais
# utiliza-se Type Code (Código de Tipo) para definição do tipo:
# >>>>>>> 'b' - char
# >>>>>>> 'i' - int
# >>>>>>> 'f' - float
# >>>>>>> 'd' - double


# importando o array
from array import array


# array de inteiros
numeros = array('i', [1, 2, 3, 4, 5, 6])
print(numeros)  # [1, 2, 3, 4, 5, 6]
numeros.append(10)
print(numeros)  # [1, 2, 3, 4, 5, 6, 10]
numeros.insert(5, 200)
print(numeros)  # [1, 2, 3, 4, 5, 200, 6, 10]
numeros.pop(1)
print(numeros)  # [1, 3, 4, 5, 200, 6, 10]
numeros.remove(5)
print(numeros)  # [1, 3, 4, 200, 6, 10]
del numeros[1]
print(numeros)  # [1, 4, 200, 6, 10]
