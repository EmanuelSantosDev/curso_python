# Diferença entre Módulo e Package


- **MÓDULOS** são arquivos unitários
- **PACKAGES** são pastas (pacotes) que agrupam vários módulos relacionados
- O arquivo ``__init__.py`` pode ser vazio ou conter código Python para executar quando o pacote é importado
- os arquivos ``__init__.py`` são necessários para que o Python trate diretórios contendo o arquivo como pacotes


```python
# Importando um módulo de um pacote
from meu_pacote.modulo2 import apresentar
```