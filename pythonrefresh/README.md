````markdown
# FastAPI Todo App

A simple CRUD API built with **FastAPI**, showcasing basic todo management.

## Features
- Create todos (`POST /todos`)
- Read todos (`GET /todos`, `GET /todos/{id}`)
- Update todos (`PUT /todos/{id}`)
- Delete todos (`DELETE /todos/{id}`)
- Auto-generated API docs via FastAPI Swagger UI (`/docs`)


## Getting Started

### Prerequisites

- Python 3.11+
- FastAPI
- Uvicorn

### Install Dependencies

```bash
pip install fastapi uvicorn
````

### Run the App

```bash
uvicorn app:app --reload
```

The API will be available at: `http://127.0.0.1:8000/`

### API Documentation

Visit Swagger UI: `http://127.0.0.1:8000/docs`

### Example Todo JSON

```json
{
  "title": "Learn FastAPI",
  "completed": false
}
```

---


### Example Requests

**Create Todo (POST)**

```
POST /todos
Content-Type: application/json

{
  "title": "Learn FastAPI",
  "completed": false
}
```

**Get All Todos (GET)**

```
GET /todos
```

**Get Single Todo (GET)**

```
GET /todos/1
```

**Update Todo (PUT)**

```
PUT /todos/1
Content-Type: application/json

{
  "title": "Updated Todo",
  "completed": true
}
```

**Delete Todo (DELETE)**

```
DELETE /todos/1
```

---

