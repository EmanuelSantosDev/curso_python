# Método ``__iter__`` e ``__next__``


- O método`` __iter__`` em Python é usado para definir um iterador personalizado para uma classe.
- O iterador retornado pelo método ``__iter__`` deve ter um método ``__next__``, que é chamado em cada iteração.
- O método ``__next__`` deve retornar o próximo elemento da iteração ou levantar a exceção ``StopIteration`` se não houver mais elementos a serem iterados.


````python
class SequenciaNumerica:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def __iter__(self):
        self.atual = self.inicio
        return self

    def __next__(self):
        if self.atual <= self.fim:
            resultado = self.atual
            self.atual += 1
            return resultado
        else:
            raise StopIteration


seq = SequenciaNumerica(1, 10)
for numero in seq:
    print(numero, end=' ')  # 1 2 3 4 5 6 7 8 9 10
````