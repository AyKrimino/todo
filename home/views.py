from django.shortcuts import render
from .forms import LoginForm, SignupForm


def index(request):
    return render(request, 'home/index.html')


def login(request):
    form = LoginForm()
    return render(request, 'home/login.html', {'form': form})


def signup(request):
    form = SignupForm()
    return render(request, 'home/signup.html', {'form': form})