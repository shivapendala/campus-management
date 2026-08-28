from django.contrib import admin
from .models import FeeCategory, FeeStructure, FeePayment


@admin.register(FeeCategory)
class FeeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'department', 'semester', 'academic_year', 'amount', 'due_date')
    list_filter = ('category', 'department', 'academic_year', 'semester')
    search_fields = ('title', 'department__name')


@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'student', 'fee_structure', 'amount_paid', 'payment_method', 'status', 'payment_date')
    list_filter = ('status', 'payment_method', 'payment_date')
    search_fields = ('invoice_number', 'student__student_id', 'transaction_id')
