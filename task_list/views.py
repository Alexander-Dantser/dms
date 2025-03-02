from django.shortcuts import render
from . import forms


# Create your views here.
def new_task(request): 
    task_form = forms.TaskForm()
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            # print(task_form.cleaned_data)
            task_form.save()
            
            task_form = forms.TaskForm()

            return render(
                request,
                'task_list/task_form.html', 
                {'form_from_model': task_form,}
            )
  
    return render(
        request,                  # Запрос
        'task_list/task_form.html',  # путь к шаблону
        {'form_from_model': task_form,} 
    )