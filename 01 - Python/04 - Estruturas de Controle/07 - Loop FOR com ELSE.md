# Loop FOR com ELSE

- é útil quando NÃO ENCONTRAMOS dentro do laço FOR o que estamos "procurando"
- o bloco ELSE será executado somente se o laço FOR não executar a instrução ``break``

````python
# sem break
for i in range(1, 11):
    print(i, end=' ')
else:
    print('Fim do Programa')
# 1 2 3 4 5 6 7 8 9 10 Fim do Programa


# com break
for i in range(1, 11):
    print(i, end=' ')
    if i == 5:
        break
else:
    print('Fim do Programa')
# 1 2 3 4 5
````