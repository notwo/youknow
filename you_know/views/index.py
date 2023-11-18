from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    @staticmethod
    def get(request):
        return render(request, "you_know/index.html")
