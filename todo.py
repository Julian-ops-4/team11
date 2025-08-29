tasks = []

def add_tasks(task):
    task.append(task)

def view_task():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}.{task}")

