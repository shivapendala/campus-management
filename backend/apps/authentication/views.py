from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserSerializer,
    UserRegisterSerializer
)

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Login endpoint taking username/password and returning JWT access & refresh tokens with user info.
    """
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    Register a new user account (student/faculty/staff).
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer


class CurrentUserProfileView(generics.RetrieveUpdateAPIView):
    """
    Get or update the currently authenticated user's profile.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    """
    List campus users (filtered by role optional).
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.all()
        role = self.request.query_params.get('role')
        department = self.request.query_params.get('department')
        if role:
            queryset = queryset.filter(role=role.upper())
        if department:
            queryset = queryset.filter(department_name__icontains=department)
        return queryset
