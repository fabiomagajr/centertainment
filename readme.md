
# 🎬 API de Filmes (Movie API)

Uma API RESTful desenvolvida com Django e Django REST Framework para catalogar filmes, diretores, atores e gêneros.

Este projeto está sendo desenvolvido como um exercício prático para aprofundar os conhecimentos em Django e DRF, focando em melhores práticas e em criar uma aplicação funcional.

---

##  STATUS DO PROJETO

- [x] Configuração inicial do projeto (core)
- [x] App principal (movies)
- [x] Modelos (Movie, Actor, Director, Genre, Country)
- [x] Tabela de junção explícita (`MovieActor`)
- [x] Serializers básicos para todos os modelos
- [x] ViewSets e Roteamento para todos os modelos
- [x] Filtros de busca (`SearchFilter`) e ordenação (`OrderingFilter`)
- [ ] Implementar autenticação (ex: Token ou JWT)
- [ ] Escrever testes (unitários e de integração)
- [ ] Documentação da API (Swagger / Redoc)
- [ ] Implementar paginação
- [ ] Otimizar Serializers (relações aninhadas, performance)
- [ ] Adicionar endpoints de estatísticas (ex: Atores com mais prêmios)

---

## 🛠️ Tecnologias Utilizadas

* Python
* Django
* Django REST Framework (DRF)
* SQLite (banco de dados para desenvolvimento)

---

## 🚀 Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    *(É uma boa prática ter um arquivo `requirements.txt`. Se não tiver, crie-o primeiro)*
    
    ```bash
    # Se você ainda não tem o arquivo:
    pip freeze > requirements.txt

    # Para instalar as dependências:
    pip install -r requirements.txt
    ```

---

## 🏃 Como Rodar o Projeto

1.  **Aplique as migrações** para criar as tabelas no banco de dados:
    ```bash
    python manage.py migrate
    ```

2.  **(Opcional) Popule o banco** com dados iniciais (Gêneros e Países):
    *(Assumindo que os comandos `pop_genre` e `pop_country` existem)*
    ```bash
    python manage.py pop_genre
    python manage.py pop_country
    ```

3.  **Crie um superusuário** para acessar o Django Admin:
    ```bash
    python manage.py createsuperuser
    ```

4.  **Inicie o servidor** de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

* A API estará acessível em `http://127.0.0.1:8000/api/movies/`
* O Django Admin estará acessível em `http://127.0.0.1:8000/admin/`

---

## 🗺️ Endpoints da API

O prefixo base para todos os endpoints é `/api/movies/`.

` Endpoint ` Método HTTP ` Descrição `
` :--- ` :--- ` :--- `
` `/api/movies/movies/` `GET, POST` Lista ou cria novos filmes. `
` `/api/movies/movies/<id>/` `GET, PUT, PATCH, DELETE` Detalha, atualiza ou deleta um filme. `
` `/api/movies/directors/` `GET, POST` Lista ou cria novos diretores. `
` `/api/movies/directors/<id>/` `GET, PUT, PATCH, DELETE` Detalha, atualiza ou deleta um diretor. `
` `/api/movies/actors/` `GET, POST` Lista ou cria novos atores. `
` `/api/movies/actors/<id>/` `GET, PUT, PATCH, DELETE` Detalha, atualiza ou deleta um ator. `
` `/api/movies/genres/` `GET, POST` Lista ou cria novos gêneros. `
` `/api/movies/genres/<id>/` `GET, PUT, PATCH, DELETE` Detalha, atualiza ou deleta um gênero. `
` `/api/movies/countries/` `GET, POST` Lista ou cria novos países. `
` `/api/movies/countries/<id>/` `GET, PUT, PATCH, DELETE` Detalha, atualiza ou deleta um país. `
` `/api/movies/movie-actors/` `GET, POST` Lista ou associa atores a filmes. `
` `/api/movies/movie-actors/<id>/` `GET, PUT, PATCH, DELETE` Detalha, atualiza ou deleta uma associação. `