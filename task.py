from pydantic import BaseModel
from fastapi import HTTPException, FastAPI

app= FastAPI()

class Task(BaseModel):
    id: int
    title: str
    done: bool

tasks = [
    Task(id=1, title="Breakfast", done=False),
    Task(id=2, title="Wash", done=True),
    Task(id=3, title="Pray", done=False)
    ]


@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def show_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")