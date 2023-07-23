from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
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
