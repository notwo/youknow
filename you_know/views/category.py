from django.views.generic import TemplateView


class CategoryIndexView(TemplateView):
    template_name = "you_know/category/index.html"
