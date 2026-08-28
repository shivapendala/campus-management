from rest_framework import serializers
from .models import Book, BookIssue
from apps.accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'isbn', 'category',
            'publisher', 'publication_year', 'total_copies',
            'available_copies', 'rack_number', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class BookIssueSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)
    book_detail = BookSerializer(source='book', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), source='book', write_only=True)

    class Meta:
        model = BookIssue
        fields = [
            'id', 'book', 'book_id', 'book_detail',
            'user', 'user_id', 'user_detail',
            'issue_date', 'due_date', 'return_date',
            'fine_amount', 'status', 'remarks'
        ]
        read_only_fields = ['id', 'issue_date']
