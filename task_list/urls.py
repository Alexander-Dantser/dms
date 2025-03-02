from django.urls import path
from . import views

urlpatterns = [
    # tasklist/  Приехало из глобального юрлз
    path('', views.new_task,name='new_task', ),
]