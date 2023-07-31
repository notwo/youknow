from django.views.generic import UpdateView, DeleteView, TemplateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse, reverse_lazy
from ..forms import UserUpdateForm, UserDeleteAccountReasonForm
from ..models import CustomUser, DeleteAccountReason, DeleteMailToken
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import Http404


class UserUpdateView(UpdateView):
    template_name = "you_know/user_setting/profile.html"
    form_class = UserUpdateForm
    model = CustomUser

    def get_queryset(self):
        queryset = CustomUser.objects.filter(uuid=self.request.user.uuid)
        return queryset

    def get_success_url(self, **kwargs):
        return reverse("you_know:profile", kwargs={'pk': self.kwargs.get('pk')})


class UserDeleteView(DeleteView):
    template_name = "you_know/user_setting/delete_account.html"
    model = CustomUser

    def get_success_url(self, **kwargs):
        token = DeleteMailToken.create(None, self.request.user.email)
        email_template_name = 'you_know/mail_template/user_delete/message.txt'
        context = {
            'current_host': self.request._current_scheme_host,
            'token': token
        }
        subject = 'アカウント削除のお知らせ'
        send_mail(subject, render_to_string(email_template_name, context), 'info@example.com', [self.request.user.email])
        return reverse('you_know:delete_account_done')


class UserDeleteDoneView(TemplateView):
    template_name = "you_know/user_setting/delete_account_done.html"


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
        print(DeleteMailToken.objects.filter(token=token))
        DeleteMailToken.objects.filter(token=token).delete()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class UserDeleteAccountReasonDoneView(TemplateView):
    template_name = "you_know/user_setting/delete_account_reason_done.html"
