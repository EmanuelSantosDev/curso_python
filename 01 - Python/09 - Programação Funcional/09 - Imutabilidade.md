# Imutabilidade


- **Imutabilidade** enfatiza a criação de funções que produzem um resultado a partir de entradas, sem modificar essas entradas.
- A imutabilidade é importante porque evita efeitos colaterais indesejados.
- Efeitos colaterais ocorrem quando uma função modifica uma variável ou objeto externo.
- Esses efeitos colaterais podem tornar o comportamento do programa imprevisível e dificultar a depuração.


````python
# Neste exemplo os dados armazenados em "numbers" não são alterados


from functools import reduce


# Lista de números inteiros
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares
even_numbers = filter(lambda x: x % 2 == 0, numbers)
# [2, 4, 6, 8, 10]

# Dobrar cada número
doubled_numbers = map(lambda x: x * 2, even_numbers)
# [4, 8, 12, 16, 20]

# Somar todos os resultados
total = reduce(lambda x, y: x + y, doubled_numbers)
print(total)  # Output: 60
````