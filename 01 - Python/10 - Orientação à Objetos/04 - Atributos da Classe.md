# Atributos da Classe


- Definem **VALORES PADRÕES** para uma classe
- Podem ser acessados mesmo que uma instância não tenha sido criada


````python
class Computador:

    # Atributos da Classe
    sistema_operacional = 'Windows 10'
    versao = 'Home'

    # Atributos da Instância
    def __init__(self, marca, memora_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memora_ram
        self.placa_de_video = placa_de_video


# Acessando Atributos da Classe sem precisar instanciar um novo objeto
(print(Computador.sistema_operacional))  # Windows 10
(print(Computador.versao))  # Home


# Alterando o valor do Atributo da Classe
Computador.sistema_operacional = 'Linux'
(print(Computador.sistema_operacional))  # Linux
````