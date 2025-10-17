"""Command-Line Interface for the To-Do List Application."""

import argparse
from typing import Optional

from .services.todo_service import TodoService
from .exception import (
    ValidationError,
    ProjectNotFoundError,
    ProjectNameExistsError,
    TaskNotFoundError,
    InvalidDeadlineError,
)

# Initialize service
service = TodoService()


def handle_error(e: Exception):
    """Display friendly error messages."""
    print(f"❌ Error: {str(e)}")


# ----------------------------- Project Commands -----------------------------

def create_project(args):
    try:
        project = service.create_project(args.name, args.description or "")
        print(f"✅ Project '{project.name}' created successfully (ID={project.id}).")
    except (ValidationError, ProjectNameExistsError) as e:
        handle_error(e)


def list_projects(args):
    projects = service.list_projects()
    if not projects:
        print("No projects found.")
        return

    print("\n📋 Projects:")
    for p in projects:
        print(f"  ID: {p.id} | Name: {p.name} | Description: {p.description or '-'} | Created: {p.created_at:%Y-%m-%d}")


def update_project(args):
    try:
        project = service.update_project(args.id, args.name, args.description)
        print(f"✅ Project {project.id} updated successfully.")
    except (ValidationError, ProjectNotFoundError, ProjectNameExistsError) as e:
        handle_error(e)


def delete_project(args):
    try:
        msg = service.delete_project(args.id)
        print(msg)
    except ProjectNotFoundError as e:
        handle_error(e)


# ----------------------------- Task Commands -----------------------------

def add_task(args):
    try:
        task = service.create_task(
            args.project_id,
            args.title,
            args.description,
            args.status,
            args.deadline,
        )
        print(f"✅ Task '{task.title}' added successfully to project {args.project_id} (ID={task.id}).")
    except (ValidationError, InvalidDeadlineError) as e:
        handle_error(e)
    except ProjectNotFoundError as e:
        handle_error(e)


def list_tasks(args):
    try:
        tasks = service.list_tasks(args.project_id)
        if not tasks:
            print("⚠️  No tasks found in this project.")
            return

        print(f"\n🗂️  Tasks for Project {args.project_id}:")
        for t in tasks:
            deadline = t.deadline.strftime("%Y-%m-%d") if t.deadline else "-"
            print(f"  ID: {t.id} | Title: {t.title} | Status: {t.status} | Deadline: {deadline}")
    except ProjectNotFoundError as e:
        handle_error(e)


def update_task(args):
    try:
        task = service.update_task(
            args.project_id,
            args.id,
            title=args.title,
            description=args.description,
            status=args.status,
            deadline=args.deadline,
        )
        print(f"✅ Task {task.id} updated successfully in project {args.project_id}.")
    except (ValidationError, InvalidDeadlineError, TaskNotFoundError) as e:
        handle_error(e)
    except ProjectNotFoundError as e:
        handle_error(e)


def delete_task(args):
    try:
        msg = service.delete_task(args.project_id, args.id)
        print(f"🗑️  {msg}")
    except (ProjectNotFoundError, TaskNotFoundError) as e:
        handle_error(e)


def change_status(args):
    try:
        task = service.change_task_status(args.project_id, args.id, args.status)
        print(f"🔄 Task {task.id} status changed to '{task.status}'.")
    except (ValidationError, ProjectNotFoundError, TaskNotFoundError) as e:
        handle_error(e)


# ----------------------------- CLI Setup -----------------------------


def main():
    parser = argparse.ArgumentParser(description="🧩 To-Do List CLI Application")
    subparsers = parser.add_subparsers(title="Commands")

    # ---- Project commands ----
    p_create = subparsers.add_parser("create-project", help="Create a new project")
    p_create.add_argument("name")
    p_create.add_argument("--description", help="Optional project description")
    p_create.set_defaults(func=create_project)

    p_list = subparsers.add_parser("list-projects", help="List all projects")
    p_list.set_defaults(func=list_projects)

    p_update = subparsers.add_parser("update-project", help="Update project info")
    p_update.add_argument("id", type=int)
    p_update.add_argument("--name", help="New name")
    p_update.add_argument("--description", help="New description")
    p_update.set_defaults(func=update_project)

    p_delete = subparsers.add_parser("delete-project", help="Delete a project and its tasks")
    p_delete.add_argument("id", type=int)
    p_delete.set_defaults(func=delete_project)

    # ---- Task commands ----
    t_add = subparsers.add_parser("add-task", help="Add a new task to a project")
    t_add.add_argument("project_id", type=int)
    t_add.add_argument("title")
    t_add.add_argument("--description", help="Optional task description")
    t_add.add_argument("--status", choices=["todo", "doing", "done"])
    t_add.add_argument("--deadline", help="Deadline in YYYY-MM-DD")
    t_add.set_defaults(func=add_task)

    t_list = subparsers.add_parser("list-tasks", help="List tasks in a project")
    t_list.add_argument("project_id", type=int)
    t_list.set_defaults(func=list_tasks)

    t_update = subparsers.add_parser("update-task", help="Update a task")
    t_update.add_argument("project_id", type=int)
    t_update.add_argument("id", type=int)
    t_update.add_argument("--title")
    t_update.add_argument("--description")
    t_update.add_argument("--status", choices=["todo", "doing", "done"])
    t_update.add_argument("--deadline")
    t_update.set_defaults(func=update_task)

    t_delete = subparsers.add_parser("delete-task", help="Delete a task")
    t_delete.add_argument("project_id", type=int)
    t_delete.add_argument("id", type=int)
    t_delete.set_defaults(func=delete_task)

    t_status = subparsers.add_parser("change-status", help="Change task status")
    t_status.add_argument("project_id", type=int)
    t_status.add_argument("id", type=int)
    t_status.add_argument("status", choices=["todo", "doing", "done"])
    t_status.set_defaults(func=change_status)

    # ---- Parse & Execute ----
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
