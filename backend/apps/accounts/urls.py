from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    RegisterView,
    CurrentUserProfileView,
    UserListView,
    ChangePasswordView,
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='accounts_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='accounts_token_refresh'),
    path('login/', CustomTokenObtainPairView.as_view(), name='accounts_login'),
    path('register/', RegisterView.as_view(), name='accounts_register'),
    path('profile/', CurrentUserProfileView.as_view(), name='accounts_profile'),
    path('users/', UserListView.as_view(), name='accounts_users_list'),
    path('change-password/', ChangePasswordView.as_view(), name='accounts_change_password'),
]
