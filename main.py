from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

tasks = [
    {"id": 0, "title": "Workout at the gym", "done": False},
    {"id": 1, "title": "Go to class", "done": False},
    {"id": 2, "title": "Get some sleep", "done": False}
]

class Task(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

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

@app.put("/tasks/{id}")
async def updateTask(id: int, updates: TaskUpdate):
    if updates.title is None and updates.done is None:
        return JSONResponse(status_code=400, content="error: Empty/Invalid Body")
    for task in tasks:
        if task["id"] == id:
            if updates.title is not None:
                task["title"] = updates.title
            if updates.done is not None:
                task["done"] = updates.done
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"}) 


@app.delete("/tasks/{id}")
async def deleteTask(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return Response(status_code=204)
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})