def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found. File will be created when you add a task.")

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks to delete.")
            return

        view_tasks()
        task_num = int(input("Enter task number to delete: "))
        
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Deleted: {deleted.strip()}")
        else:
            print("Invalid task number.")
    except (ValueError, FileNotFoundError):
        print("Error: Please enter a valid task number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
