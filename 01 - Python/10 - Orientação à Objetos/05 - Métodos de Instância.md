# Métodos de Instância


- São funções que são definidas dentro da classe e são acessíveis através de uma instância da classe.
- São usados para definir comportamentos específicos de uma instância e podem acessar e manipular seus atributos.
- São declarados usando o parâmetro ``self``, que é uma referência à própria instância da classe na qual o método está sendo chamado. Isso permite que o método acesse e modifique os atributos da instância.


````python
class Computador:

    sistema_operacional = 'Windows 10'
    versao = 'Home'

    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video

    # Método de Instância
    def exibir_dados_do_computador(self):
        print(f'Computador => {self.marca}, {self.memoria_ram}, {self.placa_de_video}')


computador = Computador('Asus', '8gb', 'Nvídia')


# Acessando Métodos de Instância
computador.exibir_dados_do_computador()  # Computador => Asus, 8gb, Nvídia
````