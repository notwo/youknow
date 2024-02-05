from rest_framework import viewsets, pagination
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from ..models import Library, Category, Keyword, Tag
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

    @action(methods=['get'], detail=False)
    def search_by_tag(self, request, **kwargs):
        sub = kwargs['you_know_customuser_pk']
        title = request.GET.get('title')
        tags = Tag.objects.filter(custom_user=sub, title__contains=title)
        if len(tags) == 0:
            return Response([])
        else:
            keywords = Keyword.objects.filter(tags__in=tags)
            categories = Category.objects.filter(keywords__in=keywords)
            libraries = Library.objects.filter(categories__in=categories).distinct()
            serializer = self.get_serializer(instance=libraries, many=True)
            return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def search_by_content(self, request, **kwargs):
        sub = kwargs['you_know_customuser_pk']
        content = request.GET.get('content')
        libraries = Library.objects.filter(custom_user=sub, content__contains=content)
        serializer = self.get_serializer(instance=libraries, many=True)
        return Response(serializer.data)
