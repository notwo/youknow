from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "you_know/index.html"
