"""Controllers package for API endpoints."""

from .projects_controller import router as projects_router
from .tasks_controller import router as tasks_router

# Export routers for easy access
__all__ = ["projects_router", "tasks_router"]