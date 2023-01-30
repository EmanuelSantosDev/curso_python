# ------------------------------------------------------------------------------------
# Classes Abstratas
# ------------------------------------------------------------------------------------


# é uma maneira de garantir a funcionalidade correta e previsivel do programa
# são uma maneira de criar um "contrato" (esqueleto) obrigando que algo seja...
# ...implementado nas classes filhas
# no exemplo abaixo definimos um método abstrato, mas poderíamos também definir...
# ... propriedades abstratas ou até mesmo uma classe completa abstrata
# o módulo "abc" fornece a infraestrutura para definir classes abstratas (ABCs)
# ABC (Abstract Base Classes)


from abc import ABC, abstractmethod


class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass  # quem herdar de Camera terá a obrigação de implementar este método


class CameraProfissional(Camera):
    pass


camera_profissional = CameraProfissional()
# Can't instantiate abstract class CameraProfissional with abstract method definir_tamanho_lente
# o erro acima ocorreu porque não implementamos o método definir_tamanho_lente() na classe filha
