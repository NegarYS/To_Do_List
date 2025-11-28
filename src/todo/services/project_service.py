"""Service layer providing high-level operations for projects."""

from __future__ import annotations

from typing import Optional, List

from ..storage.in_memory import InMemoryStorage
from ..models.project import Project

class ProjectService:
    """Provides business logic for managing projects."""

    def __init__(self, storage: Optional[InMemoryStorage] = None):
        """Initialize the service with a storage backend."""
        self.storage = storage or InMemoryStorage()

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
