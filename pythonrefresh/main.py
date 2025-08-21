def greet(name):
    return f"Hello, {name}! Welcome back to Python."

def add(a, b):
    return a + b

def summarize_tasks(tasks):
    return {"count": len(tasks)}

if __name__ == "__main__":
    print(greet("Your Name"))
    print("2 + 5 =", add(2, 5))

    tasks = ["learn python", "set up project", "commit code"]
    print("tasks:", tasks)
    print("summary:", summarize_tasks(tasks))
