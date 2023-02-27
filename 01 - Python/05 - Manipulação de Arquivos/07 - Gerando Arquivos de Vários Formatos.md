# Gerando Arquivos de Formatos Diferentes Simultaneamente

````python
arquivos = ['foto.jpg', 'video.mp4', 'musica.mp3', 'tabela.xlsx']

for arquivo in arquivos:
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        pass
````