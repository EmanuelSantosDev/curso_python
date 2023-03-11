# Método ``__iter__`` e ``__next__``


- O método`` __iter__`` é responsável por retornar um objeto iterável. Esse método é chamado quando um objeto é usado em um loop ``for``. 
- O método ``__next__`` é responsável por retornar o próximo item do iterador ou levantar a exceção ``StopIteration`` se não houver mais elementos a serem iterados. Esse método é chamado repetidamente quando o loop ``for`` é executado.


````python
class Contador:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for num in Contador(1, 5):
    print(num, end=' ')  # 1 2 3 4 5
````