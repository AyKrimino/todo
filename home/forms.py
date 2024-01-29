from django import forms
from .models import TodoUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = TodoUser
        fields = ('email', 'password')
        

class SignupForm(forms.ModelForm):
    class Meta:
        model = TodoUser
        fields = ('username', 'firstname', 'lastname', 'email', 'password', 'password')