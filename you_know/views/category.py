from rest_framework import viewsets, pagination
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from ..models import Category, Keyword, Tag
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

    @action(methods=['get'], detail=False)
    def search_by_tag(self, request, **kwargs):
        sub = kwargs['you_know_customuser_pk']
        title = request.GET.get('title')
        tags = Tag.objects.filter(custom_user=sub, title__contains=title)
        if len(tags) == 0:
            return Response([])
        else:
            keywords = Keyword.objects.filter(tags__in=tags)
            categories = Category.objects.filter(keywords__in=keywords).distinct()
            serializer = self.get_serializer(instance=categories, many=True)
            return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def search_by_content(self, request, **kwargs):
        sub = kwargs['you_know_customuser_pk']
        library_id = kwargs['library_pk']
        content = request.GET.get('content')
        categories = Category.objects.filter(custom_user=sub, library_id=library_id, content__contains=content)
        serializer = self.get_serializer(instance=categories, many=True)
        return Response(serializer.data)

    @action(methods=['delete'], detail=False)
    def multi_delete(self, request, **kwargs):
        ids = request.GET.get('ids')
        categories = Category.objects.filter(id__in=ids.split(','))
        categories.delete()

        return Response(categories, status=status.HTTP_200_OK)
