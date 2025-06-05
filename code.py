
def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '31':
            show_tasks(tasks)
        elif choice == '32':
            add_task(tasks)
        elif choice == '35':
            remove_task(tasks)
        elif choice == '34':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


