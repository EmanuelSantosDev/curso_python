# Try e Except


- O bloco ``try`` permite testar erros em um bloco de código
- O bloco ``except`` permite lidar com o erro.


````python
try:
    valor = int(input('Digite um valor em reais: '))
    print('Valor em Dólares = ', valor * 5.25)
except ValueError as erro:
    print('Digite um número válido!')
````