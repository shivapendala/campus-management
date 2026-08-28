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
    """Health check and API root endpoint."""
    return Response({
        'status': 'healthy',
        'project': 'Campus Management System API',
        'version': '1.0.0',
        'endpoints': {
            'auth': '/api/auth/',
            'campus': '/api/campus/',
            'analytics': '/api/analytics/',
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root_view, name='campus-api-root'),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/campus/', include('apps.campus.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
