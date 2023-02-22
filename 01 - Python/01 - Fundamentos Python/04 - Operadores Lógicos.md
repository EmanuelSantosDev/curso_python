# Operadores Lógicos


```python
idade = 22
possui_convite = False
filho_do_dono = True


# operadores AND e OR
print(idade >= 21 and possui_convite)  # False
print(idade >= 21 or possui_convite)  # True


# múltiplas condições
print((idade > 21 and possui_convite) or filho_do_dono)  # True


# operador NOT (operador de negação)
possui_carteira_de_trabalho = True
possui_veiculo_proprio = False
print(possui_carteira_de_trabalho and not possui_veiculo_proprio)  # True
```