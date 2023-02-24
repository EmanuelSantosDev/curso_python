# Seletores CSS

````css
/* Todos os Elementos */
* {}

/* Seletor de Tag */
p {}

/* Seletor de Descendente */
body div section p {}

/* Seleção Múltipla */
h1,
p {}

/* Seletor de Classe */
.meu-paragrafo {}

/* Seletor de Classe com Maior Especificidade */
p.meu-paragrafo {}

/* Seletor de Elemento com Múltiplas Classes (sem espaço) */
.meu-paragrafo.texto-princial {}

/* Selecionando o Filho Direto (Child Combinator) */
.pai>.filha {}

/* Seletor de Irmão Adjacente ('p' que é irmão de 'h1') */
h1+p {}

/* Seletor para Todos os Irmãos (todos os 'p' que são irmãos de 'h1' */
h1~p {}

/* Seletor de Atributo Próprio (criado) */
[meu-atributo] {}

/* Seletor de Atributo Próprio + Valor */
[meu-atributo="valor"] {}

/* Seletor de Atributo Padrão */
[type] {}

/* Seletor de Atributo que possui Múltiplos Valores */
[meu-atributo~="valor1"] {}
````