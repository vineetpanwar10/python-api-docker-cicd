from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Simple Task API")


class Task(BaseModel):
    title: str


tasks = []


@app.get("/")
def home():
    return {"message": "Task API is running"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def add_task(task: Task):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title
    }
    tasks.append(new_task)
    return new_task


@app.get("/config")
def get_config():
    return {"environment": os.getenv("APP_ENV", "development")}
