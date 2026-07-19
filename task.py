from pydantic import BaseModel
from fastapi import HTTPException, FastAPI

app= FastAPI()

@app.get("/", summary="General API info.")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health",  summary="Health check.")
def health():
    return {"status": "ok"}

class Task(BaseModel):
    id: int
    title: str
    done: bool

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

tasks = [
    Task(id=1, title="Breakfast", done=False),
    Task(id=2, title="Wash", done=True),
    Task(id=3, title="Pray", done=False)
    ]


@app.get("/tasks", summary="List all tasks.")
def get_tasks():
    return tasks

@app.get("/tasks/{id}", summary="Show a single task.")
def show_task(id: int):
    for task in tasks:
        if task.id == id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

@app.post("/tasks", status_code=201, summary="Add a new task.")
def create_task(new_task: TaskCreate):
    if new_task.title == "" or new_task.title is None:
        raise HTTPException(status_code=400, detail="Invalid Task.")
    new_task_id = max(task.id for task in tasks) + 1
    created_task = Task(id=new_task_id, title = new_task.title, done=False)
    tasks.append(created_task)
    return created_task

@app.put("/tasks/{id}", summary="Update a task.")
def update_task(id: int, updated_task: TaskUpdate):
    if updated_task.title == "" or updated_task.title is None:
        raise HTTPException(status_code=400, detail="Invalid Update.")
    for task in tasks:
        if task.id == id:
            task.title = updated_task.title
            task.done = updated_task.done
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

@app.delete("/tasks/{id}", status_code=204, summary="Delete a task.")
def delete_task(id: int):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return
    raise HTTPException(status_code=404, detail="No task to delete.")