from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()

tasks = [
    {"id": 0, "title": "Workout at the gym", "done": False},
    {"id": 1, "title": "Go to class", "done": False},
    {"id": 2, "title": "Get some sleep", "done": False}
]

class Task(BaseModel):
    title: str

@app.get("/")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/tasks")
async def task():
    return tasks


@app.get("/tasks/{id}")
async def getTaskByID(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

@app.post("/tasks", status_code=201)
async def createTask(task: Task):
    next_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": next_id, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task