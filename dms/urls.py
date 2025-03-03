from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('', include('tasks.urls')),  # Подключение маршрутов из приложения tasks
]