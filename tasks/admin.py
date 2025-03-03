from django.contrib import admin
from .models import Task, Status
from django.utils import timezone
from django.contrib.admin import DateFieldListFilter

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Отображаем только поле name
    search_fields = ('name__icontains',)  # Добавляем поиск по названию статуса

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'status', 'formatted_created_at')
    list_display_links = ('task', 'status', 'formatted_created_at',)  # Делаем колонку с датой кликабельной
    list_filter = (
        'status',
        ('created_at', DateFieldListFilter),  # Фильтр по дате
    )
    search_fields = ('task__icontains', 'status__name__icontains')
    list_per_page = 20

    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M:%S')
    formatted_created_at.short_description = 'Дата создания'
    formatted_created_at.admin_order_field = 'created_at'