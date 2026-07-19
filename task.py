from pydantic import BaseModel
from fastapi import HTTPException, FastAPI

app= FastAPI()

@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}

class Task(BaseModel):
    id: int
    title: str
    done: bool

class TaskCreate(BaseModel):
    title: str

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

@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
    if new_task.title == "" or new_task.title is None:
        raise HTTPException(status_code=400, detail="Invalid Task.")
    new_task_id = max(task.id for task in tasks) + 1
    created_task = Task(id=new_task_id, title = new_task.title, done=False)
    tasks.append(created_task)
    return created_task