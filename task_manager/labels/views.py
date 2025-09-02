from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.forms import LabelForm
from task_manager.labels.mixins import CheckTaskMixin
from task_manager.labels.models import Label


class IndexLabelView(LoginRequiredMixin, ListView):
    template_name = "labels/index.html"
    model = Label
    context_object_name = "labels"
    extra_context = {
        "title": _("Labels"),
        "ID": _("ID"),
        "name": _("Name"),
        "edit": _("Edit"),
        "delete": _("Delete"),
        "created_at": _("Created at"),
        "submit": _("Create label"),
    }
    permission_denied_message = _("Please login")


class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = "form.html"
    success_url = reverse("labels")
    extra_context = {
        "title": _("Create label"),
        "submit": _("Create"),
    }
    success_message = _("Label has been created successfully")


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "form.html"
    success_url = reverse("labels")
    extra_context = {
        "title": _("Update label"),
        "submit": _("Update"),
    }
    success_message = _("Label has been edited successfully")


class DeleteLabelView(
    LoginRequiredMixin, SuccessMessageMixin, CheckTaskMixin, DeleteView
):
    model = Label
    context_object_name = "label"
    template_name = "labels/delete.html"
    success_url = reverse("labels")
    extra_context = {
        "title": _("Delete label"),
        "submit": _("Yes, delete"),
        "confirm": _("Are you sure delete"),
    }
    success_message = _("Label was successfully deleted")
    protected_error_message = _(
        "You cannot delete a label which is currently being used"
    )
