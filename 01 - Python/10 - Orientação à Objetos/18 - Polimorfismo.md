# Polimorfismo


- Se refere à capacidade de objetos de diferentes classes serem tratados como se fossem da mesma classe, permitindo que eles sejam usados de maneira intercambiável.
- Classes são **intercambiáveis** se possuem métodos com o mesmo nome e parâmetros.
- Quando duas ou mais classes implementam um método com o mesmo nome, essas classes são consideradas **polimórficas**.

No exemplo abaixo, o método ``fazer_barulho()`` recebe um objeto ``Animal``, mas na verdade está recebendo objetos das classes ``Cachorro`` e ``Gato``. Como ambos implementam o método ``falar()``, eles podem ser usados de maneira intercambiável no método ``fazer_barulho()``.


````python
class Animal:
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        return "Au au"


class Gato(Animal):
    def falar(self):
        return "Miau"


def fazer_barulho(animal):
    print(animal.falar())


cachorro = Cachorro()
gato = Gato()

fazer_barulho(cachorro)  # "Au au"
fazer_barulho(gato)      # "Miau"
````


Em vez de escrever código para manipular objetos de tipos diferentes, é possível escrever um código genérico que usa o mesmo método para trabalhar com todos os objetos intercambiáveis. Observe que todas as classes implementam um método ``abrir()`` com o mesmo nome e parâmetros. Isso significa que elas são intercambiáveis e podem ser usadas no lugar uma da outra em um código genérico que manipula arquivos.


````python
class ArquivoTexto:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_arquivo}')


class ArquivoImagem:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_arquivo}')


class Planilha:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def abrir(self):
        print(f'Abrindo o arquivo {self.nome_arquivo}')


def carregar_arquivo(arquivo):
    arquivo.abrir()


arquivo_texto = ArquivoTexto('resumo')
arquivo_imagem = ArquivoImagem('ferias')
planilha = Planilha('fluxo')

carregar_arquivo(arquivo_texto)  # Abrindo o arquivo resumo
carregar_arquivo(arquivo_imagem)  # Abrindo o arquivo ferias
carregar_arquivo(planilha)  # Abrindo o arquivo fluxo
````