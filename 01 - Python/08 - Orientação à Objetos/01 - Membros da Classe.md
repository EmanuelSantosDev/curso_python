# Membros da Classe

````python
# podemos criar uma classe e incluir os atributos de forma dinâmica
class Data:
    def to_string(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()

d1.dia = '02'
d1.mes = '06'
d1.ano = '1986'

print(d1.to_string())  # 02/06/1986
````


### Utilizando o método mágico ``__str__(self)``

````python
class Data2:
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d2 = Data2()
d2.dia = '14'
d2.mes = '11'
d2.ano = '1998'
# não é necessário invocar o método para exibir o objeto no formato string
print(d2)  # 14/11/1998
````