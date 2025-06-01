# Gym App API - MVP

Bem-vindo à API do Gym App! Este é o backend para o aplicativo de acompanhamento de treinos de academia, versão MVP (Produto Mínimo Viável).

## 🚀 Sobre o Projeto

Esta API é responsável por gerenciar utilizadores, definições de exercícios, registo de treinos e outras funcionalidades essenciais para o aplicativo mobile Gym App.

## 🛠️ Tecnologias Utilizadas

* **Python 3.9+**
* **FastAPI:** Framework web para construção de APIs.
* **SQLAlchemy:** ORM para interação com a base de dados.
* **Pydantic:** Validação de dados.
* **PostgreSQL:** Base de dados relacional.
* **Docker & Docker Compose:** Para containerização e orquestração dos serviços.
* **Alembic:** Para migrações da base de dados.
* **Uvicorn:** Servidor ASGI para FastAPI.

## 📋 Pré-requisitos

* [Docker](https://docs.docker.com/get-docker/) instalado.
* [Docker Compose](https://docs.docker.com/compose/install/) instalado.

## ⚙️ Configuração e Execução

1.  **Clone o repositório (se ainda não o fez):**
    ```bash
    git clone <url-do-seu-repositorio>
    cd gym_app_backend # Ou o nome da pasta do seu backend
    ```

2.  **Crie o arquivo de ambiente `.env`:**
    Copie o arquivo de exemplo `.env.example` para um novo arquivo chamado `.env`:
    ```bash
    cp .env.example .env
    ```
    Abra o arquivo `.env` e **altere a `SECRET_KEY`** para um valor seguro e único. Pode também ajustar outras configurações se necessário (como as credenciais da base de dados, embora as padrão do `docker-compose.yml` devam funcionar localmente).

3.  **Construa e execute os containers Docker:**
    A partir da raiz do diretório do backend (`gym_app_backend/`), execute:
    ```bash
    docker-compose up --build
    ```
    * O parâmetro `--build` é necessário na primeira vez ou quando houver alterações no `Dockerfile` ou `requirements.txt`.
    * Para executar em background (modo detached), adicione `-d`: `docker-compose up --build -d`.

4.  **Acesse a API:**
    * A API estará disponível em: `http://localhost:8001` (ou a porta que configurou no `docker-compose.yml`).
    * Documentação interativa (Swagger UI): `http://localhost:8001/docs`
    * Documentação alternativa (ReDoc): `http://localhost:8001/redoc`
    * Health check: `http://localhost:8001/health`

## 🗄️ Migrações da Base de Dados (Alembic)

Este projeto utiliza [Alembic](https://alembic.sqlalchemy.org/) para gerenciar as migrações do esquema da base de dados.

* **Configurar o Alembic (se for a primeira vez):**
    1.  Verifique se o `alembic.ini` está configurado com a URL correta da base de dados (geralmente `sqlalchemy.url = %(DATABASE_URL)s` e a variável `DATABASE_URL` é passada).
    2.  Certifique-se que o `env.py` do Alembic (`alembic/env.py`) importa os seus modelos SQLAlchemy (`from app.models import Base` e `target_metadata = Base.metadata`).

* **Criar uma nova revisão de migração (após alterações nos modelos SQLAlchemy):**
    ```bash
    docker-compose exec api alembic revision -m "descricao_da_sua_migracao"
    ```
    Isto irá gerar um novo ficheiro de migração na pasta `alembic/versions/`. Edite este ficheiro para definir as operações de `upgrade` e `downgrade`.

* **Aplicar as migrações à base de dados:**
    ```bash
    docker-compose exec api alembic upgrade head
    ```

* **Reverter uma migração (exemplo):**
    ```bash
    docker-compose exec api alembic downgrade -1
    ```

## 📂 Estrutura do Projeto (Simplificada)

```
gym_app_backend/
├── app/                      # Diretório principal da aplicação FastAPI
│   ├── core/                 # Configurações centrais (ex: settings)
│   ├── db/                   # Configuração da base de dados, sessões
│   ├── models/               # Modelos SQLAlchemy (tabelas da base de dados)
│   ├── schemas/              # Esquemas Pydantic (validação e serialização)
│   ├── apis/                 # Módulos de API e routers (a ser preenchido)
│   ├── crud/                 # Funções de Create, Read, Update, Delete (a ser preenchido)
│   ├── deps.py               # Dependências reutilizáveis (ex: get_current_user)
│   └── main.py               # Ponto de entrada da aplicação FastAPI
├── alembic/                  # Configurações e versões de migração do Alembic
├── alembic.ini               # Ficheiro de configuração do Alembic
├── Dockerfile                # Define a imagem Docker para a API
├── docker-compose.yml        # Orquestra os serviços (API e base de dados)
├── requirements.txt          # Dependências Python
├── .env.example              # Exemplo de ficheiro de variáveis de ambiente
└── README.md                 # Este ficheiro
```

## 🔗 Endpoints da API

Para uma visão detalhada de todos os endpoints disponíveis, parâmetros e respostas, consulte a documentação interativa gerada pelo FastAPI:

* **Swagger UI:** `http://localhost:8001/docs`
* **ReDoc:** `http://localhost:8001/redoc`
