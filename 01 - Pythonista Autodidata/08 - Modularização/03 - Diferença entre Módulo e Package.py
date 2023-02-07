# ------------------------------------------------------------------------------------
# Diferença entre Módulo e Package
# ------------------------------------------------------------------------------------


# MÓDULOS - são arquivos unitários
# PACKAGES - são pastas (pacotes) que agrupam vários módulos relacionados
# eles precisam ter OBRIGATORIAMENTE o arquivo "__init__.py" totalmente EM BRANCO
# Os arquivos "__init__.py" são necessários para que o Python trate diretórios...
# ...contendo o arquivo como pacotes


# Importando um módulo de um pacote
from meu_pacote.modulo2 import apresentar
