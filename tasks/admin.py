from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_user', 'created_at', 'status')
    list_filter = ('title', 'assigned_user', 'created_at', 'status')
    search_fields = ('title', 'assigned_user', 'created_at')
    ordering = ('assigned_user', '-created_at')
