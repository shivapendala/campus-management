from rest_framework import serializers
from .models import Notification
from apps.accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class NotificationSerializer(serializers.ModelSerializer):
    recipient_detail = UserSerializer(source='recipient', read_only=True)
    recipient_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='recipient', write_only=True, required=False)

    class Meta:
        model = Notification
        fields = [
            'id', 'recipient', 'recipient_id', 'recipient_detail',
            'title', 'message', 'notification_type', 'is_read',
            'link_url', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
