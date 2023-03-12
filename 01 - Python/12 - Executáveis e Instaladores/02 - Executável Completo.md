# Executável Completo

### Instalar Biblioteca **cx-Freeze**:

    pip install cx-freeze

### Criar o arquivo **setup.py**:

```python
import sys
import os
from cx_Freeze import setup, Executable


# Definindo o que deve ser incluído na pasta final
arquivos = ['icone_python.ico', 'imagens/']


# Definindo as Configurações da Saída de Arquivos (arquivo principal + ícone)
configuracao = Executable(
    script='app.py',
    icon='icone_python.ico',
)


# Configurando o cx_freeze (detalhes do programa)
setup(
    name='Calculadora Python',
    version='1.0.0',
    description='Calculadora construída em Python, que roda cálculo de soma direto no terminal',
    author='Emanuel Santos',
    options={'build_exe': {'include_files': arquivos}},
    executables=[configuracao]
)

```

### Gerando o Executável:

    python setup.py build 