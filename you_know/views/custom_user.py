from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from ..models import CustomUser
from ..serializers import CustomUserSerializer


class CustomUserFilter(filters.FilterSet):
    sub = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = CustomUser
        fields = ['sub']


class CustomUserAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    filter_fields = ('username', 'email', 'sub')
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CustomUserFilter

    @action(methods=['get'], detail=False)
    def username_duplicated(self, request):
        username = request.GET.get('username')
        if username is None:
            return Response({"duplicated": True})
        users = CustomUser.objects.filter(username=username)
        if len(users) == 0:
            return Response({"duplicated": False})
        else:
            return Response({"duplicated": True})
