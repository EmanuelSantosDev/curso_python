# Gerenciador de Pacotes pip


**DECOBRIR QUAIS PACOTES JÁ ESTÃO INSTALADOS:**

    pip list

**INSTALANDO UM PACOTE:**

    pip install [package]

**DESINSTALANDO UM PACOTE:**

    pip uninstall [package]

**ATUALIZANDO UM PACOTE:**

- 1º Passo - Desinstalar  
- 2º Passo - Reinstalar (a atualização direta pode quebrar outros pacotes que fazem uso específico dela)

**INSTALANDO UMA VERSÃO ESPECÍFICA DE UM PACOTE:**

    pip install [package]==[versao]


**DESINSTALANDO UM PACOTE E TODAS AS SUAS DEPENDÊNCIAS:**


    pip install pip-autoremove
    pip-autoremove somepackage -y


Se ocorrer o erro `ModuleNotFoundError when trying to use pip-autoremove`, esse problema pode ser resolvido movendo o arquivo ``pip_autoremove.py`` de seu local original dentro da pasta ``Scripts`` para a pasta ``Lib``:

**Alternativa 1:**

    C:\Program Files\Python311\Scripts
    C:\Program Files\Python311\Lib

**Alternativa 2:**

    C:\Users\Username\AppData\Local\Programs\Python\Python311\Scripts
    C:\Users\Username\AppData\Local\Programs\Python\Python311\Lib

