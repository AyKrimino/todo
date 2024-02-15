from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
]