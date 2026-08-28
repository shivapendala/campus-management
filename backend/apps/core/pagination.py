"""
EduCore Enterprise Framework - Standardized API Pagination Classes

Provides flexible pagination strategies for large academic datasets:
- StandardPageNumberPagination (Configurable page size, max 100)
- FastLimitOffsetPagination
- KeysetCursorPagination (For massive audit logs and telemetry streams)
"""

from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.response import Response


class StandardInstitutionalPagination(PageNumberPagination):
    """
    Standard page-number pagination with metadata headers.
    """
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "pagination": {
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "current_page": self.page.number,
                "page_size": self.get_page_size(self.request),
                "next": self.get_next_link(),
                "previous": self.get_previous_link()
            },
            "results": data
        })


class CompactLimitOffsetPagination(LimitOffsetPagination):
    """
    High-speed limit-offset pagination for dashboard KPI feeds.
    """
    default_limit = 10
    max_limit = 50
    limit_query_param = "limit"
    offset_query_param = "offset"


class AuditStreamCursorPagination(CursorPagination):
    """
    Cursor pagination for high-volume append-only audit trails.
    """
    page_size = 50
    cursor_query_param = "cursor"
    ordering = "-timestamp"
