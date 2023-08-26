from rest_framework import serializers
from .models import Library, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["uuid"]
        read_only_fields = ('uuid',)


class LibrarySerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer

    class Meta:
        model = Library
        fields = ["id", "title", "content", "custom_user", "custom_user_id", "created_at"]
        read_only_fields = ('id', 'created_at')
