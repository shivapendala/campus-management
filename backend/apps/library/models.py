from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=25, unique=True)
    category = models.CharField(max_length=100, default='Computer Science')
    publisher = models.CharField(max_length=150, blank=True, default='')
    publication_year = models.PositiveIntegerField(default=2024)
    total_copies = models.PositiveIntegerField(default=5)
    available_copies = models.PositiveIntegerField(default=5)
    rack_number = models.CharField(max_length=30, blank=True, default='A-101')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class IssueStatus(models.TextChoices):
    ISSUED = 'ISSUED', 'Issued'
    RETURNED = 'RETURNED', 'Returned'
    OVERDUE = 'OVERDUE', 'Overdue'
    LOST = 'LOST', 'Lost'


class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='issues')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrowed_books')
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'), validators=[MinValueValidator(Decimal('0.00'))])
    status = models.CharField(max_length=20, choices=IssueStatus.choices, default=IssueStatus.ISSUED)
    remarks = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['-issue_date']
        verbose_name = 'Book Issue Record'
        verbose_name_plural = 'Book Issue Records'

    def __str__(self):
        return f"{self.book.title} issued to {self.user.username} ({self.status})"
