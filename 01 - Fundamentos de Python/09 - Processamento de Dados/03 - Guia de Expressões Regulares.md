# Guia de Expressões Regulares


**Regex**, **Expressões Regulares** ou **Regular Expression** são padrões utilizados para identificar determinadas combinações caracteres 


## Tabela Resumo

|Caractere|Ação de Captura|
|:---:|:-----|
|.| representa qualquer caracter menos "\n"|
|\\.| escapando o caractere "."|
|[ ]| representa qualquer valor contido dentro (conjunto de possibilidades)|
|^| representa o inicio da string|
|$| representa o final da string|
|[^]| diferente de um caractere|
|\w| é alfanumérico (não considera caracteres latinos como "ç" e "ã")|
|\W| não é alfanumérico|
|\s| caracter vazio|
|\S| caracter NÃO vazio|
|\d| números de 0 a 9|
|\D| tudo que NÃO é número|
|[1-9]| range de números
|[a-z]| range de letras minúsculas|
|[A-Z]| range de letras maiúsculas|
|[a-cA-Z1-5]| mesclando os ranges ( a-c + A-Z + 1-5 )|
|+| uma ou mais vezes|
|*| zero ou mais vezes|
|?| zero ou uma vez|
|\\?| escapando o caractere "?"|
|{x}| se repete "x" vezes|
|{x, y}| mínino de "x" e máximo de "y" repetições|
|( )|  captura subgrupos|
|\||  condicional OU. Exemplo: (com\\.br\|com)|

---
## Encontrando o Valor Exato:

    sou

![imagem](img/01.png)


---
## Encontrando Qualquer Dígito de 0 à 9:

    \d

![imagem](img/02.png)

    \d23

![imagem](img/03.png)


---
## Coringa para Qualquer Tipo de Caracter

    1..

![imagem](img/04.png)


---
## Escapando o Ponto

    \....

![imagem](img/05.png)


---
## Delimitando a Pesquisa

Encontrar todas as palavras com 3 caracteres no total, que iniciam tanto com "o" ou "a", tanto faz o caractere do meio, e finalizam com a letra "a":

    [oa].[a]

![img](img/06.png)


---
## Encontrando uma Combinação Válida de Telefone

    [(]\d\d[)]\d\d\d\d\d[-]\d\d\d\d

![img](img/07.png)


---
## Identificando Apenas os Clientes Nacionais com DDI 55

    [5][5][(]\d\d[)]\d\d\d\d\d[-]\d\d\d\d

![img](img/08.png)


---
## Encontrando Qualquer Combinação que NÃO Inicie com a Letra "v"

    [^v]

![img](img/09.png)


---
## Identificar os Números cujo DDD NÃO seja "55"

    [(][^5][^5][)]\d\d\d\d[-]\d\d\d\d

![img](img/10.png)


---
## Identificando uma FAIXA de Valores sem Precisar Digitá-los Individualmente

    [3-7]

![img](img/11.png)


    [e-m]

![img](img/12.png)


---
## Identificando Caracteres Alfanuméricos (que não contém acentos latinos)

O `\w` representa todas as letras de "a" a "z" em maiúsculo ou minúsculo e também todos os números de 0 a 9.

    \w

![img](img/13.png)


---
## Identificando Caracteres NÃO Alfanuméricos 

    \W

![img](img/33.png)

---
## Encontrando Repetições de um Padrão mais Rapidamente

    8{5}

![img](img/14.png)

    \d{5}

![img](img/15.png)

    \d{4,6}

![img](img/16.png)


---
## Encontrando um Padrão de Letras Específicas com uma Quantidade X de Repetições

Neste nosso exemplo queremos encontrar os padrõs **zoe** e **zue**:

    [zueo]{3}

![img](img/17.png)


---
## Encontrando um Padrão de Repetição Generalista

    .{8}

![img](img/18.png)


---
## Encontrando Uma ou mais Repetições

O caractere que precede o sinal de ``+`` pode ocorrer 1 ou mais vezes:

    de+

![img](img/19.png)


---
## Encontrando Combinações Onde o "Restante" (antes ou depois) pode ser Qualquer Combinação

    enc.*

![img](img/20.png)


    .*cont

![img](img/21.png)


---
## Pode ou Não Ter o Caractere que Precede

Pode ou Não Ter o Caractere que Precede o "?"

    arquivos?

![img](img/22.png)


Neste segundo exemplo, a primeira palavra pode ou não estar no plural, porém, a segunda obrigatoriamente tem que estar no plural:

    arquivos? baixados

![img](img/24.png)


---
## Escapando o "?"

    \?

![img](img/23.png)


---
## Identificando Espaços em Branco


**Espaço Simples**

    *inserir literalmente um ou mais espaços em branco*

![img](img/25.png)

**Nova Linha**

    \n

![img](img/26.png)

**Tab**

O VSCode não consegue identificar, mas funciona no código:

    \t

**Enter** 

O VSCode não consegue identificar, mas funciona no código:

    \r

**Qualquer Tipo de Espaço em Branco** 

    \s

![img](img/27.png)


---
## Combinando Caracteres com Espaço em Branco

Padrão que queremos encontrar: _dígito + ponto + um ou mais espaços em branco + olá_

    \d\.\s+olá

![img](img/28.png)


---
## Declarando Inicio e Fim

Utilizamos delimitadores que criam um regex mais preciso:

    ^hora de codar$

![img](img/29.png)


---
## Capturando Grupos

Capturando grupos de caracteres que contenham: _imagem + qualquer sequência de caracteres + ponto + jpg_

    (imagem.+\.)(jpg)

![img](img/30.png)


---
## Capturando um Subgrupo

Encontrando e-mails com final **"com OU com.br"** (temos dois subgrupos):

    (\w+)(@\w+\.)(com\.br|com)

![img](img/31.png)


---
## Capturando os 3 Grupos de um Telefone:

    ([(]\d{2}[)])(\d{5})([-]\d{4})

![img](img/32.png)