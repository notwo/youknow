from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import CustomUser, Library, Category, Keyword, Tag


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "sub"]
        read_only_fields = ('id',)


class LibrarySerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer

    class Meta:
        model = Library
        fields = [
            "id", "title", "content",
            "custom_user", "custom_user_id",
            "created_at", "updated_at",
        ]
        read_only_fields = ('id', 'created_at')


class CategorySerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer
    library = Library

    class Meta:
        model = Category
        fields = [
            "id", "title", "content",
            "custom_user", "custom_user_id",
            "library", "library_id",
            "created_at", "updated_at",
        ]
        read_only_fields = ('id', 'created_at')


class TagSerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer

    class Meta:
        model = Tag
        fields = [
            "id", "title", "content",
            "custom_user", "custom_user_id",
            "created_at", "updated_at",
        ]
        read_only_fields = ('id', 'created_at')


class KeywordSerializer(WritableNestedModelSerializer):
    custom_user = CustomUserSerializer
    library = Library
    category = Category
    tags = TagSerializer(many=True)

    class Meta:
        model = Keyword
        fields = [
            "id", "title", "content",
            "custom_user", "custom_user_id",
            "library", "library_id",
            "category", "category_id",
            "created_at", "updated_at",
            "tags",
        ]
        read_only_fields = ('id', 'created_at')
