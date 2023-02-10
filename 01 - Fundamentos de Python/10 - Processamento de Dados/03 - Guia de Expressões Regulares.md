# Guia de Expressões Regulares


**Regex**, **Expressões Regulares** ou **Regular Expression** são padrões utilizados para identificar determinadas combinações caracteres 


## Encontrando o Valor Exato:

    sou

![imagem](img/01.png)




## Encontrando Qualquer Dígito de 0 à 9:

    \d

![imagem](img/02.png)

    \d23

![imagem](img/03.png)



## Coringa para Qualquer Tipo de Caracter

    1..

![imagem](img/04.png)



## Escapando o Ponto

    \....

![imagem](img/05.png)



## Delimitando a Pesquisa

Encontrar todas as palavras com 3 caracteres no total, que iniciam tanto com "o" ou "a", tanto faz o caractere do meio, e finalizam com a letra "a":

    [oa].[a]

![img](img/06.png)



## Encontrando uma Combinação Válida de Telefone

    [(]\d\d[)]\d\d\d\d\d[-]\d\d\d\d

![img](img/07.png)



## Identificando Apenas os Clientes Nacionais com DDI 55

    [5][5][(]\d\d[)]\d\d\d\d\d[-]\d\d\d\d

![img](img/08.png)



## Encontrando Qualquer Combinação que NÃO Inicie com a Letra "v"

    [^v]

![img](img/09.png)


## Identificar os Números cujo DDD NÃO seja "55"

    [(][^5][^5][)]\d\d\d\d[-]\d\d\d\d

![img](img/10.png)


## Identificando uma FAIXA de Valores sem Precisar Digitá-los Individualmente

    [3-7]

![img](img/11.png)


    [e-m]

![img](img/12.png)


## Identificando apenas Letras e Números (que não contém acentos latinos)

O `\w` representa todas as letras de "a" a "z" em maiúsculo ou minúsculo e também todos os números de 0 a 9.

![img](img/13.png)


## Encontrando Repetições de um Padrão mais Rapidamente

    8{5}

![img](img/14.png)

    \d{5}

![img](img/15.png)

    \d{4,6}

![img](img/16.png)


## Encontrando um Padrão de Letras Específicas com uma Quantidade X de Repetições

Neste nosso exemplo queremos encontrar os padrõs **zoe** e **zue**:

    [zueo]{3}

![img](img/17.png)


## Encontrando um Padrão de Repetição Generalista

    .{8}

![img](img/18.png)


