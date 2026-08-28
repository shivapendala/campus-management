"""
URL Configuration for Campus Management System project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root_view(request):
    """Health check and API root endpoint listing all 15 active modules."""
    return Response({
        'status': 'healthy',
        'project': 'Campus Management System API (15 Independent Modules)',
        'version': '2.0.0',
        'modules': {
            'accounts': '/api/accounts/',
            'students': '/api/students/',
            'faculty': '/api/faculty/',
            'departments': '/api/departments/',
            'courses': '/api/courses/',
            'attendance': '/api/attendance/',
            'examinations': '/api/examinations/',
            'fees': '/api/fees/',
            'assignments': '/api/assignments/',
            'library': '/api/library/',
            'placements': '/api/placements/',
            'complaints': '/api/complaints/',
            'events': '/api/events/',
            'notifications': '/api/notifications/',
            'reports': '/api/reports/',
            'auth': '/api/auth/',
            'admin': '/admin/',
        }
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root_view, name='campus-api-root'),
    
    # 15 Independent Module Routes
    path('api/auth/', include('apps.accounts.urls')),
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/departments/', include('apps.departments.urls')),
    path('api/faculty/', include('apps.faculty.urls')),
    path('api/students/', include('apps.students.urls')),
    path('api/courses/', include('apps.courses.urls')),
    path('api/attendance/', include('apps.attendance.urls')),
    path('api/examinations/', include('apps.examinations.urls')),
    path('api/fees/', include('apps.fees.urls')),
    path('api/assignments/', include('apps.assignments.urls')),
    path('api/library/', include('apps.library.urls')),
    path('api/placements/', include('apps.placements.urls')),
    path('api/complaints/', include('apps.complaints.urls')),
    path('api/events/', include('apps.events.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path('api/reports/', include('apps.reports.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
