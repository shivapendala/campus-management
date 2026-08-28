import pytest
from datetime import date
from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from apps.fees.models import FeeCategory, FeeStructure, FeePayment, PaymentStatus, PaymentMethod
from apps.students.models import Student


@pytest.mark.django_db
class TestFeesCompleteFlow:
    def test_fee_structure_and_payment_reconciliation(self, auth_client, admin_user, sample_department):
        student = Student.objects.create(
            user=admin_user, student_id='STU-FEE-001', name='Fee Student', email='fee_stu@campus.edu', department=sample_department, year=2, section='A'
        )

        cat = FeeCategory.objects.create(name='Tuition Fee')
        structure = FeeStructure.objects.create(
            title='Fall 2026 Tuition',
            category=cat,
            department=sample_department,
            semester=4,
            amount=Decimal('4500.00'),
            due_date=date.today(),
        )

        payment = FeePayment.objects.create(
            student=student,
            fee_structure=structure,
            amount_paid=Decimal('4500.00'),
            payment_method=PaymentMethod.ONLINE,
            transaction_id='TXN-TEST-982347',
            status=PaymentStatus.SUCCESS,
        )
        assert payment.amount_paid == Decimal('4500.00')

        url = reverse('fee-payment-financial-summary')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
        assert 'total_fees' in res.data
