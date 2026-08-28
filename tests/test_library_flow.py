import pytest
from datetime import date, timedelta
from django.urls import reverse
from rest_framework import status
from apps.library.models import Book, BookIssue


@pytest.mark.django_db
class TestLibraryCompleteFlow:
    def test_book_catalog_and_issue_return_cycle(self, auth_client, admin_user):
        book = Book.objects.create(
            title='Clean Architecture in Python',
            author='Robert C. Martin',
            isbn='978-0134494166',
            total_copies=10,
            available_copies=10,
        )
        assert book.available_copies == 10

        issue = BookIssue.objects.create(
            book=book,
            user=admin_user,
            due_date=date.today() + timedelta(days=14),
            status='ISSUED',
        )
        assert issue.id is not None

        url = reverse('book-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
