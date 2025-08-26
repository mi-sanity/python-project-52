from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {
        "title": _("Task manager"),
    }


class LoginView(LoginView):
    template_name = "form.html"
    reverse_page = reverse("home")
    extra_context = {
        "title": _("Login"),
        "submit": _("Enter"),
    }

    def form_valid(self, form):
        messages.info(self.request, _("Login successfully"))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("Login Error"))
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    reverse_page = reverse("home")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("Logged out successfully"))
        return super().dispatch(request, *args, **kwargs)
