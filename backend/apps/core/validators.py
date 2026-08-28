"""
EduCore Enterprise Framework - Validation Suite

Standardized validation utilities for Indian & Global Higher-Education Data:
Roll numbers, faculty codes, course codes, phone numbers, GPA/CGPA scores,
monetary figures, ISBN-10/13 formats, and academic semester ranges.
"""

import re
from typing import Tuple, Optional


class InstitutionalDataValidator:
    """Enterprise validation rules for institutional data models."""

    ROLL_NUMBER_REGEX = re.compile(r"^[0-9]{2}[A-Z]{2}[0-9]{1}[A-Z0-9]{1}[0-9]{4}$", re.IGNORECASE)
    FACULTY_CODE_REGEX = re.compile(r"^FAC-[A-Z]{2,4}-[0-9]{3,5}$", re.IGNORECASE)
    COURSE_CODE_REGEX = re.compile(r"^[A-Z]{2,4}[0-9]{3,4}$", re.IGNORECASE)
    PHONE_REGEX = re.compile(r"^\+?[0-9]{10,15}$")
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    @classmethod
    def validate_roll_number(cls, roll_number: str) -> Tuple[bool, Optional[str]]:
        """Validate university standardized student roll number format (e.g., 23CSE01042)."""
        if not roll_number or not isinstance(roll_number, str):
            return False, "Roll number cannot be empty."
        cleaned = roll_number.strip().upper()
        if len(cleaned) < 5 or len(cleaned) > 20:
            return False, "Roll number length must be between 5 and 20 characters."
        return True, None

    @classmethod
    def validate_faculty_code(cls, faculty_code: str) -> Tuple[bool, Optional[str]]:
        """Validate faculty employee identifier (e.g., FAC-CSE-001)."""
        if not faculty_code or not isinstance(faculty_code, str):
            return False, "Faculty code cannot be empty."
        cleaned = faculty_code.strip()
        if not cls.FACULTY_CODE_REGEX.match(cleaned):
            return False, "Faculty code format must match 'FAC-<DEPT>-<ID>' (e.g. FAC-CSE-001)."
        return True, None

    @classmethod
    def validate_course_code(cls, course_code: str) -> Tuple[bool, Optional[str]]:
        """Validate curriculum course code (e.g., CS301, EC204)."""
        if not course_code or not isinstance(course_code, str):
            return False, "Course code cannot be empty."
        cleaned = course_code.strip().upper()
        if not cls.COURSE_CODE_REGEX.match(cleaned):
            return False, "Course code must consist of 2-4 uppercase letters followed by 3-4 digits (e.g., CS301)."
        return True, None

    @classmethod
    def validate_cgpa(cls, cgpa: float, scale: float = 10.0) -> Tuple[bool, Optional[str]]:
        """Validate CGPA or SGPA score against institutional grade scale."""
        try:
            val = float(cgpa)
        except (ValueError, TypeError):
            return False, "CGPA must be a valid numeric decimal."
        if val < 0.0 or val > scale:
            return False, f"CGPA must be between 0.0 and {scale}."
        return True, None

    @classmethod
    def validate_attendance_percentage(cls, percentage: float) -> Tuple[bool, Optional[str]]:
        """Validate attendance percentage range (0.0 to 100.0)."""
        try:
            val = float(percentage)
        except (ValueError, TypeError):
            return False, "Attendance percentage must be numeric."
        if val < 0.0 or val > 100.0:
            return False, "Attendance percentage must be between 0.0% and 100.0%."
        return True, None

    @classmethod
    def validate_isbn(cls, isbn: str) -> Tuple[bool, Optional[str]]:
        """Validate ISBN-10 or ISBN-13 book catalog number with checksum."""
        cleaned = isbn.replace("-", "").replace(" ", "").upper()
        if len(cleaned) == 10:
            # ISBN-10 checksum validation
            total = 0
            for i, char in enumerate(cleaned):
                if char == 'X' and i == 9:
                    val = 10
                elif char.isdigit():
                    val = int(char)
                else:
                    return False, "Invalid character in ISBN-10."
                total += val * (10 - i)
            if total % 11 == 0:
                return True, None
            return False, "Invalid ISBN-10 checksum."

        elif len(cleaned) == 13:
            # ISBN-13 checksum validation
            if not cleaned.isdigit():
                return False, "ISBN-13 must contain only digits."
            total = 0
            for i, digit in enumerate(cleaned):
                weight = 1 if i % 2 == 0 else 3
                total += int(digit) * weight
            if total % 10 == 0:
                return True, None
            return False, "Invalid ISBN-13 checksum."

        return False, "ISBN length must be either 10 or 13 digits."

    @classmethod
    def validate_monetary_amount(cls, amount: float, min_val: float = 0.0, max_val: float = 10000000.0) -> Tuple[bool, Optional[str]]:
        """Validate currency monetary amount for fees, scholarships, and salaries."""
        try:
            val = float(amount)
        except (ValueError, TypeError):
            return False, "Monetary amount must be numeric."
        if val < min_val:
            return False, f"Amount cannot be less than {min_val}."
        if val > max_val:
            return False, f"Amount exceeds maximum institutional limit of {max_val}."
        return True, None
