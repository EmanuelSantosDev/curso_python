# Construtor


O *Construtor* ``__init__`` é um método especial que é automaticamente chamado quando um objeto é criado a partir de uma classe. É usado para inicializar os atributos de um objeto.


````python
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data('02', '06', '1986')
print(d1)  # 02/06/1986
````