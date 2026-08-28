from rest_framework import serializers
from .models import Event, EventRegistration
from apps.accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class EventRegistrationSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    class Meta:
        model = EventRegistration
        fields = [
            'id', 'event', 'user', 'user_id', 'user_detail',
            'registered_at', 'attendance_status', 'certificate_url'
        ]
        read_only_fields = ['id', 'registered_at']


class EventSerializer(serializers.ModelSerializer):
    organizer_detail = UserSerializer(source='organizer', read_only=True)
    organizer_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='organizer', write_only=True, required=False, allow_null=True)
    registered_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'organizer', 'organizer_id', 'organizer_detail',
            'event_type', 'venue', 'description', 'start_time', 'end_time',
            'capacity', 'registered_count', 'banner_image_url', 'is_public',
            'registration_deadline', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
