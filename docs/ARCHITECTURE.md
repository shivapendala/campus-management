# 🏛️ Architecture & System Design Document

## 1. High-Level Modular Architecture

The Campus Management System is designed as an **Enterprise Clean Modular Monolith** with decoupled service boundaries:

```
[ Web Clients (React 18 + Vite) ]
                │
         HTTPS / REST API
                ▼
┌───────────────────────────────────────────────┐
│           Django REST Framework (DRF)         │
│  ┌─────────────────┬──────────────────────┐  │
│  │   Auth / JWT    │   Permission Guard   │  │
│  └─────────────────┴──────────────────────┘  │
│  ┌─────────────────────────────────────────┐  │
│  │       15 Modular Domain Applications    │  │
│  │ accounts    │ students  │ faculty       │  │
│  │ departments │ courses   │ timetable     │  │
│  │ attendance  │ exams     │ assignments   │  │
│  │ fees        │ library   │ placements    │  │
│  │ complaints  │ events    │ notifications │  │
│  │ reports     │           │               │  │
│  └─────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────┐  │
│  │          Domain Business Services       │  │
│  │  GradingEngine │ ShortageAudit │ Ledger │  │
│  └─────────────────────────────────────────┘  │
└───────────────────────┬───────────────────────┘
                        ▼
       [ PostgreSQL 16 Relational Engine ]
```

---

## 2. Layered Software Architecture

1. **Presentation Layer (React 18 SPA)**:
   - Modern component library built with vanilla CSS design tokens, glassmorphism, dynamic animations, and responsive flex/grid layouts.
   - Centralized Axios client (`apiClient.js`) with automatic JWT bearer header injection.
   - Dual-mode perspectives for Administrators, Faculty, and Students.

2. **API & Serialization Layer (Django REST Framework)**:
   - Strict ModelSerializers validating incoming payload types, foreign keys, and unique constraints.
   - URL routers organizing nested endpoints by domain.

3. **Domain Service Layer**:
   - `ExaminationGradingService`: 10-point standard grading scale and credit-weighted SGPA engine.
   - `AttendanceAnalyticsService`: Percentage calculations, condonation shortage filtering, and monthly heatmaps.
   - `FinancialLedgerService`: Fiscal realization, collection rate computation, and receipt generation.
   - `StudentDossierService`: GPA aggregation, student ID generation, and atomic CSV batch imports.

4. **Persistence Layer (PostgreSQL / SQLite)**:
   - Fully normalized relational schema with foreign key integrity, cascade protection, and composite indexing on query patterns.
