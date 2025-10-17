"""Command-Line Interface for the To-Do List Application."""

from todo.services.todo_service import TodoService
from todo.exception import ValidationError, ProjectNotFoundError, TaskNotFoundError

service = TodoService()


def print_menu():
    print("\n📋 --- To-Do List Menu ---")
    print("1. List all projects")
    print("2. Create a new project")
    print("3. Edit a project")
    print("4. Delete a project")
    print("5. List tasks in a project")
    print("6. Add a new task")
    print("7. Edit a task")
    print("8. Change task status")
    print("9. Delete a task")
    print("0. Exit")


def run_cli():
    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                projects = service.list_projects()
                if not projects:
                    print("⚠️  No projects found.")
                else:
                    for p in projects:
                        print(f"[{p.id}] {p.name} - {p.description or '-'}")

            elif choice == "2":
                name = input("Project name: ")
                desc = input("Description (optional): ")
                project = service.create_project(name, desc)
                print(f"✅ Project '{project.name}' created successfully!")

            elif choice == "3":
                pid = int(input("Enter project ID: "))
                name = input("New name (leave blank to keep current): ")
                desc = input("New description (leave blank to keep current): ")
                project = service.update_project(pid, name or None, desc or None)
                print(f"✅ Project {project.id} updated successfully!")

            elif choice == "4":
                pid = int(input("Enter project ID to delete: "))
                msg = service.delete_project(pid)
                print(msg)

            elif choice == "5":
                pid = int(input("Enter project ID: "))
                tasks = service.list_tasks(pid)
                if not tasks:
                    print("⚠️  No tasks in this project.")
                else:
                    for t in tasks:
                        deadline = t.deadline.strftime("%Y-%m-%d") if t.deadline else "-"
                        print(f"[{t.id}] {t.title} - {t.status} (Deadline: {deadline})")

            elif choice == "6":
                pid = int(input("Enter project ID: "))
                title = input("Task title: ")
                desc = input("Description (optional): ")
                status = input("Status (todo/doing/done, optional): ")
                deadline = input("Deadline (YYYY-MM-DD, optional): ")
                task = service.create_task(pid, title, desc, status or None, deadline or None)
                print(f"✅ Task '{task.title}' added successfully!")

            elif choice == "7":
                pid = int(input("Enter project ID: "))
                tid = int(input("Enter task ID: "))
                title = input("New title (leave blank to keep current): ")
                desc = input("New description (leave blank to keep current): ")
                status = input("New status (todo/doing/done, optional): ")
                deadline = input("New deadline (YYYY-MM-DD, optional): ")
                task = service.update_task(pid, tid, title or None, desc or None, status or None, deadline or None)
                print(f"✅ Task {task.id} updated successfully!")

            elif choice == "8":
                pid = int(input("Enter project ID: "))
                tid = int(input("Enter task ID: "))
                status = input("Enter new status (todo/doing/done): ")
                task = service.change_task_status(pid, tid, status)
                print(f"🔄 Task {task.id} status changed to '{task.status}'.")

            elif choice == "9":
                pid = int(input("Enter project ID: "))
                tid = int(input("Enter task ID: "))
                msg = service.delete_task(pid, tid)
                print(msg)

            elif choice == "0":
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_cli()
