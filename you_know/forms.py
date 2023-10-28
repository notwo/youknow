from django import forms
from .models import DeleteAccountReason


class UserDeleteAccountReasonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "

    class Meta:
        model = DeleteAccountReason
        fields = ('question1', 'question2', 'question3', 'message')
