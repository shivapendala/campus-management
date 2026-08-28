# Campus Management REST API Documentation

Base URL: `/api`

All protected endpoints require the header:
```http
Authorization: Bearer <access_token>
```

---

## 1. Authentication Endpoints

### 1.1 Obtain JWT Token (Login)
- **Endpoint**: `POST /api/auth/token/`
- **Auth**: Public
- **Request Body**:
  ```json
  {
    "username": "admin",
    "password": "admin123"
  }
  ```
- **Response** (`200 OK`):
  ```json
  {
    "access": "eyJhbGciOi...",
    "refresh": "eyJhbGciOi...",
    "user": {
      "id": 1,
      "username": "admin",
      "email": "admin@campus.edu",
      "role": "ADMIN",
      "first_name": "Admin",
      "last_name": "Director",
      "department_name": "Campus Administration"
    }
  }
  ```

### 1.2 Refresh JWT Access Token
- **Endpoint**: `POST /api/auth/token/refresh/`
- **Auth**: Public
- **Request Body**:
  ```json
  {
    "refresh": "eyJhbGciOi..."
  }
  ```
- **Response** (`200 OK`):
  ```json
  {
    "access": "eyJhbGciOi..."
  }
  ```

### 1.3 Register New User
- **Endpoint**: `POST /api/auth/register/`
- **Auth**: Public
- **Request Body**:
  ```json
  {
    "username": "johndoe",
    "email": "john@campus.edu",
    "password": "securePassword123",
    "password_confirm": "securePassword123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "STUDENT"
  }
  ```

### 1.4 Get / Update User Profile
- **Endpoint**: `GET /api/auth/profile/`, `PUT /api/auth/profile/`
- **Auth**: Bearer Token required

---

## 2. Campus Academic Endpoints

### 2.1 Departments
- `GET /api/campus/departments/` — List all departments
- `POST /api/campus/departments/` — Create new department
- `GET /api/campus/departments/{id}/` — Department details
- `PUT /api/campus/departments/{id}/` — Update department
- `DELETE /api/campus/departments/{id}/` — Delete department

### 2.2 Students
- `GET /api/campus/students/` — List students (searchable by ID, name, department)
- `POST /api/campus/students/` — Create student profile
- `GET /api/campus/students/{id}/` — Retrieve student details

### 2.3 Faculty
- `GET /api/campus/faculty/` — List faculty members
- `POST /api/campus/faculty/` — Create faculty record
- `GET /api/campus/faculty/{id}/` — Faculty details

### 2.4 Courses
- `GET /api/campus/courses/` — List active courses
- `POST /api/campus/courses/` — Create course
- `GET /api/campus/courses/{id}/` — Course details

### 2.5 Enrollments
- `GET /api/campus/enrollments/` — List student course enrollments
- `POST /api/campus/enrollments/` — Enroll student into a course

---

## 3. Analytics & Reporting Endpoints

### 3.1 Dashboard KPI Overview
- **Endpoint**: `GET /api/analytics/overview/`
- **Auth**: Bearer Token required
- **Response** (`200 OK`):
  ```json
  {
    "total_students": 1240,
    "total_faculty": 84,
    "total_courses": 52,
    "total_departments": 5,
    "average_gpa": 3.65,
    "average_attendance": 92.4,
    "active_semester": "Fall 2026"
  }
  ```

### 3.2 Enrollment Trends (Chart.js Line)
- **Endpoint**: `GET /api/analytics/enrollment-trends/`
- **Auth**: Bearer Token required

### 3.3 Department Student Distribution (Chart.js Doughnut)
- **Endpoint**: `GET /api/analytics/department-distribution/`
- **Auth**: Bearer Token required

### 3.4 Grade Distribution (Chart.js Bar)
- **Endpoint**: `GET /api/analytics/grade-distribution/`
- **Auth**: Bearer Token required
