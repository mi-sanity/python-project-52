from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["executor"].queryset = User.objects.all()
        self.fields["executor"].label_from_instance = (
            lambda obj: obj.get_full_name()
        )
        self.fields["labels"].queryset = Label.objects.all()

    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Name"),
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Description"),
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-control",
                    "choices": Status,
                }
            ),
            "executor": forms.Select(
                attrs={
                    "class": "form-control",
                    "choices": User,
                }
            ),
            "labels": forms.SelectMultiple(
                attrs={
                    "class": "form-control",
                    "choices": Label,
                }
            ),
        }
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "status": _("Status"),
            "executor": _("Executor"),
            "labels": _("Labels"),
        }
