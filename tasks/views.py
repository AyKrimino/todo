from django.shortcuts import render


def display_tasks(request):
    return render(request, 'tasks/tasks.html')


def task_details(request):
    return render(request, 'tasks/task_details.html')