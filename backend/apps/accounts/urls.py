from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    RegisterView,
    CurrentUserProfileView,
    RoleVerificationView,
    ForgotPasswordView,
    ResetPasswordConfirmView,
    ChangePasswordView,
    UserListView,
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='accounts_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='accounts_token_refresh'),
    path('login/', CustomTokenObtainPairView.as_view(), name='accounts_login'),
    path('register/', RegisterView.as_view(), name='accounts_register'),
    path('profile/', CurrentUserProfileView.as_view(), name='accounts_profile'),
    path('me/', CurrentUserProfileView.as_view(), name='accounts_me'),
    path('verify-role/', RoleVerificationView.as_view(), name='accounts_verify_role'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='accounts_forgot_password'),
    path('reset-password/', ResetPasswordConfirmView.as_view(), name='accounts_reset_password'),
    path('change-password/', ChangePasswordView.as_view(), name='accounts_change_password'),
    path('users/', UserListView.as_view(), name='accounts_users_list'),
]
