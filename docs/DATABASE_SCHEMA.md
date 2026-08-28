# 🗄️ Database Schema & Entity Relational Model

Complete database schema definitions and relationship mapping across all 15 modular tables.

---

## 1. Core Entity Tables

### 1. `accounts_user`
| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BigAutoField | Primary Key | User internal identifier |
| `username` | CharField(150) | Unique, Not Null | Institutional login handle |
| `email` | EmailField | Unique, Not Null | Official university email |
| `password` | CharField(128) | Not Null | PBKDF2 SHA-256 hashed password |
| `role` | CharField(20) | Choices: ADMIN, FACULTY, STUDENT | Role authorization |

---

### 2. `departments_department`
| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BigAutoField | Primary Key | Department identifier |
| `name` | CharField(100) | Unique, Not Null | e.g. Computer Science & Engineering |
| `code` | CharField(10) | Unique, Not Null | CSE, ECE, EEE, MECH, CIVIL |
| `hod_id` | ForeignKey | User, Nullable | Head of Department |

---

### 3. `students_student`
| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BigAutoField | Primary Key | Student record ID |
| `user_id` | OneToOne | User, Cascade | Linked authentication account |
| `student_id` | CharField(50) | Unique, Indexed | Institutional roll number (e.g. STU-2026-001) |
| `name` | CharField(100) | Not Null | Student full legal name |
| `department_id` | ForeignKey | Department, Cascade | Enrolled department |
| `year` | PositiveIntegerField | Default: 1 | Current academic year (1–4) |
| `section` | CharField(10) | Default: 'A' | Section / Cohort identifier |

---

### 4. `faculty_faculty`
| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BigAutoField | Primary Key | Faculty record ID |
| `user_id` | OneToOne | User, Cascade | Linked authentication account |
| `faculty_id` | CharField(50) | Unique, Indexed | Institutional staff ID (e.g. FAC-CSE-001) |
| `name` | CharField(100) | Not Null | Faculty full legal name |
| `designation` | CharField(50) | Choices | Professor, Associate Professor, Asst. Professor |
| `department_id` | ForeignKey | Department, Cascade | Department affiliation |

---

### 5. `courses_course` & `courses_timetableentry`
| Table | Column | Type | Description |
|---|---|---|---|
| `courses_course` | `code` | CharField(20) | Unique Course Code (e.g. CSE-101) |
| `courses_course` | `title` | CharField(200) | Full Subject Name |
| `courses_course` | `credits` | IntegerField | Academic Credits (3–4) |
| `courses_timetableentry` | `day_of_week` | CharField(20) | Monday–Friday |
| `courses_timetableentry` | `start_time` / `end_time` | TimeField | Class time slot |
| `courses_timetableentry` | `room_number` | CharField(50) | Allocated campus classroom |

---

### 6. `attendance_attendancerecord`
| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | BigAutoField | Primary Key | Attendance record ID |
| `student_id` | ForeignKey | Student, Cascade | Enrolled student |
| `course_id` | ForeignKey | Course, Cascade | Course subject |
| `date` | DateField | Indexed | Session date |
| `status` | CharField(20) | Choices | PRESENT, ABSENT, LATE, LEAVE |

---

### 7. `examinations_exam` & `examinations_examresult`
| Table | Column | Type | Description |
|---|---|---|---|
| `examinations_exam` | `title` | CharField(150) | Mid-Term, End-Semester, Lab Exam |
| `examinations_exam` | `max_internal_marks` | DecimalField | Max internal score component |
| `examinations_exam` | `max_external_marks` | DecimalField | Max external score component |
| `examinations_examresult` | `marks_obtained` | DecimalField | Total composite score |
| `examinations_examresult` | `grade` | CharField(5) | A+, A, B+, B, C, P, F |
| `examinations_examresult` | `grade_point` | DecimalField | 10.0, 9.0, 8.0, 7.0, 6.0, 4.0, 0.0 |

---

### 8. `fees_feepayment`
| Column | Type | Constraints | Description |
|---|---|---|---|
| `invoice_number` | CharField(50) | Unique, Indexed | Unique billing invoice number |
| `student_id` | ForeignKey | Student, Cascade | Student fee account |
| `fee_structure_id` | ForeignKey | FeeStructure, Cascade | Billed semester fee item |
| `amount_paid` | DecimalField | Min: 0.01 | Paid transaction amount |
| `payment_method` | CharField(30) | Choices | ONLINE, CREDIT_CARD, NET_BANKING, CASH |
| `transaction_id` | CharField(100) | Unique reference | Gateway reference ID |
| `status` | CharField(20) | SUCCESS, PENDING, FAILED | Payment verification status |
