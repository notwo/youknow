from rest_framework import viewsets
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
from ..forms import LibraryUpdateForm
from ..models import Library
from ..serializers import LibrarySerializer


# これは最終的に消す
class LibraryViews(TemplateView, ModelFormMixin):
    form_class = LibraryUpdateForm
    model = Library
    template_name = "you_know/library/index.html"

    def __init__(self):
        self.object = None


class LibraryAjaxViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all().order_by('-created_at')
    filter_fields = ('title', 'content', 'custom_user_id')
