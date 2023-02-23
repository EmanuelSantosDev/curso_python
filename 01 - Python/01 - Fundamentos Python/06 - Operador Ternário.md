# Operador Ternário


## Forma #1
````python
esta_chovendo = False
resultado = 'Estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.')
print(resultado)  # Estou com as roupas secas.
````

## Forma #2
````python
esta_chovendo = True
resultado = 'Estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo]
print(resultado)  # Estou com as roupas molhadas.
````