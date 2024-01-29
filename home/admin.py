from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TodoUser


class TodoUserAdmin(UserAdmin):
    ordering = ('-date_joined', )
    list_display = ('email', 'username', 'firstname', 'lastname', 'is_active', 'is_staff')
    search_fields = ('email', 'username', 'firstname', 'lastname')
    list_filter = ('email', 'username', 'firstname', 'lastname', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'firstname', 'lastname')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'username', 'firstname', 'lastname', 'password1', 'password2', 'is_active', 'is_staff', )
        }
        ),
    )


admin.site.register(TodoUser, TodoUserAdmin)