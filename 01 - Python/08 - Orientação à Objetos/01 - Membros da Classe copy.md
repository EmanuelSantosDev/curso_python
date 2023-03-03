# Membros da Classe

**Membros de uma classe** em Python são as variáveis e métodos definidos dentro da classe. Os membros da classe podem ser:
- **Variáveis de Instância**: são variáveis que pertencem a cada objeto criado
- **Variáveis de Classe**: são variáveis que pertencem à classe e não a cada objeto individual
- **Métodos de Instância**: são funções que operam em um objeto específico
- **Métodos de Classe**: são funções que operam na classe como um todo)

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