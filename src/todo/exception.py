class ToDoError(Exception):
    """Base exception for all ToDoList errors."""
    pass

class ProjectNotFoundError(ToDoError):
    """Raised when a project with a given ID does not exist."""
    pass

class TaskNotFoundError(ToDoError):
    """Raised when a task with a given ID does not exist."""
    pass

class ProjectNameExistsError(ToDoError):
    """Raised when trying to create a project with a name that already exists."""
    pass

class ProjectLimitExceededError(ToDoError):
    """Raised when the maximum number of projects has been reached."""
    pass

class TaskLimitExceededError(ToDoError):
    """Raised when the maximum number of tasks for a project has been reached."""
    pass

class ValidationError(ToDoError):
    """Raised when input data violates validation rules."""
    pass

class StorageError(ToDoError):
    """Raised when something goes wrong with the storage layer."""
    pass