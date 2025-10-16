"""Module defining the Project class for managing collections of tasks."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Optional

from ..config import config
from .task import Task


@dataclass
class Project:
    """Represents a project that contains a collection of tasks."""

    id: int
    name: str
    description: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    tasks: List[Task] = field(default_factory=list)

    def __post_init__(self):
        """Validate the project's attributes after initialization."""
        self._validate_name()
        self._validate_description()

    def _validate_name(self):
        """Ensure that the project name is a valid non-empty string."""
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Project name must be a non-empty string.")
        if len(self.name) > 30:
            raise ValueError("Project name must be at most 30 characters.")

    def _validate_description(self):
        """Ensure that the project description is within allowed length."""
        if self.description is None:
            self.description = ""
        if len(self.description) > 150:
            raise ValueError("Project description must be at most 150 characters.")

    def add_task(self, task: Task):
        """Add a new task to the project.

        Args:
            task (Task): The task instance to be added.

        Raises:
            ValueError: If the project already contains the maximum number of tasks.
        """
        if len(self.tasks) >= config.MAX_NUMBER_OF_TASK:
            raise ValueError("Max number of tasks reached for this project.")
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> bool:
        """Remove a task by its ID.

        Args:
            task_id (int): The ID of the task to remove.

        Returns:
            bool: True if the task was found and removed, False otherwise.
        """
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                del self.tasks[i]
                return True
        return False

    def get_task(self, task_id: int) -> Task | None:
        """Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Optional[Task]: The matching Task instance, or None if not found.
        """
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def edit(self, name: Optional[str] = None, description: Optional[str] = None):
        """Edit the project's name and/or description.

        Args:
            name (Optional[str]): New name for the project.
            description (Optional[str]): New description for the project.

        Raises:
            ValueError: If provided values are invalid.
        """
        if name is not None:
            self.name = name
            self._validate_name()
        if description is not None:
            self.description = description
            self._validate_description()
