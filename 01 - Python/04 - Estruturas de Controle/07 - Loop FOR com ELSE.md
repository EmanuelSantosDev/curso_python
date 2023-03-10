# Loop FOR com ELSE

- O loop ``for com else`` é uma construção especial que permite executar um bloco de código caso o loop for seja concluído sem interrupção. 
- O bloco ``else`` é executado somente se o loop ``for`` for executado completamente, sem a ocorrência de um ``break`` que interrompa a execução.
- Pode ser útil, por exemplo, quando estamos usando o laço ``for`` para encontrar algo em um iterável, e não encontramos. O bloco ``else`` então pode executar algum procedimento.

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