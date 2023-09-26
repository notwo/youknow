from rest_framework import viewsets
from django_filters import rest_framework as filters
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
from ..forms import CategoryUpdateForm
from ..models import Category
from django.core import serializers
from ..serializers import CategorySerializer


# これは最終的に消す
class CategoryViews(TemplateView, ModelFormMixin):
    form_class = CategoryUpdateForm
    model = Category
    template_name = "you_know/category/index.html"

    def __init__(self):
        self.object = None


class CategoryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['title']


class CategoryAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-created_at')
    filter_fields = ('title', 'content', 'custom_user_id', 'library_id')
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CategoryFilter
