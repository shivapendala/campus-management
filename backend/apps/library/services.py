from datetime import date
from decimal import Decimal
from typing import Dict, Any, List
from .models import Book, BookIssue, IssueStatus


class LibraryCirculationService:
    """
    Domain service for Book Circulation, Inventory Tracking, and Automated Daily Overdue Fine Calculation.
    """

    FINE_PER_OVERDUE_DAY = Decimal('1.00')

    @classmethod
    def calculate_overdue_fines(cls, issue: BookIssue) -> Decimal:
        """
        Computes fine based on overdue days elapsed past the return due date.
        """
        if issue.status == IssueStatus.RETURNED or date.today() <= issue.due_date:
            return Decimal('0.00')

        overdue_days = (date.today() - issue.due_date).days
        return Decimal(overdue_days * cls.FINE_PER_OVERDUE_DAY).quantize(Decimal('0.01'))

    @classmethod
    def reconcile_catalog_inventory(cls) -> Dict[str, Any]:
        """
        Reconciles total library book assets, active circulations, and overdue fines outstanding.
        """
        books = Book.objects.all()
        total_books = books.count()
        total_copies = sum(b.total_copies for b in books)
        available_copies = sum(b.available_copies for b in books)
        active_issues = BookIssue.objects.filter(status=IssueStatus.ISSUED).count()
        overdue_issues = BookIssue.objects.filter(status=IssueStatus.OVERDUE).count()

        return {
            'total_titles': total_books,
            'total_physical_copies': total_copies,
            'available_in_stacks': available_copies,
            'active_borrowed_copies': active_issues,
            'overdue_count': overdue_issues,
            'utilization_rate_pct': round(((total_copies - available_copies) / max(1, total_copies)) * 100, 1),
        }
