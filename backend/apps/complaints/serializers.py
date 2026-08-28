from rest_framework import serializers
from .models import Complaint
from apps.accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ComplaintSerializer(serializers.ModelSerializer):
    submitted_by_detail = UserSerializer(source='submitted_by', read_only=True)
    assigned_to_detail = UserSerializer(source='assigned_to', read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assigned_to',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Complaint
        fields = [
            'id', 'ticket_id', 'submitted_by', 'submitted_by_detail',
            'category', 'title', 'description', 'priority', 'status',
            'assigned_to', 'assigned_to_id', 'assigned_to_detail',
            'resolution_notes', 'resolved_at', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'ticket_id', 'submitted_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['submitted_by'] = request.user
        return super().create(validated_data)
