# ------------------------------------------------------------------------------------
#  Salvando e Modificando Arquivos
# ------------------------------------------------------------------------------------


'''
- ao abrir um arquivo, devemos ao final lembrar de fechá-lo
- se não fecharmos, pode dar algum erro, como não salvar as informações

arquivo.open()
código
código com erro 
arquivo.close()


ESTRUTURA 'WITH'


- facilita o trabalho com arquivos, pois fecha o mesmo automaticamente
- sem 'with', o código poderia dar bug antes de interpretar a linha que fecha 
  o mesmo que permaneceria aberto
- a Estrutura With diz ao programa: "com esse arquivo, cujo objetivo é XXXX e
  apelido é XXXX eu quero..."


OBJETIVOS AO ABRIR O ARQUIVO


'w'  -> usado para ESCREVER um novo arquivo ou SOBRESCREVER caso já exista 
'a'  -> usado para ACRESCENTAR informação à um arquivo
'r'  -> usado para LER o arquivo
'r+' -> usado para LER e ESCREVER no arquivo
'''


# ------------------------------------------------------------------------------------
# módulo 'os'
# ------------------------------------------------------------------------------------


# o módulo 'OS' fornece funções para interagir com o sistema operacional.
import os


# ------------------------------------------------------------------------------------
# 'w' => write
# ------------------------------------------------------------------------------------


with open('nomes.txt', 'w', newline='', encoding='utf-8') as arquivo:
    arquivo.write('Kaká' + os.linesep)


# ------------------------------------------------------------------------------------
# 'a' => append
# ------------------------------------------------------------------------------------


# 'newline='' é usado para criar uma nova linha simples (sem isso seria DUPLA)
# 'os.linesep' é usado para separar (ou melhor, encerrar) linhas


with open('nomes.txt', 'a', newline='', encoding='utf-8') as arquivo:
    arquivo.write('Suárez' + os.linesep)

nomes = ['Cristiano Ronaldo', 'Messi', 'Cafú', 'Rivaldo', 'Neymar']

with open('nomes.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)


# números precisam ser convertidos para o formato de string


numeros = [10, 20, 30, 40, 50]
with open('nomes.txt', 'a', newline='', encoding='utf-8') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)


# ------------------------------------------------------------------------------------
# 'r' => read
# ------------------------------------------------------------------------------------


with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
'''
Kaká
Suárez
Cristiano Ronaldo
Messi
Cafú
Rivaldo
Neymar
10
20
30
40
50
'''


# ------------------------------------------------------------------------------------
# 'r+' => read + append
# ------------------------------------------------------------------------------------


with open('nomes.txt', 'r+', newline='', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('FINAL DA LISTA' + os.linesep)


# ------------------------------------------------------------------------------------
# Abrindo Vários Arquivos de Formatos Diferentes Simultaneamente
# ------------------------------------------------------------------------------------


arquivos = ['foto.jpg', 'video.mp4', 'musica.mp3', 'tabela.xlsx']

for arquivo in arquivos:
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        pass
