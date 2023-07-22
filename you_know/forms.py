from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class YouKnowUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class YouKnowUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
