# Método \_\_str\_\_


O método especial ``__str__`` é usado para retornar uma representação em string de um objeto.


````python
class Data:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()

d1.dia = '14'
d1.mes = '11'
d1.ano = '1998'

# não é necessário invocar o método para exibir o objeto no formato string
print(d1)  # 14/11/1998
````