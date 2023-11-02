from rest_framework import viewsets, pagination
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from ..models import Tag
from ..serializers import TagSerializer


class TagFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tag
        fields = ['title']


class TagPagination(pagination.LimitOffsetPagination):
    ordering = ('-created_at',)
    page_size = 50


class TagAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_fields = ('title', 'content', 'custom_user_id')
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_class = TagFilter
    ordering_fields = ['-created_at']
    pagination_class = TagPagination

    def get_queryset(self):
        return Tag.objects.filter(
                    custom_user=self.kwargs['you_know_customuser_pk'],
                ).order_by('-created_at')
