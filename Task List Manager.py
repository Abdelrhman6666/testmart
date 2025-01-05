import os

# Define a global list to store tasks
tasks = []

# Function to add tasks to the list
def add_task(task):
    """Adds a new task to the list."""
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to remove completed tasks
def remove_task(task):
    """Removes a task from the list."""
    try:
        tasks.remove(task)
        print(f"Task '{task}' has been removed.")
    except ValueError:
        print(f"Error: Task '{task}' not found in the list.")

# Function to view the current task list
def view_tasks():
    """Displays all the tasks."""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current Task List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function to save tasks to a file
def save_tasks_to_file(filename):
    """Saves tasks to a text file."""
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print(f"Tasks have been saved to '{filename}'.")
    except IOError as e:
        print(f"Error saving tasks to file: {e}")

# Function to load tasks from a file
def load_tasks_from_file(filename):
    """Loads tasks from a text file."""
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                global tasks
                tasks = [line.strip() for line in file.readlines()]
            print(f"Tasks have been loaded from '{filename}'.")
        except IOError as e:
            print(f"Error reading from file: {e}")
    else:
        print(f"No such file '{filename}' found.")

# Function to handle exceptions during file operations
def handle_file_exceptions():
    """Handles file read/write exceptions."""
    try:
        # Example of task saving/loading to demonstrate exception handling
        save_tasks_to_file("tasks.txt")
        load_tasks_from_file("tasks.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Load existing tasks from the file if any
    load_tasks_from_file("tasks.txt")

    # Adding tasks
    add_task("Buy groceries")
    add_task("Finish homework")
    add_task("Walk the dog")

    # View tasks
    view_tasks()

    # Removing a task
    remove_task("Finish homework")

    # View tasks again after removal
    view_tasks()

    # Save tasks to file
    save_tasks_to_file("tasks.txt")

    # Handle any file operation errors
    handle_file_exceptions()
