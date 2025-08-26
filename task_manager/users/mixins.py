from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as _


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse("login")
    login_check_message = _("Please login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, self.login_check_message)
            return redirect(self.login_url)
        else:
            return super().dispatch(request, *args, **kwargs)


class ProtectDeleteMixin:
    protect_executor_message = _(
        "You cannot delete executor of the task"
    )

    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protect_executor_message)
        return redirect(self.success_url)


class CheckChangePermissionMixin(UserPassesTestMixin):
    change_another_user_message = _(
        "You have no permissions to change another user."
    )

    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, self.change_another_user_message)
        return redirect(self.success_url)
