# 🎓 Campus Management System (EduCore)

A modern, enterprise-grade Campus Management System built with a decoupled architecture: **React + JavaScript + Bootstrap** on the frontend, **Django + Django REST Framework** on the backend, **PostgreSQL** database, **JWT** authentication, **Chart.js** data visualizations, **Pytest & Django TestCase** testing suite, and containerized deployment via **Docker + Nginx**.

---

## 🚀 Tech Stack Overview

- **Frontend**: React 18, JavaScript (ES6+), Bootstrap 5, Bootstrap Icons, Chart.js, React-Chartjs-2, Axios, Vite
- **Backend**: Django 5.x, Django REST Framework (DRF), SimpleJWT, django-cors-headers
- **Database**: PostgreSQL 16 (with SQLite fallback for local quick testing)
- **Authentication**: Stateless JSON Web Tokens (JWT) with automatic refresh interceptors
- **Testing**: Pytest, Pytest-Django, Django TestCase
- **Deployment**: Docker, Docker Compose, Nginx Reverse Proxy Gateway

---

## 📁 Project Structure

```
campus-management/
│
├── frontend/                     # React 18 Single Page Application
│   ├── public/                   # Static assets & favicon
│   ├── src/
│   │   ├── api/                  # Axios instance & JWT interceptors
│   │   ├── components/           # UI components (Navbar, Sidebar, StatCard)
│   │   │   └── Charts/           # Chart.js components (Line, Doughnut, Bar)
│   │   ├── context/              # React AuthContext state provider
│   │   ├── pages/                # Dashboard, Login, Students, Courses, Faculty
│   │   ├── App.jsx               # Application routing and layout
│   │   ├── main.jsx              # React DOM mounting & Bootstrap imports
│   │   └── index.css             # Design tokens, glassmorphism & styling
│   ├── index.html                # HTML entrypoint with typography
│   ├── package.json              # Node dependencies & build scripts
│   ├── vite.config.js            # Vite build & proxy configuration
│   └── Dockerfile                # Multi-stage production build
│
├── backend/                      # Django REST Framework Backend
│   ├── core/                     # Project configuration & settings
│   │   ├── __init__.py
│   │   ├── settings.py           # DB, JWT, CORS, and Apps configuration
│   │   ├── urls.py               # Main routing & API root
│   │   ├── wsgi.py               # WSGI entrypoint
│   │   └── asgi.py               # ASGI entrypoint
│   ├── apps/
│   │   ├── authentication/       # Custom User model & JWT auth
│   │   ├── campus/               # Departments, Faculty, Students, Courses
│   │   └── analytics/            # Chart.js aggregated analytics endpoints
│   ├── manage.py                 # Django management command CLI
│   ├── requirements.txt          # Python dependencies
│   └── Dockerfile                # Python container image
│
├── docs/                         # System Documentation
│   ├── ARCHITECTURE.md           # Architecture diagrams & data flow
│   ├── API.md                    # REST API specifications
│   └── SETUP.md                  # Development & production setup guide
│
├── tests/                        # Automated Test Suites
│   ├── conftest.py               # Pytest DB and API fixtures
│   ├── test_auth.py              # JWT authentication & register tests
│   ├── test_campus_api.py        # Campus models & CRUD tests
│   └── test_analytics.py         # Analytics & Chart data payload tests
│
├── docker/                       # Docker & Nginx Deployment Configs
│   ├── backend/
│   │   ├── Dockerfile
│   │   └── entrypoint.sh         # DB wait & auto-migrate script
│   ├── frontend/
│   │   ├── Dockerfile
│   │   └── nginx.conf            # React SPA routing config
│   └── nginx/
│       └── default.conf          # Nginx reverse proxy gateway
│
├── .env.example                  # Environment configuration template
├── .gitignore                    # Git exclusions
├── docker-compose.yml            # Multi-container orchestration (DB, API, Web, Proxy)
├── pytest.ini                    # Pytest test discovery settings
└── README.md                     # Project documentation
```

---

## ⚡ Quick Start with Docker

```bash
# Clone or open the repository
cd campus-management

# Start the full stack with Docker Compose
docker compose up --build -d
```

### Access URLs:
- 🌐 **Nginx Gateway**: [http://localhost](http://localhost) (Routes both frontend and `/api/` endpoints)
- 💻 **Frontend Dev**: [http://localhost:3000](http://localhost:3000)
- 🔌 **Backend API**: [http://localhost:8000/api/](http://localhost:8000/api/)
- ⚙️ **Django Admin**: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 🔑 Pre-Configured Demo Accounts

| Role | Username | Password |
|---|---|---|
| **Administrator** | `admin` | `admin123` |
| **Student** | `student` | `student123` |
| **Faculty Member** | `prof_smith` | `faculty123` |

---

## 🛠️ Standalone Local Development

### 1. Backend (Django)
```bash
cd backend
python -m venv venv
# Activate venv:
# On Windows: .\venv\Scripts\activate
# On Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py init_demo_data
python manage.py runserver 0.0.0.0:8000
```

### 2. Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```

---

## 🧪 Running Automated Tests

```bash
# Run all tests via Pytest
pytest

# Run tests with coverage
pytest --tb=short
```

---

## 📊 Analytics & Visualizations

The system provides Chart.js integrated charts:
- **Enrollment Trends**: Dynamic line chart tracking student intake.
- **Department Distribution**: Interactive doughnut chart breaking down enrollments across academic faculties.
- **Performance & Grade Standings**: Bar chart illustrating academic GPA and grade spreads.
