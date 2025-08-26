from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.users.forms import UserCreateForm
from task_manager.users.mixins import (
    CheckChangePermissionMixin,
    CustomLoginRequiredMixin,
    ProtectDeleteMixin,
)
from task_manager.users.models import User


class UserIndexView(ListView):
    model = User
    context_object_name = "users"
    template_name = "users/index.html"
    extra_context = {
        "title": _("Users"),
        "ID": _("ID"),
        "username": _("Username"),
        "full_name": _("Full name"),
        "created_at": _("Created at"),
        "edit": _("Edit"),
        "delete": _("Delete"),
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = "form.html"
    success_url = reverse("login")
    extra_context = {
        "title": _("Registration"),
        "submit": _("Register"),
    }
    success_message = _("User created successfully")


class UserUpdateView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserCreateForm
    template_name = "form.html"
    success_url = reverse("users")
    extra_context = {
        "title": _("Edit user"),
        "submit": _("Update"),
    }
    success_message = _("User update successfully")


class UserDeleteView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    ProtectDeleteMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    context_object_name = "user"
    template_name = "users/delete.html"
    success_url = reverse("users")
    extra_context = {
        "title": _("Remove user"),
        "submit": _("Yes, delete"),
        "confirm": _("Are you sure delete"),
    }
    success_message = _("User was successfully deleted")
