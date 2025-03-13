from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
admin.site.register(Profile)
from .models import Profile
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):

    list_display = (
    'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login')


    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})

    )

    inlines = [ProfileInline]


    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
    )

    search_fields = ('username', 'email')
    ordering = ('username',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)