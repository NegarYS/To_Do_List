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