"""In-memory storage implementation for projects and tasks.

This module defines the InMemoryStorage class, which stores all
projects and their associated tasks in Python dictionaries.
It provides CRUD operations for both projects and tasks.
"""

from __future__ import annotations

from typing import Dict, List, Optional

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

