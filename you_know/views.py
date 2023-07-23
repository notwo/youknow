from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from .forms import YouKnowUserCreationForm, LoginForm


class IndexView(TemplateView):
    template_name = "you_know/index.html"


class SignupView(CreateView):
    form_class = YouKnowUserCreationForm
    template_name = "you_know/signup.html"
    success_url = reverse_lazy("you_know:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return response


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "you_know/login.html"


class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("you_know:index")
