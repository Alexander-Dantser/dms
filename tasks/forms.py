# tasks/forms.py
from django import forms
from .models import Task, Status

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'status']  # Указываем только существующие поля
        