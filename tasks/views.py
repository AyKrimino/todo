from django.shortcuts import render


def display_tasks(request):
    return render(request, 'tasks/tasks.html')