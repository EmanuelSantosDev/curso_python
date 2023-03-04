# Métodos Estáticos


- São métodos que não utilizam a instância da classe através do parâmetro ``self``, nem mesmo modificam a classe através do parâmetro ``cls``.
- São métodos que fazem sentido serem incluídos em uma mesma classe onde queremos agrupar todas as funcionalidades de um tema específico, como um computador.
- É uma função que é executada repetidamente e não queremos que ela fique "solta" no código.
- Utiliza o decorador ``@staticmethod``


````python
class Computador:

    sistema_operacional = 'Windows 10'
    versao = 'Home'

    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video

    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False


# Exemplo: método que identifica se um computador pode rodar um programa pesado
print(Computador.roda_programas_pesados(16))  # True
print(Computador.roda_programas_pesados(4))  # False
````
