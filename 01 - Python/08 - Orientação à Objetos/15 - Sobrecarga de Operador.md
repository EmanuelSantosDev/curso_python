# Sobrecarga de Operador

- Permite que você defina o comportamento de operadores comuns em suas próprias classes personalizadas.
- Para sobrecarregar um operador em Python, você precisa definir um método especial que corresponda ao operador que deseja sobrecarregar. 
- Por exemplo, o método especial ``__add__()`` é usado para sobrecarregar o operador de adição ``+``.
- Além do operador de adição, você pode sobrecarregar muitos outros operadores comuns, como subtração (``__sub__()``), multiplicação (``__mul__()``), divisão (``__truediv__()``), igualdade (``__eq__()``), entre outros.


````python
class MinhaClasse:

    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        return self.valor + outro.valor


objeto1 = MinhaClasse(10)
objeto2 = MinhaClasse(20)

soma = objeto1 + objeto2
print(soma)  # 30
````