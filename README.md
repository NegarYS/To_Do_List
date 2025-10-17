# 🧩 ToDoList - Phase 1 (In-Memory Implementation)

This is the **Phase 1** implementation of the *ToDoList Project*, developed in Python using OOP principles.  
It follows a clean, modular architecture with distinct layers for models, storage, services, and CLI interaction.

---

## 📘 Project Overview

This project is a simple **To-Do List Management System**, designed to help users manage multiple projects and tasks.  
It supports the following key functionalities:

### ✅ Core Features
- Create, list, update, and delete **Projects**
- Create, list, update, and delete **Tasks**
- Change **Task Status** (`todo`, `doing`, `done`)
- Validate project and task attributes (title, description, deadline, etc.)
- Interactive **menu-based CLI interface**
- Fully in-memory (no database or file storage in this phase)

---

## 🧠 Architecture Overview

The project follows a **Clean Layered Architecture**:

```
[ CLI Layer ] → [ Service Layer ] → [ Storage Layer ] → [ Model Layer ]
```

| Layer | Description |
|--------|-------------|
| **Model** | Defines domain objects (`Project`, `Task`) and validation rules |
| **Storage** | Handles CRUD operations on in-memory data structures |
| **Service** | Business logic connecting CLI and Storage |
| **CLI** | User interface layer for interaction via the terminal |

This separation ensures clean code, testability, and future scalability (e.g., adding a database layer in later phases).

---

## 🧩 Folder Structure

```
To_Do_List/
│
├── src/
│   └── todo/
│       ├── cli.py
│       ├── config.py
│       ├── exception.py
│       ├── models/
│       │   ├── project.py
│       │   └── task.py
│       ├── services/
│       │   └── todo_service.py
│       └── storage/
│           └── in_memory.py
│
├── .env.example
│
├── pyproject.toml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/To_Do_List.git
cd To_Do_List
```

### 2️⃣ Install Poetry (if not installed)

Poetry is used to manage dependencies and virtual environments.

#### Windows (PowerShell)
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

#### macOS / Linux
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Verify installation:
```bash
poetry --version
```

---

### 3️⃣ Install Dependencies
```bash
poetry install
```

---

### 4️⃣ Activate the Environment
```bash
poetry shell
```

---

### 5️⃣ Run the Interactive CLI
```bash
python -m todo.cli
```

---

## 🧭 CLI Menu Overview

Once you run the application, you will see:

```
📋 --- To-Do List Menu ---
1. List all projects
2. Create a new project
3. Edit a project
4. Delete a project
5. List tasks in a project
6. Add a new task
7. Edit a task
8. Change task status
9. Delete a task
0. Exit
```

### 🧑‍💻 Example Usage

#### ➤ Create a Project
```
Enter your choice: 2
Project name: University Work
Description: Assignments and Research
✅ Project 'University Work' created successfully!
```

#### ➤ Add a Task
```
Enter your choice: 6
Enter project ID: 1
Task title: Write final report
Deadline: 2025-11-01
✅ Task 'Write final report' added successfully!
```

#### ➤ List Tasks
```
Enter your choice: 5
Enter project ID: 1
[1] Write final report - todo (Deadline: 2025-11-01)
```

---

## ⚠️ Notes

- Data is stored **only in memory**, meaning it resets after each program run.
- Input validation ensures proper constraints (e.g., name length, valid deadlines, etc.).
- All exceptions are handled gracefully, showing user-friendly messages.

---



## 🧰 Technologies Used

- **Python 3.11+**
- **Poetry** (dependency and environment management)
- **pytest** (testing framework)
- **argparse / input-based CLI**
- **dataclasses** for clean model design




