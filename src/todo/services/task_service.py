"""Service layer providing high-level operations for tasks."""

from __future__ import annotations

from typing import Optional, List

from ..storage.in_memory import InMemoryStorage
from ..models.task import Task


class TaskService:
    """Provides business logic for managing tasks."""

    def __init__(self, storage: Optional[InMemoryStorage] = None):
        """Initialize the service with a storage backend."""
        self.storage = storage or InMemoryStorage()

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
