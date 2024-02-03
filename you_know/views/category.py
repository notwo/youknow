from rest_framework import viewsets, pagination
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from ..models import Category
from ..serializers import CategorySerializer


class CategoryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['title']


class CategoryPagination(pagination.LimitOffsetPagination):
    ordering = ('-created_at',)
    page_size = 15


class CategoryAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_fields = ('title', 'content', 'custom_user_id', 'library_id')
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = CategoryFilter
    ordering_fields = ['-created_at']
    pagination_class = CategoryPagination

    def get_queryset(self):
        return Category.objects.filter(
            custom_user=self.kwargs['you_know_customuser_pk'],
            library=self.kwargs['library_pk']
        ).order_by('-created_at')
