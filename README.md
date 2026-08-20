# Task API

A REST API for Flyrank AI Internship, with the purpose of managing a task to-do list, built with [FastAPI](https://fastapi.tiangolo.com/). Each task has an int `id`, str `title`, and bool `done` status and these task are not stored in a database as of yet.

## Install
Uses [`uv`](https://docs.astral.sh/uv/) for dependency management.

```bash
cd "project"
uv sync
```

## Run

```bash
uv run fastapi dev main.py
```
The API is accessible at `http://localhost:8000`, with interactive Swagger document at `http://localhost:8000/docs`.

![Swagger UI](docs/SwaggerUI.png)

## Endpoints

| Method | Path | Description | Success | Errors |
|---|---|---|---|---|
| GET | `/` | API metadata - Returns a JSON that describes the Task API  | 200 | — |
| GET | `/health` | Health check | 200 | — |
| GET | `/tasks` | List all tasks | 200 | — |
| GET | `/tasks/{id}` | Gets a task by id | 200 | 404 |
| POST | `/tasks` | Creates a task (`{"title": "..."}`) | 201 | 422 |
| PUT | `/tasks/{id}` | Updates a task's `title` (str) and/or `done` (bool) | 200 | 400, 404 |
| DELETE | `/tasks/{id}` | Deletes a task by id | 204 | 404 |

## Example

```
$ curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'

HTTP/1.1 201 Created
date: Wed, 19 Aug 2026 22:20:46 GMT
server: uvicorn
content-length: 40
content-type: application/json

{"id":3,"title":"Buy milk","done":false}
```
