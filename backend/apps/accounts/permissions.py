from rest_framework import permissions
from .models import UserRole


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (request.user.role == UserRole.ADMIN or request.user.is_superuser))


class IsHOD(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in [UserRole.ADMIN, UserRole.HOD])


class IsFaculty(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role in [UserRole.ADMIN, UserRole.HOD, UserRole.FACULTY])


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == UserRole.STUDENT)


class HasRole(permissions.BasePermission):
    """
    Dynamic permission class checking against a tuple of allowed roles.
    Usage: permission_classes = [HasRole(['ADMIN', 'FACULTY'])]
    """
    def __init__(self, allowed_roles=None):
        self.allowed_roles = allowed_roles or []

    def __call__(self):
        return self

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        if request.user.is_superuser or request.user.role == UserRole.ADMIN:
            return True
        return request.user.role in self.allowed_roles
