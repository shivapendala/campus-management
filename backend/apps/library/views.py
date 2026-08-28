from rest_framework import viewsets, permissions, filters
from .models import Book, BookIssue
from .serializers import BookSerializer, BookIssueSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author', 'isbn', 'category', 'rack_number']
    ordering_fields = ['title', 'author', 'publication_year', 'available_copies']


class BookIssueViewSet(viewsets.ModelViewSet):
    queryset = BookIssue.objects.select_related('book', 'user').all()
    serializer_class = BookIssueSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['book__title', 'book__isbn', 'user__username', 'user__first_name', 'user__last_name']
    ordering_fields = ['issue_date', 'due_date', 'status']
