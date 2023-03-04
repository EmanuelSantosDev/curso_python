# Criando Atributos de Forma Dinâmica


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