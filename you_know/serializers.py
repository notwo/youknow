from rest_framework import serializers
from .models import Library


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ["title", "content"]
        read_only_fields = ('id',)
