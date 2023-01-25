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
- a Estrutura With diz ao programa: "com esse arquivo cujo apelido é XXXX eu quero..."


OBJETIVOS AO ABRIR O ARQUIVO


'r'  -> usado para LER o arquivo
'r+' -> usado para LER e ESCREVER no arquivo
'w'  -> usado para ESCREVER um novo arquivo ou SOBRESCREVER caso já exista 
'a'  -> usado para ACRESCENTAR informação ao arquivo
'''


# ------------------------------------------------------------------------------------
# módulo 'os'
# ------------------------------------------------------------------------------------


# o módulo OS fornece funções para interagir com o sistema operacional.
import os


# ------------------------------------------------------------------------------------
# 'w' => write
# ------------------------------------------------------------------------------------


# se o arquivo já existir ele SOBRESCREVE o conteúdo
# se o arquivo não existir, ele CRIA um novo arquivo


# with open('06 - Trabalhando com Arquivos/senha.txt', 'w') as arquivo:
#     senha = arquivo.write('987654')


# ------------------------------------------------------------------------------------
# 'r' => read
# ------------------------------------------------------------------------------------


# método read() para arquivos simples
# ex: senhas, tokens, informações únicas, etc...
# ele até consegue ler um arquivo de várias linhas, mas NÃO consegue ISOLAR as linhas


# with open('06 - Trabalhando com Arquivos/email.txt', 'r') as arquivo:
#     email = arquivo.read()
#     print(email)
    # programadorpython2023@gmail.com


# método readlines() para arquivos maiores
# nos devolve uma lista em que cada item da lista é uma linha
# utilizamos um terceiro parâmetro, o 'encoding' para corrigir erros de impressão


# with open('06 - Trabalhando com Arquivos/mensagem.txt', 'r', encoding='utf-8') as arquivo:
#     mensagem = arquivo.readlines()
#     print(mensagem)
#     '''
#     ['Prezados,\n', '\n', 'O faturamento desse mÃªs foi de: R$15.000\n', '\n', 
#     'Qualquer dÃºvida que tiverem, Ã© sÃ³ falar.\n', '\n', 'Att.,\n', 'Lira']
#     '''
#     for linha in mensagem:
#         if 'faturamento' in linha:
#             print(linha)  # O faturamento desse mês foi de: R$15.000




# ------------------------------------------------------------------------------------
# 'a' => append
# ------------------------------------------------------------------------------------


# with open('06 - Trabalhando com Arquivos/email.txt', 'a') as arquivo:
#     arquivo.write('\nemanuel.santos@gmail.com')
