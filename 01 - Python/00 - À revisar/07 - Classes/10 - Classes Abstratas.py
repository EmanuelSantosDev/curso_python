# ------------------------------------------------------------------------------------
# Classes Abstratas
# ------------------------------------------------------------------------------------


# Abstração é o conceito em programação orientada a objetos que é usado para...
# ...esconder a funcionalidade interna das classes para os usuários.
# No contexto da programação, a Abstração é utilizada para facilitar a vida de...
# ...outros desenvolvedores. Não precisamos saber como a função sort() funciona.
# Uma classe que contém um ou mais Métodos Abstratos é chamada de Classe Abstrata
# Uma classe abstrata não pode ser instanciada e deve conter pelo menos um método abstrato
# o módulo "abc" fornece a infraestrutura para definir classes abstratas (ABCs)
# ABC = Abstract Base Class)
# cria um projeto (esqueleto) das nossas classes e são úteis em situações em que as...
# classes filhas devem fornecer sua própria implementação separadamente.


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
