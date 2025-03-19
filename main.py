from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Field, Session, create_engine, select

# Conexão com banco de dados SQLite
DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL)

app = FastAPI()


# Modelo da Tarefa
class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str = None


# Criar tabelas
def create_db():
    SQLModel.metadata.create_all(engine)


create_db()


# Dependência para sessão do banco
def get_session():
    with Session(engine) as session:
        yield session


@app.post("/tasks/")
def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.get("/tasks/")
def get_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"message": "Task deleted"}
