from django.views.generic import TemplateView


class LibraryViews(TemplateView):
    template_name = "you_know/library/index.html"
