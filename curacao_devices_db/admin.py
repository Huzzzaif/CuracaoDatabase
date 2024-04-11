from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.userAuth_model import User
from .models import Department, Device, Location, Transaction

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)
        }),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2', 'role', 'department')}),
    )
    list_display = ('email', 'name', 'is_staff', 'last_login', 'role', 'department')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'role', 'department')
    search_fields = ('email', 'name', 'department')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Device)
admin.site.register(Location)
admin.site.register(Transaction)
