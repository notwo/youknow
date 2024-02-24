from rest_framework import viewsets, pagination
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from ..models import Keyword, Tag
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

    @action(methods=['get'], detail=False)
    def search_by_tag(self, request, **kwargs):
        sub = kwargs['you_know_customuser_pk']
        title = request.GET.get('title')
        tags = Tag.objects.filter(custom_user=sub, title__contains=title)
        if len(tags) == 0:
            return Response([])
        else:
            keywords = Keyword.objects.filter(tags__in=tags).distinct()
            serializer = self.get_serializer(instance=keywords, many=True)
            return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def search_by_content(self, request, **kwargs):
        sub = kwargs['you_know_customuser_pk']
        library_id = kwargs['library_pk']
        category_id = kwargs['category_pk']
        content = request.GET.get('content')
        keywords = Keyword.objects.filter(
            custom_user=sub,
            library_id=library_id,
            category_id=category_id,
            content__contains=content)
        serializer = self.get_serializer(instance=keywords, many=True)
        return Response(serializer.data)

    @action(methods=['patch'], detail=True)
    def move(self, request, **kwargs):
        destination_category_id = request.GET.get('move_category_id')
        data = {
            'category': destination_category_id
        }
        before = Keyword.objects.get(id=kwargs['pk'])
        serializer = self.serializer_class(instance=before, data=data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False)
    def multi_delete(self, request, **kwargs):
        ids = request.GET.get('ids')
        keywords = Keyword.objects.filter(id__in=ids.split(','))
        keywords.delete()

        return Response(keywords, status=status.HTTP_200_OK)
