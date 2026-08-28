from rest_framework import serializers
from .models import Company, PlacementDrive, JobApplication
from apps.students.serializers import StudentSerializer
from apps.students.models import Student


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'industry', 'contact_person', 'contact_email', 'contact_phone', 'created_at']
        read_only_fields = ['id', 'created_at']


class PlacementDriveSerializer(serializers.ModelSerializer):
    company_detail = CompanySerializer(source='company', read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company', write_only=True)
    applications_count = serializers.SerializerMethodField()

    class Meta:
        model = PlacementDrive
        fields = [
            'id', 'company', 'company_id', 'company_detail',
            'title', 'job_role', 'job_description', 'package_lpa',
            'eligibility_gpa', 'drive_date', 'application_deadline',
            'location', 'status', 'applications_count', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_applications_count(self, obj):
        return obj.applications.count()


class JobApplicationSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    drive_detail = PlacementDriveSerializer(source='drive', read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True)
    drive_id = serializers.PrimaryKeyRelatedField(queryset=PlacementDrive.objects.all(), source='drive', write_only=True)

    class Meta:
        model = JobApplication
        fields = [
            'id', 'drive', 'drive_id', 'drive_detail',
            'student', 'student_id', 'student_detail',
            'resume_url', 'status', 'offer_letter_url', 'remarks', 'applied_at'
        ]
        read_only_fields = ['id', 'applied_at']
