"""Module defining the Task class for managing to-do items."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

from ..exception import (
    ValidationError,
    TaskLimitExceededError,
)
from ..config import config

VALID_STATUSES = ("todo", "doing", "done")


@dataclass
class Task:
    """Represents a single task in a to-do list."""

    id: int
    title: str
    description: str = ""
    status: str = config.DEFAULT_TASK_STATUS
    created_at: datetime = field(default_factory=datetime.now)
    deadline: Optional[date] = None

    def __post_init__(self):
        """Validate task fields after initialization."""
        self._validate_title()
        self._validate_description()
        self._validate_status()

    def _validate_title(self) -> None:
        """Ensure that the title is non-empty and within character limits."""
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValidationError("Task title must be a non-empty string.")
        if len(self.title) > 30:
            raise ValidationError("Task title must be at most 30 characters.")

    def _validate_description(self) -> None:
        """Ensure that the description length does not exceed 150 characters."""
        if self.description is None:
            self.description = ""
        if len(self.description) > 150:
            raise ValidationError("Task description must be at most 150 characters.")

    def _validate_status(self) -> None:
        """Ensure that the status value is valid."""
        if self.status not in VALID_STATUSES:
            raise ValidationError(f"Invalid status: {self.status}. Valid: {VALID_STATUSES}")

    def change_status(self, new_status: str) -> None:
        """Change the task's status to a new valid one.

        Args:
            new_status (str): New status, one of VALID_STATUSES.

        Raises:
            ValueError: If new_status is not valid.
        """
        if new_status not in VALID_STATUSES:
            raise ValidationError(f"Invalid status: {new_status}. Valid: {VALID_STATUSES}")
        self.status = new_status
