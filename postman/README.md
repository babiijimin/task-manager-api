

## Postman Setup

This folder contains:
- Postman collection for testing the API.
- Environment variables (e.g., base URL)


### How to Use Collection
📂 You can find it inside the `postman/` folder:  
- `postman/todos_api_collection.json`

1. Open **Postman**.
2. Go to **File → Import**.
3. Select the file: `postman/todos_api_collection.json`.
4. The collection will appear in your sidebar under **Collections**.
5. Make sure your backend server is running:
   ```bash
   uvicorn app:app --reload
    ```

6. Run the saved requests against your local server:
   `http://127.0.0.1:8000`
---

### How to Use Environment
1. Import `local-fastapi.postman_environment.json` into Postman.
2. Switch environment to **Local - FastAPI** before sending requests

---

### API Endpoints Overview

| Method | Endpoint      | Description             | Example Body (if needed)       |
| ------ | ------------- | ----------------------- | ------------------------------ |
| GET    | `/todos`      | Get all todos           | —                              |
| GET    | `/todos/{id}` | Get a single todo by ID | —                              |
| POST   | `/todos`      | Create a new todo       | `{ "title": "Learn FastAPI" }` |
| PUT    | `/todos/{id}` | Update an existing todo | `{ "title": "Updated title" }` |
| DELETE | `/todos/{id}` | Delete a todo by ID     | —                              |

---