# Grape Schools Backend

Este projeto tem como objetivo gerir as regras de negócio de escolas usando FastAPI como framework principal e PostgreSQL como banco relaiconal, Autenticação JWT e muito mais.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Python >= 3.10.6
PostgreSQL >= 14.0 | Docker
```

### 🔧 Instalação com Docker

Estamos preparando isso

### 🔧 Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Clone o Projeto com:

```
git clone https://github.com/grape-erp/grape-schools-backend.git --branch=develop grape-schools-backend
```

Crie seu ambiente virtual:

```
python3 -m venv venv
```

Instale as Bibliotecas:

```
pip3 install -r requirements.txt
```

Use o script de debug do VScode:

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```

Ou inicie o projeto com :

```
uvicorn main:app
```

Caso queira inicializar o banco de dados, use :

```
python3 initial_data.py
```

Preparar Migrations:

```
alembic revision --autogenerate -m "Your Migration"
```

Aplicar Migrations:

```
alembic upgrade head
```

* OBS: Não esqueça de configurar seu banco PostgreSQL

Assim que o projeto inicializar com sucesso na porta padrão 8000, acesse: http://localhost:8000/docs#/

## ⚙️ Executando os testes

Para executar os testes você deve instalar as dependências de teste e executar os seguintes comandos abaixo:

Instalar dependências de teste:

```
pip3 install -r requirements_test.txt
```

Rodar testes no modo verboso:

```
pytest -vv
```


## 📦 Implantação

Em breve como fazer deploy automático

## 🛠️ Construído com

O projeto foi construído com as seguintes tecnologias principais

* [Python](http://www.dropwizard.io/1.0.2/docs/) - Linguagem de Porgramação
* [FastAPI](https://maven.apache.org/) - Framework Web
* [PostgreSQL](https://rometools.github.io/rome/) - Sistema Gerenciador de Banco de Dados

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores


* **Daniel Nery** - *Desenvolvedor* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Luan Petruitis** - *Desenvolvedor* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.


---
⌨️ com ❤️ por Grape