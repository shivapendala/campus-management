import re
from typing import Dict, Any, Optional
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import permissions

User = get_user_model()


class AuthenticationService:
    """
    Enterprise Authentication and Security domain service.
    Handles credential verification, session issuance, password policies, and role provisioning.
    """

    @staticmethod
    def validate_password_strength(password: str) -> None:
        """
        Enforces institutional password complexity:
        - At least 8 characters
        - Contains at least 1 uppercase letter
        - Contains at least 1 digit
        - Contains at least 1 special character
        """
        if len(password) < 8:
            raise ValidationError("Password must contain at least 8 characters.")
        if not re.search(r"[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r"[0-9]", password):
            raise ValidationError("Password must contain at least one numerical digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Password must contain at least one special character symbol.")

    @classmethod
    def register_campus_user(cls, user_data: Dict[str, Any]) -> User:
        """
        Provisions a new campus user with encrypted credentials and role assignment.
        """
        raw_password = user_data.get('password', '')
        cls.validate_password_strength(raw_password)

        username = user_data.get('username')
        email = user_data.get('email')
        role = user_data.get('role', 'STUDENT')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=raw_password,
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', ''),
            role=role
        )
        return user


class IsCampusAdmin(permissions.BasePermission):
    """
    Allows access only to authenticated Campus Administrators.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (request.user.role == 'ADMIN' or request.user.is_staff))


class IsFacultyMember(permissions.BasePermission):
    """
    Allows access to Faculty Members and Admins.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in ['FACULTY', 'ADMIN'])


class IsStudentUser(permissions.BasePermission):
    """
    Allows access to Students and Admins.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in ['STUDENT', 'ADMIN'])
