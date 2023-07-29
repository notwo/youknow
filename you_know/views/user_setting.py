from django.views.generic import UpdateView
from django.urls import reverse
from ..forms import UserUpdateForm
from ..models import CustomUser


class UserUpdateView(UpdateView):
    template_name = "you_know/user_setting.html"
    form_class = UserUpdateForm
    model = CustomUser

    def get_queryset(self):
        queryset = CustomUser.objects.filter(uuid=self.request.user.uuid)
        return queryset

    def get_success_url(self, **kwargs):
        return reverse("you_know:user_setting", kwargs={'pk': self.kwargs.get('pk')})
