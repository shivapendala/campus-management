from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import PasswordResetToken
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserSerializer,
    UserRegisterSerializer,
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
)

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Login endpoint returning JWT tokens with user profile.
    """
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    Register a new user account in the campus management system.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer


class CurrentUserProfileView(generics.RetrieveUpdateAPIView):
    """
    Get or update the profile of currently authenticated user (/api/auth/me/ & /api/auth/profile/).
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class RoleVerificationView(APIView):
    """
    Endpoint verifying user authentication and role permissions.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'authenticated': True,
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            'is_admin': user.role in ['ADMIN', 'HOD'] or user.is_superuser,
            'is_faculty': user.role == 'FACULTY',
            'is_student': user.role == 'STUDENT',
            'is_hod': user.role == 'HOD',
            'department': user.department_name,
            'status': user.status
        })


class ForgotPasswordView(APIView):
    """
    Initiates password recovery by generating a reset token.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
            # Create a reset token
            reset_token = PasswordResetToken.objects.create(user=user)
            return Response({
                'detail': f'Password reset token generated successfully for {email}.',
                'reset_token': reset_token.token,
                'reset_code': reset_token.code,
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            # Don't expose whether user exists
            return Response({
                'detail': f'If an account with {email} exists, reset instructions have been generated.',
            }, status=status.HTTP_200_OK)


class ResetPasswordConfirmView(APIView):
    """
    Consumes reset token and sets new password.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token_str = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']

        try:
            reset_token = PasswordResetToken.objects.get(
                models.Q(token=token_str) | models.Q(code=token_str),
                is_used=False
            )
            if not reset_token.is_valid:
                return Response({'token': ['Token has expired or is invalid.']}, status=status.HTTP_400_BAD_REQUEST)

            user = reset_token.user
            user.set_password(new_password)
            user.save()

            reset_token.is_used = True
            reset_token.save()

            return Response({'detail': 'Password has been reset successfully. You can now login.'}, status=status.HTTP_200_OK)
        except PasswordResetToken.DoesNotExist:
            return Response({'token': ['Invalid reset token or code.']}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.GenericAPIView):
    """
    Change user password endpoint for authenticated users.
    """
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({'old_password': ['Incorrect old password.']}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({'detail': 'Password updated successfully.'}, status=status.HTTP_200_OK)


class UserListView(generics.ListAPIView):
    """
    List users with optional role and department filtering.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.all()
        role = self.request.query_params.get('role')
        dept = self.request.query_params.get('department')
        search = self.request.query_params.get('search')
        if role:
            queryset = queryset.filter(role=role.upper())
        if dept:
            queryset = queryset.filter(department_name__icontains=dept)
        if search:
            queryset = queryset.filter(
                models.Q(username__icontains=search) |
                models.Q(first_name__icontains=search) |
                models.Q(last_name__icontains=search) |
                models.Q(email__icontains=search)
            )
        return queryset
