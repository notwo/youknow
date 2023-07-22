from django.urls import path
from you_know import views

app_name = 'you_know'
urlpatterns = [
  # 書籍
  path("", views.IndexView.as_view(), name="index"),
]
