from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class YouKnowPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('you_know:password_change_done')
    template_name = 'you_know/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "password_change"
        return context

class YouKnowPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'you_know/password_change_done.html'
