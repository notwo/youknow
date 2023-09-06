from rest_framework import viewsets
from ..models import CustomUser
from ..serializers import CustomUserSerializer


# この部分は仮置きのため後で削除予定
class CustomUserAjaxViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomUserSerializer
    filter_fields = 'uuid'
    queryset = CustomUser.objects.all()

    def get_queryset(self, *args, **kwargs):
        username = self.request.query_params.get('username')
        queryset = CustomUser.objects.filter(username=username)
        return queryset
