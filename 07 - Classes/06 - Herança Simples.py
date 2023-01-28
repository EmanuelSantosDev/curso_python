# ------------------------------------------------------------------------------------
# Herança Simples
# ------------------------------------------------------------------------------------


# útil para quando queremos usar funcionalidades similares ou expandir...
# ...funcionalidades existentes
# toda classe em python herda de uma classe chamada de "object"
# o método super() passa a responsabilidade dos atributos herdados para a classe pai
# nossa classe está herdando da classe object
# poderiamos inicializar assim => class Camera (object)


class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(
            f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels')


# ------------------------------------------------------------------------------------
# CameraCelular herda da classe Camera, mas também possui MÉTODO e ATRIBUTO exclusivo
# ------------------------------------------------------------------------------------


class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando o filtro {filtro}')


celular = CameraCelular('Sony', 25, 4)


print(celular.marca)  # Sony
print(celular.quantidade_de_cameras)  # 4
celular.aplicar_filtro('Outono')  # Aplicando o filtro Outono


# ------------------------------------------------------------------------------------
# SOBRESCREVENDO métodos da classe pai
# ------------------------------------------------------------------------------------


class GoPro(Camera):
    def __init__(self, marca, megapixels):
        super().__init__(marca, megapixels)

    # sobrescrevendo o método tirar_foto()
    def tirar_foto(self, resolucao_maxima):
        print(
            f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels com resolução de {resolucao_maxima}K')


go_pro = GoPro('Canon', 25)


# Foto tirada com a camera Canon com a qualidade de 25 megapixels com resolução de 8K
go_pro.tirar_foto(8)


# ------------------------------------------------------------------------------------
# Verificando se uma Classe é instância de outra
# ------------------------------------------------------------------------------------


print(issubclass(CameraCelular, Camera))  # True
