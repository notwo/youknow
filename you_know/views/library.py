from rest_framework import viewsets, pagination
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from ..models import Library
from ..serializers import LibrarySerializer


class LibraryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Library
        fields = ['title']


class LibraryPagination(pagination.LimitOffsetPagination):
    ordering = ('-created_at',)
    page_size = 15


class LibraryAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    filter_fields = ('title', 'content', 'custom_user_id')
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = LibraryFilter
    ordering_fields = ['-created_at']
    pagination_class = LibraryPagination

    def get_queryset(self):
        return Library.objects.filter(
                    custom_user=self.kwargs['you_know_customuser_pk']
                ).order_by('-created_at')
