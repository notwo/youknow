from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
from ..forms import LibraryUpdateForm
from ..models import Library
from django.core import serializers
from ..serializers import LibrarySerializer


# これは最終的に消す
class LibraryViews(TemplateView, ModelFormMixin):
    form_class = LibraryUpdateForm
    model = Library
    template_name = "you_know/library/index.html"

    def __init__(self):
        self.object = None


class LibraryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Library
        fields = ['title']


class LibraryAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all().order_by('-created_at')
    filter_fields = ('title', 'content', 'custom_user_id')
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LibraryFilter
