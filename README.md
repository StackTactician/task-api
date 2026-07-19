# Task API

This is a simple task manager API. It exposes CRUD (Create, Read, Update, Delete) endpoints using the four core HTTP methods. Built with FastAPI, it stores the task list in memory, meaning all data is lost when the server restarts, since there's no database yet.

## Install & Run

1. Install dependencies:
```bash
   pip install fastapi "uvicorn[standard]"
```

2. Start the server:
```bash
   python -m uvicorn task:app --reload
```

3. Open in your browser:
   - API: http://localhost:8000
   - Interactive docs (Swagger UI): http://localhost:8000/docs

## Endpoints

| Method | Path        | Description                    |
|--------|-------------|---------------------------------|
| GET    | /           | API info                       |
| GET    | /health     | Health check                   |
| GET    | /tasks      | List all tasks                 |
| GET    | /tasks/{id} | Get a single task              |
| POST   | /tasks      | Create a new task              |
| PUT    | /tasks/{id} | Update a task (title and done) |
| DELETE | /tasks/{id} | Delete a task                  |

## Example Request
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{\"title\":\"Buy milk\"}"

Response:
HTTP/1.1 201 Created
date: Sun, 19 Jul 2026 09:47:15 GMT
server: uvicorn
content-length: 40
content-type: application/json

{"id":4,"title":"Buy milk","done":false}