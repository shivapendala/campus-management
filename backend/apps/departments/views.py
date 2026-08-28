from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Department
from .serializers import DepartmentSerializer
from apps.students.serializers import StudentSerializer
from apps.faculty.serializers import FacultySerializer
from apps.courses.serializers import CourseSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.prefetch_related('students', 'faculty_members', 'courses').all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code', 'head_of_department', 'building_block']
    ordering_fields = ['name', 'code', 'established_year']

    @action(detail=True, methods=['get'], url_path='students')
    def students(self, request, pk=None):
        """
        Returns all enrolled students in the department.
        """
        department = self.get_object()
        students = department.students.all()
        serializer = StudentSerializer(students, many=True)
        return Response({
            'department': department.name,
            'code': department.code,
            'total_students': students.count(),
            'results': serializer.data,
        })

    @action(detail=True, methods=['get'], url_path='faculty')
    def faculty(self, request, pk=None):
        """
        Returns all faculty members in the department.
        """
        department = self.get_object()
        faculty_members = department.faculty_members.all()
        serializer = FacultySerializer(faculty_members, many=True)
        return Response({
            'department': department.name,
            'code': department.code,
            'total_faculty': faculty_members.count(),
            'results': serializer.data,
        })

    @action(detail=True, methods=['get'], url_path='courses')
    def courses(self, request, pk=None):
        """
        Returns all catalog courses offered by the department.
        """
        department = self.get_object()
        courses = department.courses.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({
            'department': department.name,
            'code': department.code,
            'total_courses': courses.count(),
            'results': serializer.data,
        })

    @action(detail=True, methods=['post'], url_path='assign-hod')
    def assign_hod(self, request, pk=None):
        """
        Assigns or updates the Head of Department (HOD).
        """
        department = self.get_object()
        hod_name = request.data.get('head_of_department')
        if not hod_name:
            return Response({'detail': 'head_of_department is required.'}, status=status.HTTP_400_BAD_REQUEST)

        department.head_of_department = hod_name
        department.save()
        return Response({
            'detail': f'{hod_name} assigned as Head of Department for {department.name}.',
            'department': department.name,
            'head_of_department': department.head_of_department,
        }, status=status.HTTP_200_OK)
