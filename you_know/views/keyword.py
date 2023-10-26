from rest_framework import viewsets, pagination
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from ..models import Keyword
from ..serializers import KeywordSerializer


class KeywordFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Keyword
        fields = ['title']


class KeywordPagination(pagination.LimitOffsetPagination):
    ordering = ('-created_at',)
    page_size = 15


class KeywordAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = KeywordSerializer
    queryset = Keyword.objects.all()
    filter_fields = ('title', 'content', 'custom_user_id', 'library_id', 'category_id')
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = KeywordFilter
    ordering_fields = ['-created_at']
    pagination_class = KeywordPagination

    def get_queryset(self):
        return Keyword.objects.filter(
                    custom_user=self.kwargs['you_know_customuser_pk'],
                    category=self.kwargs['category_pk'],
                    library=self.kwargs['library_pk']
                ).order_by('-created_at')
