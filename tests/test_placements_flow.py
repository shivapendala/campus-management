import pytest
from datetime import date, timedelta
from decimal import Decimal
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from apps.placements.models import Company, PlacementDrive, JobApplication
from apps.students.models import Student


@pytest.mark.django_db
class TestPlacementsCompleteFlow:
    def test_placement_drive_and_application_lifecycle(self, auth_client, admin_user, sample_department):
        student = Student.objects.create(
            user=admin_user, student_id='STU-TPO-001', name='Placement Candidate', email='place_stu@campus.edu', department=sample_department, year=4, section='A'
        )

        company = Company.objects.create(
            name='Google Cloud',
            industry='Cloud Computing & AI',
            website='https://cloud.google.com',
        )

        drive = PlacementDrive.objects.create(
            company=company,
            title='Google Cloud Campus Drive 2026',
            job_role='Associate Cloud Solutions Engineer',
            package_lpa=Decimal('24.50'),
            eligibility_gpa=Decimal('3.50'),
            drive_date=date.today() + timedelta(days=30),
            application_deadline=timezone.now() + timedelta(days=15),
        )
        assert drive.package_lpa == Decimal('24.50')

        app = JobApplication.objects.create(
            drive=drive,
            student=student,
            resume_url='https://linkedin.com/in/placement-test',
            status='SHORTLISTED',
        )
        assert app.status == 'SHORTLISTED'

        url = reverse('placement-drive-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
