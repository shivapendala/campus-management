# 📖 Campus Management System — Comprehensive API Documentation

RESTful OpenAPI 3.0 compliant API endpoints specification for all 15 modular subsystems.

---

## 1. Base URL & Authentication

- **Base Endpoint**: `http://localhost:8000/api/v1/`
- **Authentication Header**: `Authorization: Bearer <JWT_ACCESS_TOKEN>`

---

## 2. Authentication & User Provisioning (`/api/v1/auth/`)

| Method | Endpoint | Description | Request Body | Response |
|---|---|---|---|---|
| `POST` | `/auth/register/` | Register new user | `{ "username", "email", "password", "role" }` | `201 Created` |
| `POST` | `/auth/login/` | Obtain JWT tokens | `{ "username", "password" }` | `{ "access", "refresh", "user" }` |
| `POST` | `/auth/token/refresh/` | Refresh expired access token | `{ "refresh" }` | `{ "access" }` |
| `POST` | `/auth/forgot-password/` | Request password reset token | `{ "email" }` | `200 OK` |
| `POST` | `/auth/reset-password/` | Reset password using token | `{ "token", "new_password" }` | `200 OK` |
| `GET` | `/auth/users/me/` | Current user profile | `None` | User object |

---

## 3. Student Management (`/api/v1/students/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/students/students/` | List all students with search & filter | `?search=alex&department=CSE` | Paginated Students list |
| `POST` | `/students/students/` | Enroll new student | Student JSON schema | `201 Created` |
| `GET` | `/students/students/{id}/` | Full 360° student profile dossier | `None` | Student dossier |
| `PUT` | `/students/students/{id}/` | Update student profile | Updated fields | `200 OK` |
| `DELETE` | `/students/students/{id}/` | Delete student record | `None` | `204 No Content` |
| `POST` | `/students/students/import_csv/` | Batch import students via CSV | Multi-part Form (file) | `{ "imported", "errors" }` |
| `GET` | `/students/students/export_csv/` | Export student roster to CSV | `None` | `text/csv` stream |

---

## 4. Faculty Management (`/api/v1/faculty/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/faculty/faculty/` | List faculty directory | `?department=CSE` | Paginated Faculty list |
| `POST` | `/faculty/faculty/` | Add faculty member | Faculty JSON schema | `201 Created` |
| `GET` | `/faculty/faculty/{id}/` | Faculty workload and profile | `None` | Faculty details |
| `POST` | `/faculty/faculty/{id}/assign_course/` | Assign subject / course | `{ "course_id" }` | `200 OK` |

---

## 5. Department Management (`/api/v1/departments/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/departments/departments/` | List all departments | `None` | `[CSE, ECE, EEE, MECH, CIVIL]` |
| `POST` | `/departments/departments/` | Create department | `{ "name", "code", "hod_id" }` | `201 Created` |
| `GET` | `/departments/departments/{id}/stats/` | Department statistics | `None` | `{ "students", "faculty", "courses" }` |

---

## 6. Course & Timetable Management (`/api/v1/courses/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/courses/courses/` | List courses catalog | `?department=CSE` | Paginated Courses list |
| `POST` | `/courses/courses/` | Create course & 5-unit syllabus | Course JSON schema | `201 Created` |
| `GET` | `/courses/timetable/` | Weekly schedule matrix | `?day=Monday&section=A` | Timetable grid entries |
| `POST` | `/courses/timetable/check_conflicts/` | Check room/faculty conflict | Slot JSON | `{ "conflict": bool, "details" }` |

---

## 7. Attendance System (`/api/v1/attendance/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `POST` | `/attendance/records/bulk_record/` | Faculty roll-call save | `{ "course_id", "date", "records" }` | `200 OK` |
| `GET` | `/attendance/records/monthly_report/` | Monthly attendance heatmap | `?course_id=1&month=8` | Attendance matrix |
| `GET` | `/attendance/records/semester_report/` | Condonation shortage audit | `?department_id=1` | Shortage list (<75%) |

---

## 8. Examination & Grading Engine (`/api/v1/examinations/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `POST` | `/examinations/exams/` | Schedule exam | Exam JSON schema | `201 Created` |
| `POST` | `/examinations/exams/{id}/submit_marks/` | Submit internal/external marks | `{ "marks": [...] }` | `200 OK` |
| `POST` | `/examinations/exams/{id}/verify_by_hod/` | HOD verification | `None` | `200 OK` |
| `GET` | `/examinations/exams/student_grade_card/` | Official Grade Card with SGPA | `?student_id=STU-001` | Grade dossier |

---

## 9. Assignments System (`/api/v1/assignments/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `POST` | `/assignments/assignments/` | Create assignment | `{ "title", "course_id", "deadline", "max_score" }` | `201 Created` |
| `POST` | `/assignments/assignments/{id}/submit/` | Student solution upload | `{ "submission_text", "submission_file_url" }` | `200 OK` |
| `POST` | `/assignments/submissions/{id}/grade/` | Faculty review & feedback | `{ "score", "feedback" }` | `200 OK` |

---

## 10. Fees Management & Receipts (`/api/v1/fees/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/fees/structures/` | List fee structures | `?semester=4` | Fee structures |
| `POST` | `/fees/payments/` | Process payment | Payment JSON schema | `201 Created` |
| `GET` | `/fees/payments/financial-summary/` | Total/Collected/Pending KPIs | `None` | Financial summary |
| `GET` | `/fees/payments/{id}/receipt/` | Official printable receipt | `None` | Receipt JSON schema |

---

## 11. Library Commons (`/api/v1/library/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/library/books/` | Search book catalog | `?search=algorithms` | Paginated books |
| `POST` | `/library/books/` | Add book to catalog | Book JSON schema | `201 Created` |
| `POST` | `/library/issues/` | Checkout book to student | `{ "book_id", "student_id", "due_date" }` | `201 Created` |
| `POST` | `/library/issues/{id}/return-book/` | Return book & calculate fines | `None` | `{ "fine", "status" }` |

---

## 12. Placements & Drives (`/api/v1/placements/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/placements/drives/` | List active recruitment drives | `None` | Drives list |
| `POST` | `/placements/drives/` | Announce hiring drive | Drive JSON schema | `201 Created` |
| `POST` | `/placements/applications/` | Submit job application | `{ "drive_id", "resume_url" }` | `201 Created` |

---

## 13. Grievance Redressal (`/api/v1/complaints/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/complaints/complaints/` | List grievance tickets | `?status=OPEN` | Complaints list |
| `POST` | `/complaints/complaints/` | Lodge complaint | Ticket JSON schema | `201 Created` |
| `POST` | `/complaints/complaints/{id}/resolve/` | Resolve complaint ticket | `{ "resolution_remarks" }` | `200 OK` |

---

## 14. Events & Registrations (`/api/v1/events/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/events/events/` | List campus events | `None` | Events list |
| `POST` | `/events/events/` | Create campus event | Event JSON schema | `201 Created` |
| `POST` | `/events/registrations/` | Claim event pass | `{ "event_id", "student_id" }` | `201 Created` |

---

## 15. Notifications & Broadcasts (`/api/v1/notifications/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/notifications/notifications/` | List notices feed | `?type=EXAMINATION` | Notices list |
| `POST` | `/notifications/notifications/` | Broadcast notice | Notice JSON schema | `201 Created` |
| `POST` | `/notifications/notifications/{id}/mark_read/` | Mark notice as read | `None` | `200 OK` |

---

## 16. Analytics & Reports Engine (`/api/v1/reports/`)

| Method | Endpoint | Description | Query / Body | Response |
|---|---|---|---|---|
| `GET` | `/reports/reports/executive_summary/` | Executive multi-module KPI summary | `None` | Executive intelligence |
| `GET` | `/reports/reports/academic_analytics/` | Grade distribution & pass rates | `None` | Academic metrics |
| `GET` | `/reports/reports/financial_audit/` | Financial audit ledger | `None` | Audit metrics |
