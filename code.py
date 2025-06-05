
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=10):
            print(f"{i}. {task}")

def add_task(task):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")


