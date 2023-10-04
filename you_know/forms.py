from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from .models import CustomUser, DeleteAccountReason, Library, Category


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
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class UserDeleteAccountReasonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    class Meta:
        model = DeleteAccountReason
        fields = ('question1', 'question2', 'question3', 'message')


class LibraryUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    class Meta:
        model = Library
        fields = ('title', 'content')
        labels = {
            'title': 'ライブラリ名',
            'content': '内容'
        }


class CategoryUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    class Meta:
        model = Category
        fields = ('title', 'content')
        labels = {
            'title': 'カテゴリ名',
            'content': '内容'
        }
