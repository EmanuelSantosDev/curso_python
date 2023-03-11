# Métodos Privados

- Em Python, a convenção é que nomes de métodos e atributos iniciados com um sublinhado ``_`` são considerados privados. 
- Isso significa que eles não devem ser acessados ou modificados diretamente de fora da classe que os contém.


````python
class MinhaClasse:
    def __init__(self, valor):
        self.__valor = valor  # atributo privado iniciado com valor passado no construtor

    def __metodo_privado(self):
        print("Este é um método privado!")

    def metodo_publico(self):
        print("Este é um método público!")
        self.__metodo_privado()  # método privado é chamado dentro do método público


objeto = MinhaClasse(10)
# chamando o método público, que internamente chama o método privado
objeto.metodo_publico()

# Este é um método público!
# Este é um método privado!
````