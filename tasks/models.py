# tasks/models.py
from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название статуса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class Task(models.Model):
    task = models.TextField(blank=True, verbose_name="Задача")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"