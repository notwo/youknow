from rest_framework import serializers
from .models import Library, Category, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id"]
        read_only_fields = ('id',)


class LibrarySerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer

    class Meta:
        model = Library
        fields = ["id", "title", "content", "custom_user", "custom_user_id", "created_at", "updated_at"]
        read_only_fields = ('id', 'created_at')


class CategorySerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer
    library = Library

    class Meta:
        model = Category
        fields = ["id", "title", "content", "custom_user", "custom_user_id", "library", "library_id", "created_at", "updated_at"]
        read_only_fields = ('id', 'created_at')
