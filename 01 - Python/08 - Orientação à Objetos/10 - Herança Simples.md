# Herança Simples


- Útil para quando queremos usar funcionalidades similares ou expandir funcionalidades existentes.
- Toda classe em python herda de uma classe chamada de ``object``
- Poderiamos inicializar nossa classe assim => ``class Camera (object)``
- O método ``super()`` é uma função que permite acessar e chamar métodos e atributos de uma classe pai (superclasse) a partir de uma classe filha (subclasse).


### Exemplo #1


````python
class Animal:
    def fazer_barulho(self):
        print('Algum barulho')


class Cachorro(Animal):
    def fazer_barulho(self):
        # invocando método da classe pai
        super().fazer_barulho()
        print('O cachorro late')


cachorro = Cachorro()
cachorro.fazer_barulho()
# Algum barulho
# O cachorro late
````


### Exemplo #2



````python
class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(
            f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels')


# ------------------------------------------------------------------------------------
# CameraCelular herda da classe Camera, mas também possui MÉTODO e ATRIBUTO exclusivos
# ------------------------------------------------------------------------------------


class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando o filtro {filtro}')


celular = CameraCelular('Sony', 25, 4)


print(celular.quantidade_de_cameras)  # 4
celular.tirar_foto()  # Foto tirada com a camera Sony com a qualidade de 25 megapixels
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
go_pro.tirar_foto(8)
# Foto tirada com a camera Canon com a qualidade de 25 megapixels com resolução de 8K


# ------------------------------------------------------------------------------------
# Verificando se uma CLASSE derivada de outra CLASSE
# ------------------------------------------------------------------------------------


print(issubclass(CameraCelular, Camera))  # True


# ------------------------------------------------------------------------------------
# Verificando se uma INSTANCIA é derivada de uma CLASSE
# ------------------------------------------------------------------------------------


print(isinstance(go_pro, GoPro))  # True
````