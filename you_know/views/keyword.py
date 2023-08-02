from django.views.generic import TemplateView


class KeywordIndexView(TemplateView):
    template_name = "you_know/keyword/index.html"
