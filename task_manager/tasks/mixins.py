from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as _


class AuthorRequireMixin(UserPassesTestMixin):
    author_require_message = _("Only author has permission")
    redirect_url = reverse("tasks")

    def test_func(self):
        return self.get_object().author.id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, self.author_require_message)
        return redirect(self.redirect_url)
