# Campus Management System — Setup & Execution Guide

## Prerequisites

- **Docker & Docker Compose** (Recommended for full stack containerized run)
- Or **Python 3.10+** and **Node.js 18+** (for manual local execution)

---

## Option 1: Quickstart with Docker Compose (Recommended)

Run all services (PostgreSQL, Django Backend, React Frontend, Nginx Gateway) with one command:

```bash
# 1. Clone or navigate to the project directory
cd campus-management

# 2. Start all services in the background
docker compose up --build -d

# 3. View running logs
docker compose logs -f
```

### Access Ports:
- **Application Portal (via Nginx Gateway)**: `http://localhost`
- **Frontend Direct (Dev)**: `http://localhost:3000`
- **Backend API Direct**: `http://localhost:8000/api/`
- **Django Admin**: `http://localhost:8000/admin/`

### Demo Login Accounts:
- **Admin**: `admin` / `admin123`
- **Student**: `student` / `student123`
- **Faculty**: `prof_smith` / `faculty123`

---

## Option 2: Standalone Local Development

### 1. Backend Setup (Django)

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (will use SQLite by default locally if PostgreSQL is not active)
python manage.py migrate

# Seed initial demo data
python manage.py init_demo_data

# Start backend dev server
python manage.py runserver 0.0.0.0:8000
```

### 2. Frontend Setup (React + Vite)

```bash
cd frontend

# Install npm dependencies
npm install

# Start Vite development server
npm run dev
```

The React app will be accessible at `http://localhost:3000`.

---

## Option 3: Running Tests

Run the full Pytest test suite from the root directory:

```bash
# Run pytest
pytest

# Run Django test runner specifically
python backend/manage.py test
```
