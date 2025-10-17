"""Module defining the Task class for managing to-do items."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

from ..exception import (
    ValidationError,
    TaskLimitExceededError,
    InvalidDeadlineError
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
        self._validate_deadline()

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

    def _validate_deadline(self) -> None:
        """Ensure that the deadline, if provided, is a valid date and not in the past."""
        if self.deadline is None:
            return

        #if the deadline is of type string, convert it to a date.
        if isinstance(self.deadline, str):
            try:
                self.deadline = datetime.strptime(self.deadline, "%Y-%m-%d").date()
            except ValueError:
                raise ValidationError("Deadline format must be YYYY-MM-DD.")

        # error if the deadline is in the past.
        if self.deadline < date.today():
            raise InvalidDeadlineError("Deadline cannot be in the past.")

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

    def edit(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        deadline: Optional[str] = None,
    ) -> None:
        """Edit task details with proper validation.

        Args:
            title (Optional[str]): New title.
            description (Optional[str]): New description.
            status (Optional[str]): New status ("todo", "doing", "done").
            deadline (Optional[str]): New deadline (YYYY-MM-DD).

        Raises:
            ValidationError: If any of the fields are invalid.
        """
        if title is not None:
            self.title = title
            self._validate_title()

        if description is not None:
            self.description = description
            self._validate_description()

        if status is not None:
            self.status = status
            self._validate_status()

        if deadline is not None:
            if isinstance(deadline, str):
                try:
                    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
                except ValueError:
                    raise ValidationError("Deadline format must be YYYY-MM-DD.")
            self.deadline = deadline
            self._validate_deadline()


