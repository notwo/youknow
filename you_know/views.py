from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
#from you_know.models import Book

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "you_know/index.html")
