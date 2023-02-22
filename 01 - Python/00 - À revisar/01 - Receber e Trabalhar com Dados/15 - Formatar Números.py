# ------------------------------------------------------------------------------------
# Formatar Números
# ------------------------------------------------------------------------------------


faturamento = 15000
custo = 400.53423
lucro = faturamento - custo
margem = lucro / faturamento

# Definindo a Quantidade de Casas Decimais (.2f)
print(f'R$ {lucro}')  # R$ 14599.46577
print(f'R$ {lucro:.2f}')  # R$ 14599.47

# Incluindo o Separador de Milhar (,)
print(f'R$ {lucro:,.2f}')  # R$ 14,599.47

# Formatando para o Real Brasileiro (_)
valor = 153839283.24
valor_formatado = f'R$ {valor:,=_.2f}'.replace('.', ',').replace('_', '.')
print(valor_formatado)  # R$ 153.839.283,24

# Formatando para Percentual (.2%)
print(f'{margem}')  # 0.9732977180000001
print(f'{margem:.2%}')  # 97.33%
