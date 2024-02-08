from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from .models import Task


def display_tasks(request):
    tasks = Task.objects.all()
    
    if request.method == 'POST':
        if request.POST.get('title'):
            new_task = Task(
                title=request.POST.get('title'),
                assigned_user=request.user,            
            )
            new_task.save()
        return redirect('tasks:display-tasks')
    
    context = {
        'tasks': tasks,
    }
    return render(request, 'tasks/tasks.html', context)


def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {
        'task': task,
    }
    return render(request, 'tasks/task_details.html', context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks:display-tasks')
    
    form = TaskForm(instance=task)
    context = {
        'form': form,
    }
    return render(request, 'tasks/edit_task.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:display-tasks')
    
    context = {
        'task': task,
    }
    return render(request, 'tasks/delete_task.html', context)