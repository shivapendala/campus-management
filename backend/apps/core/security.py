"""
EduCore Enterprise Framework - Security & RBAC Engine

Implements enterprise-grade Role-Based Access Control (RBAC), permission matrices,
cryptographic verification, JWT token blacklist management, session lifecycle tracking,
and password complexity policy enforcement for higher-education campus systems.
"""

import re
import hmac
import hashlib
import secrets
import datetime
from typing import Dict, List, Set, Optional, Tuple, Any
from dataclasses import dataclass, field


@dataclass
class PermissionDefinition:
    """Represents a granular permission in the campus management system."""
    code: str
    name: str
    category: str
    description: str
    risk_level: str = "NORMAL"  # LOW, NORMAL, HIGH, CRITICAL
    requires_mfa: bool = False


@dataclass
class RoleDefinition:
    """Represents an institutional role with associated permissions and hierarchy."""
    role_id: str
    name: str
    hierarchy_level: int  # 1 (Admin) to 7 (Guest)
    permissions: Set[str] = field(default_factory=set)
    inherits_from: List[str] = field(default_factory=list)
    is_system_role: bool = True
    description: str = ""


class InstitutionalPermissionMatrix:
    """
    Centralized RBAC Matrix defining permissions for all 7 campus roles:
    ADMIN, HOD, FACULTY, STUDENT, LIBRARIAN, ACCOUNTANT, RECRUITER.
    """

    PERMISSION_REGISTRY: Dict[str, PermissionDefinition] = {
        # Student Management
        "student.view": PermissionDefinition("student.view", "View Students", "STUDENTS", "View student profiles and directory"),
        "student.create": PermissionDefinition("student.create", "Create Student", "STUDENTS", "Enroll new students into institution", "HIGH"),
        "student.edit": PermissionDefinition("student.edit", "Edit Student", "STUDENTS", "Update student biographical and academic data", "HIGH"),
        "student.delete": PermissionDefinition("student.delete", "Delete Student", "STUDENTS", "Archive or remove student records", "CRITICAL", requires_mfa=True),
        "student.export": PermissionDefinition("student.export", "Export Students", "STUDENTS", "Export student roster to CSV/PDF", "HIGH"),

        # Faculty Management
        "faculty.view": PermissionDefinition("faculty.view", "View Faculty", "FACULTY", "View faculty directory and profiles"),
        "faculty.create": PermissionDefinition("faculty.create", "Create Faculty", "FACULTY", "Add new faculty member", "HIGH"),
        "faculty.edit": PermissionDefinition("faculty.edit", "Edit Faculty", "FACULTY", "Update faculty designations and departments", "HIGH"),
        "faculty.delete": PermissionDefinition("faculty.delete", "Delete Faculty", "FACULTY", "Terminate or archive faculty record", "CRITICAL", requires_mfa=True),
        "faculty.assign_subject": PermissionDefinition("faculty.assign_subject", "Assign Subject", "FACULTY", "Assign courses and subjects to faculty"),

        # Academic & Curriculum
        "course.view": PermissionDefinition("course.view", "View Courses", "ACADEMIC", "View curriculum, subjects, and syllabi"),
        "course.manage": PermissionDefinition("course.manage", "Manage Courses", "ACADEMIC", "Create, edit, or retire courses and syllabi", "HIGH"),
        "department.view": PermissionDefinition("department.view", "View Departments", "ACADEMIC", "View departmental stats and structure"),
        "department.manage": PermissionDefinition("department.manage", "Manage Departments", "ACADEMIC", "Configure departments, budgets, and HODs", "CRITICAL"),
        "timetable.manage": PermissionDefinition("timetable.manage", "Manage Timetables", "ACADEMIC", "Create and modify schedule matrices"),

        # Attendance
        "attendance.mark": PermissionDefinition("attendance.mark", "Mark Attendance", "ATTENDANCE", "Take roll-call attendance for classes"),
        "attendance.view": PermissionDefinition("attendance.view", "View Attendance", "ATTENDANCE", "Inspect attendance percentages and logs"),
        "attendance.audit": PermissionDefinition("attendance.audit", "Audit Attendance", "ATTENDANCE", "Modify retroactive attendance or grant medical exemptions", "HIGH"),

        # Examinations & Grading
        "exam.create": PermissionDefinition("exam.create", "Create Exam", "EXAMINATIONS", "Schedule internal or semester exams", "HIGH"),
        "exam.enter_marks": PermissionDefinition("exam.enter_marks", "Enter Marks", "EXAMINATIONS", "Input student internal or external marks", "HIGH"),
        "exam.verify_results": PermissionDefinition("exam.verify_results", "Verify Results", "EXAMINATIONS", "Approve and publish final semester grade cards", "CRITICAL"),
        "exam.view_results": PermissionDefinition("exam.view_results", "View Results", "EXAMINATIONS", "View individual examination scores"),

        # Financial Operations
        "fee.view": PermissionDefinition("fee.view", "View Fees", "FINANCE", "Inspect student dues, payment logs, and receipts"),
        "fee.collect": PermissionDefinition("fee.collect", "Record Payments", "FINANCE", "Issue official fee receipts and record cash/online payments", "HIGH"),
        "fee.structure_manage": PermissionDefinition("fee.structure_manage", "Manage Fee Structures", "FINANCE", "Set annual tuition, lab, and transport fees", "CRITICAL"),
        "fee.refund": PermissionDefinition("fee.refund", "Process Fee Refunds", "FINANCE", "Approve fee cancellations and refund vouchers", "CRITICAL", requires_mfa=True),

        # Library Operations
        "library.view": PermissionDefinition("library.view", "View Catalog", "LIBRARY", "Search library catalog and check availability"),
        "library.issue": PermissionDefinition("library.issue", "Issue Books", "LIBRARY", "Check out books to students or faculty"),
        "library.manage_catalog": PermissionDefinition("library.manage_catalog", "Manage Catalog", "LIBRARY", "Add or delete books, assign barcodes"),
        "library.collect_fines": PermissionDefinition("library.collect_fines", "Collect Library Fines", "LIBRARY", "Record overdue fine payments"),

        # Placements & Careers
        "placement.view": PermissionDefinition("placement.view", "View Placement Drives", "PLACEMENTS", "View company drives and job vacancies"),
        "placement.manage": PermissionDefinition("placement.manage", "Manage Placements", "PLACEMENTS", "Create drives, schedule interviews, post offers", "HIGH"),
        "placement.apply": PermissionDefinition("placement.apply", "Apply to Drives", "PLACEMENTS", "Submit job applications and resume profiles"),

        # Institutional Administration
        "system.audit_logs": PermissionDefinition("system.audit_logs", "View Audit Logs", "ADMIN", "Inspect full security and operation audit trail", "CRITICAL"),
        "system.settings": PermissionDefinition("system.settings", "Configure System", "ADMIN", "Modify institutional parameters, SMTP, and integrations", "CRITICAL", requires_mfa=True),
        "report.generate": PermissionDefinition("report.generate", "Generate Reports", "REPORTS", "Export compliance, academic, and financial reports", "HIGH"),
    }

    ROLE_DEFINITIONS: Dict[str, RoleDefinition] = {
        "ADMIN": RoleDefinition(
            role_id="ADMIN",
            name="Institutional Administrator",
            hierarchy_level=1,
            permissions=set(PERMISSION_REGISTRY.keys()),
            description="Full omnipotent system administrative privileges across all institutional units"
        ),
        "HOD": RoleDefinition(
            role_id="HOD",
            name="Head of Department",
            hierarchy_level=2,
            permissions={
                "student.view", "student.edit", "student.export",
                "faculty.view", "faculty.assign_subject",
                "course.view", "course.manage", "department.view", "timetable.manage",
                "attendance.view", "attendance.mark", "attendance.audit",
                "exam.create", "exam.enter_marks", "exam.verify_results", "exam.view_results",
                "fee.view",
                "library.view",
                "placement.view",
                "report.generate",
            },
            description="Departmental administrative leader with academic, faculty, and examination oversight"
        ),
        "FACULTY": RoleDefinition(
            role_id="FACULTY",
            name="Faculty Member / Professor",
            hierarchy_level=3,
            permissions={
                "student.view",
                "faculty.view",
                "course.view",
                "department.view",
                "attendance.mark", "attendance.view",
                "exam.enter_marks", "exam.view_results",
                "library.view",
                "placement.view",
                "report.generate",
            },
            description="Teaching staff member with roll-call, internal assessment, and syllabus viewing access"
        ),
        "STUDENT": RoleDefinition(
            role_id="STUDENT",
            name="Enrolled Student",
            hierarchy_level=4,
            permissions={
                "course.view",
                "attendance.view",
                "exam.view_results",
                "fee.view",
                "library.view",
                "placement.view", "placement.apply",
            },
            description="Active enrolled student with personal academic progress, timetable, fee and placement access"
        ),
        "LIBRARIAN": RoleDefinition(
            role_id="LIBRARIAN",
            name="Chief Librarian",
            hierarchy_level=3,
            permissions={
                "student.view", "faculty.view",
                "library.view", "library.issue", "library.manage_catalog", "library.collect_fines",
                "report.generate",
            },
            description="Library curator managing book repository, loans, RFID tracking, and overdue fees"
        ),
        "ACCOUNTANT": RoleDefinition(
            role_id="ACCOUNTANT",
            name="Finance / Accounts Officer",
            hierarchy_level=3,
            permissions={
                "student.view",
                "fee.view", "fee.collect", "fee.structure_manage", "fee.refund",
                "report.generate",
            },
            description="Institutional bursar handling tuition collection, receipts, scholarships, and refunds"
        ),
        "RECRUITER": RoleDefinition(
            role_id="RECRUITER",
            name="Corporate Placement Partner",
            hierarchy_level=5,
            permissions={
                "student.view",
                "placement.view", "placement.manage",
            },
            description="External or internal placement coordinator managing job drives and student candidates"
        ),
    }

    @classmethod
    def has_permission(cls, role_code: str, permission_code: str) -> bool:
        """Check if a specific institutional role possesses the requested permission."""
        normalized_role = role_code.upper()
        role = cls.ROLE_DEFINITIONS.get(normalized_role)
        if not role:
            return False
        return permission_code in role.permissions

    @classmethod
    def get_role_permissions(cls, role_code: str) -> List[PermissionDefinition]:
        """Retrieve all resolved permission objects granted to a role."""
        normalized_role = role_code.upper()
        role = cls.ROLE_DEFINITIONS.get(normalized_role)
        if not role:
            return []
        return [cls.PERMISSION_REGISTRY[p] for p in role.permissions if p in cls.PERMISSION_REGISTRY]

    @classmethod
    def validate_hierarchy_access(cls, actor_role: str, target_role: str) -> bool:
        """Ensure an actor cannot manage a user of equal or higher hierarchy level."""
        actor = cls.ROLE_DEFINITIONS.get(actor_role.upper())
        target = cls.ROLE_DEFINITIONS.get(target_role.upper())
        if not actor or not target:
            return False
        return actor.hierarchy_level < target.hierarchy_level


class PasswordSecurityPolicy:
    """
    Enforces institutional password complexity, dictionary checks,
    entropy calculations, and expiration intervals.
    """

    MIN_LENGTH = 8
    MAX_LENGTH = 128
    REQUIRE_UPPERCASE = True
    REQUIRE_LOWERCASE = True
    REQUIRE_DIGIT = True
    REQUIRE_SPECIAL = True
    SPECIAL_CHARACTERS = r"!@#$%^&*()_+-=[]{}|;:,.<>?"

    COMMON_PASSWORDS = {
        "password", "password123", "admin123", "campus123",
        "college123", "university", "welcome123", "12345678"
    }

    @classmethod
    def evaluate_strength(cls, password: str) -> Tuple[bool, List[str], int]:
        """
        Evaluate password compliance and return (is_valid, error_messages, score_0_to_100).
        """
        errors = []
        score = 0

        if not password:
            return False, ["Password cannot be empty."], 0

        # Length check
        if len(password) < cls.MIN_LENGTH:
            errors.append(f"Password must be at least {cls.MIN_LENGTH} characters long.")
        elif len(password) >= 12:
            score += 30
        else:
            score += 15

        if len(password) > cls.MAX_LENGTH:
            errors.append(f"Password must not exceed {cls.MAX_LENGTH} characters.")

        # Lowercase check
        if cls.REQUIRE_LOWERCASE and not any(c.islower() for c in password):
            errors.append("Password must contain at least one lowercase character (a-z).")
        else:
            score += 15

        # Uppercase check
        if cls.REQUIRE_UPPERCASE and not any(c.isupper() for c in password):
            errors.append("Password must contain at least one uppercase character (A-Z).")
        else:
            score += 15

        # Digit check
        if cls.REQUIRE_DIGIT and not any(c.isdigit() for c in password):
            errors.append("Password must contain at least one numeric digit (0-9).")
        else:
            score += 20

        # Special character check
        if cls.REQUIRE_SPECIAL and not any(c in cls.SPECIAL_CHARACTERS for c in password):
            errors.append("Password must contain at least one special character (!@#$%^&*...).")
        else:
            score += 20

        # Common password check
        if password.lower() in cls.COMMON_PASSWORDS:
            errors.append("This password is too common and easily guessable.")
            score = min(score, 20)

        is_valid = len(errors) == 0
        return is_valid, errors, min(score, 100)


class TokenRevocationBlacklist:
    """
    In-memory / Redis cache proxy for blacklisting revoked JWT tokens
    upon user logout, password reset, or privilege revocation.
    """

    _blacklist: Dict[str, datetime.datetime] = {}

    @classmethod
    def revoke(cls, jti: str, expires_at: datetime.datetime) -> None:
        """Add a token unique identifier (JTI) to the revocation blacklist."""
        cls._blacklist[jti] = expires_at
        cls._cleanup()

    @classmethod
    def is_revoked(cls, jti: str) -> bool:
        """Check if a JTI token has been revoked."""
        if jti not in cls._blacklist:
            return False
        expiry = cls._blacklist[jti]
        if datetime.datetime.now(datetime.timezone.utc) > expiry:
            del cls._blacklist[jti]
            return False
        return True

    @classmethod
    def _cleanup(cls) -> None:
        """Purge expired tokens from the blacklist dictionary."""
        now = datetime.datetime.now(datetime.timezone.utc)
        expired_keys = [k for k, exp in cls._blacklist.items() if now > exp]
        for k in expired_keys:
            del cls._blacklist[k]


class CryptographicSignatureManager:
    """
    Generates HMAC-SHA256 signatures for printable student receipts,
    hall tickets, transcript verification URLs, and digital documents.
    """

    DEFAULT_SALT = "EduCoreInstitutionalCryptographicSalt2026"

    @classmethod
    def generate_document_signature(cls, payload: str, secret_key: Optional[str] = None) -> str:
        """Generate a tamper-evident cryptographic hash signature for a document."""
        secret = (secret_key or cls.DEFAULT_SALT).encode("utf-8")
        h = hmac.new(secret, payload.encode("utf-8"), hashlib.sha256)
        return h.hexdigest()

    @classmethod
    def verify_document_signature(cls, payload: str, signature: str, secret_key: Optional[str] = None) -> bool:
        """Verify that a document payload matches its cryptographic signature."""
        expected = cls.generate_document_signature(payload, secret_key)
        return hmac.compare_digest(expected, signature)

    @classmethod
    def generate_random_token(cls, length: int = 32) -> str:
        """Generate a cryptographically secure random hexadecimal token."""
        return secrets.token_hex(length // 2)
