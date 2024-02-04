from django.shortcuts import render
from .forms import TaskForm


def display_tasks(request):
    return render(request, 'tasks/tasks.html')


def task_details(request):
    return render(request, 'tasks/task_details.html')


def edit_task(request):
    context = {}
    context['form'] = TaskForm()
    return render(request, 'tasks/edit_task.html', context)