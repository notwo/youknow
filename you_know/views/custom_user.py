from rest_framework import viewsets
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

    def get_queryset(self):
        return CustomUser.objects.filter(sub=self.request.query_params.get('sub'))
