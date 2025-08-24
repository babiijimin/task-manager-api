# Imports

    #Imports the FastAPI class from the FastAPI library. This class lets you build an API app.
from fastapi import FastAPI

    # FastAPI uses Pydantic models to validate and parse request data (like JSON from Postman).
        #..so if a client sends bad JSON, FastAPI will automatically reject it with a helpful error message.
from pydantic import BaseModel

from fastapi import HTTPException


app = FastAPI()  #Creates an instance of the FastAPI application; #This app object is what Uvicorn uses to run your server.





# Data model for incoming todo; this defines the shape of data a client must send when creating a new todo
class Todo(BaseModel):
    task: str   # required field (must be a string)
    done: bool = False  # optional (defaults to false if not provided)

# Note: when you POST a new todo, you only need to send { "task": "something" }




# Fake database (in-memory list); # Creates a Python list of dictionaries — each dictionary is a fake "todo item" with an id, a task, and a done status
    # Later youd replace this with a real database
todos = [
        {"id": 1, "task": "Learn FastAPI", "done": False},
        {"id": 2, "task": "Build my first API", "done": False},
        {"id": 3, "task": "Push to GitHub", "done": True},
]


#-----------------------------------------

#Creating Core Endpoints & /todos routes:

# Read root (get)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"} #The function returns JSON.


# Get todos (get)
@app.get("/todos") # New /todos endpoint: This is a route decorator; tells FastAPI: When a GET request is made to /, call this function.
def get_todos():  # defines the function that will run when someone visits /; Another route. This time for GET requests to /todos
    return {"todos": todos} # Returns the todos inside another dictionary. So the JSON has a top-level key "todos" whose value is the list.
    

# Get todos by Id 
@app.get("/todos/{todo_id}") # whenever someone makes a GET request to /todos/anything-here, capture that as todo_id.”
def get_todo(todo_id: int): # FastAPI automatically converts the path parameter to an integer. If someone passes a string, FastAPI will return a validation error.
   
    # Loop through the in-memory todos list to find the matching one; If found → return it as JSON
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    # If not → raise a 404 error
    raise HTTPException(status_code=404, detail="Todo not found")


# Create todo function (post)
@app.post("/todos") # says “when someone sends a POST request to /todos, run this function.

# Function exp: 
# 1. FastAPI will take the JSON body from the request,
# 2. validate it against the Todo model,
# 3. passes it in as a todo object
def create_todo(todo: Todo):    
   # OLD: new_id = len(todos) + 1 -> creates a new unique id: this didnt consider case of entry deletion and add a new one(it would use same id)
    #new logic:
    new_id = max([t["id"] for t in todos], default=0) +1
    new_todo = {"id": new_id, **todo.model_dump()}    # converts the Pydantic model into a dictionary
    todos.append(new_todo)  # adds it to our "database"
    return new_todo # sends the newly created todo back in the response

# !! Note: 
# Basically...This endpoint lets a client send a new todo (with just a task name).
# FastAPI checks the data, gives it a new ID, saves it in memory, and sends it back



# -- NEW ENDPOINTS --

# Update a Todo
@app.put("/todos/{todo_id}")
    # in POST route, we use "todo: Todo" because we are creating a new todo.
    # in PUT route, we are updating an existing todo. The request body is still a Todo object, 
        # but to make code more readable and avoid confusion with the existing todos list, it is called updated_todo.
def update_todo(todo_id: int, updated_todo: Todo):  # -- takes both the path parameter (todo_id) and a JSON body (updated_todo)
    for t in todos:
        if t["id"] == todo_id:
            t["task"] = updated_todo.task
            t["done"] = updated_todo.done
            return t
    raise HTTPException(status_code=404, detail="Todo not found")


# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):  #dont need todo: todo cuz it is delete and we dont need a request body
    for t in todos:
        if t["id"] == todo_id:
            todos.remove(t) #refers to in-memory list of all todos and removes it by id
            return {"message": "todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")




















# Notes:

    # FastAPI automatically converts Python dictionaries into JSON for you.
    # So when you go to /, you get {"message":"Hello, World!"}
    """ Key idea: Each @app.get(...) (or post, put, etc.) defines an endpoint. 
    The function below it is what runs to handle requests. """