from django import forms
from django.utils.translation import gettext_lazy
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        label=gettext_lazy("Status"), queryset=Status.objects.all()
    )
    executor = ModelChoiceFilter(
        label=gettext_lazy("Executor"), queryset=User.objects.all()
    )
    labels = ModelChoiceFilter(
        label=gettext_lazy("Label"), queryset=Label.objects.all()
    )
    my_tasks = BooleanFilter(
        label=gettext_lazy("My tasks"),
        widget=forms.CheckboxInput,
        method="get_tasks",
    )

    def get_tasks(self, queryset, _, value):
        tasks = queryset.filter(author_id=self.request.user.id)
        return tasks if value else queryset

    class Meta:
        model = Task
        fields = ("status", "executor", "labels")
