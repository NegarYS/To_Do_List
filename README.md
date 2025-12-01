# ToDoList Project — Phase 2 (Relational Database Version)

## 📌 Overview
This README describes **Phase 2** of the ToDoList project, where the system transitions from an *in-memory implementation* (Phase 1) to a **Relational Database (RDB)-based architecture**.  
This phase introduces PostgreSQL, SQLAlchemy ORM, migrations, repository pattern, and improved modular design — while keeping the business logic from Phase 1 intact.

---

## 🎯 Objectives of Phase 2
In Phase 2, the ToDoList system is upgraded to support persistent data storage.  
Key goals:

- Replace in-memory storage with **PostgreSQL**
- Implement **SQLAlchemy ORM models** for `Project` and `Task`
- Add **CRUD operations** through repository classes
- Add **Alembic migrations** for schema versioning
- Introduce a **command** for auto-closing overdue tasks
- Maintain clean-layered architecture:
  ```
  CLI → Services → Repositories → Database (PostgreSQL)
  ```

---

## 🧩 Features Implemented in Phase 2

### ✔ Persistent Storage  
All Projects and Tasks are saved in a PostgreSQL database.

### ✔ ORM-Based Models  
Using SQLAlchemy Declarative Base for:
- Project model  
- Task model (with status + deadline + closed_at)

### ✔ Repository Pattern  
Each model has a dedicated repository for:
- Adding records  
- Fetching by ID  
- Listing  
- Project-specific task filtering  
- Overdue task detection  

### ✔ Business Logic in Services  
Service layer handles:
- Validations  
- Status updates  
- Autoclose-overdue logic  
- Coordination between repositories  

### ✔ Command: Auto-Close Overdue Tasks  
A CLI command:
```
python -m todo.commands.autoclose_overdue
```
Automatically sets status of overdue tasks to `done`.

---


## 🛠 Setup Instructions

### 1️⃣ Install Dependencies
```
poetry install
```

### 2️⃣ Configure Environment
Create `.env`:
```
DATABASE_URL=postgresql+psycopg2://user:pass@localhost:5432/todolist
```

### 3️⃣ Run PostgreSQL (Docker recommended)
```
docker compose up -d
```

### 4️⃣ Run Alembic Migrations
```
alembic upgrade head
```

### 5️⃣ Run CLI Interface
```
poetry run todo
```

---


## 🧠 Notes

- Phase 2 maintains the clean architecture introduced in Phase 1  
- Database versioning is now handled through **Alembic**  
- Repositories abstract SQL operations  
- Services ensure business rules remain separate and testable  

---

## 📚 Technologies Used
- Python 3.11+
- SQLAlchemy 2.0 ORM
- PostgreSQL 15+
- Alembic migrations
- Poetry (dependency management)
- dotenv for configuration

---




