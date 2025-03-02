from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["path_file",  "parent_task", "status",]
        labels = {
            "path_file": "Путь к файлу",
            "status": "Статус задачи",
            "parent_task": "Родительская задача",
        }

