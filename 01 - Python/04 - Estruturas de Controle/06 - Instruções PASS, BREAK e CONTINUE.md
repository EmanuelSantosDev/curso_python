# Instruções PASS, BREAK e CONTINUE

### Instrução PASS


- Cria um espaço reservado para código futuro
- Evita que o interpretador fique acusando erro


````python
numero = 0

while numero < 5:
    pass

for numero in range(1, 11):
    pass
````

### Instrução CONTINUE

````python
for numero in range(21):
    if numero % 2 == 0:  # imprimindo apenas os números PARES
        print(numero, end=" ")
    else:
        continue
# 0 2 4 6 8 10 12 14 16 18 20
````

### Instrução BREAK

````python
for numero in range(100):
    if numero > 10:
        break
    else:
        print(numero, end=" ")
print('\nEncerramos a contagem em 10')
# 0 1 2 3 4 5 6 7 8 9 10
# Encerramos a contagem em 10
````