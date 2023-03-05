# Formatar Números

````python
valor = 14599.465773848223


# Definindo a Quantidade de Casas Decimais (.2f)
print(f'{valor}')  # 14599.465773848224
print(f'{valor:.2f}')  # 14599.47


# # Incluindo o Separador de Milhar (,)
print(f'{valor:,.2f}')  # 14,599.47


# Formatando para o Real Brasileiro (_)
print(f'R$ {valor:_.2f}'.replace('.', ',').replace('_', '.'))
# R$ 14.599,47


# Formatando para Percentual (.2%)
print(f'{2/5}')  # 0.4
print(f'{2/5:.2%}')  # 40.00%
````