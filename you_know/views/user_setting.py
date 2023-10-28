from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy
from ..forms import UserDeleteAccountReasonForm
from ..models import DeleteAccountReason, DeleteMailToken
from django.http import Http404


class UserDeleteAccountReasonView(TemplateView, ModelFormMixin):
    form_class = UserDeleteAccountReasonForm
    model = DeleteAccountReason
    template_name = "you_know/user_setting/delete_account_reason.html"
    success_url = reverse_lazy("you_know:delete_account_reason_done")

    def __init__(self):
        self.object = None

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        if not token:
            raise Http404

        db_token = DeleteMailToken.objects.filter(token=token)
        if not db_token:
            raise Http404

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        token = kwargs.get('token')
        DeleteMailToken.objects.filter(token=token).delete()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserDeleteAccountReasonDoneView(TemplateView):
    template_name = "you_know/user_setting/delete_account_reason_done.html"
