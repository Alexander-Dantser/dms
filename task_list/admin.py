from django.contrib import admin
from . import models
 
# Register your models here.

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in models.Task._meta.get_fields()]
    list_display = [
        "path_file",
        "status",
        "parent_task",
    ]
    
@admin.register(models.Task_Status)
class Task_StatusAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in models.Task_Status._meta.get_fields()]
    list_display = [
        "name",
    ]
