

## Postman Collection

This project includes a Postman collection for testing the API.

📂 You can find it inside the `postman/` folder:  
- `postman/todos_api_collection.json`

### How to Use
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

### API Endpoints Overview

| Method | Endpoint      | Description             | Example Body (if needed)       |
| ------ | ------------- | ----------------------- | ------------------------------ |
| GET    | `/todos`      | Get all todos           | —                              |
| GET    | `/todos/{id}` | Get a single todo by ID | —                              |
| POST   | `/todos`      | Create a new todo       | `{ "title": "Learn FastAPI" }` |
| PUT    | `/todos/{id}` | Update an existing todo | `{ "title": "Updated title" }` |
| DELETE | `/todos/{id}` | Delete a todo by ID     | —                              |

---