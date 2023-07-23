from django.urls import path
from you_know import views

app_name = 'you_know'
urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path('signup/', views.SignupView.as_view(), name="signup"),
  path('login/', views.LoginView.as_view(), name="login"),
  path('logout/', views.LogoutView.as_view(), name="logout"),
  path('password_change/', views.YouKnowPasswordChangeView.as_view(), name='password_change'),
  path('password_change/done/', views.YouKnowPasswordChangeDoneView.as_view(), name='password_change_done'),
]
