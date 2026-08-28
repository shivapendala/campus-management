"""
EduCore Enterprise Framework - Structured Exception Hierarchy (RFC 7807)

Defines domain-specific business exceptions and formats RFC-7807 Problem Details:
- AcademicDetentionException
- FeeShortageException
- AttendanceShortageException
- PrerequisiteViolationException
- DuplicateEnrollmentException
"""

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger("EduCore.Exceptions")


class EduCoreBaseException(Exception):
    """Base exception for all domain errors in EduCore platform."""
    default_code = "INTERNAL_ERROR"
    default_status = 500

    def __init__(self, message: str, code: str = None, details: dict = None):
        super().__init__(message)
        self.message = message
        self.code = code or self.default_code
        self.details = details or {}


class AcademicDetentionException(EduCoreBaseException):
    default_code = "STUDENT_ACADEMICALLY_DETAINED"
    default_status = 403


class FeeShortageException(EduCoreBaseException):
    default_code = "OUTSTANDING_FEE_DUES"
    default_status = 402


class AttendanceShortageException(EduCoreBaseException):
    default_code = "ATTENDANCE_BELOW_STATUTORY_MINIMUM"
    default_status = 403


class PrerequisiteViolationException(EduCoreBaseException):
    default_code = "COURSE_PREREQUISITES_NOT_MET"
    default_status = 400


class DuplicateEnrollmentException(EduCoreBaseException):
    default_code = "STUDENT_ALREADY_ENROLLED"
    default_status = 409


def custom_rfc7807_exception_handler(exc, context):
    """
    Transforms DRF and custom exceptions into RFC-7807 Problem Details JSON format.
    """
    response = exception_handler(exc, context)

    if response is not None:
        custom_data = {
            "type": f"https://educore.campus.edu/errors/{getattr(exc, 'code', 'error').lower()}",
            "title": getattr(exc, "message", str(response.data.get("detail", "An error occurred."))),
            "status": response.status_code,
            "invalid_params": response.data if isinstance(response.data, dict) else {},
            "instance": context.get("request").path if context.get("request") else None
        }
        response.data = custom_data
    elif isinstance(exc, EduCoreBaseException):
        response = Response({
            "type": f"https://educore.campus.edu/errors/{exc.code.lower()}",
            "title": exc.message,
            "status": exc.default_status,
            "details": exc.details
        }, status=exc.default_status)
    else:
        logger.error("Unhandled system exception: %s", exc, exc_info=True)

    return response
