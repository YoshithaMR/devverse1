import os

FILENAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILEsss, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

