# Venv - Ambiente Virtual

- São úteis para isolar as dependências de cada projeto individualmente.
- Se utilizarmos o comando ``pip list`` ao abrir o terminal irá mostrar todos os pacotes instalados globalmente.


## PowerShell - Bloqueio para Execução de Scripts

- Por padrão o PowerShell possui um bloqueio para a execução de scripts.  
- ``Set-ExecutionPolicy`` define as políticas de execução do PowerShell para computadores Windows. 


### Como habilitar a permissão para a execução de scripts

    (Abrir PowerShell como Administrador)
    Set-ExecutionPolicy Unrestricted -Force

## Criando o Ambiente Virtual

Navegar no PowerShell até o diretório que deseja iniciar o projeto:

    python -m venv [nome_ambiente_virtual]

## Ativando o Ambiente Virtual

    [nome_ambiente_virtual}\Scripts\activate

## Criando a Lista de Requisitos de Dependências

    pip freeze > requirements.txt

## Desativando o Ambiente Virtual

    deactivate

## Instalando as Dependências Definidas em requirements.txt

    pip install -r requirements.txt
