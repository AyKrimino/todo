from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.display_tasks, name='display-tasks'),
    path('task_details/<int:task_id>/', views.task_details, name='task-details'),
    path('edit/', views.edit_task, name='edit-task'),
    path('delete/', views.delete_task, name='delete-task'),
]