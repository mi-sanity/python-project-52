from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from task_manager.tasks.filter import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.mixins import AuthorRequireMixin
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskIndexView(LoginRequiredMixin, FilterView, ListView):
    model = Task
    filterset_class = TaskFilter
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    extra_context = {
        "title": _("Tasks"),
        "ID": _("ID"),
        "name": _("Name"),
        "status": _("Status"),
        "author": _("Author"),
        "executor": _("Executor"),
        "edit": _("Edit"),
        "delete": _("Delete"),
        "select": _("Select"),
        "created_at": _("Created at"),
    }
    permission_denied_message = _("Please login")


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = "form.html"
    success_url = reverse("tasks")
    extra_context = {
        "title": _("Add Task"),
        "submit": _("Create"),
    }
    success_message = _("Task created successfully")
    permission_denied_message = _("Please login")

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "form.html"
    success_url = reverse("tasks")
    extra_context = {
        "title": _("Edit task"),
        "submit": _("Update"),
    }
    success_message = _("Task updated successfully")
    permission_denied_message = _("Please login")


class TaskDeleteView(
    LoginRequiredMixin, AuthorRequireMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    template_name = "tasks/delete.html"
    context_object_name = "task"
    success_url = reverse("tasks")
    extra_context = {
        "title": _("Remove task"),
        "submit": _("Yes, delete"),
        "confirm": _("Are you sure delete"),
    }
    permission_denied_message = _("Please login")
    success_message = _("Task was successfully deleted")


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    extra_context = {
        "title": _("Task view"),
        "author": _("Author"),
        "executor": _("Executor"),
        "status": _("Status"),
        "created": _("Created"),
        "labels": _("Labels"),
        "edit": _("Edit"),
        "delete": _("Delete"),
    }
    permission_denied_message = _("Please login")
