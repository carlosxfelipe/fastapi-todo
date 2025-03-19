# FastAPI Task Manager

Este é um projeto simples de **gerenciador de tarefas** usando **FastAPI** e **SQLite**. Ele permite criar, listar e excluir tarefas por meio de uma API REST, garantindo **persistência de dados**.

## 🚀 Como rodar o projeto

1. **Criar e ativar um ambiente virtual** (recomendado):

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # No macOS/Linux
   venv\Scripts\activate  # No Windows
   ```

2. **Instalar as dependências**:

   ```sh
   pip install fastapi uvicorn sqlmodel sqlite
   ```

3. **Executar o servidor**:

   ```sh
   uvicorn main:app --reload
   ```

4. **Acessar a API**:
   - Documentação Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Documentação Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 Endpoints da API

### 🔹 Criar uma tarefa

- **Rota:** `POST /tasks/`
- **Corpo da requisição (JSON):**
  ```json
  {
    "title": "Minha nova tarefa",
    "description": "Descrição da tarefa"
  }
  ```
- **Resposta:**
  ```json
  {
    "id": 1,
    "title": "Minha nova tarefa",
    "description": "Descrição da tarefa"
  }
  ```

### 🔹 Listar todas as tarefas

- **Rota:** `GET /tasks/`
- **Resposta:**
  ```json
  [
    {
      "id": 1,
      "title": "Minha nova tarefa",
      "description": "Descrição da tarefa"
    }
  ]
  ```

### 🔹 Buscar uma tarefa específica

- **Rota:** `GET /tasks/{task_id}`
- **Exemplo:** `GET /tasks/1`
- **Resposta:**
  ```json
  {
    "id": 1,
    "title": "Minha nova tarefa",
    "description": "Descrição da tarefa"
  }
  ```

### 🔹 Excluir uma tarefa

- **Rota:** `DELETE /tasks/{task_id}`
- **Exemplo:** `DELETE /tasks/1`
- **Resposta:**
  ```json
  {
    "message": "Task deleted"
  }
  ```

## 🐋 Construir a imagem Docker

No terminal, dentro do diretório do projeto, execute:

```json
docker build -t task-api .

```

Agora, execute a aplicação com:

```json
docker run -p 8000:8000 task-api
```

### Persistência do Banco de Dados

Atualmente, seu banco de dados SQLite `(tasks.db)` está dentro do contêiner. Isso significa que, sempre que o contêiner for removido, os dados serão apagados.

**📌 Solução: Usar um volume Docker para persistir o banco fora do contêiner.**

Agora, ao rodar o contêiner, use:

```json
docker run -p 8000:8000 -v $(pwd)/tasks.db:/app/tasks.db task-api
```

Isso faz com que:

- O arquivo `tasks.db` seja armazenado na máquina **fora do contêiner**.
- Mesmo se o contêiner for removido, o banco continuará intacto.

## 🛠 Tecnologias utilizadas

### 🔹 Backend

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework rápido para APIs
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI para FastAPI
- **[SQLModel](https://sqlmodel.tiangolo.com/)** - ORM leve baseado em SQLAlchemy e Pydantic
- **[SQLite](https://www.sqlite.org/)** - Banco de dados embutido
- **[Docker](https://www.docker.com/)** - Containerização para facilitar a execução da aplicação

### 🎨 Frontend

- **HTML5** - Estrutura da aplicação
- **CSS3** - Estilização e layout
- **JavaScript (ES6+)** - Funcionalidade e interatividade

---

Criado para fins de aprendizado 🚀
