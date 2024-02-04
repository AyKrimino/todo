from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.display_tasks, name='display-tasks'),
    path('task_details/', views.task_details, name='task_details'),
]