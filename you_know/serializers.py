from django.core.paginator import Paginator
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import CustomUser, Library, Category, Keyword, Tag


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "sub"]
        read_only_fields = ('id',)


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
    library_title = serializers.ReadOnlyField(source="library.title")
    category_title = serializers.ReadOnlyField(source="category.title")
    tags = TagSerializer(many=True)

    class Meta:
        model = Keyword
        fields = [
            "id", "title", "content",
            "custom_user", "custom_user_id",
            "library", "library_title",
            "category", "category_title",
            "tags",
            "created_at", "updated_at",
        ]
        read_only_fields = ('id', 'created_at')

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CategorySerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer
    library_title = serializers.ReadOnlyField(source="library.title")
    paginated_keywords = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id", "title", "content",
            "custom_user", "custom_user_id",
            "library", "library_title",
            "paginated_keywords",
            "created_at", "updated_at",
        ]
        read_only_fields = ('id', 'created_at')

    def get_paginated_keywords(self, instance):
        if instance is None:
            return {
                'prev': False,
                'next': False,
                'data': []
            }
        keywords = Keyword.objects.filter(category=instance).order_by('-created_at')
        if keywords.count() == 0:
            return {
                'prev': False,
                'next': False,
                'data': []
            }
        paginator = Paginator(keywords, 50)
        page = paginator.page(1)
        serializer = KeywordSerializer(page, many=True)
        result = {
            'prev': page.has_previous(),
            'next': page.has_next(),
            'data': serializer.data
        }
        return result


class LibrarySerializer(serializers.ModelSerializer):
    custom_user = CustomUserSerializer
    paginated_categories = serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = [
            "id", "title", "content",
            "custom_user", "custom_user_id",
            "paginated_categories",
            "created_at", "updated_at",
        ]
        read_only_fields = ('id', 'created_at')

    def get_paginated_categories(self, instance):
        if instance is None:
            return {
                'prev': False,
                'next': False,
                'data': []
            }
        categories = Category.objects.filter(library=instance).order_by('-created_at')
        if categories.count() == 0:
            return {
                'prev': False,
                'next': False,
                'data': []
            }
        paginator = Paginator(categories, 30)
        page = paginator.page(1)
        serializer = CategorySerializer(page, many=True)
        result = {
            'prev': page.has_previous(),
            'next': page.has_next(),
            'data': serializer.data
        }
        return result
