# Leitura Stream

- leitura de arquivo sobre demanda (Stream)
- podemos fazer analogia com o YouTube, que faz o envio do vídeo em partes (Streaming)
- assim economizamos recursos de memória do computador

````python
arquivo = open('pessoas.csv', encoding='utf-8')

for registro in arquivo:
    # utilizandos strip() para retirar os espaços entre as linhas
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()

if arquivo.closed:
    print('Arquivo Fechado')

# Nome: Maria Idade: 45
# Nome: João Idade: 33
# Nome: Pedro Idade: 63
# Nome: Ana Idade: 21
# Nome: Bia Idade: 40
# Nome: Carlos Idade: 14
# Arquivo Fechado
````