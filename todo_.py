import json
import os

# File to store tasks
DATA_FILE = "todo_data.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save updated tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Show all tasks
def view_all_tasks(tasks):
    print("\n📋 Your To-Do List:")
    if not tasks:
        print("Nothing here! Add some tasks.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}. [{status}] {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("Enter the task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("✅ Task added.")
    else:
        print("⚠️ Task can't be empty.")

# Mark a task as done
def mark_task_done(tasks):
    view_all_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("🎉 Task marked as done!")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a number.")

# Delete a task
def delete_task(tasks):
    view_all_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['title']}' deleted.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a number.")

# App menu
def main_menu():
    tasks = load_tasks()

    while True:
        print("\n========= TO-DO LIST MENU =========")
        print("1. View all tasks")
        print("2. Add new task")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Exit")
        print("===================================")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_all_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... See you again!")
            break
        else:
            print("❗ Invalid choice. Please select from 1 to 5.")

# Run the app
if __name__ == "__main__":
    main_menu()