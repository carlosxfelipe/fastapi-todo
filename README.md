# FastAPI Task Manager

Este é um projeto simples de **gerenciador de tarefas** usando **FastAPI**. Ele permite criar, listar e excluir tarefas por meio de uma API REST.

## 🚀 Como rodar o projeto

1. **Criar e ativar um ambiente virtual** (opcional, mas recomendado):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # No macOS/Linux
   venv\Scripts\activate  # No Windows
   ```

2. **Instalar as dependências**:
   ```sh
   pip install fastapi uvicorn
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
    "task_id": 1,
    "title": "Minha nova tarefa",
    "description": "Descrição da tarefa"
  }
  ```

### 🔹 Listar todas as tarefas
- **Rota:** `GET /tasks/`
- **Resposta:** 
  ```json
  {
    "1": {
      "title": "Minha nova tarefa",
      "description": "Descrição da tarefa"
    }
  }
  ```

### 🔹 Buscar uma tarefa específica
- **Rota:** `GET /tasks/{task_id}`
- **Exemplo:** `GET /tasks/1`
- **Resposta:**
  ```json
  {
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

## 🛠 Tecnologias utilizadas
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework rápido para APIs
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI para FastAPI

---
Criado para fins de aprendizado 🚀
