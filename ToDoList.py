# To-Do List Application
# This program allows users to manage daily tasks using a CLI-based menu

tasks = []  # List to store all tasks

# Function to display menu options
def show_menu():
    print("_______________________________________")
    print("              To-Do List               ")
    print("_______________________________________")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# Function to add a new task
def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)  # Add task to list
        print("Task added successfully.")
    else:
        print("Task cannot be Empty.")

# Function to view all tasks
def view_task():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n Your tasks: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to update an existing task
def update_task():
    view_task()
    if tasks:
        try:
            choice = int(input("Enter task number to update: "))
            if 1 <= choice <= len(tasks):
                new_task = input("Enter updated task: ").strip()
                if new_task:
                    tasks[choice - 1] = new_task
                    print("Task updated successfully.")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_task()
    if tasks:
        try:
            choice = int(input("Enter task number to delete: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f" Task '{removed}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("_______________________________________")
        print("     Exiting To-Do List. Goodbye!")
        print("_______________________________________")
        break
    else:
        print("Invalid choice. Please select between 1 to 5.")
