# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task, Status
from .forms import TaskForm

@csrf_exempt  # Отключаем CSRF для AJAX-запросов (можно настроить иначе)
def update_task_status_ajax(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        status_id = request.POST.get('status_id')

        try:
            task = Task.objects.get(id=task_id)
            status = Status.objects.get(id=status_id)
            task.status = status
            task.save()
            return JsonResponse({'success': True})
        except (Task.DoesNotExist, Status.DoesNotExist):
            return JsonResponse({'success': False, 'error': 'Задача или статус не найдены'})
    return JsonResponse({'success': False, 'error': 'Недопустимый метод запроса'})

def task_list(request):
    tasks = Task.objects.all()
    statuses = Status.objects.all()  # Получаем все статусы
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'statuses': statuses,  # Передаём статусы в шаблон
    })


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    # Преобразуем choices в список кортежей (значение, метка) и удаляем пустой элемент
    status_choices = [
        (str(value), label) for value, label in form.fields['status'].choices if value != ''
    ]
    return render(request, 'tasks/add_task.html', {
        'form': form,
        'status_choices': status_choices,  # Передаем список статусов без пустого элемента
    })

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    statuses = Status.objects.all()

    if request.method == 'POST':
        task.task = request.POST.get('task')
        status_id = request.POST.get('status')
        task.status = get_object_or_404(Status, id=status_id)
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {
        'task': task,
        'statuses': statuses,
    })

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        new_status_id = request.POST.get('status')
        new_status = get_object_or_404(Status, id=new_status_id)
        task.status = new_status
        task.save()
        return redirect('task_list')
    statuses = Status.objects.all()
    return render(request, 'tasks/update_status.html', {'task': task, 'statuses': statuses})
