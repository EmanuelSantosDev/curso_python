# Introdução à APIs


## O que são APIs?


**API** significa "Interface de Programação de Aplicativos" (em inglês, "Application Programming Interface"). Em resumo, é um conjunto de regras, protocolos e ferramentas que permitem que diferentes aplicativos se comuniquem e compartilhem informações entre si.

As APIs são usadas para facilitar a integração de diferentes sistemas e aplicativos, permitindo que desenvolvedores de software utilizem as funcionalidades de outros sistemas em seus próprios aplicativos. Com isso, é possível criar aplicativos mais complexos e ricos em recursos, sem a necessidade de recriar todas as funcionalidades já existentes em outros sistemas.

## As APIs possuem 4 partes:

1. **URL Base**
    - é a parte inicial de uma URL que identifica o domínio e o protocolo de um site ou aplicação web.
    - Exemplo: **https://api.exemplo.com/**.
1. **Endpoint** 
    - é um ponto final de uma comunicação entre duas ou mais aplicações.
    - é o endereço web (URL) que uma aplicação pode acessar para interagir com outra aplicação ou serviço web.
    - cada endpoint possui um **método HTTP** associado que define o tipo de interação que pode ser realizada com o endpoint.
    - Exemplo: **https://api.exemplo.com/cotacao**.
1. **Recurso** 
    - é tudo que é retornado ou enviado a uma api.
    - pode ser qualquer coisa, desde um documento até uma imagem, vídeo ou um conjunto de dados estruturados.
1. **Verbos HTTP** 
    - **GET**: solicita dados ou recursos de um servidor. Por exemplo, um cliente pode usar o método GET para obter informações de uma página web ou para buscar dados de uma API.
    - **POST**: envia dados ou recursos para serem processados por um servidor. Por exemplo, um cliente pode enviar um formulário preenchido para um servidor usando o método POST para criar um novo registro ou atualizar um registro existente em um banco de dados.
    - **PUT**: atualiza um recurso existente no servidor. Por exemplo, um cliente pode usar o método PUT para atualizar uma página da web ou um registro em um banco de dados.
    - **DELETE**: exclui um recurso do servidor. Por exemplo, um cliente pode usar o método DELETE para remover uma página da web ou um registro de um banco de dados.


## Status Code

**Status code (código de status)** é um número de três dígitos que é retornado pelo servidor em resposta a uma solicitação do cliente. Ele fornece informações sobre o resultado da solicitação, indicando se ela foi bem-sucedida ou não, e se houve algum erro ou problema na comunicação.

Os status code são divididos em cinco classes, de acordo com o primeiro dígito do código:

- **1xx: informações** - Indica que a solicitação foi recebida e o servidor continua processando-a.
- **2xx: sucesso** - Indica que a solicitação foi bem-sucedida e o servidor conseguiu processá-la sem problemas.
- **3xx: redirecionamento** - Indica que a solicitação precisa ser redirecionada para outro recurso ou servidor.
- **4xx: erro do cliente** - Indica que a solicitação contém erros ou não pôde ser processada pelo servidor por problemas causados pelo cliente.
- **5xx: erro do servidor** - Indica que o servidor encontrou um erro ao processar a solicitação do cliente.

Alguns exemplos comuns de status code incluem:

- **200 OK**: indica que a solicitação foi bem-sucedida e o servidor retornou uma resposta.
- **400 Bad Request**: indica que a solicitação contém informações inválidas ou não pode ser processada pelo servidor.
- **404 Not Found**: indica que o recurso solicitado não foi encontrado no servidor.
- **500 Internal Server Error**: indica que ocorreu um erro interno no servidor ao processar a solicitação do cliente.

O uso correto dos status code é importante para garantir uma comunicação clara e consistente entre o cliente e o servidor em uma API. Eles permitem que os desenvolvedores identifiquem rapidamente os problemas e solucionem os erros na comunicação.


### Status Code no Navegador


Para visualizar na prática aperte **F12** em qualquer site e navegue até a aba **network (rede)**.