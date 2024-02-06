from django.shortcuts import render, get_object_or_404
from .forms import TaskForm
from .models import Task


def display_tasks(request):
    tasks = Task.objects.all()
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


def edit_task(request):
    form = TaskForm()
    context = {
        'form': form,
    }
    return render(request, 'tasks/edit_task.html', context)


def delete_task(request):
    return render(request, 'tasks/delete_task.html')