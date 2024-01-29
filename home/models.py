from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class TodoUserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password, **other_fields):
        
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, firstname=firstname, lastname=lastname, **other_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, username, firstname, lastname, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        if not other_fields.get('is_staff'):
            raise ValueError('Superuser must be assigned to is_staff=True.')
        
        if not other_fields.get('is_superuser'):
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, username, firstname, lastname, password, **other_fields)
        


class TodoUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email adress'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150, blank=True, null=True)
    lastname = models.CharField(max_length=150, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']
    
    objects = TodoUserManager()
    
    def __str__(self):
        return self.username