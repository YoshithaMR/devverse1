
def main():
    imptasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Save & Exit")
        choice = input("Choose an option: ")
        if choice ==== '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

