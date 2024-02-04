from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('title', 'description', 'status')
        
        labels = {
            'title': '',
            'description': '',
            'status': 'Did you complete this task?',
        }
        
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'border-2 border-gray-300 rounded py-2 w-full placeholder:text-sm px-4',
                    'placeholder': 'Task title',
                }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'border-2 border-gray-300 rounded py-2 w-full placeholder:text-sm px-4 mt-2',
                    'placeholder': 'Task description',
                    'rows': 5,
                    'cols': 33,
                }    
            ),
            'status': forms.RadioSelect(
                attrs={
                    'class': 'h-4 w-4 text-indigo-600 focus:ring-indigo-500 cursor-pointer border-gray-300 inline',
                }
            ),
        }
        
        error_messages = {
            'title': {
                'required': 'Please Enter a task title',
                'invalid': 'this is an invalid task title'
            }
        }