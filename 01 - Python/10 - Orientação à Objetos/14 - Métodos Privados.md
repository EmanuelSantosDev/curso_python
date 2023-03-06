# Métodos Privados

- Em Python, a convenção é que nomes de métodos e atributos iniciados com um sublinhado ``_`` são considerados privados. 
- Isso significa que eles não devem ser acessados ou modificados diretamente de fora da classe que os contém.


````python
class MinhaClasse:
    
    def __init__(self, valor):
        self._valor = valor
        
    def _metodo_privado(self):
        print("Este é um método privado.")
        
    def metodo_publico(self):
        print("Este é um método público.")
        self._metodo_privado()


objeto = MinhaClasse(42)
objeto._metodo_privado()  # imprime "Este é um método privado."

````