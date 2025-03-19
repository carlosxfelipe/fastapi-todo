from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Estrutura da Tarefa
class Task(BaseModel):
    title: str
    description: str = None


# Banco de dados fictício (em memória)
tasks = {}
task_id_counter = 1


@app.post("/tasks/")
def create_task(task: Task):
    global task_id_counter
    task_id = task_id_counter
    tasks[task_id] = task
    task_id_counter += 1
    return {"task_id": task_id, **task.dict()}


@app.get("/tasks/")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}
