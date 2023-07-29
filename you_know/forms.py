from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser


class YouKnowUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class YouKnowUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
