from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

tasks = [
    {"id": 0, "title": "Workout at the gym", "done": False},
    {"id": 1, "title": "Go to class", "done": False},
    {"id": 2, "title": "Get some sleep", "done": False}
]

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