from django.views.generic import TemplateView


class LibraryIndexView(TemplateView):
    template_name = "you_know/library/index.html"
