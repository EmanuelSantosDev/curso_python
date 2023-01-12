# Impressão de múltiplas linhas

print('''Até a pé nós iremos,
para o que der e vier,
mas o certo é que nós estaremos,
com o Grêmio, onde o Grêmio estiver!!!''')

# Caracteres de Escape

# nova linha
print('Olá o meu nomé é \nEmanuel Olivio dos Santos')
# não interpreta as aspas internas
print('Codar todos os dias \'deve se tornar\' um hábito')
# desativando o escape da barra "\" com "\\"
print('O arquivo está localizado em \\c:drive\\arquivo1.txt')

# Escape mesclando aspas (') com aspas ("")

print('Vamos "codar"')  # Vamos "codar"

# len()

nome = 'Emanuel Olivio dos Santos'
quantidade_letras = len(nome)
print(quantidade_letras)  # 25
