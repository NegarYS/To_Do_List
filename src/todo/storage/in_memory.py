"""In-memory storage implementation for projects and tasks.

This module defines the InMemoryStorage class, which stores all
projects and their associated tasks in Python dictionaries.
It provides CRUD operations for both projects and tasks.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from ..exception import (
    ProjectLimitExceededError,
    TaskLimitExceededError,
    ProjectNameExistsError,
    ProjectNotFoundError,
    TaskNotFoundError,
    ValidationError
)
from ..models.project import Project
from ..models.task import Task
from ..config import config


class InMemoryStorage:
    """A simple in-memory repository for managing projects and their tasks."""

    def __init__(self) -> None:
        """Initialize empty project storage with counters for IDs."""
        self._projects: Dict[int, Project] = {}
        self._next_project_id: int = 1
        self._next_task_id: int = 1

    # ----------------------------- Project Methods -----------------------------

    def list_projects(self) -> List[Project]:
        """Return list of projects sorted by creation time (ascending)."""
        return sorted(self._projects.values(), key=lambda p: p.created_at)

    def create_project(self, name: str, description: str = "") -> Project:
        """Create a new project and add it to the storage.

        Args:
            name (str): The project name (must be unique).
            description (str): Optional project description.

        Returns:
            Project: The created project instance.

        Raises:
            ValueError: If the project limit is reached or name is not unique.
        """
        if len(self._projects) >= config.MAX_NUMBER_OF_PROJECT:
            raise ProjectLimitExceededError("Max number of projects reached.")

        for p in self._projects.values():
            if p.name == name:
                raise ProjectNameExistsError("Project name must be unique.")

        project = Project(id=self._next_project_id, name=name, description=description)
        self._projects[self._next_project_id] = project
        self._next_project_id += 1
        return project

    def get_project(self, project_id: int) -> Project:
        """Return the project with the given ID, or raise an error if not found."""
        project = self._projects.get(project_id)
        if not project:
            raise ProjectNotFoundError(f"Project with ID {project_id} not found.")
        return project

    def update_project(self, project_id: int, name: str = None, description: str = None) -> Project:
        """Create a new project and add it to the storage.

        Args:
            project_id (int): The project ID.
            name (str): The project name (must be unique).
            description (str): Optional project description.

        Returns:
            Project: The created project instance.

        Raises:
            ValueError: If the project limit is reached.
            ProjectNameExistsError: If the new name already exists.
        """
        project = self.get_project(project_id)
        if name and name != project.name:
            for p in self._projects.values():
                if p.name == name:
                    raise ProjectNameExistsError("Project name must be unique.")

        try:
            project.edit(name=name, description=description)
            print(f"Project {project_id} updated successfully.")
            return project
        except ValueError as e:
            raise ValidationError(str(e)) from e

    def delete_project(self, project_id: int) -> str:
        """Delete a project and all its associated tasks.

        Args:
            project_id (int): The ID of the project to delete.

        Returns:
            str: The appropriate success or error message.

        """
        project = self.get_project(project_id)

        # Explicit cascade delete for clarity
        num_tasks = len(project.tasks)
        project.tasks.clear()
        del self._projects[project_id]

        return f"✅ Project {project_id} deleted successfully with {num_tasks} tasks."

    # ----------------------------- Task Methods -----------------------------

    def add_task(
            self,
            project_id: int,
            title: str,
            description: str = "",
            status: Optional[str] = None,
            deadline: Optional[str] = None,
    ) -> Task:
        """Add a new task to a project.

        Args:
            project_id (int): ID of the parent project.
            title (str): Task title.
            description (str): Optional task description.
            status (Optional[str]): Optional task status.
            deadline (Optional[str]): Optional task deadline.

        Returns:
            Task: The created task instance.

        Raises:
            TaskLimitExceededError: If the maximum number of tasks is reached.
            ValidationError: If task fields are invalid (title, description, status, deadline).
        """
        project = self.get_project(project_id)

        if len(project.tasks) >= config.MAX_NUMBER_OF_TASK:
            raise TaskLimitExceededError("Max number of tasks for this project reached.")

        try:
            task = Task(
                id=self._next_task_id,
                title=title,
                description=description,
                status=status or config.DEFAULT_TASK_STATUS,
                deadline=deadline,
            )
        except ValidationError as e:
            raise ValidationError(str(e))

        project.add_task(task)
        self._next_task_id += 1
        return task

    def remove_task(self, project_id: int, task_id: int) -> str:
        """Remove a task from the given project.

        Args:
            project_id (int): ID of the parent project.
            task_id (int): ID of the task to remove.

        Returns:
            str: The appropriate success or error message.
        """
        project = self.get_project(project_id)
        deleted = project.remove_task(task_id)
        if deleted:
            return f"Task {task_id} deleted successfully from project {project_id}."
        else:
            return f"Error: Task {task_id} not found in project {project_id}."

    def change_task_status(
            self,
            project_id: int,
            task_id: int,
            new_status: str,
    ) -> Task:
        """Change the status of a task inside a project.

        Args:
            project_id (int): The ID of the project containing the task.
            task_id (int): The ID of the task.
            new_status (str): The new status to set.

        Returns:
            Task: The updated task instance.

        Raises:
            KeyError: If the project or task is not found.
            ValueError: If the new status is invalid.
        """
        project = self.get_project(project_id)
        task = project.get_task(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found.")
        try:
            task.change_status(new_status)
        except ValueError as e:
            raise ValidationError(str(e)) from e
        return task