from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, PlacementDriveViewSet, JobApplicationViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='placement-company')
router.register(r'drives', PlacementDriveViewSet, basename='placement-drive')
router.register(r'applications', JobApplicationViewSet, basename='placement-application')

urlpatterns = [
    path('', include(router.urls)),
]
