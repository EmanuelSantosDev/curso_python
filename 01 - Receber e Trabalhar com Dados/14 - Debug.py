# Debug


# F9  - Marcar um breakpoint
# F5  - Abrir modo debug
# F10 - Passar sobre uma linha SEM entrar em métodos internos
# F11 - Passar sobre uma linha e ENTRAR em métodos internos

# <<<< DEBUG CONSOLE >>>>
# Muito útil para digitar o nome de uma variável e verificar seu valor atual


# código para testar o debug
print('Olá')


def calcular_preco_combo(pizza, refrigerante):
    total = pizza + refrigerante
    print(total)


calcular_preco_combo(30, 'vinte reais')
print('Programa finalizado')
