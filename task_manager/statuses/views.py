from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.mixins import CheckTaskMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = "statuses"
    template_name = "statuses/index.html"
    extra_context = {
        "title": _("Statuses"),
        "ID": _("ID"),
        "name": _("Name"),
        "edit": _("Edit"),
        "delete": _("Delete"),
        "created_at": _("Created at"),
        "create_status": _("Create status"),
    }
    permission_denied_message = _("Please login")


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "form.html"
    success_url = reverse("statuses")
    extra_context = {
        "title": _("Create status"),
        "submit": _("Create"),
    }
    success_message = _("Status created successfully")
    permission_denied_message = _("Please login")


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = "form.html"
    success_url = reverse("statuses")
    extra_context = {
        "title": _("Update status"),
        "submit": _("Update"),
    }
    success_message = _("Status successfully changed")
    permission_denied_message = _("Please login")


class StatusDeleteView(
    CheckTaskMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView
):
    model = Status
    context_object_name = "status"
    template_name = "statuses/delete.html"
    success_url = reverse("statuses")
    extra_context = {
        "title": _("Remove status"),
        "confirm": _("Are you sure delete"),
        "submit": _("Yes, delete"),
    }
    success_message = _("Status was deleted successfully")
    permission_denied_message = _("Please login")
    protected_error_message = _("Cannot delete busy status")
