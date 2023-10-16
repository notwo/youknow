from rest_framework import viewsets
from django_filters import rest_framework as filters
from ..models import Library
from ..serializers import LibrarySerializer


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

    def get_queryset(self):
        return Library.objects.filter(custom_user=self.kwargs['you_know_customuser_pk']).order_by('-created_at')
