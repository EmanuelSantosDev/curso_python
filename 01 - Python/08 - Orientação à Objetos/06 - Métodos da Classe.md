# Métodos da Classe


- Os **métodos da classe** são funções que são definidas dentro da classe e são acessíveis através da própria classe, em vez de uma instância da classe.
- Eles são usados para definir comportamentos que se aplicam a classe em vez de comportamentos específicos de uma instância da classe.
- Os métodos da classe são declarados usando o decorador ``@classmethod``.
- O primeiro parâmetro do método deve ser a própria classe, geralmente chamado de ``cls``, em vez do parâmetro ``self`` usado para métodos de instância.


### Exemplo #1


````python
class Pessoa:
    contador = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.contador += 1

    def apresentar(self):
        print("Meu nome é", self.nome, "e eu tenho", self.idade, "anos.")

    @classmethod
    def contar(cls):
        print("Já foram criadas", cls.contador, "instâncias da classe Pessoa.")


Pessoa.contar()  # Já foram criadas 0 instâncias da classe Pessoa.

pessoa1 = Pessoa('João', 34)
pessoa2 = Pessoa('Maria', 29)
pessoa3 = Pessoa('Pedrinho', 19)

Pessoa.contar()  # Já foram criadas 3 instâncias da classe Pessoa.
````


### Exemplo #2


````python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Meu nome é", self.nome, "e eu tenho", self.idade, "anos.")

    @classmethod
    def de_string(cls, string):
        nome, idade = string.split(",")
        return cls(nome.strip(), int(idade.strip()))


p1 = Pessoa('João', 29)
p1.apresentar()  # Meu nome é João e eu tenho 29 anos.


# criando uma nova instância de Pessoa usando o método de classe "de_string"
p2 = Pessoa.de_string("Maria, 25")


print(p2.nome)  # Maria
print(p2.idade)  # 25
p2.apresentar()  # Meu nome é Maria e eu tenho 25 anos.
````