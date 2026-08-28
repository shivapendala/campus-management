from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet,
    FacultyMemberViewSet,
    StudentViewSet,
    CourseViewSet,
    EnrollmentViewSet
)

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'faculty', FacultyMemberViewSet, basename='faculty')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('', include(router.urls)),
]
