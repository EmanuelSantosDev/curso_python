# Construtor e Atributos da Instância


- O **Construtor** ``__init__`` é um método especial invocado automaticamente quando um objeto é instanciado 
- É ele quem define os **Atributos da Instância**.
- O parâmetro ``self`` faz referência ao próprio objeto que está sendo instanciado


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