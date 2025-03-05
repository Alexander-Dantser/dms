from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/update-status/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('tasks/update-status-ajax/', views.update_task_status_ajax, name='update_task_status_ajax'),
    # добавляем URL для получения списка задач в формате JSON
    path('get-tasks-json/', views.get_tasks_json, name='get_tasks_json'),
]