from decimal import Decimal
import uuid
from django.db import models
from django.core.validators import MinValueValidator
from apps.departments.models import Department
from apps.students.models import Student


class FeeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Fee Category'
        verbose_name_plural = 'Fee Categories'

    def __str__(self):
        return self.name


class FeeStructure(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE, related_name='structures')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='fee_structures')
    semester = models.PositiveIntegerField(default=1)
    academic_year = models.CharField(max_length=20, default='2026-2027')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-academic_year', 'semester']
        verbose_name = 'Fee Structure'
        verbose_name_plural = 'Fee Structures'

    def __str__(self):
        return f"{self.title} ({self.department.code} Sem {self.semester}): ${self.amount}"


class PaymentStatus(models.TextChoices):
    SUCCESS = 'SUCCESS', 'Payment Success'
    PENDING = 'PENDING', 'Pending Verification'
    FAILED = 'FAILED', 'Failed'
    REFUNDED = 'REFUNDED', 'Refunded'


class PaymentMethod(models.TextChoices):
    ONLINE = 'ONLINE', 'Online Gateway'
    UPI = 'UPI', 'UPI Payment'
    CREDIT_CARD = 'CREDIT_CARD', 'Credit Card'
    DEBIT_CARD = 'DEBIT_CARD', 'Debit Card'
    NET_BANKING = 'NET_BANKING', 'Net Banking'
    CASH = 'CASH', 'Cash'
    CHEQUE = 'CHEQUE', 'Cheque / DD'


class FeePayment(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fee_payments')
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    payment_method = models.CharField(max_length=30, choices=PaymentMethod.choices, default=PaymentMethod.ONLINE)
    transaction_id = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.SUCCESS)
    payment_date = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['-payment_date']
        verbose_name = 'Fee Payment'
        verbose_name_plural = 'Fee Payments'

    def __str__(self):
        return f"Inv #{self.invoice_number} - {self.student.student_id} (${self.amount_paid})"
