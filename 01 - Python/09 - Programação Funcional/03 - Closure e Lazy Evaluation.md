# Closure e Lazy Evaluation


- **Closure** é um conceito de programação que se refere à capacidade de uma função de "lembrar" e acessar as variáveis ​​que estavam presentes em seu ambiente de definição original, mesmo que essa função seja chamada em um ambiente diferente. Isso é possível porque a função encapsula essas variáveis ​​em seu escopo local.
- **Lazy Evaluation** (avaliação preguiçosa ou atrasada) é uma estratégia que "atrasa" a computação do valor de uma expressão até que seja necessário. Usada em linguagens de programação funcionais para evitar o cálculo desnecessário de valores intermediários e melhorar o desempenho do programa.


````python
def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


dobro = multiplicar(2)
triplo = multiplicar(3)


print(dobro(10))  # 20
print(triplo(10))  # 30
````