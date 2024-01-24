from django.shortcuts import render
from .forms import UserForm


def home(request):
    return render(request, 'home/index.html')


def login(request):
    form = UserForm()
    return render(request, 'home/login.html', {'form': form})