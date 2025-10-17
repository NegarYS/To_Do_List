"""Service layer providing high-level operations for projects and tasks."""

from __future__ import annotations

from typing import Optional, List

from ..storage.in_memory import InMemoryStorage
from ..models.project import Project
from ..models.task import Task


class TodoService:
    """Provides business logic for managing projects and tasks."""

    def __init__(self, storage: Optional[InMemoryStorage] = None):
        """Initialize the service with a storage backend."""
        self.storage = storage or InMemoryStorage()

    # ----------------------------- Project Methods -----------------------------

    def create_project(self, name: str, description: str = "") -> Project:
        """Create a new project.

        Args:
            name (str): The project name (must be unique).
            description (str): Optional project description.

        Returns:
            Project: The created project instance.
        """
        return self.storage.create_project(name, description)

    def list_projects(self) -> List[Project]:
        """Return all projects sorted by creation time."""
        return self.storage.list_projects()

    def get_project(self, project_id: int) -> Project:
        """Retrieve a specific project by ID."""
        return self.storage.get_project(project_id)

    def update_project(self, project_id: int, name: str = None, description: str = None) -> Project:
        """Update an existing project's name or description.

        Args:
            project_id (int): The project ID.
            name (Optional[str]): New project name (must be unique).
            description (Optional[str]): New description.

        Returns:
            Project: The updated project instance.
        """
        return self.storage.update_project(project_id, name, description)

    def delete_project(self, project_id: int) -> str:
        """Delete a project and its associated tasks."""
        return self.storage.delete_project(project_id)

    # ----------------------------- Task Methods -----------------------------

    def create_task(
        self,
        project_id: int,
        title: str,
        description: str = "",
        status: Optional[str] = None,
        deadline: Optional[str] = None,
    ) -> Task:
        """Add a new task to a project."""
        return self.storage.add_task(project_id, title, description, status, deadline)

    def list_tasks(self, project_id: int) -> List[Task]:
        """List all tasks for a given project.

        Args:
            project_id (int): The ID of the parent project.

        Returns:
            List[Task]: All tasks of that project.
        """
        project = self.storage.get_project(project_id)
        return project.tasks

    def change_task_status(self, project_id: int, task_id: int, new_status: str) -> Task:
        """Change the status of a specific task."""
        return self.storage.change_task_status(project_id, task_id, new_status)

    def delete_task(self, project_id: int, task_id: int) -> str:
        """Remove a task from a project."""
        return self.storage.remove_task(project_id, task_id)

    def update_task(
        self,
        project_id: int,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        deadline: Optional[str] = None,
    ) -> Task:
        """Update an existing task."""
        return self.storage.update_task(project_id, task_id, title, description, status, deadline)
