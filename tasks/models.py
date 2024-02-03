from django.db import models
from home.models import TodoUser


class Task(models.Model):
    STATUS_CHOICES = (
        ('completed', 'completed'),
        ('not completed', 'not completed'),
    )
    
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True)
    assigned_user = models.ForeignKey(TodoUser, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default='not completed')
    
    def __str__(self):
        return self.title
