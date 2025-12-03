# ToDo List API - Phase 3

A modern **RESTful Web API** built with **FastAPI**, replacing the deprecated CLI interface. This project provides full CRUD operations for Projects and Tasks with automatic interactive documentation.

---

## 🚀 Overview

The old command-line interface (CLI) is now **deprecated** and will be removed in Phase 4.

### Migration

Use the new HTTP API:

```
uvicorn todo.api.main:app --reload
```

---

## 🏗️ Architecture

```
HTTP Layer (FastAPI) → Service Layer → Repository Layer → PostgreSQL
```

---

## ⚡ Quick Start

```bash
# 1. Install dependencies
poetry install

# 2. Start PostgreSQL
docker-compose up -d
alembic upgrade head

# 3. Run API
uvicorn todo.api.main:app --reload
# Access: http://localhost:8000
```

---

## 📍 API Endpoints

### **Projects**

* `GET /api/v1/projects` – List all projects
* `POST /api/v1/projects` – Create a new project
* `GET /api/v1/projects/{id}` – Get project details
* `PUT /api/v1/projects/{id}` – Update a project
* `DELETE /api/v1/projects/{id}` – Delete a project

### **Tasks (Nested under Projects)**

* `GET /api/v1/projects/{id}/tasks` – List tasks in a project
* `POST /api/v1/projects/{id}/tasks` – Create a new task
* `GET /api/v1/projects/{id}/tasks/{task_id}` – Get task details
* `PUT /api/v1/projects/{id}/tasks/{task_id}` – Update a task
* `PATCH /api/v1/projects/{id}/tasks/{task_id}/status` – Update task status
* `DELETE /api/v1/projects/{id}/tasks/{task_id}` – Delete a task

---

## 📚 Documentation

* Swagger UI: **[http://localhost:8000/docs](http://localhost:8000/docs)**

---

## 🛠️ Features

* ✔️ Auto-generated Swagger/OpenAPI docs
* ✔️ Pydantic validation
* ✔️ Nested RESTful resources
* ✔️ Proper HTTP status codes
* ✔️ CORS enabled
* ✔️ SQLAlchemy ORM
* ✔️ Layered architecture (Controller → Service → Repository)

---

## 🔧 Tech Stack

* **FastAPI** – Modern Python framework
* **Pydantic** – Data validation
* **SQLAlchemy** – ORM
* **PostgreSQL** – Database
* **Uvicorn** – ASGI server





